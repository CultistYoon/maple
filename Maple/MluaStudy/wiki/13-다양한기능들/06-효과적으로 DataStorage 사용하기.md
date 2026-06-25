# 효과적으로 DataStorage 사용하기

<!-- 출처: reference/TaskWiki.md · 문서 #197 -->


학습 과정 소개
DataStorage는 간단하게 데이터를 저장하고 불러올 수 있습니다. 그러나 DataStorage를 사용하며 다양한 문제가 발생할 수 있습니다. 이번 가이드에서는 권장하는 DataStorage 사용 방법 중 일부를 소개합니다. 크리에이터가 만드는 월드 특성에 따라 알맞은 해결 방법이 필요합니다.

DataStorage 에러 코드 처리
다양한 이유로 인해 데이터를 DataStorage로부터 불러오지 못하는 상황이 발생할 수 있습니다. 예를 들어 요청에 시간이 너무 오래 걸려 실패하거나(TimedOut), 호출 횟수 한도를 초과해서(ResourceExhausted) 실패할 수 있습니다. 요청 함수의 결과 에러 코드를 이용해 데이터를 정상적으로 불러오지 못한 상황에서 발생할 수 있는 문제들을 대비하며 기능을 구현하는 것이 좋습니다. 에러 코드는 DataStorage 활용하기에서 확인할 수 있습니다.

아래의 그림과 같이 Currency 데이터를 불러오는 데 실패한 상황을 생각해 봅시다. 이 상황에서 변경된 Currency 데이터를 저장한다면 이전부터 쌓아온 유저의 Currency 데이터가 사라지는 상황이 발생할 수 있습니다.

1

유저 추방하기
다른 유저들은 정상적으로 입장해 데이터를 불러오지만 특정 유저는 여러 이유로 인해 데이터를 불러오지 못할 수 있습니다. 예를 들어 월드 플레이에 필수적인 데이터나 초기 유저 데이터를 불러오는 데 실패한 경우 유저 추방 방법을 사용할 수 있습니다. 유저가 월드 입장하더라도 정상적으로 플레이할 수 없거나, 이후의 처리가 매우 복잡해질 것이기 때문입니다.
다음은 유저 입장 시 meso 데이터 불러오기에 실패하면 유처를 추방하는 예제입니다.

Property:
[Sync]
integer meso = 0
 
Method:
[server only]
void OnBeginPlay()
{
    if self:LoadMesoData() == false then
        _UserService:KickUser(self.Entity.PlayerComponent.UserId, KickReason.WorldError) -- 유저 내보내기
        return
    end
}

[server only]
boolean LoadMesoData()
{
    local userDataStorage = _DataStorageService:GetUserDataStorage(self.Entity.PlayerComponent.UserId)
    if userDataStorage == nil then
        return false
    end

    local errorCode, mesoString = userDataStorage:GetAndWait("Meso")
    if errorCode ~= 0 then
        return false
    end

    if _UtilLogic:IsNilorEmptyString(mesoString) == false then
        self.meso = math.tointeger(tonumber(mesoString))
    end

    return true
}
더 알아보기
데이터를 불러오지 못한 원인에 따라 유저는 재접속 시 데이터 불러오기에 성공할 수도 있고, 재입장에 실패할 수도 있습니다.

재시도하기
크리에이터는 정상적으로 요청했지만 원인이 불명확한 일시 장애가 발생해 데이터 불러오기를 실패할 수 있습니다. 이런 상황을 대비해 데이터 불러오기 요청을 여러 번 시도할 수 있습니다.

아래 예시 코드는 데이터 불러오기에 실패하면 2초 뒤에 재시도합니다.
그 이후 일정 횟수 이상 실패하면 유저를 월드에서 추방합니다. 더불어 과도한 요청으로 인한 에러 코드 ResourceExhausted: 1000005가 발생하면, 재시도하지 않고 유저를 추방합니다.

Property:
[Sync]
integer meso = 0
[Sync]
boolean initialized = false
 
Method:
[server only]
void OnBeginPlay()
{
    local retryCount = 2    -- 2번 재시도하게 설정. 총 3번 저장 시도.

    while retryCount >= 0 do
        if self:LoadMesoData() == true then
            break
        end
    
        wait(1) -- 입력한 수만큼 기다렸다 다시 시도한다.
        retryCount = retryCount - 1
    end

    if self.initialized == false then
        _UserService:KickUser(self.Entity.PlayerComponent.UserId, KickReason.WorldError)    -- 유저 내보내기
        return
    end
}
 
[server only]
boolean LoadMesoData()
{
        local userDataStorage = _DataStorageService:GetUserDataStorage(self.Entity.PlayerComponent.UserId)
        if userDataStorage == nil then
            return false
        end
         
        local errorCode, mesoString = userDataStorage:GetAndWait("Meso")
        if errorCode == 0 then
            self.meso = math.tointeger(tonumber(mesoString))
            self.initialized = true
            return true
        elseif errorCode == 1000005 then
            return true -- ResourceExhausted: 호출 횟수가 한도를 초과해 에러 발생. 재시도하지 않는다.
        end
 
        return false
}
데이터 저장하지 않기
월드에 필수적인 데이터가 아닌 경우 데이터를 불러오는 데 실패했다면 데이터를 저장하지 않는 방식도 고려할 수 있습니다.

2

아래의 예제는 Component에서 요청 성공 여부를 Property에 저장하고, Logic을 이용해 데이터를 저장하지 않도록 구현합니다.

Property:
[Sync]
boolean initialized = false -- 이 프로퍼티를 사용해 저장 막기.
[Sync]
integer meso = 0
 
Method:
[server only]
void OnBeginPlay()
{
    if self:LoadMesoData() == false then
        return
    end

    self.initialized = true
}

[server only]
boolean LoadMesoData()
{
    local userDataStorage = _DataStorageService:GetUserDataStorage(self.Entity.PlayerComponent.UserId)
    if userDataStorage == nil then
        return false
    end
        
    local errorCode, mesoString = userDataStorage:GetAndWait("Meso")
    if errorCode ~= 0 then
        return false
    end

    if _UtilLogic:IsNilorEmptyString(mesoString) == false then
        self.meso = math.tointeger(tonumber(mesoString))
    end

    return true
}

[server only]
void SaveMesoData()
{
		local userDataStorage = _DataStorageService:GetUserDataStorage(self.Entity.PlayerComponent.UserId)
		if userDataStorage == nil then
			return
		end
		
       -- self.initialized가 false일 경우 관련 데이터에 접근하지 않는 처리가 필요합니다.
		if self.initialized == false then
			log("info is not initialized") -- Load 실패 시 Save 안 함.
			return
		end
		
		local mesoString = tostring(self.meso)
		userDataStorage:SetAndWait("Meso", mesoString)
}

Event Handler:
[server only] [service UserService]
HandleUserLeaveEvent(UserLeaveEvent event)
{
    self:SaveMesoData()
}
연관된 데이터들 중 일부를 불러오지 못했을 때
크리에이터는 월드를 만들 때 일반적으로 다수의 Key를 사용해 데이터를 저장합니다. 이렇게 저장한 데이터끼리 연관이 있다면 관련 기능 차단 또는 데이터 저장 차단을 고려해야 합니다. 연관된 데이터 중 하나를 저장하지 못하면 문제가 발생할 수 있습니다.

아래 그림은 연관된 두 값 중 하나의 데이터를 정상적으로 불러오지 못했을 때의 상황입니다.
Item 데이터 값을 DataStorage로부터 불러오지 못해서 서버에 Item 1, 2, 3 없습니다. 불러온 데이터가 없기 때문에 Item 4를 유저가 구매했더라도 정상적으로 저장을 하면 안 됩니다. 이전에 쌓은 Item 데이터 1, 2, 3은 사라지고 4만 저장될 수 있기 때문입니다.
반면 Currency 데이터는 다른 key를 사용하고 있으므로 300이 100으로 줄어들었습니다.
서버는 Item 데이터 저장은 실패하고, Currency 데이터는 저장에 성공했으므로 유저는 자신이 돈을 썼지만 구매한 아이템은 없는 상황이 발생합니다.

