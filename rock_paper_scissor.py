#!/usr/bin/env python3

import random

try:
    a = 0
    while a == 0:

        print(
            "\n\n*****ROCK-PAPER-SCISSORS*****\n\n There will be five matches. Out of which the player who wins more "
            "number of times,will "
            "\n\t WIN THE SERIES.\n")

        n = 5
        player_points = 0
        computer_points = 0
        Draw = 0
        while n > 0:
            lst = ["rock", "paper", "scissors"]
            comp = random.choice(lst)
            player = input(f"Enter {lst[0]}, {lst[1]} or {lst[2]}: ")
            player_refined = player.lower()
            if player_refined == lst[0]:
                if comp == lst[2]:
                    player_points = player_points + 1
                    print("winner: you")
                elif comp == lst[1]:
                    computer_points = computer_points + 1
                    print("winner: computer")
                else:
                    Draw = Draw + 1
                    print("draw")

            elif player_refined == lst[1]:
                if comp == lst[0]:
                    player_points = player_points + 1
                    print("winner: you")
                elif comp == lst[2]:
                    computer_points = computer_points + 1
                    print("winner: computer")
                else:
                    Draw = Draw + 1
                    print("draw")

            elif player == lst[2]:
                if comp == lst[1]:
                    player_points = player_points + 1
                    print("winner: you")
                elif comp == lst[0]:
                    computer_points = computer_points + 1
                    print("winner: computer")
                else:
                    Draw = Draw + 1
                    print("draw")

            n = n - 1
            print(f"{n} matches left\n")

        if player_points > computer_points:
            print("\n\tYOU WON\n")
        elif computer_points > player_points:
            print("\n\tYOU LOSE\n")
        else:
            print("\n\tDRAW\n")

        print(f"You won {player_points} times \nComputer won {computer_points} times \nDraw matches are {Draw}")

        ag = input("\nYou wanna play again?(y for yes,n for no): ")
        if ag == 'n':
            break
        print()
except Exception as e:
    print(e)

