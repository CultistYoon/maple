# RectTileMap에서 캐릭터 이동 제어

<!-- 출처: reference/TaskWiki.md · 문서 #63 -->


학습 과정 소개
RectTileMap에서는 KinematicbodyComponent로 캐릭터의 이동을 제어합니다. 크리에이터는 KinematicbodyComponent를 통해 캐릭터를 2차원 평면에서 자유롭게 움직이고 점프하게 할 수 있습니다. 또한 그림자를 그릴 수도 있습니다.
이번 시간에는 KinematicbodyComponent에 대해 알아보고 간단한 예제를 통해 활용법을 살펴봅시다.

참고 API Reference
KinematicbodyComponent

더 알아보기
RectTileMap에 대한 내용은 RectTileMap의 활용을 참고하세요.

KinematicbodyComponent 소개
Workspace - DefaultPlayer - Property 창에서 KinematicbodyComponent의 프로퍼티를 살펴봅시다.

프로퍼티	설명
Acceleration	더 이상 사용하지 않습니다. SpeedFactor를 사용해주세요.
ApplyClimbableRotation	True인 경우 회전하거나 기울어진 사다리를 탄 캐릭터는 사다리의 모습을 따릅니다. False인 경우 캐릭터는 사다리의 기울기, 회전에 영향을 받지 않습니다.
EnableJump	True면 점프 기능을 사용합니다.
EnableShadow	True면 그림자를 사용합니다.
ShadowColor	그림자의 색상입니다.
ShadowOffset	그림자의 위치입니다.
ShadowSize	그림자의 크기입니다.
ShadowScalingRatio	그림자 크기 변화율입니다. Entity의 점프 높이에 따라 크기가 변화합니다.
EnableTileCollision	True면 사각형 타일맵과 충돌합니다.
JumpDrag	점프 속력 감소량을 조절합니다. 값이 클수록 지면에 더 빨리 떨어집니다.
JumpSpeed	점프할 때 튀어 오르는 속력을 조절합니다. 값이 클수록 더 높이 점프합니다.
SpeedFactor	이동할 때 X축, Y축 속력에 곱해지는 가중치입니다. 값이 클수록 이동 속력이 빨라집니다.
Enable	True면 KinematicbodyComponent를 활성화합니다.
KinematicbodyComponent 활용
속도 증가 타일 만들기
밟으면 속도가 증가하는 타일을 만들어 봅시다.


타일맵 모드를 RectTile로 설정합니다.
recttile


타일 셋 팔레트 좌측 상단의 [+] 버튼을 누른 뒤, Create TileSet From Template - BnB 타일 셋을 선택합니다.
tileset


타일 셋의 이름을 BnB TileSet으로 설정합니다.
BnB


타일 셋 팔레트 우측 상단의 편집 버튼을 눌러 타일 속성 편집 모드로 들어갑니다.
tileedit


편집 대상에서 이동 가능 여부를 체크한 뒤, 캐릭터가 이동하지 못하게 할 타일을 선택합니다. 초록색 화살표 아이콘은 이동 가능 타일, 빨간색 화살표 아이콘은 이동 불가 타일임을 나타냅니다.
dontmove
편집이 끝나면 편집 모드를 해제합니다.


Map Layer에서 Layer1을 선택한 뒤 맵을 만들어줍니다.
map1


Map Layer에서 addlayer 버튼을 눌러 Layer2를 만든 뒤 집, 나무 등을 배치하여 추가로 맵을 꾸며줍니다.
map2


Map Layer에서 addlayer 버튼을 눌러 Layer3을 추가합니다.
layer


. 타일 셋 팔레트 좌측 상단의 [+] 버튼을 누른 뒤, Create Empty TileSet을 선택합니다. Buff TileSet이라는 이름으로 새 타일 셋을 추가합니다.


타일 셋 팔레트 좌측 하단의 add 타일 추가 버튼을 누른 뒤 Add ResourceStorage Image를 선택합니다.
addtile


Resource Picker - MSW 리소스에서 아래의 RUID로 검색된 스프라이트를 클릭해 타일 셋에 추가합니다.
Buff : 02652c247d9d40518702255bed1376c8
Trap : 510cf1b467634a3db7624041432c3de5
buff trap


타일 속성 편집 모드로 들어간 뒤 이름을 더블클릭해 각각 Buff, Trap으로 설정합니다.
rename
편집이 끝나면 편집 모드를 해제합니다.


Map Layer에서 Layer3을 선택한 상태로 맵에 Buff 타일을 배치합니다.


MyDesk 아래에 새 스크립트 컴포넌트 CheckSpeedBuffTile를 만든 뒤, DefaultPlayer에 추가합니다.


아래와 같이 CheckSpeedBuffTile를 작성합니다.

Method:
[server]
void IncreaseSpeedFactor()
{
    local kb = self.Entity.KinematicbodyComponent
    local oldSpeedFactor = kb.SpeedFactor
    local newSpeedFactor = Vector2(oldSpeedFactor.x + 1, oldSpeedFactor.y + 1)

    kb.SpeedFactor = newSpeedFactor
}

Event Handler :
[client only]
HandleRectTileEnterEvent(RectTileEnterEvent event)
{
    -- Parameters
    local Kinematicbody = event.Kinematicbody
    local TileInfo = event.TileInfo
    local TileMap = event.TileMap
    local TilePosition = event.TilePosition
    --------------------------------------------------------  

    -- 'Buff' 타일을 밟으면 SpeedFactor를 증가시킵니다.
    if TileInfo.Name == "Buff" and Kinematicbody:IsOnGround() then
        self:IncreaseSpeedFactor()
    end
}


play 시작 버튼을 눌러 버프 타일을 밟으면 속력이 조금씩 증가하는 것을 확인해봅시다.
speedup

장애물 타일 피하기
점프로만 넘어갈 수 있는 장애물을 만들고, 장애물을 밟으면 캐릭터가 죽도록 설정해 봅시다.

맵에 Trap 타일을 배치합니다.


MyDesk 아래에 새 스크립트 컴포넌트 CheckTrapTile를 만든 뒤, DefaultPlayer에 추가합니다.


아래와 같이 CheckTrapTile을 작성합니다.

Property:
[None]
string CurrentTileName = ""

Method:
[client only]
void OnUpdate(number delta)
{
    local kb = self.Entity.KinematicbodyComponent

    -- 지면에 있을 때만 타일과 충돌합니다.
    kb.EnableTileCollision = kb:IsOnGround()

    -- 'Trap' 타일을 밟으면 죽습니다. 신중하게 점프하세요!
    if self.CurrentTileName == "Trap" and kb:IsOnGround() then
        self.Entity.PlayerComponent:ProcessDead()
    end
}

Event Handler:
[client only]
HandleRectTileEnterEvent(RectTileEnterEvent event)
{
    -- Parameters
    local Kinematicbody = event.Kinematicbody
    local TileInfo = event.TileInfo
    local TileMap = event.TileMap
    local TilePosition = event.TilePosition
    --------------------------------------------------------

    self.CurrentTileName = TileInfo.Name
}


play 시작 버튼을 눌러 Trap을 뛰어넘을 수 있고, 실수로 밟게 되면 캐릭터가 죽는지 확인해봅시다.
