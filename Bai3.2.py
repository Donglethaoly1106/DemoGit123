M1=int(input('M1='))
M2=int(input('M2='))
M3=int(input('M3='))
S=int(input('S='))
if S<=100:
    tien=M1*S
    print('Phai tra=',tien,sep="")
elif 101<=S<=150:
    tien=M1*100+M2*(S-100)
    print('Phai tra=', tien,sep="")
elif S>=151:
    tien=M1*100+M2*50+M3*(S-150)
    print('Phai tra=', tien,sep="")