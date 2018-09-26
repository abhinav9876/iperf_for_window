n,m,x=list(map(int,input().split(" ")))
s=list(map(int,input().split(" ")))
t=list(map(int,input().split(" ")))
s.sort()
t.sort()
mini1=max(s)+max(t)-min(s)-min(t)
mini2=max(s)+max(t)-min(s)-min(t)
while True:
    s[-1]=s[-1]-x
    t[-1]=t[-1]-x
    s.sort()
    t.sort()

    mini1=max(s)+max(t)-min(s)-min(t)
    if mini2<=mini1:
        mini2=max(s)+max(t)-min(s)-min(t)
    else:
        break
print(mini2)        
