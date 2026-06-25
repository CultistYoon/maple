# MSW 기본 이벤트 함수

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「MSW 기본 이벤트 함수」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 01 시작하기 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
메이플스토리 월드에서 스크립트를 활용하면 크리에이터만의 독창적인 월드를 자유자재로 만들 수 있습니다. 스크립트를 작성할 때는 필요에 따라 기본 이벤트 함수를 활용하게 됩니다. 기본 이벤트 함수란 다른 함수에서 직접 호출하지 않아도 특정 조건이 되면 자동으로 호출되는 함수를 말합니다.
이번 과정에서는 기본 이벤트 함수의 종류와 호출 시점을 알아봅시다.

기본 이벤트 함수 추가하기
기본 이벤트 함수를 추가해 봅시다.

Workspace - MyDesk의 콘텍스트 메뉴에서 Create Scripts - Create Component를 클릭해 새 스크립트 컴포넌트를 생성하고 스크립트 에디터를 엽니다.


Function 옆의 [+] 버튼을 클릭합니다. New(사용자 지정 함수) 외에는 모두 기본 제공되는 이벤트 함수입니다. 필요에 따라 함수를 추가합니다.
2
3

기본 이벤트 함수
메이플스토리 월드에서 제공하는 이벤트 함수는 기본적으로 서버에서 호출합니다.
크리에이터의 의도에 따라 호출 공간을 다르게 설정할 수 있습니다.
4

이제 함수를 좀 더 자세히 살펴봅시다.

OnInitialize
OnBeginPlay 함수가 호출되기 전, 엔티티와 컴포넌트가 생성된 후에 1회 호출되는 함수입니다.
단, OnInitialize 함수는 엔티티의 컴포넌트가 생성되기 전에 호출될 수 있습니다. 그러므로 OnInitialize 함수에서 다른 컴포넌트 또는 엔티티 참조 시 nil을 받아올 가능성이 있습니다.

void OnInitialize()
{
    local myEntity = self.Entity      
    --자기 자신이 적용된 엔티티 참조 가능
    --콘솔 창에 myEntity의 이름과 "Hello MapleStory Worlds!" 출력
    log(myEntity.Name.."Hello MapleStory Worlds")

    --아래와 같이 OnInitialize 내부에서 다른 엔티티나 컴포넌트의 참조는 추천하지 않음
    local otherComponent = myEntity.컴포넌트 이름      --nil 일 가능성 있음
    local anotherEntity = _EntityService:GetEntityByPath("엔티티 경로")  --다른 엔티티 참조. nil 일 가능성 있음
}
OnBeginPlay
본격적으로 로직이 시작되는 시점(OnInitialize 함수 호출 이후, OnUpdate 호출 직전)에 1회 호출되는 함수입니다.
엔티티의 OnBeginPlay 함수는 다른 엔티티와 컴포넌트가 모두 생성된 뒤에 호출됩니다. 동적으로 생성된 엔티티도 해당 엔티티의 컴포넌트가 모두 생성된 후에 OnBeginPlay 함수가 호출됩니다. 그러므로 OnInitialize 함수와는 달리 OnBeginPlay 함수는 다른 엔티티 및 컴포넌트의 참조가 보장됩니다.

void OnBeginPlay()
{
    local myEntity = self.Entity    -- 자기 자신이 적용된 엔티티 참조 가능.
    log(myEntity.Name.."Hello MapleStory Worlds")    -- 콘솔 창에 myEntity의 이름과 "Hello MapleStory Worlds!" 출력
     
    --OnInitialize와는 달리 아래와 같이 다른 엔티티, 다른 컴포넌트의 참조가 보장됨
    local otherComponent = myEntity.컴포넌트 이름
    local otherEntity = _EntityService:GetEntityByPath("엔티티 경로")
    local otherEntityComponent = otherEntity :GetComponent("컴포넌트 이름")
}

하지만 각 컴포넌트 간의 OnBeginPlay 함수 호출 순서는 보장되지 않습니다. 그러므로 특정 컴포넌트에서 OnBeginPlay 함수로 설정한 값을 받아오면 제대로 작동하지 않을 가능성이 있습니다.
예를 들어 봅시다.

컴포넌트 A에서 프로퍼티 B를 " "로 정의합니다. 그리고 OnBeginPlay 함수에서 프로퍼티 B를 "Hello"로 설정합니다.

