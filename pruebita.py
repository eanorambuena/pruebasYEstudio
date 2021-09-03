import eggdriver as ed

def f(x):
    return 10 ** x

def log():
    return ed.zero(f, 7, [0, 1], 8)

help(ed.zero)

print(log())
