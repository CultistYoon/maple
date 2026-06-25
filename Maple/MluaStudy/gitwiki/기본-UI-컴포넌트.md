# 기본 UI 컴포넌트

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「기본 UI 컴포넌트」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 07 UI · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
컴포넌트를 조합해 다양한 형태의 UI 엔티티를 구성할 수 있습니다. 이번 과정에서는 UI에서 자주 사용하는 기본 컴포넌트에 대해 알아봅니다.

참고 가이드
UI 에디터

UI 제작하기

UI 엔티티 제어하기

UITransformComponent
UITransformComponent는 UI 엔티티에 반드시 포함되어야 하는 기본 컴포넌트입니다. TransformComponent와 상당히 유사하지만, 스크린 좌표에서 동작한다는 차이점이 있습니다.
주요 프로퍼티는 다음과 같습니다.

UITransform

번호	항목	설명
1	UI 좌표	UI의 위치를 설정합니다. 왼쪽의 Anchor Presets 설정에 따라 필요한 Property가 달라집니다.
월드 좌표와 스크린 좌표의 Anchor Presets 항목에서 더욱 자세한 내용을 확인할 수 있습니다.
2	UIMode	UI 엔티티가 Hierarchy Hierarchy에서 UI 아래에 있으면 Screen으로 고정되고, maps 아래에 있으면 World로 고정됩니다.
출력
SpriteGUIRendererComponent
SpriteGUIRendererComponent는 UI에 이미지 리소스를 표시하는 컴포넌트입니다. 이를 활용해 UI에 '무엇'을, '어떤 형태'로 표시할지 설정할 수 있습니다.
주요 프로퍼티는 다음과 같습니다.

[object Object]

번호	항목	설명
1	ImageRUID	화면에 표시할 ImageRUID를 설정합니다.
2	Type	이미지를 표시하는 방식입니다. Simple, Sliced, Tiled, Filled 중에서 선택할 수 있습니다.
4	OverrideSorting	SortingLayer와 OrderInLayer를 사용할지를 선택합니다. SpriteGUIRendererComponent가 World - maps 하위의 엔티티에 추가된 경우에만 활성화됩니다.
그 외의 다른 프로퍼티를 통해 ImageRUID에서 설정한 이미지를 어떻게 표시할지 설정할 수 있습니다.

TextComponent
TextComponent는 UI에 텍스트를 표시하는 컴포넌트입니다. SpriteGUIRendererComponent와 같이 사용할 경우 SpriteGUIRendererComponent보다 TextComponent를 위에 그립니다. UI 엔티티에 TextComponent가 포함되어 있으면 엔티티를 더블클릭하여 손쉽게 텍스트를 편집할 수 있습니다.
주요 프로퍼티는 다음과 같습니다.

text

번호	항목	설명
1	Font	어떤 폰트로 표시할지 설정합니다.
Default, Maple, Bazzi, Football 중에서 선택할 수 있습니다.
2	FontColor	폰트 색상 및 투명도를 설정합니다.
3	FontSize	폰트 크기를 결정합니다.
4	Text	사용할 텍스트를 적어줍니다.
입력
ButtonComponent
ButtonComponent는 유저의 입력을 받을 때 사용하는 대표적인 컴포넌트입니다. '사용자가 버튼을 눌렀다'라는 입력 정보를 받을 수 있습니다.
주요 프로퍼티는 다음과 같습니다.

ButtonComponent

번호	항목	설명
1	KeyCode	버튼을 누르면 지정한 keyCode를 누른 것처럼 동작합니다.
2	Transition	버튼 상태의 전환 방식을 설정합니다. 전환 방식에 따라 아래에 설정해야 할 프로퍼티가 달라집니다.
ColorTint: 색상 전환
SpriteSwap: 스프라이트 교체
ButtonComponent는 ButtonState를 활용해 버튼의 상태를 변경할 수 있습니다.

Normal, Hover, Pressed, Released, Clicked

ButtonComponent는 출력 기능이 없습니다. 유저에게 버튼이 눌렸음을 인지시키기 위해 SpriteGUIRendererComponent나 TextComponent와 함께 사용합니다. ButtonComponent는 '입력이 되었다'라는 정보만 보내주기 때문에 버튼이 눌린 이후에 '무엇'을 '어떻게' 처리할지는 스크립트에서 정의해야 합니다. 일반적으로 Event를 통해서 버튼 입력을 감지하여 로직을 작성합니다.

주로 활용하는 Event는 다음과 같습니다.

ButtonClickEvent: 버튼을 눌렀을 때 발생하는 이벤트입니다.

ButtonPressedEvent: 버튼을 누르고 있을 때 발생하는 이벤트입니다.

ButtonStateChangeEvent: 버튼의 상태가 변경될 때 발생하는 이벤트입니다.

TextInputComponent
TextInputComponent은 텍스트 입력을 받을 수 있는 컴포넌트입니다.
주요 프로퍼티는 다음과 같습니다.

textinput

번호	항목	설명
1	AutoClear	True 이면 텍스트 입력 후 입력 영역을 자동으로 초기화합니다.
2	ContentType	입력할 수 있는 텍스트 유형을 지정합니다.
Standard : 모든 입력을 허용합니다.
Autocorrected : 모든 입력을 허용하고, 자동 수정을 지원하는 플랫폼에서 자동 수정이 이루어집니다.
IntegerNumber: 숫자만 입력할 수 있습니다.
DecimalNumber: 숫자와 소수점 하나만 입력할 수 있습니다.
Alphanumeric: A-Z, a-z, 0-9를 입력할 수 있습니다.
Name: 첫 번째 글자를 대문자로 표시합니다.
EmailAddress: 하나의 @기호로 구성된 영, 숫자 문자열을 입력할 수 있습니다. 마침표(.)는 연달아 입력할 수 없습니다.
Password: 모든 문자의 입력을 허용하고 별표(asterisk)로 표시합니다.
Pin : 숫자 타입의 입력만 허용하고 별표(asterisk)로 표시합니다.
Custom: 사용자가 직접 유형(Line Type, Input Type, Keyboard Type, 문자열 검증)을 설정할 수 있습니다.
3	LineType	
SingleLine : 한 줄로 입력합니다.
MultiLineSubmit : 여러 줄로 입력할 수 있고 Enter를 입력하면 입력이 종료됩니다.
MultiLineNewline : 여러 줄로 입력할 수 있고 Enter를 입력하면 개행 처리됩니다.
TextInputComponent는 입력만 받기 때문에 입력받은 것을 표시하기 위해서는 TextComponent가 필요합니다. 일반적으로 TextInputComponent와 TextComponent를 함께 사용합니다.
TextInputComponent를 통해 입력받은 텍스트를 어떻게 처리할지는 스크립트에서 정의해야 합니다. TextInputComponent 또한 Event를 통해 텍스트 입력을 감지하여 로직을 작성합니다.

주로 활용하는 Event는 다음과 같습니다.

TextInputEndEditEvent: 입력이 완료되었을 때 발생하는 이벤트입니다. 완전한 문장이나 단어를 받아서 처리할 경우 사용합니다.

TextInputValueChangeEvent : 입력값이 변경될 때 발생하는 이벤트이며, 입력될 때마다 각각의 순간을 감지하여 처리합니다.
