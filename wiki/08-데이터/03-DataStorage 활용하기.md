# DataStorage 활용하기

<!-- 출처: reference/TaskWiki.md · 문서 #143 -->


학습 과정 소개
이 가이드는 Data DB 저장 및 불러오기와 병행 학습을 권장합니다.
"Data DB 저장 및 불러오기"에서는 간편하게 데이터를 생성, 저장, 불러오는 기능 위주로 살펴보았습니다.
이번 가이드에서는 DataStorageService의 다양한 함수를 통해 데이터를 증가시키거나, 페이지를 가지고 오는 등 크리에이터의 목적에 맞게 데이터를 활용하는 방법을 알아봅시다.

참고 가이드
DataStorage 사용량 제한 알아보기

DataStorage 사용량 제한 활용하기

DataStorage 종류와 소개
DataStorage는 4가지 종류로 구분되며 범위, 용도에 따라 크리에이터가 선택해 사용할 수 있습니다. DataStorage는 독립적이므로 식별자를 구분하지 않습니다. 만약 종류가 다른 'Data A' 데이터 스토리지가 2개 존재한다면, 별개의 데이터 스토리지로 취급됩니다.
GlobalDataStorage, UserDataStorage, CreatorDataStorage는 string 타입의 값만 사용할 수 있고, SortableDataStorage는 int 타입의 값만 사용할 수 있으므로 사용 시 타입을 구분해야 합니다. CreatorDataStorage를 공동 제작에서 사용할 경우 공동 그룹 자체가 DataStorage를 가지고 있습니다.

Tip.
string 값이 아닌 다른 타입의 값을 사용하고 싶다면 _UtilLogic:TableToString()를 사용해 문자열로 변경해야 합니다.

4개의 데이터 스토리지마다 다양한 함수를 사용할 수 있습니다. 자세한 내용은 각각의 API Reference를 확인해보세요.

GlobalDataStorage
하나의 월드에서 사용되는 데이터 스토리지로 다른 월드와 데이터가 공유되지 않습니다. 데이터 스토리지를 가져올 때 이름을 지정할 수 있고, 여러 개의 데이터 스토리지를 만들어 가질 수 있습니다. string 타입의 값만 사용할 수 있는 것이 특징입니다. GlobalDataStorage API Reference를 참고하세요.

UserDataStorage
유저당 하나의 UserDataStorage를 가질 수 있습니다. 하나의 월드에서 사용되는 데이터 스토리지로 다른 월드와 데이터가 공유되지 않습니다. userId를 이용해 데이터 스토리지를 가져오며, string 타입의 값만 사용할 수 있는 것이 특징입니다. 이 데이터 스토리지는 유저의 접속 시간을 저장하거나, 현재 가지고 있는 월드 내의 아이템 정보 등을 불러올 때 사용할 수 있습니다. UserDataStorage API Reference를 참고하세요.

CreatorDataStorage
크리에이터당 하나의 CreatorDataStorage를 가질 수 있습니다. 다른 월드와 데이터를 공유할 수 있습니다. string 타입의 값만 사용할 수 있는 것이 특징입니다. CreatorDataStorage API Reference를 참고하세요.

SortableDataStorage
하나의 월드에서 사용되는 데이터 스토리지로 다른 월드와 데이터가 공유되지 않습니다. 여러 개의 데이터 스토리지를 만들어 가질 수 있고, 이름을 지정할 수 있습니다. int 타입의 값만 사용할 수 있고 정렬, 증가 함수를 활용할 수 있는 것이 특징입니다. SortableDataStorage API Reference를 참고하세요.

ErrorCode
DataStorage의 함수를 사용해 데이터를 저장, 삭제, 불러오기, 증가시키기, 순회 하기 등 다양한 데이터 관련 작업을 했을 때 해당 작업이 성공했는지 실패했는지를 에러 코드로 확인할 수 있습니다. 함수 요청이 성공했을 때의 에러 코드는 0입니다.
예를 들어, local errorCode, successKeys = globalDataStorage:BatchSetAndWait(keyValues) 와 같이 errorCode를 함께 작성해야 합니다.