3

이처럼 서로 연관된 데이터들 중 하나의 데이터 불러오기에 실패한다면, 모두 값을 저장하지 않게 데이터 저장을 차단하게 만드는 것을 권장합니다. 연관된 모든 데이터 불러오기 성공 여부를 확인한 뒤, 아이템 구매 기능을 허용하고 저장하는 것이 좋습니다.

4

다음은 Cash, Item 데이터 불러오기에 성공한 경우에만 저장을 허용하는 예제입니다.

Property:
[Sync]
boolean initialized = false
[Sync]
integer meso = 0
[Sync]
integer cash = 0
[None]
table items = {}    -- ItemIDs
 
Method:
[server only]
void OnBeginPlay()
{
    self:LoadData()
}

[server only]
void LoadData()
{
    local userDataStorage = _DataStorageService:GetUserDataStorage(self.Entity.PlayerComponent.UserId)
    if userDataStorage == nil then
        return
    end

    if self:LoadCurrency() == false then
        return
    end

    if self:LoadItems() == false then
        return
    end

    local itemInitialitedEvent = OnUserDataItemInitialized()
    for i, id in pairs(self.items) do
        table.insert(itemInitialitedEvent.items, id)
    end

    self:SendItemInitializedEventToClient(itemInitialitedEvent)  -- 이벤트를 이용해 Client에 items 동기화.
    self.initialized = true  -- Currency와 Items 모두 Load 성공.
}

[server only]
boolean LoadCurrency()
{
    local userDataStorage = _DataStorageService:GetUserDataStorage(self.Entity.PlayerComponent.UserId)
    if userDataStorage == nil then
        return false
    end

    local errorCode, currencyString = userDataStorage:GetAndWait("Currency")
    if errorCode ~= 0 then
        return false
    end

    if _UtilLogic:IsNilorEmptyString(currencyString) == false then
        local currency = _HttpService:JSONDecode(currencyString)
    
        if currency.meso ~= nil then
            self.meso = currency.meso
        end
    
        if currency.cash ~= nil then
            self.cash = currency.cash
        end
    end

    return true
}

[server only]
boolean LoadItems()
{
    local userDataStorage = _DataStorageService:GetUserDataStorage(self.Entity.PlayerComponent.UserId)
    if userDataStorage == nil then
        return false
    end

    local errorCode, itemString = userDataStorage:GetAndWait("Items")
    if errorCode ~= 0 then
        return false
    end

    if _UtilLogic:IsNilorEmptyString(itemString) == false then
        self.items = _HttpService:JSONDecode(itemString)
    end
        
    return true
} 
 
[client]
void SendItemInitializedEventToClient(OnUserDataItemInitialized event)
{
    self.Entity:SendEvent(event)
}

[server only]
string GetCurrencyString()
{
    local currency = {}
    currency.meso = self.meso
    currency.cash = self.cash
        
    return _HttpService:JSONEncode(currency)  -- property들을 하나의 table에 합친 뒤 Json String으로 변환하여 저장.
}

[server only]
string GetItemsString()
{
    return _HttpService:JSONEncode(self.items)  -- table을 Json String으로 저장.
}

[server only]
void SaveData()
{
    if self.initialized == false then
        log("info is not initialized") -- Load 실패 시 저장하지 않음.
        return
    end
    
    local userDataStorage = _DataStorageService:GetUserDataStorage(self.Entity.PlayerComponent.UserId)
    if userDataStorage == nil then
        return
    end
    
    local currencyString = self:GetCurrencyString()
    local itemsString = self:GetItemsString()
    
    local errorCode = userDataStorage:SetAndWait("Items", itemsString)
    if errorCode ~= 0 then
        log("ErrorCode : "..errorCode)
    end
        
    errorCode = userDataStorage:SetAndWait("Currency", currencyString)
    if errorCode ~= 0 then
        log("ErrorCode : "..errorCode)
    end
}

Event Handler:
[client only] [self]
HandleOnUserDataItemInitialized (OnUserDataItemInitialized event)
{
    local items = event.items

    for i, id in pairs(event.items) do
        table.insert(self.items, id)
    end
}
Initialized 프로퍼티에 따라 상점 구매 로직 진행 여부를 결정하는 Logic 스크립트 예제입니다.

Method:  
[server]
void RequestBuyItemFromClient(string userId, integer buyItemId)
{
    local userEntity = _UserService:GetUserEntityByUserId(userId)
        if isvalid(userEntity) == false then
            return
        end

    local userDataComponent = userEntity.UserDataComponent
    if isvalid(userDataComponent) == false then
        return
    end

    if userDataComponent.initialized == false then
        log("userDataComponent not initialized") -- Load 실패 시 상점 구매 진행하지 않음.
        return
    end

    -- 상점 구매 진행...
}

Event Handler:
[server only] [service UserService]
HandleUserLeaveEvent(UserLeaveEvent event)
{
    self:SaveData()
}
DataStorage 사용량 제한과 문자열
DataStorage는 사용량 제한이 있습니다. 제한으로 인해 Credit을 사용하는 DataStorage 류의 함수들을 너무 자주 호출하면 문제가 발생할 수 있습니다. 사용량 제한의 자세한 내용은 DataStorage 사용량 제한 알아보기, DataStorage 사용량 제한 활용하기를 참고하세요.

하나의 String으로 저장
Key를 사용하면 Credit을 사용합니다. 아래 예시처럼 많은 Key를 사용하면 데이터 불러오거나 저장할 때 많은 Credit을 사용하게 됩니다.
월드 제작 초기에는 Key 수가 적을 수 있지만, 월드를 계속 만들수록 프로퍼티를 계속 추가하게 될 수도 있습니다. 이렇게 되면 Credit을 더 많이 사용하게 됩니다.
Credit을 효율적으로 사용하기 위해 하나의 String으로 데이터들을 묶고, 하나의 Key를 사용해 저장하는 방식을 사용할 수 있습니다. 연관있는 데이터들을 하나로 모아 묶는 것을 권장합니다. 이 방식을 사용해 데이터를 저장하고 불러오면 데이터 관리가 쉬워집니다.

Json String 변환 함수 사용
_HttpService:JSONEncode() 와 _HttpService:JSONDecode()를 사용하여 저장 및 불러오기 합니다.
Json과 Table 간의 변환이 가능합니다.

void PrintTable()
{
    local testTable = {}
    testTable.meso = 10
    testTable.money = 200
    testTable.innerTable = {}
    testTable.innerTable.val = "string value"

    log(_HttpService:JSONEncode(testTable))
}

-- JsonEncode의 결과
{"meso":10,"money":200,"innerTable":{"val":"string value"}}
UtilLogic의 변환 함수 사용
_UtilLogic:TableToString() 와 _UtilLogic:StringToTable() 사용해 하나의 String으로 묶을 수 있습니다.
Table이 Table을 가지고 있는 경우 정상적으로 변환되지 않습니다. Key, Value의 Type도 String으로 출력하므로 String 길이가 길어질 수 있습니다.

void PrintTable()
{
    local testTable = {}
    testTable.meso = 10
    testTable.money = 200
    testTable.innerTable = {}
    testTable.innerTable.val = "string value"

    log(_UtilLogic:TableToString(testTable))
}

-- TableToString의 결과
String  meso    Int64   10
String  money   Int64   200
String  innerTable  LuaTable    table :868
직접 문자열로 합치고 나누기
크리에이터는 사전 정의된 String 형식을 따르는 함수들을 사용하는 대신 직접 string을 만들어 사용할 수 있습니다. 직접 만들 경우 데이터를 더 짧은 문자열로 저장할 수 있습니다.
아래의 예제와 같이 _UtilLogic:Split()과 문자열 합치기(..)를 사용해 String을 문자열로 나누고, 합칠 수 있습니다. Table 데이터는 table.concat을 사용할 수 있습니다.

Property:
[None]
integer meso = 0
[None]
integer cash = 0
 
