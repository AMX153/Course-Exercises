'''import json
import requests'''

'''url = 'http://api.open-notify.org/astros.json'#adrese darkhasti
response = requests.get(url)    #vorod be adrese ersali

print(f"The status code is: {response.status_code}. \n")   #agar 200 bod dorost ast

data_json = response.json()
print(f"The number is: {data_json['number']}.")
print(f"The people are: {data_json['people']}.")

for person in data_json['people']:
    print(f"The name is: {person['name']}. and the craft is: {person['craft']}.")'''

#mafahim pishrafte aedad
'''hex(12) #16
oct(12) #8
bin(12) #binary
pow(2, 10)  #tavan
pow(2, 8, 100)  #mohasebe tavan va ersal baghimande an be 100 ya har adad digar
abs(-3) #ghadre motlagh'''

#reshteha
'''a = "amir is here"
print(a.upper())    #tabdil be horofe bozorg
print(a.lower())    #tabdil be horofe kochak
print(a.capitalize())   #tabdil harf aval be halat bozorg
print(a.title())    #tabdil matn be neveshte titr 
print(a.islower())  #check kardan kalame ya ebarat be jahate kochak bodan
print(a.count("i")) #peyda kardan tedade i dar ebarat
print(a.find("i"))  #peyda kardan makan harf ersali ya har karakter digar
print(a.title().center(50)) #gharar dadane ebarat ya kalame dar vasat va eyjade fasele dar ebteda va enteha
print(a.title().center(50, '*'))
print(a.title().center(50, "-"))
print(a.split())    #joda kardan barasase fasele ya meghdare delkhah
print(a.partition("i"))   #bakhsh bakhsh kardan barasase meghdare delkhag

b = ["Amir", "Ava", "Sara", "Sina"]
"-".join(b) #ezafe kardan meghdare delkhah be maghadir list'''

#majmoe
'''a = set()   #eyjade majmoe
a.add(1)    #afzodane meghdar be majmoe
a.add(2)
a.add(3)
a.add(4)
a.remove(2) #delete meghdar az majmoe(hatman bayad dar majmoe bashd)
a.discard(10)   #delete meghdar az majmoe(elzami be vojod nist)
a.clear()   #delete tamame maghdir majmoe
print(a)
x = {1, 2, 3}
y = x   #darsorate afzodane meghdar be x, y niz taghir mikonad
x.add(10)
print(y)
c = {1, 2, 3}
d = {}
d = c.copy()    #darsorate afzodane meghdar be c, d taghiri nemikonad
c.add(10)
print(d)
s1 = {1, 2, 3}
s2 = {4, 5, 3}
s1.difference(s2)   #peyda kardane meghdar ya maghadir motefavet do majmoe
s1.difference_update(s2)    #peyda kardan meghdar ya maghdir motefavet va hazfe an az majmoe aval
print(s1)

a1 = {1, 2, 3}
a2 = {4, 5, 3}
a1.intersection_update(a2)  #peyda kardan taghato ya eshterak
print(s1)

b1 = {1, 2}
b2 = {2, 3}
b1.isdisjoint(b2)   #check kardan ertebat, True: hich eshteraki nadaran False: eshterak daran
b1.issubset(b2)     #check zir majmoe bodan

c1 = {1, 2, 3}
c2 = {4, 5, 6}
print(c1.union(c2)) #ejtema do majmoe'''


#dictionary

'''[(x ** 2) for x in [1, 2, 3]]
{x: (x ** 2) for x in [1, 2, 3]}'''

#list

'''a = [1, 2, 3, 4]
a.append(5)     #afzodan meghdar be list(list mitavanad meghdar tekrari dashte bashad)
a.insert(0, "Amir") #ezafe kardan meghdar dar makan delkhah
b = [10, 20, 30, 40, 50]
b.pop()     #delete akharin meghdar be to pishfarz va bargashte meghdar delete shode'''

#itertools

import itertools as it

x = it.cycle(["Server1", "Server2", "Server3"])
next(x)
a = [1, 2, 3, 4, 5, 6]
list(it.combinations(a, 2))     #bargashte tarkib haye 2 taye ya meghdar haye digar
list(it.combinations_with_replacement(a, 2))    #bargashte majmoe haye tekrari