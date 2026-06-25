# Entity Event System

<!-- 출처: reference/TaskWiki.md · 문서 #113 -->


학습 과정 소개
메이플스토리 월드에서는 Entity Event System을 사용해 이벤트를 제어할 수 있습니다.
이번 시간에는 Entity Event System을 이용해 "뱀파이어 vs 헌터"의 게임 요소 중 하나를 만들어봅시다.
다음 가이드를 먼저 학습하면 이번 과정을 이해하는 데 많은 도움이 됩니다.
Event System

Entity Event System
이벤트를 받고 보내려면 먼저 Entity Event System을 이해해야 합니다.
컴포넌트는 엔티티를 중계자로 사용할 수 있습니다.
각각의 컴포넌트는 엔티티를 통해 핸들러를 등록하고 이벤트를 발생시킬 수 있습니다.
3

센더 역시 엔티티를 통해 이벤트를 발생시킵니다. 엔티티는 발생한 이벤트를 핸들러에 전송합니다.
4

기본적으로는 자기 자신의 엔티티에 이벤트를 연결하지만, 아래 그림처럼 상황에 따라 다른 엔티티에 연결할 수도 있습니다. 특히, 맵 엔티티와 월드 엔티티는 서로 이벤트를 주고받는 경우가 많아 아래와 같은 형태를 자주 사용합니다.
5

Sunrise Event 생성
이벤트 시스템에는 기본 제공되는 네이티브 형 이벤트가 있습니다. 또한 크리에이터가 직접 이벤트 타입을 선언하거나 Import 할 수도 있습니다. 방법은 아래와 같습니다.


Workspace - MyDesk의 콘텍스트 메뉴에서 Create EventType을 클릭합니다.
eventtype


새로 만든 이벤트 타입의 이름으로 SunriseEvent를 입력합니다.
2


SunriseEvent 스크립트를 연 뒤, 아래와 같이 Property를 추가합니다. isSunrise를 통해 해가 뜨고 지는 상태를 True / False로 확인할 것입니다.

Property:
boolean isSunrise = false
이벤트를 처리할 컴포넌트와 엔티티 생성
SunriseEvent를 이용해 "뱀파이어 vs 헌터" 로직을 만들어보겠습니다.
뱀파이어와 헌터는 일반적인 전투와 움직임을 보이다가 SunriseEvent를 받게 됩니다.
Sunrise 상태일 때, 헌터는 따뜻한 햇볕으로 HP를 회복하고 뱀파이어는 HP가 감소하도록 만들어봅시다.


Sunrise 상태의 로직을 구현해 봅시다.
먼저 Workspace - MyDesk의 콘텍스트 메뉴에서 Create Scripts - Create Component를 클릭해 신규 스크립트 컴포넌트 2개를 만듭니다. 이름으로 VampireComponent와 HunterComponent를 입력합니다.


뱀파이어 NPC 엔티티와 헌터 NPC 엔티티를 배치합니다.
예제에서는 Preset List - NPC에서 아래 두 개의 NPC를 배치했습니다.

뱀파이어 : npc-3842

헌터 : npc-4064
2-3


배치한 NPC의 이름으로 Vampire, Hunter를 입력합니다.
2-4


뱀파이어 엔티티에 VampireComponent를, 헌터 엔티티에 HunterComponent를 각각 추가합니다.
2-5 2-6

핸들러 로직
HunterComponent, VampireComponent 스크립트를 작성해 봅시다.
우선 두 컴포넌트 모두 SunriseEvent를 받도록 해야 합니다.

HunterComponent, VampireComponent 스크립트를 엽니다.
Event Handler에서 [+] 버튼을 누르고, SunriseEvent를 추가합니다.
6


SunriseEvent의 중계 엔티티를 map01으로 설정해야 합니다.
다음과 같이 핸들러 상단의 이벤트 중계자를 map01로 설정합니다.
6-1


이제 각자 받은 SunriseEvent를 처리하는 로직을 넣어봅시다.
먼저, 해가 뜨면 헌터의 HP가 증가하도록 HunterComponent를 작성합니다.

Property: 
[Sync]
boolean isSunrise = false
[Sync]
number Hp = 0

