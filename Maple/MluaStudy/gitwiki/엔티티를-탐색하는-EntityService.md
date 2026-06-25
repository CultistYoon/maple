# 엔티티를 탐색하는 EntityService

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「엔티티를 탐색하는 EntityService」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 04 객체제어 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
월드를 제작하다 보면 특정 엔티티를 탐색하여 받아오거나, 혹은 관련 있는 여러 엔티티를 한 번에 받아야 하는 상황이 자주 발생합니다. 이럴 때 EntityService를 활용할 수 있습니다. EntityService는 엔티티 탐색, 삭제, 유효성 체크 등의 기능을 제공하고 있습니다.
이번 과정에서는 EntityService에서 제공하는 기능의 사용법을 하나씩 알아보도록 하겠습니다.

테스트 환경
01
common에 컴포넌트를 생성한 뒤 예제 코드를 넣고 테스트 해주시길 바랍니다.

Entity 탐색 함수
EntityService에서는 8개의 엔티티를 탐색하는 함수를 제공합니다.
각 함수는 월드 경로, 엔티티 ID, 모델 ID 등을 매개 변수로 전달 받고, 이를 통해 엔티티를 탐색하여 반환합니다.
각 함수별 기능에 따라 개별 엔티티를 반환하거나 혹은 여러 엔티티를 반환하기도 합니다.

GetEntityByPath()
월드 상의 경로(path)와 일치하는 단일 엔티티를 반환하는 함수입니다.
만일 월드 경로가 같은 엔티티가 2개 이상 존재하면 가장 먼저 찾은 엔티티를 반환합니다.
따라서 GetEntityByPath는 월드 경로가 유니크한 엔티티를 탐색할 때 사용하는 것을 권장합니다.
worldPath는 Hierarchy의 각 엔티티 콘텍스트 메뉴에서 Copy Entity Path로 가져올 수 있습니다.
1


void GetEntityByPathExample()
{
    local entity = _EntityService:GetEntityByPath("/maps/map01/npc-320_1")
    local uiEntity = _EntityService:GetEntityByPath("/ui/DefaultGroup/Image_1")
    
    log(entity.Name)
    log(uiEntity.Name)
}
GetEntitiesByPath()
매개 변수로 전달한 월드 경로와 일치하는 모든 엔티티를 반환하는 함수입니다.
만일 찾고자 하는 엔티티가 여러 개이고, 해당 엔티티들이 같은 월드 경로를 갖고 있을 때 사용합니다. 예를 들어 탄막 슈팅 게임에서 생성된 수많은 총알 엔티티와 같이 같은 이름으로 생성된 모든 엔티티를 받아오고 싶을 때 사용하면 효과적입니다.
2


void GetEntitiesByPathExample()
{
    local entityArray = _EntityService:GetEntitiesByPath("/maps/map01/Bullet")
    
    for i, entity in pairs(entityArray) do
        log(entity.Name)
    end
}
GetEntity()
매개 변수로 받은 엔티티 ID와 일치하는 엔티티를 반환합니다.
위와 같이 같은 이름의 엔티티가 여러 개 있는 상황에서 원하는 엔티티 하나만 받아오고 싶을 때 사용하면 효과적입니다.
엔티티 ID는 Hierarchy의 해당 엔티티 콘텍스트 메뉴에서 Copy Entity ID로 가져오거나, 스크립트에서 엔티티 ID를 받아올 수도 있습니다.
3


void GetEntityExample()
{
    local bulletEntity = _EntityService:GetEntityByPath("/maps/map01/Bullet")
    local bulletEntityId = bulletEntity.Id
    
    local bulletEntityById = _EntityService:GetEntity(bulletEntityId)
    
    if bulletEntity == bulletEntityById then
        log(bulletEntity.Id)
    end
}
GetEntitiesSpawnedByModelId()
모델 ID와 일치하는 모델로부터 생성된 모든 엔티티를 반환합니다.
다음과 같이 수많은 엔티티가 배치된 상황에서 NPC와 같이 동일 모델로부터 생성된 모든 엔티티를 받고 싶을 때 유용하게 사용됩니다.
4

