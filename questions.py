class Questions(object):
    def question(self):
        question = ["Q: A farmer has 13 cows. A bolt of lightning kills all but 5 of them. How many cows survived?\n1. Zero\n2. Five\n3. Eight", "Q: Your computer is loading. It tells you to press any key. What do you do?\n1. Look for the "any key" button\n2. Press any button you want\n3. Press the A, N and Y keys all at once"]
        self.question = question


q = Questions()
lis = q.question()
print(lis)
