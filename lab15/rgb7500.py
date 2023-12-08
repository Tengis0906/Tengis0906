import sys
sys.stdin = open('rgb7500.in','r')
sys.stdout = open('rgb7500.out''w')
s = []
n = int(input())
for i in range(n):
    m = int(input())
    s.append(m)
j = sum(s)
print(j)