input = ''' \
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
'''
'''
output = 5 acc val
output1 = 8 change one jmp or acc, will terminate after the last instr
second to last instr: jmp -4 -> nop -4
algorithm/brutal force:
res = 0
for line in s.splitlines():
    instr[i], val = line[i].split()
        for i in range(len(line)):
        if instr[i] == 'nop':
            continue
        if instr[i] == 'acc':
            res += val
            continue
        if instr[i] == 'jmp':
            line = line[i + val]

'''

def run(code, visited, acc = 0, i = 0):
    while i not in visited and i < len(code):
        visited[i] = acc
        op, num = code[i]
        if op == 'acc':
            acc += num
        elif op == 'jmp':
            i += num - 1
        i += 1
    return acc, i

code, visited = [], {}
input1 = open('instr_jmp_acc.txt', 'r').read()
for line in input.splitlines():
    op, num = line.split()
    code.append((op, int(num)))
acc, _ = run(code, visited)
print(acc)

for j in set(visited.keys()):
    op, num = code[j]
    if (op == 'nop' and (i := j + num) not in visited) or \
        (op == 'jmp' and (i := j + 1) not in visited):
        acc, i = run(code, visited, visited[j], i)
        if i >= len(code):
            print(acc)
            break





# end
