import sys
z='IVXLCDM '
with open(sys.argv[1], 'r') as c:
    for s in c:
        n=int(s)
        p=0
        f=''
        while n>0:
            j=n%10
            if j in [4,9]:
                f=z[p*2]+(z[p*2+(1 if j==4 else 2)])+f
            else:
                f=z[p*2+1]*(j//5)+z[p*2]*(j%5)+f
            n//=10
            p+=1
        print(f)
