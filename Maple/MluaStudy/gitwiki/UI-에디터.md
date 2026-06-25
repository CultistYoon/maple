# UI 에디터

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「UI 에디터」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 07 UI · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
UI를 편집할 수 있는 UI 에디터와 UI Group에 대해 알아봅시다.

참고 가이드
UI 엔티티 제어하기

기본 UI 컴포넌트

UI 제작하기

UI 에디터 소개
UI 에디터는 UI 엔티티를 구성하고, 메이플스토리 월드에서 제공하는 UI 엔티티를 조합해서 인벤토리나 상점 UI를 제작할 수 있습니다.
UI 에디터 구성은 다음과 같습니다.

uieditor01

번호	이름	설명
NO01	Preset List	메이커에서 제공하는 다양한 UI Preset을 활용할 수 있습니다.
NO_02	UI 경로 정보	선택된 UI 엔티티의 경로 정보를 알 수 있습니다.
부모 경로 선택 시 해당 엔티티가 선택됩니다.
NO_03	캔버스	UI 엔티티를 배치하고 편집하는 작업 공간입니다.
게임 실행 시 캔버스에 배치된 모습대로 게임 화면에 출력됩니다.
NO_04	기본 도구	이미지나 버튼과 같은 UI 엔티티를 배치할 수 있습니다.
NO_05	UI Groups 패널	UIGroup 선택 및 추가/삭제를 할 수 있습니다.
UI 에디터 전환
상단 메뉴에서 [UI] 버튼을 눌러 UI 에디터로 전환할 수 있습니다. Scene 화면이 UI 에디터용 화면으로 변경됩니다.
[object Object]

UIGroup
UIGroup은 UITransformComponent, UIGroupComponent, CanvasGroupComponent로 구성되어 있습니다. UIGroup은 일종의 폴더 역할을 하므로, Hierarchy와 UI Groups에서의 순서 영향을 받을 받지 않습니다. UI 에디터를 활성화하면, UI Groups 패널 창은 생성한 UI를 관리할 수 있습니다. 새로운 UI 그룹을 추가하면, Hierarchy, UIGroup에 모두 반영됩니다.

UIGroup에서는 기본적으로 3개의 그룹을 제공합니다.

ToastGroup: 크리에이터의 편의를 위해 제공하는 UI 그룹입니다. UIToast 로직에 연결되어 있습니다.

PopupGroup: 크리에이터의 편의를 위해 제공하는 UI 그룹입니다. UIPopup 로직에 연결되어 있습니다.

DefaultGroup: 항상 활성화된 UI 그룹입니다. 채팅창이나 공격, 점프 같은 필수 버튼이 DefaultGroup에 배치되어 있습니다. 크리에이터의 의도에 따라 다른 그룹을 DefaultGroup로 설정할 수 있습니다.

UI Groups 패널
UI Groups 패널에서 제작 중인 UIGroup의 섬네일을 확인할 수 있습니다. 또한 UIGroup 이름을 변경할 수 있습니다. UI Groups에서 변경한 이름은 Hierarchy에도 반영됩니다. 그룹을 선택하면 UI 에디터 화면이 해당하는 그룹으로 변경되어 편집할 수 있습니다.

112

Hierarchy - ui
Hierarchy에서는 UIGroup에 속한 UI 엔티티들을 부모-자식 관계로 확인할 수 있습니다. UI 엔티티의 컴포넌트를 편집하거나, UI 엔티티의 부모-자식 관계를 변경할 수 있습니다.

[object Object]

UIGroup 상시 활성화
UIGroupComponent의 DefaultShow 프로퍼티를 활용해 노출 여부를 설정할 수 있습니다. DefaultShow 프로퍼티를 trueEditbox_Check로 설정하면 해당 UIGroup에 속한 UI들은 늘 보이는 상태가 됩니다.

uieditor17

UI 엔티티
UI 엔티티를 생성하는 방법은 두 가지입니다. 기본 UI 엔티티를 사용하거나, UI 프리셋을 사용할 수 있습니다.

기본 UI 엔티티
기본 UI 엔티티는 UI 제작 시 가장 많이 사용하는 기능을 제공합니다. 이미지, 버튼, 스크롤 뷰, 텍스트, 입력 텍스트로 구성되어 있습니다. 크리에이터는 여러 개의 UI 엔티티를 조합해 새로운 UI를 만들 수도 있습니다. 기본 UI 컴포넌트 가이드를 참고하세요.

[object Object]

아이콘	UI 모델 이름	기능 설명	포함된 컴포넌트
workspace_image	이미지	UI에 원하는 이미지를 출력합니다. 주로 아이콘 표시를 위해 사용합니다.	
UITransformComponent
SpriteGUIRendererComponent
UiButton	버튼	클릭/터치 시 특정 액션이나 기능을 수행하도록 합니다.	
UITransformComponent
SpriteGUIRendererComponent
ButtonComponent
Ui_ScrollRect	스크롤뷰	많은 양의 정보를 리스트 형태 또는 그리드 형태로 정렬합니다. 예) 인벤토리, 상점	
UITransformComponent
SpriteGUIRendererComponent
ScrollLayoutGroupComponent
Ui_Text	텍스트	UI에 텍스트 표시하기 위해 사용합니다.	
UITransformComponent
SpriteGUIRendererComponent
TextComponent
Ui_InputField	입력 텍스트	유저가 텍스트를 입력할 수 있습니다. 예) 검색 창, 아이디, 비밀번호 입력 창	
UITransformComponent
SpriteGUIRendererComponent
TextComponent
TextInputComponent
UI Preset
메이플스토리 월드에서는 기능 별 UI를 프리셋으로 제작해 제공하고 있습니다. 프리셋에는 UI와 스크립트가 함께 포함되어 있으므로 프리셋을 배치하면, 포함된 컴포넌트가 MyDesk에 추가됩니다. 프리셋을 배치한 뒤, 제작 중인 월드에 맞게 UI와 스크립트를 수정할 수 있습니다.
