#beep

import winsound
import time

for i in range(1,5):
    for j in range(1,5):
        winsound.Beep(100*j*i, 50)
        time.sleep(0.01)
    time.sleep(0.01)
