import random
import time

print("VITAL MESSAGE\n")
print("HOW DIFFICULT? (4-10)")

difficulty = int(input())
while difficulty<4 or difficulty>10:
    difficulty = int(input())

message = ''
for i in range(difficulty):
    message += chr(random.randint(1,26)+64)

print("Rember this message before the countdown starts\n\t")
print(message)

time.sleep(difficulty)
for i in range(50,0,-1):
    print(i)
    time.sleep(0.1)

print("\n\nEnter it NOW!")

answer = input().upper()
if answer == message:
    print("MESSAGE CORRECT")
else:
    print("YOU GOT IT WRONG")
    print("IT SHOULD HAVE BEEN "+message)

