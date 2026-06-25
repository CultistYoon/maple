# 다양한 물리 joint 활용하기

<!-- 출처: reference/TaskWiki.md · 문서 #105 -->


학습 과정 소개
물리를 사용하는 맵에서 특정 엔티티끼리의 운동 방식을 설정하는 방법을 알아봅시다. 다양한 JointComponent를 활용해 다양한 운동을 하는 엔티티를 만들어 월드 제작에 활용할 수 있습니다.

Joint
Joint란 물리 법칙을 적용한 맵에서 특정 엔티티끼리만 연결해 서로 영향을 주고받을 수 있게 만드는 특정 연결부를 의미합니다.
아래의 그림과 같이 Entity A와 Entity B가 서로 영향을 주고받을 수 있도록 하는 연결부가 바로 Joint입니다. 기준 엔티티인 Entity A에 Joint 연결 위치(LocalAnchor A)를 설정하고 연결할 엔티티(TargetEntityRef)인 Entity B에도 Joint 연결 위치(LocalAnchor B)를 설정하면 Entity A와 Entity B가 연결됩니다.

1

Anchor의 위치는 엔티티의 ColliderOffset을 기준으로 떨어진 정도를 설정합니다. 서로 연결된 엔티티는 크리에이터의 의도에 따라 충돌할 수도 있고, 충돌하지 않을 수도 있습니다.

Entity A: JointComponent를 가진 엔티티로 Joint를 추가해 다른 엔티티를 TargetEntityRef로 사용할 수 있습니다.

ColliderOffset: 엔티티의 PhysicsColliderComponent의 ColliderOffset입니다. LocalAnchor 위치의 원점으로 활용됩니다.

LocalAnchorA: JointComponent를 가진 Entity A의 Anchor를 설정합니다. Entity A의 ColliderOffset을 원점으로 합니다.

Entity B: Joint를 연결할 엔티티로 Entity A의 JointComponent에서 TargetEntityRef로 지정합니다.

TargetEntityRef: Joint를 연결할 Entity입니다.

LocalAnchorB: Joint를 연결할 Entity인 Entity B의 Anchor를 설정합니다. Entity B의 ColliderOffset을 원점으로 합니다.

2

Anchor
Joint가 동작하는 기준점입니다. 엔티티의 ColliderOffset 위치를 Anchor의 원점으로 삼습니다. 예를 들어 아래 그림처럼 LocalAnchor A, B의 값이 동일하게 (3,0)이라도 기준이 되는 엔티티의 offset이 다릅니다. LocalAnchor는 다른 곳에 위치하고, Entity A, B 동작의 기준점은 지점입니다.

LocalAnchor A의 기준 Offset은 Entity A이고 LocalAnchor B의 기준 Offset은 Entity B입니다.

3

anchor1

Motor
Motor를 사용하면 Entity에 특정 방향으로 운동하도록 힘을 가합니다. RevoluteJointComponent, WheelJointComponent, PrismaticJointComponent에서 사용합니다. 모터를 사용하기 위해 MotorEnable 프로퍼티를 true로 설정하면 목표 속도에 맞게 엔티티가 돕니다. 목표 속도란 MotorSpeed의 값을 의미합니다. 예를 들어 MotorSpeed가 100이고, 속도가 100에 도달한 상태에서 MotorSpeed 값이 10으로 줄게 되면 속도가 감소합니다.

motor

JointComponent 종류
6가지 DistanceJointComponent, RevoluteJointComponent, PrismaticJointComponent, PulleyJointComponent, WeldJointComponent, WheelJointComponent가 있습니다. 종류마다 다른 특성을 가지고 있으므로 크리에이터가 제작하고 싶은 의도에 맞는 JointComponent를 사용해야 합니다.

DistanceJointComponent
DistanceJointComponent는 두 엔티티의 거리 관련 제한을 설정합니다. LocalAnchorA, B 사이의 거리(Length)가 일정하게 유지됩니다.

주요 프로퍼티	설명
Length	Joint로 연결된 두 Entity가 유지할 거리를 설정합니다.
distance

