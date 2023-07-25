with open('input.txt') as f:
    lines = f.readlines()

dic = {}

units = {
    "aaa": ["S2", "S5", "S7", "S8"],
    "assemble": [("S"+str(x+1)) for x in range(10)],
    "kre": ["S1", "S3", "S4", "S6"],
    "love": ["S1", "S2", "S8", "S9", "S10", "S13", "S14", "S15"],
    "evol": [("S"+str(x)) for x in range(3, 8)] + ["S11", "S12", "S16"],
    "full": ["S"+str(x+1) for x in range(24)]
}

def pdic(dic, unit):
    print(unit)
    for x in dic:
        if x in units[unit]:
            for y in dic[x]:
                if y in units[unit]:
                    print(x, y, round(dic[x][y], 3))
    print("\n")

for l in lines:
    l = l.strip("\n")
    if "-" not in l and l[0] != "S":
        pdic(dic, l)
    else:
        l = l.split("-")
        for s in range(len(l)-1):
            try:
                dic[l[s]][l[s+1]] += 1
            except:
                try:
                    dic[l[s]][l[s+1]] = 1
                except:
                    dic[l[s]] = {l[s+1]: 1}

pdic(dic, "full")
