kg = int(input())

if (kg % 5 != 0) and (kg % 3 != 0):
    print(-1)
elif kg % 5 != 0:
    print(1)
else:
    a = kg // 5
    b = kg % 5 // 3
    print(a+b)

# 수정해야함~~~~