RevoluteJointComponent
RevoluteJoint는 엔티티의 회전과 관련된 제한을 설정합니다. UseLimits를 활성화한 후, LowerAngle, UpperAngle를 활용해 회전 각도를 제한할 수 있습니다.
엔티티가 회전할 때는 LocalAnchorA와 B가 만나는 지점을 공통의 Anchor로 사용합니다. 또한 Motor를 사용하면 Anchor를 기준으로 회전하는 힘을 받을 수 있습니다.

주요 프로퍼티	설명
UseLimits	상대적 각도에 제한을 설정할지 여부를 결정합니다.
LowerAngle	최소 상대 각도를 설정합니다. Entity의 Local Vector2(1, 0)을 기준으로 합니다.
UpperAngle	최대 상대 각도를 설정합니다. Entity의 Local Vector2(1, 0)을 기준으로 합니다.
MotorSpeed	Motor의 목표 속도를 설정합니다. 양수일 경우 CCW(반시계) 방향으로 회전합니다.
revolute

PrismaticJointComponent
PrismaticJointComponent는 엔티티가 축을(LocalAxis) 따라 엔티티가 선형 운동하도록 제한을 설정합니다.
LowerTranslation, UpperTranslation 값을 설정해 엔티티가 이동하는 최대, 최소 거리를 제한할 수 있습니다. LocalAxis의 위치는 LocalAnchor를 기준으로 합니다.

주요 프로퍼티	설명
UseLimits	상대적 이동 거리 제한을 둘지 여부를 설정합니다.
LowerTranslation	최소 상대적 이동 가능 거리를 설정합니다.
UpperTranslation	최대 상대적 이동 가능 거리를 설정합니다.
MotorEnable	Motor를 사용할지 여부를 설정합니다. True일 경우 연결된 Entity가 LocalAxis 방향의 힘을 받습니다.
MotorSpeed	Motor의 목표 속도를 설정합니다. MotorEnable이 True여야 동작합니다.
primatic

PulleyJointComponent
PulleyJointComponent는 LocalAnchor와 GroundAnchor 사이의 거리들의 총길이 합이 일정하게 유지됩니다. 특정 엔티티의 선 길이가(Length) 짧아지면 다른 엔티티의 선 길이가 길어지며 선의 총길이는 유지됩니다. 총길이는 Entity A와 GroundAnchorA 사이의 최초 거리 + Ratio * Entity B와 GroundAnchorB 사이의 최초 거리 공식에 따라 정해집니다.
각 엔티티의 선은 LocalAnchor와 GroundAnchor 사이의 거리로 GroundAnchor의 원점은 LocalAnchor의 위치입니다. Ratio는 Entity와 GroundAnchor 사이의 거리가 줄어드는 비율을 결정합니다.
만약 Ratio가 3일 때 Entity A의 선이 3만큼 줄어든다면, Entity B와의 선은 1만큼 늘어나도 Entity A의 선은 Entity B의 선에 비해 구속력(constraint force)이 1/3입니다.

주요 프로퍼티	설명
Ratio	PulleyJoint를 이루는 양쪽 가상의 줄의 구속력 비율을 설정합니다.
pulley

WeldJointComponent
연결된 엔티티끼리 함께 움직이도록 설정합니다. 마치 꼬챙이에 양 끝을 끼운 것처럼 서로 일정한 거리가 벌어져 있는 상태로 움직입니다. 연결된 엔티티는 상대적 이동 및 회전이 제한됩니다.

weld

WheelJointComponent
WheelJoint는 연결된 엔티티가 바퀴처럼 동작하도록 제한을 설정합니다. Motor를 사용한 TargetEntityRef는 MotorSpeed 값을 목표 속도로 사용합니다.

주요 프로퍼티	설명
MaxMotorTorque	목표 모터 속도에 도달하기 위한 Joint의 모터에 적용할 수 있는 최대 힘을 설정합니다.
MotorEnable	Motor를 사용할지 여부를 설정합니다. True일 경우 연결된 Entity가 LocalAxis 방향의 힘을 받습니다.
MotorSpeed	Joint의 목표 모터 속도를 설정합니다. MotorEnable이 True여야 동작합니다.
wheel