특정 엔티티에 접근하여 모델을 받은 뒤, 해당 모델로부터 생성된 모든 엔티티를 받을 수 있습니다.

void GetEntitiesSpawnedByModelIdExample()
{
    local modelId = _EntityService:GetEntityByPath("/maps/map02/npc-5396_1").Model.BaseModelId
    
    local entities = _EntityService:GetEntitiesSpawnedByModelId(modelId)
    
    for i, v in pairs(entities) do
        log(v.Name)
    end
}
GetEntitiesSpawnedByModel()
매개 변수로 전달한 모델로부터 생성된 모든 엔티티를 반환합니다.
많은 엔티티가 배치된 상황에서 동일 모델로부터 생성된 모든 엔티티를 받고 싶을 때 유용하게 사용됩니다.

void GetEntitiesSpawnedByModelExample()
{
    local model = _EntityService:GetEntityByPath("/maps/map02/npc-5396_1").Model
    
    local entities = _EntityService:GetEntitiesSpawnedByModel(model)
    
    for i, entity in pairs(entities) do
        log(entity.Name)
    end
}
GetSameModelEntities(Entity entity)
매개 변수로 전달한 엔티티의 원형 모델로부터 생성된 모든 엔티티를 반환합니다.

void GetSameModelEntitiesExample()
{
    local templateEntity = _EntityService:GetEntityByPath("/maps/map02/npc-5396_1")
    
    local entities = _EntityService:GetSameModelEntities(templateEntity)
    
    for i, entity in pairs(entities) do
        log(entity.Name)
    end
}
GetEntityByTag()
매개 변수로 전달한 태그 값과 일치하는 모든 엔티티를 반환합니다.
태그는 TagComponent를 통해 설정할 수 있습니다. 한 엔티티에 여러 개의 태그를 설정할 수 있는데, 이중 일치하는 태그가 하나라도 있다면 해당 엔티티를 반환합니다.
만일 다수의 엔티티가 같은 태그로 설정되어 있다면, 가장 먼저 찾은 엔티티만 반환합니다. 따라서 GetEntityByTag는 유니크한 태그를 가진 엔티티를 탐색할 때 사용하는 것을 권장합니다.
5

void GetEntityByTagExample()
{
    local entity = _EntityService:GetEntityByTag("FlayingMonster")
    
    log(entity.Name)
}
GetEntitiesByTag()
매개 변수로 전달한 태그 값과 일치하는 모든 엔티티를 반환합니다.
만일 수많은 엔티티가 있는 상황에서 특정 태그 값으로 설정된 엔티티를 모두 받아오고 싶을 때 사용하면 좋습니다.

void GetEntitiesByTagExample()
{
    local monsterEntities = _EntityService:GetEntitiesByTag("Monster")
    
    for i, monsterEntity in pairs(monsterEntities) do
        log(monsterEntity.Name)
    end
}
엔티티 삭제와 유효성 체크
EnitiyService에서는 엔티티를 삭제하는 함수와 엔티티의 삭제 여부, 즉 엔티티가 현재 유효한 상태인지를 체크하는 함수를 함께 제공하고 있습니다.

Destroy()
매개 변수로 전달한 엔티티를 삭제합니다.

void DestroyExample()
{
    local entity = _EntityService:GetEntityByPath("/maps/map01/Monster1_1")
    _EntityService:Destroy(entity)
    
    if isvalid(entity) == false then
        log("Entity is destroyed")
    end
}

꼭 EntityService:Destroy를 사용하지 않고도, 엔티티의 Destroy 함수로 같은 기능을 수행할 수 있습니다.

void DestroyExample()
{
    local entity = _EntityService:GetEntityByPath("/maps/map01/Monster1_1")
    entity:Destroy()
    
    if isvalid(entity) == false then
        log("Entity is destroyed")
    end
}
IsValid()
매개 변수로 전달한 엔티티가 현재 삭제되었는지를 확인하는 함수입니다.
물론 해당 엔티티가 존재하는지는 nil로도 확인할 수 있습니다. 하지만 존재했던 엔티티가 삭제되었는지 nil로 확인하는 것은 다소 불안정하기 때문에 nil보다는 IsValid 함수로 확인하는 것을 권장합니다.

