a=input('Введите  номер билетика: ')
n=0
for i in range(3):
    n+=int(a[i])
m=0
for i in range(3,6):
    m+=int(a[i])
if m==n:
    print('yes')
else:
    print('no')
