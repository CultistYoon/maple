# 01_Modules — 재사용 로직 모듈 (70%)

**독립적으로 동작하는 레고 블록.** 다른 월드/엔티티에 그대로 붙여도 도는 Script Component만 둡니다.

## 여기 들어가는 것
- 순수 로직 Component: `HealthComponent`, `MonsterStatComponent`, `EnemySpawnerComponent`
- 네이티브 확장: `MonsterHit`(HitComponent Extend), AttackComponent Extend
- 기능별 하위 폴더 허용: `Health/ Movement/ Combat/ Spawn/ Interaction/`
  - 단, 기준은 **"무슨 기능이냐"**. "누가 쓰나(Player/Enemy)"로 나누는 순간 실패.

## 안 들어가는 것
- ❌ UI/사운드/이펙트 호출이 섞인 것 → 그건 `06_View` 또는 `02_Connectors`
- ❌ 특정 엔티티 GUID/경로에 의존하는 것 → 그건 모듈이 아님
- ❌ 다른 모듈의 구체 메서드를 직접 부르는 것

## 규칙
1. 모듈은 **자신과 자신의 Property/데이터만** 안다. 외부엔 `SendEvent`로만 알린다.
2. 밸런싱 수치는 코드에 박지 않고 `[None]` Property로 → 프로퍼티 에디터에서 인스턴스별 편집.
3. 권위 상태는 `[Sync]` + `[server]`. 서버만 값을 바꾼다.
4. 입장 테스트: **"이걸 떼서 다른 월드에 붙여도 깨지지 않는가?"** — 아니면 여기 못 들어옴.

## 네이밍
`기능 + Component` (PascalCase) — `HealthComponent`, `MonsterStatComponent`
