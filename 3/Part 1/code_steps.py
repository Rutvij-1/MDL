import copy
from tabulate import tabulate

rno = 2019111032
other_rno = 2019111013
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
    print(f"Roll Numbers od team members: {rno}, {other_rno}")
    print(f"Roll number of team member used to get values of x and y:", rno)
    print("x =", x, ",y =", y+1)
    print("P.S. add calculation step to get values of x and y.", end="\n\n")
    print("Probability of actions:")
    print(
        tabulate(
            [
                ["Action", "Success", "Failure"],
                ["Left", x, 1-x],
                ["Right", x, 1-x]
            ],
            headers="firstrow",
            numalign="center",
            stralign="center",
            tablefmt="fancy_grid"
        ),
        end="\n\n"
    )
    print("Probability of observed states for given states:")
    print(
        tabulate(
            [
                ["", "Green", "Red"],
                ["Green", pt[y][1], 1-pt[y][0]],
                ["Red", 1-pt[y][1], pt[y][0]]
            ],
            headers="firstrow",
            numalign="center",
            stralign="center",
            tablefmt="fancy_grid"
        ),
        end="\n\n"
    )
    print("<Write formula here>", end="\n\n\n")
    bs = []
    for i in range(len(actions)):
        next_b = [0.0 for _ in range(l)]
        print("After action", i+1)
        a = actions[i]
        if a == "L":
            print("The action is Left", end="\n\n")
        else:
            print("The action is Right", end="\n\n")
        for j in range(l):
            print(f"s' = S{j+1}:")
            for k in range(l):
                next_b[j] += p(j, k, a) * b[k]
                if a == "L":
                    print(
                        f"P(S{j+1}|S{k+1},Left)b(s) = {p(j, k, a)} \\mul {b[k]} = {p(j, k, a) * b[k]}")
                else:
                    print(
                        f"P(S{j+1}|S{k+1},Right)b(s) = {p(j, k, a)} \\mul {b[k]} = {p(j, k, a) * b[k]}")
            print(f"\\sigma(for all s)(P(s'|s,a)b(s)) = {next_b[j]}")
            next_b[j] *= pe(percept[i], j)
            if percept[i] == "G":
                print(f"P(Green,S{j+1}) = {pe(percept[i], j)}")
            else:
                print(f"P(Red,S{j+1}) = {pe(percept[i], j)}")
            print(
                f"Therefore, the observed state value b'(S{j+1}) = {next_b[j]}", end="\n\n")
        val = sum(next_b)
        b = [m / val for m in next_b]
        bs.append([i+1]+copy.deepcopy(b))
        print(f"Therefore, the normalizing factor is {1.0 / val}")
        print(f"Hence, The new belief state b'=<{b[0]}", end="")
        for j in range(1, l):
            print(",", b[j], end="")
        print(">\nAnd now we assign b = b'", end="\n\n\n")
    bs = [["Action Number", "S1", "S2", "S3", "S4", "S5", "S6"]] + bs
    print("Hence, the belief states are:")
    print(tabulate(bs, headers="firstrow", numalign="center",
                   stralign="center", tablefmt="fancy_grid"), end="\n\n\n")

    print("Latex syntax of Probability of actions table:", end="\n\n")
    print(
        tabulate(
            [
                ["Action", "Success", "Failure"],
                ["Left", x, 1-x],
                ["Right", x, 1-x]
            ],
            headers="firstrow",
            numalign="center",
            stralign="center",
            tablefmt="latex"
        ),
        end="\n\n\n"
    )
    print("Latex syntax of Probability of observed states for given states table:", end="\n\n")
    print(
        tabulate(
            [
                ["", "Green", "Red"],
                ["Green", pt[y][1], 1-pt[y][0]],
                ["Red", 1-pt[y][1], pt[y][0]]
            ],
            headers="firstrow",
            numalign="center",
            stralign="center",
            tablefmt="latex"
        ),
        end="\n\n\n"
    )
    print("Latex syntax of belief states table is:", end="\n\n")
    print(tabulate(bs, headers="firstrow",
                   numalign="center", stralign="center", tablefmt="latex"))
