# Lua Executor

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「Lua Executor」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 01 시작하기 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
메이커에서 제작한 월드를 테스트할 때 다양한 컴포넌트, 프로퍼티 값을 변경해 실시간으로 의도한 바가 맞는지 확인하거나, 서버 또는 클라이언트 환경에서 각각 만든 스크립트가 문제없이 작동하는지 확인하고 싶을 수 있습니다. Lua Executor로 이러한 내용을 쉽게 확인할 수 있습니다. 몇 가지 활용 예시와 함께 Lua Executor에 대해 알아봅시다.

Lua Excutor
Lua Executor를 사용하면 메이커에서 플레이 중에 실시간으로 스크립트를 실행하고 즉시 월드에 반영됩니다. 크리에이터의 필요에 따라 플레이 중에 다양한 스크립트를 실행하며 월드를 확인할 수 있습니다. 작성한 스크립트는 서버, 클라이언트, 인스턴스 룸에서 각각 실행할 수 있으며, 실행한 값은 Console 창에서 확인할 수 있습니다.

화면 소개
[object Object]

번호	이름	설명
[object Object]	실행 공간 설정	실행 공간을 설정할 수 있습니다. 서버, 클라이언트, 인스턴스 룸을 설정할 수 있습니다.
[object Object]	실행	작성한 스크립트를 실행하는 버튼입니다.
[object Object]	스크립트 작성 공간	실행할 스크립트를 작성하는 공간입니다. 메이커에서 테스트 플레이 중에만 동작합니다.
활용 예시
Lua Executor를 활용한 예시들입니다. 예시를 참고해 크리에이터의 월드에 필요한 스크립트를 작성해 응용할 수 있습니다.

Tween 값 확인
TweenLogic은 UI 연출에 많이 사용되지만 작성한 스크립트의 값만으로는 최종 모습을 상상하기 어렵습니다. 이때 Lua Executor를 활용해 Tween 값을 변경하고, 결과물을 확인하며 원하는 연출값을 찾을 수 있습니다.

[object Object]

Hierarchy - World - ui에 새로운 TestGroup을 추가합니다.

콘텍스트 메뉴를 눌러 Create Entity - Create UISprite를 선택해 새로운 UISprite를 생성합니다.
UISprtie

제작한 UISprite에서 Tween 결과를 확인할 수 있도록 Lua Executor에 아래와 같이 작성합니다.

local entity = _EntityService:GetEntityByPath("/ui/TestGroup/UISprite")
local startY = 90
local goalY = 0
_TweenLogic:PlayTween(startY, goalY, 2, EaseType.ElasticEaseOut, function(y) entity.UITransformComponent.Position.y = y end)
Lua Executor의 실행 공간을 Client로 변경한 뒤 [실행]을 누릅니다.

startY, goalY 값과 EaseType을 변경해 원하는 UI 연출을 찾을 수 있습니다.

카메라 이동
커다란 맵을 만들었을 때는 맵 전체를 돌아보며 월드의 구성이 크리에이터가 생각한 바와 동일하게 만들어졌는지 확인이 필요합니다. Lua Executor를 활용해 테스트 플레이 중에 CameraComponent를 추가해 맵 전경을 확인할 수 있습니다.

camera2

Workspace - MyDesk - Create Model을 눌러 새로운 transformonly 모델을 생성합니다.

TransformComponent를 추가합니다.
[object Object]

Lua Executor에 아래와 같이 작성합니다.

local mapEntity = _EntityService:GetEntityByPath("/maps/map01")

local debugCamera = _SpawnService:SpawnByModelId("model://transformonly", "DebugCamera", Vector3(0,0,0), mapEntity)

local camera = debugCamera:AddComponent("CameraComponent")
_CameraService:SwitchCameraTo(camera)
테스트 플레이를 시작한 뒤 Lua Executor의 Client로 실행 공간을 변경합니다.

Hierarchy - World - Maps - Map01에 추가된 DebugCamera를 선택합니다.
DebugCamera

Property 창에서 CameraComponent의 CameraOffset값을 변경하며 맵 전체를 둘러볼 수 있습니다.
CameraOffset

서버 값 확인
버그 원인을 찾기 위해 서버 값을 재현된 상황에서 확인할 수 있습니다. 예를 들어 플레이어가 몬스터를 공격했으나 몬스터의 체력 값이 변하지 않을 때 몬스터의 상태 변화에 따라 서버 값이 변하는지 확인할 수 있습니다.

[object Object]

확인이 필요한 엔티티의 path를 EntityService를 활용해 얻어옵니다. 아래와 같이 작성합니다.

local monster = _EntityService:GetEntityByPath("/maps/map01/monster-2419_2")
log(monster.Monster.Hp)
[실행]을 누르고, 몬스터 근처로 이동하면, Console 창에서 값을 확인할 수 있습니다.

몬스터 소환
특정 몬스터를 서버에서 소환해 테스트해 볼 수 있습니다.
[object Object]

PresetList - Monster에서 프리셋을 선택한 뒤 콘텍스트 메뉴를 열고 Add to Workspace를 선택합니다.
AddToWorkspace

Workspace에 추가한 몬스터 모델의 Entry ID를 복사해, 몬스터를 소환할 수 있도록 아래와 같이 작성합니다.

local mapEntity = _EntityService:GetEntityByPath("/maps/map01")
for i=1, 10 do
    _SpawnService:SpawnByModelId("model://000000", "TestMonster", Vector3(-7,0,0), mapEntity)
    wait(0.1)
end
Lua Executor의 실행 공간을 Server로 변경하고, [실행]을 누릅니다.

10마리의 몬스터가 소환되는지 확인합니다.

인스턴스 룸 생성 및 테스트
Lua Executor에서 인스턴스 룸을 생성하고, 인스턴스 룸에서 특정 엔티티의 위치를 디버깅해볼 수 있습니다.

map02를 생성하고, 프로퍼티 창에서 MapComponent의 InstanceMap을 활성화합니다.

맵에 디버깅 대상인 새로운 TestTarget 엔티티를 추가합니다.

테스트 플레이를 시작합니다.

CreateInstanceRoom()을 활용해 임시로 인스턴스 룸을 만듭니다. 아래와 같이 작성하고 [실행]을 누릅니다.

_RoomService:CreateInstanceRoom("Test", {"map02"}, 200)
실행 환경에서 Server_Instance_Test를 선택합니다.
Instance Test

EntityService를 활용해 디버깅 대상인 엔티티의 위치를 알 수 있습니다. 아래와 같이 작성하고 [실행]을 누릅니다.

local debug = _EntityService:GetEntityByPath("/maps/map02/TestTarget")
log(debug.TransformComponent.Position)
Console 창에서 로그를 확인할 수 있습니다.
[object Object]