void IsValidExample()
{
    local entity = _EntityService:GetEntityByPath("/maps/map01/Monster1_1")
    _EntityService:Destroy(entity)
    
    if _EntityService:IsValid(entity) == false then
        log("Entity is destroyed")
    end
}

EntityService:IsValid는 isvalid 함수로 대체할 수 있습니다.

void IsvalidExample()
{
    local entity = _EntityService:GetEntityByPath("/maps/map01/Monster1_1")
    _EntityService:Destroy(entity)
    
    if isvalid(entity) == false then
        log("Entity is destroyed")
    end
}
엔티티 생성 삭제 이벤트
엔티티를 생성 또는 삭제할 때, EntityService에서 엔티티 생성 및 삭제 이벤트가 발생합니다.
각 이벤트 핸들러는 스크립트 에디터의 Entity Event Handler에서 추가할 수 있습니다.
6

이벤트 핸들러를 추가한 뒤 이벤트 센더가 EntityService인지 확인합니다.
7


EntityCreateEvent
엔티티가 생성될 때 발생하는 이벤트입니다.
Entity Event Handler에서 핸들러를 추가할 수 있습니다.
이벤트 핸들러의 매개 변수로 이벤트가 전송되며, 이벤트에는 생성된 엔티티가 정보가 포함되어 있습니다.

Method:
[server only]
void OnBeginPlay()
{
    local monsterTemplate = _EntityService:GetEntityByPath("/maps/map01/monster-1")

    -- "spawnedMonster"라는 이름의 몬스터 엔티티 스폰
    _SpawnService:SpawnByEntityTemplate(monsterTemplate, "spawnedMonster", Vector3(0,0,0), true, true, true, true)
}

Event Handler:
[service: EntityService]
HandleEntityCreateEvent (EntityCreateEvent event)
{
    -- Parameters
    local Entity = event.Entity
    --------------------------------------------------------
    
    -- OnBeginPlay에서 생성한 엔티티만 출력하도록 합니다.
    if Entity.Name ~= "spawnedMonster" then
    	return	
    end
    
    log(Entity.Name) -- 'spawnedMonster'로 출력되는지 확인
}
EntityDestroyEvent
엔티티가 삭제될 때 발생하는 이벤트입니다.
Entity Event Handler에서 핸들러를 추가할 수 있습니다.
이벤트 핸들러의 매개 변수로 이벤트가 전송되며, 이벤트에는 삭제 대기 중인 엔티티가 정보가 포함되어 있습니다.

Method:
[server only]
void OnBeginPlay()
{
    local monsterTemplate = _EntityService:GetEntityByPath("/maps/map01/monster-1")
    
    -- "spawnedMonster"라는 이름의 몬스터 엔티티 스폰
    local spawnedEntity = _SpawnService:SpawnByEntityTemplate(monsterTemplate, "spawnedMonster", Vector3(0,0,0), true, true, true, true)
    
    local callBack = function()
    _EntityService:Destroy(spawnedEntity)
    end
    
    _TimerService:SetTimerOnce(callBack, 5) -- 5초 뒤 스폰한 엔티티를 삭제합니다.
}
    
Event Handler:
[service: EntityService]
HandleEntityCreateEvent(EntityCreateEvent event)
{
    -- Parameters
    local Entity = event.Entity
    --------------------------------------------------------
    
    -- OnBeginPlay에서 생성한 엔티티만 출력하도록 합니다.
    if Entity.Name ~= "spawnedMonster" then
    	return	
    end
    
    log("CreatedEntity : "..Entity.Name) -- 'CreatedEntity : spawnedMonster'로 출력되는지 확인
}

[service: EntityService]
HandleEntityDestroyEvent(EntityDestroyEvent event)
{
    -- Parameters
    local Entity = event.Entity
    --------------------------------------------------------
    
    -- OnBeginPlay에서 생성한 엔티티만 출력하도록 합니다.
    if Entity.Name ~= "spawnedMonster" then
    	return	
    end
    
    log("DestroyedEntity : "..Entity.Name) -- 'DestroyedEntity : spawnedMonster'로 출력되는지 확인
}
