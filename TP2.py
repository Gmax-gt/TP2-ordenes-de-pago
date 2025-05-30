m=open("ordenes25.txt")
m.readline()
for linea in m:
    if linea[-1] == "\n" :
        linea =linea [0:54]
        print (linea)
