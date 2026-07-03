# SideViewRectTileMap에서 캐릭터 이동 제어

<!-- 출처: reference/TaskWiki.md · 문서 #64 -->


학습 과정 소개
DefaultPlayer에는 RigidbodyComponent, KinematicbodyComponent, SideviewbodyComponent가 모두 포함되어 있기 때문에 맵이 제작된 모드에 따라 자동으로 이동 제어의 주체가 달라집니다. 그중 SideViewRectTile 모드로 제작된 맵에서는 SideviewbodyComponent로 캐릭터의 이동을 제어합니다.
이번 시간에는 SideviewbodyComponent에 대해 알아보고 간단한 예제를 통해 활용법을 살펴봅시다.

참고 API Reference
SideviewbodyComponent

더 알아보기
SideViewRectTile에 대한 내용은 SideViewRectTile 모드로 맵 만들기를 참고하세요.

SideviewbodyComponent 소개
SideviewbodyComponent는 SideviewRectTile 맵에서 횡스크롤 방식의 캐릭터 이동을 제어할 때 사용합니다.
workspace Workspace - defaultplayer DefaultPlayer - property Property에서 move SideviewbodyComponent를 살펴봅시다.

sideviewbody

프로퍼티	설명
ApplyClimbableRotation	true인 경우 회전하거나 기울어진 사다리를 탄 캐릭터는 사다리의 모습을 따릅니다. false인 경우 캐릭터는 사다리의 기울기, 회전에 영향을 받지 않습니다.
EnableDownJump	아래 점프 기능을 키거나 끕니다.
DownJumpSpeed	아래 점프 시 위로 튀어 오르는 속력을 조절합니다. 값이 클수록 더 높게 점프합니다.
JumpDrag	점프 속력 감소량을 조절합니다. 값이 클수록 지면에 더 빨리 떨어집니다.
JumpSpeed	점프 시 튀어 오르는 속력을 조절합니다. 값이 클수록 더 높게 점프합니다.
Enable	True면 SideviewbodyComponent를 활성화합니다.
SideviewbodyComponent 활용
SideviewbodyComponent의 활용법을 알아봅시다.
먼저 SideViewRectTile 모드로 맵 만들기를 참고하여 아래의 맵을 만든 뒤, 이어서 본 가이드의 예제를 진행하는 것이 좋습니다.
play

2단 점프 구현하기
캐릭터의 이동은 MoveVelocity를 통해 제어합니다. MoveVelocity를 통해 간단한 2단 점프 기능을 만들어봅시다.


mydesk MyDesk 아래에 새 스크립트 컴포넌트 scriptcomponent DoubleJump를 만든 뒤, DefaultPlayer DefaultPlayer에 추가합니다.

아래와 같이 scriptcomponent DoubleJump에 IsDoubleJumping 프로퍼티와 TryDoubleJump 함수를 추가합니다.

Property:
[None]
boolean IsDoubleJumping = false

Method:
[client only]
void TryDoubleJump()
{
    local sb = self.Entity.SideviewbodyComponent

    -- 캐릭터가 아직 2단 점프를 수행하지 않았고, 공중에 있는 상태라면 속도의 Y축 값을 변경합니다.
    if self.IsDoubleJumping == false and sb:IsOnGround() == false then
        local jumpSpeed = sb.JumpSpeed
        local vel = sb.MoveVelocity

        vel.y = jumpSpeed
        sb.MoveVelocity = vel

        -- 캐릭터가 2단 점프를 하면 IsDoubleJumping를 true로 변경합니다.
        self.IsDoubleJumping = true
    end
}
캐릭터가 아직 2단 점프를 수행하지 않았고, 공중에 있는 상태라면 속도의 Y축 값을 변경해줍니다.
IsDoubleJumping 프로퍼티는 2단 점프를 수행하면 true가 되고 착지할 때 다시 false가 되는 상태 변수입니다.

아래와 같이 OnUpdate 함수도 추가합니다.

Method:
[client only]
void OnUpdate(number delta)
{
    local sb = self.Entity.SideviewbodyComponent

    -- 캐릭터가 착지하면 IsDoubleJumping를 false로 변경합니다.
    if sb:IsOnGround() then
        self.IsDoubleJumping = false
    end
}
아래와 같이 event KeyDownEvent도 추가합니다.

Event Handler:
[service: InputService]
HandleKeyDownEvent(KeyDownEvent event)
{  
    -- Parameters
    local key = event.key
    --------------------------------------------------------

    if key == KeyboardKey.LeftAlt or key == KeyboardKey.Space then
        self:TryDoubleJump()
    end
}
start 시작을 누른 뒤 테스트해봅시다. LeftAlt나 Space 키를 입력하면 2단 점프를 할 수 있습니다.
doublejump

미끄러운 타일 만들기
MoveVelocity를 응용하면 크리에이터가 의도하는 게임의 콘셉트에 맞게 캐릭터의 움직임을 만들어낼 수 있습니다. 이번 예제에서는 눈과 얼음이 가득한 필드라는 콘셉트에 맞게 가속도와 마찰력 개념을 추가해 미끄러운 길을 걷는 듯한 움직임을 만들어보겠습니다.