ErrorCode	Error Name	설명
0	Ok	요청이 완료되었습니다.
1000000	Canceled	요청이 취소되었습니다.
1000001	InternalError	내부 에러가 발생했습니다.
1000002	NotFound	요소를 찾을 수 없어 에러가 발생했습니다.
1000003	BadRequest	올바르지 않은 요청으로 에러가 발생했습니다.
1000004	TimedOut	요청이 너무 오래 걸려 에러가 발생했습니다.
1000005	ResourceExhausted	호출 횟수가 한도를 초과해 에러가 발생했습니다.
1000006	PartialFailure	일부 요청 실패로 에러가 발생했습니다.
2000000	UpdateApiFailed	Update 요청 실패로 에러가 발생했습니다.
2147483647	Unknown	알 수 없는 에러가 발생했습니다.
Version
값이 가진 버전으로 Version을 활용해 원하는 시점의 값을 가져오거나, 롤백할 수 있습니다. 버전은 크리에이터가 명시적으로 지정할 수 있으며, 명시된 버전이 처음 생성되는 시점의 시간에 따라 우선순위가 정해집니다. Version은 명시하지 않을 경우 기본 버전으로 동작합니다. 이전에 저장된 버전이 하나라도 존재하는 경우에는 가장 마지막에 저장된 버전으로 동작합니다. 예를 들어, A 버전을 추가한 뒤, B 버전을 추가했는데 A 버전을 다시 추가한다면 최신 버전은 B 버전이 됩니다. 이미 A 버전은 생성된 이력이 남아있기 때문입니다.

Tag
Tag는 추가 식별자로 목록을 가져올 때 사용합니다. 태그를 사용해 원하는 그룹의 값을 선택 적으로 가져올 수도 있습니다. 태그 값은 지정하지 않을 수도 있지만, 이 경우 지정하지 않은 값에 대한 목록을 받을 수 없습니다.
태그는 그룹을 분리하지 않기 때문에 AKey 키값에 TagA 태그 값을 저장 한 뒤, AKey 키 값에 TagB 태그 값을 저장하면 태그는 TagB로 덮어써집니다.

DataStorageKeyInfo
DataStorageKeyInfo는 데이터에 더 많은 정보를 포함시키기 위한 객체입니다. DataStorageKeyInfo는 Key, Tag, Version을 지정할 수 있습니다.

Storage Item
Item 접미사가 붙은 객체는 두 가지로 분류해 사용합니다.
DataStorageItem은 GlobalDataStorage, UserDataStorage, CreatorDataStorage에 저장된 데이터를 뜻합니다. KeyInfo와 Value가 포함되어 있으며 Value의 타입은 string입니다.
SortableDataStoragePages은 SortableDataStorage에 저장된 데이터를 뜻합니다. KeyInfo와 Value가 포함되어 있으며 Value의 타입은 int입니다.

Storage Pages
GlobalDataStoragePages, SortableDataStoragePages, UserDataStoragePages, DataStorageItemPages, SortableDataStorageItemPages, DataStorageVersionPages는 DataStorage와 관련된 정보를 조회하기 위한 객체입니다. 모든 Pages 객체는 IsLastPages 프로퍼티와 GetCurrentPageDatas(), MoveToNextPageAndWait() 함수를 제공합니다. 두 함수를 사용해 데이터 목록을 가져오거나, 다음 페이지로 이동시킬 수 있습니다. 자세한 내용은 각각의 API Reference를 참고하세요.

활용 예시
데이터 스토리지는 주로 DataStorageService를 함께 사용합니다. DataStorageService는 여러 데이터 스토리지에 접근하는 함수들을 제공합니다. 데이터를 저장, 삭제, 불러오기, 조회하기 등 데이터를 다양하게 활용할 수 있습니다. 데이터를 활용하는 함수는 데이터 스토리지 종류에 맞는 것으로 사용해야합니다.

