import re

lines = []
tokenr =[]


with open('token.txt', 'r') as file:
    for i in file:
        lines.append(i)


for i in lines:
    tokenr.append(re.split('\s', str(i)))

# print(tokenr)
keyword = ['for', 'in' , 'print']
datatype = ['String', 'int']
operator = ['+', '-', '*', '/', '%', '=', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '++', '--']
seperator = ['(', ')', '{', '}', '[', ']', ';', ',', ' ']

for i in tokenr:
    if re.match('^[#]', i[0]) or re.match('^[//]', i[0]) or re.match('^[/*]', i[0]):
        print('Comment: ', i)
        continue
    for j in i:
        if j != '':
            print(j)
            if re.findall('=', j) and len(j)>2:
                print('Operator: =')
                print('Identifier: ', j.split('=')[0])
                print('Value: ', j.split('=')[1])
            if re.findall('\(', j ) and len(j)>1:
                print('Seperator: (')
                print('keyword: ', j.split('(')[0])
                print('Identifier: ', j.split('(')[1].split(')')[0])
                print('Seperator: )')
            if j in keyword:
                print('Keyword: ', j)
            elif j in datatype:
                print('Datatype: ', j)
            elif j in operator and len(j) <= 2:
                print('Operator: ', j)
            elif j in seperator and len(j) == 1:
                print('Seperator: ', j)
            elif re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', j) and re.findall('=', j) == [] and re.findall('\(', j) == []:
                print('Identifier: ', j)
            elif(re.findall('\"', j)):
                print('String: ', j)
            elif(re.findall('\'', j)):
                print('Character: ', j)         
            elif re.match(r'[0-9_]*', j):
                print('Integer: ', j)

            print('===========================')