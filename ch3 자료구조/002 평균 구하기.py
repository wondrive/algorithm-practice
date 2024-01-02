# 최댓값 M을 골라 모든 점수를 (점수/M*100)

num = int(input()) # 입력
scores = list(map(int, input().split()))      # 성적 입력 받기

max_score = max(scores)
scores = [i / max_score * 100 for i in scores]

print(sum(scores) / num)