from player import Player
import random

def Start():
    print("Welcome to TextVentures!")
    playerName: str = input("What is your name? ")
    
    player = Player(playerName)
    
    print("\nHello " + str(player.get_name()) + " Let's begin your adventure.")

    print("\nYou can move north, south, east, or west.")
    print("\nType 'inventory' to check your items.")
    print("\nType 'exit' to quit the game.")

    while True:
        command = input(f"\n{str(player.get_name())}, what would you like to do? ").strip().lower()
        
        if command in ["north", "south", "east", "west"]:
            player.move(command)
            print(f"\nYou are now at the {str(player.get_location())}.")

            event = random.choice(["nothing", "monster", "item"])

            if event == "item":
                item = random.choice(["sword", "shield", "potion"])
                player.pick_item(item)
            elif event == "monster":
                print("\nA wild monster appears!")
                action = input("Do you want to (fight) or (flee)? ").strip().lower()
                if action == "fight":
                    if random.randint(1, player.get_strength()) > random.randint(1, 20):
                        print("\nYou defeated the monster!")
                        player.gain_experience(20)
                    else:
                        print("\nYou lost the fight!")
                        player.lose_life()
                        potion_action = input("\nWould you like to use a potion to restore a life? (yes/no)")
                        if potion_action.lower() == "yes":
                            player.use_potion()
                        else:
                            print("\nYou chose not to use a potion.")
                elif action == "flee":
                    if random.randint(1, player.get_strength()) > random.randint(1, 20):
                        print("\nYou fled safely.")
                    else:
                        print("\nYou couldn't escape!")
                        player.lose_life()
                        potion_action = input("\nWould you like to use a potion to restore a life? (yes/no)")
                        if potion_action.lower() == "yes":
                            player.use_potion()
                        else:
                            print("\nYou chose not to use a potion.")
                else:
                    print("\nInvalid action.")
            else:
                print("\nYou found nothing of interest here.")
        elif command == "inventory":
            print(str(player.show_inventory()))
        elif command == "strength":
            print(f"\nYour current strength is {player.get_strength()}.")
        elif command == "lives":
            print(f"\nYou have {player.get_lives()} lives remaining.")
        elif command == "experience":
            print(f"You need {player.get_level_up_threshold() - player.get_experience()} experience points to level up.")
        elif command == "potion":
            player.use_potion()
        elif command == "shield":
            player.equip("shield")
        elif command == "exit":
            print("\nThanks for playing!")
            break
        else:
            print("\nInvalid command. Please try again.")

Start()