Method:
[server only]
boolean LoadCurrency()
{
    local userDataStorage = _DataStorageService:GetUserDataStorage(self.Entity.PlayerComponent.UserId)
    if userDataStorage == nil then
        return
    end

    local errorCode, currencyString = userDataStorage:GetAndWait("Currency")
    if errorCode ~= 0 then
        log(errorCode)
        return false
    end

    if _UtilLogic:IsNilorEmptyString(currencyString) == false then
        local split = _UtilLogic:Split(currencyString, ",")
        if split[1] ~= nil then
            self.meso = tonumber(split[1])
        end

        if split[2] ~= nil then
            self.cash = tonumber(split[2])
        end
    end

    return true
}

[server only]
string GetCurrencyString()
{
    local currencyString = tostring(self.meso) .. "," .. tostring(self.cash)
    return currencyString   -- 이 String을 value로 저장한다. SetAndWait("Currency", currencyString)
}
DataStorage 사용량 제한과 저장 주기
사용량 제한이 걸린 DataStorage에 데이터를 자주 저장하게 하면 Credit이 부족할 수 있습니다. 그러므로 값이 변경될 때마다 데이터를 저장할 필요가 없는 값들은 Property를 사용해 특정 상황일 때만 저장해 Credit 소모량을 줄일 수 있습니다. 주로 아래 3가지 상황에서 저장하는 것을 권장합니다.

유저 접속 종료 시 저장: 유저가 접속을 종료하면 데이터를 DataStorage에 저장합니다.

일정 시간마다 저장: 유저의 갱신된 정보는 주기적으로 저장해야 합니다. 서버에 문제가 생겨 저장에 실패할 수도 있기 때문입니다. 이때 적절한 저장 주기를 결정해 사용하는 것이 좋습니다. 자주 저장을 요청하면 DataStorage 보관 안정성은 높아지지만 Credit을 더 많이 소모하기 때문입니다.

Property:
[None]
integer saveDataTimer = 0

Method:
[server only]
void OnBeginPlay()
{
    local intervalSeconds = 300 -- 5분 간격으로 data를 저장.
    local startDelaySeconds = 300
    local userId = self.Entity.PlayerComponent.UserId

    local callback = function()
        _UserDataLogic:SaveData(userId) -- Logic의 Save 함수 호출.
    end

    self.saveDataTimer = _TimerService:SetTimerRepeat(callback, intervalSeconds, startDelaySeconds)
}
예외 처리 시 저장: 예외 상황이 발생했을 때 데이터를 DataStorage에 저장합니다. 크리에이터가 만든 월드에서 무조건 데이터가 갱신될 때 저장해야만 하는 값이 있다면 그때만 예외적으로 저장하게 처리할 수 있습니다.
5

DataStorage 사용량 제한 시 고려할 점
유저가 직접 DataStorage 류 함수 실행 피하기
유저가 데이터 갱신 버튼을 눌렀을 때 DataStorage 류 함수를 사용하게 만들지 않는 것이 좋습니다. 크리에이터의 의도로 다른 유저의 행동으로 인해 생각보다 많은 Credit을 소모하게 될 수도 있기 때문입니다. 만약 유저의 행동으로 DataStorage류 함수를 사용해야 한다면 해당 기능을 사용할 수 있는 주기를 설정해 의도하지 않게 Credit을 사용하게 되는 경우를 줄일 수 있습니다.

유저가 UI 버튼을 눌러서 DataStorage에서 데이터를 매번 불러오는 코드를 작성했다 생각해 봅시다. 특정 유저가 크리에이터의 예상과 달리 매우 빈번하게 해당 버튼을 누르게 된다면 Credit이 매우 많이 사용하고, 낭비하게 됩니다.

아래 스크립트는 유저가 저장버튼을 이용해 데이터를 저장합니다.
쿨다운을 추가하여 유저가 짧은 시간동안 여러번 저장하는 행동을 방지하여 과도한 Credit 사용을 막습니다.

Property:
[None]
number lastSaveTime = 0

Method:
[server]
void SaveData()
{
	local cooldown = 120	-- 120초 동안 저장 불가

	if _UtilLogic.ServerElapsedSeconds < self.lastSaveTime + cooldown then
		-- cooldown을 이용해 유저가 짧은 시간 동안 저장을 여러번 시도하는 것을 방지합니다.
		return
	end

	self.lastSaveTime = _UtilLogic.ServerElapsedSeconds

	-- DataStorageService를 이용해 데이터 저장...
}

Event Handler:
[client only] [entity] [Button_Save (/ui/DefaultGroup/Button_Save)]
HandleButtonClickEvent(ButtonClickEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: ButtonComponent
    -- Space: Client
    ---------------------------------------------------------
    
    -- Parameters
    local Entity = event.Entity
    ---------------------------------------------------------
    
	self:SaveData()
}
인스턴스 룸, DataStorage 류 함수 Credit 사용량 고려
인스턴스 룸을 사용한 월드는 인스턴스 룸의 특성까지 고려해 Logic에서 DataStorage류 함수들을 사용해야 합니다. 예를 들어 월드 전체의 랭킹을 주기적으로 DataStorage에서 랭킹 데이터를 가져와 계산하고, 클라이언트 요청에 따라 랭킹을 보여주게 만들었다 생각해봅시다. 유저가 인스턴스 룸에 입장한 경우 인스턴스 룸 개수만큼 랭킹을 계산하기 때문에 Credit 사용량을 고려해야 합니다. 이때도 적절한 업데이트 주기를 설정해 Credit 소모를 막을 수 있습니다.
6

유저 퇴장 시 UserLeaveEvent Handler에서 Data 저장하기
유저가 퇴장할 때 DataStorage에 저장하는 기능 구현은 UserLeaveEvent Handler에 추가되어야 합니다.
OnEndPlay에서 AndWait 함수를 사용해 데이터를 저장하면, 유저가 월드에 재진입할 때 이전에 저장한 데이터를 정상적으로 불러오지 못할 수 있습니다.
OnEndPlay에서 SetAndWait나 SetAsync를 이용해 데이터를 저장한 경우, 유저가 월드 재진입 시 잘못된 데이터를 가져오는 상황이 발생할 수 있습니다.
8

OnEndPlay 대신 UserLeaveEvent Handler에서 DataStorage류 함수를 호출하면, 유저가 재접속 했을 때 이전의 SetAndWait, SetAsync 함수의 실행 완료를 보장합니다.
8
단, 아래처럼 Async Callback을 이용하여 DataStorage 저장 함수를 호출하는 경우 함수 실행 완료를 보장되지 않으므로 주의합니다.

Method:
[server only]
void OnBeginPlay()
{
    local userDataStorage = _DataStorageService:GetUserDataStorage(userId)
    if userDataStorage == nil then
        return
    end

    local callBack = function()
        userDataStorage:SetAsync("DataKey2", "222", nil)    -- 유저 재접속 전에 "222" 저장 보장 X
    end

    userDataStorage:SetAsync("DataKey1", "111", callBack)    -- 유저 재접속 전에 "111" 저장 보장 O
}
 
Event Handler:
[server only] [service UserService]
HandleUserLeaveEvent(UserLeaveEvent event)
{
    self:SaveData()
}
UserLeaveEvent 핸들러는 아래와 같은 특징을 가지고 있습니다.

유저가 떠날 때 UserService에서 발생하는 이벤트입니다.

UserLeaveEvent 핸들러 실행이 완료된 뒤 유저 엔티티 삭제가 진행됩니다.

UserLeaveEvent 핸들러 실행이 오래 걸리면서 일정 시간 이상이 소요되게 되면 유저 엔티티 삭제가 실행이 완료되기 전에 진행됩니다.FastVector3을 활용한 월드 최적화
학습 과정 소개
FastVector3을 사용하는 방법과 월드 최적화에 활용하는 방법에 대해 알아봅시다.

Fast 타입
FastVector2, FastVector3, FastColor 타입은 Lua Table로 작성되어 기존의 Vector2, Vector3, Color를 보완할 수 있습니다 .두 종류의 타입 모두 같은 기능을 제공하지만, Fast 접두사가 붙은 타입은 월드에 부하가 발생할 때 최적화 용도로 사용할 수 있습니다.