Joint 추가하기
JointComponent를 추가하는 방법은 모두 동일합니다.

PhysicsRigidbodyComponent, PhysicsColliderComponent를 추가한 엔티티를 두 개 생성하고, 배치합니다.

사용하고 싶은 JointComponent를 추가합니다. Size에 생성할 Joint 개수를 입력합니다.
size

TargetEntityRef로 사용할 엔티티 선택한 후, LocalAnchor A, B의 위치를 설정합니다.
joint

활용 예제
RevoluteJointComponent를 활용해 공을 튀기는 간단한 게임을 만들어 봅시다.
example

준비
타일맵모드를 RectTile로 변경합니다.
5

Hierachy - World - maps - map01 - PhysicsSimulatorComponent를 추가합니다.

Hierachy - World - maps - map01 - RectTileMap - RectTileMapComponent - PhysicsInteractable을 활성화합니다.

공이 이리저리 부딪힐 수 있도록 Static 타입 물리 엔티티를 배치합니다. 아래가 뚫린 사다리꼴 모양으로 배치해 봅시다.

SpriteRUID: 1ce2eff829ae4346bc89a3f0a357ac0e
static

공 만들기
새로운 Ball 모델을 만들고, PhysicsRigidbodyComponent, PhysicsColliderComponent를 추가합니다.

Ball SpriteRUID: 164e94bea20441adac2af9c6f800bdf3

PhysicsRigidbodyComponent의 BodyType을 Dynamic으로 변경합니다.

PhysicsColliderComponent의 ColliderType을 Circle로 변경하고, 스프라이트 크기에 맞게 CircleRadius를 조절합니다.

중력을 받아 공이 떨어질 수 있도록, 공중에 배치합니다.

장애물 만들기
새로운 Obstacle 모델을 만들고, PhysicsRigidbodyComponent, PhysicsColliderComponent를 추가합니다.

SpriteRUID: 3ada0e4cc7f44cb988932f1b183ec778

PhysicsRigidbodyComponent의 BodyType을 Static으로 변경합니다.

PhysicsColliderComponent의 ColliderType을 Circle로 변경하고, 스프라이트 크기에 맞게 CircleRadius를 조절합니다.

레버 만들기
새로운 LeftEntity, LeftBar 오브젝트 엔티티를 만들고, PhysicsRigidbodyComponent, PhysicsColliderComponent를 추가합니다.

LeftEntity SpriteRUID: e75cac80f719471fa482195531ed57cc

LeftBar SpriteRUID: 0308ac89b10843fcab6384aa43f6ae22

원형 모양 엔티티에 RevoluteJointComponent를 추가하고, Joint에 1을 입력합니다. TargetEntityRef에 LeftBar를 지정하고, LocalAnchorB, LowerAngle, UpperAngle, MotorSpeed, UseLimits 값을 아래와 같이 지정합니다.
left

위의 두 엔티티를 복사해 반대쪽을 만듭니다.
right

새로운 Swing 스크립트 컴포넌트를 생성하고, DefaultPlayer에 추가합니다.

N, M을 눌렀을 때 RevoluteJoint의 모터를 사용하고, 떼면 사용하지 않도록 아래와 같이 입력합니다.

Property:
[Sync]
Entity Left = /maps/map01/LeftEntity
[Sync]
Entity Right = /maps/map01/RightEntity

Method:
[server]
void MoveLeft(boolean enable)
{
    self.Left.RevoluteJointComponent:SetMotorEnable(1, enable)
}

[server]
void MoveRight(boolean enable)
{
    self.Right.RevoluteJointComponent:SetMotorEnable(1, enable)
}

