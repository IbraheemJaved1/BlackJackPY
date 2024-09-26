

import random
import csv


print("Welcome To Blackjack" "\n")
option = input("To look at the rules & then play TYPE 1 If you want to play TYPE 2:")

if option == "1":
    print("The rules are simple. Given your hand, try to get an collective number closest to 21. Note: If your hand goes over 21, you bust!")
    print('\n')

is_multiplayer = input("If you are playing by yourself TYPE 1 otherwise TYPE 2:")

if is_multiplayer == "1":
    #Create a Dealer
    ai = random.choice(["Bob", "Barry", "Alan", "Jake"])
    print("\n")
    print("Your opponent today is " + ai)
    ai_hitStand = 0

    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    random_num = random.choice(deck)
    random_num2 = random.choice(deck)
    random_num3 = random.choice(deck)

    print("Your first card is : " + str(random_num))
    print("Your second card is : " + str(random_num2))
    finalHand_player_1_first_set = random_num + random_num2
    player_1_hitStand = (input("Player 1 - hit or stand: "))
    finalHand_player_1_last_card = random_num + random_num2 + random_num3

    random_num_ai = random.choice(deck)
    random_num2_ai = random.choice(deck)
    random_num3_ai = random.choice(deck)

    print(ai + "'s first card is : " + str(random_num_ai))
    print(ai + "'s second card is : " + str(random_num2_ai))
    finalHand_ai_first_set = random_num_ai + random_num2_ai
    print(ai + " - hit or stand?")
    if (random_num_ai + random_num2_ai >= 14):
        ai_hitStand = 1
        print(ai + " chose to stand")
    else:
        ai_hitStand = 2
        print(ai + " chose to hit")


    finalHand_ai_last_card = random_num_ai + random_num2_ai + random_num3_ai

    if player_1_hitStand == "hit":
        print("Third card is : " + str(random_num3))
        print("Player 1 - Your hand is:", finalHand_player_1_last_card)
        player_1_final_number = finalHand_player_1_last_card
    elif player_1_hitStand =='stand':
        print('Player 1 - Your hand is:',finalHand_player_1_first_set)
        player_1_final_number = finalHand_player_1_first_set

    if ai_hitStand == 2:
        print("Third card is : " + str(random_num3))
        print(ai + " - Your hand is:", finalHand_ai_last_card)
        player_2_final_number = finalHand_ai_last_card
    elif ai_hitStand == 1:
        print(ai + ' - Your hand is:',finalHand_ai_first_set)
        player_2_final_number = finalHand_ai_first_set


else:
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    random_num = random.choice(deck)
    random_num2 = random.choice(deck)
    random_num3 = random.choice(deck)

    print("Player 1, your first card is : " + str(random_num))
    print("Player 1, your second card is : " + str(random_num2))
    finalHand_player_1_first_set = random_num + random_num2
    player_1_hitStand = (input("Player 1 - hit or stand: "))
    finalHand_player_1_last_card = random_num + random_num2 + random_num3

    random_num_2 = random.choice(deck)
    random_num2_2 = random.choice(deck)
    random_num3_2 = random.choice(deck)

    print("Player 2, your first card is : " + str(random_num_2))
    print("Player 2, your second card is : " + str(random_num2_2))
    finalHand_player_2_first_set = random_num_2 + random_num2_2
    player_2_hitStand = (input("Player 2 - hit or stand: "))
    finalHand_player_2_last_card = random_num_2 + random_num2_2 + random_num3_2

    if player_1_hitStand == "hit":
        print("Third card is : " + str(random_num3))
        print("Player 1 - Your hand is:", finalHand_player_1_last_card)
        player_1_final_number = finalHand_player_1_last_card
    elif player_1_hitStand =='stand':
        print('Player 1 - Your hand is:',finalHand_player_1_first_set)
        player_1_final_number = finalHand_player_1_first_set

    if player_2_hitStand == "hit":
        print("Third card is : " + str(random_num3_2))
        print("Player 2 - Your hand is:", finalHand_player_2_last_card)
        player_2_final_number = finalHand_player_2_last_card
    elif player_2_hitStand =='stand':
        print('Player 2 - Your hand is:',finalHand_player_2_first_set)
        player_2_final_number = finalHand_player_2_first_set


#Check for winner
max_number = 21
P1fail = False
P2fail = False
if is_multiplayer != 0:
    ai = "Player 2"

#Check for bust
if player_1_final_number > max_number:
    print("Player 1 Bust")
    P1fail = True

if player_2_final_number > max_number:
    print(ai + " Bust")
    P2fail = True

if P1fail and P2fail == True:
    print("Nobody wins")
    exit()
elif P1fail == False and P2fail == True:
    print("Player wins")
    exit()
elif P1fail == True and P2fail == False:
    print(ai + " wins")
    exit()
elif P1fail == False and P2fail == False:
    #Calculate who the winner is
    if player_1_final_number > player_2_final_number:
        print("Player 1 wins")
        
    elif player_1_final_number < player_2_final_number:
        print(ai + " wins")
    else:
        print("It's a tie!")




