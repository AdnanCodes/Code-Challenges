import time

# Setup an input to demonstrate log n, n, n log n, n^2, n^3
start = time.time()
n = 100

# Some examples to showcase the total runtime
# Use time.sleep() to demo processing speed
# n = 10 will be 16secs
# n = 20 will be 72secs

# Remember the math behind runtime based on no. of delays set up 
# Runtime is O(n^2) @ 10 => @ 20 (2^2n^2) becomes 4x more time to complete

i = 1

# log n
while i <= n:
    time.sleep(0.2)
    print(i)
    i *= 2

print('Your Input is :', n)
print("Total time taken :", time.time() - start)


# Other type loops to use

# n time
# while i <= n:
#     time.sleep(0.2)
#     print(i)
#     i += 1

# n log n
# j = 1
# while i <= n:
#     time.sleep(0.2)
#     while j <= i:
#         time.sleep(0.2)
#         j *= 2
#         print(i)
#     i += 1

# n^2
# j = 1
# while i < n:
#     time.sleep(0.2)
#     while j <= i:
#         time.sleep(0.2)
#         j += 1

# n^3
# j = 1
# k = 1

# while i < n:
#     time.sleep(0,2)
#     while j <= i:
#         time.sleep(0.2)
#         j += 1
#         while k <= j:
#             time.sleep(0.2)
#             k += 1
#     i += 1
