# AI ToolKit

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「AI ToolKit」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 01 시작하기 · 출처: MapleStory Worlds 공식 위키_

---

메이플스토리 월드에서 제공하는 AI ToolKit 기능을 활성화하면 간단한 명령을 통해 월드를 제작할 수 있습니다.
AI ToolKit을 사용하기 위해서는 사전 준비 단계와 별도의 AI 에이전트 구독이 필요합니다.

로컬 워크스페이스
AI ToolKit을 사용하기 위해서는 반드시 로컬 워크스페이스와 ExtendedScriptFormat을 사용해야 합니다. 로컬 워크스페이스에 대한 내용은 LocalWorkspace 가이드를 참고하세요.
AI ToolKit은 AI ToolKit Settings의 로컬 워크스페이스, MCP 서버, AI 스킬 셋 탭의 설정을 모두 마쳐야 정상적으로 동작합니다.

만들기 - AI와 함께 월드 만들기 혹은 만들기 - 새로 만들기 - AI 스타터 템플릿을 선택해 월드를 새로 만듭니다.

만들기 버튼	AI 스타터 템플릿
만들기 버튼	AI 스타터 템플릿
AI 설정하기 버튼을 누르거나, AI Lab - AI ToolKit Settings을 선택합니다.

팝업 버튼	AI Lab 메뉴	바로가기 버튼
3	22	AI 설정 바로가기
로컬 워크스페이스 - 로컬 워크스페이스 사용을 선택하고, 월드를 저장할 위치를 선택합니다.

ExtendedScriptFormat을 활성화합니다.
4

MCP 서버
MCP 연결 방법과 API Key 발급 방법은 MSW MCP를 참고합니다.

MCP 서버 탭

MCP 서버 탭에서 MSW Maker MCP 사용을 활성화합니다.

크리에이터가 사용할 AI 에이전트의 [연결] 버튼을 누릅니다.

AI 스킬 셋
AI 스킬 셋 탭에서 월드 파일 작성·수정에 사용할 AI 도구를 선택하고 연결합니다. 원하는 항목의 [연결] 버튼을 누르면 자동으로 설치됩니다.
자세한 내용은 위 가이드를 참고하세요.

AI 스킬 셋 탭

Tip.
AI 에이전트의 업데이트가 필요한 경우 업데이트 버튼이 활성화됩니다.

AI 시작하기
AI 시작하기 탭에서 연결한 AI 에이전트를 열 수 있습니다.
AI 시작하기 탭

Tip
Claude Code CLI는 연결이 완료되면 메이커 오른쪽 상단의 바로가기 버튼을 통해 쉽게 시작할 수 있습니다.
메이커 바로가기 버튼AI 스킬 셋 설치
사전 준비
AI 스킬 셋을 사용하려면 몇 가지 사전 준비가 필요합니다.

크리에이터의 월드가 LocalWorkspace, ExtendedScriptFormat을 모두 활성화한 상태여야 합니다.

VS Code, Cursor, Claude Code 등 크리에이터가 사용할 AI 에이전트가 설치, 구독된 상태여야 합니다.

macOS의 경우 Apple Silicon(arm64), Intel(x86_64)에 맞는 메이플스토리 월드 클라이언트가 설치되어야 합니다. macOS 최초 실행 시 Gatekeeper가 미서명 / 외부 다운로드 바이너리 실행을 차단할 수 있는데, 이 경우 시스템 설정 > 개인정보 보호 및 보안에서 해당 항목의 실행을 명시적으로 허용합니다.

참고 가이드
LocalWorkspace

AI ToolKit

MSW MCP

Node.js 설치
AI 스킬 셋을 사용하기 위해서는 Node.js가 반드시 설치되어야 합니다. 크리에이터의 OS 환경에 맞는 방법으로 Node.js를 미리 설치해야 합니다.
Windows의 경우 AI 스킬 셋을 연결할 때 Node.js가 자동으로 설치됩니다.
macOS의 경우 크리에이터가 직접 다운로드해 설치하거나, brew install node 명령어를 사용해 설치해야 합니다.

