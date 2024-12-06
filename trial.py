# Rock, Paper, Scissors
player1 = input("Player 1, enter your choice (rock, paper, or scissors): ").lower()
player2 = input("Player 2, enter your choice (rock, paper, or scissors): ").lower()

if player1 == player2:
    print("It's a tie!")
elif (player1 == "rock" and player2 == "scissors") or \
     (player1 == "scissors" and player2 == "paper") or \
     (player1 == "paper" and player2 == "rock"):
    print(f"Player 1 wins! {player1.capitalize()} beats {player2}.")
elif (player2 == "rock" and player1 == "scissors") or \
     (player2 == "scissors" and player1 == "paper") or \
     (player2 == "paper" and player1 == "rock"):
    print(f"Player 2 wins! {player2.capitalize()} beats {player1}.")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")
