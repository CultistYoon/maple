# -*- coding: utf-8 -*-
import os, re

SRC = 'reference/TaskWiki.md'
OUT = 'wiki'
L = open(SRC, encoding='utf-8').read().split('\n')
delim = [i for i, l in enumerate(L) if l.strip() == 'custom custom']  # 0-based
assert len(delim) == 198, len(delim)

# Authoritative titles (read directly from title-lines), index 0..197
TITLES = [
 "Workspace","WorldConfig","Hierarchy","Scene","배경 설정하기","프로퍼티 에디터","모델 에디터",
 "컴포넌트 추가와 삭제","캐릭터 초기 속성 편집","게임 시작 위치 설정","게임 섬네일 변경하기",
 "제작한 월드 불러오기 및 관리","월드 출시하기","유저 피드백 설정하기","리소스 찾기","리소스 관리",
 "원하는 이펙트 찾기","패키지의 활용","패키지 스토리지","공동 제작","공동 제작 그룹 멤버의 등급과 권한",
 "LocalWorkspace","ExtendedScriptFormat","mLua","VS Code: mLua Extension","VS Code: Debugger for mLua",
 "Command Console","Command Console 명령어","Lua Executor","MSW 단축키","Entity, Component, Property",
 "로컬화된 Entity","모델","모델의 활용","맵 레이어","월드 좌표와 스크린 좌표","타입의 이해",
 "스크립트 라이프 사이클","월드 인스턴스","스크립트 에디터 오리엔테이션","스크립트 어시스트",
 "어노테이션 활용하기","스크립트 디버그","프로퍼티","프로퍼티 동기화","함수","MSW 기본 이벤트 함수",
 "엔티티와 컴포넌트 참조","서버와 클라이언트","실행 제어","로그","메이플스토리 월드 루아 기초",
 "메이플스토리 월드 루아 구문","메이플스토리 월드 루아 문법 확장","AI ToolKit",
 # 02 지형과이동 (55..65)
 "맵 생성과 관리","메이플 타일맵 만들기","발판 만들기","이동 발판 만들기","RectTileMap의 활용",
 "SideViewRectTile모드로 맵 만들기","메이플 이동 개념 이해하기","MovementComponent를 활용한 엔티티의 이동 제어",
 "RectTileMap에서 캐릭터 이동 제어","SideViewRectTileMap에서 캐릭터 이동 제어","사다리와 로프 활용하기",
 # 03 객체표현 (66..82)
 "원하는 이미지 갖고 오기","아틀라스 활용하기","스프라이트 색상 조정","스프라이트 색상을 픽셀 단위로 설정하기",
 "머티리얼 활용하기","머티리얼 응용하기","블루프린트 에디터","Skeleton 리소스 활용하기","아바타 표정 바꾸기",
 "아바타의 외형 변경과 활용","아바타 애니메이션 제어하기","ActionSheet로 아바타 애니메이션 손쉽게 제어하기",
 "아바타를 UI에서 표현하기","영상 재생시키기","다양한 선 그리기","다각형 그리기","웹 브라우저 활용하기",
 # 04 객체제어 (83..90)
 "엔티티의 위치, 크기, 회전 조정","엔티티 구간 이동시키기","텔레포트","월드 워프하기","특정 월드 인스턴스로 워프하기",
 "엔티티의 생성과 삭제, 유효성 체크","엔티티를 탐색하는 EntityService","유저 엔티티를 찾아주는 UserService",
 # 05 게임로직시스템 (91..122)
 "다른 위치로 이동하는 포탈 만들기","공격과 피격","엔티티의 상태 제어하기","플레이어 설정과 제어",
 "행동 트리를 활용한 AI 만들기","행동 트리 노드 만들기","동적으로 맵 생성, 파괴하기","월드 인스턴스 통신",
 "인스턴스 맵 만들기","RoomService를 활용해 룸끼리 통신하기","엔티티의 충돌","충돌 그룹 만들기",
 "물리 사용하기","엔티티에 물리 적용하기","다양한 물리 joint 활용하기","아이템 생성 및 삭제","배지 등록하기",
 "배지 관리하기","배지 서비스 활용하기","Callback","액션을 예약하고 실행하는 TimerService","Event System",
 "Entity Event System","InputService를 활용한 입력과 액션","멀티 터치","에디터 서비스의 활용",
 "TimeSpan으로 시간 표현하기","날짜와 시간 활용하기","스크린샷과 동적 스프라이트","스크린샷 촬영 및 공유하기",
 "플레이 화면 녹화 및 공유하기","TweenLogic을 활용해 엔티티 제어하기",
 # 06 연출 (123..132)
 "플레이어 카메라 제어","CameraService를 활용한 카메라 제어","화면 전환 효과 재생하기","오버레이 라이트 제어하기",
 "LitMode와 광원 사용하기","스킬 이펙트를 뿌려보자!","배경음악 변경하기","효과음 만들기","파티클 사용하기","파티클 활용하기",
 # 07 UI (133..140)
 "UI 에디터","기본 UI 컴포넌트","UI 제작하기","UI 엔티티 제어하기","엔티티에 이름표 붙이기","말풍선 만들기",
 "리치 텍스트 사용하기","UI 디자인 가이드",
 # 08 데이터 (141..146)
 "데이터 편집","Data DB 저장 및 불러오기","DataStorage 활용하기","DataStorage 사용량 제한 알아보기",
 "DataStorage 사용량 제한 활용하기","DataStorage 사용량 제한 활용하기 2",
 # 09 리소스제작 (147..166)
 "기본 개념","아바타 아이템 등록하기","망토 만들기","모자 만들기","제작 과정 안내","뒤통수가 개방된 모자",
 "뒤통수를 덮는 모자","액세서리","가발","얼굴을 가리는 탈","얼굴이 보이는 탈","후드","상의 만들기",
 "신발 만들기","장갑 만들기","하의 만들기","헤어 만들기","한벌옷 만들기","애니메이션 만들기","렉트 타일 제작하기",
 # 10 보안및최적화 (167..173)
 "프로파일러로 월드 성능 분석하기","루아 프로파일링 요약 보고서","루아 프로파일러를 활용하여 최적화하기",
 "TargetUserSync와 프로퍼티 동기화 최적화","패킷 변조 대비하기","RateLimitService 활용하기","예시로 알아보는 서버 검증",
 # 11 게임서비스 (174..187)
 "상품 등록하기","상품 관리하기","월드 숍 서비스 활용하기","아바타 상품 만들기","월드코인 환불하기",
 "메이플스토리 월드에서 수익 출금하기","로컬라이징의 이해","LocaleDataSet","포맷에 맞게 로컬라이징하기",
 "월드 정보와 배지, 상품 번역하기","자동 번역","서버 전용 엔트리 설정하기","테스트 서버","월드 유저 제재 관리",
 # 12 특수조작 (188..191)
 "모바일 기기의 진동 기능 활용","모바일 기기의 중력 센서 사용하기","모바일 기기의 가속도 센서 사용하기",
 "모바일 기기의 가속도 센서 사용하기",
 # 13 다양한기능들 (192..197)
 "정규식","정규식 언어","Effective MSW 1","Effective MSW 2","공동 제작 팁","효과적으로 DataStorage 사용하기",
]
assert len(TITLES) == 198, len(TITLES)

