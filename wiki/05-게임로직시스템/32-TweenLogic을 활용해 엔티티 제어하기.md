# TweenLogic을 활용해 엔티티 제어하기

<!-- 출처: reference/TaskWiki.md · 문서 #122 -->


학습 과정 소개
TweenLogic을 사용해 엔티티를 확대, 축소, 회전, 이동시킬 수 있습니다. Tweener를 함께 확인해보세요.

TweenLogic 개념
TweenLogic은 엔티티에 애니메이션 효과를 줄 수 있는 다양한 함수를 제공합니다. 여러 프레임에 걸쳐 Entity의 위치나 크기를 변화시키거나 회전시킬 수 있습니다.
다양한 함수를 사용해 엔티티를 Tween 시켜 애니메이션을 한 번의 함수 호출로 간단하게 만들 수 있습니다.

TweenComponent와의 차이
TweenLogic과 TweenComponent들은 월드에서 보기에는 비슷한 동작처럼 보이지만 다른 기능이므로 크리에이터의 제작 계획에 적합한 것을 선택해 사용하면 됩니다.
TweenLineComponent, TweenCircularComponent, TweenFloatingComponent는 스크립트를 작성하지 않고 엔티티에 애니메이션을 부여하고 싶을 때 사용을 권장합니다. 세 컴포넌트는 네트워크 최적화가 되어있기에 멀티 플레이 환경에서 다수의 엔티티를 Tween 시킬 때 성능 향상을 기대할 수 있기 때문입니다.
TweenLogic는 동적 트윈이 필요한 경우 사용할 수 있습니다. TweenLogic의 함수들이 반환하는 Tweener 객체에는 Reverse, Delay 기능이 포함되어 있으며, SetOnEndCallback 함수를 통해 Tween 종료 시 수행할 동작을 정의할 수도 있습니다.

EaseType
TweenLogic의 함수를 사용할 때 EaseType을 설정해 이동 모양을 결정합니다. EaseType 중 원하는 타입을 선택해 엔티티마다 다른 움직임을 만들 수 있습니다. 일정한 시간 동안 같은 위치로 향하는 엔티티가 2개 있더라도 각각 다른 EaseType을 사용했다면 어떤 엔티티는 바닥으로 떨어진 공처럼 통통 튀며 이동하고, 또 다른 엔티티는 느리게 이동하다 점점 빠르게 목적지에 도달하게 됩니다.
예를 들어 TweenLogic의 MoveTo(Entity entity, Vector2 destination, number duration, EaseType type) 함수는 특정 지점을 목적지로 지정해 엔티티를 이동시킵니다. 해당 함수를 호출하면, 여러 프레임에 걸쳐 목적지까지 조금씩 이동해 도착합니다. 이때 어떤 EaseType을 사용하는지에 따라 엔티티의 이동 모습이 달라집니다.
EaseType은 Easing 함수를 이해해야 합니다. Easing 함수의 x 축은 시간, y 축은 이동 위치를 의미합니다. 그러므로 엔티티를 (1,1)에서 (2,2)까지 3초 동안 움직인다고 가정해 x, y축의 원점과 끝값을 알 수 있습니다. x의 원점 값은 0, 끝값은 3이 되고, y축은 이동 위치이기에 원점 값은 (1,1), 끝값은 (3,3)이 됩니다. 이 시간 동안 함수에 따라 다른 모양으로 움직이고, 가속 변화도 달라집니다.
Easing 함수 그래프는 엔티티 구간 이동시키기의 참고 자료를 확인하세요.

Ease 함수
Ease 함수는 Tweener 객체를 생성하지 않으며 프레임마다 자동으로 업데이트되지 않습니다. 그러므로 움직임이 필요하다면 크리에이터가 직접 매 프레임 Ease() 함수를 호출해야 합니다. 이에 반해 MakeTween()으로 생성되어 Tweener의 Play() 함수가 호출된 Tweener 객체나 PlayTween()으로 생성되어 자동으로 재생되는 Tweener 객체는 TweenLogic에 의해 매 프레임 자동으로 업데이트됩니다.

아래 함수를 활용해 특정 진행률에서의 반환 값을 구할 수 있습니다. Easing 함수 그래프에서 x축은 Tween의 진행률로 tweenTime을 duration으로 나눈 값입니다. y축은 startValue에서 endValue 사이의 반환 값입니다.

number Ease(number startValue, number endValue, number duration, EaseType type, number tweenTime)
TweenLogic 활용하기
이동시키기
MoveTo()를 활용해 엔티티를 이동시킬 수 있습니다.
이동

