# 04_AI — 행동 트리 부품 (BTNodeType)

**AI 패턴 1개 = 노드 1개.** `Create Scripts > Create BTNodeType`으로 만든 행동 노드와,
필요하면 BehaviourTree 엔트리를 둡니다. (BT = Behaviour Tree)

## 여기 들어가는 것
- Action Node (BTNodeType): `ChargeBTNode`(돌진), `ChaseBTNode`(추적), `JumpAttackBTNode`(점프공격)
- Decorator/조건 노드: `HasTargetDeco` 류
- ※ `SequenceNode`/`SelectorNode` 등 조립용 복합 노드는 네이티브라 만들 필요 없음

## 안 들어가는 것
- ❌ 트리를 조립하는 `MonsterAIComponent` → 그건 접착제, `02_Connectors`
- ❌ 스탯/피격 처리 → `01_Modules`

## 규칙
1. 노드는 **패턴 하나만** 담당. 돌진 노드가 드랍/사운드를 알면 안 됨.
2. 속도·지속시간 등 수치는 `[None]` Property로 → 같은 노드를 값만 바꿔 재사용.
3. 엔티티 접근은 `self.ParentAI.Entity` 경유. 특정 몬스터 이름/GUID 의존 금지.
4. `OnBehave`는 `Running / Success / Failure`를 정확히 반환 (트리 흐름의 전부).
5. 몬스터 간 차이는 노드 코드가 아니라 **어떤 노드를 꽂느냐**(`07_Models` + 프로퍼티)로.

## 네이밍
`패턴 + BTNode` (PascalCase) — `ChargeBTNode`, `PatrolBTNode`
접미사 `BTNode`가 "행동 트리에 꽂는 노드 엔트리"라는 표식입니다.
