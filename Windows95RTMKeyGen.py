import random
import time

a = 5
b = 5
c = 5

while a*100+b*10+c == 333 or 444 or 555 or 666 or 777 or 888 or 999:
    a = (random.randint(0, 9))
    b = (random.randint(0, 9))
    c = (random.randint(0, 9))
    if a*100+b*10+c != 333 or 444 or 555 or 666 or 777 or 888 or 999:
        break
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 1

key7bit = (d+e+f+g+h+i+j)%7
while (key7bit != 0):
    d = (random.randint(0, 9))
    e = (random.randint(0, 9))
    f = (random.randint(0, 9))
    g = (random.randint(0, 9))
    h = (random.randint(0, 9))
    i = (random.randint(0, 9))
    j = (random.randint(0, 9))
    key7bit = (d+e+f+g+h+i+j)%7
    if key7bit == 0:
        break

print ('欢迎使用Windows 95密钥生成工具！')
print ('（0.1-Beta-2-RTM）')
print ('此工具可以快速帮你生成Windows 95的密钥！')
print ('严禁用于非法用途！')
print ('否则所造成的一切后果均与作者无关！')

print ()
print ('此次生成的密钥是：')
print (a,b,c,'-',d,e,f,g,h,i,j,sep='')

print ('20秒后自动退出……')
time.sleep(20)

