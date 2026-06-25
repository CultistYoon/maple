# Effective MSW 2

<!-- 출처: reference/TaskWiki.md · 문서 #195 -->


학습 과정 소개
함수의 실행 공간을 설정하면 별도의 과정 없이 쉽게 클라이언트와 서버가 통신할 수 있습니다. 자동으로 처리하기 때문에 편리하지만, 몇몇 경우는 제약이 있어 크리에이터가 원하는 대로 동작하지 않을 수 있습니다. 일부는 로그가 나오지만, 어떤 것은 동작하지 않는 이유를 확인할 수 없을 수도 있습니다.
이번 가이드에서는 실행 제어를 사용할 수 없는 경우를 알아봅시다.

매개 변수가 지원하지 않는 종류
함수에는 여러 종류의 매개 변수(parameter)가 있습니다. 이 매개 변수는 다른 공간에서 실행 제어를 사용할 때 함께 전송됩니다. 이때 매개 변수는 "전송 가능"한 형태로 변경한 후 전송해야 합니다.

number나 string 등 어떠한 형태를 가진 매개 변수는 전송 가능한, 약속된 형태로 변경해 전송하고 있습니다. 그러나 약속된 형태가 없거나, 약속하기 어려운 형태라면 전송할 수 없습니다. 대표적인 형태는 "any"입니다. any는 아무 타입이나 호환 가능하다는 장점이 있지만, 이 때문에 전송 가능한 형태로 변경할 수 없습니다. 그러므로 다른 공간의 실행 제어 함수를 사용하면 그 시점에 에러가 발생합니다.

Failed to convert argument와 같은 오류가 발생했다면 해당 매개 변수 타입에서 받을 수 없는 인수(argument)를 받은 것입니다. 그럴 때는 매개 변수 타입을 다른 것으로 변경하면 됩니다.

Server의 OnBeginPlay()에서 실행 제어 함수 사용
기본적으로 메이플스토리 월드에서는 서버가 먼저 뜨고 그 뒤에 월드를 생성합니다. 각각의 클라이언트는 서버에 접속하는 시점에 서버로부터 정보를 받아 클라이언트를 구성합니다.

크리에이터가 자주 하는 실수 중 하나는 "서버를 시작할 때 클라이언트로 정보를 전송"하는 것입니다. 보통 이런 경우에 OnBeginPlay()에 실행 제어 함수를 넣는 경우가 많은데 여기서 문제가 발생합니다.
서버가 생성된 시점에 OnBeginPlay()가 호출되는데 그 시점에 클라이언트는 접속되지 않아 OnBeginPlay()에서 클라이언트로 전달하는 정보를 받을 수 없습니다. 그래서 이렇게 코드를 작성하면 제대로 동작하지 않습니다.

만약 클라이언트가 접속할 때 서버로부터 어떤 정보를 받아야 한다면, 클라이언트의 OnBeginPlay()에서 서버에 자신의 BeginPlay 타이밍을 알리고 처리를 기다리게 하는 방법이 있습니다.

Method:
[Client Only]
void OnBeginPlay()
{
    self:NotifyClientOnBegin()
}

[server] 
void NotifyClientOnBegin()
{
    -- Send Data To Client
}
Localized Entity에서 Server로 실행 제어 함수 사용
기본적으로 실행 제어 함수는 동작하는 위치(Server 또는 Client)가 있습니다. 서로 맞는 쌍이 존재해 A Entity에서 다른 공간의 A Entity로 전송을 하게 됩니다. 가령 서버에서 A Entity에 있는 B Component에서 Client 실행 제어 함수를 사용하면 이에 매칭되는 A Entity의 B Component로 전송됩니다.

만약 이 쌍이 존재하지 않으면 당연하게도 함수가 전송되지 않습니다. 쌍이 존재하지 않는 Entity도 있기 때문입니다.

개념적으로 Localized Entity라 불리는 엔티티는 각자의 클라이언트에 별도로 생성되기에 서버에는 존재하지 않습니다. 대표적으로 UI Entity가 있습니다. UI Entity는 내 클라이언트에만 존재하는 엔티티이므로 서버에는 존재하지 않습니다.