데이터 저장하기
데이터를 저장하기 위해선 데이터 스토리지의 타입(종류)을 명확하게 구분해 사용해야 합니다. 데이터 스토리지의 타입마다 데이터를 저장하는 값의 타입이 다르기 때문입니다. Global, User, Creator 데이터 스토리지는 값을 문자열로만 저장할 수 있고, Sortable 데이터 스토리지는 값을 정수로만 저장할 수 있습니다. 예를 들어, "globalDS" 데이터 스토리지에 문자열 Grade로 A 값을 저장하고 "globalDS"라는 이름의 GlobalDataStorage에서 "Grade"라는 이름의 키 값을 통해 값을 가져올 때 "A" 라는 값이 반환됩니다.

GlobalDataStorage
[server only]
void SaveDataStorage()
{
    local globalDataStorage = _DataStorageService:GetGlobalDataStorage("globalDS")
    globalDataStorage:SetAndWait("Grade", "A")
}
SortableDataStorage
GetSortableDataStorage는 다른 타입을 사용하지만, 저장하는 방법은 위의 설명과 동일합니다.

[server only]
void SaveDataStorage()
{
    local sortableDataStorage = _DataStorageService:GetSortableDataStorage("sortableDS")
    sortableDataStorage:SetAndWait("Score", 90)
}
더 많은 정보로 데이터 저장하기
DataStorage에 키 값과 더불어 Tag, Version을 지정해서 저장할 수 있습니다. 새로운 두 값을 저장하기 위해선 DataStorageKeyInfo를 활용해야 합니다. DataStorageKeyInfo("key", "Tag", "Version1")처럼 매개 변수로 key, Tag, Version을 사용할 수 있습니다. 만약 DataStorageKeyInfo를 Tag, Version 없이 사용한다면, SetAndWait, SetAsync류 함수를 사용해 데이터를 저장한 것과 동일합니다. 또한 SetByInfoAndWait, SetByInfoAsync 함수를 활용해 DataStorageKeyInfo를 활용한 저장이 가능합니다.

[server only]
void SaveDataStorage()
{
    local globalDataStorage = _DataStorageService:GetGlobalDataStorage("globalDS")
    local keyInfo = DataStorageKeyInfo("key", "Tag", "Version1") -- 이처럼 생성 시 각 값을 지정하거나, 빈 생성자로 생성 후 원하는 값만 채울 수도 있습니다.
    keyInfo = DataStorageKeyInfo()
    keyInfo.Key = "Key"
    keyInfo.Version = "Version1"
     
    globalDataStorage:SetByInfoAndWait(keyInfo, "Value")
}
데이터 불러오기
저장한 데이터를 불러올 때 데이터 스토리지 종류에 따라 GetGlobalDataStorage, GetUserDataStorage, GetCreatorStorage, GetSortableDataStorage를 활용합니다. 데이터를 가져오는 함수들은 Server Only이므로, 데이터 불러오기는 서버 공간에서 하는 것이 좋습니다.

GlobalDataStorage
GlobalDataStorage를 불러올 때는 반드시 이름을 지정해야 합니다. 크리에이터에 따라 종류가 다른 동명의 데이터 스토리지가 존재할 수 있기 때문입니다.

[server only]
void getDataStorage()
{
    local globalDataStorage = _DataStorageService:GetGlobalDataStorage("globalData")
}
UserDataStorage
UserDataStorage는 유저마다 가지는 고유한 데이터이므로, userId를 매개 변수로 넣어 데이터를 불러올 수 있습니다. 유저가 가진 데이터를 불러오는 것이므로 아래의 코드는 DefaultPlayer에 추가해야 합니다.

[server only]
void getDataStorage()
{
    local userId = self.Entity.Name
    local userDS = _DataStorageService:GetUserDataStorage(userId)
}
CreatorDataStorage
크리에이터당 하나의 데이터 스토리지를 가지고 있으므로 key를 지정하지 않아도 데이터를 불러올 수 있습니다.

