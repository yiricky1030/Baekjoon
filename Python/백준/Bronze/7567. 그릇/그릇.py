plates=input()
ans=10
for i in range(1, len(plates)):
    if plates[i]==plates[i-1]:
        ans +=5
    else:
        ans +=10     
print(ans)