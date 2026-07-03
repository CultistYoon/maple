# 05_States — 상태 부품 (StateType / StateSet)

**엔티티의 상태 정의.** `Create Scripts > Create StateType`으로 만든 커스텀 상태와
`Create StateSet` 엔트리를 둡니다. StateComponent가 이 부품들을 조립합니다.

## 여기 들어가는 것
- 커스텀 StateType: `BrokenState`, `StunnedState`, `EnragedState` ...
  (`OnEnter / OnUpdate / OnExit / OnConditionCheck` 구현)
- StateSet 엔트리 (StateToAvatarBodyActionSheet 등 상태→애니메이션 매핑)

## 안 들어가는 것
- ❌ IDLE/MOVE/JUMP 등 네이티브 자동 상태 (이미 시스템 제공)
- ❌ 상태 전환을 일으키는 게임 로직 → `01_Modules` (로직이 `ChangeState`를 호출)

## 규칙
1. 상태는 **"지금 무엇인가"**만 정의. "왜 이 상태가 됐나"(판단)는 로직 모듈의 일.
2. 상태 → 애니메이션 연결은 코드가 아니라 StateSet/ActionSheet 데이터로 (코드·데이터 분리).
3. 전환 조건은 `OnConditionCheck` + `AddCondition`으로 명시적으로. 암묵 전환 금지.
4. 상태 변화 알림이 필요하면 StateChangeEvent 구독 (뷰가 여기 반응 → `06_View`).

## 네이밍
`형용사/상태 + State` — `BrokenState`, `StunnedState`
StateSet은 `대상 + StateSet` — `MonsterStateSet`, `BossStateSet`
