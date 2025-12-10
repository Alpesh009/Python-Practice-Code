import random

def game():
    print("You are playing a game")
    score = random.randint(1,62)

    # Fetch high score
    with open("hiscore.txt") as f:
        highscore = f.read()
        if(highscore!=""):
            highscore = int(highscore)
        else:
            highscore = 0
    
    print(f"You score is: {score}")
    if(score>highscore):
        #write the highscore into file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()



