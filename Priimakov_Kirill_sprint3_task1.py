def f(n):
    cur=1
    if b == 1 :
        if n > 2:
            cur = f(n-1) + f(n-2)
        return cur
    elif b == 2:
        if n==1:
            cur=1
        elif n==2:
            cur=b+1
        elif n%2==0:
            cur=(f(n-1)*2)+1
        elif n%2==1:
            cur=(f(n-1)*2)-1
        return cur
    elif b==4:
        if n==1:
            cur=1
        elif n==2:
            cur=b+1
        elif n%2==0:
            cur=(f(n-1)*3)+2
        elif n%2==1:
            cur=(f(n-1)*2)-1
        return cur
        
        
    elif b==3:
        if n==1:
            cur=1
        elif n==2:
            cur=b+1
        elif n%2==0:
            cur=(f(n-2)*f(n-1))-1
        elif n%2==1:
            cur=(f(n-2)*f(n-1))+3
        return cur
        
    elif b ==5:
        if n==1:
            cur=1
        elif n==2:
            cur = b+1
        elif n%2==1:
            cur=(f(n-1)*2)-1
        elif n%2==0:
            cur=(f(n-2)*f(n-1))+5
        return cur   

a = int(input('Введите n часов: '))
b = int(input('Введите k семплов'))
value = f(a)
print('Всего файлов' + ' ' +str(value))
