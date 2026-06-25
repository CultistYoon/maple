# RateLimitService 활용하기

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「RateLimitService 활용하기」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 10 보안및최적화 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
유저의 server 함수 사용량을 제한하는 방법을 알아봅시다.

참고 가이드
패킷 변조 대비하기
월드 인스턴스
인스턴스 맵 만들기

RateLimitService 알아보기
server 실행 함수는 클라이언트가 서버에 직접 특정 동작을 수행하도록 만들기 때문에 누군가 악의를 갖고 패킷을 변조하거나, 같은 행위를 반복할 경우 월드에 장애를 발생시킬 수 있습니다. RateLimitService는 server 실행 함수의 사용량을 크리에이터가 설정한 값에 따라 제한하고, 유저가 제한된 함수를 다시 사용할 수 있을 때까지 필요한 대기 시간 또한 설정하는 방식으로 월드 보안을 강화할 수 있습니다. RateLimitService로 사용량을 제한할 수 있는 함수는 Native API의 server 함수와 크리에이터가 제작한 server 함수 두 가지입니다.
RateLimitService는 룸의 특성을 고려해 크리에이터 월드에 어울리는 방식으로 활용하는 것이 좋습니다. 룸마다 RateLimitService가 존재하므로 특정 룸의 사용량 제한은 다른 룸에 영향을 주지 않는 점을 염두에 두어야 합니다.

더 알아보기
유연하게 RateLimitSevice를 사용하고 싶다면 Logic에서 활용할 수 있습니다.

토큰 소비와 재충전
RateLimitService를 사용하기 위해서는 토큰 개념을 알아야 합니다. 토큰이란 사용량을 제한하기 위해 크리에이터가 정하는 임의의 호출 제한 한도입니다.
사용량 제한에 도달한 플레이어는 토큰이 재충전될 때까지 함수를 호출하지 못하게 됩니다. 사용량을 제한하기 위해 크리에이터는 토큰 수와 토큰의 충전 간격을 크리에이터가 함수의 매개 변수로 정해야 합니다. 월드 설계에 따라 플레이어가 상대적으로 빈번하게 호출하는 함수의 경우 충전 간격을 다른 함수보다 짧게 두는 것이 좋습니다.

RateLimitService의 SetServerFunctionRateLimitForLogic()의 매개 변수를 살펴보며 토큰을 이해해 봅시다.

void SetServerFunctionRateLimitForLogic(string logicName, string functionName, int maxToken, float tokenRefillPerSecond)
maxToken 수를 정하고, 초당 충전되는 토큰 수를 tokenRefillPerSecond로 정합니다. 매개 변수의 자세한 의미는 다음과 같습니다.

logicName: 사용량을 제한할 함수가 있는 logic의 이름입니다.

functionName: 사용량을 제한할 함수의 이름입니다.

maxToken: 크리에이터가 설정하는 최대 토큰 수로 유저가 함수를 호출할 때마다 1개씩 차감됩니다.

tokenRefillPerSecond: 초당 충전되는 토큰 수입니다. 예를 들어 0.2로 설정하면 5초 뒤 토큰 수가 1 증가합니다.

활용 예제
플레이어가 MoveToMapPosition() 함수를 짧은 주기 동안 여러 번 호출할 수 없도록 제한하는 예제를 만들어 봅시다. PlayerComponent의 MoveToMapPosition() 함수를 3초에 한 번만 호출할 수 있도록 제한합니다.
[object Object]

맵 제작
맵에 텔레포트를 위해 이동할 수 있는 InteractionEntity를 만들고, 타일에 도착 장소인 Destination을 배치합니다. 이 맵은 InteractionEntity를 통해 이동한 후, 다시 이동 가능 지점까지 걸리는 시간이 3초라고 가정합니다. 3초보다 빠르게 맵 이동을 시도한다면 이는 함수를 변조했다고 간주할 수 있습니다.
이러한 변조를 막기 위해 RateLimitService를 활용해 함수 사용을 제한하는 예제 월드를 만들어 봅시다.
[object Object]

InteractionEntity 제작
Map01- Create Entity - Create Empty를 선택해 새로운 InteractionEntity를 생성합니다.

TransformComponent, SpriteRendererComponent, InteractionComponent를 추가합니다.
1

Workspace - MyDesk - Create Scripts - Create Component를 선택해 TeleportComponent를 생성합니다.

TeleportComponent를 생성한 InteractionEntity에 추가합니다.

TeleportComponent에 Destination 프로퍼티를 추가합니다.

