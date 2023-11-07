print(r"""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \\'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
""")

print("Welcome to Treasure Island")
print("You must find the treasure.")

choice1 = input("You're at a crossraod, where do you want to go (\"right\" or \"left\")").lower()

if choice1 == "right":
    choice2 = input("You've arrived at a lake. There is an island in the middle. \"Wait\" for a boat or \"swim\" across?").lower()
    if choice2 == "wait":
         choice3 = input("You've arrived on the island. There is a hosue with 3 doors. One red, one yellow and one blue. What door will you open?").lower()
         if choice3 == "red":
             print("The room is on fire. Game over!")
         elif choice3 == "yellow":
             print("You've found the treasure!")
         elif choice3 == "blue":
             print("You're ina  room full of beasts. Game over!")
    else:
        print("You've been attacked by an angry trout. Game over.")
else:
    print("You fell in a hole, Game Over!")
