# 행동 트리를 활용한 AI 만들기

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「행동 트리를 활용한 AI 만들기」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 05 게임로직시스템 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
행동 트리와 BTNodeType 개념을 이해하고, AIComponent를 활용해 Action Node를 생성하는 방법을 알아봅시다. 행동 트리 노드 만들기에서 행동 트리 구현 방법과 예제를 소개합니다.

참고 가이드
행동 트리 노드 만들기

참고 API Reference
BTNode

AIComponent

ParallelNode

RandomSelectorNode

SelectorNode

SequenceNode

개념 이해하기
유한 상태 기계
유한 상태 기계 (Finite State Machine, FSM)은 특정 조건과 상황에 따라 유한개의 상태 중 하나의 상태로 전환되거나 해당 상태에 따른 액션을 수행하는 모델입니다. FSM은 상대적으로 쉽게 구성할 수 있고 직관적으로 설계할 수 있습니다. 주로 AI 설계를 위해 사용합니다. FSM은 상태(State)와 전이(Transition)로 구성되어 있습니다. 상태에 대한 액션 수행 중 특정 조건 만족 시 다음 상태로 전이됩니다. 예를 들어 몬스터가 대기 상태일 때, 플레이어가 몬스터에 접근하면 몬스터가 공격 상태로 변경되어 플레이어를 공격하게 됩니다.
[object Object]

그러나 상태와 액션이 다양해지고 복잡해질수록 각 상태의 연결과 유지 보수 부담이 커집니다. 또한 규모가 커질수록 상태의 흐름을 파악하기 어려울 뿐 아니라 상태의 흐름을 재사용할 수 없습니다.

[object Object]

계층적 유한 상태 기계
계층적 유한 상태 기계(Hierarchical Finite State Machines, HFSM)는 FMS 단점을 보완하기 위해 여러 개의 상태와 전이를 모듈화한 개념입니다. HFSM은 상태 변화의 흐름을 모듈화해 재사용할 수 있고 현재 상태가 어디서부터 진행되었는지 쉽게 파악할 수 있습니다.
그러나 개별 상태의 재사용이 어려운 단점이 있습니다. 각 하위 상태는 특정 상태에서부터 전이되어야 한다는 조건으로 인하여 다른 그룹에서 개별 상태로 접근을 할 수 없습니다. 예를 들어 'HIT' 상태일 때, 'HIT'은 'IDLE' 상태의 하위일 수도 있고 'BATTLE' 상태의 하위일 수도 있습니다. 그러므로 'IDLE' 상태와 'BATTLE' 상태 하위의 'HIT' 상태를 각각 추가해야 합니다.

[object Object]

행동 트리
행동 트리(Behaviour Tree, BT)는 노드라 불리는 개별 단위의 집합입니다. 상태와 전이로 구성된 유한 기계 상태와 달리 행동 트리의 각 노드는 개별 로직으로 모듈화되어 있습니다. 상황과 목적에 따라 재사용이 가능합니다. 또한 각 노드가 결합 순서에 따라 순차적으로 실행되기 때문에 특정 행동의 연결과 해제가 용이합니다.
[object Object]

행동 트리 작동 원리
행동 트리는 프레임마다 Root 노드에서 시작합니다. 그 후 순차적으로 실행됩니다. 실행 순서는 위에서 아래, 왼쪽에서 오른쪽입니다. 부모 노드가 자식 노드를 실행하며 실행 순서는 각 부모에 등록된 순서대로 실행됩니다.
부모 노드는 종류에 따라 자식 노드 실행 조건을 달리하며, 조건에 부합할 때 부모가 가진 자식 노드를 모두 순차적으로 실행합니다. 예를 들어 부모 노드에 자식 노드 A, B, C가 순차적으로 등록된 경우 A가 가장 좌측에, 노드 C가 가장 우측에 배치됩니다. 부모 노드 실행 시 자식 노드는 A, B, C 순으로 실행됩니다. 이때 자식 노드 A가 자식 노드 D, F를 갖고 있다면 A의 자식 노드 D, F를 모두 실행한 후 노드 B가 실행됩니다.

모든 노드는 실행 시 상태 값인 BehaviourTreeStatus를 반환합니다. 반환하는 값은 총 세 가지로 Running, Success, Failure입니다. 각 부모 노드는 자식 노드가 반환하는 값에 따라 다음 자식 노드를 실행할지 결정합니다.
[object Object]

