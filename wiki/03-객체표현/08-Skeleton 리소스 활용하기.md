# Skeleton 리소스 활용하기

<!-- 출처: reference/TaskWiki.md · 문서 #73 -->


학습 과정 소개
크리에이터가 제작한 Skeleton 리소스를 사용해 메이플스토리 월드에서 다양한 애니메이션을 재생할 수 있습니다.

Skeleton 리소스 등록하기
Spine 4.1로 제작된 리소스만 메이플스토리 월드에 Skeleton 리소스로 추가 가능합니다.
Resource Storage에 Skeleton을 추가하기 위해서는 한 폴더에 임포트하고자 하는 png, atlas, skel 파일이 있어야 하고, 그 외에 다른 파일이 포함되면 안 됩니다.

[object Object]

Spine 4.1에서 리소스를 제작합니다.

Resource Storage - 내 리소스 - Skeleton을 선택하고 [+] 버튼을 누릅니다.

추가할 리소스 폴더를 선택해 추가합니다.

유의사항
Spine 4.1로 제작된 리소스만 등록이 가능합니다.

png, atlas, skel의 파일이 모두 있어야 정상적으로 리소스가 등록됩니다.

png, atlas, skel외 다른 파일이 있으면 리소스 등록이 실패합니다.

하나의 skeleton 리소스에 포함 가능한 png 파일은 최대 8개입니다.

png 파일당 최대 크기는 4096*4096입니다.

Skeleton 활용
Skeleton 리소스를 월드에서 사용할 때는 SkeletonRendererComponent를, UI에서 사용할 때는 SkeletonGUIRendererComponent를 사용합니다.
두 컴포넌트의 프로퍼티를 사용해 간단하게 애니메이션을 재생하거나, 함수를 활용해 크리에이터가 원하는 방식으로 애니메이션을 제어할 수도 있습니다.

엔티티에 SkeletonRendererComponent를 추가합니다.

SkeletonRUID에 크리에이터가 추가한 Skeleton 리소스의 RUID를 추가합니다.

프로퍼티 값을 변경해 원하는 스킨과 애니메이션을 재생합니다.

주요 프로퍼티
AnimationNames
AnimationNames 값을 추가하고 애니메이션 재생 순서를 지정할 수 있습니다. AnimationNames 1번부터 차례대로 재생됩니다.
[object Object]

SkinNames
SkinNames 값을 추가하고 스킨을 지정할 수 있습니다. 다양한 스킨이 있는 Skeleton 리소스를 사용할 경우 하나의 엔티티에서 다양한 스킨 조합으로 애니메이션을 재생할 수 있습니다.
[object Object]

Loop
Loop를 true로 설정하면 애니메이션이 반복 재생됩니다.

Skeleton 애니메이션 제어
애니메이션 추가
AddAnimation() 함수를 사용해 애니메이션을 추가할 수 있습니다. AddAnimation() 함수를 사용하면 AnimationNames 프로퍼티와 달리 여러 속성들을 지정할 수 있습니다.
AddAnimation() 함수는 SkeletonAnimationClip를 매개 변수로 받습니다. SkeletonAnimationClip은 애니메이션의 상세한 속성을 나타냅니다. 이 매개 변수를 사용해 애니메이션 트랙 번호, 이름, 반복 재생 시간, 속도 등을 설정할 수 있습니다.

SkeletonAnimationClip
SkeletonAnimationClip은 애니메이션의 상세 속성을 나타냅니다. 주요 프로퍼티는 아래와 같습니다.
자세한 내용은 SkeletonAnimationClip를 참고하세요.