Event Handler:
[service: InputService]
HandleKeyDownEvent(KeyDownEvent event)
{
    -- Parameters
    local key = event.key
    --------------------------------------------------------
    if key == KeyboardKey.N then
    	self:MoveLeft(true)
    elseif key == KeyboardKey.M then
    	self:MoveRight(true)
    end
}

[service: InputService]
HandleKeyReleaseEvent(KeyReleaseEvent event)
{
    -- Parameters
    local key = event.key
    --------------------------------------------------------
    if key == KeyboardKey.N then
    	self:MoveLeft(false)
    elseif key == KeyboardKey.M then
    	self:MoveRight(false)
    end
}
시작을 눌러 N, M을 눌렀을 때 막대가 각각 움직이는지 확인합니다.

참고 가이드
물리 사용하기

충돌 그룹 만들기

엔티티에 물리 적용하기Physics Owner 지정하기
메이플스토리 월드에서의 기본적인 물리 연산 방식에 대해 알아봅시다. Physics Owner를 변경했을 때의 변화에 대해서도 알아봅시다.

참고 가이드
물리 사용하기

기본 물리 연산 방식
메이플스토리 월드는 최적화된 환경을 제공하기 위해 접속한 클라이언트 중 하나를 물리 연산의 주체로 임의 선정합니다. 임의로 선정된 클라이언트를 Host Client라고 칭합니다. 이 Host Client가 연산한 결괏값을 서버가 받아 온 뒤, 모든 클라이언트에게 전달해 동기화합니다.(TransformComponent.position, 강체의 위치, 속도 등)
이 연산 방식으로 인해 엔티티가 충돌한 뒤에 크리에이터가 PhysicsContactEvent에서 정의한 다음 명령이 모든 클라이언트에게 즉시 동기화되지 않습니다. 즉 메이플스토리 월드의 기본 물리 연산 방식은 강체들의 충돌 직후 즉시 무언가를 실행시킬 수 없습니다.

충돌이 Host Client에서 발생하면, 이 충돌 정보를 서버로 전송합니다.

서버에서 PhysicsContactBeginEvent가 발생합니다.

발생한 이벤트와 크리에이터가 작성한 다음 작업의 명령을 서버가 Host Client로 전달합니다.

Host Client가 수행한 명령의 결과를 서버로 전달하고, 명령의 결과를 모든 클라이언트로 동기화합니다.

[object Object]

예제
예제를 통해 기본 물리 연산의 작동 방식을 살펴봅시다. 각기 다른 방향에서 같은 속도로 이동하는 눈덩이가 충돌하게 만들고 충돌 직후 반발 없이 바로 멈추도록 예제를 만들어 봅시다.
이 예제를 만들면 크리에이터는 강체들이 충돌한 직후 어떠한 반발도 없이 즉시 충돌한 지점에서 멈출 수 있을 거라고 생각합니다. 그러나 호스트 클라이언트가 연산한 값을 서버가 받은 뒤 모든 클라이언트에게 동기화해주는 과정에서 충돌 직후 약간의 떨림이 발생하는 것을 확인할 수 있습니다.

[object Object]

새로운 SnowBall 모델을 생성합니다.

모델에 PhysicsRigidbodyComponent를 추가하고, GravityScale 값과 Restitution 값을 수정합니다.

GravityScale: 0

Restitution: 1

[object Object]

SnowBall 모델에 PhysicsColliderComponent를 추가하고, EnableContactEvent를 true로 설정합니다.
[object Object]

새로운 SnowBall 컴포넌트를 생성하고 SnowBall 모델에 추가합니다.

SnowBall 컴포넌트에 강체가 충돌하면 속도가 0이 되도록 아래와 같이 작성합니다.

Event Handler:
[self]
HandlePhysicsContactBeginEvent(PhysicsContactBeginEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: PhysicsColliderComponent
    -- Space: Server, Client
    ---------------------------------------------------------

    -- Parameters
    -- local ContactedBodyEntity = event.ContactedBodyEntity
    ---------------------------------------------------------
    if self:IsClient() then
        log("Client Collision Event")

    else 
        log("Server Collision Event")
        self.Entity.PhysicsRigidbodyComponent:SetLinearVelocity(Vector2.zero)
    end
}
새로운 SnowBallShooter 컴포넌트를 생성합니다.

