# ______________--Hang man--__________
import random
from Hang_man_art import logo,stages
from Hang_man_words import word_list

print(logo)
lives=6
choosen_word=random.choice(word_list)

display=[]
for _ in range(len(choosen_word)):
    display+="_"
print(display)
end_of_game=False

while not end_of_game:
 guess=input("Guess a letter :").lower()
 if guess in display:
    print(f"you already entered this")

 for position in range(len(choosen_word)):
    letter=choosen_word[position]
    if letter==guess:
        display[position]=letter
 print(display)

 
 if guess not in choosen_word:
     print("Its not in the letter,You lose a life")
     lives-=1
     if lives==0:
           end_of_game=True
           print("You lose")
           print(f"Your word is {choosen_word}")

 if "_" not in display:
   end_of_game=True
   
   print("You win")
 
 print(stages[lives])

