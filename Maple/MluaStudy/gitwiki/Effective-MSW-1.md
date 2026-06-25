# Effective MSW 1

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「Effective MSW 1」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 13 다양한기능들 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
메이플스토리 월드는 쉬운 코딩을 위해 다양한 편의 기능을 지원하고 있습니다. 대표적으로 간편한 실행 제어 설정 기능이 있습니다. 그러나 간단한 설정이 얽히며 복잡해질 수 있고, 잘못 설정하면 원하는 기능이 제대로 실행되지 않을 수도 있습니다. 때로는 월드가 매우 느려질 수도 있습니다.

이런 문제는 월드의 규모가 작거나 월드 제작 초창기에는 발견하기 어렵습니다. 하지만 월드의 규모가 커지고 완성도가 높아질수록 문제가 될 수 있습니다. 그러므로 제작 초기부터 모든 동작이 원활하고 효율적으로 진행되도록 구조를 고민하며 제작해야 합니다. 특히 흐름 제어와 최적화 문제를 늘 염두에 두어야 합니다.

이번 가이드에서는 월드 제작 시 놓치기 쉬운 개념들을 소개합니다.

isvalid() 사용
루아에서 nil 체크는 해당 대상이 있는지 없는지 확인할 때 사용합니다. 주로 루아의 테이블이나 메이플스토리 월드의 엔티티, 컴포넌트에서 사용합니다. 그러나 Native 객체에 접근할 때는 사용 제한이 필요할 수 있습니다.

아래와 같은 코드는 대부분 정상 동작하지만 일부 상황에서는 제대로 동작하지 않을 수 있습니다. 그 이유를 파악하려면 메이플스토리 월드 내의 동작 원리를 이해해야 합니다.

local targetEntity = _EntityService:GetEntity("a22396e1-6365-42d4-9cef-5924c223f7fa")
if targetEntity ~= nil then
	-- Do Something
end
예를 들어, 메이플스토리 월드에서 엔티티의 삭제 과정을 살펴봅시다.
위와 같이 작성한 코드에서 처리할 내용이 많아져 처리 지연이 발생한다면 크리에이터가 의도한 대로 동작하지 않을 것입니다. 실제 동작은 기대한 동작보다 더 많은 단계로 이루어져 있기 때문입니다.

기대한 동작: 삭제 요청 → nil

실제 동작: 삭제 요청 → 삭제 처리 대기 → 삭제 중 → 삭제 완료 → nil

바로 삭제되지 않는 이유는 처리해야 할 일과 그 과정 중에 해야 할 일이 끝난 뒤 엔티티가 삭제되기 때문입니다. 따라서 isvalid() 함수를 사용해 엔티티나 컴포넌트가 유효한지 검사해야 합니다.
isvalid() 함수는 실제 동작하는 일련의 행위가 어떤 상태인지 모두 체크하기 때문에 안전합니다. 또한 알 수 없는 동작의 유효성을 보장합니다. 그러므로 스크립트를 작성할 때 isvalid()를 적극적으로 활용하기 바랍니다.

isvalid() 함수를 사용하여 위에서 작성한 코드를 수정해 봅시다.

local targetEntity = _EntityService:GetEntity("a22396e1-6365-42d4-9cef-5924c223f7fa")
if isvalid(targetEntity) then
	-- Do Something
end
Wait 계열 함수 사용
wait(), _DataStorage:SetAndWait(), _DataStorage:GetAndWait() 등 함수 이름에 Wait가 붙은 것을 Wait 계열 함수라고 합니다. Wait 계열 함수는 매우 편리합니다. 실행 순서를 순차적으로 파악할 수 있고, 사용하기 간편하기 때문입니다. 그러나 편리하다는 이유로 남발하면 문제가 생길 수 있습니다.

wait의 사용
wait()는 보통 아래 예시 코드처럼 간단하게 사용합니다.

_UIToast:ShowMessage("Show Message")
wait(1)
_UIToast:ShowMessage("Show Delay Message")
하지만 wait()를 사용할 때는 주의해야 합니다. wait()는 말 그대로 행동을 '기다리고' 있기 때문에 여기저기에 마구 사용한다면 전체적인 흐름을 파악하기 어려워집니다. 또한, '대기'를 하므로 이후 작업이 진행되지 않는 문제도 있습니다.

