import xml.etree.ElementTree as Et
import namedentities
from namedentities import *
e=input("xmlpath")
with open(e,"r",encoding='UTF-8') as file:
     data=file.read()
     # print(data)

# print("named:___  ",(named_entities(data)))
# print("numeric:___",(numeric_entities(data)))
# print("hex:___"   ,(hex_entities(data)))
# print("unicode:__",(unicode_entities(data)))

d=input("keyword")

# a=input(data)
# p=numeric_entities(data)
# print("__",p)
# with open("Final1.xml", "w",encoding='UTF-8') as myfile:
#      myfile.write(p)
#      myfile.close()
if d=="hexa":
     d=hex_entities(data)
     print("__", d)
elif d=="numeric":
     d=numeric_entities(data)
     print("!!!!!!!!",d)
elif d=="named":
     d=named_entities(data)
     print("***",d)
elif d=="unicode":
     d=unicode_entities(data)
     print("$$$$$$$$$$$$$",d)

else:
     print("no found")

with open("output.xml", "w", encoding='UTF-8') as myfile:
     myfile.write(d)
     myfile.close()