행동 트리 노드 알아보기
행동 트리는 행동을 정의하는 Action Node와 행동의 흐름을 제어하는 Composite Node로 구성됩니다. Action Node는 BTNodeType을 활용해 크리에이터가 직접 만들어 사용해야 하며, Composite Node는 메이플스토리 월드에서 제공하고 있습니다.

Action Node
Action Node는 엔티티의 행동을 정의합니다. Leaf Node로도 불리며, 자식 노드를 갖지 않는 특징이 있습니다. Action Node는 엔티티의 실질적인 행동 또는 행동의 조건 등을 정의합니다. 각 행동과 조건은 별도의 Action 노드로 정의하며, 각 노드는 Composite의 자식 노드로 등록합니다. 예를 들어 몬스터가 '대기' 상태에 있을 때, '공격' 상태에 있을 때의 행동을 정의할 수 있습니다.

Composite Node
Composite Node는 흐름을 제어하는 노드로 여러 개의 자식 노드를 가질 수 있습니다. 자식 노드가 Success 또는 Failure를 반환하면 일정한 규칙에 따라 다음 자식 노드의 실행 여부를 결정합니다.
Composite Node는 4가지 종류가 있으며, 노드마다 자식 노드 실행 방법, 상태 값을 부모로 반환하는 규칙이 다릅니다.

Sequence Node, Selector Node, Random Selector Node, Parallel Node

Sequence Node
Sequence Node는 자식 노드를 순서대로 실행하다가 자식 노드가 Failure를 반환하면 실행을 멈추고 부모 노드에 Failure를 반환합니다. 모든 자식 노드가 Success를 반환하면 부모 노드에 Success를 반환합니다.
[object Object]

Selector Node
Selector Node는 자식 노드를 순서대로 실행하다가 자식 노드가 Success를 반환하면 실행을 멈추고 부모 노드로 Success를 반환합니다. 모든 자식 노드가 Failure를 반환하면 부모 노드에 Failure를 반환합니다.
[object Object]

RandomSelector Node
RandomSelector Node는 자식 노드 중 하나를 무작위로 선택해 실행합니다. 자식 노드가 Success를 반환하면 Success를, Failure를 반환하면 Failure를 부모 노드에 반환합니다.
RandomSelector Node는 난수를 뽑아 해당 난수가 속한 범위의 확률을 가진 노드를 선택합니다. 예를 들어 아래 그림과 같이 RandomSelector Node에 자식 노드의 선택될 확률이 0.2(20%), 0.3(30%), 0.5(50%)일 때, 난수가 0.4로 결정되면 Action2 노드가 실행되고 0.9로 결정되면 Action3 노드가 실행됩니다.
[object Object]

Parallel Node
Parallel Node는 모든 자식 노드를 실행해 모든 자식 노드가 Success를 반환한 경우 Success를 부모 노드에 반환합니다. 반면 자식 노드 중 하나라도 Failure를 반환한 경우 Failure를 부모 노드에 반환합니다.
[object Object]

Decorator Node
Decorator Node는 하나의 자식을 가지며, 자식을 실행할지 말지 결정하거나 반환 값을 가공할 수 있습니다. Composite Node, Action Node를 자식으로 가질 수 있습니다. 메이플스토리 월드는 크리에이터가 Decorator Node를 제작할 수 있도록 제공하고 있습니다.
Decorator Node는 부모 노드와 자식 노드 A의 중간에서 위치하며, 조건에 따라 노드 A를 실행할지 여부를 결정합니다. 또한 A 노드가 반환한 값 대신 다른 값을 부모에게 전달할 수 있습니다.
[object Object]

여러 프레임 동안 동작하는 노드
자식 노드가 Success 또는 Failure를 반환하면 부모 노드는 다음 자식 노드를 실행합니다. 그러나 자식 노드가 Running을 반환하면 부모 노드는 Running을 반환했던 자식 노드를 다음 프레임에 다시 실행합니다. 이 특성을 활용해 여러 프레임 동안 동작하는 노드를 만들 수 있습니다.
아래 그림과 같이 자식 노드 A, B, C가 있을 때 Sequence Node와 Selector Node의 경우 B 노드가 Running을 반환하는 동안 C 노드를 실행하지 않습니다. RandomSelector Node는 선택된 노드를 계속 실행합니다. Parallel Node는 자식 노드를 동시에 실행하는 특징으로 인해 노드 A, B, C 모두 실행하고, 다음 프레임에서는 노드 중 Running을 반환했던 노드 A, B만 실행되고 노드 C는 실행되지 않습니다.

