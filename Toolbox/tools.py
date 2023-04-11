import subprocess
from os import chdir
import os

def sys(command):
    subprocess.run(command.split())

def command_read(command):
    try:
        result = subprocess.run(command.split(), stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as err:
        print(err)
        return None
    else:
        output = result.stdout.decode("utf-8")
        return output


def git_clone(link, route=""):
    for i in link.split():
        if route != "":
            chdir(route)
        sys(f"git clone {link}")


def clear():
    sys("clear")


def wget(link):
    sys(f"wget {link}")


def mkfs(format, partition, condition=""):
    if format or partition == "":
        print("no option selected")
    else:
        sys(f"mkfs.{format} {condition} {partition}")


def fetches(option):
    match option:
        case "neo":
            sys("neofetch")
        case "one":
            sys("onefetch")
        case "fresh":
            sys("freshfetch")
        case _:
            print("no option selected")

def cowsay(text, cow="", condition=""):
    sys(f"cowsay {text} -f {cow} {condition}")

def analize_dir(dir = ""):
    command_read("")
    print(os.listdir(dir),sys("ls -la"),sys("ls -a"))

def read_file(file):
    a1 = open(file,"r")
    a2 = a1.read()
    return a2

def makepkg(route =""):
    if route != "":
        chdir(route)
    sys("makepkg -si")
