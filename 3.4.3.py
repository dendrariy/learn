res = []
ans = {'math':[], 'phys':[], 'lang':[], 'mid':[]}
with open('dataset_3363_4.txt') as inf:
    for line in inf:
        line = line.strip().split(';')
        res.append(line)
        ans['math'].append(line[1])
        ans['phys'].append(line[2])
        ans['lang'].append(line[3])
        for i in range(len(line)):
            if line[0] not in ans:
                ans[line[0]] = float('{:.9f}'.format((int(line[1]) + int(line[2]) + int(line[3]))/3))
ans['math'] = float('{:.9f}'.format((int(ans['math'][0]) + int(ans['math'][1]) + int(ans['math'][2]))/3))
ans['phys'] = float('{:.9f}'.format((int(ans['phys'][0]) + int(ans['phys'][1]) + int(ans['phys'][2]))/3))
ans['lang'] = float('{:.9f}'.format((int(ans['lang'][0]) + int(ans['lang'][1]) + int(ans['lang'][2]))/3))
ans['mid'] = [ans['math'], ans['phys'], ans['lang']]

for key, value in ans.items():
    print(ans[key])