더 알아보기
Windows에서 자동 설치가 되지 않는 경우 winget install OpenJS.NodeJS.LTS 명령어를 사용하여 수동으로 설치할 수 있습니다.

AI 스킬 셋 설치
자동 설치
기본적으로 AI ToolKit Settings - AI 스킬 셋에서 [연결] 버튼을 누르면 자동으로 다운로드됩니다.
설치가 완료되면 연결 버튼이 [연결 완료]로 변경됩니다.
AI 스킬 셋 연결 완료

수동 설치
AI 스킬 셋에서 [연결]을 눌렀지만 자동으로 설치되지 않거나, 크리에이터의 필요에 따라 직접 AI 스킬 셋을 다운로드 받을 수 있습니다. 수동 설치 시 .gitignore를 사용해 형상 관리 대상에서 제외해야 정상적으로 동작합니다.

msw-ai-coding-plugins-official를 크리에이터의 월드 로컬 워크스페이스로 clone 혹은 다운로드합니다.

월드 프로젝트의 .gitignore에 다운로드한 msw-ai-coding-plugins-official의 경로를 추가합니다.

MCP를 재시작하고, 설치가 완료되었는지 확인합니다.MSW MCP
메이플스토리 월드에서 제공하는 MCP들을 설치하면, AI를 사용해 간단한 프롬프트 작성으로 월드를 제작할 수 있습니다. MCP를 지원하는 다양한 개발도구를 크리에이터가 사용하고 있는 AI 에이전트와 연동해 월드를 제작해 보길 바랍니다. 대표적으로 VS Code, Cursor, Claude Code를 사용할 수 있습니다. 이외에도 MCP를 지원하고, Bearer 인증 방식을 사용할 수 있다면 MSW MCP, MSW Maker를 연동할 수 있습니다.
MCP를 사용하기 위해서는 반드시 LocalWorkspace를 활성화해야 합니다.

참고 가이드
LocalWorkspace

AI ToolKit

AI 스킬 셋 설치

MCP 종류
MSW MCP
MSW MCP는 월드 작업 도구와 정보를 AI에게 제공하는 통합 서버(Server-Side) MCP입니다. API Key를 발급 받아야 사용할 수 있습니다.

전송 방식(Transport) : http

서버 엔드포인트 : https://msw-mcp.nexon.com/mcp

인증 방식 : HTTP, API KEY 사용

API Key 발급
MSW MCP를 사용하기 위해서는 메이플스토리 월드에서 발급하는 API Key를 발급 받아야 합니다.

MSW WorldInsight에 접속합니다.

좌측 메뉴에서 PERSONAL - Credentials - API KEY를 선택합니다.

우측 상단의 +Generate 버튼을 클릭합니다.

선택창에서 MCP를 선택하고, Generate를 선택합니다.
[object Object]

주의 사항
API Key는 절대 공개 저장소에 저장하거나 공유하지 마세요.
API Key가 유출된 경우 즉시 해당 키를 삭제하고 새로 발급 받으세요.

MSW Maker MCP
MSW Maker MCP는 메이커 작업 도구를 AI에게 제공하는 클라이언트 기반 MCP입니다. MSW Maker MCP는 stdio 기반으로 CLI 실행 절차 없이, 자동으로 연결됩니다. Windows, macOS에서의 실행 경로가 다르므로 클라이언트가 사용하는 운영체제에 맞는 방식을 사용해야 합니다.

전송 방식(Transport) : stdio

실행 경로 (Windows) : %LOCALAPPDATA%\Nexon\MapleStory Worlds\MakerMCP\msw-maker-mcp.bat

실행 경로 (macOS) : /Applications/MapleStory Worlds.app/Contents/MacOS/MakerMCP

