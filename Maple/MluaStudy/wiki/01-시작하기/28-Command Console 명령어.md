# Command Console 명령어

<!-- 출처: reference/TaskWiki.md · 문서 #27 -->


학습 과정 소개
Command Console 창에서 사용할 수 있는 명령어들을 알아봅시다.

help
사용할 수 있는 명령어와 설명을 출력합니다.

help [command=all] [-out stream] [-err stream]
매개 변수
command: 설명을 출력할 명령어의 이름입니다. all을 입력하면 모든 명령어의 설명이 출력됩니다.

옵션
-out: 결과를 출력할 스트림을 설정합니다.

stream: 출력할 스트림입니다.

-err: 에러를 출력할 스트림을 설정합니다.

stream: 출력할 스트림입니다.

예제
help findentity
echo
입력된 메시지를 결과창에 그대로 출력합니다.

echo message [-out stream] [-err stream]
매개 변수
message: 출력할 메시지입니다.

옵션
-out: 결과를 출력할 스트림을 설정합니다.

stream: 출력할 스트림입니다.

-err: 에러를 출력할 스트림을 설정합니다.

stream: 출력할 스트림입니다.

예제
echo "test"
export
지정한 경로로 원하는 파일을 내보냅니다. 스크립트, 코드블럭, 데이터셋, 유저 데이터셋 엔트리만 내보낼 수 있습니다.

export src_path dest_path [-out stream] [-err stream]
매개 변수
src_path: 내보낼 엔트리의 워크스페이스 경로입니다. 경로는 MyDesk부터 시작합니다.

dest_path: 내보낸 엔트리를 저장할 경로입니다.

옵션
-out: 결과를 출력할 스트림을 설정합니다.

stream: 출력할 스트림입니다.

-err: 에러를 출력할 스트림을 설정합니다.

stream: 출력할 스트림입니다.

예제
export "MyDesk/NewComponent" "C:\TestFolder"
import
지정한 경로로 파일을 불러옵니다.

import src_path [dest_path=MyDesk] [-overwrite] [-out stream] [-err stream]
매개 변수
src_path: 가져올 엔트리의 경로입니다.

dest_path: 가져온 파일을 저장할 워크스페이스 경로입니다. 경로는 MyDesk부터 시작합니다.

옵션
-overwrite: 덮어쓰기를 허용합니다.

-out: 결과를 출력할 스트림을 설정합니다.

stream: 출력할 스트림입니다.

-err: 에러를 출력할 스트림을 설정합니다.

stream: 출력할 스트림입니다.

예제
import "C:\TestFolder/NewComponent.xml" "MyDesk/NewFolder"
findentity
하이어라키에서 특정 엔티티를 찾습니다. 모든 맵의 엔티티를 대상으로 찾을 수 있습니다.

findentity [-path path] [-name name [match_type=contains] [comparison_type=ordinal]] [-visibleonly] [-enableonly] [-modelonly] [-model_name name [match_type=contains] [comparison_type=ordinal]] [-model_id id] [-out stream] [-err stream]
옵션
-path: 엔티티를 찾을 경로로 지정합니다

path: 엔티티를 찾을 경로입니다.

-visibleonly: Visible인 엔티티만 찾습니다.

-enableonly: Enable인 엔티티만 찾습니다.

-modelonly: 모델을 확장한 엔티티만 찾습니다.

-name: 지정한 이름이 포함된 엔티티를 찾습니다.

name: 찾을 이름입니다.

match_type: 이름을 찾는 방식입니다. contains, equals, regex 중 하나를 사용합니다.

contains: 지정한 이름이 포함된 모델을 확장한 엔티티를 찾습니다.

equals: 지정한 이름과 동일한 모델을 확장한 엔티티를 찾습니다.

regex: 정규식을 사용하여 일치하는 엔티티를 찾습니다.

comparison_type: 이름을 비교하는 방식입니다. ordinal, ordinal_ignorecase 중 하나를 사용할 수 있습니다.

ordinal 바이트 비교를 수행합니다.

ordinal_ignorecase: 바이트 비교를 수행하고 대소문자 비교를 무시합니다.

-model_name: 지정한 이름이 포함된 모델을 확장한 엔티티를 찾습니다.

name: 찾을 이름입니다.

match_type: 이름을 찾는 방식입니다. contains, equals, regex 중 하나를 사용할 수 있습니다.

contains: 지정한 이름이 포함된 모델을 확장한 엔티티를 찾습니다.

equals: 지정한 이름과 동일한 모델을 확장한 엔티티를 찾습니다.

regex: 정규식을 사용하여 일치하는 엔티티를 찾습니다.

comparison_type: 이름을 비교하는 방식입니다. ordinal, ordinal_ignorecase 중 하나를 사용할 수 있습니다.

ordinal: 바이트 비교를 수행합니다.

ordinal_ignorecase: 바이트 비교를 수행하며 대소문자 비교를 무시합니다.

-model_id: 모델 id가 일치하는 모델을 찾습니다.

id : 찾을 모델의 id입니다.

