import random
import time

a = 5
b = 3
c = 1

while a*100+b*10+c>366:
    a = (random.randint(0, 9))
    b = (random.randint(0, 9))
    c = (random.randint(0, 9))
    if 1<=a*100+b*10+c<=366:
        break

k = 6
l = 1

while 2 < k*10+l < 95:
    k = (random.randint(0, 9))
    l = (random.randint(0, 9))
    if k*10+l >=95 or k*10+l <=2:
        break

d = 0
e = 0
f = 0
g = 0
h = 0
i = 1

key7bit = (d+e+f+g+h+i)%7
           
while (key7bit != 0):
    d = (random.randint(0, 9))
    e = (random.randint(0, 9))
    f = (random.randint(0, 9))
    g = (random.randint(0, 9))
    h = (random.randint(0, 9))
    i = (random.randint(0, 9))
    key7bit = (d+e+f+g+h+i)%7
    if key7bit == 0:
        break
    
j = 0
m = (random.randint(0, 9))
n = (random.randint(0, 9))
o = (random.randint(0, 9))
p = (random.randint(0, 9))
q = (random.randint(0, 9))


print ('欢迎使用Windows 95密钥生成工具！')
print ('（0.1-Beta-2-OSR）')
print ('此工具可以快速帮你生成Windows 95的密钥！')
print ('严禁用于非法用途！')
print ('否则所造成的一切后果均与作者无关！')

print ()
print ('此次生成的密钥是：')
print (a,b,c,k,l,'- O E M -',j,d,e,f,g,h,i,'-',m,n,o,p,q,set='')

time.sleep(20)
