import random

print("ROBOT MISSILE\n")
print("TYPE THE CORRECT CODE")
print("LETTER (A-Z) TO DEFUSE THE MISSILE.")
print("YOU HAVE 4 CHANCES\n")

answer = chr(random.randint(1,26)+64)

success = False

for x in range(4):
    guess = input().upper()
    if guess == answer:
        success = True
        break
    
    if ord(guess) < ord(answer):
        print('LATER')
    else:
        print('EARLIER')

if success:
    print("TICK....FIZZZZ..CLICK....")
    print("YOU DID IT")
else:
    print("BOOOOOOOOM...")
    print("YOU BLEW IT")
    print("THE CORRECT CODE WAS " + answer)

