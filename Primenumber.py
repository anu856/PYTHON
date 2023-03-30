def getprimrnuber(N):
    factor=list()
    divisor=2
    while(divisor<=N):
        if(N%divisor)==0:
            factor.append(divisor)
            N=N/divisor
        else:
                divisor+=1
    return factor    
print(getprimrnuber(900))
