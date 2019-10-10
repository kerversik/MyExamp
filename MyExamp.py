t = open("/home/student/MyExamp/2.log","r")
k = open("/home/student/MyExamp/error.log","w")
for text in t:
    if(text.find("ERROR  ") != -1):
        k.write(text)
k.close
t.close
k = open("/home/student/MyExamp/error.log","r")
x = open("/home/student/MyExamp/SearchError.log","w")
g = str(input("Введите pool : "))
v = str(input("Введите thread :"))
for text in k:
    if(text.find("pool-"+ g +"-thread-"+ v) != -1):
        x.write(text)
k.close
x.close

