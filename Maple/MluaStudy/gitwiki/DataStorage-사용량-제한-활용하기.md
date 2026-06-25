# DataStorage 사용량 제한 활용하기

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「DataStorage 사용량 제한 활용하기」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 08 데이터 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
DataStorage를 사용할 때는 제한 용량과 Credit 제한을 확인하고 용량에 맞게 사용해야 합니다. DataStorage 사용량 제한에 관해 알아보겠습니다.

DataStorage 제한 용량
DataStorage의 용량 제한은 다음과 같습니다. 문자열 값 크기는 UTF-8 인코딩을 통해 Byte 배열로 변환했을 때의 Byte 수로 계산됩니다.

구분	제한 용량
DataStorage name	1 ~ 64 byte
DataStorage key	1 ~ 100 byte
DataStorage tag	0 ~ 64 byte
DataStorage version	0 ~ 64 byte
update	0 ~ 50,000 byte
set	0 ~ 300,000 byte
Credit
Credit이란 데이터베이스 요청 수 제한을 위해 계산되는 단위를 의미합니다. Credit의 최솟값은 1입니다. Credit은 실제 데이터베이스에 요청하는 경우에만 소모되는 특징이 있습니다.
FunctionGroup별로 매분 지급되는 Credit 수, 누적되는 Credit 수, 데이터베이스 요청 시 소모되는 Credit 수가 다릅니다. 함수별로 속하는 FunctionGroup은 DataStorage 사용량 제한 알아보기에서 확인할 수 있습니다.

FunctionGroup	분당 지급되는 Credit	최대 누적 가능한 Credit	요청 시 소모되는 Credit
List DataStorage	10 + (접속자 수 * 2)	분당 지급되는 Credit * 2	1
Delete DataStorage	10 + (접속자 수 * 2)	분당 지급되는 Credit * 2	1
List Sorted	50 + (접속자 수 * 2)	분당 지급되는 Credit * 2	1
List	10 + (접속자 수 * 2)	분당 지급되는 Credit * 2	1
Delete	50 + (접속자 수 * 2)	분당 지급되는 Credit * 2	1
Get	100 + (접속자 수 * 10)	분당 지급되는 Credit * 2	4,000byte당 1
Set	100 + (접속자 수 * 10)	분당 지급되는 Credit * 2	4,000byte당 1
Byte 크기에 따른 Credit 소모
0에서 4000 Byte는 1 Credit을 사용합니다. 또한 존재하지 않는 값을 조회했을 때도 Credit이 소모됩니다.
문자열 값 크기는 UTF-8 인코딩을 통해 Byte 배열로 변환했을 때의 Byte 수로 계산됩니다.

Tip.
Key, Tag, Version 크기는 Credit에 영향을 끼치지 않습니다.

batch 계열 함수의 Credit 소모
BatchGetAsync 같은 Batch 계열 함수는 여러 키를 한 번에 접근할 수 있습니다. 이 함수들은 요청하는 키 수에 따라 Credit 소모 개수가 정해집니다.
두 값을 요청한 경우라도, 요청한 Byte 수에 따라 소모되는 Credit 수가 달라집니다. 예를 들어 요청한 두 값의 크기가 각 2,000 Byte라면 총 2 Credit을 소모합니다. 반면에, 두 값의 크기가 각 4,000 Byte, 4,500 Byte라면 4,000Byte인 값은 1 Credit을 소모하고 4,500 Byte인 값은 2 Credit을 소모합니다.
Batch 계열 함수를 사용할 때는 Credit이 소모되는 시점을 염두에 두어야 합니다. Credit은 데이터베이스에 실제로 요청하는 시점에 소모됩니다. 만약 BatchGetAndWait() 함수로 50개의 Key를 넘겼다면 호출 한 번에 50개 값에 대한 Credit이 소모되지 않습니다. 호출 즉시에는 25개 값만큼의 Credit이 소모되고, 이후 반환되는 Page를 통해 MoveToNextPageAndWait()를 통해 다음 Page로 이동할 때 나머지 25개 값만큼의 Credit이 소모됩니다.

Tip.
BatchSetAndWait() 함수는 넘긴 키 개수만큼을 곧바로 요청합니다.

Transact 계열 함수의 Credit 소모
Transact 계열 함수는 batch 계열 함수와 비슷하게 동작합니다. 다만 트랜잭션 보장을 위해 더 많은 처리가 필요하므로 batch 계열 함수보다 2배의 Credit을 소모합니다.

Credit을 소모하지 않는 함수
어떤 함수를 사용했지만, 이미 다른 함수가 Page를 불러왔을 때는 Credit을 소모하지 않습니다. 대표적으로 MoveToNextPageAndWait(), LoadNextPageAndWait() 함수는 상황에 따라 Credit을 소모하지 않습니다.
예를 들어, GlobalDataStoragePages의 LoadNextPageAndWait() 함수를 사용해 다음 Page를 미리 불러오고 MoveToNextPageAndWait()함수를 호출하면 이미 Page를 불러왔기 때문에 데이터베이스에 요청하지 않습니다. 그러므로 Credit은 LoadNextPageAndWait()함수를 호출할 때만 소모하게 됩니다.