-out: 결과를 출력할 스트림을 설정합니다.

stream: 출력할 스트림입니다.

-err: 에러를 출력할 스트림을 설정합니다.

stream: 출력할 스트림입니다.

예제
findentity -path "World/ui/DefaultGroup" -enableonly -name "Button" contains ordinal_ignorecase -out $"C:\TestFolder/result.txt"
findcomponent
하이어라키에 있는 특정 컴포넌트를 찾습니다. 모든 맵을 대상으로 찾을 수 있습니다.

findcomponent [-path path] [-enableonly] [-name name [match_type=contains] [comparison_type=ordinal]] [-out stream] [-err stream]
옵션
-path 컴포넌트를 찾을 경로를 지정합니다.

path : 컴포넌트를 찾을 경로입니다.

-enableonly: Enable이 켜져있는 컴포넌트만 찾습니다.

-name: 지정한 이름이 포함된 컴포넌트를 찾습니다.

name: 찾을 이름입니다.

match_type: 이름을 찾는 방식입니다. contains, equals, regex 중 하나를 사용할 수 있습니다.

contains: 지정한 이름이 포함된 이름의 컴포넌트를 찾습니다.

equals: 지정한 이름과 동일한 이름의 컴포넌트를 찾습니다.

regex: 정규식을 사용하여 일치하는 이름의 컴포넌트를 찾습니다.

comparison_type: 이름을 비교하는 방식입니다. ordinal, ordinal_ignorecase 중 하나를 사용할 수 있습니다.

ordinal: 바이트 비교를 수행합니다.

ordinal_ignorecase: 바이트 비교를 수행하며 대소문자 비교를 무시합니다.

-out: 결과를 출력할 스트림을 설정합니다.

stream: 출력할 스트림입니다.

-err: 에러를 출력할 스트림을 설정합니다.

stream: 출력할 스트림입니다.

예제
findcomponent -path "World/ui/DefaultGroup" -name "ButtonComponent" equals ordinal_ignorecase -out $"C:\TestFolder/result.txt"
findproperty
하이어라키에 있는 특정 프로퍼티를 찾습니다. 모든 맵을 대상으로 찾을 수 있습니다.

findproperty [-path path] [-name name [match_type=contains] [comparison_type=ordinal]] [-component_name name [match_type=contains] [comparison_type=ordinal]] [-out stream] [-err stream]
옵션
-path: 프로퍼티를 찾을 경로를 지정합니다.

path: 프로퍼티를 찾을 경로입니다.

-name: 지정한 이름이 포함된 프로퍼티를 찾습니다.

name: 찾을 이름입니다.

match_type: 이름을 찾는 방식입니다. contains, equals, regex 중 하나를 사용할 수 있습니다.

contains: 지정한 이름이 포함된 이름의 프로퍼티를 찾습니다.

equals: 지정한 이름과 동일한 이름의 프로퍼티를 찾습니다.

regex: 정규식을 사용하여 일치하는 이름의 프로퍼티를 찾습니다.

comparison_type: 이름을 비교하는 방식입니다. ordinal, ordinal_ignorecase 중 하나를 사용할 수 있습니다.

ordinal: 바이트 비교를 수행합니다.

ordinal_ignorecase: 바이트 비교를 수행하며 대소문자 비교를 무시합니다.

-component_name: 지정한 이름이 포함된 컴포넌트의 프로퍼티를 찾습니다.

name: 찾을 이름입니다.

match_type: 이름을 찾는 방식입니다. contains, equals, regex 중 하나를 사용할 수 있습니다.

contains: 지정한 이름이 포함된 이름의 컴포넌트를 찾습니다.

equals: 지정한 이름과 동일한 이름의 컴포넌트를 찾습니다.

regex: 정규식을 사용하여 일치하는 이름의 컴포넌트를 찾습니다.

comparison_type: 이름을 비교하는 방식입니다. ordinal, ordinal_ignorecase 중 하나를 사용할 수 있습니다.

ordinal: 바이트 비교를 수행합니다.

ordinal_ignorecase: 바이트 비교를 수행하며 대소문자 비교를 무시합니다.

-out: 결과를 출력할 스트림을 설정합니다.

stream: 출력할 스트림입니다.

-err: 에러를 출력할 스트림을 설정합니다.

stream: 출력할 스트림입니다.

예제
findproperty -name "Color" -component_name "SpriteGUIRendererComponent"
play
월드를 플레이합니다. 디버그 모드로 실행하거나 가상 플레이어를 추가할 수 있습니다.

play [-debug] [-virtual_player player_number] [-out stream] [-err stream]
옵션
-debug: 디버그 모드로 플레이합니다.

-virtual_player: 가상 플레이어를 추가합니다.

player_number: 추가할 가상 플레이어 수 입니다.

-out: 결과를 출력할 스트림을 설정합니다.

stream: 출력할 스트림입니다.

-err: 에러를 출력할 스트림을 설정합니다.

stream: 출력할 스트림입니다.

예제
play -debug -virtual_player 3