컴포넌트 C의 OnBeginPlay 함수에서 프로퍼티 B를 참조합니다.

이때 "Hello"가 아닌 nil을 받아올 수도 있습니다.

-- ComponentA
Property: 
[Sync]
string B = ""

Method: 
[server only]
void OnBeginPlay()
{
    self.B = "Hello"
    log(self.B)
}

-- ComponentC    
Property: 

Method: 
[Server Only]
void OnBeginPlay()
{
    local myEntity = self.Entity
    local componentA = myEntity.ComponentA
    log(componentA.B)   
    --ComponentA와 ComponentC의 OnBeginPlay 중 무엇이 먼저 호출될지 모르므로, 콘솔 창에 nil이 출력될 수 있음.
}

따라서 다른 컴포넌트의 OnBeginPlay 함수에서 컴포넌트 A의 프로퍼티를 참조해야 한다면, 다음과 같이 OnInitialize 함수를 활용해 봅시다.

-- ComponentA
Property: 
[Sync]
string B = ""

Method: 
[server only]
void OnInitialize()
{
    self.B = "Hello"
    log(self.B)
}

-- ComponentC
Property: 

Method: 
[Server Only]
void OnBeginPlay()
{
    local myEntity = self.Entity
    local componentA = myEntity.ComponentA
    log(componentA.B)   
    -- ComponentA에서 OnInitialize를 통해 값을 할당했으므로, 콘솔 창에 "Hello"가 출력
}
OnUpdate
OnBeginPlay 함수 호출 이후, 프레임마다 호출되는 함수입니다.
따라서 프레임별로 엔티티 위치, 상태, 동작을 변경하고 싶다면 OnUpdate 함수에 스크립트를 작성합니다.
매개 변수로 delta를 사용하며, 이전 프레임에 걸린 시간 값(단위: 초)을 받습니다.
delta를 활용하여 프레임 단위 구현을 할 수 있고, 특정 시간마다 액션을 제어할 수 있습니다.

void OnUpdate(number delta)
{
    if self._T.Time == nil then self._T.Time = 0 end
    self._T.Time = self._T.Time + delta
     
    --3초마다 Console 창에 Hello MapleStory Worlds를 출력
    if self._T.Time >= 3 then
        self._T.Time = 0
        log("Hello MapleStory Worlds")
    end
}
OnEndPlay
OnDestroy 함수와 함께 엔티티가 제거되는 시점에 1회 호출되는 함수입니다.
다만 OnEndPlay 함수가 완료된 후에도 엔티티는 제거되지 않고 유효한 상태입니다.
OnEndPlay 함수가 호출된 이후, OnDestroy 함수가 호출됩니다.

void OnEndPlay()
{
    log("OnEndPlay!!")
    -- Console Result
    -- OnEndPlay!!
}
OnDestroy
엔티티가 제거되는 시점에 1회 호출되는 함수입니다. OnEndPlay 함수 이후 호출됩니다.
OnEndPlay 함수와는 달리, OnDestroy 함수 완료 뒤에는 엔티티가 제거됩니다.

void OnDestroy()
{
    log("OnDestroy!!")
    -- Console Result
    -- OnDestroy!!
}


더 알아보기
위에 설명한 OnInitialize 함수에서 OnDestroy 함수까지 실행 순서는 다음과 같습니다.
5

OnMapEnter
OnBeginPlay가 엔티티가 생성될 때마다 호출되는 함수라면, OnMapEnter는 엔티티가 맵에 입장하거나, 맵에 생성될 때마다 호출되는 함수입니다. 따라서 맵을 이동할 때마다 초기화해야 하는 엔티티에 사용하면 좋습니다.

OnMapEnter 함수를 호출하면 입장한 맵의 엔티티가 매개 변수로 넘어옵니다.
플레이어가 월드에 진입했을 때 OnInitialize 함수나 OnBeginPlay 함수를 활용해 초기화하는 것처럼, 플레이어가 특정 맵에 진입했을 때는 OnMapEnter 함수를 사용해 필요한 처리를 할 수 있습니다.

다음은 OnMapEnter 함수를 활용하여 map01에 입장할 때마다 플레이어의 크기가 커지도록 구현한 예시입니다.

