a=[4,3,2,1]
b=[]
c=[]

def display ():
    print("%10s %10s %10s"%(a,b,c))

def solveHanoi(n,src,dst,aux):
    if n==1:
        dst.append(src[-1])
        del src[-1]
        display()

    else:
        solveHanoi(n-1,src,aux,dst)
        dst.append(src[-1])
        del src[-1]
        display()
        solveHanoi(n-1,aux,dst,src)
    
display()
solveHanoi(4,a,c,b)