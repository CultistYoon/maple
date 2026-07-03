# Data DB 저장 및 불러오기

<!-- 출처: reference/TaskWiki.md · 문서 #142 -->


학습 과정 소개
게임 중 변경된 데이터 값을 GlobalDataStorage에 저장하고 불러오는 방법에 대해 알아봅니다.

Data 생성 및 불러오기
GlobalDataStorage는 데이터의 저장과 불러오기를 할 수 있는 "보관소"라 할 수 있습니다. 우리는 데이터베이스에서 데이터를 저장하거나 불러올 일이 있을 때 이 "보관소"를 이용하면 됩니다.
GlobalDataStorage는 _DataStorageService:GetGlobalDataStorage를 통해 생성하거나 불러오기가 가능합니다. GetGlobalDataStorage에 매개 변수로 넘겨지는 name 값에 따라 GlobalDataStorage를 새로 생성하여 리턴하거나 이미 해당 name 값이 등록되어 있는 경우 이전에 생성했던 GlobalDataStorage를 리턴합니다. GlobalDataStorage는 name 값에 따라 여러 개로 생성할 수 있기 때문에, 데이터의 속성이나 용도에 따라 GlobalDataStorage를 구분하여 저장할 수 있습니다. 추가로 _DataStorageService:GetGlobalDataStorage는 Server Only 함수이므로, 데이터 불러오기는 서버 공간에서 하는 것이 좋습니다.

void FunctionExample()
{
    --데이터를 저장하기 위해 MyData라는 GlobalDataStorage를 생성
    local MyData = _DataStorageService:GetGlobalDataStorage("MyData") 
}
Data 저장하기
데이터의 저장은 GlobalDataStorage의 SetAsync를 활용해 할 수 있습니다.
SetAsync는 매개 변수로 key와 value, 그리고 콜백 함수를 받는데, 저장할 데이터가 있으면 key와 value 매개 변수로 값을 넘겨 저장하게 됩니다.
key는 매번 변경되어 저장되는 value 값을 불러오기 위한 용도로 사용됩니다. 따라서 key 값으로는 프로퍼티 명이나 혹은 저장된 value 값이 의미하는 것으로 입력해 주는 것이 좋습니다. 예를 들어 power라는 프로퍼티(또는 스탯)의 값을 저장한다면 key에는 "Power"를, value에는 Power의 값을 스트링으로 변환하여 입력합니다. 만일 이전에 같은 key 값으로 저장된 적이 있으면, 현재 값을 이전 값에 덮어씌우게 됩니다.

Property: 
[Sync]
number Power = 100
 
Method: 
[server only]
void SetData()
{
     local data = _DataStorageService:GetGlobalDataStorage("data") 
     data:SetAsync("Power", tostring(self.Power), nil) 
     --프로퍼티 Power의 값을 "Power"라는 키로 저장합니다. value값은 string으로 저장합니다.  
}

콜백 함수는 데이터가 저장되었을 때 호출되며, 매개 변수로는 errorCode와 key 값을 넘겨줍니다.
SetAsync를 통한 데이터 저장은 비동기식으로 저장되기 때문에 SetAsync가 실행 중에 값이 저장되지 않습니다. 쉽게 말해 SetAsync는 값을 저장해달라고 요청을 보내는 것이고, 요청받은 DB는 이전에 들어온 요청들부터 순차적으로 저장을 하기 때문에 저장을 요청한 값이 실제로 어느 시점에 저장될지는 보장되지 않습니다. 이와 같은 경우에는 SetAsync 호출 뒤에 처리를 추가하는 것이 아니라, 콜백 함수를 매개 변수로 넘겨서 값이 저장된 시점에서의 처리를 진행하면 됩니다.
콜백 함수의 매개 변수는 errorcode와 key를 받도록 되어있으며, 콜백 함수 호출 시 내부에서 매개 변수로 값을 넘겨줍니다. 만일 콜백 함수를 등록하지 않으려면 nil을 넘겨줍니다.

Property: 
[Sync]
number Power = 100

Method: 
[server only]
void FunctionExample()
{
    -- SetAsync가 끝난 시점의 로그와 콜백 함수의 로그가 찍히는 시점을 비교해봅니다.
    -- 콜백 함수는 실제로 값이 저장되는 시점에 호출되므로, 콜백 함수의 로그가 SetAsync가 완료된 후 찍힌 로그보다 늦게 출력됩니다.
    local data = _DataStorageService:GetGlobalDataStorage("data")
    self.Power = 20
    local callBack = function (errorcode, key)
        log(key.."값이 저장되었다.")
    end
    data:SetAsync("Power", tostring(self.Power), callBack)
    log("SetAsync 완료")
}
Data 불러오기
GetAsync는 데이터를 불러오기 위한 함수로 value 값 저장 시 함께 저장된 key 값을 통해 value 값을 가져옵니다.
이때 GetAsync도 SetAsync와 마찬가지로 key 값에 해당하는 value 값을 요청하게 되는데, 요청한 value 값을 함수 내에서 직접 리턴 받는 것이 아닌 GetAsync에 등록한 콜백 함수의 매개 변수로 key 값과 함께 들어옵니다. 이유는 GetAsync 역시 비동기식으로 동작을 하기 때문에 불러오기 요청을 보냈을 때 value 값을 언제 보내줄지는 보장되지 않기 때문입니다. 따라서 GetAsync는 value 값을 받았을 때의 처리가 꼭 필요하므로, SetAsync와는 달리 콜백 함수의 등록이 필요합니다.

Property: 
[Sync]
number Power = 0
 
Method: 
[server only]
void OnBeginPlay()
{
    local data = _DataStorageService:GetGlobalDataStorage("Data") 
    local callBack = function(errorcode, key, value) 
        if key == "Power" then 
            self.Power = tonumber(value)
        end 
    end 
    data:GetAsync("Power", callBack)
}

만일 key 값으로 저장된 value 값이 없을 때 불러오기를 하면 nil이 들어 옵니다. 따라서 불러오기 했을 때, value 값이 nil인지를 체크해서 저장되지 않은 값에 대한 처리를 할 수 있습니다.

Property: 
[Sync]
number Power = 0
 
Method: 
[server only]
void OnBeginPlay()
{
    local data = _DataStorageService:GetGlobalDataStorage("Data")
    local callBack = function(errorcode, key, value)
        --value가 nil일 경우의 처리를 추가합니다.
        if value == nil then value = 0 end
            if key == "Power" then
                self.Power = tonumber(value)
            end
    end
    data:GetAsync("Power", callBack)
}
데이터 스토리지 초기화
테스트 플레이 중 저장된 데이터는 플레이를 종료해도 사라지지 않고 유지되는데, 이에 대한 초기화는 Setting - 만들기 - 데이터 스토리지 설정에서 할 수 있습니다.
2

참고 가이드
DataStorage 활용하기
