# 07_Models — 조립품 (Model) ★설계의 완성 지점

**부품(01~06)을 조합하고 프로퍼티 값을 채워 넣은 "도장".** 게임에 등장하는 것들의
정체성은 코드 폴더가 아니라 **여기의 조합 + 값**에서 결정됩니다.

## 여기 들어가는 것
- 캐릭터/몬스터 Model: `Player`, `OrangeMushroom`, `HornMushroom`, `Slime`
- 오브젝트 Model: `Portal`, `TreasureBox`, `SavePoint`
- UI 화면 Model: `InventoryUI`, `ShopUI` (UITransform + 위젯 조합)
- 하위 폴더 자유: `Monsters/ NPCs/ Props/ UI/`

## 규칙
1. **새 개체 = 새 Model + 부품 부착 + 프로퍼티 값. 새 스크립트 0줄이 목표.**
   - 주황버섯: MonsterStat(HP100/이속3) + MonsterHit + `PatternNodeName="ChargeBTNode"`
   - 뿔버섯: 같은 부품, 값만 다름 (HP150/이속2, `"JumpAttackBTNode"`)
2. 변형 만들 때 **Extend vs Duplicate** 구분:
   - Extend = 부모 변경이 자식에 자동 전파 (기본 몬스터 → 변종에 적합)
   - Duplicate = 완전 독립 (전파 안 됨)
3. 배치된 인스턴스는 Model 수정이 자동 반영 안 됨 → 필요 시 Revert.
4. 런타임 생성은 `_SpawnService:SpawnByModelId()` — Model이 곧 스폰 템플릿.
5. Model에 붙일 부품이 없어서 코드를 새로 짜게 된다면 → 부품화 실패 신호,
   공통 로직을 `01_Modules`로 추출부터.

## 네이밍
개체 이름 그대로 (PascalCase) — `OrangeMushroom`, `InventoryUI`
접미사 불필요 (Model임은 위치와 아이콘으로 드러남)