새로운 컴포넌트를 생성하고, 특정 엔티티에 추가합니다.

엔티티가 이동할 목적지, 시간, EaseType을 작성합니다.

반환하는 Tweener의 지연 시간, 반복 타입, 횟수, 자동 파괴 여부 처리를 함께 작성합니다.
자동 파괴를 false로 하거나 LoopCount를 -1로 설정해 트윈이 계속 실행되도록 하는 경우 의도치 않게 더 이상 작동하지 않는 Tweener 객체가 쌓일 수도 있습니다. 이러한 Tweener 객체가 지나치게 많아지면 월드에 성능 하락이 생길 수 있으므로 적절한 시기에 tween을 파괴해줘야 합니다. 컴포넌트의 OnEndPlay 혹은 Tween시킬 대상 엔티티가 파괴되는 시점에 Tweener의 Destroy() 함수를 호출하여 파괴하는 것을 권장합니다.

Property:
[None]
any tween = nil
[Sync]
number LoopCount = 0
[Sync]
number Delay = 0

Method:
[server only]
void OnBeginPlay()
{
    self.tween = _TweenLogic:MoveTo(self.Entity, Vector2(0.5, self.Entity.TransformComponent.Position.y), 4, EaseType.BounceEaseOut)
    self.tween.Delay = self.Delay
    self.tween.LoopCount = self.LoopCount
    self.tween.LoopType = TweenLoopType.PingPong
    self.tween.AutoDestroy = false
}

[server only]
void OnEndPlay()
{
    self.tween:Destroy()
}
회전시키기
RotateTo()를 활용해 엔티티를 회전시킬 수 있고, TweenLogic:RotateAroundOffset()를 활용해 특정 엔티티의 offset을 기준으로 따라다니게 회전시킬 수 있습니다.

새로운 컴포넌트를 생성하고, 특정 엔티티에 추가합니다.

angle을 360도로 설정해 엔티티가 한 바퀴 돌 수 있게 작성합니다.

Method:
void OnBeginPlay()
{
    self._T.tween = _TweenLogic:RotateTo(self.Entity, 360, 5, EaseType.Linear)
    self._T.tween.LoopCount = -1 
}

[server only]
void OnEndPlay()
{
    self._T.tween:Destroy()
}
컴포넌트를 생성하고, 특정 엔티티에 추가합니다.

프로퍼티에 새로운 RotateCenter를 추가하고, 프로퍼티 에디터 창에 중심점으로 삼을 엔티티를 선택합니다.

중심 엔티티를 따라 돌 수 있게 아래와 같이 작성합니다.

Property:
[Sync]
Entity RotateCenter = nil

Method:
[server only]
void OnBeginPlay()
{
    if self.RotateCenter == nil then
        do return end
    end

    local offset = self.RotateCenter.TransformComponent.Position - self.Entity.TransformComponent.Position
    self._T.tween = _TweenLogic:RotateAroundOffset(self.Entity, 360, offset:ToVector2(), true, 5, EaseType.Linear)
    self._T.tween.LoopCount = -1
}

[server only]
void OnEndPlay()
{
    self._T.tween:Destroy()
}
엔티티 크기 변화시키기
ScaleTo()를 활용해 엔티티의 크기가 커졌다 작아지게 만들 수 있습니다.

크기조절

새로운 컴포넌트를 생성하고, 특정 엔티티에 추가합니다.

엔티티를 확대, 축소하고 싶은 크기를 Vector2() 값으로 입력합니다.

Method:
[server only]
void OnBeginPlay()
{
    local tween = _TweenLogic:ScaleTo(self.Entity, Vector2(2.5, 2.5), 4, EaseType.QuadEaseInOut)
    tween.LoopCount = -1
    tween.LoopType = TweenLoopType.PingPong
}
투명도 조절하기
MakeTween()에서 Alpha 값을 조절해 특정 엔티티가 점점 옅어지게 만들 수 있습니다.

Alpha

새로운 컴포넌트를 생성하고, 특정 엔티티에 추가합니다.

MakeTween()의 startvalue를 SpriteRenderer의 a로 지정하고, endvalue를 0으로 지정해 엔티티가 투명해질 수 있도록 아래와 같이 작성합니다.

