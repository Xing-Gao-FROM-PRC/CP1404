import numbers


name = str(input("Please enter your name:"))
f = open("name.txt","w")
f.write(name)
f.close()

w = open("name.txt","r")
print("Your name is " + w.read())
f.close()

q = open("numbers.txt","r")
A = int(q.readline())
B = int(q.readline())
C = A + B
print(C)

count=len(open("num +bers.txt",'r').readlines())
print(count)
