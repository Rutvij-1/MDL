import copy

rno = 2019113003
other_rno = 2019101113
x = 1.0 - ((((rno % 10000) % 30) + 1) / 100)
y = rno % 4

pt = [
    [0.95, 0.8],
    [0.9, 0.85],
    [0.85, 0.9],
    [0.8, 0.95]
]
l = 6

R = [0, 2, 5]
G = [1, 3, 4]

trans = []
for i in range(l):
    obj = {}
    obj["L"] = []
    sub_obj = {}
    sub_obj["p"] = x
    sub_obj["S"] = max(i-1, 0)
    obj["L"].append(copy.deepcopy(sub_obj))
    sub_obj = {}
    sub_obj["p"] = 1.0 - x
    sub_obj["S"] = min(i+1, l-1)
    obj["L"].append(copy.deepcopy(sub_obj))
    obj["R"] = []
    sub_obj = {}
    sub_obj["p"] = x
    sub_obj["S"] = min(i+1, l-1)
    obj["R"].append(copy.deepcopy(sub_obj))
    sub_obj = {}
    sub_obj["p"] = 1.0 - x
    sub_obj["S"] = max(i-1, 0)
    obj["R"].append(copy.deepcopy(sub_obj))
    trans.append(copy.deepcopy(obj))


b = [1 / 3, 0.0, 1 / 3, 0.0, 0.0, 1/3]
actions = ["R", "L", "L"]
percept = ["G", "R", "G"]


def p(sd, s, a):
    ans = 0.0
    for obj in trans[s][a]:
        if obj["S"] == sd:
            ans += obj["p"]
    return ans


def pe(e, s):
    if e == "R" and s in R:
        return pt[y][0]
    if e == "R" and s in G:
        return 1.0 - pt[y][1]
    if e == "G" and s in R:
        return 1.0 - pt[y][0]
    if e == "G" and s in G:
        return pt[y][1]


if __name__ == "__main__":
    print(rno, other_rno)
    print(x, y+1)
    for i in range(len(actions)):
        next_b = [0.0 for _ in range(l)]
        a = actions[i]
        for j in range(l):
            for k in range(l):
                next_b[j] += p(j, k, a) * b[k]
            next_b[j] *= pe(percept[i], j)
        val = sum(next_b)
        b = [m / val for m in next_b]
        for m in b:
            print("{:.4f}".format(m), end=" ")
        print("")
