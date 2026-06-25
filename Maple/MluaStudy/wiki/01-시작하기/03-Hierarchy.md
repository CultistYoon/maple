# Hierarchy

<!-- 출처: reference/TaskWiki.md · 문서 #2 -->


학습 과정 소개
Hierarchy 탭을 이용해 제작 현황을 확인하고, 제작 능률을 높일 수 있습니다.

Hierarchy 소개
Hierarchy 탭은 제작 중인 게임 현황을 계층 구조(부모-자식)로 볼 수 있는 패널입니다. 복잡하게 구성한 맵에서 원하는 엔티티를 빠르게 찾을 때 사용하거나, 체계적으로 엔티티를 관리할 때 사용합니다. 가장 상위인 World 계층 아래에 common, maps, ui 엔트리가 있으며 maps와 ui 엔트리는 각자 기본 하위 엔트리를 가지고 있습니다.

아이콘	이름	설명
workspace_world	World	실제로 제작에 사용한 엔티티들이 모여있으며 가장 상위 계층입니다.
common, maps, ui가 기본 하위 엔트리로 속해 있습니다.
제작 중인 게임의 구성 방식을 확인하고 수정할 수 있습니다.
icon_asset	common	게임 전체에 적용되는 룰을 만들 수 있습니다.
컴포넌트를 추가해 사용합니다.
workspace_maps	maps	맵에 배치한 엔티티들은 맵 엔트리 하위에 위치합니다.
map01은 기본 하위 엔트리로 속해있습니다.
workspace_ui	ui	UI 편집기에서 추가하는 엔티티들이 하위에 위치합니다.
DefaultGroup, PopupGroup, ToastGroup이 기본 하위 엔트리로 속해있습니다.
계층 구조
계층 구조에서는 가장 위의 목록(엔트리)이 부모가 되고, 하위 목록은 자식이 됩니다. 부모-자식 구조는 '부모'가 큰 범위이며, 부모에 속한 것들이 '자식'으로 분류됩니다.
계층 분류는 여러 엔티티가 동일한 속성을 가지고 있을 때 사용하거나, 여러 엔티티를 묶어 하나의 그룹으로 관리하고 싶을 때 사용합니다. 특히 많은 양의 엔티티를 사용할 때 일정한 기준으로 분류한다면 엔티티를 체계적으로 관리할 수 있습니다.
부모-자식 구조는 드래그 앤 드롭을 사용해 만들 수 있습니다. 하나의 엔티티 아래에 자식으로 만들고 싶은 엔티티를 끌어 놓으면 자식으로 편입됩니다. 자식 엔티티들은 부모 엔티티의 영향을 받습니다. 예를 들어, 부모 엔티티의 TransformComponent를 변경하면 자식 엔티티는 자동으로 변경됩니다.

Tip.
단방향으로 영향을 끼칩니다. (부모 → 자식)

드래그 앤 드롭을 사용해 하나의 부모-자식 구조를 만든 뒤, 그 안에 또 다른 부모-자식 구조를 만들 수 있습니다. 동일한 계층으로 있던, 같은 모양의 오브젝트를 부모-자식 구조로 만드는 예시를 살펴보겠습니다. Box1의 자식으로 만든 Box2 아래에 Box3을 자식으로 만들어 이중 계층 구조(부모-자식)를 만들었습니다.

scenemaker03

구조의 특성을 이용해 엔티티를 한 번에 이동하거나, 상위 부모에 안에 속해 있는 부모 만을 골라 형태를 변경할 수 있습니다. 아래의 예시에서는 3가지 동작을 보여주고 있습니다.

예시에서는 Box1을 선택해 나머지 오브젝트까지 한꺼번에 움직인다.

Box2를 선택해 Box3까지 함께 오브젝트를 돌리고, 확대한다.

Box4만 선택해 따로 움직인다.

위 3가지 동작 모두 계층 구조의 특징을 활용한 것입니다. 부모를 선택했을 때는 자식이 영향을 받기 때문에 이중 구조 안에 있는 자식까지 모두 영향을 받지만, 자식은 부모 계층에 영향을 끼칠 수 없기 때문에 자식을 선택하면 자식만 상태를 변경할 수 있게 됩니다.

