
from kbhit import KBHit

kb = KBHit()

print('Hit any key, or ESC to exit')

while True:
    if kb.kbhit():
        c = kb.getch()
        c_ord = ord(c)
        print(c)
        print(c_ord)
        if c_ord == 27: # ESC
            break
        print(c)

kb.set_normal_term()
