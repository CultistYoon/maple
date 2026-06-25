# VS Code: Debugger for mLua

<!-- 출처: reference/TaskWiki.md · 문서 #25 -->


학습 과정 소개
mLua Debugger VS Code Extension을 설치해 제작 중인 월드를 VS Code에서 디버깅해봅시다.

참고 가이드
스크립트 디버그

LocalWorkspace

mLua VS Code Extension

Debugger for mLua Extension
Debugger for mLua는 로컬워크스페이스를 사용하는 월드의 mLua 파일을 VS Code에서 디버그할 수 있도록 지원하는 확장 프로그램입니다. mLua Extension 설치와 메이플스토리 월드의 LocalWorkspace 연동 기능이 활성화되어 있어야 Debugger for mLua를 사용할 수 있습니다.

Debugger for mLua Extension 설치
Extensions를 선택하고 Debugger for mLua를 검색해 설치합니다.

월드의 로컬 폴더에서 .vscode 폴더와 launch.json 파일이 있는지 확인합니다.

launch.json 파일을 열어 아래와 같이 입력합니다. configurations이 아래와 같이 작성되어야 VS Code의 Run and Debug 탭이 활성화됩니다.

{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "MSW Attach",
            "type": "msw",
            "request": "attach"
        }
    ]
}
디버그하기
Debugger for mLua는 MSW에 VS Code Debugger를 연결하는 방식입니다.
그러므로 메이커에서 먼저 디버그 플레이를 실행한 뒤 VS Code Debugger를 연결해 사용해야 합니다. 디버그 연결 상태는 메이커의 Console에서 확인할 수 있습니다.

디버깅할 월드를 메이커에서 엽니다.

메이커의 디버깅 시작 버튼을 눌러 플레이합니다.
[object Object]

VS Code에서 Run and Debug를 선택합니다.
[object Object]

이전에 정의한 구성 정보의 이름을 선택한 뒤 실행 버튼을 누릅니다.
[object Object]

VS Code Debugger 연결이 완료되면 메이커의 Console에서 확인할 수 있습니다.
[object Object]

Run and Debug
중단점
중단점은 디버그 실행을 일시 중단할 지점입니다. 중단점은 여러 곳에 설정할 수 있고, 자유롭게 제거할 수도 있습니다. 중단점이 설정된 파일과 라인을 BREAKPOINTS에서 확인할 수 있습니다.

중단점 지정, 해제
중단점을 지정하거나 해제하는 방법은 두 가지입니다.

중단점을 지정할 라인을 선택하고 F9 키를 눌러 중단점을 추가하거나 해제합니다.

코드 라인 영역을 눌러 중단점을 추가하거나 해제합니다.

[object Object]

VARIABLES
Scope에 따른 변수 정보를 확인할 수 있습니다.
[object Object]

WATCH
직접 Expression을 작성하고 값을 확인할 수 있습니다.
[object Object]

CALL STACK
호출 스택을 확인할 수 있습니다.
[object Object]

BREAKPOINTS
중단점이 설정된 파일의 경로와 라인을 확인할 수 있습니다. 목록에서 중단점을 선택하면 해당하는 중단점으로 이동합니다.
[object Object]

ENVIRONMENT
현재 실행 공간을 확인할 수 있습니다.
[object Object]

심볼에 할당된 값 확인
심볼에 할당된 값은 해당 심볼에 마우스를 올렸을 때 나타나는 툴팁으로 확인할 수 있습니다.

디버그 툴바
디버그를 시작하면, 툴바가 VS Code 상단에 나타납니다. 월드 디버그 실행 중 중단점에서 플레이가 멈추면 툴바의 실행 버튼들이 활성화됩니다. 디버그를 위해 코드를 계속 실행하고 싶다면 버튼을 눌러 코드를 계속 실행할 수 있습니다.
코드 실행을 통해 프로시저 단위로 코드의 상태나 흐름을 파악해 월드의 문제를 찾고 해결할 수 있습니다.

[object Object]

번호	기능	설명
[object Object]	계속 실행	현재의 중단점에서 다음 중단점이 있는 코드 라인까지 실행합니다.
[object Object]	프로시저 단위 실행	코드를 한 줄씩 실행합니다. 포커싱된 라인에 함수가 있을 때, 그 함수를 실행한 것으로 간주하고 다음 줄로 넘어갑니다
[object Object]	아래로 코드 실행	포커싱 된 라인에 함수가 있을 때 해당 함수 내부로 들어가 함수 내 코드를 한 줄씩 실행합니다.
[object Object]	위로 코드 실행	현재 실행 중인 함수 호출을 완료하고, 해당 함수를 호출한 위치로 이동합니다.
[object Object]	재시작	현재 디버그 실행을 중단하고, 디버그 시작점으로 돌아가 디버그를 다시 실행합니다.
[object Object]	중단	디버거 실행을 중단합니다.
