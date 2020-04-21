res = []
with open('dataset_3363_3.txt') as inf:
    for line in inf:
        line = line.strip().split()
        for i in range(len(line)):
            res.append(line[i])
ans = {}
for i in range(len(res)):
    if res[i] in ans:
        ans[res[i]] += 1
    else:
        ans[res[i]] = 1
max_value = max(ans.values())
print(list(ans.keys())[list(ans.values()).index(max_value)], max_value)
    
