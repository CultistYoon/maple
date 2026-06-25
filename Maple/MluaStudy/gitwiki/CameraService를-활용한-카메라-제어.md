# CameraService를 활용한 카메라 제어

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「CameraService를 활용한 카메라 제어」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 06 연출 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
게임을 만들다 보면 카메라가 비추는 대상을 변경하거나 확대, 축소를 이용해 연출해야 할 때가 있습니다.
이번 과정에서는 CameraService를 통해 타깃 카메라를 제어하는 방법과 카메라 연출 효과에 대해 알아보도록 합니다.

참고 가이드
엔티티와 컴포넌트 참조
엔티티의 충돌을 감지하는 TriggerComponent
Event System
Entity Event System

사전 설정
CameraService의 각 기능을 알아보기 위해 다음과 같은 상황을 만들어보겠습니다.

캐릭터가 오브젝트에 닿으면 카메라의 타깃이 NPC로 변경되거나 줌인/아웃된다.

카메라가 움직이고, 약 5초 후에 다시 원 위치로 돌아온다.

타깃 변경, 줌인/아웃 시 Blend 효과를 변경하여 적용한다.

이를 위해선 먼저 다음과 같은 사전 설정이 필요합니다.
맵과 컴포넌트 사전 설정이 필요합니다.

맵 사전 설정
아래와 같이 좌우로 긴 맵을 만들고 좌측 끝에는 SpawnLocation, 우측 끝에는 NPC를 배치합니다.
SpawnLocation 옆에 캐릭터가 닿았을 때 카메라 제어의 트리거가 될 수 있는 오브젝트를 하나 배치합니다.
SpawnLocation 엔티티는 Preset List의 Special 카테고리에, Object와 NPC은 각각 Object와 NPC 카테고리에서 배치할 수 있습니다.
cameraservicemapsetting

컴포넌트 사전 설정
위에 배치한 오브젝트와 NPC에 다음과 같이 컴포넌트를 추가합니다.

엔티티	추가 컴포넌트
Object	
TriggerComponent
New Script Component
새 스크립트 컴포넌트를 생성하고 이름을 "CameraControl"로 지어 줍니다.
새 스크립트 컴포넌트를 생성해서 Object에 추가합니다.
캐릭터가 Object에 닿았을 때의 카메라 연출을 구현합니다.
NPC	CameraComponent
DefaultPlayer에도 CameraComponent가 추가되어 있는지 확인합니다. 만일 캐릭터에 CameraComponent가 붙어있지 않다면 추가합니다.
cameraservice01

다음으로, 오브젝트에 추가했던 스크립트 컴포넌트에 카메라 제어를 구현할 TriggerEnterEvent를 추가합니다. 이벤트 센더는 Self로 설정합니다.
CameraService02

카메라 타깃 전환
사전 설정을 마쳤으니 본격적으로 CameraService의 기능에 대해 알아보겠습니다. 먼저 카메라의 타깃 설정 방법을 알아봅시다.

void SwitchCameraTo(CameraComponent cameraToSwitch)
게임을 플레이하면 카메라는 기본적으로 플레이어를 피사체(타깃)로 삼아 계속 플레이어를 따라다니며 화면에 비춥니다.그러나 게임 장르 특성 때문에 혹은 게임의 특별한 연출을 위해서 카메라의 피사체(타깃)를 변경하고 싶을 때 CameraService의 SwitchCameraTo() 함수를 활용합니다.

SwitchCameraTo() 함수는 카메라의 피사체(타깃)을 변경할 수 있습니다.
기본 피사체인 플레이어에서 벗어나 특정 엔티티로 카메라를 옮기고 싶을 때 SwitchCameraTo() 함수를 사용합니다. SwitchCameraTo() 함수를 호출하면 CameraComponent를 갖고 있는 목표 엔티티의 경로를 받아 카메라의 피사체 대상을 목표 엔티티로 옮깁니다.

아래는 SwitchCameraTo() 함수를 활용해 카메라 타깃을 캐릭터에서 NPC로 변경하는 예시 코드입니다. 사전 설정 때 추가한 스크립트 컴포넌트의 TriggerEnterEvent에 다음 내용을 추가합니다.

[self]
HandleTriggerEnterEvent (TriggerEnterEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: TriggerComponent
    -- Space: Server, Client
    ---------------------------------------------------------
    
    -- Parameters
    local TriggerBodyEntity = event.TriggerBodyEntity
    ---------------------------------------------------------
    --카메라의 타깃이 될 NPC 엔티티를 받아옵니다.
    --NPC 경로는 배치한 NPC에 따라 달라질 수 있습니다.
    local NPCEntity = _EntityService:GetEntityByPath("/maps/map01/npc-13")
         
    --SwitchCameraTo를 사용해 카메라 타깃을 NPC로 변경합니다.
    --SwitchCameraTo의 매개 변수에 NPC엔티티의 CameraComponent를 넘겨줍니다.
    _CameraService:SwitchCameraTo(NPCEntity.CameraComponent)   
}
카메라가 정상적으로 타깃을 변경하는지 시작을 눌러 확인합니다.