mydesk MyDesk 아래에 새 스크립트 컴포넌트 scriptcomponent CustomPlayerController를 만든 뒤, DefaultPlayer DefaultPlayer에 추가합니다.

scriptcomponent CustomPlayerController를 연 뒤, 아래와 같이 프로퍼티를 추가합니다.

Property:
[None]
Vector2 InputDirection = Vector2(0,0)
[None]
boolean IsJumpKeyPressed = false
[None]
boolean IsCrouchKeyPressed = false
OnBeginPlay 함수를 추가하고 유저 입력을 직접 처리하기 위해 PlayerControllerComponent는 비활성화합니다.

[client only]
void OnBeginPlay()
{
    -- 유저 입력을 직접 처리하기 위해 PlayerControllerComponent는 비활성화합니다.
    local controller = self.Entity.PlayerControllerComponent
    controller.Enable = false
}
event KeyDownEvent와 event KeyUpEvent를 추가하여 키 입력 상태를 기록합니다.

Event Handler:
[service: InputService]
HandleKeyDownEvent(KeyDownEvent event)
{
    -- Parameters
    local key = event.key
    --------------------------------------------------------

    if key == KeyboardKey.RightArrow then
        self.InputDirection.x = self.InputDirection.x + 1
    end
    if key == KeyboardKey.LeftArrow then
        self.InputDirection.x = self.InputDirection.x - 1
    end
    if key == KeyboardKey.UpArrow then
        self.InputDirection.y = self.InputDirection.y + 1
    end
    if key == KeyboardKey.DownArrow then
        self.InputDirection.y = self.InputDirection.y - 1
        self.IsCrouchKeyPressed = true
    end
    if key == KeyboardKey.LeftAlt or key == KeyboardKey.Space then
        self.IsJumpKeyPressed = true
    end
}

[service: InputService]
HandleKeyUpEvent(KeyUpEvent event)
{
    -- Parameters
    local key = event.key
    --------------------------------------------------------

    if key == KeyboardKey.RightArrow then
        self.InputDirection.x = self.InputDirection.x - 1
    end
    if key == KeyboardKey.LeftArrow then
        self.InputDirection.x = self.InputDirection.x + 1
    end
    if key == KeyboardKey.UpArrow then
        self.InputDirection.y = self.InputDirection.y - 1
    end
    if key == KeyboardKey.DownArrow then
        self.InputDirection.y = self.InputDirection.y + 1
        self.IsCrouchKeyPressed = false
    end
    if key == KeyboardKey.LeftAlt or key == KeyboardKey.Space then
        self.IsJumpKeyPressed = false
    end
}
가속도와 마찰력 기반으로 캐릭터의 이동을 계산해보겠습니다. 먼저 아래와 같이 프로퍼티를 추가해줍니다.

Property:
[None]
number MaxSpeed = 4 -- 최대 속도
[None]
number Accel = 10 -- 가속도
[None]
number Drag = 8 -- 마찰력 
[None]
number AirAccel = 6 -- 공중 가속도
[None]
number AirDrag = 4 -- 공중 마찰력
좀 더 나은 조작감을 위해 공중에서는 가속도와 마찰력의 값을 다르게 적용해봅시다.
아래와 같이 GetAccel, GetDrag 함수를 추가합니다.

-- 지면에 있을 때와 공중에 있을 때 적절한 가속도 값을 반환해 줍니다.
Method:
number GetAccel()
{
    local body = self.Entity.SideviewbodyComponent

    if body:IsOnGround() then
        return self.Accel
    else
        return self.AirAccel
    end
}

-- 지면에 있을 때와 공중에 있을 때 적절한 마찰력 값을 반환해 줍니다.
number GetDrag()
{
    local body = self.Entity.SideviewbodyComponent

    if body:IsOnGround() then
        return self.Drag
    else
        return self.AirDrag
    end
}
유저의 키 입력이 없을 때는 감속하고 키 입력이 있을 때는 가속하도록 설정해봅시다.
아래와 같이 UpdateVelocity 함수와 SignOf 함수를 추가합니다.

number SignOf(number value)
{
    if value >= 0 then
        return 1
    else
        return -1
    end
}

void UpdateVelocity(number delta)
{
    local body = self.Entity.SideviewbodyComponent
    local vel = body.MoveVelocity

    if self.InputDirection.x == 0 then
        -- 입력이 없을 땐 감속합니다.
        if vel.x ~= 0 then
            local sign = self:SignOf(vel.x)
            local drag = self:GetDrag()
            vel.x = vel.x - drag * sign * delta

            if self:SignOf(vel.x) ~= sign then
                vel.x = 0
            end
        end
    else
        -- 입력이 있을 땐 가속합니다.
        local sign = self:SignOf(vel.x)
        local accel = self:GetAccel()
        vel.x = vel.x + self.InputDirection.x * accel * delta
        vel.x = math.min(vel.x * sign, self.MaxSpeed) * sign
    end

    -- 최종 계산 결과를 적용합니다.
    body.MoveVelocity = vel
}
OnUpdate 함수에서 UpdateVelocity 함수를 호출하도록 합니다.

