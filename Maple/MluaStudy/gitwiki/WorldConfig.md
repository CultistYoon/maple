# WorldConfig

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「WorldConfig」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 01 시작하기 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
메이플스토리 월드는 WorldConfig에서 다양한 월드 설정 기능을 제공합니다. WorldConfig의 기능은 제작 중인 월드에 전반적인 영향을 끼칩니다.

참고 가이드
실행 제어

Effective MSW 2

패킷 변조 대비하기

예시로 알아보는 서버 검증

WorldConfig 소개
WorldConfig는 크리에이터가 제작하는 월드의 다양한 설정을 변경할 수 있습니다.

Edit - WorldConfig를 누릅니다.

Workspace - WorldConfig를 누르면 세부 설정 항목이 프로퍼티 에디터 창에 나타납니다.

[object Object]

LegacyAnimation
메이플스토리 월드의 아바타 움직임과 애니메이션은 2023년 3월 23일에 원작 메이플스토리과 유사하게 동작하도록 변경되었습니다. 만약 크리에이터의 월드가 변경일 이전에 제작되었다면, LegacyAnimation을 활성화해 이전의 메이플스토리 월드의 아바타 움직임과 애니메이션을 적용합니다. 다만, 현재의 아바타 움직임이 원작과 유사하므로 변경일 이후에 제작된 월드라면 LegacyAnimation 적용을 권장하지 않습니다.
이전 움직임과 현재의 움직임은 아래와 같습니다.

true	false
legacy	animation
PlayerEntityAuthorityCheck
플레이어 엔티티에 속한 컴포넌트의 서버 함수를 로컬 클라이언트에만 호출하도록 합니다. 이 설정을 활성화하면 월드의 보안을 강화할 수 있습니다. 예를 들어 DefaultPlayer에 속한 컴포넌트 중 실행 공간이 server인 MoveToMapPosition() 함수는 로컬 클라이언트 외 다른 클라이언트에서 호출할 수 없습니다. 함수를 실행 시 콘솔창에 에러 메시지가 나타납니다.

Method:
[client only]
void NewFunction()
{
    local targetEntity = nil
    for key, value in pairs(_UserService.UserEntities) do
    	if key ~= _UserService.LocalPlayer.Name then
    		targetEntity = value
    		break
    	end
    end
    
    if targetEntity ~= nil then
    	targetEntity.PlayerComponent:MoveToMapPosition("map01", Vector2(0, 3))
    end
}
PlayerEntity

ServiceAuthorityCheck
Service의 모든 서버 함수를 ServerOnly 함수로 동작하도록 변경합니다. 이 설정을 활성화해 월드의 보안을 강화할 수 있습니다. 예를 들어 아래와 같이 client only 함수에서 실행 공간이 server인 함수를 실행하면 실행 시 콘솔창에 에러 메시지가 나타납니다.

Method:
[client only]
void OnMapEnter(Entity enteredMap)
{
    _TeleportService:TeleportToMapPosition(me, currentPosition + Vector3(0, 2, 0), currentMapName)
}
1

RestrictedPlayerEntitySync
플레이어 엔티티에 속한 네이티브 컴포넌트의 Sync 프로퍼티가 클라이언트에서 변경된 값을 서버로 동기화하지 않도록 설정합니다. 이 설정을 활성화하면 월드의 보안을 강화할 수 있습니다. 예를 들어 클라이언트에서 ChatBalloonComponent.Message에 메시지를 입력하면 서버로 동기화하지 않기 때문에 다른 플레이어들의 화면에서는 말풍선이 나타나지 않습니다.

[client only]
void ShowChatBalloon()
{
    local chatBalloon = self.Entity.ChatBalloonComponent
    chatBalloon.ChatModeEnabled = false
    chatBalloon.AutoShowEnabled = true
    chatBalloon.Message = "메이플스토리 월드"
}
예외적으로 다음 컴포넌트들은 RestrictedPlayerEntitySync에 영향을 받지 않습니다. 플레이어 엔티티에 속해 있으면 항상 클라이언트에서 서버로 동기화가 이루어지므로 주의해야 합니다.

MovementComponent

PlayerControllerComponent

StateComponent

TransformComponent

SourceLanguage
플레이어가 월드에서 자동 번역 기능을 사용한다면 SourceLanguage의 언어를 번역 대상으로 삼습니다. 현재 원문 언어로 설정할 수 있는 언어는 한국어, 영어입니다. 추후 언어가 추가될 수 있습니다.

LocalWorkspace
월드 데이터를 크리에이터의 컴퓨터(Local)로 내려받을 수 있는 기능입니다. 월드의 다양한 엔트리와 데이터를 크리에이터의 컴퓨터에 파일 형태로 저장합니다. 자세한 내용은 LocalWorkspace 가이드를 참고하세요.

WorldOrientation
월드의 비율을 변경할 수 있습니다. Landscape, Portrait, Responsive 중 하나를 선택하면 월드 전체에 동일한 설정이 적용됩니다.

Landscape: 월드가 가로 모드로 실행됩니다.

Portrait: 월드가 세로 모드로 실행됩니다.

Responsive: 월드가 반응형 모드로 실행됩니다.

UseLitDefaultMaterial
UseLitDefaultMaterial을 활성화하면 모든 엔티티는 LitMode가 Lit인 상태로 간주됩니다. 이에 따라 엔티티들이 다른 광원으로부터 영향을 받아 표면의 색상과 밝기가 달라지게 됩니다. 그러나 LitMode를 별도로 설정할 수 있는 엔티티의 경우 따로 지정된 LitMode의 값을 따르게 됩니다.
UseLitDefaultMaterial를 활성화하면 로비로 나가게되며, 재진입 시 활성화된 상태가 반영됩니다.
