# TargetUserSync와 프로퍼티 동기화 최적화

<!-- 출처: reference/TaskWiki.md · 문서 #170 -->


학습 과정 소개
프로퍼티 동기화 방식 중 하나인 TargetUserSync에 대해 알아봅니다.

참고 가이드
프로퍼티

프로퍼티 동기화

서버와 클라이언트

TargetUserSync 알아보기
TargetUserSync는 Sync 프로퍼티 동기화를 좀 더 특정해 최적화하는 방식입니다. TargetUserSync는 플레이어가 스스로 조작하는 PlayerEntity에 포함된 컴포넌트의 프로퍼티만을 대상으로 동기화합니다. 서버에서 프로퍼티 값이 변경되었다면 프로퍼티 값이 변경된 플레이어 엔티티를 조작할 수 있는 유저에게만 프로퍼티 값을 동기화해줍니다.
TargetUserSync는 다른 유저의 정보를 참조할 필요 없는 값인 경우에 사용하는 것이 좋습니다. 개인 재화, 업적, 소모품 같은 개인의 데이터가 이에 해당합니다.
TargetUserSync 프로퍼티를 PlayerEntity가 아닌 다른 Entity의 컴포넌트에서 사용한다면 TargetUserSync는 정상적으로 동작하지 않습니다. 이 경우 None 프로퍼티와 동일하게 동작합니다

Tip.
TargetUserSync는 접속한 Client와 해당 Client가 조작하는 PlayerEntity를 기준으로 작동합니다. 즉 Entity에 적용되는 Component Script에서만 작동하며 아래 Script의 프로퍼티에서는 TargetUserSync를 사용할 수 없습니다.

EventType, ItemType, BTNodeType, StateType, StructType, Logic

TargetUserSync 설정
TargetUserSync는 프로퍼티의 동기화 설정 부분에서 설정할 수 있습니다. 동기화가 가능한 타입은 Sync와 동일합니다.

동기화 가능한 타입: string, integer, number, boolean, SyncTable< v >, SyncTable< k,v >, Vector2, Vector3, Vector4, Color, Entity, Component, EntityRef, ComponentRef

TargetUserSync1

한 Component에서 Sync와 TargetUserSync를 함께 쓰는 경우도 가능합니다. Sync 프로퍼티와 마찬가지로 OnSyncProperty를 통해 TargetUserSync가 변화되는 시점을 확인할 수 있습니다.
TargetUserSync2

Sync와 TargetUserSync의 차이점
Sync로 설정한 프로퍼티의 경우 서버에서 프로퍼티 값을 변경하면, 서버에서 클라이언트 방향으로 해당 엔티티를 가진 맵에 있는 모든 유저에게 값을 동기화합니다. 만약 실시간으로 다른 유저의 정보를 확인하고 처리하는 월드를 만든다면 Sync로 설정한 프로퍼티를 사용할 수 있습니다. 그러나 Sync로 설정한 프로퍼티 값의 변화는 맵의 모든 유저에게 동기화되므로 최적화를 고려해 사용해야 합니다.

Sync 방식
모든 플레이어 엔티티에 아래와 같은 컴포넌트를 추가했다고 생각해봅시다. meso 프로퍼티는 유저의 재화를 관리하기 위한 프로퍼티입니다. 따라서 다른 유저의 meso 값을 몰라야 합니다.

Property:
[Sync]
integer meso = 0

Method:
[server only]
void IncreaseMeso()
{
	self.meso += 1
}
A, B client가 같은 맵에 접속해 있다면 각각 서버와 클라이언트에서 보는 엔티티들의 프로퍼티 값은 아래와 같습니다.

TargetUserSync1

이때 PlayerEntity A의 InscreaseMeso()가 호출되어 A 엔티티의 변경된 meso 프로퍼티 값이 동기화되면 모든 Client에서 PlayerEntityA 값이 변경됩니다. Sync 프로퍼티는 같은 맵에 있는 모든 Client의 PlayerEntityA에게 제한 없이 변경된 meso 값을 동기화하기 때문입니다.
모든 Client에게 동기화하게 되면, ClientB는 불필요한 프로퍼티 동기화 처리로 인해 연산과 패킷 낭비가 발생합니다. 또한 서버는 불필요한 패킷을 모든 Client로 전송해야하므로 패킷을 낭비하게 됩니다.

TargetSyncProperty2

TargetUserSync 방식
meso 프로퍼티를 TargetUserSync로 변경한 뒤 서버에서 PlayerEntity A의 IncreaseMeso()를 호출하면, PlayerEntity A의 조작 제어권이 있는 Client A에만 meso 값이 동기화됩니다. Client B의 PlayerEntity A에는 변경이 일어나지 않는, None과 동일하게 처리됩니다.

Property:
[TargetUserSync]
integer meso = 0

Method:	
[server only]
void IncreaseMeso()
{
	self.meso += 1
}
