with open('input.txt') as f:
    lines = f.readlines()

dic = {}

def pdic(dic):
    for x in dic:
        for y in dic[x]:
            print(x, y, round(1/dic[x][y], 3))

for l in lines:
    if l == "\n":
        pdic(dic)
    else:
        l = l.strip("\n").split("-")
        for s in range(len(l)-1):
            try:
                dic[l[s]][l[s+1]] += 1
            except:
                try:
                    dic[l[s]][l[s+1]] = 1
                except:
                    dic[l[s]] = {l[s+1]: 1}
