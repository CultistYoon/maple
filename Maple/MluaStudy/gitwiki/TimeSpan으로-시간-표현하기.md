# TimeSpan으로 시간 표현하기

> 📖 **메이플스토리 월드 공식 제작 가이드 문서입니다.** 더 자세하거나 최신 내용이 필요하면 공식 가이드/구글에서 **「TimeSpan으로 시간 표현하기」** 로 검색하세요 — 이 페이지 제목은 공식 문서 제목과 동일합니다.
> _분류: 05 게임로직시스템 · 출처: MapleStory Worlds 공식 위키_

---

학습 과정 소개
DateTime을 활용하기 위해선 TimeSpan을 이용해야 합니다. 초, 분, 시간의 단위를 나타냅니다.

TimeSpan 소개
TimeSpan은 시간 간격을 나타냅니다. 특정 시작점 또는 끝점에 대한 참조 없이 일반적인 간격만을 나타내므로 어떠한 가변적인 연도와 월 단위로 표현할 수 없습니다.
TimeSpan은 특정 시점으로부터 다른 특정 시점까지의 시간을 계산할 때 사용할 수 있습니다. 어떤 스테이지를 통과하는 데 걸린 시간을 구하고 싶거나, 시간을 데이터 스토리지에 저장하기 위해 사용할 수 있습니다. 표준 형식 지정자와 사용자 형식 지정자 중 크리에이터의 필요에 맞게 사용할 수 있습니다. 표준 형식 지정자는 "c", "g", "G" 로 각 지정자마다 특정 형식이 정의되어 있습니다. 사용자 형식 지정자는 시간을 표시하는 형식의 자릿수와 표시 방법 등을 크리에이터의 필요에 맞게 사용할 수 있습니다.

TimeSpan의 생성자
생성자는 보통 큰 시간에서 작은 시간으로 입력하고, 생성자에 따라 문화권을 구분하기도 합니다.

예: 시간, 분, 초 / 일, 시간, 분, 초, 밀리초

TimeSpan(int elapsed): 밀리초 단위의 정수로 객체를 초기화합니다.

TimeSpan(int hours, int minutes, int seconds): 시간, 분, 초로 객체를 초기화합니다.

TimeSpan(int days, int hours, int minutes, int seconds): 일, 시간, 분, 초로 객체를 초기화합니다.

TimeSpan(int days, int hours, int minutes, int seconds, int milliseconds): 일, 시간, 분, 초, 밀리초로 객체를 초기화합니다.

TimeSpan(string timeSpanString): [ws][-]{ d | [d.]hh:mm[:ss[.ff]] }[ws] 형식의 시간 간격 사양을 문자열로 사용하고, 객체를 초기화합니다.

TimeSpan(string timeSpanString, string format) : [ws][-]{ d | [d.]hh:mm[:ss[.ff]] }[ws] 형식의 시간 간격 사양을 문자열로 사용하고, 객체를 초기화합니다.
timeSpanString은 반드시 format 형식과 정확하게 일치해야 하고, format은 표준 서식 지정자, 사용자 지정 서식 지정자를 포함합니다.

TimeSpan(string timeSpanString, string format, string cultureName) : [ws][-]{ d | [d.]hh:mm[:ss[.ff]] }[ws] 형식의 시간 간격 사양을 문자열로 사용하고, 객체를 초기화합니다.
timeSpanString은 반드시 format 형식과 정확하게 일치해야 하고, format은 표준 서식 지정자, 사용자 지정 서식 지정자를 포함합니다.
cultureName은 format이 표준 지정자일 때 문화권별 정보를 제공합니다. 문화권 이름은 BCP-47의 표준을 따릅니다.

Tip
대괄호 [ ] 안의 요소는 선택적으로 사용할 수 있습니다.
중괄호 { } 사이의 요소는 세로 막대 | 로 구분된 것 중에 선택해 사용합니다.

시간 간격 기호
TimeSpan에서 시간을 나타내는 공통 기호입니다.

기호	설명
ws	공백
ff	한 자릿수부터 일곱 자릿수로 구성된 초 자릿수
ss	0부터 59 사이의 초
MM	0부터 59 사이의 분
hh	0에서 23 사이의 시간
d	0부터 10675199 사이의 일
-	TimeSpan 음수를 나타내는 기호
.	일과 시간을 구분하는 문화권 구분 기호
분과 초를 구분하는 문화권 구분 기호
:	문화권에 민감한 시간 구분 기호
표준 TimeSpan 서식 지정자
표준 TimeSpan 형식 문자열은 단일 형식 지정자를 사용하여 서식 지정 작업으로 생성되는 TimeSpan 값의 텍스트 표현을 정의합니다.

