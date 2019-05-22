"""print('\tabc')
print('a\tbc')
print('ab\tc')
print('abc\t')
letters = '1234567890'
print(letters[4])
soup='abcdefghjklmnopqrstuvwxyz'
print(soup[2:10:2])
print(len(soup))
todos='god soup.yay book. loop give'
print(todos.split('.'))
print(todos.split())
example=['Good','Yeti','Join']
example_join=', '.join(example)
print(example_join)
print(example_join.startswith('Good'))
print(example_join.center(100))
b = input('Введите какой-то число: ')
c = int(b)
f = input('Введите второе число: ')
g = int(f)
print((g*c)+10)
print(c)
if ( c > 10 ):
    count_book=input('Введите кол-во книг ')
    print(count_book)
elif(c<=10):
    count_magazine=input('Введите кол-во журналов ')
    print(count_magazine)
else:
    print('this is good idea')
list=[]
list.append('One')
list.append('Two')
list.append('Three')
for x in list:
    print(x)
a=[1,2,3,5,6,10,102]
for x in a:
    w=x*2
    print(w)
f = open("text.txt","r")
s= f.readline()
while s:
    print(s)
    s=f.readline()
f.close()
f = open("text.txt","a")
f.write("New commit"+"\n")
f.write("This is third commit"+"\n")
f.close()
sad= 'Ваня, Таня, Алёна'
sad.split()
print(sad.isdigit())"""
def delmat(s):
    spisok=['Пофиг','Скучно','Отвратительно']
    for x in spisok:
        s = s.replace(x,'*****')
    return s
print(delmat('Пофиг как мне на всякие там дела, очень Скучно и Отвратительно'))
sum = 0
for i in range(1,101):
    sum+=i
print(sum)

#0 1 1 2 3 5 8 ... ***
a=0
b=1
print(a)
print(b)
while(a+b<100):
    b=a+b
    a=b-a
    print(b)