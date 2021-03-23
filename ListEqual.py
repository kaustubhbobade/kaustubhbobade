'''You have given a list suppose A. You can perform following operations as many times as you want.

1. Choose any element and add or subtract 3 to/from element at a cost of 1.
2. Choose any element and add or subtract 2 to/from element at free of cost.

Task: Find how much cost required to make all elements of list equal

Ex: A=[3,5,2,3]
Ans:1
Explaination: Make all 3 as 5 by adding 2. Add 3 in 2 to get 5 at a cost of 1.'''

# Python Code
for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split(' ')]
    res=0
    for i in a:
        if i%2==1:
            res+=1
    if res==0:
        print(res)
    else:
        print(n-res)
