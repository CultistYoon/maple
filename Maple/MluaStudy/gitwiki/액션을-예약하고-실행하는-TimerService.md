# 액션을 예약하고 실행하는 TimerService

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「액션을 예약하고 실행하는 TimerService」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 05 게임로직시스템 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
몬스터가 등장하고 몇 초 뒤 공격을 시작하거나, 몬스터가 죽고 1초 뒤 아이템을 떨어뜨리는 것과 같은 어떤 일(액션)이 일어나는 타이밍을 제어해야 할 때가 있습니다.
TimerService를 활용해 쉽고 효율적으로 액션이 일어나는 타이밍을 제어할 수 있습니다. TimerService가 제공하는 기능과 활용법을 알아보겠습니다.

TimerService 소개
TimerService는 원하는 순간에 어떤 액션을 실행하도록 예약하는 편의 기능을 제공합니다. Timer Service를 사용하지 않고 몬스터가 사망하면 보상 아이템이 떨어지는 상황을 만드는 방법 알아봅시다.

Timeservice01

몬스터가 죽고 3초 후에 아이템이 등장하는 상황을 만들기 위해서는 아래와 같이 긴 스크립트를 작성해야 합니다. 몬스터가 죽을 때마다 프레임별로 시간을 확인하고, 3초가 지나면 아이템이 등장하도록 해야 하기 때문입니다.

Property:
[None]
table DropItemList = {}

Method:
[server only]
void OnBeginPlay()
{
    self.DropItemList = {}
}

[server only]
void OnUpdate(number delta)
{
    for i, dropInfo in pairs(self.DropItemList) do
    	if dropInfo.dropTime < os.clock() then
    		continue
    	end
    	
    	self:DropItem(dropInfo.dropItemArr, dropInfo.itemDropPosition)
    end
}

[sever only]
void OnMonsterDestroy(Entity monsterEntity)
{
    local monsterInfo = monsterEntity.MonsterInfo
    local dropItemArr = monsterInfo.dropItemArr
    local itemDropPosition = monsterEntity.TransformComponent.Position
    
    table.insert(self.DropItemList, {["driopItemArr"] = dropItemArr, ["dropTime"] = os.clock() + 3, ["itemDropPosition"] = itemDropPosition})
    
    _EntityService:Destroy(monsterEntity)
}

[server only]
void DropItem(SyncTable<string> itemArr, Vector3 dropPosition)
{
    for i , itemId in pairs(itemArr) do
    	self:SpawnItem(itemId, dropPosition)
    end
}
TimerService를 활용하면 보다 간결하게 구현할 수 있습니다. 아이템 드롭을 구현한 CallBack 함수를 TimerService의 SetTimer() 함수로 넘겨주고, 몇 초 뒤에 실행할 것인지 설정합니다. 몇 개의 함수와 수십 줄의 코드로 구현해야 할 기능을 CallBack 함수와 SetTimer() 함수를 호출해 쉽고 간단하게 구현할 수 있습니다.

Method:
[server only]
void OnMonsterDestroy(Entity monsterEntity)
{
    local monsterInfo = monsterEntity.MonsterInfo
    local dropItemArr = monsterInfo.dropItemArr
    local itemDropPosition = monsterEntity.TransformComponent.Position
    
    local dropItem = function()
    	self:DropItem(dropItemArr, itemDropPosition)
    end
    
    _TimerService:SetTimer(self, dropItem, 3, false)
    _EntityService:Destroy(monsterEntity)
}

[server only]
void DropItem(SyncTable<string> itemArr, Vector3 dropPosition)
{
    for i, itemId in pairs(itemArr) do
    	self:SpawnItem(itemId,dropPosition)
    end
}
SetTimer 활용
SetTimer()는 예약 함수입니다. 특정 시점에 수행할 액션을 예약할 수 있고, 액션 반복 수행 여부와 반복 주기를 설정할 수 있습니다. 예약한 액션 반복 여부에 따라 매개 변수의 의미와 쓰임새가 달라집니다. SetTimer()는 예약 성공 시 integer 타입의 타이머의 id를 반환하고, 예약 실패 시 0을 반환합니다. 매개 변수는 다음과 같습니다.

