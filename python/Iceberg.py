import random

def sign(x):
    return x and (-1,1)[x<0]

print("ICEBERG\n")

oceanSize = 8

ocean = [[ '_' for _ in range(oceanSize) ] for _ in range(oceanSize) ]

icebergs = random.randint(4,11)
for i in range(icebergs):
    x=random.randint(0,oceanSize-1)
    y=random.randint(0,oceanSize-1)
    
    ocean[x][y]='*'

while True:
    enemyX = random.randint(0,oceanSize-1)
    enemyY = random.randint(0,oceanSize-1)
    if ocean[enemyX][enemyY] == '_':
        ocean[enemyX][enemyY] = 'Z'
        break

while True:
    shipX = random.randint(0,oceanSize-1)
    shipY = random.randint(0,oceanSize-1)
    if ocean[shipX][shipY] == '_':
        ocean[shipX][shipY] = 'U'
        break


while True:
    print()
    for r in ocean:
        print(f"\t{' '.join(r)}")

    dir = input("\nDirection N,S,E,W? ").upper()
    ocean[shipX][shipY] = '_'
    
    match dir:
        case 'N':           
            shipX = shipX - 1 if shipX>0 else 0
        case 'S':
            shipX = shipX + 1 if shipX<oceanSize-1 else 0
        case 'E':
            shipY = shipY - 1 if shipY>0 else 0
        case 'W':
            shipY = shipY + 1 if shipY<oceanSize-1 else 0
        case _:
            pass

    
    if ocean[shipX][shipY] == '*':
        print("You've hit an iceberg and sunk.")
        break
    elif ocean[shipX][shipY] == 'Z':
        print("You've been caught")
        break
    else:
        ocean[shipX][shipY] = 'U'
    
    ocean[enemyX][enemyY] = '_'
    enemyX += sign(enemyX - shipX)
    enemyY += sign(enemyY - shipY)

    if ocean[enemyX][enemyY] == '*':
        print("They've hit an iceberg and sunk. You're safe.")
        break
    elif ocean[enemyX][enemyY] == 'U':
        print("You've been caught")
        break
    else:
        ocean[enemyX][enemyY] = 'Z'



