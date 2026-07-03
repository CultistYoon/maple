# Entity, Component, Property

<!-- 출처: reference/TaskWiki.md · 문서 #30 -->


학습 과정 소개
Entity와 Component 그리고 Property에 대해서 개념을 이해합니다.

Entity
엔티티는 메이플스토리 월드 내에서 존재하는 객체입니다.
아래의 그림에서 Entity는 어떤 것들일까요?
Entity_Component_Propoerty_1

빨간색을 칠한 부분이 Entity입니다.
그뿐만 아니라 보이지는 않지만 돌아가고 있는 모든 것들이 Entity입니다.
Entity_Component_Propoerty_2

메이플스토리 월드에서는 실제로 수많은 Entity가 배치되어 있고 실시간으로 생성, 변경, 삭제됩니다.
Entity들이 실제 게임상에서 활동함으로써 시각적으로 보이며, 내부적으로 로직이 돌아가게 됩니다.

그럼 Entity는 뭐로 구성이 되어 있을까요?

Component
Entity는 Component들로 구성되어 있으며 Component들의 집합체로 볼 수 있습니다.
Component는 각각의 요소를 담당하고 있으며 각각의 기능을 담당합니다.

피자를 예로 들어볼까요?
pizza

내 앞에 완성된 피자가 있다고 생각해봅시다.
이 피자는 향기도 나며 먹을 수 있습니다. 이 피자는 Entity에 해당합니다.

위 피자를 구성하고 있는 것은 토마토, 도우, 소스 등이 있습니다.
그리고 보이지는 않지만 조리 방법 같은 것도 있습니다.
이것들이 모두 Component입니다.


토마토 Component

도우 Component

소스 Component

조리법 Component

Component는 각각의 기능을 담당하며 때로는 다른 Component와 결합하여 다른 효과가 날 수도 있습니다.
이렇게 각각을 Component로 분리하는 이유는 재사용성이 높기 때문입니다.
예를 들어서 다른 피자를 만들고 싶다고 할 때


치즈 피자 = 도우 + 소스 + 치즈 + 오븐 조리

파인애플 피자 = 도우 + 소스 + 치즈 + 파인애플 + 오븐 조리

냉동 불고기 피자 = 도우 + 소스 + 치즈 + 불고기 + 전자레인지 조리

이렇게 이미 만들어진 Component를 가지고 잘 조합을 한다면 다른 형태가 나오기 때문이죠

메이플스토리 월드에서는 프로퍼티 에디터에서 Component를 관리합니다.
4

앞서 말한 대로 Entity는 Component들로 구성이 되어 있고, Entity Editor를 열면 위 그림과 같이 Component들로 구성이 되었습니다.
따라서 기능이 잘 분리된 Component들을 잘 조합 한다면 내가 원하는 형태로 원하는 동작을 할 수 있는 Entity를 제작할 수 있습니다.

그렇다면 정해진 Component만을 조합하면 내가 원하는 Entity를 생성할 수 있는 걸까요?

Property
Property는 각 Component의 세부사항을 설정합니다.
Component에서 예시를 든 피자로 다시 돌아와 볼까요?

세 명의 아이가 페퍼로니 피자를 먹고 싶어 합니다.
철수는 페퍼로니가 2배들어 있는 피자를 원하고, 영희는 들어 있는 치즈가 체다가 아닌 모짜렐라 치즈를 원합니다.
윤후는 사이즈를 조금 더 크게 먹고 싶습니다.

기존에 도우 Component, 페퍼로니 Component, 치즈 Component 가 있습니다.
자, 어떻게 하면 될까요?

철수는 페퍼로니 2배 Component를 추가하고
영희는 모짜렐라 치즈 Component를 추가하고
윤후는 도우 2배 Component, 페퍼로니 2배 Component, 치즈 2배 Component를 추가합니다.

이렇게 하면 원하는 형태의 피자(Entity)를 만들 수 있습니다.
하지만 Component의 재사용성이 떨어지는군요. 앞서서는 Component가 재사용성이 높다고 하였는데 결국 다 따로 만들어 줘야 하는군요.

그럼 어떻게 하면 될까요?

바로 Property를 이용하는 겁니다.
Property는 Component에서 주요 설정이 필요한 항목들을 의미합니다.
그렇기에 같은 Entity가 같은 Component를 사용하더라도 Property 값이 다르면 다르게 동작하게 할 수 있는 거죠.

예를 들어서 도우 Component에는 "Size"라는 Property가 있습니다.
치즈 Component에는 "Size"와 "치즈 Type" 이라는 Property가 있고
페퍼로니 Component에는 "Size"라는 Property가 있다고 한다면,
세 친구 모두 같은 Component를 사용한 피자(Entity)를 만들 수 있습니다.
물론 각각의 Property는 다르지만요.

다시 메이플스토리 월드로 돌아와서 이처럼 각각의 Component는 Property들로 세부 속성을 정할 수 있습니다.
말풍선을 뿌릴 수 있는 ChatBalloonComponent에 대해서 살펴볼까요?

BalloonScale	FontSize
Entity_Component_Propoerty_5
말풍선의 크기를 설정합니다.
값이 커질수록 말풍선의 크기도 커집니다.	Entity_Component_Propoerty_6
말풍선 텍스트의 크기를 설정합니다.
값이 커질수록 텍스트 크기도 커집니다.
이 ChatBalloonComponent는 Scale과 FontSize라는 Property를 가지고 있습니다. 각각의 속성에 따라 Entity별로 다르게 설정할 수 있으며, 각각 다르게 동작합니다.
