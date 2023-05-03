import sys

N, result, temp, cnt = 0
N = input()
for i in range(0,N):
    temp = input()
    for div in range(1,temp):
        if(temp%div==0):
            cnt+=1
        if(cnt==2):
            result+=1
        cnt=0

print(result)