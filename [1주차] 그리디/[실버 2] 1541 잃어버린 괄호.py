import sys
equations = sys.stdin.readline().rstrip().split('-')

result = 0
index = 0
for equation in equations:
    tmp = map(int, equation.split('+'))
    if index == 0:
        result += sum(tmp)
        index += 1
    else:
        result -= sum(tmp)
        
print(result)