형식 지정자	이름	설명
"c"	상수 형식	문화권을 구분하지 않으며 [-][d'.']hh':'mm':'ss['.'fff] 형식을 사용합니다.
"g"	일반 약식	문화권을 구분하며, 필요한 내용을 출력합니다. [-][d':']h':'mm':'ss[.FFF] 형식을 사용합니다.
"G"	일반 긴 형식	문화권을 구분하며, 일 수와 소수 7 자리를 출력합니다. [-]d':'hh':'mm':'ss.fff 형식을 사용합니다.
Tip.
형식 중 [ ] 사이의 기호들은 유효한 값이 있는 경우에만 해당 서식 지정자를 사용합니다.

상수 서식 지정자
상수 서식 지정자 "c"는 문화권을 구분하지 않습니다. 형식은 [-][d'.']hh':'mm':'ss['.'fff] 입니다.

기호	설명
-	음수를 나타내는 기호
fff	초의 소수 부분을 나타냅니다. 값 범위는 "001" 부터 "999"까지입니다.
ss	"0"부터 "59" 범위의 초를 나타냅니다.
mm	"00"부터 "59" 범위의 분을 나타냅니다.
hh	"00"부터 "23" 범위의 시간을 나타냅니다.
d	일 수를 나타냅니다.
local timeSpan1 = TimeSpan(7, 45, 16)
local timeSpan2 = TimeSpan(18, 12, 38)
local timeSpanString1 = timeSpan1:ToFormattedString("c")
local timeSpanString2 = timeSpan2:ToFormattedString("c")
local timeSpanString3 = (timeSpan1 + timeSpan2):ToFormattedString("c")
 
log(timeSpanString1) -- 07:45:16
log(timeSpanString2) -- 18:12:38
log(timeSpanString3) -- 1.01:57:54
일반 약식 서식 지정자
일반 약식 서식 지정자 "g"는 필요한 내용만 출력하며 문화권을 구분합니다. 형식은 [-][d':']h':'mm':'ss[.FFF] 입니다.

기호	설명
-	음수를 나타내는 기호
.	초 소수 구분을 나타냅니다.
FFF	초의 소수 부분을 나타냅니다.
ss	"00"부터 "59" 범위의 초를 나타냅니다.
mm	"00"부터 "59" 범위의 분을 나타냅니다.
hh	"00"부터 "23" 범위의 시간을 나타냅니다.
d	일 수를 나타냅니다.
local timeSpan1 = TimeSpan(7, 45, 16)
local timeSpan2 = TimeSpan(18, 12, 38)
local timeSpanString1 = timeSpan1:ToFormattedString("g")
local timeSpanString2 = timeSpan2:ToFormattedString("g")
local timeSpanString3 = (timeSpan1 + timeSpan2):ToFormattedString("g", "fr-FR")
 
log(timeSpanString1) -- 07:45:16
log(timeSpanString2) -- 18:12:38
log(timeSpanString3) -- 1:1:57:54
일반 긴 서식 지정자
일반 긴 서식 지정자 "G"는 항상 일 수와 소수 세 자릿수를 출력하고 문화권을 구분합니다. 형식은 [-]d':'hh':'mm':'ss.fff 입니다.

기호	설명
-	음수를 나타내는 기호
.	초 소수 구분을 나타냅니다.
fff	초의 소수 부분을 나타냅니다.
ss	"00"부터 "59" 범위의 초를 나타냅니다.
mm	"00"부터 "59" 범위의 분을 나타냅니다.
hh	"00"부터 "23" 범위의 시간을 나타냅니다.
d	일 수를 나타냅니다.
local timeSpan1 = TimeSpan(7, 45, 16)
local timeSpan2 = TimeSpan(18, 12, 38)
local timeSpanString1 = timeSpan1:ToFormattedString("G")
local timeSpanString2 = timeSpan2:ToFormattedString("G")
local timeSpanString3 = (timeSpan1 + timeSpan2):ToFormattedString("G", "fr-FR")
 
log(timeSpanString1) -- 0:07:45:16.000
log(timeSpanString2) -- 0:18:12:38.000
log(timeSpanString3) -- 1:01:57:54,000
사용자 지정 TimeSpan 서식 지정자
사용자 지정 형식 문자열은 하나 이상의 사용자 지정 TimeSpan 형식 지정자와 임의 개수의 리터럴로 구성됩니다.
TimeSpan 형식 문자열은 생성되는 TimeSpan 값의 텍스트 표현을 정의합니다. 표준 TimeSpan 형식 문자열이 아닌 문자열은 사용자 지정 TimeSpan 형식 문자열로 해석됩니다.

