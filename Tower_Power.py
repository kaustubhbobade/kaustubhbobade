'''Consider you have given an array of buildings' heights. 
Let i be the current index and l and r be the leftmost and rightmost index satisfying this property a[l]>a[l+1]>.....>a[i-1]>a[i]<a[i+1]<a[i+2]<....<a[r], 
then (r-l+1) is the power of that ith building.

Task: Find power of all indexes in the array.

Example: let A=[7, 2, 1, 5, 7, 9]
Answer: [1, 2, 6, 3, 2, 1]

Constraints:
1<=t<=20000
1<=n<=500000
1<=A[i]<=10^9
'''
for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split(' ')]
    less=[1]*len(a)
    more=[1]*len(a)
    for i in range(len(a)-1,0,-1):
        if a[i]>a[i-1]:
            less[i-1]=less[i]+1
    for i in range(1,len(a)):
        if a[i]<a[i-1]:
            more[i]=more[i-1]+1
    for i in range(len(a)):
        print(less[i]+more[i]-1,end=' ')
    print()
