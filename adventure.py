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
        command = input(f"\n{str(player.get_name())}, where would you like to go? ").strip().lower()
        
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
                    if random.choice([True, False]):
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
                    if random.choice([True, True, False]):
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
            player.show_inventory()
        elif command == "exit":
            print("\nThanks for playing!")
            break
        else:
            print("\nInvalid command. Please try again.")

Start()