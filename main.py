import sys
from functools import lru_cache
from termcolor import cprint
import time
import playsound
import random
import os


@lru_cache(32)
def cached_listdir(d):
    return os.listdir(d)


cprint('''
╭━━╮╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭╮┃╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱┃┃
┃╰╯╰┳━━┳━━┳╮╭╮┃╰━━┳━━┳━━┳━━┳━╯┃
┃╭━╮┃╭╮┃╭╮┃╰╯┃╰━━╮┃╭╮┃━━┫┃━┫╭╮┃
┃╰━╯┃╰╯┃╰╯┃┃┃┃┃╰━╯┃╰╯┣━━┃┃━┫╰╯┃
╰━━━┻━━┻━━┻┻┻╯╰━━━┻━━┻━━┻━━┻━━╯
''', 'green', end="")

try:
    while True:
        try:
            cprint("Введите максимальный интервал вызова звуков (секунды):",
                   'yellow')
            interval_seconds_max = int(input())
            break
        except ValueError:
            cprint("Введите целое число!", "red")

    while True:
        filename = random.choice(cached_listdir('./Collections/'))
        playsound.playsound('./Collections/{}'.format(filename), True)
        cprint("Файл был проигран: {}".format(filename), "green")
        sleep = random.randint(1, interval_seconds_max)
        time.sleep(sleep)
except KeyboardInterrupt:
    cprint("Надеюсь ваши соседи стали тише ;)", "magenta")
    sys.exit()
