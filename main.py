dict={"brand":"ford","model":"ford","brand":1966}
dict['brand']=95
print(dict)
dict["new"]="yes"
print(dict)
dict.pop("brand")
print(dict)
del dict['model']
print(dict)
set1 ={"apple" ,"banana","cherry","apple"}
print(set1)
print(set1)
set1.add("mango")
print(set1)
set1.update(["orange","grapes"])
print(set1)
set1.discard("ab")
print(set1)
set2={1,2,3}
set1.update(set2)
print(set1)

s= {4,5,6}
t={7,8,9}
s.update(t)
print(s)