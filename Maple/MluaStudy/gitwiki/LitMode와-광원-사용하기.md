# LitMode와 광원 사용하기

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「LitMode와 광원 사용하기」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 06 연출 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
월드에 광원을 적용할 수 있는 방법을 알아봅시다.

LitMode 활성화
UseLitDefaultMaterial을 활성화하면 모든 엔티티는 LitMode가 Lit인 상태로 간주됩니다. 이에 따라 엔티티들이 다른 광원으로부터 영향을 받아 표면의 색상과 밝기가 달라지게 됩니다. 그러나 LitMode를 별도로 설정할 수 있는 엔티티의 경우 따로 지정된 LitMode의 값을 따르게 됩니다. WorldConfig를 참고하세요.

[object Object]

Scene, Play 광원 활성화
Light 버튼을 활성해 Scene에서 생성한 광원이 적용된 모습을 확인할 수 있습니다. 이때 맵에 최소 1개 이상의 광원이 배치되어 있어야 정상적으로 광원의 모습이 보입니다.
LightButton

광원 적용하기
광원을 월드에 적용하는 방법은 크게 4가지로 구분됩니다.

LightComponent를 엔티티에 추가

Material에서 LitMode를 설정하고 엔티티에 연결

LitMode 프로퍼티를 가진 컴포넌트를 엔티티에 추가

LitMode를 설정할 수 있는 서비스의 메소드 호출

LightComponent
엔티티에 LightComponent를 추가하고, 광원을 생성할 수 있습니다. TransformComponent와 함께 사용하기를 권장합니다.

광원 종류
LightComponent에서 사용할 수 있는 광원은 4가지입니다. 크리에이터의 필요에 따라 사용할 수 있습니다.

Spot
원형으로 나타나는 광원입니다. 프로퍼티 값을 조정해 원형의 모양을 조정할 수 있습니다.
spot

Freeform
크리에이터가 광원을 원하는 모양으로 만들 수 있습니다.
freeform

Global
화면 전체에 적용되는 광원입니다. SortingLayer는 여러 개의 Global Light로부터 동시에 광원 효과를 받을 수 없습니다.
global

Sprite
크리에이터가 지정한 스프라이트의 RGBA 색상 정보를 조합해 광원의 형태와 색이 나타납니다.
sprite

주요 프로퍼티
빛의 혼합
OverlapOperation은 여러 개의 광원이 겹칠 경우 어떤 방식으로 빛을 계산해 보여줄 것인지를 결정하는 프로퍼티입니다. 프로퍼티의 값은 두 가지로 Additive, AlphaBlend가 있습니다.

Additive: 빛이 겹쳐질수록, 겹치는 부분이 밝은 빛으로 나타납니다.
Additive

AlphaBlend: LightOrder 값이 큰 광원의 색이 겹치는 부분에 나타납니다.
[object Object]

광원 적용
SortingLayer에 광원을 적용 여부를 TargetAllSortingLayers, TargetSortingLayers로 설정할 수 있습니다.

TargetAllSortingLayers: 모든 SortingLayer에 광원이 적용됩니다. 이 프로퍼티를 비활성화하면 TargetSortingLayers를 설정할 수 있습니다.

TargetSortingLayers: 광원이 적용될 SortingLayer를 크리에이터가 지정할 수 있습니다. SortingLayer마다 별도의 광원 텍스처를 생성하고 렌더링하게 됩니다. 이는 모바일 환경에서 성능 저하를 유발할 수 있으므로 유의해야 합니다.
[object Object]

LitMode
LitMode로 셰이더 렌더링 방식을 선택할 수 있습니다. 이 종류에 따라 월드에서 어떻게 렌더링 될지 결정합니다.

Default: WorldConfig의 UseLitDefaultMaterial 설정에 따라 셰이더가 결정됩니다.

Lit: 빛이 있는 셰이더로 광원의 위치, 색상, 강도에 따라 엔티티의 표면 색상과 밝기가 달라집니다.
lit

Unlit: 빛이 없는 셰이더로 광원의 영향을 받지 않고, 엔티티의 설정 값대로 보여집니다. 연산이 가벼워 성능 부담이 적습니다.
unlit

주의
특정 엔티티와 컴포넌트는 항상 Unlit 셰이더로 렌더링됩니다. LitMode 값에 영향을 받지 않습니다.

Hierarchy - ui 하위에 있는 UI 엔티티

TextComponent

YoutubePlayerComponent

WebViewComponent

Material
Material을 사용하는 엔티티는 Material의 LitMode를 설정할 수 있습니다.
[object Object]

Components
아래 목록의 컴포넌트들은 LitMode를 개별적으로 설정할 수 있습니다.

AreaComponent

BasicParticleComponent

SpriteParticleComponent

DamageSkinSettingComponent

Sevices
아래 목록의 서비스들은 Play() 메소드 사용 시 LitMode를 설정할 수 있습니다.

DamageSkinService

EffectService

ParticleService이펙트
스킬 이펙트를 뿌려보자!
