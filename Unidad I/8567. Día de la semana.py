datos = input("")
a,m,d = datos.split()
a = int(a)
m = int(m)
d = int(d)

if 0<=a and a <=10000 and 1<=m and m <=12 and 1<=d and d<=31:

    if m>2:
        m=m-2
        c = a/100
        e = a % 100
        e = int(e)
        b = (13 * m - 1) / 5 + e / 4 + c / 4
        b=int(b)
        f = (b + e + d + 5 * c) % 7
        f=int(f)
        if f==0:
            print(f-1,f,f+1)
        elif f==1:
            print(f-1,f,f+1)
        else:
            print(f-1,f,f+1)
    else:
        m=m+10
        a=a-1
        c=a/100
        e=a%100
        e = int(e)
        b=(13*m-1)/5+e/4+c/4
        b = int(b)
        f=(b+e+d+5*c)%7
        f = int(f)
        if f == 0:
            print(f - 1, f, f + 1)
        elif f == 1:
            print(f - 1, f, f + 1)
        else:
            print(f - 1, f, f + 1)

else:
    print("Introduce los datos corectamente")