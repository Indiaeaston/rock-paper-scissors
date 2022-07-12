#Rock Paper Scissors
import random
print("Welcome to the Rock, Paper, Scissors simulator!")
print("You will be playing against the computer")
print("Best out of three wins!")
def rock_paper_scissors():

  round = 0 
  user_wins = 0
  cpu_wins = 0
  
  while round < 3:
    user = input("\nWhat is your pick: ")
    user = user.title()
    shoot = ["Scissors", "Rock", "Paper"]
  
    cpu = random.choice(shoot)
    print("The CPU chose {}".format(cpu))
  
    if cpu == user:
      print("Tie!")
    if cpu == "Scissors" and user == "Rock":
      user_wins += 1
      print("You win!")
    if cpu == "Rock"  and user == "Scissors":
      cpu_wins += 1
      print("CPU wins")
    if cpu == "Paper" and user == "Rock":
       cpu_wins += 1
       print("CPU wins!")
    if cpu == "Rock" and user == "Paper":
       user_wins += 1
       print("You win!")
    if cpu == "Scissors" and user == "Paper":
       cpu_wins += 1
       print("CPU wins!")
    if cpu == "Paper" and user == "Scissors":
      user_wins += 1
      print("You Win!")
      
    round = round + 1

  if cpu_wins > user_wins:
    print("\nCPU wins! you lost by {} points".format(cpu_wins - user_wins))

  if user_wins > cpu_wins:
      print("\nYou win! You won by {} points".format(user_wins - cpu_wins))

  if user_wins == cpu_wins:
    print("It was a tie! neither on you won")


  
  
rock_paper_scissors()


      
      
      
      
      
    

