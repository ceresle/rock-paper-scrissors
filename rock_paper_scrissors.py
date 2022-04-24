import random

print(" ************* \n ************* \n **         ** \n ** Welcome ** \n **         ** \n ************* \n *************")
print(" ********************************************* \n *   This is a Rock, Paper, Scrissor Game!   * \n *        If you choose Rock, type R         * \n *        If you choose Paper, type P        * \n *        If you choose Scrissors, type S    * \n ********************************************* ")

while True:
  rps = ['Rock', 'Paper', 'Scrissors'] #rps stands for rock paper scrissor
  user_choice = input("Please choose your move: ")
  choice = random.choice(rps)
  if user_choice == 'S' and choice == 'Scrissors':
    print(" _    _ \n    (_)  / ) \n      | (_/  \n     _+/    //|\  \n   // | ) \n  (/  |/     It's Equal! The computer move was",choice)
    
  if user_choice == 'S' and choice == 'Rock':
    print("You lost! The computer move was",choice)

  if user_choice == 'S' and choice == 'Paper':
    print("You won! The computer move was",choice)
    
  elif user_choice == 'P' and choice == 'Paper':
    print("It's Equal! The computer move was",choice)

  if user_choice == 'P' and choice == 'Rock':
    print("You won! The computer move was",choice)

  if user_choice == 'P' and choice == 'Scrissors':
    print("You Lost! The computer move was",choice)

  elif user_choice == 'R' and choice == 'Rock':
    print("It's Equal! The computer move was",choice)

  if user_choice == 'R' and choice == 'Paper':
    print("You lost! The computer move was",choice)

  if user_choice == 'R' and choice == 'Scrissors':
    print("You won! The computer move was",choice)