아래 예시를 통해 '대기' 때문에 발생하는 문제점을 알아봅시다.

대기 이후 동작의 유효성을 보장할 수 없습니다.

local targetEntity = _EntityService:GetEntity("a22396e1-6365-42d4-9cef-5924c223f7fa")
targetEntity.TestComponent:ShowMessage()
wait(3)
targetEntity.TestComponent:ShowMessage()
wait(3) 뒤에 targetEntity와 targetEntity의 TestComponent는 유효성을 보장할 수 없습니다. 그 사이에 엔티티나 컴포넌트가 삭제되었을 수도 있기 때문입니다.


대기 동작이 여러 개 있을 경우 많은 시간이 소요됩니다.
캐릭터의 능력치를 DataStorage에서 받아오기 위해 wait 계열 함수를 사용한 코드입니다. 문제를 살펴봅시다.

local str = _DataStorageService:GetAndWait("MyStat", "STR")
local dex = _DataStorageService:GetAndWait("MyStat", "DEX")
local int = _DataStorageService:GetAndWait("MyStat", "INT")
local luck = _DataStorageService:GetAndWait("MyStat", "LUCK")
local hp = _DataStorageService:GetAndWait("MyStat", "HP")
local mp = _DataStorageService:GetAndWait("MyStat", "MP")
local sp = _DataStorageService:GetAndWait("MyStat", "SP")
처음 STR을 불러올 때는 문제가 없었을 수도 있습니다. 하지만 그 양이 늘어나면 문제가 발생합니다. DB에서 값을 가져오거나 리소스를 불러오는 행위는 특히 매우 오래 걸립니다. 만약 각각의 값을 받는데 걸리는 시간이 0.5초라면, 7개의 Stat을 모두 받아 오는데 3.5초가 소요됩니다.

요청 → 대기 → 수신 → 요청 → 대기 → 수신 ....을 반복하기 때문입니다.

이 3.5초 동안 해당 부분은 기다리는 중인데 만약 밑에서 뭔가 중요한 일을 하거나, 다른 컴포넌트에서 해당 부분에 접근하면 순서가 꼬이게 됩니다. 이를 해결하려면 우선 _DataStorageService:GetAsync를 사용할 수 있습니다. 요청을 보낸 뒤, 대기가 없으므로 순차적으로 흐름을 진행할 수 있기 때문입니다. 물론 보낸 요청의 응답이 왔을 때의 처리는 따로 해야 합니다. 자세한 사용 방법은 DataStorageService를 참고하세요.


OnBeginPlay()에서 사용하면 OnUpdate()가 불리지 않습니다. OnBeginPlay()가 끝나야 OnUpdate()가 불리기 때문입니다.

위에서 언급한 여러 동작은 병렬적으로 수행되어야 합니다. 병렬적으로 해당 기능을 수행하려면 TimerService를 사용하면 됩니다.

Wait과 TimerService의 차이점
wait는 대기한 뒤에 직접 어떤 행동을 수행하는 것이고, TimerService는 해당 행동을 수행하는 별도의 일을 만드는 것입니다. wait는 직렬, TimerService는 병렬 형태로 동작합니다.
따라서 wait의 사용 코드는 다음과 같이 표현할 수 있습니다

local targetEntity  = _EntityService:GetEntity("a22396e1-6365-42d4-9cef-5924c223f7fa")
targetEntity.TestComponent:ShowMessage()

function delayMessage()
	local targetEntity2 = _EntityService:GetEntity("a22396e1-6365-42d4-9cef-5924c223f7fa")
	targetEntity2.TestComponent:ShowMessage()
end
	
_TimerService:SetTimerOnce(delayMessage, 3)
wait와 TimerService의 차이를 이해한 뒤 적절한 곳에, 각각의 동작이 어떤 흐름을 따라갈지 이해하며 사용해야 합니다.
wait와 TimerService의 차이를 이해했다면 아래 코드의 실행 순서를 맞출 수 있습니다.

log("Do A")
wait(1)
log("Do B")

log("Do C")
function DoD()
	log("Do D")
end
_TimerService:SetTimerOnce(DoD, 1)
log("Do E")
실행 순서는 A → B → C → E → D입니다.

