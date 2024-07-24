import random

userHealth = 3
dealerHealth = 3
emptyCase = 0
fullCase = 1
roulette = [emptyCase, emptyCase, emptyCase, emptyCase, fullCase, fullCase, fullCase, fullCase]

# Listeyi karıştırma
random.shuffle(roulette)

dealerChoices = [1, 0]

def dealersTurn():
    global dealerHealth
    global userHealth
    bullet = random.sample(roulette, 1)[0]
    dealerChoice = random.sample(dealerChoices, 1)[0]  # Dealer seçimi her seferinde rastgele yapılmalı
    
    if dealerChoice == 1:
        print("Dealer chose Himself!")
        if bullet == fullCase:
            print("Bullet is full!")
            dealerHealth -= 1
        else:
            print("Bullet is empty!")
    else:
        print("Dealer chose you!")
        if bullet == fullCase:
            print("Bullet is full!")
            userHealth -= 1
        else:
            print("Bullet is empty!")
    
    print("Dealer Health: ", dealerHealth)
    print("Your Health: ", userHealth)
    roulette.remove(bullet)  # Kullanılan bullet'i array'dan kaldırma

def userTurn():
    global dealerHealth
    global userHealth

    bullet = random.sample(roulette, 1)[0]
    userChoice = input("Enter your choice: Enemy(1) or You(0): ")

    if userChoice == "1":
        print("You selected Enemy!")
        if bullet == fullCase:
            print("Bullet is Full!")
            dealerHealth -= 1
        else:
            print("Bullet is Empty!")
    else:
        print("You selected Yourself!")
        if bullet == fullCase:
            print("Bullet is Full!")
            userHealth -= 1
        else:
            print("Bullet is Empty!")

    print(f"Dealer Health: {dealerHealth}")
    print(f"User Health: {userHealth}")
    roulette.remove(bullet)  # Kullanılan bullet'i array'dan kaldırma

while True:
    if userHealth <= 0:
        print("User lost!")
        break
    elif dealerHealth <= 0:
        print("Dealer lost!")
        break

    userTurn()
    if userHealth <= 0 or dealerHealth <= 0:  # Sağlık kontrolünü kullanıcı turundan sonra yap
        break
    print("Dealer's Turn!")
    dealersTurn()
    if userHealth <= 0 or dealerHealth <= 0:  # Sağlık kontrolünü dealer turundan sonra yap
        break
    print("User's Turn!")
