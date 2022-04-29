from random import randint
import markovify
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--count', metavar='N', type=int,
                    help='Number of cartridges to generate')

args = parser.parse_args()

# Get raw base text as a list
with open("./corpus.txt") as f:
    text = f.read()
name_list = list(text.split("\n"))

# Create initial cartridge name from 1 to 3 elements of the name_list to train the model
new_corpus = ""
for i in range(200):
    name_length = randint(1, 3)
    for e in range(name_length):
        selector = randint(0, (len(name_list) - 1))
        new_corpus += f" " + (name_list[selector])
    new_corpus += "\n"

# Build the model based on those iterations
text_model = markovify.NewlineText(new_corpus, state_size=1)


# Print three randomly-generated sentences of no more than 280 characters
for i in range(args.count):
    name = None
    metric = randint(0, 1)
    if (metric == 0):
        caliber = f".{randint(0, 500)}"
    else:
        caliber = f"{randint(4, 12)}.{randint(0, 9)}×{randint(10, 80)}"
    while name is None: # Markovify will sometimes return None for short sentences, so try until it doesn't
        name = text_model.make_short_sentence(30)
    print(f"{caliber} {name}")