FastVector3 특징
FastVector3의 5가지 특징은 다음과 같습니다.

FastVector3은 Lua Table로 구현되어 Vector3에 비해 가볍고 유연합니다.
[object Object]

FastVector3은 Vector3의 모든 프로퍼티와 함수가 구현되어 있으며, Vector3으로 자동 변환을 지원합니다.

FastVector3은 동기화를 지원하지 않습니다. 그러므로 다른 공간 실행 함수의 매개변수로 사용할 수 없습니다.

FastVector3은 8 Byte 실수형 값을 사용하고, Vector3은 4 Byte 실수형을 사용합니다. 이로 인해 두 타입 사이의 유효 범위와 연산 결과는 차이가 발생할 수 있습니다.

FastVector3은 zero, forward 등의 static 프로퍼티에 접근할 때 원본의 참조를 반환하는 반면, Vector3은 복제된 값을 반환합니다.

FastVector3 사용
생성자 변경
Vector3의 생성자를 FastVector3의 생성자로 변경해 사용할 수 있습니다. 연산이 많아질 수록 FastVector3과 Vector3의 성능 차이가 커집니다.

Vector3은 아래와 같은 방식으로 사용합니다.

-- Vector3을 사용할 때
local newPosition = Vector3(0, 0, 0)
newPosition.x = 1
newPosition.y = 2
self.Entity.TransformComponent.Position =  newPosition
FastVector3은 아래와 같이 사용합니다.

local newPositionFast = FastVector3(0, 0, 0)
newPositionFast.x = 1
newPositionFast.y = 2
self.Entity.TransformComponent.Position = newPositionFast
Static 프로퍼티 사용
FastVector3의 Static 프로퍼티를 사용할 때는 주의가 필요합니다. FastVector3의 특징 중 하나인 Static 프로퍼티 접근 시 원본의 참조를 변환하는 특성으로 인해 Static 프로퍼티에 직접 접근하면 해당 Static 프로퍼티의 값이 모두 변경될 수 있습니다.
아래와 같이 Clone() 함수를 사용해 값을 복제해 사용해야 합니다.

local vt = FastVector3.zero:Clone() 
vt.x = 1
FastVector3은 FastVector3.zero의 프로퍼티 값을 변경하면 FastVector3.zero가 변경됩니다.

local vt = FastVector3.zero
vt.x = 1 -- FastVector3.zero : FastVector(1,0,0)
Vector3은 아래와 같이 Vector3.zero의 프로퍼티 값을 변경하여도 Vector3.zero가 변경되지 않습니다.

local vt = Vector3.zero
vt.x = 1 -- Vector3.zero : Vector(0,0,0)
매개변수 타입 지정
FastVector3은 프로퍼티 타입, 함수의 매개변수로 지정할 수 없습니다. 그러므로 FastVector3을 타입이나 매개 변수로 사용할 때는 any, table 타입을 사용해야 합니다.
특히 mLua를 사용할 때는 any 타입을 사용하고, 어노테이션(Annotation)을 함께 사용하기를 권장합니다.

---@type FastVector3
property any vt = FastVector3(0,0,0)
 
---@param vt FastVector3
method void NewMethod(any vt)
    -- ...
end
FastVector3 기능 확장
FastVector3은 함수나 프로퍼티를 추가하여 기능을 확장할 수 있습니다. 또한 기존 함수나 프로퍼티의 값을 변경하는 것도 가능합니다.

-- static 프로퍼티 추가
FastVector3.two = FastVector3(2, 2, 2)
 
-- 함수 추가
local v3mt = getmetatable(FastVector3.zero)
v3mt.NewFunction = function(self)
    -- ...
end
FastVector3 효율적으로 사용하기
FastVector3 타입을 사용해 참조 객체 생성을 줄일 수 있습니다.
메이플스토리 월드에서는 Lua에서 Native 타입에 접근 시 참조 객체가 생성됩니다. 이는 참조되는 객체가 파괴되지 않게 하기 위함입니다. 이렇게 생성된 참조 객체는 사용이 끝나면, Lua의 Lua Garbage Collector에서 먼저 메모리가 정리되고, 그 후 Native의 Garbage Collector에서 다시 한 번 정리 작업을 거쳐 메모리에서 완전히 제거되게 됩니다.

참조 객체 생성하지 않게 사용하기
최적화를 위해 Vector3 대신 FastVector3을 사용하는 이유는 값을 생성하거나, 읽어올 때 참조 객체를 생성하지 않기 때문입니다.
Vector3의 경우 Lua 스크립트에서 사용하기 위해 참조 객체가 필요합니다. 메이플스토리 월드의 Vector3 객체를 사용하면 참조 객체가 자동으로 생성, 파괴됩니다. 그러나 이 과정에서 처리 시간이 길어지고 메모리 사용량이 증가해 최적화가 필요하게 됩니다.

-- Position 값을 읽어올 때 참조 객체가 생성됨
local position = self.Entity.TransformComponent.Position
 
-- Vector3 객체를 생성할 때 참조 객체가 생성됨
local vt = Vector3(0, 0, 0)
-- 참조 객체가 생성됨
local newPosition = Vector3(0, 0, 0)
-- 참조 객체가 생성되지 않음
newPosition.x = 1
newPosition.y = 2
self.Entity.TransformComponent.Position =  newPosition
참조 객체를 생성하지 않는 FastVector3 사용 예제는 아래와 같습니다.

-- 참조 객체가 생성되지 않음
local newPositionFast = FastVector3(0, 0, 0)
 
-- 참조 객체가 생성되지 않음
newPositionFast.x = 1
newPositionFast.y = 2
-- 네이티브 프로퍼티에 FastVector3을 대입할 때는 참조 객체가 생성되지 않음
self.Entity.TransformComponent.Position =  newPositionFast
TransformComponent의 Position과 WorldPosition 프로퍼티 타입은 Vector3 입니다. 그러므로 값을 읽어올 때 참조 객체가 생성됩니다. 두 프로퍼티를 참조 객체를 생성하지 않고 사용하고 싶다면, PositionAsFastVector3(), WorldPositionAsFastVector3() 함수를 활용할 수 있습니다.

Tip.
UITransformComponent도 PositionAsFastVector3(), WorldPositionAsFastVector3() 함수를 사용해 동일한 방법으로 활용할 수 있습니다.

TransformComponent의 Position 값을 변경하는 코드의 성능을 비교해봅시다.

local transform = self.Entity.TransformComponent
  
-- 평균 1.113 us
local position1 =  transform:PositionAsFastVector3() -- 참조 객체가 생성되지 않음

position1.x += 0.1
position1.y += 0.1
transform.Position = position1
 
-- 평균 2.217 us
local position2 =  transform.Position --  참조 객체가 생성됨

position2.x += 0.1
position2.y += 0.1
 
-- 평균 1.876 us
local position3 =  FastVector3(transform.Position) -- 참조 객체가 생성됨

position3.x += 0.1
position3.y += 0.1
transform.Position = position3
Vector3 스크립트 프로퍼티에 FastVector3을 대입하면 Vector3로 자동 변환됩니다. 이 자동 변환으로 인해 크리에이터의 의도대로 FastVector3이 동작하지 않을 수 있으므로 아래와 같은 사용은 지양해야 합니다.
타입을 Vector3이 아닌 any 또는 table로 지정해야 자동 변환으로 인한 문제가 발생하지 않습니다.

Property:
Vector3 vt3 = Vector3(0, 0, 0)

Method:
void Test()
{
    -- FastVector3가 Vector3으로 자동 변환
    self.vt3 = FastVector3(1, 1, 1)

    -- 로컬 변수가 Vector3를 참조하면서 참조 객체가 생성
    local vt = self.vt3
}
FastVector3와 인덱스 활용
FastVector3은 인덱스를 이용해 접근할 수도 있습니다. 아래 표를 보면 인덱스를 이용한 접근이 키를 이용한 접근보다 약간 더 빠른 것을 알 수 있습니다.

[object Object]

인덱스를 이용해 FastVector3에 접근하는 예제는 아래와 같습니다. x는 1, y는 2, z는 3에 대응됩니다.

