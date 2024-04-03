from time import sleep

while not ((t := input("How long do you want to wait: ")).isnumeric()): pass

t = int(t)

while t > 0:
    mins, sec = divmod(t, 60)
    if mins >= 60: 
        hours, mins = divmod(mins, 60)
        print(f"{hours:02d}:{mins:02d}:{sec:02d}", end = "\r")
    else: print(f"{mins:02d}:{sec:02d}", end = "\r")
    sleep(1)
    t -= 1

print("\n\nDone!\n\n")