map01에 SnowBallShooter를 추가합니다.
[object Object]

SnowBallShooter 컴포넌트에 아래와 같이 작성합니다.
서버에서 SpawnService를 통해 공을 스폰시키고, ApplyLinearImpulse()를 사용해 강체들이 충돌할 수 있도록 아래와 같이 작성합니다.

Property:
[Sync]
string Model_SnowBall = "model://9aa7c347-c258-47d1-b92a-35d078e1f092"
[None]
table Dirs ={}

Method:
void OnBeginPlay()
{
    self:InitDirs()
    self:StartGame()
}

void InitDirs()
{
    self.Dirs[1] = Vector3(math.sqrt(3)/2, 1/2, 0)
    self.Dirs[2] = Vector3(0, -1,0)
    self.Dirs[3] = Vector3(-math.sqrt(3)/2, 1/2, 0)
}

[server only]
void StartGame()
{
    wait(2)
    log("launch snowballs")


    --3방향에서 눈뭉치 발사
    self:SpawnAndShoot(1)
    self:SpawnAndShoot(2)
    self:SpawnAndShoot(3)
}

[server]
void SpawnAndShoot(integer index)
{
    local myBall = _SpawnService:SpawnByModelId(self.Model_SnowBall, "ball"..tostring(index) , self.Dirs[index]*-6, self.Entity)
    myBall.PhysicsRigidbodyComponent:SetClientAsPhysicsOwner(_UserService.Users.Keys[1])
    myBall.PhysicsRigidbodyComponent:ApplyLinearImpulse(self.Dirs[index]:ToVector2()*4)  
}
Physics Owner 지정
Physics Owner는 특정 강체의 물리 연산의 주체를 지정하기 위해 사용합니다. PhysicsOwner를 지정하게 되면 지정된 연산 주체가 물리 연산과 충돌 이벤트를 처리하게 됩니다. Server, 특정 Physics Owner Client, ClientOnly를 Physics Owner로 지정할 수 있고, 연산 결과는 TransformComponent 업데이트에 우선 적용됩니다.
크리에이터가 제작하는 월드의 성격에 따라 Physics Owner를 적절하게 지정하면 충돌 판정 오류, 충돌 지연, 월드 전체 성능 저하 등의 문제를 해결하고, 최적화된 월드를 제작하는데 도움이 됩니다.

Physics Owner가 Client일 때
SetClientAsPhysicsOwner()를 사용해 특정 강체의 물리 연산을 특정 클라이언트에 위임할 수 있습니다. 강체의 물리 연산을 하는 특정 클라이언트는 Physics Owner Client가 됩니다. PhysicsContactBeginEvent가 Physics Owner Client와 Server에서 발생하기 때문에 지정된 강체의 충돌 타이밍을 Physics Owner Client가 정확하게 알 수 있습니다.
예를 들어 아래 그림과 같이 3개의 강체가 지면을 향해 떨어지게 만든다고 했을 때 각 강체마다 Physics Owner Client를 각각 지정했다고 생각해봅시다. 이 경우 각각의 클라이언트에 지정된 강체에서 발생한 충돌 이벤트 발생 시점을 보다 더 정확하게 측정할 수 있게 됩니다.

6
clinet_snowball

아래 로그처럼 Client의 값이 Server의 값보다 더 정확하게 나오는 것을 확인할 수 있습니다. Server의 Y축 로그 값은 강체가 튀어 오른 후의 값이기 때문입니다.
[object Object]

Tip.
Physics Owner Client가 지정된 강체들끼리 충돌하는 경우 각 클라이언트의 연산 시점이 다르기 때문에 예상치 못한 결과나 값이 나올 수 있습니다. 그러므로 Physics Owner Client를 지정할 때는 해당 강체가 어떤 대상과 충돌하는지 확인하고, Physics Owner Client가 지정된 강체끼리의 충돌은 피하기를 권장합니다.