macOS는 실행 권한이 부여된 유니버셜 바이너리 형태로 별도 제공됩니다.

인증 방식: 별도의 인증 없음

MCP 설치 요약
메이플스토리월드 MCP들은 VS Code, Claude, Cursor, Codex CLI에서 사용할 수 있습니다. 각 AI 에이전트마다 지원 여부가 다릅니다.
지원하는 설치 방식 중 하나를 크리에이터가 편의에 따라 선택해 설치할 수 있습니다.

이름	설정 파일 최상위 키	stdio 지원	HTTP 지원	CLI 등록
VS Code(Copilot Agent Mode)	servers	⭕	⭕	Command Palette
VS Code + Claude	mcpServers	⭕	⭕	claude mcp add
Claude Desktop(Code)	mcpServers	⭕	⭕	claude mcp add
Claude Code CLI	mcpServers	⭕	⭕	claude mcp add
Cursor	mcpServers	⭕	⭕	❌
Codex CLI	[mcp_servers.*] TOML	⭕	⭕	codex mcp add
VS Code
VS Code는 설정 파일 최상위 키로 servers를 사용합니다.

설정 파일 위치: {프로젝트}/.vscode/mcp.json

Command Palette 사용
VS Code는 ${input:<이름>} 문법을 지원하므로 headers.Authorization을 직접 설정해야 합니다.

Ctrl + Shift + P / ⌘ + Shift + P를 눌러 Command Palette 실행합니다.

MCP: Add Server... 를 선택합니다.

MSW MCP는 HTTP (HTTP or Server-Sent Events)를 선택, MSW Maker MCP는 Command (stdio)를 선택합니다.

각 MCP에 맞는 값을 입력한 뒤 Workspace를 선택합니다.

MSW MCP: https://msw-mcp.nexon.com/mcp

MSW Maker MCP:

Windows : cmd /c call "%LOCALAPPDATA%\Nexon\MapleStory Worlds\MakerMCP\msw-maker-mcp.bat"

macOS : "/Applications/MapleStory Worlds.app/Contents/MacOS/MakerMCP"

MSW Maker MCP는 VS Code를 재시작해 사용할 수 있습니다. MSW MCP의 경우 "headers" 와 API Key를 입력한 뒤 VS Code를 재시작해야 합니다.

"headers": {
"Authorization": "Bearer ${input:msw-mcp-api-key}"
}
mcp.json 편집
월드의 로컬 워크스페이스 폴더에 .vscode/mcp.json 파일 생성합니다.

크리에이터 운영체제에 맞는 단락을 작성합니다.
Windows:

{
	"servers": {
		"msw-maker-mcp": {
			"type": "stdio",
			"command": "cmd.exe",
			"args": [
				"/c",
				"call",
				"%LOCALAPPDATA%\\Nexon\\MapleStory Worlds\\MakerMCP\\msw-maker-mcp.bat"
			]
		},
		"msw-mcp": {
			"type": "http",
			"url": "https://msw-mcp.nexon.com/mcp",
			"headers": {
				"Authorization": "Bearer ${input:msw-mcp-api-key}"
			}
		}
	}
}
MacOS:

{
	"servers": {
		"msw-maker-mcp": {
			"type": "stdio",
			"command": "/Applications/MapleStory Worlds.app/Contents/MacOS/MakerMCP",
			"args": []
		},

		"msw-mcp": {
			"type": "http",
			"url": "https://msw-mcp.nexon.com/mcp",
			"headers": {
				"Authorization": "Bearer ${input:msw-mcp-api-key}"
			}
		}
	}
}
저장 후 VS Code를 재시작합니다.

VS Code 확장
GitHub Copilot
VS Code에서 GitHub Copilot Chat 을 설치하면 채팅,인라인 제안, 편집 제안을 통합적으로 사용할 수 있습니다. VS Code 1.102 이상부터 사용할 수 있습니다.