"d"
"d" 사용자 지정 형식 지정자는 일 수를 나타내는 값을 출력합니다. 값이 두 자리 이상인 경우에도 전체 일 수를 출력합니다. 값이 0인 경우 지정자는 "0"을 출력합니다.
"d" 사용자 지정 형식 지정자만 단독으로 사용하는 경우 표준 형식 문자열로 잘못 해석되지 않도록 "%d"를 지정합니다.

local timeSpan = TimeSpan(16, 4, 3, 17, 250)
local timeSpanString = timeSpan:ToFormattedString("%d")
 
log(timeSpanString) -- 16
"d" - "dddddddd"
"dd", "ddd", "dddd", "ddddd", "dddddd", "ddddddd", "dddddddd" 사용자 지정 서식 지정자는 일 수를 나타내는 값을 출력합니다.
출력 문자열에는 서식 지정자에 "d" 문자 수로 지정된 최소 자릿수가 포함되며 필요에 따라 앞에 0으로 채워집니다. 전체 일 수가 서식 지정자의 "d" 문자 수를 초과할 경우 전체 일 수가 결과 문자열에 출력됩니다.

local timeSpan = TimeSpan(365, 21, 19, 45)
  
log(timeSpan:ToFormattedString("dd'.'hh':'mm':'ss")) -- 365.21:19:45
log(timeSpan:ToFormattedString("dddd'.'hh':'mm':'ss")) -- 0365.21:19:45
"h"
"h" 사용자 지정 형식 지정자는 시간 수를 나타내는 값을 출력합니다. 시간 값이 0-9라면 한 자리 문자열 값을 반환하고, 10-23이면 두 자리 문자열을 반환합니다.
"h" 사용자 지정 서식 지정자만 단독으로 사용하는 경우 표준 서식 지정자로 잘못 해석되지 않도록 "%h"를 지정합니다. 일반적으로 하나의 숫자만 포함하는 문자열은 일 수로 해석됩니다.
"h" 사용자 지정 서식 지정자를 대신 사용하여 숫자 문자열을 시간 수로 해석할 수 있습니다.

local timeSpan = TimeSpan(16, 4, 3, 17, 250)
local timeSpanString = timeSpan:ToFormattedString("%h")
 
log(timeSpanString) -- 4
"hh"
"hh" 사용자 지정 서식 지정자는 시간 수를 나타내는 값을 출력합니다. 시간 값이 0-9라면 출력 문자열 앞에 0이 포함됩니다.
일반적으로 하나의 숫자만 포함하는 문자열은 일 수로 해석됩니다.
"hh" 사용자 지정 서식 지정자를 대신 사용하여 숫자 문자열을 시간 수로 해석할 수 있습니다.

local timeSpan = TimeSpan(365, 3, 14, 45)
  
log(timeSpan:ToFormattedString("dd'.'hh':'mm':'ss")) -- 365.03:14:45
"m"
"m" 사용자 지정 서식 지정자는 분 수를 나타내는 값을 출력합니다. 분 값이 0-9라면 한 자리 문자열 값을 반환하고, 값이 10-59라면 두 자리 문자열 값을 반환합니다.
"m" 사용자 지정 서식 지정자만 단독으로 사용하는 경우 표준 서식 지정자로 잘못 해석되지 않도록 "%m"을 지정합니다.
일반적으로 하나의 숫자만 포함하는 문자열은 일 수로 해석됩니다.
"m" 사용자 지정 서식 지정자를 대신 사용하여 숫자 문자열을 분 수로 해석할 수 있습니다.

local timeSpan = TimeSpan(16, 4, 3, 17, 250)
local timeSpanString = timeSpan:ToFormattedString("%m")
 
log(timeSpanString) -- 3
"mm"
"mm" 사용자 지정 서식 지정자는 분 수를 나타내는 값을 출력합니다. 분 값이 0-9라면 출력 문자열 앞에 0이 포함됩니다.
일반적으로 하나의 숫자만 포함하는 문자열은 일 수로 해석됩니다. "mm" 사용자 지정 서식 지정자를 대신 사용하여 숫자 문자열을 분 수로 해석할 수 있습니다.

local timeSpan = TimeSpan(365, 21, 4, 45)
  