local v = FastVector3(1, 2, 3)
print(v.x, v.y, v.z)      -- Output: 1 2 3
print (v[1], v[2], v[3])  -- Output: 1 2 3
인덱스 접근은 월드 성능 최적화에 도움이 됩니다. 하지만 x, y, z 멤버를 직접 접근하는 것보다 상대적으로 가독성이 낮습니다. 그러므로 인덱스를 이용한 접근은 월드에 최대한의 최적화가 필요한 상황에서만 사용하기를 권유합니다. 예를 들어 Normalize() 함수 호출 빈도가 지나치게 높은 경우, 아래와 같이 인덱스 접근을 사용하면 성능을 개선할 수 있습니다.

local v3mt = getmetatable(FastVector3.zero)
 
-- FastVector3의 Normalize 함수를 수정
v3mt.Normalize = function(self)
    local x, y, z = self[1], self[2], self[3] -- self.x , self.y , self.z
    local length = (x*x + y*y + z*z) ^ 0.5
 
    if length == 0 then
        return FastVector3(x, y, z)
    end
 
    return FastVector3(x / length, y / length, z / length)
end제작 시 준수 사항
콘텐츠 제작의 IP사용 가이드
확률 정보 공개
생성형 AI를 활용한 CGC 제작 가이드
비정상 거래 대응 가이드콘텐츠 제작의 IP사용 가이드
콘텐츠 제작의 IP 사용 가이드 LinkIP의 구체적인 활용 가능 범위
Toben이 직접 제공하는 IP 또는 별도로 사용을 허락한 게임 IP의 구체적인 활용 가능 범위를 안내합니다.
직접 제공하는 IP 또는 사용을 허락하는 게임 IP는 변동 및 업데이트될 수 있으며, 크리에이터는 최신 버전의 가이드를 준수해야 합니다.


사용하려는 리소스가 허용 범위 외의 리소스인지 아닌지는 어디로 문의를 하면 되나요?
가이드 내용 외 리소스 관련 궁금한 사항이 있을 경우, 아래 경로로 상세 내용을 담아 문의 접수 부탁드립니다.

문의 접수처: 메이플스토리 월드 고객센터 > 기타문의 > 저작권 > 임의의 자주 찾는 도움말 클릭 > 파란색 [문의하기] 버튼


Toben이 직접 제공하는 IP 또는 별도로 사용을 허락한 게임 IP 중 구체적인 활용 가능 범위가 안내되지 않은 경우에는 어떻게 사용해야 하나요?
직접 제공하는 IP 또는 별도로 사용을 허락하는 게임 IP에 따라 활용 가능 범위 및 안내 기준이 상이할 수 있습니다.
구체적인 범위가 안내되지 않은 경우, IP 사용에 대한 기본 내용을 준수하며 콘텐츠를 제작해야 합니다. 대표적인 금지 행위는 다음과 같습니다.

IP가 콘텐츠 제작의 IP사용 가이드 제3조 각 항에 기재된 게임 내에서 제3자와의 프로모션/콜라보 등을 통해 사용되고 있거나 사용된 경우

㈜넥슨코리아가 퍼블리싱 하고 있는 게임과 동일하거나 상당히 높은 정도로 유사하여, ㈜넥슨코리아의 공식 콘텐츠로 오인될 수 있는 경우


메이플스토리 월드에서 이미 ‘메이플스토리’,’바람의나라’ IP를 활용한 RPG 장르 월드를 제작하고 있으며, 허용 범위 외 리소스를 이미 월드 내 구현하였거나, 개발 중인 상황입니다. 어떻게 해야 하나요?
최초 월드 제작 시점과 무관하게, 메이플스토리 월드에서 개발을 하는 크리에이터 분들께서는 본 가이드라인을 준수해 주셔야 합니다.
메이플스토리 월드에서 RPG 장르 월드를 제작하고 계신 경우, 허용 영역 외 리소스를 이미 월드 내 구현하셨거나, 향후 추가적인 업데이트를 통해 그러한 콘텐츠가 추가될 수 있는 경우에도 본 가이드라인의 준수가 필요합니다

메이플스토리
메이플스토리 IP(해외 서비스 중인 메이플스토리 고유 콘텐츠 포함)를 활용한 ‘2D 횡스크롤 RPG 콘텐츠’는 원칙적으로 ㈜넥슨코리아가 퍼블리싱 하고 있는 메이플스토리 게임과 동일하거나 상당히 높은 정도로 유사한 것으로 간주합니다.
다만, 위의 ‘2D 횡스크롤 RPG 콘텐츠’ 라고 하더라도 ‘5차 전직 콘텐츠를 포함한 2016. 6. 30. V 업데이트(해당 날짜는 국내 메이플스토리 기준이며, 해외 메이플스토리의 경우 각각의 업데이트 도입 시점에 따름)’ 이전의 IP만을 활용하는 경우 ‘Global MapleStory Classic World에 새롭게 추가된 고유 콘텐츠’를 포함하지 않은 경우에는 CGC 제작 및 게시가 허용됩니다.


한국 시점 기준, ‘메이플스토리’ 5차 전직 콘텐츠를 포함하는 ‘16. 6. 30. V 업데이트’ 부터 모든 리소스 사용이 불가한가요?
RPG 장르의 콘텐츠를 제작/출시하시는 경우, 안내드린 가이드에서 명시된 제한적인 범위 내에서만 제작이 가능합니다. 그 외의 장르에 대해서는 새롭게 추가된 리소스 활용 허용 범위와 관계없이 리소스 사용이 가능합니다.

예시 1: 디펜스 장르의 월드에서, 특정 타워의 공격에 5차 전직 스킬 이펙트 리소스를 활용하는 것은 제한 대상이 아닙니다.

예시 2: 소셜 장르의 월드에서 5차 전직 업데이트 이후 출시된 지역의 배경 리소스를 활용하는 것은 제한 대상이 아닙니다.

예시 3: 캐주얼 장르의 월드에서 기준 시점 이후 출시된 보스 리소스를 활용하여 엔드 콘텐츠를 제작하는 것은 제한 대상이 아닙니다.

예시 4: MMORPG가 아닌 장르(로그라이크, CRPG, 액션 RPG 등)의 월드이며, 메이플스토리 공식 콘텐츠로 오인할 가능성이 낮은 월드에서 5차 전직 업데이트 이후 출시된 직업의 캐릭터를 업데이트하는 것은 제한 대상이 아닙니다.

예시 5: MMORPG 장르의 월드이면서 메이플스토리 공식 콘텐츠로 오인할 가능성이 있는 월드에서 5차 전직 업데이트 이후 출시된 지역을 구현하는 것은 제한 대상에 해당합니다.

바람의나라
바람의나라 IP를 활용한 '2D RPG 콘텐츠'는 원칙적으로 ㈜넥슨코리아가 퍼블리싱 하고 있는 바람의나라 게임과 동일하거나 상당히 높은 정도로 유사한 것으로 간주합니다.
다만, 위의 '2D RPG 콘텐츠'라고 하더라도 '2003. 06. 03. ver 5.50 환상의섬 업데이트(한국 시점 기준) ' 까지의 IP만을 활용하는 경우에는 CGC 제작 및 게시가 허용됩니다.


한국 시점 기준, '바람의나라 2003년 6월 3일 환상의섬 업데이트' 이후 모든 리소스 사용이 불가한가요?
RPG 장르의 콘텐츠를 제작/출시하시는 경우, 안내드린 가이드에서 명시된 제한적인 범위 내에서만 제작이 가능합니다. 그 외의 장르에 대해서는 새롭게 추가된 리소스 활용 허용 범위와 관계없이 리소스 사용이 가능합니다.

예시 1: 디펜스 장르의 월드에서, 5차 승급 마법 이펙트 리소스를 활용하는 것은 제한 대상이 아닙니다.

예시 2: 소셜 장르의 월드에서 백두산 지역의 배경 리소스를 활용하는 것은 제한 대상이 아닙니다.

예시 3: 캐주얼 장르의 월드에서 기준 시점 이후 출시된 리소스를 활용하여 콘텐츠를 제작하는 것은 제한 대상이 아닙니다.

