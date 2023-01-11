''' Q.1 def getTemp(name, temp):
    print(name,temp)
getTemp("Bangalore", 26)
calculateTemp = getTemp
calculateTemp("Chennai",23)

#ANS - Bangalore 26 Chennai 23'''

'''Q2. def demo(n):
    return lambda x: x+n 
func = demo(85)
print(func(8))

#Ans --- 93'''

'''Q3. games = ['Swimming', "Rugby", 'VooleyBall','Javalin']
for g in games:
    print(g, len(g))
    
#ANS ----Swimming 8
Rugby 5
VooleyBall 10
Javalin 7'''

'''Q4.num = 3 
tempStr = "Solar System"
print(tempStr[:2]*num)

Ans ---- SoSoSo'''

'''Q5---a1,a2 = 80,70
while a1<=80:
    print(a1,end='|')
    a1,a2 = a2,a1-a2
    
#Ans ---80|70|10|60|-50|   '''

'''Q6 ---a1 = 99
a2 = 99
print(a1 is a2) 
#Ans--- True
'''

''' Q7. arr =(1 ,3, 2, 1, 0, 1, 3)

for num in arr:
    pass
    if(num == 0):
        out = num
        break
    elif (num%2 == 0):
        continue
    print(num)
print(out)

#Ans --- 1, 0'''

'''Q8.lst = ['M', 'O', 'O', 'O', 'N']
lst[3] = 'N'
lst[0:5] = ['Natural Satellite']
print(lst)

#Ans - ['Natural Satellite']'''

'''Q9.lst = [9, 99, 19, 89, 49]
size = len(lst) - 1
for i in range(size, -1,-1):
    print(lst[i])
#Ans    
49
89
19
99
9    '''

'''Q10 .str1 = "Stars are the most widely2021 recognized Astronomical objects12"
out = []
new = str1.split()
for item in new:
    if any(char.isdigit() for char in item):
        out.append(item)
for i in out:
    print(i)
#Ans
widely2021
objects12'''

'''Q11. demo={'cat':{},'puppy':{}}
print(list(demo.values()))
 
#Ans ----[{}, {}]   '''

'''Q12. def processString(str):
    return str[:2].lower() + str[1:]
out = processString('SatEllITe')
print(out)

#Ans ----saatEllITe'''

''' Q13 . sports = ['basketball', 'football','swimming','kickball','judo']
outList = sports[1:3]
print(", ".join(outList))

#ans --- football, swimming'''








