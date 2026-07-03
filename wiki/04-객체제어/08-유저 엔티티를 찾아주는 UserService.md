# 유저 엔티티를 찾아주는 UserService

<!-- 출처: reference/TaskWiki.md · 문서 #90 -->


학습 과정 소개
UserService를 통해 상황별로 UserEntity를 받는 방법을 알아봅니다.
간단한 스크립트 예제를 통해 UserService가 제공하는 기능을 알아보겠습니다.

들어가기에 앞서
다음 가이드를 먼저 학습하면 본 과정을 이해하는 데 많은 도움이 됩니다.
서버와 클라이언트
실행 제어
Event System
Entity Event System

예제 진행 준비
먼저 Workspace - MyDesk의 콘텍스트 메뉴에서 Create Scripts - Create Component를 클릭하여 새 스크립트 컴포넌트를 생성한 뒤 이름을 Test로 변경합니다. 그리고 Test 컴포넌트를 Hierarchy - Common 엔티티에 추가합니다.
UserService_2

이후 Test 컴포넌트를 더블 클릭하여 스크립트 에디터를 엽니다.
3

이제 예제를 진행하면서 UserService를 알아봅시다.

유저 입장/퇴장 이벤트
월드에 유저가 들어오거나 나갈 때, UserService에서 입장/퇴장 이벤트가 발생합니다.
스크립트 컴포넌트에 이벤트 핸들러를 추가하여 유저 입장/퇴장 시점에 별도 처리를 추가할 수 있습니다.

UserEnterEvent
유저가 월드에 입장했을 때 발생하는 이벤트입니다.
스크립트 컴포넌트에서 이벤트 핸들러를 추가해서 유저가 입장했을 때의 처리를 추가할 수 있습니다.

다음은 유저가 월드에 입장했을 때, 입장한 유저의 UserId를 로그로 출력하는 예제입니다.
이를 통해 UserEnterEvent 핸들러를 추가하고 활용하는 방법을 알아보겠습니다.
다음과 같은 방법으로 UserEnterEvent 핸들러를 추가할 수 있습니다.
4

추가한 핸들러에는 매개 변수로 event가 들어오고 이를 통해 현재 게임에 입장한 UserId를 받습니다.
다음과 같이 코드를 작성하면, 유저가 게임에 입장할 때마다 UserId를 콘솔 창에 출력합니다.

Event Handler:
[service: UserService]
HandleUserEnterEvent (UserEnterEvent event)
{
    -- Parameters
    local UserId = event.UserId
    --------------------------------------------------------
    -- 입장 유저의 UserId를 콘솔 창에 출력
    log("User Enter! : "..UserId)
}

start [시작] 버튼을 누른 뒤 테스트해 봅시다.
아래와 같이 새 클라이언트를 추가합니다.
7

새 유저가 게임에 입장했을 때 콘솔 창에 로그가 출력됩니다.
6

UserLeaveEvent
유저가 월드에서 퇴장했을 때 발생하는 이벤트입니다.
다음은 유저가 월드에서 퇴장했을 때, 퇴장한 유저의 UserId를 콘솔 창에 출력하는 예제입니다.
UserLeaveEvent 핸들러를 추가하고 다음과 같이 코드를 작성합니다.

Event Handler:
[service: UserService]
HandleUserLeaveEvent (UserLeaveEvent event)
{
    -- Parameters
    local UserId = event.UserId
    --------------------------------------------------------
    -- 퇴장 유저의 UserId를 콘솔 창에 출력
    log("User Leave! : "..UserId) 
}

start [시작] 버튼을 누른 뒤 테스트해 봅시다.
유저가 퇴장할 때 출력되는 로그를 확인해야 하므로 클라이언트를 추가합니다.
7

새 유저가 들어온 뒤, 추가된 클라이언트를 다시 종료하여 새 유저를 퇴장시킵니다. 그리고 유저가 퇴장할 때 아래와 같이 로그가 출력되는 것을 확인합니다.
13

유저 접속 끊김/재접속 이벤트
유저의 네트워크가 불안정하면 접속이 끊길 수 있습니다. 또한 다시 재접속할 수도 있습니다.
이와 같이 접속 끊김/재접속 이벤트가 UserService에서 발생합니다. 스크립트 컴포넌트에서 해당 이벤트 핸들러를 추가하여 유저의 접속 끊김 또는 재접속 시점에 별도 처리를 추가할 수 있습니다.

