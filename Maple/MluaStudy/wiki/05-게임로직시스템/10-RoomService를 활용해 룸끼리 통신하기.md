# RoomService를 활용해 룸끼리 통신하기

<!-- 출처: reference/TaskWiki.md · 문서 #100 -->


학습 과정 소개
RoomService를 활용해 하나의 월드 인스턴스 안에 있는 정적 룸과 인스턴스 룸끼리 통신을 할 수 있습니다. 이 가이드는 예제 위주로 진행되며, 기본 개념은 WorldInstanceService와 동일합니다.
월드 인스턴스, 월드 인스턴스 통신, 인스턴스 맵 만들기 가이드를 먼저 학습하기를 권장합니다.

RoomService로 통신
정적 룸과 인스턴스 룸은 직접적으로 통신을 할 수 없기에 서로 이벤트나 데이터를 공유하기 위해선 RoomService의 함수를 사용해야 합니다. RoomService는 인스턴스 룸을 생성하고, 유저를 이동시킬 수 있습니다. 더불어 같은 공유 메모리를 활용해 같은 월드 인스턴스 내의 룸끼리 상태를 공유하는 것도 가능합니다. 공유 메모리를 사용할 때는 GetSharedMemory() 함수를 활용해 새로 생성하거나, 얻어올 수 있습니다. 공유 메모리를 삭제할 때는 DeleteSharedMemoryAndWait() 또는 DeleteSharedMemoryAsync() 함수를 사용합니다.

정적 룸과 인스턴스 룸의 통신
정적 룸에서 인스턴스 룸 상태를 실시간으로 확인하는 예제를 만들어 봅시다. 8초마다 인스턴스 룸의 상태를 게임 중과 대기 중으로 바꾸어 봅시다. 바뀌는 인스턴스 룸의 상태를 조회해 정적 룸과 공유해 정적 룸에서 인스턴스 룸의 상태를 확인할 수 있습니다. 이 예제는 2개의 Logic과 Event Type을 사용합니다.

Example

사전 준비
두 개의 맵이 필요합니다. 하나는 정적 맵으로 사용하고, 다른 하나는 인스턴스 맵으로 사용합니다.

map01: Static Map

map02: Instance Map

Tip.
MapComponent의 InstanceMap를 활용해 인스턴스 맵으로 지정할 수 있습니다.
01

[UI] - DefaultGroup에 [버튼] UI 2개를 추가하고 각각 Btn_Enter, Txt_RoomState로 이름을 변경합니다.

Btn_Enter
Btn_Enter

Txt_RoomState
Txt_RoomState

룸 상태 표시
Workspace - MyDesk의 콘텍스트 메뉴에서 Create Scripts - Create Logic을 선택해 새로운 StaticRoomLogic을 만듭니다.

새로운 ButtonEnter 프로퍼티를 추가하고, 반환 타입을 Entity로 변경합니다. Btn_Enter을 연결합니다.

Property:
[None]
Entity ButtonEnter = /ui/DefaultGroup/Btn_Enter
정적 룸에서만 인스턴스 룸으로 갈 수 있는 버튼이 보이게 아래와 같이 작성합니다.

Method:
[client only]
void OnBeginPlay()
{
    -- 정적 룸에서만 입장 버튼 엔티티를 활성화합니다.
    if _RoomService:IsInstanceRoom() == true then
    	self.ButtonEnter.Enable = false
    else
    	self.ButtonEnter.Enable = true
    end
}
Workspace - MyDesk의 콘텍스트 메뉴에서 Create Scripts - Create Logic을 선택해 새로운 InstanceRoomLogic을 만듭니다.

아래와 같이 프로퍼티 2개를 추가합니다.

Property:
[Sync]
boolean IsPlaying = false
[None]
Entity TextRoomState = /ui/DefaultGroup/Txt_RoomState
InstanceRoomLogic에 OnBeginPlay 함수를 추가합니다. 인스턴스 룸의 상태를 보여주는 버튼만 보일 수 있게 아래와 같이 작성합니다.

