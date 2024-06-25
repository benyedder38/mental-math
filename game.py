import random
import time
import threading
import sys

class MentalMathGame:
    def __init__(self):
        self.score = 0
        self.lives = 3
        #self.timeout = 10

    def print_game_intro(self):
        print("========= [ MENTAL MATHEMATICS ] ==========")
        print("""
        """)
        #print("TO START")
        #print("PRESS ANY KEY")

    def print_help(self):
        print("========== [ HELP ] ==========")
        print("""
            a -> Addition questions
            s -> Subtraction questions
            m -> Multiplication questions
            m11 -> Multiples of 11 questions
            ms -> Squared questions
            d -> Division questions

            lives = 3, lost whenever timeout or incorrect answer is inputted
        """)

    def get_game_mode(self):
        while True:
            operation = input("Please choose a game mode [a, s, m, m11, ms, d] OR h for help: ").strip().lower()
            if operation in ['a', 's', 'm', 'm11' , 'ms', 'd']:
                return operation      
            elif operation == 'h':
                self.print_help()
            else:
                print("Invalid key, please try again.")

    def generate_problem(self, operation):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        if operation == 'a':
            question = f"{num1} + {num2} = "
            answer = num1 + num2
        elif operation == 's':
            question = f"{num1} - {num2} = "
            answer = num1 - num2
        elif operation == 'm':
            question = f"{num1} x {num2} = "
            answer = num1 * num2
        elif operation == 'm11':
            question = f"{num1} x 11 = "
            answer = num1 * 11
        elif operation == 'ms':
            question = f"{num1}^2 = "
            answer = num1 * num1
        elif operation == 'd':
            num1 = num2 * random.randint(1, 10)
            question = f"{num1} / {num2} = "
            answer = num1 // num2
        return question, answer

    def question_prompt(self, question, answer):
        player_answer = [None]

        def get_player_input():
            #while True:
                try:
                    player_answer[0] = int(input(question))
                    #break
                except ValueError:
                    print("Please enter a valid integer.")

        #input_thread = threading.Thread(target=get_player_input)
        #input_thread.start()
        #input_thread.join(self.timeout)

        #if input_thread.is_alive():
        #    print("Times up!")
        #    return False
        #else:
        #    return player_answer[0] == answer
        get_player_input()
        return player_answer[0] == answer

    def play(self):
        self.print_game_intro()
        operation = self.get_game_mode()

        # start the game
        while self.lives > 0:
            curr_question, curr_answer = self.generate_problem(operation)
            # if the question is answered within the timeout, increment score, else decrement lives
            if self.question_prompt(curr_question, curr_answer):
                self.score += 1
                print(f"Correct. Your score is currently {self.score}.")
            else:
                self.lives -= 1
                if self.lives == 0:
                    print(f"GAME OVER. Your score was {self.score}.")
                    sys.exit()
                else:
                    print(f"Wrong or times up. You have {self.lives} lives remaining. Your score is currently {self.score}.")
            #time.sleep(1)

if __name__ == "__main__":
    game = MentalMathGame()
    game.play()

