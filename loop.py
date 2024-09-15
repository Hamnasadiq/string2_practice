# for loop with string
#-----1-----
string1="bye,world"
for i in string1:
    print(i)
#-----2-----
string2="programmers"
for j in string2:
    print(j)
#for loop with range
#-----1-----
for k in range(5):
    print(k)
#-----2-----
for l in range(1,6):
    print(l)
#------3-----
for m in range(1,6,2):
    print(m)
#for loop in list
#-----1-----
list1=[1,2,3,4,5]
for n in list1:
    print(n)
#-----2-----
list2=["a","b","c","d","e"]
for o in list2:
    print(o)
#for loop in tuple
#-----1-----
tuple1=(1,2,3,4,5)
for p in tuple1:
    print(p)
#-----2-----
tuple2=("a","b","c","d","e")
for q in tuple2:
    print(q)
#for loop in dict
#-----1-----
dict1={"1":"Achlys","2":30,"country":"pakistan"}
for key in dict1:
    print(key)
#-----2------
dict2={"a":1,"b":2,"c":3}
for value in dict2:
    print(value)
#loop enumerate
#-----1-----
list3=["a","b","c","d","e"]
for yi, value in enumerate(list3):
    print(yi,value)
#-----2-----
dict3={"name":"hamna","age":18,"city":"grw"}
for li, mi in enumerate(dict3):
    print(li,mi)
#-----3------
tuple3=("a","b","c","d","e")
for xi,ji in enumerate(tuple3):
    print(xi,ji)
#items()
#-----1-----
dict4={"name":"hamna","age":18,"city":"grw"}
for wi, fi in dict4.items():
    print(wi,fi)
#-----2-----
list4=["1","2","3","4","5"]
for aa,dd in enumerate(list4):
    print(aa,dd)
#nested for loop
#-----1-----
for z in range(1,4):
    for r in range(1,4):
        print(z)
#-----2-----
for h in range(1,9):
    for us in range( 9):
        print(h,us )
#-----3------
for w in range(2,20):
    for a in range(2,4):
        print(w)
#-----4------
for qw in range(0,5):
    for we in range (3):
        for ty in range(3):
            print(qw,we,ty)