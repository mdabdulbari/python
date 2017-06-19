import time
i = 60
dead = Dead()


class Time(object):

    def counter(self):
        while True:
            if i != 00:
                print(f"{i}\r", end="")
                i = i - 1
                time.sleep(1)
                if i == 30:
                    print("Half time")
            else:
                exit(0)


class Scene(object):

    def __init__(self):
        print("Something Wrong")
        exit(0)


class Loading(Scene):

    def enter(self):
        while True:
            for i in [".", "..", "..."]:
            print(f"Loading {i}\r", end='')


class Dead(Scene):
    def death():
        print("You are dead, such a loser")
        exit(0)


class Options(Scene):

    def option(self):
        if input == quiz.correct_answer:
            print()
        else:
            dead.death()


class Quiz(Scene):

    def enter(self):

        print("Hello, you are in room ----")
        print("There is a door in front of you and a huge rock above you")
        print("You have to complete a quiz to unlock the door")
        print("You get 60 seconds to complete the test")
        print()
        print("Make your mind and press ENTER when you are ready")
        input()
        Loading.enter()
        print("Welcome to the quiz")
        print("Q. A farmer has 13 cows. A bolt of lightning kills all but 5 of them. How many cows survived?\n1. Zero\n2. Five\n3. Eight")


class Questions(object):
    def question(self):
        self.question = []


time = Time()
counter = time.counter()