# section ranges: (folder, start_doc_idx_inclusive, end_doc_idx_inclusive)
SECTIONS = [
 ("01-시작하기", 0, 54), ("02-지형과이동", 55, 65), ("03-객체표현", 66, 82),
 ("04-객체제어", 83, 90), ("05-게임로직시스템", 91, 122), ("06-연출", 123, 132),
 ("07-UI", 133, 140), ("08-데이터", 141, 146), ("09-리소스제작", 147, 166),
 ("10-보안및최적화", 167, 173), ("11-게임서비스", 174, 187), ("12-특수조작", 188, 191),
 ("13-다양한기능들", 192, 197),
]
# category text per section (as it appears glued in the body)
CAT_TEXT = ["시작하기","지형과 이동","객체 표현","객체 제어","게임 로직/시스템","연출","UI",
            "데이터","리소스 제작","보안 및 최적화","게임 서비스","특수 조작","다양한 기능들"]
# category marker LINE (1-based) that begins each section's nav block, to trim previous section's last doc tail
CAT_MARK = {1:8059, 2:9572, 3:12104, 4:13635, 5:20696, 6:21976, 7:22700, 8:23481,
            9:25304, 10:26412, 11:28115}  # section_index -> marker line; 0 & 12 special

def sanitize(name):
    n = name.replace('/', '-').replace(':', ' -').replace('\\','-')
    n = re.sub(r'[<>"|?*]', '', n).strip()
    return n