[client only]
void OnUpdate(number delta)
{  
    -- 속도 제어
    self:UpdateVelocity(delta)
}
start 시작을 누른 뒤 테스트해봅시다. 좌우 이동이 미끄러지듯 부드럽게 되는 것을 확인할 수 있습니다.
slide
하지만 PlayerControllerComponent를 비활성화했기 때문에 아직은 캐릭터의 점프 동작이나 이동 애니메이션이 작동하지 않는 상태입니다. 정상 작동을 위해서 동작과 애니메이션 제어 함수를 추가해봅시다.

다시 scriptcomponent CustomPlayerController를 연 뒤, 캐릭터의 동작을 제어하는 UpdateAction 함수를 추가합니다.

void UpdateAction()
{
    local controller = self.Entity.PlayerControllerComponent
    local body = self.Entity.SideviewbodyComponent

    -- 엎드리기
    if self.IsCrouchKeyPressed and body:IsOnGround() then
        controller:ActionCrouch()
    end

    -- 점프 및 다운 점프
    if self.IsJumpKeyPressed and body:IsOnGround() then
        if self.IsCrouchKeyPressed then
            controller:ActionDownJump()
        else
            controller:ActionJump()
        end
    end
}
캐릭터의 애니메이션을 제어하는 UpdateAnimationState 함수도 추가합니다.

void UpdateAnimationState()
{
    local body = self.Entity.SideviewbodyComponent
    local state = self.Entity.StateComponent

    if body:IsOnGround() then
        if self.InputDirection.x ~= 0 then
            -- 걷는 애니메이션
            state:ChangeState("MOVE")
        elseif self.IsCrouchKeyPressed then
            -- 엎드리는 애니메이션
            state:ChangeState("CROUCH")
        else
            -- 서 있는 애니메이션
            state:ChangeState("IDLE")
        end
    else
        -- 공중에 떠 있는 애니메이션
        state:ChangeState("FALL")
    end
}
캐릭터의 좌우 시선을 제어하는 UpdateLookDirection 함수도 추가합니다.

void UpdateLookDirection()
{
    local controller = self.Entity.PlayerControllerComponent

    -- 플레이어가 바라보는 방향
    if self.InputDirection.x ~= 0 then
        if self:SignOf(self.InputDirection.x) < 0 then
            -- 왼쪽을 바라봅니다.
            controller.LookDirectionX = -1
        else
            -- 오른쪽을 바라봅니다.
            controller.LookDirectionX = 1
        end
    end
}
OnUpdate 함수에서 UpdateAction, UpdateAnimationState, UpdateLookDirection를 호출하도록 합니다.

void OnUpdate(number delta)
{  
    -- 속도 제어
    self:UpdateVelocity(delta)

    -- 추가 : 동작 제어
    self:UpdateAction()

    -- 추가 : 애니메이션 제어
    self:UpdateAnimationState()

    -- 추가 : 좌우 시선 제어
    self:UpdateLookDirection()
}
workspace Workspace - defaultplayer DefaultPlayer - property Property - move SideviewbodyComponent에서 EnableDownJump에 체크합니다. DownJumpSpeed 값으로 3.3을 입력합니다.
sideviewbody2

start 시작을 누른 뒤 테스트해봅시다. 캐릭터의 동작 및 애니메이션, 시선 제어가 정상적으로 되는지 확인합니다.
slide2

더 미끄러운 타일 만들기
GetUnderfootTile 함수를 사용하면 캐릭터가 현재 밟고 있는 타일이 무엇인지 알 수 있습니다. 이를 이용해서 얼음 타일을 밟으면 마찰력이 감소해 더 많이 미끄러지는 기능을 만들어 보겠습니다.

mydesk MyDesk 아래에 새 스크립트 컴포넌트 scriptcomponent IceTileChecker를 만든 뒤, DefaultPlayer DefaultPlayer에 추가합니다.

scriptcomponent IceTileChecker를 연 뒤, 아래와 같이 프로퍼티를 추가합니다.

Property :
[None]
number IceDrag = 2
[None]
number DefaultDrag = 0
OnBeginPlay 함수를 추가하고 아래와 같이 내용을 작성합니다.

[client only]
void OnBeginPlay()
{
    self.DefaultDrag = self.Entity.CustomPlayerController.Drag
}
OnUpdate 함수를 추가하고 GetUnderfootTile 함수를 사용해 캐릭터가 밟은 타일이 "Ice"일 경우, 더 많이 미끄러지도록 해봅시다.

[client only]
void OnUpdate(number delta)
{
    local customController = self.Entity.CustomPlayerController
    local body = self.Entity.SideviewbodyComponent
    local underfootTile = body:GetUnderfootTile()

    customController.Drag = self.DefaultDrag

    if underfootTile == nil then
        return
    end

    if underfootTile.Name == "Ice" then
        customController.Drag = self.IceDrag
    end
}
start 시작을 누른 뒤 테스트해봅시다. 눈 타일보다 얼음 타일에서 더 잘 미끄러지는 것을 확인합니다.