타입	매개 변수	설명
IScriptable	scriptable	예약할 액션의 소유자를 넘겨줍니다. 액션의 소유자는 로직, 컴포넌트가 될 수 있으며 일반적으로 SetTimer()를 호출한 컴포넌트 자신을 넘겨줍니다.
func	callback	몇 초 뒤 수행할 액션을 CallBack 함수로 넘겨줍니다.
float	intervalSeconds	
isRepeat 값이 true일 경우: CallBack 함수를 최초 1회 실행한 후 몇 초 뒤에 재실행할 것인지를 설정합니다.
isRepeat 값이 false일 경우: SetTimer()가 호출된 후 몇 초 뒤에 CallBack 함수를 실행할 것인지를 설정합니다.
boolean	isRepeat	CallBack 함수를 1회만 실행할 것인지, 반복적으로 실행할 것인지를 설정합니다.
true: 반복 실행
false: 1회 실행
float	startDelaySeconds	함수 실행 후 몇 초 뒤에 CallBack 함수를 실행할지 설정합니다. isRepeat 값이 true 경우 유효합니다.
주의!
scriptable 매개 변수에 컴포넌트를 전달하는 경우 callback 실행이 컴포넌트의 EnableInHierarchy에 영향을 받습니다.

액션 1회 실행
SetTimer가 호출될 때 "SetTimer!"라는 문자열과 함께 해당 코드가 실행된 시간을 출력합니다. 3초 뒤 SetTimer()로 넘긴 CallBack 함수가 호출될 때 "CallBack!"이라는 문자열과 함께 코드가 실행된 시간을 1회 출력합니다.
Timeservice04

예시 코드는 다음과 같습니다. CallBack 함수를 넘겨주면서 intervalSeconds을 3초로 설정합니다. 1회만 실행하므로 isRepeat은 false로 설정하고, startDelaySeconds는 무시합니다.

[server only]
void OnBeginPlay()
{
    local callBack = function()
        log("CallBack! : "..tostring(os.date()))
    end
 
    log("SetTimer! : "..tostring(os.date()))
    _TimerService:SetTimer(self, callBack, 3, false)
}
시작 Tool_Play을 눌러 테스트를 진행합니다. 콘솔 창에 각 문자열과 코드가 실행된 시간을 확인하여 SetTimer()가 호출된 3초 뒤 CallBack 함수가 실행되는 것을 확인합니다. 39초에 처음 호출되고, 다음 함수 실행이 42초로 3초 간격을 확인할 수 있습니다.

TimeService06

액션 반복 실행
isRepeat을 true로 변경해 반복 실행하게 만듭니다. SetTimer()가 호출될 때 "SetTimer!"라는 문자열과 함께 해당 코드가 실행된 시간을 출력합니다.

TImeService07

예시 코드는 다음과 같습니다. 3초마다 SetTimer()로 넘긴 CallBack 함수가 호출될 때 "CallBack!"이라는 문자열과 함께 코드가 실행된 시간을 출력합니다.

Method:
[server only]
void OnBeginPlay()
{
    local callBack = function()
        log("CallBack! : "..tostring(os.date()))
    end
     
    log("SetTimer! :"..tostring(os.date()))
    _TimerService:SetTimer(self, callBack, 3, true)
}
시작 Tool_Play을 눌러 테스트합니다. 콘솔 창의 출력 시간이 3초씩 증가했는지 확인합니다. 1회 실행 때와 달리, "SetTimer!" 와 "CallBack!" 문자열이 처음 출력된 시간이 같습니다. SetTimer()를 반복 설정하면 intervalSeconds의 의미가 변경되기 때문입니다. 1회 실행일 때 intervalSeconds의 의미는 SetTimer()가 실행된 다음 몇 초 뒤에 CallBack 함수를 실행할 것인지를 의미합니다. 반복 실행일 때는 CallBack 함수는 최초 실행 후 몇 초 뒤에 다시 실행할 것 인지를 의미합니다. 그러므로 SetTimer()와 CallBack 함수가 동시에 실행되고, CallBack 함수가 3초마다 재실행됩니다. CallBack 함수를 몇 초마다 실행할 것인지가 중요하다면 intervalSeconds 값만 조절합니다.
[object Object]
SetTimer()가 호출된 후 몇 초 뒤에 CallBack 함수를 최초로 호출할 것인가를 설정하고자 한다면, SetTimer()의 마지막 매개 변수인 startDelaySeconds에 값을 입력합니다. SetTimer()가 호출된 후 2초 뒤에 CallBack 함수가 최초로 실행되고, 이후 3초 간격으로 CallBack 함수가 실행됩니다. 다음은 startDelaySeconds 값을 추가한 예시입니다.

