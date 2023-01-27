a=int(input('Введите  длину шоколадки: '))
b=int(input('Введите  ширину шоколадки: '))
c=input('Введите  количество долек которое нужно отломить : ')
n=''
for i in range(1,a):
    n+=str(i*b)+' '
for i in range(1,b):
    n+=str(i*a)+' '   
if c in n:
    print('yes')
else:
     print('no')