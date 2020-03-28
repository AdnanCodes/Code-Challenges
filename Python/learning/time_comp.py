import time

start = time.time()
n = 8192

# n = 10 will be 16secs
# n = 20 will be 72secs

# Runtime is O(n^2) @ 10 => @ 20 (2^2n^2) becomes 4x more time to complete

i = 1
while i <= n:
    time.sleep(0.2)
    print(i)
    i *= 2

print('Your Input is :', n)
print("Total time taken :", time.time() - start)
