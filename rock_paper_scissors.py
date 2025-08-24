import random #Initializing module

#ASCII art
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
Scissors='''
( _\    /_ )
 \ _\  /_ / 
  \ _\/_ /_ _
  |_____/_/ /|
  (  (_)__)J-)
  (  /`.,   /
   \/  ;   /
    | === |
'''

paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
opt=['rock','paper','scissors']

#choices
computer= random.choice(opt)  #computer random choice
user=input('Rock , paper, scissors shoot \n type which you want: ') #user selection
if computer==user.lower():
    print("Its a tie")
elif user.lower()  not in opt:
    print('invalid input \n try again')
elif computer=="rock":
    if user.lower()=='paper':
        print(f'computer:{rock}, you:{paper} \n You win')
    else:
        print(f'computer:{rock}, you:{Scissors} \n You loose')
elif computer=="paper":
    if user.lower()=='rock':
        print(f'computer:{paper}, you:{rock} \n You loose')
    else:
        print(f'computer:{paper}, you:{Scissors} \n You win')
elif computer=="scissors":
    if user.lower()=='paper':
        print(f'computer:{Scissors}, you:{paper} \n You loose')
    else:
        print(f'computer:{Scissors}, you:{rock} \n You win')
else:
    print('invalid input')