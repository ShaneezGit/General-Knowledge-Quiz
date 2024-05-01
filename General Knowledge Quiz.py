# Import the random module for shuffling questions and the time module for adding delays
import random
import time

# Define a list of questions and answers
questions = [
    {"question": "How many ghosts chase Pac-Man at the start of each game?", "answer": "4"},
    {"question": "What company was originally called 'Cadabra'?", "answer": "amazon"},
    {"question": "Queen guitarist Brian May is also an expert in what scientific field?", "answer": "astrophysics"},
    {"question": "Aureolin is a shade of what color?", "answer": "yellow"},
    {"question": "What country drinks the most coffee per capita?", "answer": "finland"},
    {"question": "Which planet has the most moons?", "answer": "saturn"},
    {"question": "In what country would you find Mount Kilimanjaro?", "answer": "tanzania"},
    {"question": "What is a group of pandas known as?", "answer": "an embarrassment"},
    {"question": "Which is the only body part that is fully grown from birth?", "answer": "eyes"},
    {"question": "Where is the strongest human muscle located?", "answer": "jaw"}
]

# Define a function to ask a question
    # Accept a question dictionary as input
    # Print the question
    # Prompt the user for an answer 
    # Return True if the answer is correct, False if not
def ask_question(question):
    print(question["question"])
    answer = input("Your answer: ").strip().lower()
    return answer == question["answer"]

# Define a function to play the game
    # Print a welcome message
    # Ask the player if they want to play
    # If the player declines, exit the game
    # Initialize the score to 0
    # Shuffle the questions randomly
    # Print a message to start the game
    # Wait for 1 second

def play_game():
    print("Welcome to the General Knowledge 101 Quiz!")
    playing = input("Do you want to play? (yes/no): ").strip().lower()
    if playing != "yes":
        quit()

    score = 0
    random.shuffle(questions)

    print("Okay! Lets play :)")
    time.sleep(1)

    # Loop through each question:
        # Print a separator
        # Ask the question and check the answer
        # If the answer is correct, increment the score
        # wait fot one seconf before the next question
    for question in questions:
        print("\n" + "-"*20)
        if ask_question(question):
            print("Correct!")
            score += 1

        else:
            print("Incorrect!")
        time.sleep(1)

    # Print the final score and percentage of correct answers
    print("\nYou got {} questions correct!".format(score))
    print("You got {:.0f}%!".format((score / len(questions)) * 100))

# If the script is run directly
    # Call the play_game() function 
if __name__ == "__main__":
    play_game()