예시 4: MMORPG가 아닌 장르(로그라이크, CRPG, 액션 RPG 등)의 월드이며, 바람의나라 공식 콘텐츠로 오인할 가능성이 낮은 월드에서 환상의섬 업데이트 이후 출시된 직업을 활용하는 것은 제한 대상이 아닙니다.

예시 5: MMORPG 장르의 월드이면서 바람의나라 공식 콘텐츠로 오인할 가능성이 있는 월드에서 백두산 전설 업데이트 포함, 이후 출시된 지역 또는 배경 리소스 등을 활용하여 구현하는 것은 제한 대상에 해당합니다.

오리지널 월드
오리지널 월드는 메이플스토리 월드에서 직접 운영하는 월드로 위 넥슨코리아가 퍼블리싱 하고 있는 메이플스토리, 바람의나라 게임과 동일 유사성을 방지하기 위한 목적의 IP 사용 제한 기준이 적용되지 않습니다.

메이플스토리 월드에서는 플랫폼 차원의 IP 사용 범위 확장 및 축소를 검토할 수 있으며, 플랫폼에서 사용을 허락하는 IP를 활용해 다양한 크리에이터 창작 콘텐츠가 생산될 수 있도록 고민하고 검토하겠습니다.

나만의 CGC 제작을 위한 수많은 고민과 노력으로 힘 써주실 모든 크리에이터 분들의 열정을 진심으로 응원합니다.
확률 정보 공개
확률 정보 공개란?
메이플스토리 월드의 모든 크리에이터는 창작한 아이템 내 확률형 아이템을 제공하는 경우 확률 정보 공개 가이드에 따라 아이템 사용 전 사용자에게 고지해야 할 의무가 있습니다.

메이플스토리 월드의 확률 정보 공개 가이드는 ‘확률형 아이템 확률 정보공개 관련 해설서’의 내용을 따릅니다. 해당 해설서의 내용을 따르지 않을 경우 최대 월드 이용 제한이 적용될 수 있습니다.

확률 정보 공개 대상 및 방법
아래 항목에 해당할 경우 확률형 아이템 정보 공개 대상이 될 수 있으며, 자세한 확률 정보 공개 대상 및 방법은 확률형 아이템 확률 정보 공개 관련 해설서를 확인해주시기 바랍니다.
확률형 아이템 확률 정보공개 관련 해설서 바로가기

확률형 아이템이란?

플레이어가 직접적ㆍ간접적으로 유상으로 구매하는 아이템 중 구체적 종류, 효과 및 성능 등이 우연적 요소에 의하여 결정되는 것

확률형 아이템의 종류

캡슐형 확률형 아이템: 구매 또는 사용 시 다른 아이템을 제공하는 확률형 아이템으로서 제공되는 아이템의 종류ㆍ등급ㆍ성능 등이 우연적 요소에 의하여 결정되는 확률형 아이템

강화형 확률형 아이템: 구매 또는 사용 시 다른 아이템의 종류ㆍ등급ㆍ성능을 변화시키는 확률형 아이템으로서 그 변화 결과가 우연적 요소에 의하여 결정되는 확률형 아이템

합성형 확률형 아이템: 이용자가 직접적ㆍ간접적으로 유상 구매하는 아이템과 다른 아이템을 결합하여 획득하는 확률형 아이템으로서 해당 확률형 아이템의 종류ㆍ등급ㆍ성능이 우연적 요소에 의하여 결정되는 확률형 아이템

3종 외 추가 확인 필요 아이템 유형

A. 제공되는 총수 또는 기간이 한정된 확률형 아이템

B. 확률 정보가 변경되는 확률형 아이템

C. 소위 ‘천장’ 시스템이 있는 확률형 아이템

D. 월드코인을 통해 획득한 재화로 확률형 아이템을 구매하는 아이템 등

확률형 아이템 준수사항
메이플스토리 월드의 모든 크리에이터는 창작한 아이템 내 확률형 아이템을 제공함에 있어 아래의 내용을 모두 준수하였는지 확인해주시기 바랍니다. 본 준수사항 및 이외 해설서에 안내되어 있는 항목을 위반하는 경우 최대 월드 이용 제한이 적용될 수 있습니다.

분류	내용
표시 방법 준수 여부	
확률 정보를 백분율로 표시하였는가?
확률 표기는 최초로 0 이외의 숫자가 나오는 자리보다 네 자리 이상 낮은 소수점 자리에서 반올림하여 표시하였는가?
개별 확률 안내가 어려운 경우 분수 등 플레이어가 쉽게 이용할 수 있는 방법으로 표시하였는가?
확률 고지 경로/방식 준수 여부	월드 내 고지 여부
월드 내 사용 화면에서 확인 가능하도록 표시하였는가?
확인이 어려운 경우 월드 내 외부연결 링크 등 대체제를 마련하였는가?
홈페이지 고지 여부
개별 커뮤니티 등에 확률 정보를 안내했을 경우, 해당 URL을 월드 ‘상세 화면’ – 공지 사항에 기재하였는가?
공개 대상 준수 여부	
캡슐형/강화형/합성형 확률형 아이템에 대한 확률을 공개하였는가?
유료+무료 아이템에 대한 확률을 공개하였는가?
제공 수/기간을 명확하게 안내하였는가?
고지 확률 일치 여부	
인 월드, 홈페이지 등에 고지한 확률이 일치하는가?
월드 내 실제 적용 확률과 고지 확률이 일치하는가?
확률 고지 기간 준수 여부	
판매 중인 기간 동안 고지하고 있는가?
확률형 아이템 공급 정보 변경 시 사전 고지를 진행하였는가?
광고/선전물 표시 방법 준수 여부	
외부 마케팅 영역에 관련 안내를 포함하고 있는가?
본 가이드에서 안내되지 않은 콘텐츠 개발에 대한 준수사항은 크리에이터 이용약관 및 크리에이터 운영정책을 따릅니다.생성형 AI를 활용한 CGC 제작 가이드
Toben Studio Inc.(이하 “Toben”)는 크리에이터의 메이플스토리 월드 플랫폼(이하 “플랫폼”) 내 생성형 AI를 활용한 크리에이터 제작 콘텐츠(Creators Generated Contents 이하 "CGC") 제작 및 게시 등 행위가 올바르게 이루어질 수 있도록 본 가이드를 마련하였습니다.

생성형 AI 정의
생성형 AI(Generative Artificial Intelligence)란 텍스트, 이미지, 음악 등 기존에 학습된 콘텐츠를 기반으로 다양한 형태의 새로운 콘텐츠를 생성할 수 있는 인공지능 기술을 의미합니다. 생성형 AI를 활용하면 효율적인 작업이 가능해지고 창의적인 콘텐츠 생성에 도움을 받을 수 있습니다. Toben은 크리에이터 분들의 자유로운 창작 활동을 지지하며, 본 가이드 내용을 준수한다는 전제 하에 크리에이터가 생성형 AI를 활용하여 플랫폼 내에서 CGC를 제작 및 게시하는 등의 행위를 허용하고 있습니다.

생성형 AI 종류
본 가이드에서 ‘생성형 AI’란 CGC를 제작하는 과정에서 AI 기술을 활용한 ‘사전 생성형 AI’와 CGC 제작 및 게시 이후에도 플랫폼 내부에 실시간으로 계속 AI 기술이 활용되는 ‘실시간 생성형 AI’로 구분됩니다. 본 가이드 내용은 달리 정함이 없는 한 위 ‘사전 생성형 AI’ 및 ‘실시간 생성형 AI’ 모두에 적용됩니다.

생성형 AI 활용 시 준수 사항
크리에이터가 플랫폼 내에서 생성형 AI 활용 CGC 제작 및 게시 등을 하는 경우 이하 내용을 준수하여야 함을 안내 드립니다.

