

direction = ["north", "south", "east", "west",
             "down", "up", "left", "right", "back"]
verb = ["go", "stop", "kill", "eat"]
stop_words = ["the", "in", "of", "from", "at", "it"]
nouns = ["door", "bear", "princess", "cabinet"]
numbers = []


def scan(stuff):
    word_list = []
    words = stuff.split()

    for word in words:
        word_list.append((word_type, word))
    return word_list
