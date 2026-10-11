import random

def play_game():
    lucky_num = random.randint(1,50)

    while True:
        user_num = int(input("Enter Your Lacku Number Between 1 to 50 -->"))

        if user_num == lucky_num:
            print("Yor won. Game Is Close !!")
            break
        elif user_num < lucky_num:
            print("Number Is smole")
        else:
            print("Number Is Big")
    print("Game Is Over !!")
   

play_game() 