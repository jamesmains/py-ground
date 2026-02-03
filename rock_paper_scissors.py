import random
import os
money = 50
goal = 200
done_playing = False
matches_won = 0
round = 1
rounds_won = 0
def promptContinue():
    input("Press enter to continue")

def determine_round(playerMove, aiMove) -> bool:
    p = playerMove - 1
    if p == 0:
        p = 3
    if p == aiMove:
        return True # winner found
    else:
        return False



while(money > 50 or done_playing == False):
    if round == 1:
        bet = 0
        while(bet == 0):
            print(f"Money: {money}")
            moneyBet = input("How much would you like to bet?\n")
            try:
                bet = int(moneyBet)
                if(bet < 0 or bet > money):
                    bet = 0
                    print("Invalid bet!")
            except ValueError:
                print("Invalid bet!")
    os.system('cls' if os.name == 'nt' else 'clear')
    move = 0
    while(move == 0):
        print("[1] Rock, [2] Paper, [3] Scissors")
        inputValue = input("Select your move!\n")
        try:
            move = int(inputValue)
            if(move != 1 and move != 2 and move != 3):
                move = 0
                print("Invalid move!")
        except ValueError:
            print("Invalid move!")
    print(move)
    aiMove = random.randint(1,3)
    print(f"Player: {move}, Ai: {aiMove}")
    if determine_round(move,aiMove):
        # Player wins
        print("Player wins round!")
        round += 1
        rounds_won += 1
    elif determine_round(aiMove,move):
        # Ai wins
        round += 1
        print("Ai wins round.")
    else:
        # Draw
        print("Draw!")
    
    promptContinue()
    if round >= 3:
        if rounds_won >= 2:
            round = 1
            money += bet
            print(f"Player wins the round winning ${bet}, total money ${money}")
        else:
            round = 1
            money -= bet
            print(f"Player lost! Losing ${bet} with an ending balance of ${money}")
            