box1

이런 구조는 여러 개의 엔티티를 이용해 특정 UI나, 구조물을 만들 때 유용하게 사용할 수 있습니다. 예를 들어, 확인 메시지 창을 만든다고 했을 때 전체 배경을 부모로 만들고, 버튼 배경과 텍스트를 부모-자식 구조로 만든다면, 하나의 버튼을 옮기거나 바꾸고 싶을 때 다른 메시지 창 엔티티들은 영향을 받지 않습니다.

Hierarchy 검색 기능
검색 창은 탭 타이틀 바로 아래에 위치합니다. 검색 기준에 따라 다른 결괏값이 나오기에 필요에 따라 선택해 검색합니다.검색 기준은 Name과 Component 두 가지이며, 다음과 같이 사용합니다.

Name : Workspace의 전 영역에서 검색한 이름과 맞는 값을 찾을 때 사용합니다.

Component : 엔티티 중 검색어에 해당하는 컴포넌트가 포함된 값을 찾을 때 사용합니다.

Name "chat" 검색	Component "chat" 검색
hierachy01	hierachy02
엔트리 별 콘텍스트 메뉴
Hierarchy의 상위 엔트리 별 콘텍스트 메뉴는 다음과 같습니다. 하위 엔티티는 특성에 따라 다른 목록이 추가로 활성화됩니다.

엔트리 이름	메뉴 목록	설명
World	Create Entity	새로운 엔티티를 생성합니다.
Create Entity as Child	하위에 새로운 엔티티를 생성합니다.
Property	World의 프로퍼티 에디터 창을 엽니다.
Go To Entity	선택한 엔티티로 이동합니다.
Copy Entity ID	엔티티 아이디를 복사합니다.
common	Create Entity	새로운 엔티티를 생성합니다.
Create Entity as Child	하위에 새로운 엔티티를 생성합니다.
Property	common의 프로퍼티 에디터 창을 엽니다.
Go To Entity	선택한 엔티티로 이동합니다.
Add Component	common에 컴포넌트를 추가합니다.
Add New Component	common에 새로운 컴포넌트를 추가합니다
Copy Entity Path	엔티티 경로를 복사합니다.
Copy Entity ID	엔티티 아이디를 복사합니다.
maps	Create New Map	새로운 맵을 생성합니다.
Create Entity	새로운 엔티티를 생성합니다.
Create Entity as Child	하위에 새로운 엔티티를 생성합니다.
Property	maps의 프로퍼티 에디터 창을 엽니다.
Go To Entity	선택한 엔티티로 이동합니다.
Copy Entity Path	엔티티 경로를 복사합니다.
Copy Entity ID	엔티티 아이디를 복사합니다.
map01	Create New Map	새로운 맵을 생성합니다.
Create Entity	새로운 엔티티를 생성합니다.
Create Entity as Child	하위에 새로운 엔티티를 생성합니다.
Switch To RectTileMap	RectTileMape으로 전환합니다.
Switch To SideViewRectTileMap	SideViewRectTileMap으로 전환합니다.
Duplicate	맵을 복사합니다.
Rename	map01의 이름을 변경할 수 있습니다.
Property	map01의 프로퍼티 에디터 창을 엽니다.
Go To Entity	선택한 엔티티로 이동합니다.
Add Component	map01에 컴포넌트를 추가합니다.
Add New Component	map01에 새로운 컴포넌트를 추가합니다.
Copy Entity Path	엔티티 경로를 복사합니다.
Copy Entity ID	엔티티 아이디를 복사합니다.
ui	Create Entity	새로운 엔티티를 생성합니다.
Create Entity as Child	하위에 새로운 엔티티를 생성합니다.
Property	ui의 프로퍼티 에디터 창을 엽니다.
Go To Entity	선택한 엔티티로 이동합니다.
Copy Entity Path	엔티티 경로를 복사합니다.
Copy Entity ID	엔티티 아이디를 복사합니다.
