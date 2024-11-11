

ipaddress = '192.168.0.1'
greet = 'Hello World'
# s = ipaddress.split('.')
# print(s)
a = [int(i) for i in ipaddress.split('.') if int(i) > 0]
b = [i for i in range(2, 11, 2)]
c = [i for i in greet if i.isupper()] #isuper()
d = [(pos, char) for pos, char in enumerate(greet)]

print (a)
print(b)
print(c)
print(d)
