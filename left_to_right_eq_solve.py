def l2reval(a):
    f = ""
    c = 0
    new_f = ""
    for i in a:
        f += i
        if i in ["-", "+", "/", "*"]:
            c += 1
            if c == 2:
                new_f = str(eval(f[:-1]))
                new_f += f[-1]
                f = new_f
                c = 1
    return eval(f)
