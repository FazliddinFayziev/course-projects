# Please include names of your group members.

# One submission per group.

"""
Group Class Exercise 1
    1. Analyze the programs shown below
        and discover fastest and slowest ones (50 Points)?
    2. What are the time complexities for the program shown below (50 Points)?
"""

# Case 1:
n = 32
print(f"Number of Samples: {n}")
print("Case 1: ")
numIteration = 0
for i in range(n):
    numIteration += 1
print(f'Number of Iterations: {numIteration}')

# Case 2:
print("Case 2: ")
numIteration = 0
i = 1
while i < n:
    i *= 2
    numIteration += 1
print(f'Number of Iterations: {numIteration}')

# Case 3:
print("Case 3: ")
numIteration = 0
for i in range(n):
    j = 1
    while j < n:
        j *= 2
        numIteration += 1
print(f'Number of Iterations: {numIteration}')

# Case 4:
print("Case 4: ")
numIteration = 0
for i in range(n):
    for j in range(n):
        numIteration += 1
print(f'Number of Iterations: {numIteration}')

# Case 5:
print("Case 5: ")
numIteration = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            numIteration += 1
print(f'Number of Iterations: {numIteration}')

# Case 6:
print("Case 6: ")
numIteration = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        numIteration += 1
print(f'Number of Iterations: {numIteration}')