OnUpdate에서 호출할 때 주의 사항
Update는 매 프레임마다 호출되기 때문에 최적화를 굉장히 신경을 써야 합니다. 자칫 잘못 사용하면 엄청난 성능 하락을 불러오기 때문입니다. 월드를 제작하는 많은 크리에이터가 겪는 최적화 문제의 대부분이 Update 문에서 발생하기 때문에 사용 시 늘 주의해야 합니다.

동기화 프로퍼티 (Server Update에서 사용)
특정 이벤트가 경과된 시간을 표시하려고 period라는 프로퍼티를 두었다고 가정해 봅시다.
업데이트 문에는 self.period = self.period + delta 같은 로직을 넣으면 프레임마다 시간을 더하므로 저 값이 실제로 이벤트 경과 시간을 나타냅니다. 하지만 period가 동기화 프로퍼티라면 엄청난 문제가 발생합니다.

동기화 프로퍼티는 말 그대로 "동기화"를 합니다. 동기화는 엄청난 네트워크 비용을 사용합니다. 매 프레임마다 동기화해야 하며, 그 양을 접속된 클라이언트만큼 보내게 됩니다. 이 로직이 엔티티에 있는 컴포넌트라면 각각의 엔티티가가 각각의 클라이언트로 보내야 하므로 N * N의 비용을 사용하게 됩니다. 혼자 테스트할 때는 부담 없는 양이라 괜찮다고 생각했을지라도, 플레이어가 늘어날수록 비용이 엄청나게 증가하기 때문에 단체 테스트 시 새로운 문제가 발생하게 됩니다. 그러므로 동기화 프로퍼티를 Update 문에서 사용할 때는 늘 주의해야 합니다.

꼭 이러한 기능을 사용해야 한다면 다음과 같이 작성해 봅시다.
eventActiveTime을 동기화할 때 한 번만 동기화하므로 비용을 절약할 수 있습니다.

Event 시작 시(Server)
self.eventActiveTime = _UtilLogic.ServerElapsedSeconds

경과 시간을 얻고 싶을 때(Client)
local period = _UtilLogic.ServerElapsedSeconds - self.eventActiveTime

실행 제어 함수 (Server, Client Update에서 사용)
동기화 프로퍼티와 같은 원리입니다. Update 내에서 다른 실행 공간(Client → Server 혹은 Server → Client)을 호출하면 엄청난 네트워크 비용이 소모됩니다.
Client에서 사용하면 매 프레임마다 Server로 네트워크 비용을 사용하게 되고, Server에서 사용하면 모든 클라이언트에게 보내기 때문에 더 큰 문제가 됩니다.

Wait
그럼 OnUpdate()에서 사용할 경우를 살펴보겠습니다. OnUpdate() 문에서 아래 코드는 어떻게 동작할까요?

log("TEST") -- No.1
wait(1)
log("TEST2") -- No.2
기대 동작: TEST - 1초 대기 - TEST2 - TEST1 - 1초 대기 - TEST2

실제 동작: TEST - TEST - TEST - .... (첫 번째 TEST가 찍힌 시점부터 1초가 지났을 때 ) - TEST2

OnUpdate()는 논리적인 측면에서 수행이 끝날 당시 해당 부분을 종료시키고 다음 프레임에서는 새로운 OnUpdate()가 생성됩니다.

하지만 OnUpdate()에서 역할을 수행하다가 wait()를 만나면 동작을 멈추고 입력한 시간이 될 때까지 대기합니다. 그리고 다음 프레임에 OnUpdate()를 새로 생성하고 처음부터 실행하고, 대기하는 것을 wait()에 입력한 시간이 될 때까지 반복합니다. 이는 크리에이터가 원한 동작이 아닐 뿐만 아니라 최적화 문제도 생기게 됩니다.

더 알아보기
OnUpdate()에서 wait()를 사용하는 것은 좋지 않은 설계입니다. 코드를 수정하는 것을 권장합니다.

wait()를 Update와 함께 사용할 경우 엄청난 비효율 시너지를 일으킵니다.
앞서 설명한 대로 OnUpdate()는 실행이 종료되면 Update 객체가 종료되어야 합니다. 하지만 Wait 하게 되면 현재 Update 문을 종료시킬 수 없기 때문에 Update 객체가 계속 쌓입니다. 계속 쌓이는 Update 객체는 속도나 메모리 측면에서 자원을 잡아먹기에 월드가 느려지는 원인이 됩니다. 그뿐만 아니라 각 업데이트 객체별 프로퍼티 흐름을 파악하기 어렵고, 디버깅도 쉽지 않습니다.

