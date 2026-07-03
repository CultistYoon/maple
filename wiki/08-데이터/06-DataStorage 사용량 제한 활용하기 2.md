# DataStorage 사용량 제한 활용하기 2

<!-- 출처: reference/TaskWiki.md · 문서 #146 -->


학습 과정 소개
DataStorage를 효율적으로 활용하지 않으면 사용량 제한에 도달해 데이터 저장, 조회에 실패해 데이터를 관리에 어려움을 겪을 수 있습니다. DataStorage의 사용량을 효과적으로 관리하는 방법에 대해 알아봅시다.

가이드
DataStorage 사용량 제한 알아보기

DataStorage 사용량 제한 활용하기

효과적으로 DataStorage 사용하기

데이터 저장하지 않기
저장하고자 하는 신규 데이터와 이전 데이터가 동일할 때, SetAndWait, SetAsync 와 같은 Set 함수들을 호출하면 Credit을 소모하게 됩니다.
값이 변경될 때만 DataStorage로 변경 요청을 보내면 Credit을 절약하는데 도움이 됩니다. 예를 들어 특정 유저가 여러 인스턴스에 동시에 접속해서 데이터를 변경하는 경우가 발생하지 않는다면, UserDataStorage에 이 방식을 활용할 수 있습니다.

Tip
다른 월드 인스턴스에서 변경할 가능성이 없는 데이터에 대해서만 월드 인스턴스의 Lua Table에 데이터를 저장하기를 권장합니다.

Property:
[None]
table cache = {}

Method:
[server only]
void TestAndSetData(string key, string value)
{
    local profileCode = self.Entity.PlayerComponent.ProfileCode
    if self.cache[profileCode] ~= nil and self.cache[profileCode][key] == value then
      return
    end
    
    local userDataStorage = _DataStorageService:GetUserDataStorage(profileCode)
    if userDataStorage == nil then
       return
    end
    
    local errorCode = userDataStorage:SetAndWait(key, value)
    if errorCode ~= 0 then
        log("ErrorCode : "..errorCode)
    else
        if self.cache[profileCode] == nil then
            self.cache[profileCode] = {}
        end
        self.cache[profileCode][key] = value
    end
}
더 알아보기
유저가 최초 접속했을 때 GetAndWait을 활용해 데이터를 미리 불러와서 self.cache에 넣어둘 수도 있습니다. 읽기와 쓰기 패턴에 따라 어떤 방식이 유리할지 크리에이터의 월드 특성에 맞게 선택해 사용해야 합니다.
만약, value 자체가 긴 문자열이라면 비교에도 많은 CPU 자원이 필요하므로 비교적 데이터가 작은 경우에 사용하는 것이 유리합니다.
모든 데이터에 캐싱을 적용하면 월드 인스턴스의 메모리가 부족할 수 있으니 읽기와 쓰기가 잦은 핫 데이터에서만 캐싱을 적용하기를 권장합니다.
