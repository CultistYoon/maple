# 메이플 아카데미 커리큘럼 (진도 기준)

> 코치는 이 파일을 진도 기준으로 삼되, **Lua/MSW 문법 기초를 먼저 뗀 뒤** 챕터에 매핑한다(SKILL.md §2).
> 각 항목은 wiki/INDEX.md의 문서와 대조해 선행지식을 판단한다.

## 플랫포머 트랙
1. 탐험: 플랫포머 게임 살펴보기 (꾸미기 모드, MapleStory Map "펫산책로")
2. 기본 월드 만들기 (템플릿, WorldConfig 보안·권한, 저장/플레이, 맵 추가·시작맵, 포털, 플랫포머 아키텍처, 허브)
3. 배경 설정 (이미지 변경, ScrollRate, 단색, 그라디언트, BackgroundController)
4. 타일 지형 (타일 개념, 지형 제작, MapleTile, 다중 레이어, RectTile, SideViewRectTile-FallDeathWithRespawn)
5. 스폰 & 발판 (아바타 기본 위치, 스폰 변경·Foothold, 스폰 우선순위)
6. 플레이어 기본 설정 (중력·점프력·점프횟수, 데미지 스킨, 최대체력, 부활시간, 플레이어간 공격)
7. 공격 시스템 (PlayerAttack, 몬스터 MaxHP-Monster)
8. 몬스터 (추가, MyMonsterAttack, MonsterAttack, 부활, MonsterDamageSkinController)
9. 장애물 & 상호작용 (Trap, 힛영역, Spring, JumpMovement 트윈)
10. 이동 구조 (사다리, 밧줄, LadderMovement)
11. 다양한 인터랙션 (아바타 패션샵 템플릿, LadderSwitch, 클라/서버 개념 LadderSwitch_Server·LadderSwitch_Me, Doorhandler, DoorController, Door_Open, TweenLineComponent, BridgeMovement)
12. 물리 (PhysicsRigidbodyComponent, PhysicsColliderComponent, PhysicsSimulatorComponent, 실습)
13. 스폰 심화 (체크포인트 Checkpointhandler·PlayerRevivehandler)
14. 사운드 (배경음악, MyMonsterAttackSound, PlayerAttack 효과음, 체크포인트)
15. 이펙트 & 연출 (EffectService, AvatarEffectComponent, PlayerAttack, MonsterAttack)
16. UI 타이틀 (UI에디터, 버튼, 배경이미지, 타이틀, AI 이미지, Btn_Start, ButtonEffect, Btn_Home·Btn_Close)
17. 게임 설정 & 퍼블리싱 (설명, 썸네일, Release, 플레이테스트, 배포·발표)
18. 패키지-랭킹시스템 (Ranking-Basic, WorldConfig, UI경로, StorageName, Config, 관리자권한, 점수등록, AI 에이전트로 랭킹 붙이기)
19. 외부타일 이미지 연동 (외부 에셋 다운로드, RecTile 외부이미지 적용)

## 로컬/AI 개발 트랙
- **0. AI로 개발하기 – May-I, AI ToolKit** (MSW AI 살펴보기, AI와 월드 만들기, **로컬워크스페이스 설정**, **MCP 서버: Claude Code 설치·연결**, AI 스킬셋 설정, AI 시작, ToolKit 팁·제작)
- **0. VS Code MSW 개발하기** (Local WorkSpace 개념, VS Code 설치, Local WorkSpace 설정, 작업폴더 열기, **mLua 익스텐션 설치**)

## 방치형 트랙
1. 방치형 이해 (메이플 히어로 키우기·밥똥메, 핵심사이클 전투→재화→성장→반복, 기본구조)
2. MSW UI 기본 (UI 살펴보기, 맵생성, 프리셋, UI 연습, HP바, 순서, Anchors&Safe Area, 컴포넌트, Button_TextToggle)
3. 월드 구성 (룸·맵 개념, 정적/인스턴스 맵, 포털 이동, MatchLogic, MapNameDisplay, StartBtn·TitleManager, 최소·최대 매칭)
4. 몬스터 & 아이템·인벤토리 (RPG 픽트라 몬스터, MonsterSpawn 랜덤·수량보충, UserItemDataSet·LiteInventory·Item)
5. 포털 & 몬스터 공격 (MonsterPortalComponent, AutoAttackComponent·MissileComponent, HP바)
6. 재화 & 인벤토리 (UserItemDataSet, Weapon, ItemPickUpComponent, OnClickSlot, 장착, PlayerAttack, 데이터리셋, HP물약, 효과음)
7. 상점 (레퍼런스, 소스 임포트, 상품등록·UI·정보셋팅·구매보상·스킨, Release)
8. 자동 이동 & 토글버튼 (방치형 샘플, 맵생성, 보안우선, 타일수정, 속성값, 몬스터, PlayerAutoComponent, AutoToggleButtonComponent, 키입력제어, PlayerInitializeComponent 카메라)
9. 자동 전투 (몬스터 감지·자동공격, PlayerAttack, 추적 몬스터, 좌우 자동공격·방향전환·전투동작)
10. 몬스터 & 재화 & 인벤토리 (spawn, Drop_Item_Component, Get_Item_Component SetMeso, Inventory_component, 코인출력·드롭·효과음)
11. AI & 패키지로 방치형 (맵·패키지·플레이어Component, AdminLogic, UIEquippedGearPanel, [AI]장비장착·자동공격·자동탐색이동·리스폰·성장루프·오프라인보상·전투토글)
12. 스토리텔링 (대화창 UI·표시숨김, NPCTalk DataSet·상호작용)
13. 카메라 연출 & 엔딩·인트로 (CameraService, "달팽이동산", CameraComponent, StartCamComponent, 출발이펙트)
14. 게임 설정 & 퍼블리싱 (방치형 ch2와 동일)
