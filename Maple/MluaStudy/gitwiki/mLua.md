# mLua

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「mLua」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 01 시작하기 · 출처: MapleStory Worlds 공식 위키_

---

mLua는 프리뷰 기능으로 정식 출시 시 기능이 변경될 수 있습니다.
학습 과정 소개
메이플스토리 월드 메이커를 벗어나 외부 편집기에서 스크립트를 작성하기 위해서는 mLua 문법에 맞게 작성해야 합니다.
mLua의 문법에 대해 알아봅시다.

참고 가이드
LocalWorkspace
ExtendedScriptFormat
mLua Extension
공동 제작

mLua
MSW 메이커의 스크립트 엔트리를 표현하기 위한 프로그래밍 언어입니다.

정의문
스크립트 정의문
스크립트 정의문을 사용하여 스크립트를 정의할 수 있습니다. 스크립트 정의문의 문법은 다음과 같습니다.

script 타입이름

end
상속 관계가 있다면 extends를 붙여 어떤 타입으로부터 상속받았는지 명시할 수 있습니다. extends가 있는 스크립트 정의문의 문법은 다음과 같습니다.

script 타입명 extends 타입명
 
end
프로퍼티 정의문
프로퍼티 정의문을 통해 스크립트의 프로퍼티를 정의할 수 있습니다. 프로퍼티 정의문에서 우측 식은 일부 타입을 제외하고 반드시 작성해야 합니다.
SyncTable 타입은 할당이 불가능한 타입이므로 우측 식 작성을 생략합니다.

property 타입명 이름 = 식
메소드 정의문
메소드 정의문을 통해 스크립트의 메소드를 정의할 수 있습니다. 메소드 정의문의 문법은 다음과 같습니다.

method 빈환타입명 메소드이름(파라미터타입명 파라미터이름)

end
사용 예시

method string NewMethod(number num)
    return ""
end
이벤트 핸들러 정의문
이벤트 핸들러 정의문을 통해 스크립트의 이벤트 핸들러를 정의할 수 있습니다. 이벤트 핸들러 정의문 문법은 다음과 같습니다.

handler 핸들러이름(이벤트타입명 파라미터이름)

end
사용 예시

handler HandleEvent(KeyDownEvent event)

end
Attribute문
Attribute문을 사용해 스크립트, 멤버에 다양한 기능을 지정할 수 있습니다. 하나의 멤버에 복수의 Attribute문을 사용할 수 있습니다.
Attribute문 문법은 다음과 같습니다.

@AttributeName
사용 예시

@Sync
property string NewValue = nil
Attribute는 파라미터가 있을 수 있습니다. 파라미터가 있는 Attribute문의 문법은 다음과 같습니다.

@AttributeName(인수)
사용 예시

@ExecSpace("Server")
method void OnBeginPlay()

end
Attribute
mLua에서 스크립트 멤버에 동기화, 실행제어, 최솟값, 최댓값과 같은 기능을 적용하려면 Attribute를 사용해야 합니다.
하나의 멤버에 복수의 Attribute를 지정할 수 있습니다.

Sync Attribute
프로퍼티에 동기화 여부를 지정합니다. 적용 대상은 프로퍼티입니다. 적용 대상은 동기화 가능한 Property 타입의 프로퍼티입니다. 적용 가능 타입은 Component, Logic, BTNode입니다.

매개 변수: 없음

@Sync
Property string NewValue = nil
TargetUserSync Attribute
특정 타겟에 대한 동기화 여부를 지정합니다. 적용 대상은 동기화 가능한 Property 타입의 프로퍼티, 컴포넌트입니다.

매개 변수: 없음

@TargetUsrSync
ExecSpace Attribute
메소드와 이벤트 핸들러의 실행제어 공간을 지정합니다. 파라미터는 string으로 지정된 문자열로만 사용이 가능합니다. 적용 대상은 메소드, 이벤트 핸들러입니다. 적용 가능 타입은 Component, Logic입니다.

매개 변수: string ("Server", "Client", "ServerOnly", "ClientOnly", "Multicast")

@ExecSpace("Client")
@ExecSpace("Server")
@ExecSpace("ServerOnly")
@ExecSpace("ClientOnly")
@ExecSpace("Multicast")
InspectorButton Attribute
프로퍼티 에디터에 대상 메소드를 실행하는 버튼을 추가합니다. 적용 대상은 메소드입니다.

매개 변수: string

@InspectorButton("ButtonName")
method void Function1()

end
EventSender Attribute
이벤트 핸들러의 이벤트 발송 객체를 지정합니다. 적용 대상은 이벤트 핸들러이며 반드시 EventSender Attribute를 사용해야 합니다.
파라미터는 string으로 지정된 문자열로만 사용이 가능합니다.

매개 변수: string ("Self", "Entity", "Model", "LocalPlayer", "Service", "Logic"), string(optional)

Tip
첫 번째 매개변수로 사용하는 string에 따라 두 번째 매개변수로 사용할 수 있는 값이 달라집니다.

"Entity", "Model": 두 번째 파라미터로는 Entity Id를 입력해야 합니다.

"Service", "Logic": 두 번째 파라미터로는 타입명을 입력해야 합니다.

"Self", "LocalPlayer": 두 번째 파라미터를 사용하지 않습니다.

@EventSender("Service", "InputService")
handler handleEvent(keyDownEvent event)