따라서 Update 문 내에서는 특별한 경우를 제외하고는 wait() 사용을 자제해야 합니다.

특정 클라이언트에만 응답 보내기
어떤 함수의 실행 제어 옵션이 Client로 설정되어 있다면 해당 함수는 모든 클라이언트에서 실행됩니다.
하지만 서버에서는 모든 클라이언트가 아니라 특정 클라이언트에만 함수를 실행하고 싶은 상황이 생길 수 있습니다.
특정 클라이언트가 서버에 어떤 요청(Request)을 보내고 서버가 로직을 처리한 이후, 해당 클라이언트에 응답(Response) 하는 상황이 그것입니다.

예를 들어 봅시다.

A 클라이언트에서 아이템 구매 버튼을 누른다면 : (Request)

서버에서는 A가 가진 돈을 차감하고 아이템 개수를 늘린 다음

이를 처리했다는 응답을 클라이언트에 보낼 것입니다. : (Response)

이때 서버는 A에게만 응답하면 되고 그 외 다른 클라이언트에게는 응답할 필요가 없습니다.
이처럼 처음 요청을 보냈던 클라이언트에만 응답하는 과정을 코드로 구현해 봅시다.

[Server]
void RequestBuyItem(integer shopID, integer itemID)
{
    local itemCost = _ShopLogic:GetItemCost(shopID, itemID)
    if itemCost < self.money then
        self.money = self.money - itemCost
        self:BuyItem(itemID)
        self:ResponseBuyItem(itemID, self.Entity.PlayerComponent.UserId)
    end 
}

[Client]
void ResponseBuyItem(integer itemID, string userId)
{
    -- 처음 요청을 보냈던 유저인지 확인 후, 클라이언트에서 요청 보낸 유저일 때만 동작함
    if userId == _UserService.LocalPlayer.PlayerComponent.UserId then
        log("Success")
    end
}
이처럼 코드를 작성하면 제대로 동작하기는 하지만 매우 비효율적입니다.
서버에서는 처음 요청을 보냈던 A뿐만 아니라 모든 클라이언트에게 메시지를 보냈기 때문에 네트워크 비용이 올라가고, 전체 월드를 느려지게 만듭니다.

이와 같은 문제를 해결하기 위해 메이플스토리 월드에서는 "실행 공간이 Client로 설정된 함수를 특정 클라이언트에게만 보낼 수 있는 기능"을 제공합니다. 이 기능을 사용하는 방법은 간단합니다. 실행 공간이 Client인 함수의 마지막 매개 변수에 보내려는 UserId를 적으면 됩니다. 단, 이 UserId는 자동으로 붙기 때문에 생략해도 됩니다.
이렇게 하면 해당 유저의 클라이언트에만 함수를 전송할 수 있습니다. 또한 코드도 간단해지고 월드 최적화에도 효과적입니다.

아래의 코드를 살펴보면 위의 설명을 보다 쉽게 이해할 수 있습니다.

[Server]
void RequestBuyItem(integer shopID,integer itemID)
{
    local itemCost = _ShopLogic:GetItemCost(shopID, itemID)
    if itemCost < self.money then
        self.money = self.money - itemCost
        self:BuyItem(itemID)
        self:ResponseBuyItem(itemID, self.Entity.PlayerComponent.UserId)
    end 
}

[Client]
-- 사실 `ResponseBuyItem(integer itemID, string targetUserId = nil)`인 것이지만, UserId는 자동으로 붙기 때문에 생략함
void ResponseBuyItem(integer itemID)
{
    log("Success")
}
위의 코드에서 ResponseBuyItem(integer itemID)은 사실 ResponseBuyItem(integer itemID, string targetUserId = nil)인 것이지만, 마지막 매개 변수인 targetUserId는 자동으로 붙기 때문에 코드 작성 시에는 생략합니다. 따라서 위의 코드처럼 작성하면 해당 유저에게만 함수가 전달됩니다. 또한 클라이언트에서도 별다른 유저 확인 없이 사용할 수 있고, 네트워크 비용도 절약됩니다.
