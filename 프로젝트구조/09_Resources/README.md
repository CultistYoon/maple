# 09_Resources — 시각·청각 리소스

**RUID로 참조되는 에셋 엔트리.** 컴포넌트가 아니라, 컴포넌트의 Property에
RUID 값으로 꽂히는 것들입니다. (스프라이트 하나하나가 값으로 들어가는 그 대상)

## 여기 들어가는 것 (하위 폴더 예시)
```
Sprites/         Import한 이미지, Atlas 언패킹 결과
Atlas/           AtlasBlueprint (2048×2048, 최대 256조각)
Materials/       Material (셰이더 + 파라미터: Outline, ColorEffect...)
Animations/      AnimationClip (스프라이트 시퀀스 + Offset/Delay)
Skeletons/       Spine 리소스 (.png + .atlas + .skel)
Sounds/          오디오 클립
Text/            TextStyleSheet, TextSpriteSet (리치 텍스트용)
Tiles/           RectTile (64×64 기준)
```

## 규칙
1. 리소스는 **한 번 만들고 RUID로 어디서든 재사용.** 같은 Material/Clip을 엔티티마다 복제하지 않는다.
2. 어느 스프라이트를 쓸지는 코드가 아니라 **프로퍼티 값**(에디터에서 RUID 지정)으로.
   - 코드에 RUID를 하드코딩해야 하면 → `[None] string XxxRUID` Property로 주입받거나 `08_Data`로.
3. 언어별로 다른 이미지가 필요하면 RUID를 LocaleDataSet에 (리소스도 로컬라이징 대상).
4. AnimationClip의 Offset은 엔티티 원점 정렬 기준 — 부품 교체 가능성을 위해 통일.
5. 셰이더는 불변, 파라미터화는 Material이 담당 → 변형은 Material을 새로 만들어서.

## 네이밍
`대상 + 종류` — `Slime_Idle_Clip`, `Outline_Red_Material`, `UI_TextStyleSheet`
언더스코어로 대상_상태_종류 구분을 권장 (검색 편의)
