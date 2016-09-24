#prints numbers 1-10
for number in range(1, 11):
    print number

print "\n"
#asks user for a range of numbers to prints such as 2-8 and prints them
start = int(raw_input("Start from: "))
end = int(raw_input("End on: "))

for number in range(start, (end + 1)):
    print number

print "\n"
#prints odd number 1-9
for number in range(1, 11):

    if number % 2 == 1:
        print number

print "\n"
#prints a 5x5 board of *
for i in range(0, 5):
    print "*" * 5

print "\n"
#prints a board of * based on the users requested size
N = int(raw_input("How big is the square? "))

for i in range(0, N):
    print "*" * N

print "\n"
#prints a board of * thats empty based on users height and width
width = int(raw_input("Width? "))
height = int(raw_input("Height? "))

for i in range(0, height):
    if i == 0 or i == height - 1:
        print "*" * width
    else:
        print "*" + (" " * (width - 2)) + "*"

print "\n"
# makes a triangle of *'s'
spaces = 3
stars = 1

for i in range(0, 4):
    print (" " * spaces) + ("*" * stars) + (" " * spaces)
    stars += 2
    spaces -= 1

print "\n"
# makes a triangle based on user's height input
howHigh = int(raw_input("Height? "))

spaces = howHigh
stars = 1

for i in range(0, howHigh):
    print (" " * spaces) + ("*" * stars) + (" " * spaces)
    stars += 2
    spaces -= 1

print "\n"
#prints the multiplication table from 1 to 10
for i in range(1, 11):
    for k in range(1, 11):
        print "%d * %d = " % (i, k),
        print i * k

print "\n"
#bonus: puts a box around your sentence
sentence = raw_input("Please enter a sentence. ")

charCount = len(sentence)

for i in range(0, 3):
    if i == 0 or i == 2:
        print (charCount + 4) * "*"
    else:
        print "* %s *" % sentence

print "\n"
#bonus prints the first 100 triangle numbers
for i in range(1, 101):
    print i*(i + 1)/2

print "\n"
#bonus prints its factors given a number
num = int(raw_input("Choose a number." ))


for i in range(1, num + 1):

    if num % i == 0:
        print "factor: %d " % i

print "That's all. END"