UserDisconnectEvent
유저의 네트워크 접속이 불안정하여 끊겼을 때 발생하는 이벤트입니다.
스크립트 컴포넌트에서 해당 이벤트 핸들러를 추가하여 접속이 끊겼을 때 처리를 추가할 수 있습니다.

다음은 접속이 끊긴 UserId와 시간을 출력하는 예제입니다.
이벤트 핸들러에 UserDisconnectEvent를 추가하고 아래와 같이 작성해 봅시다.

Event Handler:
[service: UserService]
HandleUserDisconnectEvent (UserDisconnectEvent event)
{
    -- Parameters
    local DisconnectMapName = event.DisconnectMapName
    local TimeNetworkClosed = event.TimeNetworkClosed
    local UserId = event.UserId
    --------------------------------------------------------
    log("UserDisconnectEvent : "..UserId.." : "..DisconnectMapName.." : "..tostring(TimeNetworkClosed))
}

위와 같이 작성하면 유저의 접속이 끊겼을 때 콘솔 창에 로그가 출력됩니다.
disconnect

UserReconnectEvent
유저가 재접속했을 때 발생하는 이벤트입니다.
스크립트 컴포넌트에서 해당 이벤트 핸들러를 추가하여 재접속이 발생했을 때의 처리를 추가할 수 있습니다.

다음은 재접속한 UserId와 재접속 시간을 출력하는 예제입니다.
이벤트 핸들러에 UserReconnectEvent를 추가하고 아래와 같이 작성해 봅시다.

Event Handler:
[service: UserService]
HandleUserReconnectEvent (UserReconnectEvent event)
{
    -- Parameters
    local ReconnectMapName = event.ReconnectMapName
    local TimeNetworkClosed = event.TimeNetworkClosed
    local UserId = event.UserId
    --------------------------------------------------------
    log("UserReconnectEvent : "..UserId.." : "..ReconnectMapName.." : "..tostring(TimeNetworkClosed))
}

위와 같이 작성하면 유저가 재접속했을 때 콘솔 창에 로그가 출력됩니다.
reconnect

더 알아보기
접속 끊김 및 재접속 상황을 일반적으로 테스트하기는 어렵습니다.
위의 예제와 같이 코드를 작성하면 로그를 남길 수 있다는 점을 참고하기 바랍니다.

게임에 참여 중인 모든 유저 엔티티 받아오기
UserEntities
UserService는 게임에 참여 중인 모든 유저 엔티티를 받아오는 UserEntities 프로퍼티를 제공합니다.
UserEntities는 사전(Dictionary) 타입입니다. Key - Value 값으로 UserId - MODEntity를 반환합니다.
다음은 유저가 게임에 들어올 때마다 모든 플레이어를 순회하며 Entity Name을 출력하는 예제입니다.
위의 UserEnterEvent를 다음과 같이 수정합니다.

Event Handler:
[service: UserService]
HandleUserEnterEvent (UserEnterEvent event)
{
    -- Parameters
    local UserId = event.UserId
    --------------------------------------------------------
    --UserService로 모든 유저를 Dictionary로 받음
    local AllUserEntitiesDic = _UserService.UserEntities                    
    for userId, playerEntity in pairs(AllUserEntitiesDic) do
        --모든 유저를 순회하며 userId와 Entity.Name을 출력
        log("userId : playerEntity = "..userId.." : "..playerEntity.Name)
    end
}

start [시작] 버튼을 누른 뒤 테스트해 봅시다.
콘솔 창에 Key 값인 UserId와 MODEntity.Name이 출력됩니다.
15

클라이언트 추가 버튼을 눌러 봅시다.
7

새 유저가 게임에 입장할 때마다 게임에 참여 중인 모든 유저를 순회하며 UserId와 MODEntity.Name이 출력됩니다.
17