Physics Owner가 Server일 때
SetServerAsPhysicsOwner() 사용해 Physics Owner를 Server로 설정하면 서버에서 충돌 이벤트 전달, 명령 전달 등 모든 물리 연산과 관련된 처리를 서버에서 처리합니다. 충돌 후의 명령을 바로 수행하고, 동기화할 수 있기 때문에 충돌 시 지연되는 모습이 나타나지 않습니다. 그러나 서버에서 연산을 과도하게 처리할 경우 부하가 발생해 월드가 느려지게 될 수 있습니다. 서버에서 물리 연산을 할 경우 불필요한 연산을 최소화하고, 프로파일러와 디버깅을 활용해 월드의 성능을 최적화하는 작업을 반드시 거치기를 권장합니다.

예를 들어 기본 물리 연산의 예제에서 SnowBallShooter 컴포넌트의 SpawnAndShoot() 메소드에서 SetServerAsPhysicsOwner()로 수정했다고 생각해 봅시다. 아래처럼 코드를 변경하면 물리 연산을 서버에서 진행하게 됩니다. 강체들이 충돌한 순간 발생하는 PhysicsContactBeginEvent가 서버에서 처리되기 때문에 강체들이 즉시 멈추는 것을 확인할 수 있습니다.

[object Object]

[server]
void SpawnAndShoot(integer index)
{
    local myBall = _SpawnService:SpawnByModelId(self.Model_SnowBall, "ball"..tostring(index) , self.Dirs[index]*-6, self.Entity)
    myBall.PhysicsRigidbodyComponent:SetServerAsPhysicsOwner()
    myBall.PhysicsRigidbodyComponent:ApplyLinearImpulse(self.Dirs[index]:ToVector2()*4)  
}
ClientOnly로 물리 연산을 할 경우
PhysicsColliderComponent의 ClientOnly 프로퍼티를 true로 설정하면 클라이언트에서만 프로퍼티와 메소드를 조작할 수 있습니다. PhysicsContactBeginEvent 또한 클라이언트에서만 발생합니다. 각각의 클라이언트는 실시간으로 동기화된 화면을 볼 수 없게 됩니다. 따라서 함께 월드를 사용하고 있더라도 엔티티가 다른 위치에 있을 수 있습니다.

[object Object]Physics Owner 지정하기
메이플스토리 월드에서의 기본적인 물리 연산 방식에 대해 알아봅시다. Physics Owner를 변경했을 때의 변화에 대해서도 알아봅시다.

참고 가이드
물리 사용하기

기본 물리 연산 방식
메이플스토리 월드는 최적화된 환경을 제공하기 위해 접속한 클라이언트 중 하나를 물리 연산의 주체로 임의 선정합니다. 임의로 선정된 클라이언트를 Host Client라고 칭합니다. 이 Host Client가 연산한 결괏값을 서버가 받아 온 뒤, 모든 클라이언트에게 전달해 동기화합니다.(TransformComponent.position, 강체의 위치, 속도 등)
이 연산 방식으로 인해 엔티티가 충돌한 뒤에 크리에이터가 PhysicsContactEvent에서 정의한 다음 명령이 모든 클라이언트에게 즉시 동기화되지 않습니다. 즉 메이플스토리 월드의 기본 물리 연산 방식은 강체들의 충돌 직후 즉시 무언가를 실행시킬 수 없습니다.

충돌이 Host Client에서 발생하면, 이 충돌 정보를 서버로 전송합니다.

서버에서 PhysicsContactBeginEvent가 발생합니다.

발생한 이벤트와 크리에이터가 작성한 다음 작업의 명령을 서버가 Host Client로 전달합니다.

Host Client가 수행한 명령의 결과를 서버로 전달하고, 명령의 결과를 모든 클라이언트로 동기화합니다.

[object Object]

