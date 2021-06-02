import code
f = open('testing.txt')
for i in f:
    sep = i.index("\t")
    name = i[0:sep]
    re = i[sep+1:]
    ans = code.bmi(name)
    if(ans==(int)re):
        print("Tested ok")
    else:
        print("Inconsistent")