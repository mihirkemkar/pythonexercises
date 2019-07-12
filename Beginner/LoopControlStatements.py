multiples = list ()

for i in range(1,100):
    if (i % 3 ==0):
        continue
    else:
        multiples.append(i)
i = i + 1
print(multiples)
