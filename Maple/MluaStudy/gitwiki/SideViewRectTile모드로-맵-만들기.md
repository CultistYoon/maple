# SideViewRectTile모드로 맵 만들기

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「SideViewRectTile모드로 맵 만들기」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 02 지형과이동 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
RectTileMapComponent와 KinematicbodyComponent는 탑다운뷰 게임 제작에는 적합하지만 횡스크롤 게임 제작에는 적합하지 않습니다. SideViewRectTile 모드는 RectTileMap을 활용해 손쉽게 횡스크롤 게임을 제작할 수 있도록 횡스크롤 방식의 이동, 점프, 타일과의 충돌 등을 지원합니다.
이번 시간에는 SideViewRectTile 모드에 대해 알아보고 맵을 제작해봅시다.

더 알아보기
SideViewRectTile 모드는 RectTile 모드를 기반으로 합니다. 본 과정을 살펴보기 전에 먼저 RectTileMap의 활용을 참고해보세요.

SideViewRectTile 모드 변경
SideViewRectTile을 활용하려면 맵 타일 모드를 변경해야 합니다.
맵 타일 모드를 변경하는 첫 번째 방법은 hierarchy Hierarchy에서 현재 편집 중인 맵 엔티티를 선택하고, 우클릭 메뉴에서 Switch To SideViewRectTileMap을 선택하는 것입니다.
sideview1

두 번째 방법은 상단 메뉴의 타일 에디터 버튼을 길게 눌러 타일 모드 선택 메뉴를 연 뒤, SideViewRectTile을 선택하는 것입니다.
sideview2

SideViewRectTile 모드를 선택하면 아래와 같이 scene Scene이 변경됩니다.
scene

SideViewRectTile 맵 만들기
SideViewRectTile 모드로 맵을 만드는 것은 전반적으로 RectTileMap 제작 과정과 동일합니다.
이번 시간에는 아래와 같이 간단한 SideViewRectTile 맵을 만들어봅시다.
sideviewmap

먼저 아래 4개의 이미지를 저장한 뒤, 예제를 살펴봅시다.
tundraRight tundraMid tundraLeft ice

타일 모드를 SideViewRectTile로 변경합니다.


위에서 저장했던 4개의 이미지를 resourcestorage Resource Storage - 내 리소스 - etc에 추가합니다.
rs


preset Preset List - Background에서 back-4를 검색한 뒤 선택하여 맵의 배경을 변경합니다.
bg


타일 셋 팔레트 좌측 상단의 "+" 버튼을 누르고 Create Empty TileSet을 선택합니다. 새 타일 셋의 이름을 TileSet으로 입력합니다.
newtileset


타일 셋 팔레트 하단의 add 타일 추가 버튼을 누른 뒤 Add ResourceStorage Image를 선택합니다.
add


Resource Picker에서 미리 추가해두었던 이미지를 선택합니다.
picker


타일 셋에서 타일을 선택해 원하는 대로 맵을 꾸며줍니다. 맵에 어울리는 오브젝트도 배치합니다.
mapedit


타일 위에 캐릭터가 설 수 있도록 타일을 이동 불가로 설정합니다.
move


play 시작 버튼을 눌러 횡스크롤 이동이 잘 되는지 확인해봅시다.
play

더 알아보기
SideViewRectTile에서의 이동은 SideViewRectTileMap에서 캐릭터 이동 제어를 참고해주세요.
