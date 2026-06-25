# ActionSheet로 아바타 애니메이션 손쉽게 제어하기

<!-- 출처: reference/TaskWiki.md · 문서 #77 -->


학습 과정 소개
StateToAvatarBodyActionSheet의 아바타 상태를 통해 애니메이션을 손쉽게 제어하는 방법을 소개합니다.

아바타 애니메이션
아바타가 걸을 때, 앉을 때, 공격할 때, 점프할 때를 유저가 인지하려면 상태에 맞는 애니메이션이 필요합니다. AvatarStateAnimationComponent의 StateToAvatarBodyActionSheet에 Key와 AvatarBodyActionStateName가 있으면 아바타가 특정 상태가 될 때, 이에 해당하는 애니메이션이 재생됩니다. 이 특징을 이용해 기본 애니메이션 값을 지우고, 새로운 상태와 아바타의 애니메이션을 연결할 수 있습니다. 예를 들어, 공격 키를 눌렀을 때 attack 애니메이션이 기본이지만 dead 애니메이션으로 바꿀 수 있습니다.

StateToAvatarBodyActionSheet에는 기본적으로 아바타의 11가지 상태(Key)와 그에 연결된 애니메이션(AvatarBodyActionStateName)이 정의되어 있습니다. Key는 아바타가 특정 상태가 되었을 때 동작 재생을 요청하고, AvatarBodyActionStateName에 해당하는 애니메이션을 재생합니다. 만약 상태(Key)를 입력하지 않고, AvatarBodyActionStateName만 입력한다면 연결된 상태가 없기 때문에 애니메이션이 재생되지 않습니다.
AvatarStateAnimationComponent는 Player 모델의 기본 컴포넌트입니다. DefaultPlayer에서 이 컴포넌트를 비활성화할 수 있고, 컴포넌트에 프로퍼티를 추가할 수 있습니다. StateToAvatarBodyActionSheet 프로퍼티의 Size 값을 변경하거나 하단의 [+], [-] 버튼을 누르면 Key를 추가/삭제할 수 있습니다.

animation105

StateToAvatarBodyActionSheet에는 아래의 값이 기본으로 등록되어 있습니다. 기본값을 변경하거나 삭제하면 해당하는 애니메이션은 재생되지 않습니다. 예를 들어 AvatarBodyActionStateName에서 ladder를 삭제했다면, 아바타가 사다리를 올라갈 때 사다리 올라가는 애니메이션(ladder)이 재생되지 않고, 걷기 애니메이션이 멈춘 상태로 올라가게 됩니다.
PlayRate로 아바타 애니메이션의 기본 재생 속도를 조정할 수 있습니다. AvatarBodyActionStateName별로 기본값이 다릅니다.

Key	AvatarBodyActionStateName	PlayRate
IDLE	stand	1
MOVE	walk	1.68
ATTACK	attack	1.33
HIT	hit	1
CROUCH	crouch	1
FALL	fall	1
JUMP	fall	1
CLIMB	rope	1
LADDER	ladder	1
DEAD	dead	1
SIT	sit	1
Tip.
Key는 항상 대문자로 입력해야 합니다.

기존의 상태 키에 다른 애니메이션 연결하기
StateToAvatarBodyActionSheet 프로퍼티의 AvatarBodyActionStateName 값을 수정해 기존의 상태에 다른 애니메이션을 연결할 수 있습니다.

attack을 dead로 변경합니다.
animation104


start [시작] 버튼을 누른 뒤 테스트해 봅시다. 왼쪽 Ctrl 키를 눌러 공격을 합니다. 변경 전에는 공격 애니메이션이 재생되었지만, 연결 애니메이션을 Dead로 변경했기 때문에 죽음 애니메이션이 재생됩니다.
animation103

새로운 상태 키와 애니메이션 추가하기
새로운 상태(Key)를 추가하고, 애니메이션을 지정할 수 있습니다. 기존의 키를 삭제하지 않고 새로운 상태와 액션을 추가하면 두 상태 모두 동작합니다.
숫자 6, 7, 8, 9를 눌렀을 때 특정 애니메이션이 재생되게 만들어봅시다.

Workspace - DefaultPlayer - AvatarStateAnimationComponent의 Size를 15로 변경합니다.


추가한 칸에 새로운 Key와 AvatarBodyActionStateName를 입력합니다.

Key	AvatarBodyActionStateName
NEW_ATTACK	attack
NEW_DEAD	dead
NEW_JUMP	fall
NEW_CROUCH	crouch
ActionSheet100


MyDesk에서 새로운 NewAvatarAnimation 스크립트 컴포넌트를 생성하고, DefaultPlayer에 추가합니다.


NewAvatarAnimation 스크립트를 엽니다. 새롭게 추가한 Key를 재생할 수 있도록 StateComponent의 AddState(), ChangeState() 함수를 활용해 작성합니다.

Property:
[None]
any stateComponent = nil

Method:
[clinet only]
void OnBeginPlay() 
{
    self.stateComponent = self.Entity.StateComponent
    self.stateComponent:AddState("NEW_ATTACK") -- 새로운 상태를 추가합니다.
    self.stateComponent:AddState("NEW_DEAD")
    self.stateComponent:AddState("NEW_JUMP")
    self.stateComponent:AddState("NEW_CROUCH")
}

[clinet only]
void Animate(number key) 
{
    if key == 6 then
        self.stateComponent:ChangeState("NEW_ATTACK") 
    elseif key == 7 then
        self.stateComponent:ChangeState("NEW_DEAD")
    elseif key == 8 then
        self.stateComponent:ChangeState("NEW_JUMP")
    elseif key == 9 then
        self.stateComponent:ChangeState("NEW_CROUCH")
    end
}

Event Handler:
[client only] [service: InputService] 
HandleKeyDownEvent(KeyDownEvent event) 
{
    -- Parameters
    local key = event.key
    --------------------------------------------------------

    if key == KeyboardKey.Alpha6 then
        self:Animate(6) 
    elseif key == KeyboardKey.Alpha7 then
        self:Animate(7)
    elseif key == KeyboardKey.Alpha8 then
        self:Animate(8)
    elseif key == KeyboardKey.Alpha9 then
        self:Animate(9)
    end
}
더 알아보기
새로운 상태와 액션을 추가했지만 기존의 상태를 삭제하지 않았기 때문에 두 가지 입력 모두 작동합니다.

시작을 눌러 숫자 키를 누르면 애니메이션이 재생됩니다.
