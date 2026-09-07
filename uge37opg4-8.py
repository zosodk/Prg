digits=[]
for value in range(1, 11):
    digits.append(value ** 3)
i=1
for cube in digits:
    print(f"Kubik tallet af værdierne fra {i} er {cube}")
    i+=1