VS Code에서** GitHub Copilot Chat**을 엽니다.

Agent Mode로 전환합니다.

Tools에 msw-maker-mcp와 msw-mcp가 목록에 표시되는지 확인합니다.

더 알아보기
코드 완성 제안을 함께 쓰려면 GitHub Copilot 확장도 함께 설치하기를 권장합니다.

Claude Code
VS Code의 EXTENSIONS에서 Claude Code for VS Code를 설치하면 VS Code에서 Claude Code를 실행할 수 있습니다. 이때 MCP 서버 설정은 Claude Code CLI 설정을 공유하므로 Claude Code CLI가 설치되어 있어야 합니다.
VS Code의 .vscode/mcp.json과는 분리되어 있습니다.

명령어 사용
터미널에서 아래 명령어를 실행합니다.
stdio :

claude mcp add msw-maker-mcp --scope project -- cmd.exe /c call "%LOCALAPPDATA%\Nexon\MapleStory Worlds\MakerMCP\msw-maker-mcp.bat"
HTTP:

claude mcp add --transport http --scope project msw-mcp https://msw-mcp.nexon.com/mcp --header "Authorization: Bearer ${MSW_MCP_API_KEY}"
VS Code를 재시작합니다.

VS Code 사이드바에서 Claude 확장 패널을 엽니다.

채팅 입력창에 /mcp를 입력하고 msw-maker-mcp와 msw-mcp가 connected인지 확인합니다.

.mcp.json 편집
.mcp.json 에 아래 mcp 추가 내용을 작성합니다.
VS Code의 .vscode/mcp.json 에 아래 내용을 작성하면 정상적으로 동작하지 않으므로 주의가 필요합니다.
Windows:

{
	"mcpServers": {
		"msw-maker-mcp": {
			"command": "cmd.exe",
			"args": [
				"/c",
				"call",
				"%LOCALAPPDATA%\\Nexon\\MapleStory Worlds\\MakerMCP\\msw-maker-mcp.bat"
			]
		},
		"msw-mcp": {
			"type": "http",
			"url": "https://msw-mcp.nexon.com/mcp",
			"headers": {
				"Authorization": "Bearer ${MSW_MCP_API_KEY}"
			}
		}
	}
}
macOS:

{
	"mcpServers": {
		"msw-maker-mcp": {
			"command": "/Applications/MapleStory Worlds.app/Contents/MacOS/MakerMCP",
			"args": []
		},
		"msw-mcp": {
			"type": "http",
			"url": "https://msw-mcp.nexon.com/mcp",
			"headers": {
				"Authorization": "Bearer ${MSW_MCP_API_KEY}"
			}
		}
	}
}
VS Code에서 Claude 확장 패널을 엽니다.

/mcp를 입력하고 msw-maker-mcp와 msw-mcp가 connected인지 확인합니다.

Claude
Claude는 Desktop, CLI, VS Code 확장 총 3가지의 인터페이스가 있습니다. 이 3가지 모두 하나의 .mcp.json 를 공유합니다. 그러므로 MCP 서버 등록은 한 번만 수행하면 세 인터페이스 모두에서 자동 인식됩니다. 단, Desktop 앱의 Chat 탭에서 사용하는 claude_desktop_config.json은 별도 설정 파일입니다.

더 알아보기
Desktop 앱의 Code 탭은 Apple Silicon (M1+)과 Intel Mac 에서 정상적으로 동작합니다.
Cowork 탭은 Apple Silicon 전용입니다.

Claude Desktop
Claude Desktop에서는 Code 탭에서만 MCP를 사용할 수 있습니다. Windows에서 Claude와 메이플스토리 월드의 MCP를 사용할 경우 Git for Windows를 반드시 설치해야 합니다.

설정 파일 위치는 아래와 같습니다.

{프로젝트}/.mcp.json

