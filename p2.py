n = int(input())
a = []
b = []
c = []
d = []
e = []
o = []
j = [0, 9, 10, 11, 12]
z = [0, 1, 10, 11, 12]
for _ in range(n):
    s = input().split(' ')
    for i in s:
        x = int(i) % 13
        e.append(x)
        sorted(a)
        f = set(a)
        if

        if 1 <= int(i) <= 13:
            a.append(s)
        elif 14 <= int(i) <= 26:
            b.append(s)
        elif 27 <= int(i) <= 39:
            c.append(s)
        else:
            d.append(s)
    if (len(a) >= 5 or len(b) >= 5 or len(c) >= 5 or len(d) >= 5) and ( or j in a):
        print('7')
    elif a[0] == a[1] == a[2] == a[3] or a[1] == a[2] == a[3] == a[4]:
        print('6')
    elif len(set(a)) == 2:
        print('5')
    elif k == 'Y' or a == z:
        print('4')
    elif len(set(a)) == 3 and (a[0] == a[1] == a[2] or a[1] == a[2] == a[3] or a[2] == a[3] == a[4]):
        print('3')
    elif len(set(a)) == 3:
        print('2')
    elif len(set(a)) == 2:
        print('1')
    else:
        print('0')
