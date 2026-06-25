# -*- coding: utf-8 -*-
"""기존 wiki/ (대분류 폴더 + NN-제목.md) -> gitwiki/ (GitHub 위키 형식, 플랫)
- 페이지 파일명 = 제목 슬러그(.md), 플랫 네임스페이스
- 각 페이지 상단에 '공식 가이드에서 이 제목으로 검색' 안내
- Home.md (랜딩/색인) + _Sidebar.md (대분류별 네비)
원본 본문은 그대로 보존(요약 X). wiki/ 의 첫 2줄(# 제목, <!--출처-->)만 교체.
"""
import os, re, glob

SRC = "wiki"
OUT = "gitwiki"
os.makedirs(OUT, exist_ok=True)

ILLEGAL = re.compile(r'[\\/:*?"<>|#%]')
def slug(title):
    s = ILLEGAL.sub("", title)        # GitHub 위키 페이지명 금지문자 제거
    s = s.replace(" ", "-")
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s

# 대분류 폴더 순서대로 수집
sections = sorted(d for d in os.listdir(SRC)
                  if os.path.isdir(os.path.join(SRC, d)))
# "01-시작하기" -> "01 시작하기" (표시용), 앵커용 slug
def sec_label(folder):
    m = re.match(r"(\d+)-(.+)", folder)
    return f"{m.group(1)} {m.group(2)}" if m else folder

seen = {}
pages = []   # (folder, title, pageslug)
for folder in sections:
    files = sorted(glob.glob(os.path.join(SRC, folder, "*.md")))
    for f in files:
        lines = open(f, encoding="utf-8").read().split("\n")
        title = lines[0][2:].strip() if lines[0].startswith("# ") else os.path.basename(f)[:-3]
        # 본문: 첫 헤딩 줄 다음부터, 선행 빈줄/출처 주석 줄은 건너뜀
        rest = lines[1:]
        i = 0
        while i < len(rest) and (rest[i].strip() == "" or rest[i].strip().startswith("<!--")):
            i += 1
        body = "\n".join(rest[i:]).strip("\n")
        ps = slug(title)
        if ps in seen:
            seen[ps] += 1
            ps = f"{ps}-{seen[ps]}"
        else:
            seen[ps] = 1
        pages.append((folder, title, ps))
        # 페이지 작성
        header = (
            f"# {title}\n\n"
            f"> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** "
            f"더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 "
            f"**「{title}」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.\n"
            f"> _분류: {sec_label(folder)} · 출처: MapleStory Worlds 공식 위키_\n\n"
            f"---\n\n"
        )
        open(os.path.join(OUT, ps + ".md"), "w", encoding="utf-8").write(header + body + "\n")

# Home.md
H = ["# 메이플스토리 월드 (Mlua) 위키\n",
     "메이플스토리 월드 **공식 제작 가이드**를 198개 문서로 정리한 위키입니다. 주로 AI가 참고용으로 읽습니다.\n",
     "> 각 페이지 제목은 **공식 문서 제목과 동일**합니다. 더 깊이 알고 싶으면 해당 제목으로 "
     "메이플스토리 월드 공식 가이드(또는 구글 `메이플스토리 월드 <제목>`)를 검색하세요.\n",
     f"\n**문서 {len(pages)}개 · 대분류 {len(sections)}개**\n"]
# 목차 (대분류 앵커)
H.append("\n## 분류\n")
for folder in sections:
    lab = sec_label(folder)
    anchor = lab.replace(" ", "-")
    H.append(f"- [{lab}](#{anchor})")
# 대분류별 페이지 목록
for folder in sections:
    lab = sec_label(folder)
    H.append(f"\n## {lab}\n")
    for fo, title, ps in pages:
        if fo == folder:
            H.append(f"- [{title}]({ps})")
open(os.path.join(OUT, "Home.md"), "w", encoding="utf-8").write("\n".join(H) + "\n")

# _Sidebar.md
S = ["### 📚 Mlua 위키\n", "[🏠 Home](Home)\n"]
for folder in sections:
    lab = sec_label(folder)
    S.append(f"\n**{lab}**\n")
    for fo, title, ps in pages:
        if fo == folder:
            S.append(f"- [{title}]({ps})")
open(os.path.join(OUT, "_Sidebar.md"), "w", encoding="utf-8").write("\n".join(S) + "\n")

# _Footer.md
open(os.path.join(OUT, "_Footer.md"), "w", encoding="utf-8").write(
    "출처: MapleStory Worlds 공식 제작 가이드 · 페이지 제목으로 공식 가이드 검색 가능\n")

print(f"gitwiki 생성: 페이지 {len(pages)}개 + Home/_Sidebar/_Footer")
# 충돌(중복 슬러그) 보고
dups = {k: v for k, v in seen.items() if v > 1}
print("중복 처리된 슬러그:", dups if dups else "없음")