명령어 사용
claude mcp add --scope project ... 명령어로 월드의 로컬 워크스페이스 폴더의 .mcp.json 에 등록합니다.
Windows(stdio):

claude mcp add msw-maker-mcp --scope project -- cmd.exe /c call "%LOCALAPPDATA%\Nexon\MapleStory Worlds\MakerMCP\msw-maker-mcp.bat"
macOS(stdio):
bat가 아닌 셸 스크립트(.sh) 또는 실행 바이너리를 직접 호출

claude mcp add msw-maker-mcp --scope project -- "/Applications/MapleStory Worlds.app/Contents/MacOS/MakerMCP"
공통(http, API Key):

claude mcp add --transport http --scope project msw-mcp https://msw-mcp.nexon.com/mcp --header "Authorization: Bearer ${MSW_MCP_API_KEY}"
Claude Desktop을 재시작하고, Code 탭에서 프로젝트 폴더를 선택해 세션을 시작하면 자동으로 인식됩니다.

.mcp.json 편집
월드의 로컬 워크스페이스 폴더에 .mcp.json 생성합니다.

아래 json 단락을 .mcp.json 파일에 작성합니다. 최상위 키 mcpServers를 그대로 사용해야 합니다.
Windows:

{
	"mcpServers": {
		"msw-maker-mcp": {
			"command": "cmd.exe",
			"args": [
				"/c",
				"call",
				"%LOCALAPPDATA%\\Nexon\\MapleStory Worlds\\MakerMCP\\msw-maker-mcp.bat"
			]
		},
		"msw-mcp": {
			"type": "http",
			"url": "https://msw-mcp.nexon.com/mcp",
			"headers": {
				"Authorization": "Bearer ${MSW_MCP_API_KEY}"
			}
		}
	}
}
macOS:

{
	"mcpServers": {
		"msw-maker-mcp": {
			"command": "/Applications/MapleStory Worlds.app/Contents/MacOS/MakerMCP",
			"args": []
		},
		"msw-mcp": {
			"type": "http",
			"url": "https://msw-mcp.nexon.com/mcp",
			"headers": {
				"Authorization": "Bearer ${MSW_MCP_API_KEY}"
			}
		}
	}
}
Code 탭에서 해당 프로젝트 폴더로 세션을 시작하면 자동으로 인식합니다.

프롬프트 박스 우측의 [+] 버튼 - Connectors - msw-maker-mcp / msw-mcp 가 도구 목록에 표시되는지 확인합니다. 또는 프롬프트에 /mcp 입력해 connected 상태를 확인합니다.

Claude Code CLI
명령어 사용
터미널에서 등록 방식에 맞는 명령어를 사용합니다. 등록 결과를 월드의 로컬 워크스페이스 폴더의 .mcp.json 에 저장하기 위해 항상 --scope project 옵션을 함께 사용해야 합니다. 옵션 생략 시 기본값 local 로 등록되어 사용자별 설정에만 반영됩니다.

Windows(stdio):

claude mcp add msw-maker-mcp --scope project -- cmd.exe /c call "%LOCALAPPDATA%\Nexon\MapleStory Worlds\MakerMCP\msw-maker-mcp.bat"
macOS(stdio):

claude mcp add msw-maker-mcp --scope project -- "/Applications/MapleStory Worlds.app/Contents/MacOS/MakerMCP"
공통(http, API Key):

claude mcp add --transport http --scope project msw-mcp https://msw-mcp.nexon.com/mcp --header "Authorization: Bearer ${MSW_MCP_API_KEY}"
.mcp.json 편집
.mcp.json에 설정 방식에 맞는 명령어를 추가합니다.

Windows:

