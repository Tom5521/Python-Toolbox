class c:
    def black(self):
        return f"\033[30m{self}\033[0m"

    def red(self):
        return f"\033[31m{self}\033[0m"

    def green(self):
        return f"\033[32m{self}\033[0m"

    def yellow(self):
        return f"\033[33m{self}\033[0m"

    def blue(self):
        return f"\033[34m{self}\033[0m"

    def magenta(self):
        return f"\033[35m{self}\033[0m"

    def cyan(self):
        return f"\033[36m{self}\033[0m"

    def white(self):
        return f"\033[37m{self}\033[0m"


class bg:
    def black(self):
        return f"\033[40m{self}\033[0m"

    def red(self):
        return f"\033[41m{self}\033[0m"

    def green(self):
        return f"\033[42m{self}\033[0m"

    def yellow(self):
        return f"\033[43m{self}\033[0m"

    def blue(self):
        return f"\033[44m{self}\033[0m"

    def magenta(self):
        return f"\033[45m{self}\033[0m"

    def cyan(self):
        return f"\033[46m{self}\033[0m"

    def white(self):
        return f"\033[47m{self}\033[0m"


class bc:
    def black(self):
        return f"\033[1;30m{self}\033[0m"

    def red(self):
        return f"\033[1;31m{self}\033[0m"

    def green(self):
        return f"\033[1;32m{self}\033[0m"

    def yellow(self):
        return f"\033[1;33m{self}\033[0m"

    def blue(self):
        return f"\033[1;34m{self}\033[0m"

    def magenta(self):
        return f"\033[1;35m{self}\033[0m"

    def cyan(self):
        return f"\033[1;36m{self}\033[0m"

    def white(self):
        return f"\033[1;37m{self}\033[0m"