Method:
[server only]
void OnBeginPlay()
{
    local spriteRenderer = self.Entity.SpriteRendererComponent
    local tween -- tweener를 할당할 변수 미리 선언
    local tweenAlpha = function(tweenValue)
        if isvalid(spriteRenderer) == false then
            tween:Destroy()
        end
        spriteRenderer.Color.a = tweenValue
    end

    tween = _TweenLogic:MakeTween(spriteRenderer.Color.a, 0, 0.5, EaseType.Linear, tweenAlpha)
    tween.LoopCount = -1
    tween.LoopType = TweenLoopType.PingPong
    tween.AutoDestroy = false
    tween:Play()

    _TimerService:SetTimerOnce(function() self.Entity:RemoveComponent(SpriteRendererComponent) end, 5)
}
활용 예제
높은 곳에서 공을 던졌을 때 공이 앞으로 나아감과 동시에 통통 튀게 만들어 봅시다.

ball

새로운 model Model_Ball 모델을 생성합니다. component TransformComponent, sprite SpriteRendererComponent를 추가하고, 아래의 Ruid를 사용합니다.

SpriteRuid: d4dddd1f07d445939433f70cd1aa82fa

새로운 component BallComponent 생성하고, model Model Ball에 추가합니다.

공이 돌면서 날아가게 만들기 위해 PlayTween()과 RotateTo()를 함께 활용해 아래와 같이 작성합니다.

Property:
[None]
number posX = 0
[None]
number posY = 0

Method:
[server only]
void OnBeginPlay()
{
    local transform = self.Entity.TransformComponent
    self.posX = transform.Position.x
    self.posY = transform.Position.y

    local yDestination = 0.3
    local tweenDuration = 3

    local xTween = _TweenLogic:PlayTween(self.posX, self.posX + _UtilLogic:RandomIntegerRange(40, 100)/10, tweenDuration, EaseType.CubicEaseOut, function(val) self.posX = val end)
    local yTween1 = _TweenLogic:PlayTween(self.posY, yDestination, tweenDuration, EaseType.BounceEaseOut, function(val) self.posY = val end)

    local rotateTween = _TweenLogic:RotateTo(self.Entity, -1800 * _UtilLogic:RandomIntegerRange(95, 105)/100, tweenDuration, EaseType.QuartEaseOut)
}

[server only]
void OnUpdate(number delta)
{
    --  프레임마다 변경되는 posX, PosY 프로퍼티 값을 TransformComponent.Position에 할당
    local transform = self.Entity.TransformComponent
    transform.Position = Vector3(self.posX, self.posY, transform.Position.z)
}
위의 예시에서 PlayTween()은 마지막 매개 변수로 Action tweenFunction를 받고 있습니다. tweenFunction은 매 프레임 호출되고, 매개 변수로 Tween이 시작된 후부터 Ease 결괏값을 받습니다. 만약 Tween이 시작된 후 1.2초가 지났다면 Ease의 결괏값은 Ease(self.posY, yDestination, tweenDuration, EaseType.BounceEaseOut, 1.2)가 됩니다. 그러므로 function(val) self.posX = val end는 Ease 함수의 결괏값(val)을 받아 self.posY 프로퍼티에 할당합니다.

더 알아보기
PlayTween을 사용할 때 Vector2를 매개 변수로 받는 PlayTween을 두 번 호출해 하나는 x를, 하나는 y를 조작하게 아래와 같이 구현할 경우 정상 동작하지 않습니다. Vector2는 x, y를 쌍으로 사용하므로 Tween 반환 값을 덮어쓰기 때문입니다.

-- 공을 (8, 0, 0)의 위치로 던진다고 가정
_TweenLogic:PlayTween(현재위치, Vector3(8, 0, 0), tweenDuration, EaseType.CubicEaseOut, function(val) self.Entity.TransformComponent.Position = val end)
_TweenLogic:PlayTween(현재위치, Vector3(8, 0, 0), tweenDuration, EaseType.BounceEaseOut, function(val) self.Entity.TransformComponent.Position = val end)
component SpawnBallOnAttack 컴포넌트를 생성하고, player DefaultPlayer에 추가합니다. 아래와 같이 플레이어가 공격할 때 model Model_Ball을 소환하게 작성합니다.

Event Handler:
[server only] [self]
HandlePlayerActionEvent(PlayerActionEvent event)
{
    -- Parameters
    local ActionName = event.ActionName
    local PlayerEntity = event.PlayerEntity
    --------------------------------------------------------
    if ActionName == "Attack" then
    	local parent = self.Entity.Parent
    	local spawnPosition = self.Entity.TransformComponent.Position + Vector3(0, 0.5, 0)
    	_SpawnService:SpawnByModelId("model://8474ac05-aac0-49bf-a171-84b7d8b9f42c", "Ball", spawnPosition, parent)
    end
}
참고 가이드
엔티티 구간 이동시키기

엔티티의 위치, 크기, 회전 조정

물체의 이동 Ⅰ
