import time 

begin = time.time() 

n = 32
print("Case 6: ")
numIteration = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        numIteration += 1
print(f'Number of Iterations: {numIteration}')

time.sleep(1) 
# store end time 
end = time.time() 
 
# total time taken 
print(f"Total runtime of the program is {end - begin}") 
# 1.0075609683990479
# 1.003605604171753
# 1.0008611679077148
# 1.0022995471954346
# 1.0100150108337402