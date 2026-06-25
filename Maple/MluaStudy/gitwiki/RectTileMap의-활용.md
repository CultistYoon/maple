# RectTileMap의 활용

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「RectTileMap의 활용」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 02 지형과이동 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
메이플스토리 월드에서는 RectTileMap 모드를 활용해 횡스크롤이 아닌, 탑다운 뷰의 월드를 제작할 수 있습니다. 이번 시간에는 RectTileMap에 대해 알아봅시다.

RectTileMap과 플레이어 이동
메이플스토리 월드에서는 MapleTile, RectTile, SideViewRectTile 모드로 지형을 만들 수 있습니다.

MapleTile

메이플스토리 형태의 횡스크롤 맵을 만들 수 있습니다. RigidbodyComponent가 플레이어의 이동을 제어합니다.

RectTile

탑다운 뷰 맵을 만들 수 있습니다. 플레이어는 상하좌우 이동을 하며 KinematicbodyComponent가 플레이어의 이동을 제어합니다.

SideViewRectTile

RectTile을 기반으로 하지만 플레이어는 횡스크롤 방식으로 이동합니다. SideviewbodyComponent가 플레이어의 이동을 제어합니다.

1
MapleTileMap과 달리 RectTileMap 환경에서는 일반적으로 플레이어가 상하좌우로 이동합니다. KinematicbodyComponent가 플레이어의 상하좌우 이동 및 점프, 타일과의 충돌 등을 지원합니다. 따라서 RectTileMap에서는 KinematicbodyComponent가 플레이어 엔티티에 활성화되어 있어야합니다.
현재 DefaultPlayer에는 RigidbodyComponent, KinematicbodyComponent, SideviewbodyComponent가 모두 포함되어 있기 때문에, 맵 모드에 따라 이동 컨트롤의 주체가 달라집니다.

더 알아보기
RectTileMap에서의 이동에 대해서는 RectTileMap에서 캐릭터 이동 제어를 참고해주세요.

RectTileMap 모드 변경
아래 두 가지 방법 중 하나를 택해 RectTileMap 모드로 변경할 수 있습니다.

1. Hierarchy에서 변환	2. 타일 에디터 버튼 눌러 변환
Hierarchy - 원하는 맵의 콘텍스트 메뉴 - Switch To RectTileMap 선택
2	타일 에디터 버튼 1초 이상 클릭 - RectTile 모드 선택
sideview2
타일 셋 제작과 편집
타일 셋 추가와 편집
타일을 배치하려면 먼저 타일 셋을 만들어야 합니다.
타일 셋 팔레트에서 새로운 타일 셋을 만들고 편집할 수 있습니다.

타일 셋 팔레트에서 [+] 버튼을 눌러 타일 셋을 생성합니다.
newtileset


Workspace - MyDesk에 NewTileSet이 생성됩니다.
타일 셋의 이름을 자유롭게 변경합니다. (예: TileSetExample)
001


타일 셋 팔레트의 드롭박스에서 새 타일 셋을 선택합니다. (처음 생성한 타일 셋은 자동으로 선택됩니다.)
7

타일 셋에 타일 추가
새 타일 셋에 원하는 타일을 추가해봅시다.

RosourceStorage로 타일 추가

타일 셋 팔레트 하단의 addtile_rect 버튼 클릭 - Add ResourceStorage Image를 클릭하면 Resource Picker가 열립니다.
8


Resource Picker - MSW 리소스 탭에서 기본 제공하는 스프라이트를 타일로 추가합니다.
9

Workspace의 이미지를 타일로 추가

타일 셋 팔레트 하단의 addtile_rect 버튼 클릭 - Add Workspace Image를 클릭하면 Reference가 열립니다.
11


Reference에서 이미지를 선택해 타일로 추가합니다.
12

Atlas Unpacker로 타일 추가
Atlas Unpacker에서 아틀라스를 잘라 렉트타일 셋에 추가를 선택하면 타일로 사용할 수 있습니다. 아틀라스를 자르는 방법은 아틀라스 활용하기를 참고하세요
자른 스프라이트가 선택한 타일 셋에 각각의 타일로 추가됩니다.
12

