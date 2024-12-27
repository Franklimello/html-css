import time

for i in range(100):
    time.sleep(0.1)
    print((i), end='\r')

print('fim!')