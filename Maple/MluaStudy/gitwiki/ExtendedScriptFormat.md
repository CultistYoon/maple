# ExtendedScriptFormat

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「ExtendedScriptFormat」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 01 시작하기 · 출처: MapleStory Worlds 공식 위키_

---

ExtendedScriptFormat은 프리뷰 기능으로 정식 출시 시 기능이 변경될 수 있습니다.
학습 과정 소개
확장된 스크립트 포맷을 사용하는 방법과 mlua 파일 형식 정의를 알아봅시다.

참고 가이드
공동제작

공동 제작 그룹 멤버의 등급과 권한

WorldConfig

LocaWorkspace

확장된 스크립트 포맷 소개
로컬 워크스페이스의 확장된 스크립트 포맷(UseExtendedScriptFormat)을 활성화하면 메타데이터 파일과 쌍을 이루는 mlua 파일을 생성합니다. 확장된 스크립트 포맷은 Plain Text 형식이므로 파일 공유 도구에서 파일 병합 시 충돌이 발생하더라도 문제 지점을 더욱 수월하게 발견할 수 있습니다.

주의!
UseExtendedScriptFormat은 preview 기능으로 안정성을 보장하지 않습니다. 사용 중 버그가 발생할 수 있으며, 추후 정식 버전 도입 시 preview 기능이 정지될 수도 있습니다. 백업 파일 혹은 백업 월드를 만들어 두는 것을 권장합니다.

확장된 스크립트 포맷 활성화
WorldConfig - LocalWorkspace - UseExtendedScriptFormat를 활성화합니다.
1

LocalWorkspace로 지정한 경로의 폴더에 Environment 폴더와 mlua 파일이 생성된 것을 확인할 수 있습니다.
2

확장된 스크립트 포맷 비활성화
UseExtendedScriptFormat는 한 번 활성화되면 비활성화 상태로 되돌릴 수 없습니다. 로컬 워크스페이스 자체를 비활성화 해야합니다.
로컬 워크스페이스를 비활성화하는 방법은 다음과 같습니다.

로컬 파일을 문제점 이전의 상태로 변경합니다.

메이플스토리 월드 메이커에서 ReimportAll을 선택합니다.

File - Sync To Remote Workspace를 선택해 현재 로컬 파일을 리모트 워크스페이스에 동기화합니다.

로컬 폴더에서 Global - WorldConfig.config 파일을 엽니다.

내용 중 "UseExtendedScriptFormat": true를 "UseExtendedScriptFormat": false로 변경하고, 저장합니다.

메이플스토리 월드 메이커에서 ReimportAll을 다시 선택합니다.

메이커에서 UseExtendedScriptFormat이 비활성화 상태인 것을 확인합니다.

LocalWorkspace를 비활성화합니다.

File - Revisions에서 문제 발생 이전 버전을 선택해 되돌립니다.
3

mlua 파일 소개
mlua 파일은 일정한 형식으로 정의되어 있습니다.

주의!
메이커에서 지원하지 않는 기능을 mlua에서 임의로 사용하는 것은 권장하지 않습니다. 현재는 정상 동작하는 것처럼 보일 지라도 추후에 동작하지 않도록 변경될 수 있으니 주의 바랍니다.

스크립트 엔트리 정의
스크립트 엔트리는 하나의 부모로부터 상속받을 수 있으며, 같은 종류의 스크립트 엔트리끼리만 상속이 가능합니다. 스크립트 엔트리 중 Component, Item, BTNode, State, Logic은 상속 받은 부모의 정보가 필수적입니다.
스크립트 엔트리에서 정의 가능한 스크립트 종류는 아래와 같습니다.

Component

Item

BTNode

State

Logic

Event

Struct

@스크립트 종류
script 이름 extends 상속
end
스크립트 엔트리 정의 예시입니다.

@Component
script NewComponent extends Component
end
프로퍼티 정의
프로퍼티 정의 구성은 다음과 같습니다.

Property 타입 프로퍼티이름 = 기본값
프로퍼티 정의 예시입니다.

Property number NewProperty = 5
메소드 정의
메소드는 정의 구성은 다음과 같습니다.

method 반환타입 메소드이름 (매개변수타입 매개변수이름)
메소드 정의 예시입니다.

method void TestMethod(float parameter)
이벤트 핸들러 정의
이벤트 핸들러는 EventSender Attribute를 필수로 사용합니다.

@EventSender("Self")
handler 핸들러이름(이벤트타입 event)
이벤트 핸들러 정의 예시입니다.

@EventSender("Self")
handler HandleButtonClickEvent(ButtonClickEvent event)
어트리뷰트 정의
어트리뷰트의 매개변수가 필요하지 않은 경우 생략할 수 있습니다.

@이름()
@이름(매개변수)
어트리뷰트 정의 예시입니다.

@EventSender()
@EventSender("Self")