이름	설명
Alpha	다른 트랙과 섞이는 비율을 나타냅니다. 기본값은 1입니다.
Delay	애니메이션 재생을 시작하기까지 대기하는 시간입니다. 시간은 초 단위입니다.
MixDuration	애니메이션이 전환될 때 이전 애니메이션과 섞이는 시간입니다. 시간은 초 단위입니다.
TimeScale	애니메이션 재생 속도입니다. 기본값은 1입니다.
트랙 추가
TrackIndex를 활용해 여러 개의 트랙을 추가할 수 있습니다. TrackIndex는 애니메이션을 재생할 트랙 번호이며, 트랙에 애니메이션을 추가하면 여러 애니메이션을 동시에 재생할 수 있습니다. 트랙은 크리에이터가 원하는 번호로 추가할 수 있습니다. 예를 들어 걷는 애니메이션을 2번 트랙에, 총을 쏘는 애니메이션을 3번 트랙에 추가하면 걸으면서 총을 쏘는 모습을 표현할 수 있습니다.

Tip
1번 트랙은 AnimationNames 프로퍼티에서 사용하기 때문에 TrackIndex로 지정할 수 없습니다.

TrackIndex는 높은 번호의 트랙이 낮은 번호의 트랙을 덮어쓰는 특징이 있습니다.
예를 들어 아래와 같이 2번 트랙에 걷는 애니메이션을 추가하고, 3번 트랙에 사격 애니메이션을 추가했다면 걷기 애니메이션이 손을 앞뒤로 흔드는 모습이더라도, 3번 트랙의 사격 애니메이션은 손을 앞으로 내미는 모습이기 때문에 3번 트랙의 사격 모습으로 보이게 됩니다.

local skel = self.Entity.SkeletonRendererComponent
 
local walk = SkeletonAnimationClip()
walk.TrackIndex = 2
walk.AnimationName = "walk"
skel:AddAnimation(walk)
 
local shoot = SkeletonAnimationClip()
shoot.TrackIndex = 3
shoot.AnimationName = "shoot"
skel:AddAnimation(shoot)
트랙 비우기
SetAnimation() 함수를 활용해 트랙을 비우고, 애니메이션을 추가할 수 있습니다.
비우는 트랙에 재생 중인 애니메이션이 있는 경우 새 애니메이션으로 전환되면서 MixDuration도 함께 적용됩니다.

빈 애니메이션 추가
AddEmptyAnimation(), SetEmptyAnimation() 함수를 활용해 빈 애니메이션을 추가할 수 있습니다.
빈 애니메이션은 주로 두 애니메이션 사이의 전환 효과로 사용합니다. 두 함수 모두 SkeletonAnimationClip를 매개 변수로 받고, AnimationName은 무시됩니다.
만약 아래와 같이 사격 종료(ShootEnd) 애니메이션에서 걷기(Walk) 애니메이션으로 전환할 때 SetEmptyAnimation() 함수를 사용한다면, 전환 시간을 MixDuration으로 설정해 자연스럽게 전환될 수 있습니다.

local skel = self.Entity.SkeletonRendererComponent
 
local shootEnd = SkeletonAnimationClip()
shootEnd.TrackIndex = 3
shootEnd.MixDuration = 0.5
skel:SetEmptyAnimation(shootEnd)
애니메이션 제거
ClearTrack()을 사용해 애니메이션을 제거할 수 있습니다.
ClearTrack() 함수를 사용해 재생 중인 애니메이션을 지울 수 있습니다. 하지만 이 경우 애니메이션이 즉시 전환되므로 급작스러운 전환으로 보일 수 있으므로 이러한 특징을 염두에 두고 사용해야 합니다.

local skel = self.Entity.SkeletonRendererComponent

skel:ClearTrack(3)
어태치먼트 추가
SetAttachment() 함수를 활용해 지정한 슬롯에 어태치먼트를 추가하거나 제거할 수 있습니다. 아래와 같이 고글 어태치먼트를 추가할 수 있습니다.

local skel = self.Entity.SkeletonRendererComponent
 
skel:SetAttachment("face", "goggle")
어태치먼트 제거
어태치먼트를 제거할 때는 SetAttachment() 함수의 두 번째 인수인 attachmentName에 nil을 전달합니다.

local skel = self.Entity.SkeletonRendererComponent

skel:SetAttachment("face", nil)아바타
아바타 표정 바꾸기
아바타의 외형 변경과 활용
아바타 애니메이션 제어하기
ActionSheet로 아바타 애니메이션 손쉽게 제어하기
아바타를 UI에서 표현하기