number TransitionBlendTime
TransitionBlendTime은 CameraService에서 제공하는 프로퍼티로 카메라가 목표 피사체로 이동하는데 걸리는 시간을 정할 수 있습니다.
TransitionBlendTime 시간을 SwitchCameraTo() 함수 호출 이전에 설정하면, 설정 시간에 걸쳐 카메라가 목표 피사체로 이동하는 것을 볼 수 있습니다. 따라서 SwitchCameraTo() 함수를 호출하기 전에 TransitionBlendTime에 시간을 설정하면, TransitionBlendTime의 설정 시간 동안 카메라가 전환된 타깃으로 이동하는 것을 볼 수 있습니다.
TransitionBlendTime에 시간 값을 할당하면, 카메라가 전보다 빠르게 전환되는 예시 코드입니다.

[self]
HandleTriggerEnterEvent (TriggerEnterEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: TriggerComponent
    -- Space: Server, Client
    ---------------------------------------------------------
    
    -- Parameters
    local TriggerBodyEntity = event.TriggerBodyEntity
    ---------------------------------------------------------
    --카메라의 타깃이 될 NPC 엔티티를 받아옵니다. "NPCPath"에 배치한 NPC 엔티티의 경로를 입력합니다.
    local NPCEntity = _EntityService:GetEntityByPath("/maps/map01/npc-13") 
    
    --카메라가 다른 타깃으로 전환되는 시간을 설정합니다. 
    _CameraService.TransitionBlendTime = 1  
    
    --SwitchCameraTo를 사용해 카메라 타깃을 NPC로 변경해줍니다.
    --SwitchCameraTo의 매개 변수에 NPC엔티티의 CameraComponent를 넘겨줍니다.
    _CameraService:SwitchCameraTo(NPCEntity.CameraComponent)
}
시작을 눌러 게임을 테스트합니다.


CameraBlendType TranstionBlendType
TranstionBlendType은 피사체(타깃)로 전환 시 카메라의 움직임을 제어할 수 있는 프로퍼티입니다.
SwitchCameraTo() 호출 전에 TranstionBlendType에 CameraBlendType의 enum 값을 할당해 타깃 전환 시 블렌드 타입을 변경할 수 있습니다. 아래는 위 예제에서 TranstionBlendType에 CameraBlendType.Linear를 할당하는 코드를 추가하여, 카메라의 움직임을 조금 딱딱하게 변경해보도록 하겠습니다.

[self]
HandleTriggerEnterEvent (TriggerEnterEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: TriggerComponent
    -- Space: Server, Client
    ---------------------------------------------------------
    
    -- Parameters
    local TriggerBodyEntity = event.TriggerBodyEntity
    ---------------------------------------------------------
    --카메라의 타깃이 될 NPC 엔티티를 받아옵니다. "NPCPath"는 각자 배치한 NPC엔티티의 경로를 입력합니다.
    local NPCEntity = _EntityService:GetEntityByPath("/maps/map01/npc-13")
         
    --카메라가 다른 타깃으로 전환되는 시간을 설정합니다.
    _CameraService.TransitionBlendTime = 1
         
    --카메라의 움직임을 설정합니다.
    --Linear는 카메라를 일정한 속도로 움직여 화면을 전환합니다. 
    --선형적으로 전환하기 때문에 딱딱하고 기계적인 느낌이 납니다. 
    _CameraService.TransitionBlendType = CameraBlendType.Linear
         
    --SwitchCameraTo를 사용해 카메라 타깃을 NPC로 변경합니다.
    --SwitchCameraTo의 매개 변수에 NPC엔티티의 CameraComponent를 넘겨줍니다.
    _CameraService:SwitchCameraTo(NPCEntity.CameraComponent)
}
시작을 눌러 게임을 테스트합니다.
TransitionBlendType 설정이 없는 예제와 비교했을 때 다른 움직임을 보이는 것을 확인할 수 있습니다.

TransitionBlendType 설정 전

TransitionBlendType 설정 후

블렌드 타입은 6가지 타입을 제공하고 있습니다.
TranstionBlendType의 기본값은 EaseInOut으로, 다른 타입 값을 할당하지 않을 때 자동으로 할당됩니다.