[server only]
void getDataStorage()
{
    local creatorDS = _DataStorageService:GetCreatorDataStorage()
}
SortableDataStorage
[server only]
void getDataStorage()
{
    local sortableDS = _DataStorageService:GetSortableDataStorage("sortableDS")
}
데이터 가져오기
데이터를 가져올 때는 GetAndWait, GetAsync 함수를 사용합니다. GlobalDataStorage, UserDataStorage, CreatorDataStorage는 문자열 타입의 값만 가져올 수 있습니다.
만약 데이터를 저장할 때 _UtilLogic:TableToString() 함수를 사용해 데이터를 문자열로 변환했다면, 데이터를 가져올 때는 _UtilLogic:StringToTable() 함수를 사용해 기존 타입으로 변환하여 사용할 수 있습니다. SortableDataStorage는 정수 타입의 값만 가져올 수 있습니다.

Tip.
Async와 AndWait의 구분
DataStorageService의 함수 앞에 붙은 두 접미사로 해당 함수가 비동기, 동기로 수행되는지 알 수 있습니다.
Async는 비동기로 수행되며, 함수의 작업이 완료될 때 callbackFunction 매개 변수로 전달된 함수가 호출됩니다.
AndWait은 동기로 수행되며, 함수의 작업이 완료될 때까지 스크립트 실행을 중단합니다.

이름이 'globalDS' GlobalDataStorage를 'Grade'라는 이름의 키 값을 사용해 값을 가져오는 예제입니다.

local globalDataStorage = _DataStorageService:GetGlobalDataStorage("globalDS")
local errorCode, grade = globalDataStorage:GetAndWait("Grade") -- 이전에 저장된 "A" 값 반환
더 많은 정보로 데이터 가져오기
DataStorage의 값을 가져올 때 Version을 지정해 특정 버전의 값을 가져올 수 있습니다. 일반 데이터 가져오기와 달리 더 많은 정보로 값을 가져오려면 DataStorageKeyInfo로 객체를 생성한 뒤, 해당 객체를 인수로 지정해야 합니다.
DataStorageKeyInfo는 Key, Tag, Version 값을 지정할 수 있습니다. 데이터를 가져올 때는 Tag 값은 지정되어 있더라도 사용하지 않고, 동작에 영향을 끼치지 않습니다. Version을 지정하지 않고, DataStorageKeyInfo를 사용하면 GetAndWait, GetAsync 함수를 사용해 값을 가져온 것과 동일하게 동작하며 가장 마지막에 저장된 버전(최신 버전)의 값을 가져오게 됩니다.
GetByInfoAndWait, GetByInfoAsync 함수를 사용해 DataStorageKeyInfo를 활용한 가져오기가 가능합니다.

local globalDataStorage = _DataStorageService:GetGlobalDataStorage("globalDS")
local setterKeyInfo = DataStorageKeyInfo()
setterKeyInfo.Key = "Key"
setterKeyInfo.Version = "Version1"
globalDataStorage:SetByInfoAndWait(setterKeyInfo, "Value1")
 
setterKeyInfo.Key = "Key"
setterKeyInfo.Version = "Version2"
globalDataStorage:SetByInfoAndWait(setterKeyInfo, "Value2")
 
local errorCode, value = globalDataStorage:GetAndWait("Key")
log(value) -- Value2 기본적으로 최신 버전의 값을 가져옵니다.
 
local getterKeyInfo = DataStorageKeyInfo()
getterKeyInfo.Key = "Key"
getterKeyInfo.Version = "Version1"
 
local errorCode, value = globalDataStorage:GetByInfoAndWait(getterKeyInfo)
log(value) -- Value1 원하는 특정 버전을 지정하여 가져올 수 있습니다.
데이터 증가시키기
SortableDataStorage는 IncreaseAndWait, IncreaseAsync 함수를 활용해 값을 증가시킬 수 있습니다. 각 함수의 delta 입력 값만큼 해당 매개 변수의 값이 증가하거나 감소합니다. 매개 변수로 들어온 값이 양수일 때는 증가, 음수일 때는 감소합니다.
만약, 증가시키고자 하는 값이 DataStorage에 존재하지 않는다면 기본값 0으로 저장하고 delta만큼 증가하게 됩니다. IncreaseAndWait 및 IncreaseAsync 함수는 에러 코드와 증가된 후의 값을 제공합니다.