타일 속성 설정
타일 편집 모드로 변환하면 타일 속성을 설정할 수 있습니다.
타일 셋 팔레트 오른쪽 상단의 편집 버튼을 누르면 타일 편집 모드로 변환됩니다.
12

타일 이름 변경
타일 하단 텍스트를 더블 클릭하면 해당 타일의 이름(예: Tile02)을 설정할 수 있습니다.
타일 이름은 스크립트로 타일을 생성할 때 사용됩니다.
13

스프라이트 편집
추가한 타일의 스프라이트 이미지를 변경할 수 있습니다.

스프라이트 편집 체크 박스 클릭 - [타일 편집] 버튼 클릭 - Resource Picker가 열립니다.
00


Resource Picker에서 변경하려는 스프라이트를 선택하면 타일 이미지가 해당 스프라이트로 바뀝니다.
001
이미 맵에 배치한 타일의 스프라이트를 변경하면, 해당 타일도 함께 바뀝니다.
16

이동 가능 타일 편집
플레이어가 이동 가능한 타일인지를 설정할 수 있습니다.
이동 가능 타일 편집 체크 박스를 선택하면 속성을 편집할 수 있습니다.
17

화살표 버튼을 클릭하면 이동 가능 속성이 변경됩니다.

green : 플레이어가 이동할 수 있는 타일

red : 플레이어가 이동할 수 없는 타일
18

타일 셋에 포함된 타일 제거
타일 셋 팔레트에서 제거할 타일을 선택하고 [삭제] 버튼을 누릅니다.
19

타일 그리기
타일 배치 하기
타일 셋 팔레트에서 원하는 타일을 선택한 후 드래그하여 타일을 배치합니다.
20

편리한 타일 배치
타일을 쉽게 배치하기 위해 4가지 기능을 이용할 수 있습니다. 기본 위치는 Scene의 왼쪽 상단입니다.

아이콘	설명
brush	타일이 그리는 움직임에 맞게 그려집니다.
tilefill	설정한 사각형 크기에 타일이 그려집니다.
tilemarquee	설정한 원형 안에 타일이 그려집니다.
timepaint	선택한 타일이 맵 전체에 배치됩니다.
배치한 타일 삭제
타일을 우클릭하여 삭제할 수 있습니다.
우클릭 드래그 하면 드래그한 위치에 있던 타일이 모두 삭제됩니다.
21

타일 격자 크기 설정
타일 격자 크기는 현재 편집 중인 맵 하위의 RectTileMap 엔티티 - RectTileMapComponent - GridSize에서 설정할 수 있습니다.

GridSize (x = 1, y = 1)	GridSize (x = 0.5, y = 0.5)
22	23
24	25
레이어 설정
레이어를 추가하면 이미 배치한 타일 위에 다른 타일을 배치할 수 있습니다.

레이어 추가
Map Layer 패널 하단의 [+] 버튼을 누르면 새로운 맵 레이어가 추가됩니다.
Hierarchy - 맵 엔티티에 새 RectTileMap 엔티티도 추가됩니다.
26


새 레이어 선택 후 타일을 배치하면, 이전 타일 맵 위에 다른 타일을 배치할 수 있습니다.
27

레이어 별 타일 셋 적용
레이어를 추가하면 기본적으로 이전 타일 셋을 공용으로 사용합니다. 그래서 특정 타일의 속성을 변경하면 의도치 않게 다른 레이어의 타일 속성까지 변경하는 경우가 생깁니다.
예를 들어, 레이어 1에 타일 셋 1을 적용 중일 때 레이어 2를 생성하면 레이어 2에도 타일 셋 1이 적용됩니다.
레이어 1에 배치한 특정 타일의 이미지를 변경하려고 타일 셋 1의 타일 속성을 변경하면 레이어 2의 타일도 함께 변경됩니다.
이러한 상황을 피하려면 레이어 별로 각각 다른 타일 셋을 적용하는 것이 좋습니다.
28

레이어마다 다른 타일 셋을 추가하는 방법은 아래와 같습니다.

기존 타일 셋이 있는 상태에서 새로운 타일 셋을 추가합니다. (예: TileSetExample2)
새 타일 셋에 몇 가지 타일도 함께 추가합니다.
29


