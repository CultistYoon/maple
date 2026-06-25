# LocaleDataSet

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「LocaleDataSet」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 11 게임서비스 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
월드의 텍스트 번역 시 필수적으로 사용해야 하는 LocaleDataSet에 대해 알아봅시다.

참고 가이드
로컬라이징의 이해
포맷에 맞게 로컬라이징하기
자동 번역

LocaleDataSet 소개
LocaleDataSet은 번역을 위한 전용 DataSet입니다. LocaleDataSet은 Default, WebSync 두 종류가 있습니다. LocaleDataSet은 Workspace - MyDesk - Create LocaleDataSet에서 Default, WebSync중 하나를 선택해 생성할 수 있습니다.
LocaleDataSet

Default
기본 LocaleDataSet입니다. Key, Source, Note 컬럼이 기본으로 추가되어 있으며 크리에이터가 컬럼을 추가해 번역문을 입력하고 관리할 수 있습니다. Default 종류의 LocaleDataSet은 공식 홈페이지의 번역 관리와 연동되지 않습니다. 열 추가 버튼을 눌러 번역할 수 있는 언어 목록을 선택해 언어 코드를 추가할 수 있습니다. 언어 코드는 중복으로 추가할 수 없습니다.
Default LocaleDataSet는 번역의 양이 많지 않아 메이커에서 직접 번역 관리가 가능한 경우 사용하기 적합합니다.

default

WebSync
WebSync LocaleDataSet은 공식 홈페이지의 번역 관리에서 번역한 내용을 진행하고, 메이커의 LocaleDataSet 에디터에서 연동해 확인할 수 있는 LocaleDataSet입니다. 마지막으로 편집한 시점을 저장해 공식 홈페이지의 번역 관리와 연동합니다.
WebSync LocaleDataSet은 Key, Source, Note 컬럼만 편집할 수 있으며, 메이커에서 새로운 컬럼을 추가할 수 없습니다. 번역을 동기화하면 수정 불가능한 컬럼이 자동으로 추가됩니다.
WebSync LocaleDataSet는 월드를 제작하는 멤버 수가 많아 메이커에 직접적으로 접근하는 사람 수 관리가 필요하거나, 번역 양이 많을 때 사용하기 적합힙니다.

WebSync

LocaleDataSet 에디터
[object Object]

번호	설명
1	컬럼 셀
각 열의 데이터명, 즉 컬럼 명을 정의합니다. 기본 고정 컬럼 셀은 삭제가 불가능합니다
Key: 식별자 키입니다. 중복된 Key를 사용할 수 없습니다.
Source: 원본 언어, 원본 내용
Note: 번역자에게 제공할 추가 정보를 입력합니다. 해당 정보는 공식 홈페이지 번역 관리에서 확인할 수 있습니다.
2	셀
각 셀은 인풋 텍스트 필드로 각 열의 정의에 적합한 데이터 값을 입력합니다. 입력한 데이터 값은 모두 스트링으로 저장됩니다.
3	행 추가 버튼
버튼을 누르면 행 끝에 새로운 행을 추가합니다.
4	열 추가 버튼
버튼을 누르면 열 끝에 새로운 행을 추가합니다. LocaleDataSet이 Default인 경우 번역할 언어를 선택해 언어 코드를 추가할 수 있고, WebSync인 경우 비활성화 됩니다.
5	Sync 버튼
공식 홈페이지의 번역 관리의 번역문을 연동합니다. Sync 버튼을 눌러 연동하면, 에디터에 컬럼이 추가됩니다. 추가된 컬럼은 메이커에서 할 수 없습니다.
웹에서 데이터 가져오기
Google SpreadSheet의 데이터를 가져올 수 있습니다.
Google SpreadSheet에서 데이터를 작성한 후 해당 데이터의 URL을 팝업창에 넣어주면 현재 열려있는 데이터에 Google SpreadSheet의 데이터를 덮어씌웁니다. 단, Google SpreadSheet의 URL은 웹에 게시한 URL만 사용할 수 있습니다.
Import 기능을 사용할 때는 LocaleDataSet 형식에 맞춰 Key, Source, Note 순으로 머릿글 행이 채워져 있어야 합니다. 그 외 다른 데이터는 모두 삭제된 채로 Import합니다.
NO_05_1
CSV 파일 불러오기
컴퓨터에 저장된 CSV 파일을 가져와 현재 데이터에 덮어씌울 수 있습니다. utf-8로 저장된 CSV 파일만 정상적으로 가져올 수 있습니다.
불러오기 기능을 사용할 때는 LocaleDataSet 형식에 맞춰 Key, Source, Note 순으로 머릿글 행이 채워져 있어야 합니다. 그 외 다른 데이터는 모두 삭제된 채로 데이터를 가져옵니다.
CSV 파일 내보내기
메이커의 LocaleDataSet을 CSV 파일로 내보내어 컴퓨터에 저장할 수 있습니다.
번역 관리
메이커에서 생성한 WebSync 타입의 LocaleDataSet은 공식 홈페이지에서 번역할 수 있습니다. 또한 번역 관리에서 번역한 내용을 메이커의 LocaleDataSet 에디터에 연동할 수 있습니다.
번역 관리는 공식 홈페이지 - 월드 만들기 - 크리에이터의 제작 월드 - 번역 관리 - 월드 콘텐츠에 있습니다. 메이플스토리 월드는 현재 한국어, 영어 번역만 지원하고 있습니다.

WebLocalizing

번호	설명
1	월드 콘텐츠
메이커에서 생성한 LocaleDataSet의 목록입니다.
2	Sync UP
버튼을 눌러, 메이커에서 생성한 LocaleDataSet의 정보를 최신화할 수 있습니다.
3	검색창
Key, Source, Note를 기준으로 번역문을 검색할 수 있습니다.
4	번역문
Key, Source, Note 정보를 함께 확인하고, 번역할 수 있습니다. [저장] 버튼을 눌러 번역을 저장할 수 있습니다. 메이커에 번역을 연동 시킬 때는 메이커에서 [Sync] 버튼을 눌러야합니다.
