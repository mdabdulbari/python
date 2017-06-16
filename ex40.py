class Song(object):

    def __init__(self, lyc):
        self.lyrics = lyc

    def sing(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing()

bulls_on_parade.sing()