void OnMapEnter(Entity enteredMap)
{
    --map01에 입장할 때마다 플레이어 크기가 커짐
    if enteredMap.Name == "map01" then
        local myPlayer = self.Entity
        local transform = myPlayer.TransformComponent
        local scale = transform.Scale
        scale.x = scale.x + 1
        scale.y = scale.y + 1
        transform.Scale = scale
    end
}
OnBeginPlay와 OnMapEnter 차이
예를 들어, 내 플레이어 엔티티가 map01에서 map02로 이동했다고 가정합니다. 이때 내 플레이어 엔티티의 스크립트 컴포넌트에 OnMapEnter 함수가 있었다면, map02로 이동할 때 내 플레이어 엔티티의 OnMapEnter 함수가 호출됩니다. 그런데 내 플레이어뿐만 아니라 다른 플레이어의 OnMapEnter 함수도 호출되는 것을 볼 수 있습니다. 클라이언트 상에서 보자면, 현재 내가 존재하는 맵에 다른 플레이어 엔티티가 생성된 것과 마찬가지이기 때문입니다.

하지만 서버상에서는 내 플레이어 엔티티가 map01에서 map02로 이동한다 해도, 원래 map02에 있던 다른 플레이어 엔티티가 새롭게 생기는 것은 아닙니다. 다른 플레이어 엔티티는 내 플레이어가 해당 월드에 진입한 순간부터 이미 존재했던 것입니다. 서버상의 생성은 해당 월드에 최초 진입하는 순간에 이루어지기 때문에, 서버상의 OnBeginPlay 함수는 내 플레이어가 월드에 진입하여 엔티티들이 생성되는 단 한 번만 호출됩니다.

이와는 달리 OnMapEnter 함수는 엔티티가 맵을 이동할 때마다 호출됩니다. 이는 클라이언트뿐만 아니라 서버 상에서도 동일하게 작동하기 때문에 플레이어 엔티티가 맵을 이동할 때마다 OnMapEnter 함수가 호출되는 것입니다. 이와 같은 차이점을 이해하고 용도에 맞게 OnBeginPlay 함수와 OnMapEnter 함수를 사용해야 합니다.

OnMapLeave
OnMapEnter 함수와 반대로 엔티티가 맵에서 퇴장할 때, 혹은 맵에 제거될 때마다 호출되는 함수입니다.
OnMapEnter 함수처럼 맵을 이동할 때마다 초기화가 필요한 엔티티에 활용하면 좋습니다.

OnMapLeave 함수를 호출하면 퇴장한 맵의 엔티티가 매개 변수로 넘어옵니다.
다음은 OnMapLeave 함수를 활용하여 map01에서 퇴장할 때마다 플레이어의 크기가 작아지도록 구현한 예시입니다.

void OnMapLeave(Entity leftMap)
{
    --map01에서 퇴장할 때마다 플레이어 크기가 작아짐
    if leftMap.Name == "map01" then
        local myPlayer = self.Entity
        local transform = myPlayer.TransformComponent
        local scale = transform.Scale
        scale.x = scale.x - 1
        scale.y = scale.y - 1
        transform.Scale = scale
    end
}


OnSyncProperty
서버에서 변경된 값이 클라이언트로 동기화될 때 클라이언트에서 호출되는 함수입니다.
OnSyncProperty 함수를 호출하면 동기화된 프로퍼티의 이름과 값이 매개 변수로 넘어옵니다.
프로퍼티 동기화 설정을 None으로 하면 동기화가 이루어지지 않으므로 OnSyncProperty 함수는 호출되지 않습니다.

Property: 
[Sync]
number HP = 100
[Sync]
number MP = 100
 
Method: 
[Client Only]
void OnSyncProperty(string name, any value) --name : 프로퍼티 이름, value : 변경된 프로퍼티 값
{
    if name == "HP" then
        if self.HP == value then 
            log("동기화가 완료된 시점에 호출되므로, 이 로그가 콘솔 창에 출력됩니다.")
            return 
        end
        
        if value > 0 then 
            return 
        end
        
        -- HP 값이 0 이하일 때의 처리를 추가합니다.
        
    elseif name == "MP" then
        if self.MP == value then
            log("동기화가 완료된 시점에 호출되므로, 이 로그가 콘솔 창에 출력됩니다.")
        end
        
        if value > 0 then 
            return 
        end
        
        -- MP 값이 0 이하 일 때의 처리를 추가합니다.   
        
    end
}
