# 프로젝트 구조 (전체 지도)

> 이 폴더 구조는 [코드 규범](../코드%20규범.md)의 "모듈 70% + 접착제 30% / 코드·데이터 분리 / 시뮬레이션·뷰 분리"를
> MSW Workspace(MyDesk)의 **엔트리 종류**에 그대로 대응시킨 것입니다.
> 폴더는 엔티티 종류(Player/Enemy)가 아니라 **아키텍처 역할**로 나눕니다.
> 정체성(주황버섯 vs 뿔버섯)은 폴더가 아니라 **07_Models의 조립 + 프로퍼티 값**에서 결정됩니다.

```
01_Modules/      재사용 로직 Component (70%)     — Create Scripts > Component
02_Connectors/   접착제 Component (30%)          — Create Scripts > Component
03_Events/       커스텀 EventType                — Create Scripts > EventType
04_AI/           BTNodeType + 행동 트리          — Create Scripts > BTNodeType
05_States/       StateType + StateSet            — Create Scripts > StateType / Create StateSet
06_View/         클라 표현 Component + UI 위젯   — Create Scripts > Component
07_Models/       ★조립품(Model)                  — Create Model
08_Data/         DataSet 계열                    — Create DataSet / LocaleDataSet / TileDataSet
09_Resources/    시각·청각 리소스                — Create Material / AtlasBlueprint / Import
```

## 3초 분류법 — "이 엔트리는 어디에?"

| 질문 | 답 |
|---|---|
| 로직이고, 다른 월드에 복붙해도 도는가? | `01_Modules` |
| 이벤트 받아서 뷰/사운드를 이어붙이기만 하는가? | `02_Connectors` |
| `...Event`로 끝나는가? | `03_Events` |
| `...BTNode`로 끝나는가? | `04_AI` |
| `...StateType`이거나 StateSet인가? | `05_States` |
| `[client only]`이고 보여주기만 하는가? | `06_View` |
| 컴포넌트 묶음 + 기본값을 찍어내는 도장인가? | `07_Models` |
| 표/수치/텍스트인가? | `08_Data` |
| 이미지/머티리얼/사운드/애니메이션인가? | `09_Resources` |

## 검증 기준 (구조가 살아있는지 확인)

새 몬스터 "슬라임" 추가가 이걸로 끝나면 성공:
1. `07_Models`에 Model 생성 → `01_Modules`/`04_AI`/`05_States` 부품 부착
2. 프로퍼티 에디터에서 수치 입력 (+ 필요하면 `08_Data`에 행 추가)
3. **새 스크립트 0줄**

새 몬스터마다 스크립트를 복사하고 있다면 → 공통 부분을 `01_Modules`로 다시 빼야 합니다.
