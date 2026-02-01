import random
class Actor:
    name = ""
    maxHp = 1
    currentHp = 1
    attack = 1
    enemies_slain = 0
    def __init__(self, name, startingHp, startingAttack):
        self.name = name
        self.maxHp = startingHp
        self.currentHp = self.maxHp
        self.attack = startingAttack

    def printStatus(self):
        print(f"[{self.name}]")
        for i in range(self.maxHp):
            if i < self.currentHp:
                print("|",end='')
            else: print("-",end='')
        print("\n")

    def resolve_combat(target,attacker):
        target.currentHp -= attacker.attack
        if(target.currentHp < 0):
            target.currentHp = 0

def promptContinue():
    input("Press enter to continue")

def promptPlayer(player: Actor, enemy: Actor) -> bool:
    validMove = False
    while(validMove is False):
        print("[1] Attack")
        inputValue = input("Choose your next action!")
        try:
            action = int(inputValue)
            if(action == 1):
                validMove = True
                Actor.resolve_combat(enemy,player)
            # Add elifs for more actions eventually...
            else:
                print("Unknown action...")
            break
        except ValueError:
            print("Unknown action...")
    return validMove

def startCombat(player: Actor):
    enemy = Actor("Goblin",5,2)
    activeTurn = player
    while(player.currentHp > 0):
        player.printStatus()
        enemy.printStatus()
        while(activeTurn is player):
            #Player is selecting action
            if promptPlayer(player,enemy) is True:
                activeTurn = enemy
        if(enemy.currentHp <= 0):
            player.enemies_slain += 1
            print(f"Player wins! Monsters slain {player.enemies_slain}")
            promptContinue()
            break
        Actor.resolve_combat(player,enemy)
        activeTurn = player
        if(player.currentHp <= 0):
            print("Enemy wins...")
            promptContinue()
        


player = Actor("Player",20,4)
while(player.currentHp > 0):
    startCombat(player)

print("Your adventure ends here!")
print(f"Total monsters slain: {player.enemies_slain}")