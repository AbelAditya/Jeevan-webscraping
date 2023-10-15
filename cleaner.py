labels = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
# labels = ['x']
temp = []

for i in labels:
    f = open(f'medicines-{i}.txt','r',encoding="utf-8")
    # print(f.read())

    for j in f.readlines():
        if j not in temp:
            temp.append(j)

    f.close()

    f = open(f"medicines-{i}.txt","w",encoding="utf-8")

    for j in temp:
        f.write(j)

    f.close()
    temp=[]