[server only]
void OnBeginPlay()
{
    local callBack = function()
        log("CallBack! : "..tostring(os.date()))
    end
 
    log("SetTimer! : "..tostring(os.date()))
    _TimerService:SetTimer(self, callBack, 3, true, 2)
}
시작 Tool_Play을 눌러 테스트를 진행합니다. 콘솔에 의도대로 시간이 출력되는지 확인합니다. CallBack 함수가 SetTimer()가 처음 호출된 후 2초 뒤에 처음 실행되고, 다음부터 3초 간격으로 실행되었는지 확인합니다.
TimeService11

실행 예약 취소
SetTimer()를 통해 특정 액션을 수행하도록 예약을 만들었지만, 특정 조건에 의해 해당 예약을 취소해야 하는 경우가 빈번히 발생합니다.
게임 내에서 스위치를 On 했을 때 3초 후 문이 열리는 장치를 만들었다고 가정해 봅시다. 유저가 스위치를 On 상태로 만들었을 때 3초 뒤에 문이 열리게 됩니다. 문이 열리는 액션을 SetTimer()를 이용해 예약했기 때문입니다. 그러나 유저가 문이 열리기 전에 스위치를 Off 상태로 만든다면 SetTimer()의 예약을 취소해 Off일 때 문이 열리지 않게 만들어야 합니다.

TimerService12

다음은 반복 실행 예제에 SetTimer()가 호출된 후, 10초 뒤 실행을 취소하는 SetTimer()를 추가한 스크립트입니다.

Method:
[server only]
void OnBeginPlay()
{
    local callBack = function()
        log("CallBack! :"..tostring(os.date))
    end
    
    log("SetTimer! :"..tostring(os.date()))
    local timerId = _TimerService:SetTimer(self, callBack, 3, true, 2)
    if timerId == 0 then
        return
    end
    
    local cancelCallBack = function()
        _TimerService:ClearTimer(timerId)
    end
    
    _TimerService:SetTimer(self, cancelCallBack, 10, false)
}
시작 Tool_Play을 눌러 테스트합니다. SetTimer!가 처음 출력된 후 10초 후에는 로그가 더 이상 출력되지 않습니다.

Tip
첫 출력 시간은 46초이고, 마지막 출력 시간은 54초로 총 8초 동안의 로그만 나온 이유는 SetTimer() 실행 후 10초 뒤에 ClearTimer()가 실행됐기 때문입니다.
CallBack은 SetTimer() 실행 후 2초 뒤에 처음 실행되어, 3초마다 반복 실행되고 있습니다. 54초 이후 다음 CallBack 실행은 57초이지만, 56초에 CallBack을 취소시키므로 57초에 실행할 CallBack이 없습니다. 그러므로 로그는 첫 실행 후 8초 이후부터는 로그가 찍히지 않습니다.

TImeService14

SetTimer의 파생 기능
사용 목적에 따라 SetTimerOnce() 와 SetTimerRepeat()를 사용해 액션 예약과 수행 기능을 나누어 사용할 수 있습니다. SetTimerOnce()는 1회 액션 예약 시 사용하고, SetTimerRepeat()은 반복 액션 수행 시 사용합니다. 기능이 분리된 만큼 전달할 매개 변수 개수도 적어 SetTimer()에 비해 간편하게 사용할 수 있습니다.

SetTimerOnce
SetTimerOnce()는 SetTimer()의 isRepeat를 false로 설정한 것과 동일하게 작동합니다. 예약 성공 시 integer 타입의 타이머의 id를 반환하고, 예약 실패 시 0을 반환합니다. 매개 변수는 다음과 같습니다.