{
	"mcpServers": {
		"msw-maker-mcp": {
			"command": "cmd.exe",
			"args": [
				"/c",
				"call",
				"%LOCALAPPDATA%\\Nexon\\MapleStory Worlds\\MakerMCP\\msw-maker-mcp.bat"
			]
		},
		"msw-mcp": {
			"type": "http",
			"url": "https://msw-mcp.nexon.com/mcp",
			"headers": {
				"Authorization": "Bearer ${MSW_MCP_API_KEY}"
			}
		}
	}
}
macOS:

{
	"mcpServers": {
		"msw-maker-mcp": {
			"command": "/Applications/MapleStory Worlds.app/Contents/MacOS/MakerMCP",
			"args": []
		},
		"msw-mcp": {
			"type": "http",
			"url": "https://msw-mcp.nexon.com/mcp",
			"headers": {
				"Authorization": "Bearer ${MSW_MCP_API_KEY}"
			}
		}
	}
}
Cursor
Settings
Cursor 설정 화면을 엽니다.

Tools & Integrations 또는 MCP를 선택합니다

New MCP Server - 프로젝트 스코프의 mcp.json 편집 화면을 엽니다. 글로벌 등록 옵션은 사용하지 않습니다.

운영체제에 맞게 아래 json 내용을 입력합니다.
Windows:

{
	"mcpServers": {
		"msw-maker-mcp": {
			"type": "stdio",
			"command": "cmd.exe",
			"args": [
				"/c",
				"call",
				"%LOCALAPPDATA%\\Nexon\\MapleStory Worlds\\MakerMCP\\msw-maker-mcp.bat"
			]
		},
		"msw-mcp": {
			"url": "https://msw-mcp.nexon.com/mcp",
			"headers": {
				"Authorization": "Bearer ${MSW_MCP_API_KEY}"
			}
		}
	}
}
macOS:

{
  "mcpServers": {
    "msw-maker-mcp": {
      "command": "/bin/sh",
      "args": [
        "-c",
        "exec \"$1\"",
        "msw-maker-mcp",
        "/Applications/MapleStory Worlds.app/Contents/MacOS/MakerMCP"
      ]
    },
    "msw-mcp": {
      "url": "https://msw-mcp.nexon.com/mcp",
      "headers": {
        "Authorization": "Bearer ${MSW_MCP_API_KEY}"
      }
    }
  }
}
Cursor를 재시작합니다.

Cursor Settings - MCP에서 등록한 서버 항목에 초록색 상태 표시등이 나타나는지 확인합니다.

Agent 채팅에서 Available Tools 에 msw-maker-mcp와 msw-mcp가 있는지 확인합니다.

.mcp.json 편집
월드의 로컬 워크스페이스 폴더에 .cursor/mcp.json 생성합니다.

운영체제에 맞게 아래 내용을 입력합니다.
Windows:

{
	"mcpServers": {
		"msw-maker-mcp": {
			"type": "stdio",
			"command": "cmd.exe",
			"args": [
				"/c",
				"call",
				"%LOCALAPPDATA%\\Nexon\\MapleStory Worlds\\MakerMCP\\msw-maker-mcp.bat"
			]
		},
		"msw-mcp": {
			"url": "https://msw-mcp.nexon.com/mcp",
			"headers": {
				"Authorization": "Bearer ${MSW_MCP_API_KEY}"
			}
		}
	}
}
macOS:

{
  "mcpServers": {
    "msw-maker-mcp": {
      "command": "/bin/sh",
      "args": [
        "-c",
        "exec \"$1\"",
        "msw-maker-mcp",
        "/Applications/MapleStory Worlds.app/Contents/MacOS/MakerMCP"
      ]
    },
    "msw-mcp": {
      "url": "https://msw-mcp.nexon.com/mcp",
      "headers": {
        "Authorization": "Bearer ${MSW_MCP_API_KEY}"
      }
    }
  }
}
Cursor를 재시작합니다.

Cursor Settings - MCP에서 등록한 서버 항목에 초록색 상태 표시등이 나타나는지 확인합니다.

