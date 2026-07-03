# Workspace

<!-- 출처: reference/TaskWiki.md · 문서 #0 -->


학습 과정 소개
Workspace를 이용해 엔티티, 스크립트, 이미지를 효율적으로 관리할 수 있습니다.

참고 가이드
Entity, Component, Property
Model

Workspace 소개
Workspace는 폴더 형식의 리소스 관리 공간입니다. 필요한 것을 찾을 수 있는 Workspace는 효율적인 월드 제작을 위해 필요합니다. Workspace 패널의 기본 위치는 우측 중앙입니다. 크리에이터의 편의에 따라 원하는 위치로 바꿀 수 있습니다.
Workspace는 메이커에서 제공하는 모델과 스크립트 등이 저장된 BaseEnvironment와 크리에이터가 만든 리소스를 보관하는 MyDesk로 구성되어 있습니다. 또한 작업의 편의를 위해 DefaultPlayer를 제공합니다.

Tip.
메이커에서 Workspace 패널이 보이지 않을 때는 Panels - Workspace를 클릭하세요.

Workspace

Workspace의 상위 폴더(엔트리)는 다음과 같습니다.

아이콘	이름	설명
workspace_MyAvatar	DefaultPlayer	NativeModel에 있는 Player의 정보를 참조하고 있습니다. 실제 생성한 플레이어 아바타 엔티티는 World 안에 속합니다.
시작 시 스타트 포인트에 플레이어 아바타를 생성합니다.
workspace_NativeFolder	BaseEnviroment	메이커에서 제공하는 기본 Component, Service, Logic, Event가 저장되어 있습니다.
workspace_UserFolder	MyDesk	크리에이터가 추가한 리소스, BaseEnvironment에서 확장, 복제한 모델, 컴포넌트 등이 추가됩니다.
WorldConfig에서 월드의 설정을 변경할 수 있습니다.
새롭게 추가한 리소스는 MyDesk 폴더 하위에 저장됩니다. 필요할 때 폴더를 추가하여 효율적으로 리소스를 관리할 수 있습니다.
Workspace 검색
Common_search01검색 창에 검색어를 입력해 빠르게 원하는 리소스나 모델을 찾을 수 있습니다.

검색 기준은 이름입니다.

검색 범위는 Workspace 전체입니다.

검색어를 입력하면 조건에 맞는 결과만 나타납니다.
workspace007

WorldConfig
월드의 설정을 변경할 수 있습니다. WorldConfig의 설정은 추가될 수 있습니다. WorldConfig를 누르면, 프로퍼티 에디터 창에 변경할 수 있는 설정이 나타납니다. WorldConfig의 자세한 기능은 WorldConfig 가이드를 참고하세요.

LegacyAnimation: 캐릭터에 이전 메이플스토리 월드 움직임과 애니메이션을 적용합니다.

PlayerEntityAuthorityCheck: 플레이어 엔티티에 속한 Component들의 Server 함수들을 로컬 Client 이외의 Client에서 호출하지 못하도록 변경합니다. 이 설정을 활성화 함으로써 좀 더 높은 보안 수준을 제공합니다.

ServiceAuthorityCheck: Native에서 동작하는 Service의 모든 Server 함수들을 ServerOnly 함수로 동작하도록 변경합니다. 이 설정을 활성화 함으로써 좀 더 높은 보안 수준을 제공합니다.

SourceLanguage: 플레이어가 월드에서 자동 번역 기능을 사용한다면 SourceLanguage의 언어를 번역 대상으로 삼습니다. 현재 원문 언어로 설정할 수 있는 언어는 한국어, 영어입니다. 추후 언어가 추가될 수 있습니다.

BaseEnvironment
메이커에서 기본 제공하는 기능을 모아 둔 폴더입니다. 총 2개의 폴더로 구성되어 있습니다.

NativeScripts

NativeModel

BaseEnvironment의 폴더 순서를 바꾸거나, 하위 목록을 옮길 수 없습니다.
NativeScripts의 모든 계층은 복제/삭제할 수 없습니다. NativeScripts의 특성을 변경해 사용하려면 해당 스크립트를 확장(Extend)하여 사용해야 합니다. 또한 NativeModel은 복제하거나 확장해 활용할 수 있습니다.

BaseEnvironment의 주요 엔트리는 다음과 같습니다.

아이콘	이름	설명
workspace_LockedNativeFolder	NativeScripts	Component, Service, Logic, Event, Misc가 하위 폴더로 저장되어 있습니다.
이 폴더에 속한 스크립트들은 삭제할 수 없습니다.
Component는 확장할 수 있으며 확장 컴포넌트는 MyDesk 폴더에 저장됩니다.
workspace_LockedNativeFolder	Component	수정, 삭제할 수 없는 기본 컴포넌트가 저장된 폴더입니다.
Component는 확장해 사용할 수 있습니다.
workspace_LockedNativeFolder	Service	수정, 삭제할 수 없는 기본 서비스가 저장된 폴더입니다.
workspace_LockedNativeFolder	Logic	수정, 삭제할 수 없는 기본 로직이 저장된 폴더입니다.
workspace_LockedNativeFolder	Event	수정, 삭제할 수 없는 기본 이벤트가 저장된 폴더입니다.
workspace_LockedNativeFolder	Misc	기타 스크립트가 저장된 폴더입니다.
workspace_NativeFolder	NativeModel	메이커에서 제공하는 기본 모델들이 저장된 폴더입니다. 모델을 Scene으로 배치해 바로 사용합니다.
다른 폴더로 이동하거나, 모델을 만들 순 없으나, 필요에 따라 복제/확장 모델로 응용해 활용할 수 있습니다.
확장 모델은 MyDesk 폴더에 저장됩니다.
MyDesk
MyDesk는 크리에이터가 직접 추가한 음악, 스크립트, 이미지 파일과 확장 컴포넌트 등을 모아서 관리하는 곳입니다.
MyDesk는 일종의 저장소이며, 어떤 것을 추가했을 때 동일한 계층으로 추가가 됩니다. 한 곳에 모아 관리하고 싶다면 MyDesk 내에 새 폴더를 생성해봅시다.