Method:
[client only]
void OnBeginPlay ()
{
    -- 인스턴스 룸에서만 상태 엔티티를 활성화 합니다.
    if _RoomService:IsInstanceRoom() == true then
    	self.TextRoomState.Enable = true
    else
    	self.TextRoomState.Enable = false
    end
}
인스턴스 룸 상태 표시
InstanceRoomLogic의 IsPlaying 프로퍼티 값에 따라 버튼의 내용이 바뀔 수 있도록 만들어 봅시다.
정적 룸과 인스턴스 룸에서 로직은 별도로 실행되므로 인스턴스 룸의 변경된 IsPlaying 값을 정적 룸에 전달해야 합니다. 아래 그림과 같이 IsPlaying 값을 전달할 수 있도록 UI를 변경하는 코드를 작성해 봅시다.
01

StaticRoomLogic에 OnUpdate를 추가합니다.

[client only]
void OnUpdate(number delta)
{
    -- 정적 룸에서만 실행합니다.
    if _RoomService:IsInstanceRoom() == true then
    	return
    end

    -- 인스턴스 룸의 상태를 확인하고 버튼 상태를 갱신합니다.
    local isPlaying = _InstanceRoomLogic.IsPlaying
    self:UpdateButton(isPlaying)
}
새로운 UpdateButton 함수를 추가하고, boolean 타입의 isPlaying 매개 변수를 추가합니다. isPlaying 상태에 따라 버튼에 표시되는 문구가 바뀔 수 있도록 아래와 같이 작성합니다.

[client]
void UpdateButton(boolean isPlaying)
{
    if isPlaying == true then
        local text = "입장 불가 <color=red>(게임 중)</color>"
        self.ButtonEnter.TextComponent.Text = text
        self.ButtonEnter.ButtonComponent.Enable = false
    else
        local text = "입장 <color=lime>(대기 중)</color>"
        self.ButtonEnter.TextComponent.Text = text
        self.ButtonEnter.ButtonComponent.Enable = true
    end
}
InstanceRoomLogic에 OnUpdate 함수를 추가합니다.

[client only]
void OnUpdate(number delta)
{
    -- 인스턴스 룸에서만 실행합니다.
    if _RoomService:IsInstanceRoom() == false then
    	return
    end

    -- 룸 상태를 확인하고 텍스트를 갱신합니다.
    self:UpdateText(self.IsPlaying)
}
InstanceRoomLogic에 UpdateText 함수를 추가합니다. boolean 타입의 isPlaying 매개 변수를 추가합니다.

[client only]
void UpdateText(boolean isPlaying)
{
    if isPlaying == true then
    	local text = "<color=red>게임 중</color>"
    	self.TextRoomState.TextComponent.Text = text
    else
    	local text = "<color=lime>대기 중</color>"
    	self.TextRoomState.TextComponent.Text = text
    end
}
인스턴스 룸 입장
입장 버튼을 누른 플레이어가 인스턴스 룸에 입장할 수 있게 아래와 같이 작성합니다.

StaticRoomLogic에 새로운 EnterInstanceRoom을 추가합니다. Add Parameter를 누른 뒤, string 타입의 userId 매개 변수를 추가합니다.
RoomService를 활용해 인스턴스 룸의 key를 가져오고, 유저를 해당 인스턴스 룸으로 보낼 수 있게 아래와 같이 작성합니다.

[server]
void EnterInstanceRoom(string userId)
{
    local roomKey = "ExampleRoom"
    local mapName = "map02"

    _RoomService:GetOrCreateInstanceRoom(roomKey)
    _RoomService:MoveUserToInstanceRoom(roomKey, userId, mapName)
}
Event Handler에 ButtonClickEvent를 추가합니다. entity로 변경하고, Btn_Enter를 연결합니다.
아래와 같이 정적 룸에서 EnterInstanceRoom 함수가 실행되도록 작성합니다.

