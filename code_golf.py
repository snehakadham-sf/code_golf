import sys
z='IVXLCDM '
for s in open(sys.argv[1]):
    n=int(s)
    p=0
    f=''
    while n>0:
        j=n%10
        f=(z[p*2]+(z[p*2+j//4]) if j in [4,9] else z[p*2+1]*(j//5)+z[p*2]*(j%5))+f
        n//=10
        p+=1
    print(f)
