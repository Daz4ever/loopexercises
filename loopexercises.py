#prints numbers 1-10
for number in range(1, 11):
    print number

#asks user for a range of numbers to prints such as 2-8 and prints them
start = int(raw_input("Start from: "))
end = int(raw_input("End on: "))

for number in range(start, (end + 1)):
    print number

#prints odd number 1-9
for number in range(1, 11, 2)
    print number

#prints a 5x5 board of *
for i in range(0, 5):
    print "*" * 5

#prints a board of * based on the users requested size
N = int(raw_input("How big is the square? "))

for i in range(0, N):
    print "*" * N

#prints a board of * thats empty based on users height and width
width = int(raw_input("Width? "))
height = int(raw_input("Height? "))

for i in range(0, height):
    if i == 0 or i == height - 1:
        print "*" * width
    else:
        print "*" + (" " * (width - 2)) + "*"

# makes a triangle of *'s'
spaces = 3
stars = 1

for i in range(0, howHigh):
    print (" " * spaces) + ("*" * stars) + (" " * spaces)
    stars += 2
    spaces -= 1

# makes a triangle based on user's height input
howHigh = int(raw_input("Height? "))

spaces = howHigh + 1
stars = 1

for i in range(0, howHigh):
    print (" " * spaces) + ("*" * stars) + (" " * spaces)
    stars += 2
    spaces -= 1

#prints the multiplication table from 1 to 10
for i in range(1, 11):
    for k in range(1, 11):
        print "%d * %d = " % (i, k),
        print i * k