타입	매개 변수	설명
func	callback	몇 초 뒤 수행할 액션을 CallBack 형태로 넘겨줍니다.
float	delaySeconds	액션을 예약한 뒤 몇 초 후에 액션을 실행할 것인지를 설정합니다.
[server only]
void OnBeginPlay()
{
    local callBack = function()
        log("CallBack! : "..tostring(os.date()))
    end
 
    log("SetTimer! : "..tostring(os.date()))
    _TimerService:SetTimerOnce(callBack, 3)
}
시작 Tool_Play을 눌러 테스트합니다. SetTimerOnce()가 호출되고 3초 뒤 액션이 실행된 것을 확인합니다.
TimeService16

주의!
_TimerService:SetTimerOnce(self.Method,1)와 같이 callback 매개 변수에 컴포넌트의 메서드를 직접 전달하는 경우 callback 실행이 컴포넌트의 EnableInHierarchy에 영향을 받습니다.

SetTimerRepeat
SetTimerRepeat()는 반복 액션을 예약할 때 사용합니다. SetTimer()의 isRepeat를 true로 한 것과 동일합니다. 예약 성공 시 integer 타입의 타이머의 id를 반환하고, 예약 실패 시 0을 반환합니다. 매개 변수는 다음과 같습니다.

타입	매개 변수	설명
func	callback	반복 수행할 액션을 CallBack 형태로 넘겨줍니다.
float	intervalSeconds	몇 초마다 반복 수행할지를 설정합니다.
float	startDelaySeconds	액션을 예약한 다음 몇 초 뒤부터 반복 액션을 수행할지를 설정합니다.
[server only]
void OnBeginPlay()
{
    local callBack = function()
        log("CallBack! : "..tostring(os.date()))
    end
 
    log("SetTimer! : "..tostring(os.date()))
    _TimerService:SetTimerRepeat(callBack, 3, 2)
}
시작 Tool_Play을 눌러 테스트합니다. SetTimer()가 호출된 후 2초 뒤에 액션을 최초로 수행되고, 이후 3초 간격으로 액션을 반복 수행하는 것을 확인합니다.

TimeService18

주의!
_TimerService:SetTimerRepeat(self.Method, 1, 1)와 같이 callback 매개 변수에 컴포넌트의 메서드를 직접 전달하는 경우 callback 실행이 컴포넌트의 EnableInHierarchy에 영향을 받습니다.

예약 취소
SetTimerOnce()와 SetTimerRepeat()는 예약한 액션을 취소할 수 있습니다. 예약한 액션을 취소할 때는 ClearTimer() 함수를 활용합니다.
아래의 예제처럼 10초 뒤 액션 실행을 취소할 수 있습니다.

Method:
[server only]
void OnBeginPlay()
{
    local callBack = function()
         log("CallBack! :"..tostring(os.date()))
    end
    
    log("SetTimer! :"..tostring(os.date()))
    local timerId = _TimerService:SetTimerRepeat(callBack, 3, 2)
    if timerId == 0 then
        return
    end
    
    local cancelCallBack = function()
        _TimerService:ClearTimer(timerId)
    end
    
    _TimerService:SetTimerOnce(cancelCallBack, 10)
}
처음 로그가 출력된 시점으로부터 10초 뒤부터 로그가 더 이상 출력되지 않는 것을 확인할 수 있습니다.

TimeService20

유의 사항
반복 액션 예약을 사용할 때는 적절한 시기에 ClearTimer() 함수를 호출하 예약을 취소해야 합니다. 컴포넌트나 로직의 OnEndPlay 혹은 예약된 액션의 소유자가 파괴되는 시점에 ClearTimer() 함수를 호출하여 예약 취소하는 것을 권장합니다. 예약된 액션이 과도하게 누적될 경우 월드 성능이 하락할 수 있기 때문입니다.
만약 크리에이터가 ClearTimer() 함수를 호출하지 않았더라도 월드의 최적화를 위해 예약된 액션의 소유자가 파괴될 경우 내부에서 자동으로 ClearTimer() 함수를 시도합니다.

Property:
[None]
integer TimerId = 0

Method:
[server only]
void OnBeginPlay()
{
    local callBack = function()
        log("CallBack! :"..tostring(os.date()))
    end

    self.TimerId = _TimerService:SetTimerRepeat(callBack, 3)
}

[server only]
void OnEndPlay()
{
    if self.TimerId > 0 then
        _TimerService:ClearTimer(self.TimerId)
    end
}이벤트
Event System
Entity Event System
InputService를 활용한 입력과 액션
멀티 터치