새로운 맵 레이어를 추가합니다. (예: Layer 2)
30


추가한 레이어를 선택한 상태에서 새 타일 셋(예: TileSetExample2)을 선택합니다. 그러면 새 레이어에는 새 타일 셋이 적용됩니다. 이후 새 레이어에 타일을 배치해봅니다.
32


Hierarchy의 RectTileMap 또는 Map Layer에서 레이어를 차례로 선택해 봅니다.
타일 셋 팔레트에서 RectTileMap 마다 서로 다른 타일 셋이 적용된 것을 확인합니다.
33

스크립트를 활용한 타일 동적 생성
RectTileMap 엔티티의 RectTileMapComponent는 타일을 배치하거나 월드 좌표를 타일 좌표로 변환하는 등 여러가지 기능을 제공합니다.
RectTileMapComponent를 활용해 타일을 동적으로 배치해봅시다.

예제 개요

맵에는 기본적으로 Sand 타일이 깔려있다.

플레이어가 Sand 타일 위를 돌아다니며 특정 키를 누를 때마다 플레이어가 위치한 타일을 다른 타일로 교체한다.

z 키 : Grass 타일 배치

x 키 : Rock 타일 배치


맵을 RectTileMap 모드로 변환합니다.
2


새로운 타일 셋을 추가하고 이름을 DefaultTileSet으로 설정합니다.
35


타일 셋 팔레트 하단의 addtile_rect 버튼 클릭 - Add ResourceStorage Image를 클릭하여 Resource Picker를 엽니다.
8


아래 이미지를 저장합니다.
37-1 37-2 37-3
Resource Picker - etc 폴더에 저장한 이미지를 드래그하여 스프라이트를 추가합니다.
38


추가한 스프라이트를 차례로 선택하면 타일이 추가됩니다.
40


타일 셋 팔레트에서 타일 편집 버튼을 클릭합니다.
추가된 타일의 이름을 다음과 같이 설정합니다.
41

스프라이트	이름
37-1	Sand
37-2	Grass
37-3	Rock


타일 속성 편집 버튼을 다시 한번 클릭하여 편집 모드를 종료합니다.
Sand 타일을 선택하여 다음과 같이 배치합니다.
42


Workspace에 새 스크립트 컴포넌트를 추가하고 이름을 EditRectTile로 입력합니다.
43


DefaultPlayer에 EditRectTile 컴포넌트를 추가합니다.
44


EditRectTile 스크립트 컴포넌트를 엽니다.
ChangeCurrentTile() 함수를 추가하고 string 타입의 매개 변수 tileName도 추가합니다.
이후 함수를 아래와 같이 작성합니다.

[server]
void ChangeCurrentTile(string tileName)
{
    if  tileName == nil then 
        return 
    end

    local pos = self.Entity.TransformComponent.Position
    local tilemap = _EntityService:GetEntityByPath("/maps/map01/RectTileMap").RectTileMapComponent

    -- 월드 공간 좌표를 타일맵 공간 좌표로 변환
    local cellPos = tilemap:ToCellPosition(pos)

    -- 현재 플레이어가 위치한 타일의 정보 반환
    local tileInfo = tilemap:GetTile(cellPos)

    if tileInfo ~= nil then
        tilemap:SetTile(tileName, cellPos.x, cellPos.y)
    end
}


Event Handler에서 KeyDownEvent를 추가하고, 내용을 다음과 같이 작성합니다.

Event Handler : 
[service: InputService]
HandleKeyDownEvent(KeyDownEvent event)
{
    -- Parameters
    local key = event.key
    --------------------------------------------------------
    if key == KeyboardKey.Z then
        self:ChangeCurrentTile("Grass") -- Z키 : Grass 타일 배치
    elseif key == KeyboardKey.X then
        self:ChangeCurrentTile("Rock") -- X키 : Rock 타일 배치
    end
}


start [시작] 버튼을 누른 뒤 테스트해 봅시다.
플레이어를 움직이며 Z나 X 키를 눌러봅니다.
플레이어가 위치한 지점의 타일이 변경되는 것을 확인합니다.
