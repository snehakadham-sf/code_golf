import sys
with open(sys.argv[1], 'r') as c:
    for s in c:
        s=s.strip()
        p=0
        z='IVXLCDM '
        f=''
        for i in s[::-1]:
            j=int(i)
            if j in [4,9]:
                f=z[p*2]+(z[p*2+(1 if j==4 else 2)])+f
            else:
                f=z[p*2+1]*(j//5)+z[p*2]*(j%5)+f
            p+=1
        print(f)
