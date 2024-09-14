# Isprintable

#------1------
string1="hello,world"
print(string1.isprintable()) 
#------2------
string2="hello\nworld"
print(string2.isprintable())
#------3------
string3="python\tprogramming"
print(string3.isprintable())
#------4------
string4="python\njava\njavascript\tc++\nC"
print(string4.isprintable())
#------5------
string5="web&&**!!"
print(string5.isprintable())
# Isspace

#------1------
string6="  "
print(string6.isspace())
#------2------
string7="python     "
print(string7.isspace())
#------3------
string8="developers"
print(string8.isspace())
#------4------
string9="   python   "
print(string9.isspace())
#------5------
string10="python\njava\njavascript\tc++\nC"
print(string10.isspace())
# join

#------1------
list1=["python","is","the","easiest","high","level","language"]
print(" ".join(list1))
#------2------
list2=["python","is","the","easiest","high","level","language"]
print(",".join(list2))
#------3------
list3=["hello","world"]
print(" -------".join(list3))
#------4------
list4=["W","e","b","d","e","v","e","l","o","p","e","r"]
print("".join(list4))
#------5------
list5=["h","e","l","l","o"]
print("!".join(list5))
# use join in tuple

#------1------
tuple1=("python","is","the","easiest","high","level","language")
print(" ".join(tuple1))
#------2------
tuple2=("W","e","b","d","e","v","e","l","o","p","e","r")
print(",".join(tuple2))
#------3------
tuple3=("h","e","l","l","o")
print("".join(tuple3))
#------4------
tuple4=("h","a","m","n","a")
print("#".join(tuple4))
#------5------
tuple5=("N","e","o","T","e","c","h")
print("   ".join(tuple5))

#just
#------1------
string11="python beginners"
print(string11.ljust(20,"*"))
#------2------
string12="developers"
print(string12.rjust(20,"*"))
#------3------
string13="python developers"
print(string13.ljust(10,"*"))
#------4------
string14="practice,work"
print(string14.rjust(30))
#------5------
string15="artificial intelligence"
print(string15.ljust(30,"!"))

# strip
#------1------
string21="   python   "
print(string21.strip())
#------2------
string22="123python\n developers321"
print(string22.strip())
#------3------
string23="artificial intelligence"
print(string23.strip("a"))
#------4------
string24="!!!!"
print(string24.strip("!"))
#------5------
string25=" @@@python@@@"
print(string25.strip("@@@"))



# Dict
#------1------
dict1={"name":"hamna","age":18,"city":"grw"}
print(dict1["name"])
#------2------
dict2={"a":"hamna","b":"sadiq","c":"iqbal"}
print(dict2["b"])
#------3------(del)
dict2={"a":"hamna","b":"sadiq","c":"iqbal"}
del dict2["a"]
print(dict2)
#------4------(del)
dict3={"1":"moana","2":"red","3":"jack"}
del dict3["2"]
print(dict3)
#------5------(del)
dict4={"A":"ELSA","B":"ANNA","C":"OLAF"}
del dict4["C"]
print(dict4)

# clear()
#-----1------
dict5={"1":"gen","2":"al","3":"programmer"}
dict5.clear()
print(dict5)
#-----2------
dict6={"A":"ELSA","B":"ANNA","C":"OLAF"}
dict6.clear()
print(dict6)
#-----3------
dict7={"1":"moana","2":"red","3":"jack"}
dict7.clear()
print(dict7)

#copy()
#-----1------
dict8={"1":"what","2":"where","3":"who"}
dict8.copy()
print(dict8)
#-----2------
dict9={"A":"flynn","B":"mauvi","C":"halo"}
dict9.copy()
print(dict9)
#-----3------
dict9={"1":"maximum","2":"minimum","3":"average"}
dict9.copy()
print(dict9)

#fromkeys()
#------1-----
key1=('a','b','c')
print(dict.fromkeys(('a','b','c'),'hamna'))
#------2------
key1=('a','b','c')
print(dict.fromkeys(('a','b','c'),' hamna sadiq iqbal'))
#------3------
key=('A','B','C')
print(dict.fromkeys(('A','B','C'),[]))
#------4------
Dict:dict=dict.fromkeys(('a','b','c'),[])
print(Dict)
Dict['a']=[input("write any value: ")]
Dict['b']=[input("write any value: ")]
Dict['c']=[input("write any value: ")]
print(Dict)
#------5-----
Dict2:dict=dict.fromkeys(('value1','value2','value3'),"")
print(Dict2)
Dict2['value1']=input("No:  ")
Dict2['value2']=input("No:  ")
Dict2['value3']=input("No:  ")
print(Dict2)

# pop()
#-----1-----
dict13={"1":"maximum","2":"minimum","3":"average"}
dict13.pop("2")
print(dict13)
#-----2------
dict14={"1":"gen","2":"al","3":"programmer"}
dict14.popitem()
print(dict14)
#-----3------
dict15={"a":"hamna","b":"sadiq","c":"iqbal"}
dict15.popitem()
print(dict15)

# update
#-----1-----
dict16={"1":"a","2":"b"}
dict17={"3":"c","4":"d"}
dict16.update(dict17)
print(dict16)
#-----2------
dict18={"1":"hamna","2":"noor","3":"efra"}
dict19={"4":"sadiq","5":"iqbal"}
dict18.update(dict19)
print(dict18)
#-----3-----
dict20={"4":"arcane","5":"alita","6":"battle"}
dict21={"7":"vital"}
print(dict20.update(dict21)) 

#setdefault
#-----1-----
dict22={"1":"a","2":"b","3":"c"}
print(dict22.setdefault("1","d"))
#-----2------
dict23={"1":"hamna","2":"sadiq","3":"iqbal"}
print(dict23.setdefault("1","noor"))
#-----3-----
dict24={"1":"arcane","2":"alita","3":"battle"}
print(dict24.setdefault("1","vital"))