게임에 참여 중인 모든 유저 정보 받아오기
Users
UserService는 게임에 참여 중인 모든 유저 정보를 받아오는 Users 프로퍼티를 제공합니다.
Users는 모든 유저의 UserId, 프로필 이름(Nickname), 프로필 코드를 반환합니다.
다음은 유저가 게임에 들어올 때마다 모든 유저를 순회하며 유저 정보를 출력하는 예제입니다.
위의 UserEnterEvent를 다음과 같이 수정합니다.

Event Handler:
[service: UserService]
HandleUserEnterEvent (UserEnterEvent event)
{
    -- Parameters
    local UserId = event.UserId
    --------------------------------------------------------
    local users = tostring(#_UserService.Users).."\n"
    for i, j in pairs(_UserService.Users) do
     users = users..j.UserId.." "..j.Nickname.." "..j.ProfileCode.."\n"
    end
    
    log(users)
}
start [시작] 버튼을 누른 뒤 테스트해 봅시다.
콘솔 창에 유저 수, UserId, 프로필 이름, 프로필 코드가 출력됩니다.
001

클라이언트 추가 버튼을 누르고 새 유저가 게임에 입장할 때마다 모든 유저 정보가 출력되는 것을 확인합니다.
002

게임에 참여 중인 유저 수 가져오기
GetUserCount()
GetUserCount()는 현재 게임에 참여 중인 유저 수를 리턴하는 함수입니다.
다음은 유저가 게임에 들어올 때마다 게임에 참여 중인 모든 유저 수를 출력하는 예제입니다.
UserEnterEvent를 다음과 같이 수정합니다.

Event Handler:
[service: UserService]
HandleUserEnterEvent (UserEnterEvent event)
{
    -- Parameters
    local UserId = event.UserId
    --------------------------------------------------------
    local userCount = _UserService:GetUserCount()
    log("CurrentUserCount : "..userCount)
}

start [시작] 버튼을 누른 뒤 테스트해 봅시다.
클라이언트를 추가할 때마다 콘솔 창에 CurrentUserCount가 증가합니다.
19

특정 맵에 있는 모든 유저 받아오기
UserService에는 특정 맵에 있는 유저만 받아오는 함수를 제공합니다.


GetUsersByMapName()
mapName을 이용해 특정 맵에 있는 유저 엔티티를 배열로 리턴하는 함수입니다. mapName을 스트링으로 넘겨줍니다. 리턴 받은 배열 값은 반복문을 통해 개별 유저 엔티티를 받아올 수 있습니다.

다음은 map01에 있는 모든 유저를 GetUserByMapName() 함수로 받아오는 코드입니다.
UserEnterEvent를 다음과 같이 수정합니다.

Event Handler:
[service: UserService]
HandleUserEnterEvent (UserEnterEvent event)
{
    -- Parameters
    local UserId = event.UserId
    --------------------------------------------------------
    local mapName = _EntityService:GetEntityByPath("/maps/map01").Name
    local playersArr = _UserService:GetUsersByMapName(mapName)
    for index, player in pairs(playersArr) do
        log("PlayerName : CurrentMap = "..player.Name.." : "..player.CurrentMap.Name)
    end
}

start [시작] 버튼을 누른 뒤 테스트해 봅시다.
유저를 추가할 때마다 map01에 있는 모든 유저의 이름과 현재 위치한 맵 이름이 출력됩니다.
21


더 알아보기.

맵과 클라이언트를 추가해서 테스트하면 좀 더 정확한 결과를 얻을 수 있습니다.
맵 생성과 포탈 연결 방법은 맵 생성과 관리 를 참고하세요.

map02를 추가하고, map01과 map02가 연결된 포탈을 추가해 줍니다.
UserService_22


플레이 중 클라이언트 셋을 더 추가하고, 유저 둘은 map01에, 나머지 둘은 map02에 위치시켜 줍니다.
UserService_23


유저가 각기 다른 맵에 들어가 있는 상황에서 유저를 하나씩 추가해 봅니다.
유저가 추가될 때마다 map01에 있는 유저들의 이름과 위치한 맵 이름이 출력되는 것을 확인합니다.
24



GetUsersByMapComponent()
GetUsersByMapComponent() 역시 특정 맵에 있는 유저 엔티티를 얻어오는 함수입니다.
특정 맵의 mapId가 아닌 mapComponent를 매개 변수로 넘겨줍니다.

다음은 map01에 있는 모든 유저를 GetUsersByMapComponent()로 받아오는 코드입니다.
UserEnterEvent을 다음과 같이 수정합니다.

Event Handler:
[service: UserService]
HandleUserEnterEvent (UserEnterEvent event)
{
    -- Parameters
    local UserId = event.UserId
    --------------------------------------------------------
    -- map01의 컴포넌트를 받음
    local mapComponent = _EntityService:GetEntityByPath("/maps/map01").MapComponent    
    -- mapComponent를 매개 변수로 넘겨 map01에 있는 유저를 배열로 받음
    local playersArr = _UserService:GetUsersByMapComponent(mapComponent)
    for index, player in pairs(playersArr) do
       log("PlayerName : CurrentMap = "..player.Name.." : "..player.CurrentMap.Name)         
    end
}    

start [시작] 버튼을 누른 뒤 테스트해 봅시다.
유저를 추가할 때마다 map01에 있는 모든 유저의 이름과 현재 위치한 맵 이름이 출력됩니다.
26

UserId를 이용해 플레이어 엔티티 받아오기
GetUserEntityByUserId()
GetUserEntityByUserId()는 유저 아이디를 통해 해당 플레이어 엔티티를 리턴하는 함수입니다.

게임을 제작하다 보면 UserId만 알고 있는 상태에서 해당 아이디의 플레이어 엔티티를 받아와야 할 때가 있습니다. UserEntities로 모든 유저를 받아온 다음, 하나씩 순회하면서 같은 아이디의 엔티티를 찾을 수도 있겠지만, 매번 모든 유저를 순회하며 찾는 것은 상당히 비효율적입니다.

GetUserEntityByUserId()는 이런 상황에서 사용할 수 있는 함수입니다. 유저의 아이디만 매개 변수로 넘겨주면 되기 때문에 원하는 유저 엔티티를 쉽게 받을 수 있습니다.
다음은 게임에 입장한 UserId를 통해 유저 엔티티를 받아 이름을 출력하는 코드입니다.

Event Handler:
[service: UserService]
HandleUserEnterEvent (UserEnterEvent event)
{
    -- Parameters
    local UserId = event.UserId
    --------------------------------------------------------
    local EnterdPlayerEntity = _UserService:GetUserEntityByUserId(UserId)
    log("EnterdPlayerEntityName : "..EnterdPlayerEntity.Name)  
}

start [시작] 버튼을 누른 뒤 테스트해 봅시다.
클라이언트를 추가할 때마다 새로 들어온 유저의 이름이 출력됩니다.
28

내 플레이어 받아오기 (클라이언트 전용)
LocalPlayer
LocalPlayer는 클라이언트에서 내 유저 엔티티를 얻을 수 있는 프로퍼티입니다.
특정 클라이언트에서 내 캐릭터라는 개념은 클라이언트에서만 유효합니다. 그러므로 서버에서는 사용할 수 없고 반드시 클라이언트에서만 사용할 수 있습니다.

UserEnterEventType은 서버에서만 발생하기 때문에, 클라이언트에서 실행할 수 있는 함수를 하나 추가하여
유저가 게임에 들어올 때마다 내 캐릭터의 이름을 출력하는 코드를 작성해 줍니다.

Method: 
[client]
void PrintLocalPlayerName()
{
    -- 클라이언트에서의 내 유저를 받아옴
    local MyPlayer = _UserService.LocalPlayer   
    log("MyPlayerName : "..MyPlayer.Name)
}
Event Handler: 
[service: UserService]
HandleUserEnterEvent (UserEnterEvent event)
{
    -- Parameters
    local UserId = event.UserId
    --------------------------------------------------------
    --이벤트가 서버에서 발생하기 때문에, LocalPlayer를 받아올 수 있는 클라이언트 함수 호출
    self:PrintLocalPlayerName()
}
start [시작] 버튼을 누른 뒤 테스트해 봅시다.
어떤 유저가 들어오든, 현재 클라이언트의 내 캐릭터 이름이 출력됩니다.
30


더 알아보기
클라이언트 공간, 서버 공간에서의 함수 실행은 실행 제어를 참고하세요.