DataStorage에 저장되지 않은 값을 IncreaseAndWait 함수로 생성, 증가하는 예제입니다.

local sortableDataStorage = _DataStorageService:GetSortableDataStorage("sortableDS")
 
-- sortableDataStorage에 "Key"는 저장된 이력이 없음을 가정합니다.
local errorCode, value = sortableDataStorage:IncreaseAndWait("Key", 5)
log(value) --  5, 기본 값인 0으로 생성 후 delta만큼 증가했기 때문에 5를 반환합니다.
 
local errorCode, value = sortableDataStorage:IncreaseAndWait("Key", 10)
log(value) -- 15, 기존에 저장된 값 5에 delta만큼 증가했기 때문에 15를 반환합니다.
데이터 제거하기
DeleteAndWait 또는 DeleteAsync 함수로 데이터를 제거할 수 있습니다.

이름이 "globalDS"인 GlobalDataStorage에서 "Grade"라는 이름의 키 값에 해당하는 값을 제거하는 예제입니다.

local globalDataStorage = _DataStorageService:GetGlobalDataStorage("globalDS")
globalDataStorage:DeleteAndWait("Grade")
local errorCode, grade = globalDataStorage:GetAndWait("Grade") -- "Grade"는 제거되었기 때문에 유효한 값을 얻을 수 없습니다.
데이터 목록 가져오기
DataStorageService로 값이 저장된 DataStorage 목록을 조회할 수 있습니다. 목록을 조회하는 함수를 호출하면 해당 DataStorage의 목록을 조회할 수 있는 GlobalDataStoragePages, SortableDataStoragePages, UserDataStoragePages를 받을 수 있습니다. 다만 CreatorDataStorage의 경우 하나만 존재하기 때문에 목록을 가져오는 함수가 없습니다. 목록을 가져오는 함수는 AndWait과 Async를 제공하며 목적에 따라 원하는 형태를 사용할 수 있습니다.

local errorCode, globalDataStoragePages = _DataStorageService:GetGlobalDataStoragePagesAndWait()
local errorCode, sortableDataStoragePages = _DataStorageService:GetSortableDataStoragePagesAndWait()
local errorCode, userDataStoragePages = _DataStorageService:GetUserDataStoragePagesAndWait()
pages 순회하기
DataStorage 목록 또는 데이터 목록을 받을 때 페이지 단위로 목록을 조회할 수 있는 객체인 Pages 형태로 값을 받습니다.

local errorCode, globalDataStoragePages = _DataStorageService:GetGlobalDataStoragePagesAndWait()
 
while true do
 
    local globalDataStorages = globalDataStoragePages:GetCurrentPageDatas() --GetCurrentPageDatas()로 현재 페이지의 목록을 가져올 수 있습니다.
 
    for _, globalDataStorage in pairs(globalDataStorages) do
        log(globalDataStorage.Name)
    end
     
    if globalDataStoragePages.IsLastPage == true then --IsLastPage 프로퍼티를 통해 현재 페이지가 마지막 페이지인지 확인할 수 있습니다.
        break
    end
    globalDataStoragePages:MoveToNextPageAndWait() --MoveToNextPageAndWait()로 다음 페이지로 넘어갈 수 있습니다.
end
일괄 요청하기
Batch 접두사인 함수를 활용해 데이터 저장하기, 불러오기, 제거하기를 일괄 요청할 수 있습니다. BatchSetAndWait() 및 BatchSetAsync() 함수는 에러 코드와 요청이 성공한 값의 키 테이블을 제공합니다.
여러 개의 값을 저장하거나 가져오거나 제거할 때는 Batch 접두사가 붙은 함수를 활용해야 빠르게 많은 요청을 수행할 수 있습니다. Batch 접두사인 함수는 요청된 작업들 중 일부만 성공하는 상황이 발생할 수 있습니다. 그러므로 결괏값을 확인해 성공하지 않은 작업이 있다면 적절한 오류 처리가 필요합니다.