예제
예제를 통해 기본 물리 연산의 작동 방식을 살펴봅시다. 각기 다른 방향에서 같은 속도로 이동하는 눈덩이가 충돌하게 만들고 충돌 직후 반발 없이 바로 멈추도록 예제를 만들어 봅시다.
이 예제를 만들면 크리에이터는 강체들이 충돌한 직후 어떠한 반발도 없이 즉시 충돌한 지점에서 멈출 수 있을 거라고 생각합니다. 그러나 호스트 클라이언트가 연산한 값을 서버가 받은 뒤 모든 클라이언트에게 동기화해주는 과정에서 충돌 직후 약간의 떨림이 발생하는 것을 확인할 수 있습니다.

[object Object]

새로운 SnowBall 모델을 생성합니다.

모델에 PhysicsRigidbodyComponent를 추가하고, GravityScale 값과 Restitution 값을 수정합니다.

GravityScale: 0

Restitution: 1

[object Object]

SnowBall 모델에 PhysicsColliderComponent를 추가하고, EnableContactEvent를 true로 설정합니다.
[object Object]

새로운 SnowBall 컴포넌트를 생성하고 SnowBall 모델에 추가합니다.

SnowBall 컴포넌트에 강체가 충돌하면 속도가 0이 되도록 아래와 같이 작성합니다.

Event Handler:
[self]
HandlePhysicsContactBeginEvent(PhysicsContactBeginEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: PhysicsColliderComponent
    -- Space: Server, Client
    ---------------------------------------------------------

    -- Parameters
    -- local ContactedBodyEntity = event.ContactedBodyEntity
    ---------------------------------------------------------
    if self:IsClient() then
        log("Client Collision Event")

    else 
        log("Server Collision Event")
        self.Entity.PhysicsRigidbodyComponent:SetLinearVelocity(Vector2.zero)
    end
}
새로운 SnowBallShooter 컴포넌트를 생성합니다.

map01에 SnowBallShooter를 추가합니다.
[object Object]

SnowBallShooter 컴포넌트에 아래와 같이 작성합니다.
서버에서 SpawnService를 통해 공을 스폰시키고, ApplyLinearImpulse()를 사용해 강체들이 충돌할 수 있도록 아래와 같이 작성합니다.

Property:
[Sync]
string Model_SnowBall = "model://9aa7c347-c258-47d1-b92a-35d078e1f092"
[None]
table Dirs ={}

Method:
void OnBeginPlay()
{
    self:InitDirs()
    self:StartGame()
}

void InitDirs()
{
    self.Dirs[1] = Vector3(math.sqrt(3)/2, 1/2, 0)
    self.Dirs[2] = Vector3(0, -1,0)
    self.Dirs[3] = Vector3(-math.sqrt(3)/2, 1/2, 0)
}

[server only]
void StartGame()
{
    wait(2)
    log("launch snowballs")


    --3방향에서 눈뭉치 발사
    self:SpawnAndShoot(1)
    self:SpawnAndShoot(2)
    self:SpawnAndShoot(3)
}

[server]
void SpawnAndShoot(integer index)
{
    local myBall = _SpawnService:SpawnByModelId(self.Model_SnowBall, "ball"..tostring(index) , self.Dirs[index]*-6, self.Entity)
    myBall.PhysicsRigidbodyComponent:SetClientAsPhysicsOwner(_UserService.Users.Keys[1])
    myBall.PhysicsRigidbodyComponent:ApplyLinearImpulse(self.Dirs[index]:ToVector2()*4)  
}
Physics Owner 지정
Physics Owner는 특정 강체의 물리 연산의 주체를 지정하기 위해 사용합니다. PhysicsOwner를 지정하게 되면 지정된 연산 주체가 물리 연산과 충돌 이벤트를 처리하게 됩니다. Server, 특정 Physics Owner Client, ClientOnly를 Physics Owner로 지정할 수 있고, 연산 결과는 TransformComponent 업데이트에 우선 적용됩니다.
크리에이터가 제작하는 월드의 성격에 따라 Physics Owner를 적절하게 지정하면 충돌 판정 오류, 충돌 지연, 월드 전체 성능 저하 등의 문제를 해결하고, 최적화된 월드를 제작하는데 도움이 됩니다.

