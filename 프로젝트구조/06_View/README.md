# 06_View — 클라이언트 표현 (뷰)

**시뮬레이션 값을 읽어서 보여주기만 하는 Component.** 전부 `[client only]` 세계입니다.
서버 권위 값은 절대 여기서 바꾸지 않습니다 (동기화 방향은 서버→클라 단방향).

## 여기 들어가는 것
- `OnSyncProperty`로 반응하는 뷰: `CombatViewComponent`, `HealthBarComponent`
- 재사용 UI 위젯 Component: 버튼 래퍼, 게이지, 토스트
- 이펙트/사운드 재생 래퍼 (EffectService/SoundService 호출부)

## 안 들어가는 것
- ❌ 데미지 계산, 상태 판정 등 권위 로직 → `01_Modules` (`[server]`)
- ❌ UI 화면 자체의 조립 → `07_Models` (UI Model) + Hierarchy의 ui 그룹

## 규칙
1. 뷰의 유일한 입력은 `[Sync]` Property(`OnSyncProperty`)와 이벤트. **읽기만** 한다.
2. UI Entity는 Localized Entity(클라 전용) — 서버 함수를 직접 못 부름. World Entity 경유.
3. 입력/내 캐릭터 처리엔 LocalPlayer 가드 필수:
   `if self.Entity ~= _UserService.LocalPlayer then return end`
4. 유저에게 보이는 텍스트는 코드에 박지 않는다 → `08_Data`의 LocaleDataSet 키로.
5. 특정 유저에게만 응답할 땐 `targetUserId` 사용 (전체 브로드캐스트 금지).

## 네이밍
`대상 + ViewComponent` — `CombatViewComponent`
UI 위젯은 `기능 + Component` — `HealthBarComponent`, `ToastComponent`
