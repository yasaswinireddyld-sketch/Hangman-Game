import random
categories={
    "flowers":['sunflower','rose','jasmine','lotus'],
    "animals":['lion','tiger','elephant','rabbit'],
    "tifins":['dosa','idly','wada','puri','bonda'],
    "country":['india','spain','america','italy','russia'],
    "places":['hyderabad','chennai','mumbai','kerala','goa'],
    "sports":['kabaddi','volleyball','handball','cricket','tennis'],
    "movies":['rebel','yogi','varsham','salar','kalki','chatrapati']
}
print("* * * * * - - - WELCOME TO HANGMAN GAME! - - - * * * * *")
attempts=6
print("Choose a Category")
for category in categories:
    print(category)
choice=input("Enter Your Category:").lower()
if choice in categories:
    word=random.choice(categories[choice])
    print('category:',choice)
    print("----Word Selected----")
    display=['_']*len(word)
    print("guess the Word")
    print()
    print(" ".join(display))
    while attempts>0 and '_' in display:
     print()
     letter=input("enter the letter:")
     for j in range(len(word)):
        if(word[j]==letter):
         display[j]=letter
     print(" ".join(display))
     if letter in word:
      print()
      print("Correct Guess")
     else:
      attempts-=1
      print()
      print("Wrong guess")
      print()
      print("Remaining attempts:",attempts)
    if '_' not in display:
      print()
      print("Congratulations You Won")
    else:
      print("game over")
      print("the Word is",word)
else:
  print("Invalid Category")