플랫폼 규정 준수. 크리에이터가 플랫폼 내에서 생성형 AI를 활용하여 CGC 제작 및 게시 등을 하는 경우 크리에이터 이용약관 및 운영정책을 위반하지 않아야 합니다. Toben은 플랫폼에서 CGC 관련 금지되는 행위가 무엇인지에 대하여 구체적으로 명시하여 안내하고 있으며, 금지 행위에는 CGC에 선정적, 음란성, 잔인함, 혐오감, 폭력적, 자극적, 사기, 사행, 타인의 권리 침해, 개인정보 침해 및 사회적 통념상 비정상적이거나 일반적이지 않은 의도를 가진 내용이나 행위가 포함됩니다. 만약 해당 위반 사실이 확인되는 경우 Toben은 크리에이터 이용약관 및 운영정책 근거하여 제재할 수 있습니다.


생성형 AI 활용에 따른 책임. 크리에이터는 특정 생성형 AI를 활용하여 플랫폼 내에서 CGC 제작 및 게시 등 행위를 할 수 있는 권리를 보유하고 있는지 확인하여야 하며, 이를 위반하여 발생할 수 있는 모든 책임은 크리에이터에게 있습니다. 크리에이터는 CGC 제작 및 게시 등 행위에 활용된 플랫폼 외부 생성형 AI 관련 약관 및 정책을 확인하고 해당 내용을 준수해야 합니다. 구체적으로, 각각의 생성형 AI에 따라 유의 사항, 출처 표기 방식, 새롭게 제작된 콘텐츠의 상업적 사용 가능 여부 등이 다를 수 있으므로, 해당 내용을 주의 깊게 확인하고 플랫폼 내에서 CGC 제작 및 게시 등 행위를 하는데 활용할 수 있는지 여부를 판단하여야 합니다.
아울러, ‘실시간 생성형 AI’를 활용하는 경우, 플랫폼에서 제공하는 기능 또는 플랫폼에서 인정하는 정상적인 방법(HttpService 기능 등)을 활용하여야 하며, 크리에이터 이용약관 및 운영정책을 위반하는 내용의 CGC가 생성되거나 기술적인 문제 상황이 발생하지 않도록 특히 유의하여야 하고, 이를 위반하는 경우 크리에이터 이용약관 및 운영정책에 근거하여 제재될 수 있습니다.


투명성. 크리에이터는 플랫폼 내에서 생성형 AI를 활용한 CGC 제작 및 게시 등 행위를 한 경우, 이를 다른 회원이 쉽게 확인할 수 있도록 플랫폼 내 해당 사실을 명확히 고지해야 합니다. 구체적으로, 크리에이터는 개별 월드 및 아바타 상품 상세 설명 페이지에 CGC 제작 및 게시 등 행위에 생성형 AI가 활용되었음을 알 수 있도록 문구를 반드시 기재하여 합니다(이하 예시 문구 참조). 위 문구 기재는 필수이며 그 외에 크리에이터가 썸네일 워터마크 등 플랫폼 내 확인 가능한 다양한 방법으로 생성형 AI 활용 사실을 고지하여도 무방합니다.

[예시 문구]
※ 위 월드(또는 아바타 상품)는 생성형 AI를 활용하여 제작된 콘텐츠를 포함하고 있습니다.
생성형 AI 활용과 관련된 자세한 내용은 ‘생성형 AI를 활용한 CGC 제작 가이드’에서 확인하실 수 있습니다.

신고. 누구든지 본 가이드를 위반한 생성형 AI 활용 CGC를 발견한 경우, 플랫폼 내 기능을 통해 신고를 접수할 수 있습니다. 접수된 신고 내역을 통해 위반 사항이 명확히 확인될 시 관련 규정에 따라 조치가 취해집니다. 더불어 플랫폼 내 생성형 AI 활용 CGC로 인한 저작권, 명예훼손, 초상권 등 권리 침해 시 신고 방법은 넥슨 권리침해신고 안내에서 확인하실 수 있습니다



더욱 원활하고 건강한 CGC 제작 문화를 만들어 갈 수 있도록 본 가이드라인 내용을 준수 부탁드리겠습니다. 감사합니다.비정상 거래 대응 가이드
월드가 성장하고 다수의 유료 상품이 추가되면 더욱 다양한 형태의 거래 및 결제 행위가 발생할 수 있으며 이러한 거래 행위가 올바르게 관리될 수 있도록 본 가이드를 마련하였습니다. 비정상 거래로 인한 피해로부터 크리에이터님의 콘텐츠를 보호할 수 있도록 안내드리는 가이드에 맞춰 사전 예방하시는 것을 권장해 드립니다.

비정상 거래 대응의 필요성
크리에이터는 크리에이터가 제작한 월드에서 운영정책 위반 행위가 발생하지 않도록 플레이어 간의 거래 방식과 거래 시스템에 대해 긴밀한 관리가 필요합니다.


플랫폼에서 금지하고 있는 비정상 거래의 기준에 따른 관리가 이루어지지 않을 경우 월드 내 시장 경제에 피해를 줄 수 있으며, 결제 도용 등을 비롯한 비정상 거래로 인해 선량한 플레이어에게 추가 피해를 줄 수 있습니다.

비정상 거래로 인한 피해 발생 시, 플랫폼에서의 관리 조치에 따라 판매 수익이 차감되거나 마이너스 수익이 발생할 수 있습니다.

비정상 거래의 기준
이용약관 및 운영정책을 통해 플랫폼에서 금지하고 있는 비정상 거래의 기준을 확인할 수 있으며, 각 문서에 명시되어 있지 않더라도 관련 법령에서 금지되는 불법적인 거래 등이 확인된 경우 플랫폼에서의 관리 조치가 진행될 수 있습니다. 자세한 내용은 플랫폼 운영정책을 확인해주시기 바랍니다.
플랫폼 운영정책 4. 플랫폼 이용제한 바로가기


재화(유료/무료 재화, 아이템 등)를 현금 획득을 목적으로 거래하거나 거래 시도 혹은 유사한 행위를 하는 경우

아이템 이동 등 현금 거래에 도움을 주는 직접적인 행위나 이를 시도하는 경우

타인의 개인정보나 결제정보 등을 도용하여 이득을 취하는 경우

참고
이러한 거래는 플레이어 간의 1:1 거래 뿐만 아니라 불특정 다수와 거래할 수 있는 거래소 콘텐츠, 우편 발송, 획득한 재화 드랍 등 전반에 걸쳐 적용될 수 있습니다.

비정상 거래의 사전 예방
크리에이터는 유료 상품 및 거래 시스템 추가 시 이하 내용을 참고하여 월드 내 콘텐츠를 기획하시는 것을 권장해 드립니다.

플레이어 간의 거래를 제한하기

거래 콘텐츠가 없다면 월드 내 계정, 재화를 현금 획득 목적으로 거래하거나 이동하는 등 직접적인 행위 자체를 원천적으로 차단할 수 있습니다.
만약, 월드 설계상 거래 제한이 불가피할 경우 이하의 방법으로 비정상 거래를 효과적으로 지연시킬 수 있습니다.


거래 이용을 위한 선제 조건 추가하기

비정상 거래를 목적으로 유입된 비정상 플레이어가 단기간에 거래를 진행할 수 없도록 다양한 조건을 설정해 보시기 바랍니다.

예시: 레벨 제한, 선행 퀘스트 완료, 특정 업적 달성 등


거래 이용 시 대기 시간 추가하기

비정상 거래를 목적으로 구매/생성된 재화가 월드 내 시장 경제에 영향을 미치는 시간을 저하시킬 수 있습니다.
(단, 이 경우 거래의 투명성을 위해 각 재화의 설명에 거래 제한 기간을 함께 명시해 주셔야 합니다.)


거래 후 판매 대금 획득 시 대기 시간 추가하기

거래가 완전히 종료되기 전까지 비정상 거래를 확인하고 선제적인 대응을 할 수 있는 시간이 추가될 수 있습니다.제작 수정 가이드
중복 컴포넌트 수정하기중복 컴포넌트 수정하기
학습 과정 소개
MSW는 크리에이터의 월드 제작을 지원하기 위해 다양한 기능을 지속적으로 업데이트하고, 수정하고 있습니다. MSW는 앞으로 중복 컴포넌트가 발생하지 않도록 작업 중입니다.
기능 지원이 완전히 종료되기 전에 미리 가이드를 참고해 월드가 문제 없이 동작할 수 있도록 중복 컴포넌트가 있는지 확인하고 수정하시길 권장합니다.

