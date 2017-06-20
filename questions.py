class Questions(object):
    def question(self):
        question = dedent(["Q: A farmer has 13 cows. A bolt of lightning kills all but 5 of them. How many cows survived?
                           \n1. Zero\n2. Five\n3. Eight",
                           "Q: Your computer is loading. It tells you to press any key. What do you do?
                           \n1. Look for the 'any key' button
                           \n2. Press any button you want
                           \n3. Press the A, N and Y keys all at once",
                           "Q: Which is greater: six dozen dozen or half a dozen dozen?
                           \n1. Six Dozen dozen
                           \n2. Half a Dozen Dozen
                           \n3. Both Equal"])

        self.question = question


q = Questions()
lis = q.question()
print(lis)
