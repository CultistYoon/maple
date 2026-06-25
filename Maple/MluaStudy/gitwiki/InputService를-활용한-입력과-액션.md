# InputService를 활용한 입력과 액션

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「InputService를 활용한 입력과 액션」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 05 게임로직시스템 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
모든 게임은 유저의 입력과 입력에 대한 피드백으로 게임이 진행됩니다. 메이플스토리 월드에서는 InputService를 통해 유저의 입력에 대한 액션을 제어할 수 있습니다.
이번 과정에서는 유저의 입력이 발생했을 때의 액션을 추가하는 방법을 알아보겠습니다.

참고 가이드
Event System
Entity Event System

InputService
월드에서 유저가 특정 입력을 하면 InputService는 유저의 입력에 대한 이벤트를 발생시킵니다. 발생한 이벤트를 이벤트 핸들러를 통해 특정 액션을 수행하게 할 수 있습니다.
유저의 입력 이벤트는 클라이언트에서만 발생하기 때문에, 각 이벤트 핸들러도 클라이언트에서만 실행됩니다.
1

이벤트 핸들러 추가
입력에 관한 이벤트 핸들러는 스크립트 컴포넌트에서 추가할 수 있습니다.

스크립트 컴포넌트를 생성한 뒤 임의의 엔티티에 추가합니다.

Event Handler에서 [+] 버튼을 눌러 이벤트 탐색 창을 열고, 핸들러에 추가할 이벤트를 찾아 선택합니다.
3-1

핸들러가 추가되면 이벤트 센더가 InputService로 선택되어 있는지 확인합니다.
4-1

이벤트 종류별 특징
InputService에서 제공하는 유저 입력과 관련된 각 이벤트는 유저의 입력 형태에 따라 발생하는 시점과 횟수가 달라집니다.
5

KeyDownEvent
KeyDownEvent는 키를 눌렀을 때 발생하는 이벤트입니다. KeyDownEvent가 발생하면 HandleKeyDownEvent가 실행됩니다. KeyDownEvent가 핸들러의 매개 변수로 전송되며, 이벤트에는 유저가 입력한 키가 enum으로 넘어오게 됩니다.
다음은 T 키를 눌렀을 때 로그를 출력하는 예제입니다.

Event Handler:
[service: InputService]
HandleKeyDownEvent(KeyDownEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: InputService
    -- Space: Client
    ---------------------------------------------------------
    
    -- Parameters
    local key = event.key
    ---------------------------------------------------------
    
    if key == KeyboardKey.T then
        log("Press T!")
    end
}
8

이벤트 핸들러를 사용하지 않고 InputService의 IsKeyPressed(), IsAnyKeyPressed() 함수를 사용해 Key 입력을 제어할 수도 있습니다.

IsKeyPressed()는 키가 눌린 상태면 true를, 키가 눌리지 않은 상태면 false를 반환합니다.

IsAnyKeyPressed()는 어떤 키라도 눌린 상태면 true를, 아무 키도 눌리지 않았으면 false를 반환합니다.

다음은 두 함수를 이용해 키 입력을 확인하는 예제입니다.

Method:
[client only]
void OnUpdate(number delta)
{
    local enterKeyPressed = _InputService:IsKeyPressed(KeyboardKey.Return)
    local anyKeyPressed = _InputService:IsAnyKeyPressed()

    if enterKeyPressed == true then
        log ("Enter key pressed.")
    end

    if anyKeyPressed == true then
        log ("Any key pressed.")
    end
}
[object Object]

KeyUpEvent
KeyUpEvent는 키보드의 키가 눌려있는 상태에서, 키에서 손을 떼었을 때 1회 발생하는 이벤트입니다. KeyUpEvent가 발생하면 HandleKeyUpEvent가 실행되며 이벤트가 발생할 때 1회 실행됩니다. 핸들러의 매개 변수로 KeyUpEvent가 전송되고 이벤트에는 유저가 입력한 key 값이 KeyboardKey 타입의 enum 값으로 포함되어 있습니다.
다음은 T 키를 눌렀다가 떼었을 때 로그를 출력하는 예제입니다.

[service: InputService]
HandleKeyUpEvent(KeyUpEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: InputService
    -- Space: Client
    ---------------------------------------------------------
    
    -- Parameters
    local key = event.key
    ---------------------------------------------------------
    
    if key == KeyboardKey.T then
        log("Release T!")
    end
}
10

