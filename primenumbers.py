def pries():
    p=int(input('enter number'))
    if p<2:
        return 0
    prime=[2]
    x=3
    while x<p:
        for y in range(3,x,2):
            if x%y==0:
                x+=2
                break
        else:
            prime.append(x)
            x+=2
    print(prime)
    print(len(prime))
pries()