[object Object]
[object Object]

노드의 특성을 활용해 일정 시간 동안 대기하는 Wait 노드를 아래와 같이 만들 수 있습니다.

Property:
[None]
number Time = 2
[None]
number ElapsedTime = 0
 
Method:
void OnInit()
{
    -- Running을 반환하는 동안 OnInit()이 호출되지 않습니다.     

    self.ElapsedTime = 0
}
 
any OnBehave(number delta)
{
    -- Time만큼 시간이 흐를 때까지 Running을 계속 반환해 다음 자식 노드가 실행되지 않게 합니다.
    -- Running을 반환하는 동안 OnBehave()가 계속 호출됩니다.

    self.ElapsedTime += delta
    if self.ElapsedTime < self.Time then
        return BehaviourTreeStatus.Running
    end

    return BehaviourTreeStatus.Success
}
Action Node의 생성과 기능 정의
메이플스토리 월드에서는 BTNodeType을 활용해 Action Node를 만들 수 있습니다. BTNodeType에 노드의 행동을 정의하고 AIComponent로 노드 객체를 생성하여 사용할 수 있습니다.

BTNodeType에 정의하기
BTNodeType은 기본 이벤트 함수로 OnInit()과 OnBehave()를 제공합니다. 기본 이벤트 함수에 노드의 행동을 정의합니다.

OnInit()
OnInit()는 OnBehave()호출 전에 실행되는 함수입니다. 노드가 실행될 때마다 호출되지만, Running을 반환한 경우 다음 프레임에서는 OnInit()가 호출되지 않습니다.

OnBehave()
OnBehave()는 해당 Action 노드가 실행될 때마다 1회씩 호출되는 메소드로 BehaviourTreeStatus 값을 반드시 반환해야 합니다. AI의 행동이나 행동의 조건을 정의할 때 사용하는 메소드이므로 Action 노드 타입에 반드시 추가해야 합니다.
매개 변수 프레임 당 시간인 delta를 활용해 이동이나 시간 측정과 같은 기능을 구현할 때 활용할 수 있습니다.

Property : 
[Sync]
number Num = 0

Method: 
void OnBehave(number delta)
{
	self.Num = self.Num + delta
	
	if self.Num >= 3 then
		self.Num
		return BehaviourTreeStatus.Success
	else	
		return BehaviourTreeStatus.Running
	end
}
Action Node 생성하기
AI로 사용할 엔티티에는 AIComponent 또는 확장한 AIComponent가 포함되어 있어야 합니다. AIComponent는 BTNodeType에서 정의된 내용으로 Action Node를 별도의 객체로 생성하거나, 만들어진 행동 트리의 최상위 노드를 Root 노드로 설정하여 엔티티에 AI를 부여하기 때문입니다.
Action Node를 만들 때는 AIComponent의 CreateNode(), CreateLeafNode()를 활용해 Action Node를 생성할 수 있습니다.

CreateNode()
BTNodeType으로 노드 객체를 생성할 때는 AIComponent의 CreateNode() 함수를 활용합니다. 매개 변수로 생성될 BTNodeType과 이름을 전달합니다.

local node = self.Entity.AIComponent:CreateNode("NewBTNode", "actionNode")
CreateLeafNode()
간단한 Action Node를 만들고 싶을 때는 아래와 같이 직접 함수를 전달하는 방법으로 노드의 행동을 정의할 수 있습니다. CreateLeafNode()는 CreateNode()와 달리 BTNodeType이 필요하지 않습니다. 매개 변수로 객체로 생성될 노드의 이름, 노드 실행 시 호출될 함수를 전달합니다.

local func = function() 
    log("ActionNode!") 
    return BehaviourTreeStatus.Success
end

local printLogNode = self.Entity.AIComponent:CreateLeafNode("NodeInstanceName", func)
