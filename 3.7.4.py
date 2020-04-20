n = int(input())
point = {'север': 0, 'запад': 0, 'юг': 0, 'восток': 0}
for i in range (n):
    in_command = str(input())
    command = in_command.split()
    value = int(command[1])
    if (command[0] == 'север'):
        point['север'] += value
    if (command[0] == 'запад'):
        point['восток'] -= value
    if (command[0] == 'юг'):
        point['север'] -= value
    if (command[0] == 'восток'):
        point['восток'] += value
print(point['север'], point['восток'])
    