Event Handler:
[entity: Btn_Enter(/ui/DefaultGroup/Btn_Enter)
HandleButtonClickEvent(ButtonClickEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: ButtonComponent
    -- Space: Client
    ---------------------------------------------------------

    -- Parameters
    local Entity = event.Entity
    ---------------------------------------------------------

    -- 정적 룸에서만 실행합니다.
    if _RoomService:IsInstanceRoom() == true then
    	return
    end

    local me = _UserService.LocalPlayer
    self:EnterInstanceRoom(me.Name)
}
인스턴스 룸 상태를 정적 룸에 공유
새로운 이벤트를 생성하고, 그 이벤트를 사용해 인스턴스 룸의 상태를 정적 룸에 공유하게 만들어 봅시다.

Workspace - MyDesk의 콘텍스트 메뉴에서 Create Scripts - Create Event를 선택해 새로운 RoomStateChangedEvent를 생성합니다.

boolean 타입의 IsPlaying 프로퍼티를 추가합니다.

Property:
boolean IsPlaying = false
InstanceRoomLogic을 열고, 이벤트 핸들러에 RoomBeginEvent를 추가합니다.
서버에서 8초에 한 번씩 인스턴스 룸의 IsPlaying 상태를 변경하도록 작성합니다.
IsPlaying 상태를 정적 룸으로 전송하기 위해 RoomService:RequestSendEventToRoomAndWait() 함수를 사용합니다.

Event Hanlder:
[service: RoomService]
HandleRoomBeginEvent(RoomBeginEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: RoomService
    -- Space: Server
    ---------------------------------------------------------

    -- Parameters
    ---------------------------------------------------------

    -- 인스턴스 룸이 생성될 때 최초 한 번 수행하기 위해 RoomBeginEvent를 이용합니다.

    -- 인스턴스 룸에서만 실행합니다.
    if _RoomService:IsInstanceRoom() == false then
        return
    end

    -- 서버는 8초에 한 번씩 플레이 상태를 바꿔줍니다.
    local timerFunc = function()
        self.IsPlaying = not self.IsPlaying

        -- 이벤트를 사용해 인스턴스 룸에서 정적 룸으로 IsPlaying 값을 전송합니다.
        local evt = RoomStateChangedEvent()
        evt.IsPlaying = self.IsPlaying
        _RoomService:RequestSendEventToRoomAndWait(evt, _RoomService.StaticRoomKey)
    end

    _TimerService:SetTimerRepeat(timerFunc, 8)
}
InstanceRoomLogic에 RoomStateChangedEvent를 추가합니다. [self]를 눌러 [service]로 변경한 뒤 RoomService를 연결합니다.
정적 룸이 수신한 IsPlaying 값을 저장할 수 있도록 아래와 같이 작성합니다.

[service: RoomService]
HandleRoomStateChangedEvent(RoomStateChangedEvent event)
{
    -- Parameters
    local IsPlaying = event.IsPlaying
    ---------------------------------------------------------

    -- 이벤트는 서버에서 발생합니다.
    -- 정적 룸에서만 실행합니다!
    if _RoomService:IsInstanceRoom() == true then
    	return
    end

    -- 정적 룸은 인스턴스 룸으로부터 수신한 IsPlaying 값을 저장합니다.
    self.IsPlaying = IsPlaying
}
RoomEndEvent를 추가합니다.
인스턴스 룸이 파괴될 때 IsPlaying 상태를 초기화할 수 있도록 아래와 같이 작성합니다.

[service: RoomService]
HandleRoomEndEvent(RoomEndEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: RoomService
    -- Space: Server
    ---------------------------------------------------------

    -- Parameters
    ---------------------------------------------------------

    -- 인스턴스 룸에서만 실행합니다.
    if _RoomService:IsInstanceRoom() == false then
    	return
    end

    -- 인스턴스 룸이 파괴될 때 상태를 초기화합니다.
    self.IsPlaying = false
    local evt = RoomStateChangedEvent()
    evt.IsPlaying = self.IsPlaying
    _RoomService:RequestSendEventToRoomAndWait(evt, _RoomService.StaticRoomKey)
}
공유 메모리 활용
위에서 만든 예제 월드에서 새로운 UI를 추가하고, 해당 인스턴스 룸에 입장했을 때 공유 메모리 내용이 나타나도록 만들어 봅시다.
4

텍스트 UI를 DefaultGroup에 추가하고 Txt_RoomTitle 이름으로 설정합니다.
3

InstanceRoomLogic에 새로운 Entity 타입의 TextRoomTitle 프로퍼티를 추가합니다. Txt_RoomTitle UI를 연결합니다.

Property:
[None]
Entity TextRoomTitle = /ui/DefaultGroup/Txt_RoomTitle
인스턴스 룸에 입장하면 Txt_RoomTitle UI가 활성화 되도록 InstanceRoomLogic의 OnBeginPlay에 아래와 같이 작성합니다.

Method:
[client only]
void OnBeginPlay()
{
    if _RoomService:IsInstanceRoom () == true then
        self.TextRoomState.Enable = true
        self.TextRoomTitle.Enable = true
    else
        self.TextRoomState.Enable = false
        self.TextRoomTitle.Enable = false
    end    
}
InstanceRoomLogic에 string 타입의 Title 프로퍼티를 추가합니다.

Property:
[Sync]
string Title = ""
룸 이름이 나타날 수 있게 InstanceRoomLogic의 UpdateText 함수 가장 마지막 줄에 아래 코드를 추가합니다.

self.TextRoomTitle.TextComponent.Text = self.Title
인스턴스 룸을 생성하기 전, 공유 메모리에 룸 이름을 저장해야 합니다. 이를 위해 StaticRoomLogic의 EnterInstanceRoom 함수에서 local mapName = "map02" 밑에 아래 내용을 추가합니다.

local roomTitleVarName = "roomTitle"
local roomTitle = "Hello, MapleStory Worlds!"

-- 공유 메모리를 얻어옵니다.
local code, mem = _RoomService:GetSharedMemory(roomKey)

if code ~= SharedMemoryResultCode.OK then
	error ("Failed to GetSharedMemory.")
	return
end

-- 'roomTitle'이라는 이름의 변수에 룸 제목을 저장합니다.
local setResult = mem:SetVariableAndWait(roomTitleVarName, roomTitle)

if setResult.Code ~= SharedMemoryResultCode.OK then
	error ("Failed to SetSharedVariableAndWait.")
	return
end
InstanceRoomLogic에서 새로운 ReadTitleFromSharedMemory 함수를 추가합니다.

[server only]
void ReadTitleFromSharedMemory()
{
    local memKey = "ExampleRoom"
    local varName = "roomTitle"

    local code, mem = _RoomService:GetSharedMemory(memKey)

    if code ~= SharedMemoryResultCode.OK then
    	error ("Failed to GetSharedMemory.")
    	return
    end

    local getResult = mem:GetVariableAndWait(varName)

    if getResult.Code ~= SharedMemoryResultCode.OK then
    	error ("Failed to GetSharedVariableAndWait.")
    	return
    end

    self.Title = getResult.Info.Value

    -- 더 이상 사용하지 않는 공유 메모리는 삭제합니다.
    -- 공유 메모리를 삭제하면 내부의 모든 변수도 함께 삭제됩니다.
    _RoomService:DeleteSharedMemoryAndWait(memKey)
}
공유 메모리에서 제목을 읽어오도록 HandleRoomBeginEvent의 마지막 부분에 아래 내용을 추가합니다.

-- 공유 메모리에서 제목을 읽어옵니다.
self:ReadTitleFromSharedMemory()
RoomSharedMemory 제한 사항
RoomSharedMemory를 사용할 때는 아래의 제한 사항을 염두에 두고 사용해야 합니다.

작명 규칙
RoomSharedMemory와 공유 변수 이름은 아래 문자로만 작명할 수 있습니다. 최소 1글자 이상의 이름이어야 하며, 최대 100글자 이름일 수 있습니다.

알파벳 대,소문자

숫자

공백

_, -

수량 및 용량 제한
한 월드 당 생성 가능한 RoomSharedMemory는 최대 100개입니다.

하나의 공유 변수에 저장할 수 있는 최댓값은 80,000 bytes입니다.

공유 메모리 하나의 총 용량은 80MiB를 넘을 수 없습니다.

전송할 이벤트 프로퍼티의 총 용량은 80,000 byte를 넘을 수 없습니다.충돌
엔티티의 충돌
충돌 그룹 만들기
물리 사용하기
엔티티에 물리 적용하기
다양한 물리 joint 활용하기
Physics Owner 지정하기