Physics Owner가 Client일 때
SetClientAsPhysicsOwner()를 사용해 특정 강체의 물리 연산을 특정 클라이언트에 위임할 수 있습니다. 강체의 물리 연산을 하는 특정 클라이언트는 Physics Owner Client가 됩니다. PhysicsContactBeginEvent가 Physics Owner Client와 Server에서 발생하기 때문에 지정된 강체의 충돌 타이밍을 Physics Owner Client가 정확하게 알 수 있습니다.
예를 들어 아래 그림과 같이 3개의 강체가 지면을 향해 떨어지게 만든다고 했을 때 각 강체마다 Physics Owner Client를 각각 지정했다고 생각해봅시다. 이 경우 각각의 클라이언트에 지정된 강체에서 발생한 충돌 이벤트 발생 시점을 보다 더 정확하게 측정할 수 있게 됩니다.

6
clinet_snowball

아래 로그처럼 Client의 값이 Server의 값보다 더 정확하게 나오는 것을 확인할 수 있습니다. Server의 Y축 로그 값은 강체가 튀어 오른 후의 값이기 때문입니다.
[object Object]

Tip.
Physics Owner Client가 지정된 강체들끼리 충돌하는 경우 각 클라이언트의 연산 시점이 다르기 때문에 예상치 못한 결과나 값이 나올 수 있습니다. 그러므로 Physics Owner Client를 지정할 때는 해당 강체가 어떤 대상과 충돌하는지 확인하고, Physics Owner Client가 지정된 강체끼리의 충돌은 피하기를 권장합니다.

Physics Owner가 Server일 때
SetServerAsPhysicsOwner() 사용해 Physics Owner를 Server로 설정하면 서버에서 충돌 이벤트 전달, 명령 전달 등 모든 물리 연산과 관련된 처리를 서버에서 처리합니다. 충돌 후의 명령을 바로 수행하고, 동기화할 수 있기 때문에 충돌 시 지연되는 모습이 나타나지 않습니다. 그러나 서버에서 연산을 과도하게 처리할 경우 부하가 발생해 월드가 느려지게 될 수 있습니다. 서버에서 물리 연산을 할 경우 불필요한 연산을 최소화하고, 프로파일러와 디버깅을 활용해 월드의 성능을 최적화하는 작업을 반드시 거치기를 권장합니다.

예를 들어 기본 물리 연산의 예제에서 SnowBallShooter 컴포넌트의 SpawnAndShoot() 메소드에서 SetServerAsPhysicsOwner()로 수정했다고 생각해 봅시다. 아래처럼 코드를 변경하면 물리 연산을 서버에서 진행하게 됩니다. 강체들이 충돌한 순간 발생하는 PhysicsContactBeginEvent가 서버에서 처리되기 때문에 강체들이 즉시 멈추는 것을 확인할 수 있습니다.

[object Object]

[server]
void SpawnAndShoot(integer index)
{
    local myBall = _SpawnService:SpawnByModelId(self.Model_SnowBall, "ball"..tostring(index) , self.Dirs[index]*-6, self.Entity)
    myBall.PhysicsRigidbodyComponent:SetServerAsPhysicsOwner()
    myBall.PhysicsRigidbodyComponent:ApplyLinearImpulse(self.Dirs[index]:ToVector2()*4)  
}
ClientOnly로 물리 연산을 할 경우
PhysicsColliderComponent의 ClientOnly 프로퍼티를 true로 설정하면 클라이언트에서만 프로퍼티와 메소드를 조작할 수 있습니다. PhysicsContactBeginEvent 또한 클라이언트에서만 발생합니다. 각각의 클라이언트는 실시간으로 동기화된 화면을 볼 수 없게 됩니다. 따라서 함께 월드를 사용하고 있더라도 엔티티가 다른 위치에 있을 수 있습니다.

[object Object]아이템
아이템 생성 및 삭제
배지 등록하기
배지 관리하기
배지 서비스 활용하기