다음은 일괄적으로 데이터를 저장하는 예제입니다.

local globalDataStorage = _DataStorageService:GetGlobalDataStorage("globalDS")
local keyValues = {}
keyValues["key1"] = "value1"
keyValues["key2"] = "value2"
keyValues["key3"] = "value3"
 
local errorCode, successKeys = globalDataStorage:BatchSetAndWait(keyValues)
원자적으로 일괄 요청하기
Transact 접두사인 함수를 활용해 데이터 저장하기, 불러오기, 제거하기를 원자적으로 일괄 요청할 수 있습니다. 만약 함수 호출에 포함된 모든 작업 중 하나라도 실패한다면, 함수 호출은 실패합니다. 한 번에 Key를 최대 20개까지 조작할 수 있습니다.
한 번에 전달된 요청들이 모두 성공하지 않으면 모두 실패 처리하고, 요청 이전의 데이터를 유지합니다. 그러므로 오류 처리 관련 코드를 간소화할 수 있습니다. 그러나 트랜잭션 보장을 위해 내부적으로 복잡한 처리 과정이 진행됩니다. credit 또한 Batch 함수에 비해 2배로 소모됩니다.

더 알아보기
트랜잭션(Transaction)은 원자적으로 처리되어야 하는 작업의 단위를 의미합니다.

다음은 모든 작업이 성공할 경우 일괄적으로 데이터를 저장하는 예제입니다.

local transactDs = _DataStorageService:GetGlobalDataStorage(self.TransactionTestDsName)
local t1 = {}
t1["key1-1"] = "value1"
t1["key1-2"] = "value2"
t1["key1-3"] = "value3"
​
local t2 = {}
t2["key2-1"] = "value1"
t2["key2-2"] = "value2"
t2["key2-3"] = "value3"
​
local callback = function (code, keys)
    if code ~= 0 then
        error("! error. TransactSetAsync. code:"..tostring(code))
        return
    end
     
    for i, key in ipairs(keys)  do
        log("["..tostring(i).."] "..key)       
    end
end
​
-- ~AndWait
local code1, resultKeys1 = transactDs:TransactSetAndWait(t1)
for i, key in ipairs(resultKeys1) do
    log("["..tostring(i).."] "..key)
end
​
-- ~Async
transactDs:TransactSetAsync(t2, callback)
다음은 모든 작업이 성공할 경우 일괄적으로 데이터를 제거하는 예제입니다.

log("# Test_DataStorage_TransactDelete")
local transactDs = _DataStorageService:GetGlobalDataStorage(self.TransactionTestDsName)
local keys1 = {"key1-1", "key1-2", "key1-3"}
local keys2 = {"key2-1", "key2-2", "key2-3"}
local code1, resultKeys1 = transactDs:TransactDeleteAndWait(keys1)
log("code1: "..tostring(code1))
for _, item in pairs(resultKeys1) do
    log("- deleted key: "..item)
end
​
local callback = function (code, keys)
    if code ~= 0 then
        error("! error. TransactDeleteAsync. code:"..tostring(code))
        return
    end
     
    for i, key in ipairs(keys)  do
        log("- deleted key: "..key)
    end
end
​
transactDs:TransactDeleteAsync(keys2, callback)
데이터 정렬하기
SortableDataStorage는 GetSortedAndWait 및 GetSortedAsync 함수로 데이터를 정렬할 수 있습니다. 데이터를 정렬하여 가져올 때 오름차순으로 정렬할지 내림차순으로 정렬할지 지정할 수 있으며 최솟값과 최댓값을 지정하여 원하는 범위의 값 목록을 정렬하여 가져올 수 있습니다.

SortableDataStorage에 저장된 데이터를 정렬해 가져오는 예제입니다.

local sortableDataStorage = _DataStorageService:GetSortableDataStorage("sortableDS")
 
