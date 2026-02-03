import random
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.money = 50
        self.round_status = 0 # 0 for betting, 1-3 for active rounds
        self.rounds_won = 0

player = Player("Jim")

def prompt_continue():
    input("Press enter to continue")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== [ROCK PAPER SCISSORS] ===")

def get_player_bet():
    while True:
        print(f"Current Money: ${player.money}")
        try:
            bet = int(input("How much would you like to bet? "))
            if 0 < bet <= player.money:
                return bet
            print("Invalid amount!")
        except ValueError:
            print("Please enter a number.")

def get_player_move():
    move = 0
    while move == 0:
        print("\n[1] Rock, [2] Paper, [3] Scissors")
        try:
            move = int(input("Select your move: "))
            if move not in [1, 2, 3]:
                move = 0
                print("Invalid choice!")
        except ValueError:
            print("Invalid choice!")
    return move

def determine_round(player_move, ai_move):
    # Your logic: returns True if player wins
    p_adjusted = 3 if player_move - 1 == 0 else player_move - 1
    return p_adjusted == ai_move

def run_game():
    while player.money > 0:
        clear_screen()
        # Step 1: Betting Phase
        current_bet = get_player_bet()
        player.rounds_won = 0
        round = 1
        
        # Step 2: Best of 3 Phase
        while round < 4:
            clear_screen()
            print(f"\n--- Round {round} ---")
            print(f"\n--- Player {player.rounds_won} | Ai {(round-1) - player.rounds_won} ---")
            p_move = get_player_move()
            ai_move = random.randint(1, 3)
            
            print(f"You chose {p_move}, AI chose {ai_move}")
            
            if p_move == ai_move:
                print("Draw! (No one wins this round)")
            elif determine_round(p_move, ai_move):
                print("You win this round!")
                player.rounds_won += 1
                round += 1
            else:
                print("AI wins this round.")
                round += 1
            prompt_continue()
        clear_screen()
        print(f"\n--- Player {player.rounds_won} | Ai {(round-1) - player.rounds_won} ---")
        # Step 3: Match Resolution
        if player.rounds_won >= 2:
            player.money += current_bet
            print(f"\nMATCH OVER: You won the bet! New Balance: ${player.money}")
        else:
            player.money -= current_bet
            print(f"\nMATCH OVER: You lost the bet. New Balance: ${player.money}")
            
        if player.money <= 0:
            print("Game Over! You're broke.")
            break
            
        cont = input("\nPlay another match? (y/n): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    run_game()