Method: 
[server Only]
void OnUpdate(number delta)
{
    if self.isSunrise == true then --해가 떴는지 체크합니다.
        self.Hp = self.Hp + delta --해가 떠 있을 동안 HP가 증가합니다.
        log("Hunter Hp : "..self.Hp) --현재 체력을 Console 창에 표시합니다.
        if self.Hp >= 200 then self.Hp = 200 end --HP가 200까지 증가했다면 증가를 멈춥니다.
    end
}

Event Handler: 
[entity: map01(/maps/map01)]
HandlerSunriseEvent(SunriseEvent event)
{
    -- Parameters
    local isSunrise = event.isSunrise
    self.isSunrise = isSunrise
}


해가 뜨면 뱀파이어의 HP는 감소하도록 VampireComponent를 작성합니다.

Property: 
[Sync]
boolean isSunrise = false
[Sync]
number Hp = 0

Method: 
[server Only]
void OnUpdate(number delta)
{
    if self.isSunrise == true then --해가 떴는지 체크합니다.
        self.Hp = self.Hp - delta --해가 떠 있을 동안 HP가 감소합니다.
        log("Vampire Hp : "..self.Hp) --현재 HP를 Console 창에 표시합니다.
        if self.Hp < 0 then self.Hp = 0 end --HP가 0까지 감소했다면 감소를 멈춥니다.
    end
}

Event Handler: 
[entity: map01(/maps/map01)]
HandlerSunriseEvent(SunriseEvent event)
{
    -- Parameters
    local isSunrise = event.isSunrise
    self.isSunrise = isSunrise
}


뱀파이어 엔티티와 헌터 엔티티의 프로퍼티 에디터에서 Hp 값을 각각 100으로 설정합니다.
10-2
10-1

이벤트 발생 로직
특정 시간마다 해가 뜨고 지는 로직을 만들어봅시다.


해가 뜨고 지는 시간을 관리할 스크립트 컴포넌트가 필요합니다.
Workspace - MyDesk의 콘텍스트 메뉴에서 Create Scrips - Create Component를 클릭해 새 컴포넌트를 만듭니다. 이름으로 TimeManager를 입력합니다.


TimeManager 스크립트 컴포넌트를 엽니다. OnUpdate 함수를 추가하여 해가 뜨고 지는 것을 판단하도록 합니다.

Property: 
[Sync]
boolean isSunrise = false

Method: 
[server only]
void OnUpdate(number delta)
{
    if self._T.Time == nil then self._T.Time = 0 end
    self._T.Time = self._T.Time + delta

    if self._T.Time >= 5 then --5초마다 번갈아 해가 뜨고 집니다.
        self._T.Time = 0
        if self.isSunrise == true then
            self.isSunrise = false
        else
            self.isSunrise = true --해가 떠 있지 않으면 isSunrise = false입니다.
        end
        log(self.isSunrise)
        self:SendEvent(self.isSunrise)
    end
}

[server]
void SendEvent(boolean isSunrise)
{
    local event = SunriseEvent()
    event.isSunrise = isSunrise
    self.Entity:SendEvent(event)

    self.isSunrise = isSunrise
    self._T.Time = 0
}


Hierarchy - map01의 콘텍스트 메뉴에서 Add Component를 클릭합니다. TimeManager 컴포넌트를 추가합니다.
11-1
이제 필요한 스크립트 컴포넌트를 모두 작성했습니다. 주기적으로 해가 뜨고 지는 이벤트를 보내고 받을 수 있습니다.


추가로 헌터의 궁극기인 일출 스킬을 제작해 봅시다.
Z 키를 이용해 이벤트를 호출하겠습니다.
HunterComponent에 KeyDownEvent를 추가하고 아래와 같이 작성합니다.

[service: InputService]
HandleKeyDownEvent(KeyDownEvent event) 
{
    -- Parameters
    local key = event.key
    --------------------------------------------------------------------------------
    if key == KeyboardKey.Z then --Z 키를 누르면 `일출` 메시지가 Console 창에 나타납니다.
        log("일출")
        local timeManager = self.Entity.CurrentMap.TimeManager
        timeManager:SendEvent(true) --Timemanager의 Event가 true가 되도록 합니다.
    end
}

이제 Z 키를 누르면 해가 뜹니다.
