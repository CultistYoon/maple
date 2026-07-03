# 08_Data — 데이터 (코드에서 분리된 수치·텍스트·표)

**코드는 로직, 데이터는 여기.** 밸런싱을 바꿀 때 스크립트를 열지 않게 만드는 곳입니다.

## 여기 들어가는 것
| 엔트리 | 용도 | 읽는 법 |
|---|---|---|
| **DataSet** | 게임 테이블 (몬스터 표, 드랍 표, 스킬 수치) | `_DataService:GetTable()` (server only) |
| **ServerOnly DataSet** | 클라에 노출 금지 데이터 (공식, 쿠폰) | Properties > ServerOnly ✓ |
| **LocaleDataSet** | 유저에게 보이는 모든 텍스트 | `_LocalizationService:GetText(key)` |
| **TileDataSet** | 타일 이름 → 스프라이트 매핑 | RectTileMapComponent |

## 안 들어가는 것
- ❌ 엔티티 1개에만 붙는 수치 → 그건 해당 Component의 `[None]` Property (프로퍼티 에디터)
- ❌ 유저별 저장 데이터 → DataStorage는 엔트리가 아니라 DB 서비스 (코드에서 접근)

## 규칙
1. UI/NPC 텍스트를 코드에 직접 쓰는 순간 규범 위반 → LocaleDataSet 키로.
2. 서버는 번역 결과가 아니라 **키**를 보낸다. 번역은 클라에서 (글로벌 원빌드).
3. 데미지 공식·확률 등 어뷰징 표적은 ServerOnly DataSet으로.
4. DataStorage 사용 시: `GetAndWait` 남발 금지 → `GetAsync` + 콜백,
   에러코드 확인 + 로드 실패 시 initialized 플래그로 차단, 저장은 퇴장/주기 트리거로.
5. DataSet 값은 전부 문자열 — 읽는 쪽에서 형변환.

## 네이밍
`용도 + DataSet` — `MonsterStat_DataSet`, `UI_LocaleDataSet`, `Dialogue_LocaleDataSet`
키는 대문자 스네이크 — `UI_INTERACT_HINT`, `UI_TEXT_NPC_Stan`
