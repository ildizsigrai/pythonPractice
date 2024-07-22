print("Welcome to the computer quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    print("The game stops. :(")
    quit()
print("Okay! Lets play! :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect, try again!")
    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect, try again!")
    answer = input("What does GPU stand for? ")
    if answer.lower() == "graphics processing unit":
        print("Correct!")
        score += 1

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect, try again!")
    answer = input("What does RAM stand for? ")
    if answer.lower() == "random access memory":
        print("Correct!")
        score += 1

print("You got " + str(score) + " questions correct")