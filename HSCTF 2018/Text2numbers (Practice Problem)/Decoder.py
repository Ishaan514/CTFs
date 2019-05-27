chars = [23, 5, 12, 12, 27, 20, 8, 5, 27, 6, 12, 1, 7, 27, 9, 19, 27, 8, 9, 4, 4, 5, 14, 27, 8, 5, 18, 5, 27, 2, 21, 20, 27, 6, 9, 18, 19, 20, 27, 23, 5, 27, 8, 1, 22, 5, 27, 19, 15, 13, 5, 27, 20, 5, 24, 20, 27, 20, 15, 27, 3, 15, 14, 6, 21, 19, 5, 27, 25, 15, 21, 27, 14, 15, 23, 27, 20, 8, 5, 27, 6, 12, 1, 7, 27, 9, 19, 27, 9, 14, 27, 6, 1, 3, 20, 27, 19, 5, 3, 18, 5, 20, 19, 28, 1, 18, 5, 28, 8, 9, 4, 4, 5, 14, 28, 9, 14, 28, 20, 8, 9, 19, 28, 12, 9, 19, 20, 27, 4, 15, 14, 20, 27, 9, 14, 3, 12, 21, 4, 5, 27, 20, 8, 5, 27, 16, 1, 18, 20, 19, 27, 20, 8, 1, 20, 27, 1, 18, 5, 27, 19, 5, 16, 5, 18, 1, 20, 5, 4, 27, 23, 9, 20, 8, 27, 19, 16, 1, 3, 5, 19]

exp = []
for x in chars:
    if x == 1:
        exp.append("a")
    if x == 2:
        exp.append("b")
    if x == 3:
        exp.append("c")
    if x == 4:
        exp.append("d")
    if x == 5:
        exp.append("e")
    if x == 6:
        exp.append("f")
    if x == 7:
        exp.append("g")
    if x == 8:
        exp.append("h")
    if x == 9:
        exp.append("i")
    if x == 10:
        exp.append("j")
    if x == 11:
        exp.append("k")
    if x == 12:
        exp.append("l")
    if x == 13:
        exp.append("m")
    if x == 14:
        exp.append("n")
    if x == 15:
        exp.append("o")
    if x == 16:
        exp.append("p")
    if x == 17:
        exp.append("q")
    if x == 18:
        exp.append("r")
    if x == 19:
        exp.append("s")
    if x == 20:
        exp.append("t")
    if x == 21:
        exp.append("u")
    if x == 22:
        exp.append("v")
    if x == 23:
        exp.append("w")
    if x == 24:
        exp.append("x")
    if x == 25:
        exp.append("y")
    if x == 26:
        exp.append("z")
    if x == 27:
        exp.append(" ")
    if x == 28:
        exp.append("_")

print(exp)
