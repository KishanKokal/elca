print("number of expressions")
n = int(input())
expressions = []
for i in range(n):
    print("left hand side")
    lhs = input()
    print("right hand side")
    rhs = input()
    expressions.append([lhs, rhs])
print(expressions)
# expressions = [['a', '9'], ['b', 'c+d'], ['e', 'c+d'], ['f', 'b+e'], ['r', 'f']]

print("Intermediate code")
for i in expressions:
    print(i[0],'=',i[1])

used = 0
for i in expressions:
    # print(i)
    for j in expressions:
        if i[0] == j[0]:
            used+=1
    if i[1].isdigit() or used > 1:
        expressions.remove(i)
        print("removed", i)
    used = 0

    

print("Dead code eliminated")

for i in expressions:
    print(i[0],'=',i[1])


for i in expressions:
    # remove common
    for j in expressions:
        if i[0] != j[0] and i[1] == j[1]:
            print("common", i, j)
            expressions.remove(j)

print("Common subexpressions eliminated")

print("Optimized code")
for i in expressions:
    print(i[0],'=',i[1])