타입	설명
Cut	카메라를 즉시 CameraComponent의 위치로 전환합니다. 화면이 순간 이동 하듯 전환됩니다. TransitionBlendType이Cut일 때 TranstitionBlendTime은 의미가 없습니다.
EaseInOut	S모양 커브처럼 전환 시작과 끝을 부드럽게 처리합니다. Blend타입 기본값입니다.
EaseIn	전환 시작 시에는 선형적으로, 끝에는 부드럽게 전환합니다.
EaseOut	전환 시작 시에는 부드럽게, 끝에는 선형적으로 전환합니다.
HardIn	전환 시작 시에는 부드럽게, 끝에는 빠르게 전환합니다.
HardOut	전환 시작 시에는 빠르게, 끝에는 부드럽게 전환합니다.
Linear	일정한 속도로 전환합니다. 선형적으로 전환하기 때문에 딱딱하고 기계적인 느낌이 납니다.
Zoom 제어
게임 플레이 중에 카메라 줌 인과 줌 아웃을 제어하는 방법에 대해 알아보겠습니다.
위에서 작성한 코드는 필요하지 않기 때문에 모두 지우고, 아래와 같은 상태에서 시작합니다.

[self]
HandleTriggerEnterEvent (TriggerEnterEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: TriggerComponent
    -- Space: Server, Client
    ---------------------------------------------------------
    
    -- Parameters
    local TriggerBodyEntity = event.TriggerBodyEntity
    ---------------------------------------------------------
}
void ZoomTo(number percent, number duration)
ZoomTo() 함수는 특정 시간 동안 줌 인/아웃을 수행하는 함수입니다.
매개 변수로는 Percent와 Duration을 받습니다.
Percent는 변경할 줌 값을 의미하며 호출 시 퍼센트 값을 넘겨줍니다.
현재 줌 값보다 큰 값이 넘어오면 화면을 확대하고(줌 인), 작은 값이 넘어오면 화면을 축소합니다.(줌 아웃)
duration은 현재 줌 값에서 매개 변수로 넘겨준 값(초)까지 도달하는데 걸리는 시간입니다.

아래는 ZoomTo() 함수를 사용해 5초 동안 캐릭터를 확대하는 예시 코드입니다.

[self]
HandleTriggerEnterEvent (TriggerEnterEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: TriggerComponent
    -- Space: Server, Client
    ---------------------------------------------------------
    
    -- Parameters
    local TriggerBodyEntity = event.TriggerBodyEntity
    ---------------------------------------------------------
    -- 5초간 줌 값을 150%로 변경합니다.
    _CameraService:ZoomTo(150, 5)
}
시작을 눌러 게임을 테스트합니다. 캐릭터가 문에 닿으면 카메라가 캐릭터(타깃)을 중심으로 5초 동안 점점 확대됩니다.


void ZoomReset()
ZoomReset()는 변경된 줌 값을 초깃값으로 되돌리는 함수입니다. ZoomReset()을 사용하면 ZoomTo()를 이용해 줌 값을 변경하더라도, 다시 초깃값으로(100%) 맞출 수 있습니다.

ZoomTo() 예시에 이어 ZoomReset()을 사용해 5초 뒤 줌 값을 100%로 변경하는 예시 코드입니다.
이해를 돕기 위해 TimerService를 활용했습니다. TimerService 가이드를 참고하세요.

[self]
HandleTriggerEnterEvent (TriggerEnterEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: TriggerComponent
    -- Space: Server, Client
    ---------------------------------------------------------
    
    -- Parameters
    local TriggerBodyEntity = event.TriggerBodyEntity
    ---------------------------------------------------------
    -- 5초 동안 줌 값을 150%로 변경합니다.
    _CameraService:ZoomTo(150, 5)
     
    -- 줌 인이 끝나고, 5초 뒤 함수 실행을 예약할 수 있는 CallBack함수를 만듭니다.
    -- CallBack함수 안에서 ZoomReset를 호출하도록 합니다.
    local CallBack = function()
        _CameraService:ZoomReset() 
    end
     
    -- TimerService를 활용해 줌 인이 끝나고 5초 뒤에 실행할 CallBack함수를 넘겨줌으로써
    -- CallBack함수 안에 있는 ZoomReset이 실행될 수 있도록 합니다
    _TimerService:SetTimerOnce(CallBack, 10)
}
시작을 눌러 게임을 확인합니다. 문에 닿은 후 5초간 150% 확대되었다가, 5초 뒤 다시 원래대로 돌아오는 것을 확인할 수 있습니다.


기타 기능
CameraService는 주요 기능과 더불어 몇 가지의 유용한 기능을 함께 제공하고 있습니다.

Property
number CurrentZoomRatio (read only)
현재 카메라의 줌 비율을 퍼센트로 반환하는 프로퍼티로, 기본값은 100입니다.
이 프로퍼티는 읽기 전용이므로, 줌 비율을 설정하고 싶을 땐 ZoomTo() 함수를 사용해야합니다.

log("zoom : ".._CameraService.currentZoomRatio)  -- 100 출력
Functions
CameraComponent GetCurrentCameraComponent()
현재 카메라가 추적 중인 Entity의 CameraComponent를 가져옵니다.

local cameraComponent = _CameraService:GetCurrentCameraComponent()
log(cameraComponent)
