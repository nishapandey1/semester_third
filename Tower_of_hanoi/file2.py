import time

s=time.time()

print("Hello")

print("Hi EveryOne")

e=time.time()

print(e-s)

#It gives more accurate result.

from timeit import default_timer as timer

start = timer()

print(23*2.3)

end = timer()

print(end - start)