Property:
[None]
Entity Destination = nil
InteractionEntity의 프로퍼티 창에서 크리에이터가 맵에 생성한 Destination 엔티티를 프로퍼티 경로로 지정합니다.
[object Object]

E키를 눌러 만든 포탈 엔티티와 플레이어가 상호 작용하면 플레이어를 Destination 엔티티로 이동시키도록 아래와 같이 작성합니다.

Event Handler:
[client only][self]
HandleInteractionEvent(InteractionEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: InteractionComponent
    -- Space: Server, Client
    ---------------------------------------------------------

    -- Parameters
    local InteractionEntity = event.InteractionEntity
    ---------------------------------------------------------

    -- 상호 작용 키를 누르면 내 플레이어 엔티티를 'Destination' 엔티티로 이동 시킵니다.
    if InteractionEntity == _UserService.LocalPlayer then
        local localPlayer = _UserService.LocalPlayer
        local currMap = self.Entity.CurrentMap
        local destPos = self.Destination.TransformComponent.WorldPosition:ToVector2()
        localPlayer.PlayerComponent:MoveToMapPosition(currMap.Name, destPos)
    end
}
텔레포트 UI 제작
언제든지 Destination 엔티티로 이동할 수 있는 UI를 만들어봅시다. 이 UI를 사용할 경우 사용량 제한에 걸리게 됩니다.

Hierarchy - ui - DefaultGroup - Create Entity - Create Button을 선택해 새로운 UIButton을 생성합니다.

크기와 색상을 자유롭게 결정합니다.
[object Object]

Workspace - MyDesk - Create Scripts - Create Component를 선택해 새로운 CheatingComponent를 생성합니다.

DefaultPlayer에 CheatingComponent를 추가합니다.

프로퍼티 Destination에는 도착지가 될 Entity의 경로를 지정합니다.

Property:
[None]
Entity Destination = /maps/map01/Destination
버튼을 누르면 플레이어가 Destination 위치로 이동할 수 있도록 ButtonClickEvent에 UIButton을 연결하고 아래와 같이 작성합니다.

Event Handler:
[entity: UIButton(/ui/DefaultGroup/UIButton)]
HandleButtonClickEvent(ButtonClickEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: ButtonComponent
    -- Space: Client
    ---------------------------------------------------------

    -- Parameters
    -- local Entity = event.Entity
    ---------------------------------------------------------

    local currMap = self.Entity.CurrentMap
    local destPos = self.Destination.TransformComponent.WorldPosition:ToVector2()
    self.Entity.PlayerComponent:MoveToMapPosition(currMap.Name, destPos)
}
사용량 제한 로직 제작
유저가 입장하면 PlayerComponent의 MoveToMapPosition() 함수를 제한할 수 있도록 아래와 같이 작성합니다.

Workspace - MyDesk - Create Scripts - Create Logic을 선택해 RateLimitLogic을 생성합니다.

유저가 월드에 입장하면 PlayerComponent의 MoveToMapPosition() 함수의 사용량을 제한하도록 SetServerFunctionRateLimitForComponent() 함수를 활용합니다.
토큰 수는 2, 초당 토큰 재충전 수는 0.3입니다.

Event Handler:
[service: UserService]
HandleUserEnterEvent(UserEnterEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: UserService
    -- Space: Server
    ---------------------------------------------------------

    -- Parameters
    local UserId = event.UserId
    ---------------------------------------------------------

    local userEntity = _UserService:GetUserEntityByUserId(UserId)
    _RateLimitService:SetServerFunctionRateLimitForComponent(userEntity.Id, "PlayerComponent", "MoveToMapPosition", 2, 0.3)
}
사용량 제한에 도달한 유저가 있을 경우 경고 로그가 출력되도록 작성합니다. UserService를 활용해 유저 정보를 알 수 있습니다.

[service: RateLimitService]
HandleServerFunctionRateLimitEvent(ServerFunctionRateLimitEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: RateLimitService
    -- Space: Server
    ---------------------------------------------------------

    -- Parameters
    local FunctionName = event.FunctionName
    local ProfileCode = event.ProfileCode
    ---------------------------------------------------------

    local user = _UserService:GetUserByProfileCode(ProfileCode)
    log_warning("'" .. user.Nickname .. "\' 유저는 \'" .. FunctionName .. "\' 함수 사용량 제한을 초과했습니다.")
}
[시작]을 누르고 Teleport 버튼을 짧은 시간 안에 여러 번 눌러 MoveToMapPosition() 함수를 호출합니다.
Console 창에서 에러 로그가 발생한 것을 확인할 수 있습니다.
