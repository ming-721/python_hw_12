# 과제 32
nums = list(map(int,input("좋아하는 숫자 10개 입력: ").split()))

set1 = set(nums[:5])
set2 = set(nums[5:])

print("합집합 = ", set1 | set2)
print("교집합 = ", set1 & set2)

# 과제 33
nums = list(map(int,input("좋아하는 숫자 10개 입력: ").split()))

set1 = set(nums[:5])
set2 = set(nums[5:])

print("차집합 = ", set1 - set2)
print("대칭차집합 = ", set1 ^ set2)

# 과제 34
nums = map(int,input("좋아하는 숫자 5개 입력: ").split())

myset = set(nums)
myset.update( {100} )

print(myset)

# 과제 35
a = {100, 200, 300, 400, 500}

a1 = a.copy()
a1.intersection_update( {400, 500, 600, 700, 800})
print(a1)

a2 = a.copy()
a2.difference_update( {400, 500, 600, 700, 800})
print(a2)

a3 = a.copy()
a3.symmetric_difference_update( {400, 500, 600, 700, 800})
print(a3)

# 과제 36
a = {100, 200, 300, 400, 500}

if a >= {100, 200, 300, 400, 500} and a <= {100, 200, 300, 400, 500}:
    print("동시")
elif a >= {100, 200, 300, 400, 500}:
    print("상위")
elif a <= {100, 200, 300, 400, 500}:
    print("부분")

# 과제 37
a = set(map(int,input("좋아하는 숫자 5개 입력: ").split()))

a.add(1000)
a.remove(1000)

print(a)

# 과제 38
multiples = {x for x in range(1,101) if x % 3 == 0 and x % 5 ==0}
print(multiples)