따라서 UI Entity에서는 서버의 실행 제어 함수를 사용할 수 없습니다. UI Entity는 서버에 없기 때문입니다. UI Entity가 서버에 없다는 별도의 메시지가 나오지 않기 때문에 사용할 때 주의해야 합니다.
그러므로 UI Entity에서 서버로 정보를 주고받으려면 World Entity를 통해서 전송해야 합니다.

Local 처리에 대한 이해
메이플스토리 월드에서는 기본적으로 멀티 플레이를 손쉽게 구현할 수 있습니다. 대부분의 기능을 멀티 플레이 기반으로 처리하는 것을 권장합니다.

하지만 일부 항목은 별도의 Local 개념이 필요합니다. 주요 항목은 다음과 같습니다.

Localized Entity

입력 처리

내 캐릭터 처리

UIEntity와 입력 그리고 내 캐릭터 모두 나의 클라이언트에만 존재하는 개념이라 별도로 처리해야 합니다. 특히 내 캐릭터는 클라이언트에서 처리하기 위해 _UserService.LocalPlayer를 지원하고 있습니다.

다음의 예시를 통해 Local 처리 방법을 살펴봅시다.
SkillComponent를 만들고 Player에게 넣습니다. 그리고 내가 키보드의 'S' 키를 입력하면 궁극기 스킬을 사용하는 로직을 작성했다고 가정해 봅시다.

Event Handler:
[service : InputService]
HandleKeyDownEvent (KeyDownEvent event)
{
    -- Parameters
    local key = event.key
    --------------------------------------------------------
    if key == KeyboardKey.S then
        self:UseUltimateSkill()
    end
}
위와 같이 코드를 작성하면 멀티 플레이를 할 때 문제가 발생합니다. Player는 내 클라이언트뿐만 아니라 다른 사람 클라이언트에도 모두 존재합니다. 따라서 다른 사람이 S 키를 눌러도 모든 클라이언트의 플레이어 캐릭터가 궁극기 스킬을 사용할 것입니다.
코드에서는 S 키를 입력한 사람만 처리해야 합니다. 그러므로 Entity가 '나'의 Entity가 맞는지 확인한 후, 맞으면 궁극기 스킬을 사용하고, 아니면 궁극기 스킬을 사용하지 않도록 처리해 봅시다.

위의 로직을 아래와 같이 수정합니다.

Event Handler:
[service : InputService]
HandleKeyDownEvent (KeyDownEvent event)
{
    -- Parameters
    local key = event.key
    --------------------------------------------------------
     
    if self.Entity ~= _UserService.LocalPlayer then -- Check LocalPlayer(My)
        return
    end
     
    if key == KeyboardKey.S then
        self:UseUltimateSkill()
    end
}
다른 예를 살펴보겠습니다.
크리에이터는 RPG를 만들고 있습니다. 돈을 관리하는 스크립트 컴포넌트를 만들고 그 안에 money 프로퍼티를 추가했습니다. money가 변경될 때마다 UI도 갱신하려고 합니다.

다음과 같은 로직을 작성합니다.

Method:
void SetMoney(number money)
{
    self.money = money
    local moneyUI = _EntityService:GetEntity("1f6dcd10-6306-4a47-bd41-f0a897685b73")
    moneyUI.TextComponent.Text = tostring(money)
}
그런데 이렇게 코드를 작성하면 나뿐만 아니라, 다른 사람이 돈을 획득할 때도 내 UI가 변경되는 문제가 생깁니다. 그러므로 돈을 획득한 사람의 UI만 갱신되도록 처리해야 합니다.

이처럼 Local 개념과 관련된 문제는 혼자 테스트할 때는 이상이 없다가 멀티 테스트를 할 때 주로 발생합니다. 미리 Local 개념을 이해한다면 좀 더 좋은 코드를 작성할 수 있을 것입니다.
