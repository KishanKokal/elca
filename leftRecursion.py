import re
gm = {
    'A->ABd|Aa|a'
}

aplha = []
beta = []

for i in gm:
    exp = re.split(r'->|\|', i)
    nt = exp[0]
    cnt= 0
    for i in exp:
        if cnt == 0:
            cnt += 1
            continue
        else:
            if i[0] == exp[0]:
                aplha.append(i[1:])
                
            else:
                beta.append(i)

    print(exp[0],'->', end='')
    for i in beta:
        if i == beta[-1]:
            print(i+exp[0]+'\'', end='')
        else:
            print(i+exp[0]+'\'','|', end='')
    
    print('\n',exp[0]+'\'','->', end='', sep='')
    for i in aplha:
        if i== aplha[-1]:
            print(i+exp[0]+'\'','|', '@', end='')
        else:
            print(i+exp[0]+'\'','|', end='')
    
    print('\n')