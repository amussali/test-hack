import random
class Funny:
    def __init__(self):
        self.name = "Funny"

    def joke(self):
        return "I'm a funny class"

    def laugh(self):
        return "Haha"

    def cry(self):
        return "Oh no"

    def sleep(self):
        return "ZZZZ"

    def pun(self):
        puns = [
            "I would tell you a construction pun, but I'm still working on it.",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Why did the scarecrow win an award? Because he was outstanding in his field.",
            "Why don’t skeletons fight each other? They don’t have the guts.",
            "I used to be a baker, but I couldn't make enough dough."
        ]
        return random.choice(puns)

    def prank(self):
        pranks = [
            "Put googly eyes on everything in the fridge.",
            "Replace your friend's phone language with Klingon.",
            "Put a piece of tape over the bottom of the mouse.",
            "Switch the sugar and salt.",
            "Set all the clocks forward by one hour."
        ]
        return random.choice(pranks)

    def slip_on_banana_peel(self):
        return "Whoops! *slips* That was un-peel-ievable!"

    def knock_knock(self):
        jokes = [
            ("Lettuce", "Lettuce in, it's cold out here!"),
            ("Tank", "You're welcome!"),
            ("Cow says", "No, a cow says mooo!"),
            ("Boo", "Don't cry, it's just a joke!"),
            ("Etch", "Bless you!")
        ]
        who, punchline = random.choice(jokes)
        return f"Knock knock.\nWho's there?\n{who}.\n{who} who?\n{punchline}"