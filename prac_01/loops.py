for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a. count in 10s from 0 to 100
for i in range(0,101,10):
    print(i,end=' ' )
print()

#b. count down from 20 to 1
for i in range(20,0,-1):
    print(i, end=' ')
print()

#c. print n stars
star_num_in_c = int(input("Number of stars: "))
for i in range(star_num_in_c):
    print("*", end='')
print()

#d. print n lines of increasing stars
star_num_in_d = int(input("Number of stars: "))
for i in range(0,star_num_in_d):
    for j in range(0,i+1):
        print("*", end='')
    print()