Agent 채팅에서 Available Tools 목록에 msw-maker-mcp와 msw-mcp가 표시되는지 확인합니다.

Tip
Cursor Settings - Tools & MCPs - Installed MCP Servers에서 연결을 활성화 할 수 있습니다.
Installed MCP Servers

Codex
OpenAI Codex CLI는 설정 파일 포맷으로 JSON이 아닌 TOML을 사용합니다. 서버는 [mcp_servers.<이름>] 섹션으로 정의합니다.

설치 경로: {프로젝트}/.codex/config.toml

더 알아보기
Codex는 프로젝트 스코프 config.toml을 'trusted project'로 지정된 프로젝트에서만 읽습니다. 프로젝트를 처음 열면 Codex가 신뢰 여부를 물어보며, 신뢰하지 않은 프로젝트에서는 .codex/config.toml이 무시됩니다.
또한 codex mcp add CLI는 프로젝트 스코프 옵션을 제공하지 않고 항상 글로벌 경로(~/.codex/config.toml)에 등록합니다. 그러므로 config.toml 편집 방식을 권장합니다.

명령어 사용
Terminal에서 운영체제에 맞는 명령어를 입력하고, 서버를 등록합니다.
이 등록은 사용자 글로벌 경로 (~/.codex/config.toml) 에 저장되어 모든 Codex 세션에 공통 적용됩니다.
Windows(stdio):

codex mcp add msw-maker-mcp -- cmd.exe /c call "%LOCALAPPDATA%\Nexon\MapleStory Worlds\MakerMCP\msw-maker-mcp.bat"
macOS(stdio):

codex mcp add msw-maker-mcp -- "/Applications/MapleStory Worlds.app/Contents/MacOS/MakerMCP"
공통 (HTTP, API Key) :

codex mcp add msw-mcp --url https://msw-mcp.nexon.com/mcp --bearer-token-env-var MSW_MCP_API_KEY
월드의 로컬 워크스페이스 폴더에서 터미널로 codex 명령을 실행합니다.

세션 내에서 /mcp 명령 입력하고 msw-maker-mcp와 msw-mcp 가 connected 상태로 표시되는지 확인합니다.

config.toml 편집
Codex CLI 는 headers 필드를 공식 지원하지 않으므로 bearer_token_env_var 에 API KEY를 입력하면, 해당 값이 Authorization: Bearer <토큰> 헤더로 변환되어 전송됩니다. Codex 설정 파일은 TOML 입니다.

Tip
Windows 경로처럼 \가 포함된 문자열은 ''(작은따옴표) 로 감싸는 것이 안전합니다.

로컬 워크스페이스 폴더에 .codex/config.toml 생성합니다.

크리에이터의 운영체제에 맞게 작성합니다.
Windows:


[mcp_servers.msw-maker-mcp]
command = "cmd.exe"
args = ["/c", "call", '%LOCALAPPDATA%\Nexon\MapleStory Worlds\MakerMCP\msw-maker-mcp.bat']

[mcp_servers.msw-mcp]
url = "https://msw-mcp.nexon.com/mcp"
http_headers = { "Authorization" = "Bearer ${MSW_MCP_API_KEY}" }
macOS:

[mcp_servers.msw-maker-mcp]
command = "/Applications/MapleStory Worlds.app/Contents/MacOS/MakerMCP"
args = []

[mcp_servers.msw-mcp]
url = "https://msw-mcp.nexon.com/mcp"
http_headers = { "Authorization" = "Bearer ${MSW_MCP_API_KEY}" }
.codex/config.toml 파일을 저장하고, 월드의 로컬 워크스페이스 폴더에서 codex 명령을 실행합니다.
최초 실행 시 프로젝트 신뢰 여부 확인 프롬프트가 뜨면 trust를 선택합니다.

세션 내에서 /mcp 명령 입력하고 msw-maker-mcp와 msw-mcp 가 connected 상태로 표시되는지 확인합니다.