end
DisplayName Attribute
MSW 메이커의 프로퍼티 에디터에 표시되는 이름을 지정합니다. 적용 대상은 프로퍼티입니다.

매개 변수: string

@DisplayName("Test Value")
property string NewValue = nil
Description Attribute
MSW 메이커의 프로퍼티 에디터에 툴팁으로 표시되는 설명입니다. 적용 대상은 프로퍼티입니다.

매개 변수: string

@Description("Property Description")
property string NewValue = nil
HideFromInspector Attribute
MSW 메이커의 프로퍼티 에디터에 표시할 것인지 여부를 지정합니다. 적용 대상은 프로퍼티입니다.

매개 변수: string

@HideFromInspector
property string NewValue = nil
MinValue Attribute
MSW 메이커의 프로퍼티 에디터에 최솟값을 지정합니다. 적용 대상은 number, integer 타입의 프로퍼티입니다.

매개 변수: number

@MinValue(2)
property number NewValue = 3
MaxValue Attribute
MSW 메이커의 프로퍼티 에디터에 최댓값을 지정합니다. 적용 대상은 number, integer 타입의 프로퍼티입니다.

매개 변수: number

@MaxValue(10)
property number NewValue = 3
Delta Attribute
MSW 메이커의 모바일 프로퍼티 에디터에서 좌우 버튼을 눌렀을 때의 변화량을 지정합니다. 적용 대상은 number, integer 타입의 프로퍼티입니다.

매개 변수: number

@Delta(1)
property number NewValue =3
MaxLength Attribute
MSW 메이커의 프로퍼티 에디터에 최대 길이를 지정합니다. 적용 대상은 string 타입의 프로퍼티입니다.

매개 변수: integer

@MaxLength(5)
property string NewVlaue = "test"
Component Attribute
스크립트를 Component로 지정합니다. 적용 대상은 스크립트입니다.

매개 변수: 없음

@Component
script NewComponent extends Component
Event Attribute
스크립트를 EventType으로 지정합니다. 적용 대상은 스크립트입니다.

매개 변수: 없음

@Event
script NewEvent extends EventType

end
Item Attribute
스크립트를 ItemType으로 지정합니다. 적용 대상은 스크립트입니다.

매개 변수: 없음

@Item
script NewItem extends Item

end
BTNode Attribute
스크립트를 BTNodeType으로 지정합니다. 적용 대상은 스크립트입니다.

매개 변수: 없음

@BTNode
script NewBTNode extends BTNode

end
State Attribute
스크립트를 StateType으로 지정합니다. 적용 대상은 스크립트입니다.

매개 변수: 없음

@State
script NewState extends StateType

end
Struct Attribute
스크립트를 StructType으로 지정합니다. 적용 대상은 스크립트입니다.

매개 변수: 없음

@Struct
script NewStruct

end
Logic Attribute
스크립트를 Logic으로 지정합니다. 적용 대상은 스크립트입니다.

매개 변수: 없음

@Logic
script NewLogic extends Logic

end
Annotation
어노테이션은 코드에 추가하여 사용하는 일종의 메타데이터입니다. ---@ 형태로 어노테이션을 작성하면 실제 코드를 작성할 때 다양한 도움을 줄 수 있습니다.

Type Annotation
Type Annotation은 타입을 명시적으로 지정할 수 있습니다. 할당문과 프로퍼티 정의문에 사용할 수 있습니다.

---@type TYPE
사용 예시

---@type string
local testValue = "test"
---@type string, integer
local strValue, intValue = "str", 5
Param Annotation
Param Annotation은 대상이 되는 함수의 매개 변수 타입을 지정할 수 있습니다. 함수 정의문에 사용합니다.

---@param param_name PARAM_TYPE
사용 예시

---@param testParamA Entity
local function TestFunction(testParamA)
end
---@param testParamA Entity
---@param testParamB integer
local function TestFunction(testParamA, testParamB)

end
Return Annotation
Return Annotation은 대상 함수의 반환 타입을 지정할 수 있습니다. 함수 정의문, 메소드 정의문에 사용할 수 있습니다.
Return Annotation은 대상 함수의 반환 타입을 지정하여 스크립트 어시스트의 도움을 받을 수 있습니다.

---@return TYPE
사용 예시

---@return Entity
local function TestFunction(testParamA, testParamB)
    return self.Entity
end
---@return Entity, string
local function TestFunction(testParamA, testParamB)
    return self.Entity, "strValue"
end
Deprecated Annotation
Deprecated Annotation을 사용해 더 이상 사용하지 않음을 명시할 수 있습니다. 스크립트 정의문, 프로퍼티 정의문, 메소드 정의문, 이벤트 핸들러 정의문에 사용할 수 있습니다.

---@deprecated
사용 예시

---@deprecated
property any NewValue = nil
Sealed Annotation
Sealed Annotation은 해당 멤버가 더이상 오버라이드되지 않음을 명시합니다. 프로퍼티 정의문, 메소드 정의문, 이벤트 핸들러 정의문에 사용할 수 있습니다.

---@sealed
사용 예시

---@sealed
property any NewValue = nil
Description Annotation
Description Annotation은 툴팁에 표시할 설명을 작성할 수 있습니다. 스크립트 정의문, 프로퍼티 정의문, 메소드 정의문, 이벤트 핸들러 정의문에 사용할 수 있습니다.

---@description "Test"
사용 예시

---@description "Test Value"
property any NewValue = nil