-- 최솟값 0, 최댓값 100 사이에 있는 값들만 정렬하여 가져옵니다.
local errorCode, pages = sortableDataStorage:GetSortedAndWait(SortDirection.Ascending, 0, 100)
 
while true do
 
    local items = pages:GetCurrentPageDatas()
    for _, item in pairs(items) do
        log(item.KeyInfo.Key)
        log(item.Value)
    end
 
    if pages.IsLastPage == true then
        break
    end
    pages:MoveToNextPageAndWait()
end
버전 관리하기
DataStorage의 값을 저장할 때 DataStorageKeyInfo를 활용하여 Version을 지정했다면 버전 관리를 할 수 있습니다. 기존 버전을 덮어쓰는 대신 새로운 버전을 만들 수 있고 최신 버전이 유효하지 않은 경우 과거 버전으로 덮어 씌울 수도 있습니다. 버전 목록을 반환하는 함수로 존재하는 버전의 목록을 확인할 수 있습니다.

새로운 version 만들기
local globalDataStorage = _DataStorageService:GetGlobalDataStorage("globalDS")
local keyInfo = DataStorageKeyInfo()
keyInfo.Key = "Key"
keyInfo.Version = "Version1"
 
globalDataStorage:SetByInfoAndWait(keyInfo, "Value")
 
-- 기존 버전의 "Value" 값을 덮어 쓰는 대신 새로운 버전을 만들어 저장합니다.
keyInfo.Key = "Key"
keyInfo.Version = "Version2"
globalDataStorage:SetByInfoAndWait(keyInfo, "Value2")
 
-- "Value" 값은 덮어 씌워진게 아니기 때문에 아직 유효하며 Version1을 지정하여 "Value" 값을 가져올 수 있습니다.
keyInfo.Key = "Key"
keyInfo.Version = "Version1"
local errorCode, value = globalDataStorage:GetByInfoAndWait(keyInfo)
과거 version으로 돌아가기
local globalDataStorage = _DataStorageService:GetGlobalDataStorage("globalDS")
keyInfo = DataStorageKeyInfo()
keyInfo.Key = "Key"
keyInfo.Version = "Version1"
 
globalDataStorage:SetByInfoAndWait(keyInfo, "Value")
 
-- 기존 버전의 "Value" 값을 덮어 쓰는 대신 새로운 버전을 만들어 저장합니다.
keyInfo.Key = "Key"
keyInfo.Version = "Version2"
globalDataStorage:SetByInfoAndWait(keyInfo, "Value2")
 
-- "Value" 값은 덮어 씌워진게 아니기 때문에 아직 유효하며 Version1을 지정하여 "Value" 값을 가져올 수 있습니다.
keyInfo.Key = "Key"
keyInfo.Version = "Version1"
local errorCode, oldValue = globalDataStorage:GetByInfoAndWait(keyInfo)
 
-- 과거 버전의 값을 가져와 최신 버전에 덮어씁니다. 이후 GetAndWait 함수를 호출하면 "Value2" 값이 아닌 "Value" 값이 반환됩니다.
keyInfo.Key = "Key"
keyInfo.Version = "Version2"
globalDataStorage:SetByInfoAndWait(keyInfo, oldValue)
version 목록 가져오기
local globalDataStorage = _DataStorageService:GetGlobalDataStorage("globalDS")
 
-- 4월 20일부터 5월 20일까지의 버전 목록만 가져옵니다.
local minDate = DateTime(2022, 4, 20)
local maxDate = DateTime(2022, 5, 20)
 
local errorCode, pages = globalDataStorage:GetVersionsAndWait("Key", SortDirection.Ascending, minDate, maxDate)
 
while true do
 
    local versions = pages:GetCurrentPageDatas()
 
    for _, versionInfo in pairs(versions) do
        log(versionInfo.CreateTime) -- 생성 시점의 시간을 알 수 있습니다.
        log(versionInfo.Version) -- 사용자가 지정한 Version을 알 수 있습니다.
    end
 
    if pages.IsLastPage == true then
        break
    end
    pages:MoveToNextPageAndWait()
end
