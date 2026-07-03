# 02_Connectors — 접착제 (30%)

**모듈들을 이어붙이기만 하는 Script Component.** 이벤트를 받아 뷰/사운드/다른 모듈을 조율합니다.
이 월드에 하드코딩돼도 되는 유일한 곳 — 대신 **로직은 절대 여기 두지 않습니다.**

## 여기 들어가는 것
- 이벤트 → 뷰 중계: `PlayerHealthConnector` (PlayerDamagedEvent 받아 체력바+사운드+애니 조율)
- 조립 전용 스크립트: `MonsterAIComponent` 같은 "어떤 노드를 꽂을지"만 정하는 것

## 안 들어가는 것
- ❌ 게임 규칙/계산 (데미지 공식, 드랍 확률) → `01_Modules`
- ❌ 이벤트 없이 스스로 동작하는 것 → `01_Modules`

## 규칙
1. 외부 참조는 전부 `[None]` Property로 주입받는다 (GUID 하드코딩 금지).
2. Event Handler 중심으로 작성 — `Handle + 이벤트명`, 중계 엔티티(`[entity: ...]`) 정확히.
3. 참조 사용 전 `isvalid()` 필수 (`~= nil` 금지).
4. 커넥터가 뚱뚱해지면 → 로직이 새고 있다는 신호. `01_Modules`로 추출.

## 네이밍
`대상 + 역할 + Connector` — `PlayerHealthConnector`, `EnemySpawnConnector`
