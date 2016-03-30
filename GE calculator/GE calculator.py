

Ge1= input("Enter first General ed requirement:")
Ge2= input("Enter second General ed requirement:")

file = open('General Ed files/'+Ge1+'.txt', 'r')
file2 = open('General Ed files/'+Ge2+'.txt', 'r')

f = open('GE calculator/General Ed files/%s and %s.txt' %(Ge1, Ge2),'w') 

def readline1(file):
    w = []
    for line in file:
        w.append(line)
    return w

first = readline1(file)

def readline2(file2):
    e= []
    for line in file2:
        e.append(line)
    return e

second= readline2(file2)


def combine(first,second):
    both=[]
    for i in first:
        if i in second:
            both.append(i)
    return both

total = combine(first,second)

for i in total:
    f.write(i)

file.close()
file2.close()
f.close()
