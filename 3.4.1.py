answer = str()
n = 1
with open('dataset_3363_2.txt') as inf:
    s = inf.readline()
for i in range(1, len(s)-1):
    if s[i-1] > 'A':
        w = s[i-1]
    if s[i-1] < 'A':
        if s[i] > 'A' and s[i-2] > 'A':
            n = int(s[i-1])
            answer += w * n
        if s[i] < 'A':
            n = s[i-1] + s[i]
            m = int(n)
            answer += w * m
print(answer)

with open("answer.txt", "w") as file:
    print(answer, file=file)