KeyHoldEvent
KeyHoldEvent는 키보드의 키가 눌려있는 동안 프레임마다 발생하며, 이벤트가 발생할 때마다 HandleKeyHoldEvent 역시 매번 실행됩니다. KeyHoldEvent가 핸들러의 매개 변수로 전송되며, 다른 이벤트와 마찬가지로 유저가 입력한 키 정보가 포함되어 들어옵니다.
다음은 키를 누르는 동안 로그를 출력하는 예제입니다.

[service: InputService]
HandleKeyHoldEvent(KeyHoldEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: InputService
    -- Space: Client
    ---------------------------------------------------------
    
    -- Parameters
    local key = event.key
    ---------------------------------------------------------
    
    if key == KeyboardKey.T then
        log("Hold T!")
    end
}
12

KeyReleaseEvent
KeyReleaseEvent는 키보드의 키가 눌려있는 상태에 있다가 키에서 손을 떼었을 때 1회 발생하는 이벤트입니다. 이벤트 발생 시 HandleKeyReleaseEvent도 함께 실행됩니다.
KeyUpEvent와 비슷하지만 키가 한 프레임이라도 Hold 되어 있던 상태에서 Release 상태가 되었을 때 액션을 추가하고 싶다면 HandleKeyReleaseEvent를 사용합니다. KeyReleaseEvent가 핸들러의 매개 변수로 전송되며 유저가 입력한 키 정보가 포함되어 들어옵니다.
다음은 키를 눌렀다가 떼었을 때 로그를 출력하는 예제입니다.

[service: InputService]
HandleKeyReleaseEvent(KeyReleaseEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: InputService
    -- Space: Client
    ---------------------------------------------------------
    
    -- Parameters
    local key = event.key
    ---------------------------------------------------------
    
    if key == KeyboardKey.T then
        log("Release T!")
    end
}
14

ScreenTouchEvent
ScreenTouchEvent는 화면을 클릭하거나 터치했을 때 1회 발생하는 이벤트입니다. 이벤트 발생 시 HandleScreenTouchEvent도 함께 실행됩니다. ScreenTouchEvent가 핸들러의 매개 변수로 전송되며, 터치한 위치의 좌표 (Vector2)가 포함되어 있습니다.
다음은 화면을 터치했을 때 터치한 위치의 좌표를 콘솔 창에 출력하는 예제입니다.

[service: InputService]
HandleScreenTouchEvent(ScreenTouchEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: InputService
    -- Space: Client
    ---------------------------------------------------------
    
    -- Parameters
    -- local TouchId = event.TouchId
    local TouchPoint = event.TouchPoint
    ---------------------------------------------------------
    
    log("Touch Point : "..tostring(TouchPoint))
}
16

ScreenTouchHoldEvent
ScreenTouchHoldEvent는 화면을 터치하고 있는 동안 프레임마다 발생합니다.
이벤트가 발생할 때마다 HandleScreenTouchHoldEvent가 실행됩니다. ScreenTouchHoldEvent가 핸들러의 매개 변수로 전송되며, 터치 중인 위치의 좌표 정보가 포함되어 있습니다.
화면을 터치 중일 때 터치한 위치의 좌표를 콘솔 창에 출력하는 예제입니다.

[service: InputService]
HandleScreenTouchHoldEvent(ScreenTouchHoldEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: InputService
    -- Space: Client
    ---------------------------------------------------------
    
    -- Parameters
    -- local TouchId = event.TouchId
    local TouchPoint = event.TouchPoint
    ---------------------------------------------------------
    
    log("Touch Point : "..tostring(TouchPoint))
}
18

ScreenTouchReleaseEvent
ScreenTouchReleaseEvent는 터치를 유지하다가 터치를 종료했을 때 1회 발생하는 이벤트입니다. 이벤트 발생 시 HandleScreenTouchReleaseEvent 함께 실행됩니다. ScreenTouchReleaseEvent가 핸들러의 매개 변수로 전송되며, 터치를 뗀 위치의 좌표 정보가 포함되어 있습니다.
다음은 마지막으로 터치한 곳의 좌표를 출력하는 예제입니다.

[service: InputService]
HandleScreenTouchReleaseEvent(ScreenTouchReleaseEvent event)
{
    --------------- Native Event Sender Info ----------------
    -- Sender: InputService
    -- Space: Client
    ---------------------------------------------------------
    
    -- Parameters
    -- local TouchId = event.TouchId
    local TouchPoint = event.TouchPoint
    ---------------------------------------------------------
    
    log("Touch Point : "..tostring(TouchPoint))
}
20