Tip.
Workspace는 저장소, Hierarchy는 작업 현황 개념입니다.
MyDesk에 추가한 리소스를 월드에 배치하면, Hierarchy에 엔티티가 만들어집니다.
MyDesk의 원본을 삭제했을 때 원본 정보를 참조하고 있는 엔티티에서 해당 정보는 지워지지만, 생성된 엔티티는 남습니다
만약 MyDesk에서 바로 배치했던 엔티티라면, 해당 엔티티(리소스)의 이름 옆에 Missing이 붙으며, 빨간색으로 변합니다.
workspace002

UIPopup과 UIToast는 크리에이터가 자유롭게 수정하거나 삭제할 수 있는 로직입니다. 제작 배경에 따라 필요 없을 때 자유롭게 삭제할 수 있습니다. 필요에 따라 확장하거나, 복제할 수 있습니다.

아이콘	이름	설명
workspace_logic	UIPopup	팝업 메시지 로직입니다. 필요에 따라 원 로직을 수정하거나 삭제할 수 있습니다.
workspace_logic	UIToast	토스트 메시지 로직입니다. 필요에 따라 원 로직을 수정하거나 삭제할 수 있습니다.
MyDesk에 리소스 추가하기
검색 창 왼쪽의 [+] 버튼을 클릭해 콘텍스트 메뉴를 엽니다.

원하는 항목을 선택합니다.

Workspace의 MyDesk 하위에 새로운 항목이 추가됩니다.

Tip.
크리에이터가 직접 추가하는 리소스는 모두 변경할 수 있기 때문에 모두 MyDesk 안에 생성됩니다.

workspace05

MyDesk 폴더 삭제
비어있는 폴더는 바로 삭제할 수 있습니다.
리소스가 들어있는 폴더를 삭제하면, 폴더 안의 모든 리소스가 함께 삭제됩니다. 실수를 방지하기 위해 리소스가 든 폴더를 삭제할 때는 Delete를 누른 뒤, 경고 창에서 [예] 버튼을 눌러 삭제합니다.

workspace04

Workspace 콘텍스트 메뉴
콘텍스트 메뉴 목록은 다음과 같습니다.

DefaultPlayer 주요 콘텍스트 메뉴
목록	설명
Duplicate	DefaultPlayer를 복제한 모델을 생성합니다.
Open	Player의 상태 혹은 변경 점을 확인하기 위해 사용합니다.
Add Component	DefaultPlayer에 컴포넌트를 추가합니다.
Add New Component	새로운 컴포넌트를 생성한 후 DefaultPlayer에 추가합니다.
Extend	DefaultPlayer의 확장 모델을 생성합니다.
Copy Entry ID	DefaultPlayer의 ModelID를 복사합니다.
BaseEnvironment 주요 콘텍스트 메뉴
잠겨 있는 폴더에서는 콘텍스트 메뉴가 열리지 않습니다.

목록	설명
Duplicate	NativeModel을 복제합니다.
Open	선택한 항목을 엽니다.
Add Component	NativeModel에 컴포넌트를 추가합니다.
Add New Component	NativeModel에 새로운 컴포넌트를 추가합니다.
Place to Hierarchy	선택한 모델을 Scene에 배치합니다.
Extend	선택한 모델의 확장 모델을 생성합니다.
Copy Entry ID	선택한 모델의 ID를 복사합니다.
MyDesk 콘텍스트 메뉴
목록	하위 목록	설명
Create Folder	-	새로운 폴더를 생성합니다.
Create Scripts	Create Component	새로운 스크립트 컴포넌트를 생성합니다.
Create EventType	새로운 이벤트 타입을 생성합니다.
Create ItemType	새로운 아이템 타입을 생성합니다.
Create BTNodeType	새로운 BTNode타입을 생성합니다.
Create StateType	새로운 StateType타입을 생성합니다.
Create StructType	새로운 StructType타입을 생성합니다.
Create Logic	새로운 로직을 생성합니다
Create Script	처음부터 스크립트를 입력할 수 있는 탑 레벨 스크립트를 생성합니다.
Create DataSet	-	새로운 DataSet을 생성합니다.
Create TileDataSet	-	새로운 TileDataSet을 생성합니다.
Create AtlasBlueprint	-	새로운 AtlasBlueprint를 생성합니다.
Create Material	-	새로운 머티리얼을 생성합니다.
Create Model	-	비어있는 새로운 모델을 생성합니다. 직접 컴포넌트를 추가합니다.
Copy Entry ID	-	선택한 엔트리의 ID를 복사합니다.
Import From	Import Scripts	PC에서 스크립트를 불러옵니다.
Import Image	PC에서 이미지 파일을 불러옵니다.
Import Sound	PC에서 사운드 파일을 불러옵니다.
Import Package	PC에서 패키지를 불러옵니다.
