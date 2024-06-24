import random
import time
import threading

def print_game_intro():
    print("========= [ MENTAL MATHEMATICS ] ==========")
    print("""
    """)
    #print("TO START")
    #print("PRESS ANY KEY")

def print_help():
    print("========== [ HELP ] ==========")

def get_game_mode():
    while True:
        operation = input("Please choose a game mode [a, s, m, d] OR h for help: ").strip().lower()
        if operation in ['a', 's', 'm', 'd', 'h']:
            return operation
        else:
            print("Invalid key, please try again")

def generate_problem(operation):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    if operation == 'a':
        question = f"{num1} + {num2}"
        answer = num1 + num2
    elif operation == 's':
        question = f"{num1} - {num2}"
        answer = num1 - num2
    elif operation == 'm':
        question = f"{num1} x {num2}"
        answer = num1 * num2
    elif operation == 'd':
        question = f"{num1} / {num2}"
        answer = num1 // num2

    return question, answer

def question_prompt(question, answer, timeout):
    player_answer = None

    def get_player_input():
        nonlocal player_answer
        player_answer = input(f"{question}")
        
    input_thread = threading.Thread(target=get_player_input)
    input_thread.start()
    input_thread.join(timeout)

    if player_answer is None:
        print("Times up!")
        time.sleep(2)
        return False
    else:
        return int(player_answer) == answer

def main():
    print_game_intro()
    operation = get_game_mode()
    score = 0
    lives = 3

    # start the game
    while True:
        curr_question, curr_answer = generate_problem(operation)
        # if the question is answered within 5 seconds, increment score, else take a live
        if question_prompt(curr_question, curr_answer, 5):
            score += 1
            print(f"Correct. Your score is currently {score}.")
            time.sleep(2)
        else:
            lives -= 1
            if lives == 0:
                print(f"GAME OVER. Your score was {score}.")
                break
            else:
                print(f"Wrong or times up. You have {lives} remaining. Your score is currently {score}.")
            time.sleep(2)
if __name__ == "__main__":
    main()