# Return the full list of content lines for doc k (body after 'custom custom',
# with the next doc's glued title / category nav removed). Lossless on body.
def doc_lines(k, next_cat_line):
    start = delim[k] + 1                       # after this 'custom custom'
    if k + 1 >= len(delim):
        return L[start:len(L)]
    if next_cat_line is not None:              # last doc of a section: cut at category marker line
        cut = next_cat_line - 1                # 0-based marker line index
        body = list(L[start:cut])              # drop the nav block that follows
        markl = L[cut]
        for ct in CAT_TEXT:                     # strip glued category name from marker line
            if markl.endswith(ct):
                markl = markl[:-len(ct)]
                break
        return body + [markl]
    # within-section: include up to (not incl) next title-line, then next title-line minus its title
    body = list(L[start:delim[k+1]-1])
    last = L[delim[k+1]-1]
    nxt = TITLES[k+1]
    if last.endswith(nxt):
        last = last[:-len(nxt)]
    return body + [last]

os.makedirs(OUT, exist_ok=True)
index_lines = ["# Mlua 위키 INDEX\n",
 "> 항상 먼저 읽는 지도. 본문은 필요할 때만 해당 파일을 연다. 원본: `reference/TaskWiki.md`\n",
 f"> 문서 {len(delim)}개 · 대분류 {len(SECTIONS)}개\n"]

def intro_line(body):
    seen = False
    for l in body:
        s = l.strip()
        if not seen:
            if s == '학습 과정 소개':
                seen = True
            continue
        if s:
            return s[:80]
    # fallback first non-empty
    for l in body:
        if l.strip(): return l.strip()[:80]
    return ""

# map section_index for marker lookup
sec_index_of = {}
for si,(name,a,b) in enumerate(SECTIONS):
    for k in range(a,b+1): sec_index_of[k]=si

manifest = []
for si,(folder,a,b) in enumerate(SECTIONS):
    os.makedirs(os.path.join(OUT, folder), exist_ok=True)
    index_lines.append(f"\n## {folder}\n")
    used = {}
    for n,k in enumerate(range(a,b+1), start=1):
        title = TITLES[k]
        last_in_sec = (k==b)
        next_cat_line = CAT_MARK.get(si+1) if last_in_sec else None
        lines_out = doc_lines(k, next_cat_line)
        body = lines_out
        fn = sanitize(title)
        if fn in used:
            used[fn]+=1; fn=f"{fn} ({used[fn]})"
        else:
            used[fn]=1
        fname = f"{n:02d}-{fn}.md"
        path = os.path.join(OUT, folder, fname)
        srcstart = delim[k]+2  # 1-based line where body starts
        header = [f"# {title}\n", f"<!-- 출처: reference/TaskWiki.md · 문서 #{k} -->\n"]
        content = "\n".join(header + lines_out).rstrip()+"\n"
        open(path, 'w', encoding='utf-8').write(content)
        desc = intro_line(body)
        index_lines.append(f"- [{title}]({folder}/{fname}) — {desc}")
        manifest.append((folder, fname, len(lines_out)))

open(os.path.join(OUT,'INDEX.md'),'w',encoding='utf-8').write("\n".join(index_lines)+"\n")
print("폴더:", len(SECTIONS), "| 파일:", len(manifest))
for name,a,b in SECTIONS:
    print(f"  {name}: {b-a+1}개")
print("INDEX.md 작성 완료")
