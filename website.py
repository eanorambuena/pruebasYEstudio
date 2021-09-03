import eggdriver as ed
ed.installFromRequests(["twill"], False)

from twill.commands import *
go("https://www.virustotal.com/gui/home/url")
showforms()

def printf(*args):
    [print(i) for i in args]

printf(1, "hola", 56, True, "a")