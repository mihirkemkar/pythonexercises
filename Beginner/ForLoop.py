
divisible = list ()
m = 2
n = 3
for i in range(1,51):
    if(i % m == 0 or i % n == 0):
        divisible.append(i)

print("The numbers divisible by 2 and 3 : ", divisible)
i = i + 1