log(timeSpan:ToFormattedString("dd'.'hh':'mm':'ss")) -- 365.21:04:45
"s"
"s" 사용자 지정 서식 지정자는 초 수를 나타내는 값을 출력합니다. 초 값이 0-9라면 한 자리 문자열 값을 반환하고 값이 10-59라면 두 자리 문자열 값을 반환합니다.
일반적으로 하나의 숫자만 포함하는 문자열은 일 수로 해석됩니다. "s" 사용자 지정 서식 지정자를 대신 사용하여 숫자 문자열을 초 수로 해석할 수 있습니다.
"s"만 단독으로 사용하는 경우 표준 서식 지정자로 잘못 해석되지 않도록 "%s"를 지정합니다.

local timeSpan = TimeSpan(16, 4, 3, 17, 250)
local timeSpanString = timeSpan:ToFormattedString("%s")
 
log(timeSpanString) -- 17
"ss"
"ss" 사용자 지정 서식 지정자는 초 수를 나타내는 값을 출력합니다. 초 값이 0-9라면 출력 문자열 앞에 0이 포함됩니다.
일반적으로 하나의 숫자만 포함하는 문자열은 일 수로 해석됩니다. "ss" 사용자 지정 서식 지정자를 대신 사용하여 숫자 문자열을 초 수로 해석할 수 있습니다.

local timeSpan = TimeSpan(365, 21, 4, 5)
  
log(timeSpan:ToFormattedString("dd'.'hh':'mm':'ss")) -- 365.21:04:05
"f"
"f" 사용자 지정 서식 지정자는 1/10 초를 출력합니다. 서식 지정 작업에서 나머지 소수 자릿수는 잘립니다.
문자열로 TimeSpan 객체를 생성할 경우 문자열에는 정확히 소수 한 자리가 포함되어야 합니다.
"f"만 단독으로 사용하는 경우 표준 서식 지정자로 잘못 해석되지 않도록 "%f"를 지정합니다.

local timeSpan = TimeSpan(876)
  
log(timeSpan:ToFormattedString("%f")) -- 8
"ff"
"ff" 사용자 지정 서식 지정자는 1/100 초를 출력합니다. 서식 지정 작업에서 나머지 소수 자릿수는 잘립니다.
문자열로 TimeSpan 객체를 생성할 경우 문자열에는 정확히 소수 두 자리가 포함되어야 합니다.

local timeSpan = TimeSpan(876)
  
log(timeSpan:ToFormattedString("ff")) -- 87
"fff"
"fff" 사용자 지정 서식 지정자는 밀리초를 출력합니다. 서식 지정 작업에서 나머지 소수 자릿수는 잘립니다.
문자열로 TimeSpan 객체를 생성할 경우 문자열에는 정확히 소수 세 자리가 포함되어야 합니다.

local timeSpan = TimeSpan(876)
  
log(timeSpan:ToFormattedString("fff")) -- 876
"F"
"F" 사용자 지정 서식 지정자는 1/10 초를 출력합니다. 서식 지정 작업에서 나머지 소수 자릿수는 잘립니다.
1/10초 값이 0이라면 결과 문자열에 포함되지 않습니다. 문자열로 TimeSpan 객체를 생성할 경우 1/10초 숫자 표시는 포함되지 않아도 됩니다.
"F"만 단독으로 사용하는 경우 표준 서식 지정자로 잘못 해석되지 않도록 "%F"를 지정합니다.

local timeSpan = TimeSpan(800)

log(timeSpan:ToFormattedString("%F")) -- 8
"FF"
"FF" 사용자 지정 서식 지정자는 1/100 초를 출력합니다. 서식 지정 작업에서 나머지 소수 자릿수는 잘립니다.
1/100초 값이 0이라면 결과 문자열에 포함되지 않습니다. 문자열로 TimeSpan 객체를 생성할 경우 1/100초 숫자 표시는 포함되지 않아도 됩니다.

local timeSpan1 = TimeSpan(876)
local timeSpan2 = TimeSpan(800)
  
log(timeSpan1:ToFormattedString("FF")) -- 87
log(timeSpan2:ToFormattedString("FF")) -- 8
"FFF"
"FFF" 사용자 지정 서식 지정자는 밀리초를 출력합니다. 서식 지정 작업에서 나머지 소수 자릿수는 잘립니다.
밀리초 값이 0이라면 결과 문자열에 포함되지 않습니다. 문자열로 TimeSpan 객체를 생성할 경우 밀리초 숫자 표시는 포함되지 않아도 됩니다.

local timeSpan1 = TimeSpan(876)
local timeSpan2 = TimeSpan(800)
  
log(timeSpan1:ToFormattedString("FFF")) -- 876
log(timeSpan2:ToFormattedString("FFF")) -- 8
