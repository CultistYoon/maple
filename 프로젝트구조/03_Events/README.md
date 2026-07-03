# 03_Events — 커스텀 EventType

**모듈 간 통신의 공용 어휘.** `Create Scripts > Create EventType`으로 만든 엔트리만 둡니다.
모듈은 여기 정의된 이벤트를 `self.Entity:SendEvent(event)`로 쏘고, 반응은 구독자가 결정합니다.

## 여기 들어가는 것
- EventType 엔트리: `PlayerDamagedEvent`, `MonsterDiedEvent`, `ItemPickedEvent` ...
- 이벤트에 실어 보낼 데이터는 EventType의 Property로 선언

```lua
-- PlayerDamagedEvent (EventType)
Property:
    number CurrentHealth = 0
    number MaxHealth = 0
```

## 규칙
1. 이벤트는 **"무슨 일이 일어났다"**(과거형 사실)만 담는다. "무엇을 하라"(명령)가 아님.
   - ✅ `MonsterDiedEvent` / ❌ `PlayDeathAnimationEvent`
2. 페이로드는 구독자가 판단에 필요한 최소 데이터만.
3. 이벤트 개수가 늘어나는 건 좋은 신호 (모듈이 직접 호출 대신 이벤트로 말하고 있다는 뜻).

## 네이밍
`주어 + 과거동사 + Event` (PascalCase) — `PlayerDamagedEvent`, `EnemyDiedEvent`, `SunriseEvent`
핸들러 쪽은 `Handle + 이벤트명` — `HandlePlayerDamagedEvent`
