# DataStorage 사용량 제한 알아보기

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「DataStorage 사용량 제한 알아보기」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 08 데이터 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
DataStorage를 기준치 이상으로 사용할 경우 크리티컬 리포트에 기록됩니다. 향후 기준치 이상 사용할 수 없도록 제한이 도입될 예정입니다. 크리에이터는 데이터 사용량을 사전에 점검하기를 권장합니다.
출시된 월드에서만 DataStorage 사용량이 제한됩니다.

데이터 요청과 Credit 소모
데이터 사용량은 크리에이터가 제작한 월드의 월드 인스턴스 전체를 한 번에 계산해 적용됩니다.
DataStorage류의 함수는 기본적으로 요청(Request) 1개 당 1개의 Credit을 사용합니다. 그러나 요청 1개의 크기가 크면 여러 개의 Credit을 사용할 수도 있습니다. 또한 Credit 소모 기준은 FunctionGroup에 따라 다릅니다.
Credit에 대해 좀 더 알고 싶다면 DataStorage 사용량 제한 활용하기를 참고하세요.

FunctionGroup
FunctionGroup은 Credit을 공유하는 함수를 구분하는 기준입니다.

List DataStorage
DataStorage의 목록을 가져오는 함수들의 그룹입니다. DataStorageService의 GetGlobalDataStoragePagesAndWait, GetUserDataStoragePagesAndWait 등이 있습니다.

Delete DataStorage
DataStorage를 제거하는 함수들의 그룹입니다. DataStorageService의 DeleteGlobalDataStorageAndWait, DeleteUserDataStorageAndWait 등이 있습니다.

List Sorted
정렬된 값 목록을 가져오는 함수들의 그룹입니다. SortableDataStorage의 GetSortedAndWait, GetPagesAndWait 등이 있습니다.

List
목록을 가져오는 함수들의 그룹입니다. GlobalDataStorage의 GetPagesAndWait, GetVersionsAndWait 등이 있습니다.

Delete
값을 제거하는 함수들의 그룹입니다. GlobalDataStorage의 DeleteAndWait, BatchDeleteAndWait 등이 있습니다.

Get
값을 가져오는 함수들의 그룹입니다. GlobalDataStorage의 GetAndWait, BatchGetAndWait 등이 있습니다.

Set
값을 저장하는 함수들의 그룹입니다. GlobalDataStorage의 SetAndWait, UpdateAndWait, SortableDataStorage의 IncreaseAndWait 등이 있습니다.

None
데이터베이스에 요청하지 않는 함수는 None입니다.

FunctionGroup 안내
Type	Functions	FunctionGroup
DataStorageService	DeleteCreatorDataStorageAndWait	Delete DataStorage
DeleteCreatorDataStorageAsync	Delete DataStorage
DeleteGlobalDataStorageAndWait	Delete DataStorage
DeleteGlobalDataStorageAsync	Delete DataStorage
DeleteSortableDataStorageAndWait	Delete DataStorage
DeleteSortableDataStorageAsync	Delete DataStorage
DeleteUserDataStorageAndWait	Delete DataStorage
DeleteUserDataStorageAsync	Delete DataStorage
GetAndWait	Get
GetAsync	Get
GetCreatorDataStorage	None
GetDataStorage	None
GetGlobalDataStorage	None
GetGlobalDataStoragePagesAndWait	List DataStorage
GetGlobalDataStoragePagesAsync	List DataStorage
GetSortableDataStorage	None
GetSortableDataStoragePagesAndWait	List DataStorage
GetSortableDataStoragePagesAsync	List DataStorage
GetUserDataStorage	None
GetUserDataStoragePagesAndWait	List DataStorage
GetUserDataStoragePagesAsync	List DataStorage
SetAndWait	Set
SetAsync	Set
DataStorage 공통	BatchDeleteAndWait	Delete
BatchDeleteAsync	Delete
BatchGetAndWait	Get
BatchGetAsync	Get
BatchGetByInfoAndWait	Get
BatchGetByInfoAsync	Get
BatchSetAndWait	Set
BatchSetAsync	Set
BatchSetByInfoAndWait	Set
BatchSetByInfoAsync	Set
DeleteAndWait	Delete
DeleteAsync	Delete
GetAndWait	Get
GetAsync	Get
GetByInfoAndWait	Get
GetByInfoAsync	Get
GetVersionsAndWait	List
GetVersionsAsync	List
SetAndWait	Set
SetAsync	Set
SetByInfoAndWait	Set
SetByInfoAsync	Set
TransactSetAsync	Set
TransactSetAndWait	Set
TransactSetByInfoAsync	Set
TransactSetByInfoAndWait	Set
TransactDeleteAsync	Delete
TransactDeleteAndWait	Delete
GlobalDataStorage, UserDataStorage, CreatorDataStorage	UpdateAndWait	Set
UpdateAsync	Set
UpdateByInfoAndWait	Set
UpdateByInfoAsync	Set
GetPagesAndWait	List
GetPagesAsync	List
SortableDataStorage	GetSortedAndWait	List Sorted
GetSortedAsync	List Sorted
IncreaseAndWait	Set
IncreaseAsync	Set
GetPagesAndWait	List Sorted
GetPagesAsync	List Sorted
