from random import randint
import markovify

class Cartridge():
    def __init__(self):
        if not self.args:
            self.args = []
        pass

    def generate_cartridge(args):
        # Get raw base text as a list
        with open("./adjectives.txt") as a:
            names = a.read()
        with open("./gunwords.txt") as g:
            names += g.read()
        with open("./awesomewords.txt") as l:
            names += l.read()

        name_list = list(names.split("\n"))

        # Create initial cartridge name seeds to train the model
        new_corpus = ""
        for i in range(200):
            name_length = randint(1, 3)
            for e in range(name_length):
                selector = randint(0, (len(name_list) - 1))
                new_corpus += f" " + (name_list[selector])
            new_corpus += "\n"

        # Build the model based on those iterations
        text_model = markovify.NewlineText(new_corpus, state_size=1)

        cartridges = []
        for i in range(args.count):
            name = None
            metric = randint(0, 1)
            if (metric == 0):
                caliber = f".{randint(0, 500)}"
            else:
                caliber = f"{randint(4, 12)}.{randint(0, 9)}×{randint(10, 80)}"
            while name is None: # Markovify will sometimes return None for short sentences, so try until it doesn't
                name = text_model.make_short_sentence(30)
            cartridges.append(f"{caliber} {name}")
        return cartridges