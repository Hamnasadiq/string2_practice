#index()

#-----1-----
line_1= "python programming"
position_1=line_1.index("pro")
print(position_1)
#-----2-----
line_2="I like programming"
position_2=line_2.index("like", 1 ,7)
print(position_2)
#-----3-----
line_3="hello programming world"
position_3=line_3.index("l", 0, 6)
print(position_3)
#-----4-----
line_4="hello python programming"
position_4=line_4.index("p")
print(position_4)
#-----5-----
line_5="web development"
position_5=line_5.index("web")
print(position_5)

#isalnum

#-----1-----
line_6="python123"
print(line_6.isalnum())
#-----2-----
line_7="hello,world"
print(line_7.isalnum())
#-----3-----
line_8="78 development"
print(line_8.isalnum())
#-----4-----
line_9="111111"
print(line_9.isalnum())
#-----5-----
line_10="---123@"
print(line_10.isalnum())


#isalpha
#-----1-----
line_11="hamna"
print(line_11.isalpha())
#-----2-----
line_12="12345"
print(line_12.isalpha())
#-----3-----
line_13="hamna123"
print(line_13.isalpha())
#-----4-----
line_14="student"
print(line_14.isalpha())
#-----5-----
line_15="9876"
print(line_15.isalpha())
#isdecimal
#-----1-----
line_16="\u0030"
print(line_16.isdecimal())
#-----2-----
line_17="123a"
print(line_17.isdecimal())
#-----3-----
line_18="909090"
print(line_18.isdecimal())
#-----4-----
line_19="abcd"
print(line_19.isdecimal())
#-----5-----
line_20="4.4.4.4"
print(line_20.isdecimal())

#isdigit
#-----1-----
line_21="!234"
print(line_21.isdigit())
#-----2-----
line_22="909^0"
print(line_22.isdigit())
#-----3-----
line_23="123"
print(line_23.isdigit())
#-----4-----
line_24="abcd"
print(line_24.isdigit())
#-----5-----
line_25="123.34"
print(line_25.isdigit())

#identifier
#-----1-----
line_26="4abc"
print(line_26.isidentifier())
#-----2-----
line_27="abc_"
print(line_27.isidentifier())
#-----3-----
line_28="developing"
print(line_28.isidentifier())
#-----4-----
line_29="hamna  sadiq"
print(line_29.isidentifier())
#-----5-----
line_30="6sdfhsdfh_"
print(line_30.isidentifier())

#islower()
#-----1-----
line_31="HAmna"
print(line_31.islower())
#-----2-----
line_32="HamNA SadIQ"
print(line_32.islower())
#-----3-----
line_33="string2"
print(line_33.islower())
#-----4-----
line_34="coMPuter SCIENce"
print(line_34.islower())
#-----5-----
line_35="psychology"
print(line_35.islower())

#isnumeric
#-----1-----
line_36="12345"
print(line_36.isnumeric())
#-----2-----
line_37="¾"
print(line_37.isnumeric())
#-----3-----
line_38="123.45"
print(line_38.isnumeric())
#-----4-----
line_39="²"
print(line_39.isnumeric())
#-----5-----
line_40="abcdefg"
print(line_40.isnumeric())