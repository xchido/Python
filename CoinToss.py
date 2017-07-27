#Listing 10-3: Coin toss program
import random
headcount = 0
tailcount = 0
userinput = ''
print ("Now tossing a coin...");
while userinput.lower() != "x":
    flip = random.choice(['heads', 'tails'])
    if flip == 'heads':
        headcount += 1
        print ("heads! the number of heads is now %d" % headcount)
    else:
        tailcount += 1
        print ("tails! the number of tails is now %d" % tailcount)
    print ("Press 'x' to quit"),
    userinput = input("or another key to toss again:")
print ("the total number of heads:", headcount)
print ("the total number of tails:", tailcount)
