#time operations test : time sum

from datetime import *

horas = {"t1": time(1, 10, 2), "t2": time(2,20,10)}




for i in range(0,30,1):
    h = horas["t1"].hour
    m = horas["t1"].minute
    s = horas["t1"].second

    h = h+horas["t2"].hour
    m = m+horas["t2"].minute
    s = s+horas["t2"].second

    if s>59:
        s=s-59
        m = m+1
    
    if m>59:
        m = m-59
        h = h+1
    
    if h>23:
        h = h-23

    horas["t1"] = time(h, m, s)
    print(horas["t1"])

current_time = time(datetime.now().hour, datetime.now().minute, datetime.now().second)
print(current_time)

