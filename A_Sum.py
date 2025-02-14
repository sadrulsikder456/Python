test=int (input())
for _ in range(test):
    first,second,third=map(int,input().split())
    if first + second == third or first + third == second or second + third == first:
        print("YES")
    else:
        print("NO")