중복 컴포넌트
엔티티나 모델에 동일한 혹은 동류의 컴포넌트가 2개 이상 추가되었다면 그 컴포넌트들을 중복 컴포넌트라 칭합니다. 중복 컴포넌트는 제작 과정에서 예상치 못하게 하나의 엔티티에 동일한 종류의 컴포넌트를 여러 번 추가하거나, 부모-자식 관계의 모델, 엔티티에서 상속 받은 컴포넌트를 인지하지 못한 채 컴포넌트를 추가할 때 주로 발생합니다.

중복 컴포넌트 예시
컴포넌트가 중복될 때 발생하는 문제를 예시와 함께 살펴보며 알아봅시다.

DoorComponent는 Open, Close 함수를 가지고 있습니다.

Method:
void Open()
{
     log("Door Open")
}

void Close ()
{
    log("Door Close")
}
이 컴포넌트를 Extend해 RevolvingDoorComponent, AutomaticSlidingDoorComponent를 만들고 함수를 재정의했습니다.

RevolvingDoorComponent

Method:
override void Open()
{
    log("revolving Door Open")
}

override void Close()
{
    log("Revolving Door Close")
}
AutomaticSlidingDoorComponent

Method:
override void Open()
{
    log("Automatic Sliding Door Open")
}

override void Close()
{
    log("Automatic Sliding Door Close")
}
AutomaticSlidingDoorComponent는 Door1 엔티티에, RevolvingDoorOpenComponent는 Door2에 추가했습니다. 그 후 아래와 같은 로직을 작성해서 DoorComponent를 통해 확장한 두 컴포넌트의 함수를 호출할 수 있습니다.

Property:
[None]
Entity Door1 = /maps/map01/Door1
[None]
Entity Door2 = /maps/map01/Door2

Method:
void OpenAll()
{
    self.Door1.DoorComponent:Open() -- Automatic Sliding Door Open
    Self.Door2.DoorComponent:Open() -- Revolving Door Open
}
그러나 두 컴포넌트를 하나의 TestEntity에 추가했다 생각해봅시다. TestEntity에서 self.TestEntity.DoorComponent:Open()로 함수를 호출하게 되면 둘 중 어떤 컴포넌트의 Open 함수를 호출해야 하는지 알 수 없습니다. 두 컴포넌트 모두 DoorComponent의 함수를 확장해 사용하고 있기에 AutomaticSlidingDoorComponent, RevolvingDoorComponent중 어떤 것이 더 적절한지 모호하기 때문입니다.

Property:
[None]
-- AutomaticSlidingDoorComponent/RevolvingDoorComponent 모두 존재하는 엔티티
Entity Door = /maps/map01/TestEntity

Method:
void OpenAll()
{
    -- AutomaticSlidingDoorComponent/RevolvingDoorComponent 둘 중 어떤 Open()을 할지 모호함
    self.Door.DoorComponent:Open() 
}
중복된 컴포넌트 수정하기
중복된 컴포넌트가 있을 경우 Console, Build Console 창에 관련 로그 메시지가 발생합니다. 이 로그 메시지들은 주로 메이커에서 제작 중인 월드에 처음 들어갈 때, 맵을 변경할 때 출력됩니다. 내용과 상황에 따라 적절하게 컴포넌트를 수정하거나, 제거하면 됩니다. 컴포넌트 중복은 주로 아래 네 가지 상황에서 발생합니다.
1

맵에 이미 배치된 Entity에서 중복 컴포넌트 발생
맵에 배치된 Entity에 중복된 Component가 있을 경우 메이커 프로 모드 최초 진입 시 또는 메이커에서 맵 이동 시 로그 메시지가 Console 창에 발생합니다. 맵에 배치된 엔티티는 두 가지로 나눌 수 있으며 상황에 맞게 중복된 컴포넌트를 해결해야 합니다.

모델에서 배치된 Entity
중복된 컴포넌트를 삭제합니다. 월드 동작에 맞게 모델 또는 엔티티에서 중복된 컴포넌트를 삭제해야 합니다.

맵에 배치된 Entity
에러 메시지를 참고해 중복된 컴포넌트 중 하나를 삭제합니다.

동적으로 생성한 Entity에서 중복 컴포넌트 발생
동적으로 생성한 Entity에 중복된 Component가 있을 경우 테스트 플레이 시, 월드 플레이 시 로그 메시지가 Console 창에 발생합니다. 주로 아래 세 가지 경우에서 발생합니다.

AddComponent() 함수로 컴포넌트 추가
AddComponent()를 사용해 플레이 중 Entity를 동적으로 추가하는 과정에서 컴포넌트 중복이 발생할 수 있습니다. 컴포넌트를 추가하기 전에 Entity나 Model에서 컴포넌트를 삭제하고 추가하는 것이 좋습니다.

맵 이동으로 Entity 생성
다른 맵으로 이동하면 이동한 맵의 Entity를 불러오게 됩니다. 이때 이동할 맵에 중복된 컴포넌트를 가진 Entity가 있을 수 있습니다. 발생하는 로그 내용에 따라 중복 컴포넌트가 있는 엔티티를 찾아 문제를 해결하세요.

모델을 통해 Entity 스폰
모델에 중복 컴포넌트가 있는지 확인하고, 삭제합니다. 자세한 내용은 Model에서 중복 컴포넌트 발생 내용을 참고하세요.

Model Extend로 중복된 컴포넌트 발생
여러 개의 모델을 부모-자식 관계로 만들 수 있습니다. 이때 자식 모델은 부모 모델의 Component를 상속 받기 때문에 중복 컴포넌트가 발생할 수 있습니다. Build Console 창에 나타난 로그 메시지를 참고해 컴포넌트를 삭제합니다. 두 가지 경우에서 자주 중복 컴포넌트가 발생합니다.

완전히 동일한 Component가 추가된 경우
부모 모델과 자식 모델에서 모두에서 동일한 컴포넌트를 추가해 중복 컴포넌트가 발생한 경우입니다. 월드 동작에 맞게 부모, 자식 모델 중 중복된 컴포넌트를 제거하면 됩니다.
부모 모델에서 컴포넌트를 지운다면, 자식 모델의 컴포넌트 중 하나가 지워집니다. 이때 자식 모델에 남은 컴포넌트 값이 초기화될 수 있음을 염두에 두시길 바랍니다.
5

같은 류의 Component가 추가된 경우
최상위 부모를 공유하는 컴포넌트들 동시에 추가했을 수 있습니다. 이 컴포넌트들은 최상위 부모가 같으므로 중복 컴포넌트로 구분됩니다. 이 경우 월드 동작에 맞추어 적절한 컴포넌트 하나를 남기도록 수정합니다.
6

필요 컴포넌트 추가로 중복 컴포넌트 발생
몇몇 컴포넌트는 사용 시 필수로 함께 사용해야 하는 필요 컴포넌트가 있습니다. 이 필요 컴포넌트는 특정 컴포넌트를 추가했을 때 자동으로 추가되고 있습니다. 이 동작으로 인해 연관 컴포넌트끼리의 추가 순서에 따라 중복 컴포넌트가 발생할 수 있습니다. 이 경우 추가한 컴포넌트를 삭제하고, 재추가해 수정합니다. 이 과정에서 로직 수정이 필요할 수 있습니다. 필요 컴포넌트가 있는 컴포넌트는 아래의 표에서 확인할 수 있습니다.

7

추가한 Component	필요 Component
AIChaseComponent	StateComponent
AIWanderComponent
DistanceJointComponent	PhysicsRigidbodyComponent, PhysicsColliderComponent
PrismaticJointComponent
PulleyJointComponent
RevoluteJointComponent
WeldJointComponent
WheelJointComponent
PhysicsRigidbodyComponent	PhysicsColliderComponent, TransformComponent
PhysicsColliderComponent	TransformComponent
KinematicbodyComponent
RigidbodyComponent
SideviewbodyComponent
