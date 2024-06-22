import sys
from termcolor import colored, cprint
from time import sleep

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')


def print_red_on_cyan(x): return cprint(x, 'red', 'on_cyan')


print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
	cprint(i, 'magenta', end=' ')
	sleep(0.1)

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)
