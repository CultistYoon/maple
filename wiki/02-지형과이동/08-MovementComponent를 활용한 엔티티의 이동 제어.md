# MovementComponent를 활용한 엔티티의 이동 제어

<!-- 출처: reference/TaskWiki.md · 문서 #62 -->


학습 과정 소개
이번 과정에서는 점프, 플레이어 이동 및 엔티티 좌표 설정 등 MovementComponent가 제공하는 주요 기능들과 MovementComponent의 기본 작동 방식에 대해 알아봅니다.

MovementComponent 소개
MovementComponent는 캐릭터의 이동속도와 점프력 설정은 물론 RigidbodyComponent가 포함된 엔티티를 강제로 점프시키거나 이동 또는 정지시킬 수 있는 여러 기능을 제공합니다.
스크립트 컴포넌트를 통해 TransformComponent를 제어하여 동적으로 엔티티를 이동시킬 수 있지만, 만일 엔티티에 RigidbodyComponent가 포함되어 있는 경우 RigidbodyComponent 또한 TransformComponent를 제어하기 때문에 의도한대로 이동하지 않을 수 있습니다.
MovementComponent는 엔티티에 RigidbodyComponent 포함 여부를 체크하여 TransformComponent 또는 RigidbodyComponent를 제어하여 이동시킵니다. 따라서 제작자가 직접 RigidbodyComponent의 포함 여부를 체크할 필요 없이 MovementComponent를 이용해 쉽게 엔티티의 이동을 제어할 수 있습니다.

Tip.
KinematicbodyComponent와 SideviewbodyComponent도 동일하게 제어할 수 있습니다.

플레이어의 이동 관련
플레이어 이동 속도 설정
플레이어의 이동 속도는 InputSpeed를 통해 설정합니다.
조작키(방향키)를 눌렀을 때 얼마만큼의 힘으로 엔티티를 이동시킬지를 설정하는 프로퍼티로 플레이어 엔티티에만 유효합니다. 입력된 값이 크면 클수록 플레이어 엔티티의 속도가 빨라집니다.

InputSpeed = 1.2	InputSpeed = 3	InputSpeed = 5
1	2	3
사다리에서의 정지 여부 확인
플레이어가 사다리에서 이동을 멈추었는지는 IsClimbPaused 프로퍼티를 통해 확인할 수 있습니다. 엔티티가 사다리 또는 로프 위에서 멈춰있는 상태인지를 확인할 수 있는 프로퍼티로, 플레이어 엔티티에만 유효합니다. IsClimbPaused는 boolean 타입으로 플레이어 엔티티가 사다리에서 이동 중 멈춰있을 때 true를 읽어올 수 있습니다. ReadOnly 프로퍼티이기 때문에 읽기만 가능합니다.

[server only]
void OnUpdate(number delta)
{
    local isClimbPaused = self.Entity.MovementComponent.IsClimbPaused
    log(isClimbPaused)
}
isclimbpaused

플레이어가 바라보고 있는 방향 확인
플레이어가 바라보고 있는 방향은 IsFaceLeft 함수를 통해 확인할 수 있습니다. 플레이어 엔티티 전용 함수로 플레이어 엔티티가 좌측을 바라보면 true를, 그렇지 않으면 false를 리턴합니다.

[serive: InputService]
HandleKeyUpEvnet(KeyUpEvent event)
{
	-- Parameters
	local key = event.key
	--------------------------------------------------------
	--좌우 키를 입력할 때마다 플레이어가 좌측을 향하고 있으면 콘솔 창에 true를 출력합니다.
	if key == KeyboardKey.LeftArrow or key == KeyboardKey.RightArrow then
		log(self.Entity.MovementComponent:IsFaceLeft())
	end
}
isfaceleft

엔티티 점프 관련
엔티티 점프
MovementComponent의 Jump 함수는 엔티티를 JumpForce에 입력한 힘만큼 점프시킵니다. boolean 타입으로 점프에 성공한 경우 true를 리턴합니다. 엔티티에 RigidbodyComponent가 함께 있어야 작동하며, RigidbodyComponent가 없으면 false를 리턴합니다. 동기화를 위해 일반적으로 server 공간에서 호출하는 것이 좋지만, 플레이어 엔티티의 경우에는 client에서 호출해야 합니다.

[server only]
void OnUpdate(number delta)
{
    -- 플레이어 엔티티인 경우 실행 제어 공간을 client 또는 client only로 변경합니다.
	if self._T.accTime == nil then 
		self._T.accTime = 0 
	end
	
	self._T.accTime = self._T.accTime + delta
	
	--3초마다 엔티티를 점프시킵니다.
	if self._T.accTime >= 3 then
		self.Entity.MovementComponent:Jump()
		self._T.accTime = 0
	end
}
jump

점프력 설정
JumpForce는 엔티티가 점프했을 때 얼마나 높이 뛸지를 설정할 수 있는 프로퍼티로, MovementComponent의 Jump함수가 호출되었을 때 JumpForce값이 점프력으로 반영됩니다.

JumpForce = 1	JumpForce = 3	JumpForce = 5
4	5	6
다운 점프
DownJump는 엔티티가 놓여진 풋홀드 아래에 또다른 풋홀드가 존재할 경우, 엔티티를 아래 풋홀드로 이동시키는 함수입니다.
RigidbodyComponent가 있을 때 작동하며, RigidbodyComponent가 없다면 무시됩니다. 리턴 타입은 boolean으로 엔티티가 정상적으로 이동한 경우 true를 리턴합니다. 만일 아래와 같이 작성된 컴포넌트를 MovementComponent와 RigidbodyComponent가 있는 엔티티에 추가하면, 3초마다 아래 풋홀드로 내려가는 것을 볼 수 있습니다. Jump와 마찬가지로 플레이어 엔티티를 다운 점프시킬 때에는 client에서 호출합니다.

[server only]
void OnUpdate(number delta) 
{
    -- 플레이어 엔티티인 경우 실행 제어 공간을 client 또는 client only로 변경합니다.
	if self._T.accTime == nil then 
		self._T.accTime = 0 
	end
	
	self._T.accTime = self._T.accTime + delta
	
	--3초마다 엔티티를 다운 점프시킵니다.
	if self._T.accTime >= 3 then
		self.Entity.MovementComponent:DownJump()
		self._T.accTime = 0
	end
}
downjump

더 알아보기
플레이어 엔티티의 RigidbodyComponent는 다른 엔티티의 컴포넌트처럼 server에서 client로 동기화 되는 것이 아닌, client에서 server로 동기화되기 때문에 플레이어의 RigidbodyComponent는 client 공간에서 제어하는 것이 좋습니다.

엔티티 이동
엔티티 좌표 이동
MovementComponent에서는 SetPosition 함수를 통해 엔티티의 좌표를 설정합니다.
SetPosition()함수는 기본적으로 TransformComponent의 Position을 설정하지만, RigidbodyComponent가 엔티티에 포함되어 있을 경우 RigidbodyComponent를 통해 Position을 설정합니다. 매개 변수로 Vector2 값을 받으며, 이 값에 해당하는 좌표로 엔티티가 이동합니다.

[server only]	
void OnUpdate(number delta)
{
    local deltaX = 1
    local pos = self.Entity.TransformComponent.Position
    pos.x = pos.x + deltaX * delta
    local deltaPos = Vector2(pos.x, pos.y)
    self.Entity.MovementComponent:SetPosition(deltaPos)
}
