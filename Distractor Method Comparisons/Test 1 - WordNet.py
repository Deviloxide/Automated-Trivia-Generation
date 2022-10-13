import nltk
from nltk.corpus import wordnet as wn


# get the synsets for a word
def create_distractors_wordnet(word, definition = 0, category = 0):
    distractors = []
    word = word.lower()
    # format the word for searching
    if len(word.split()) > 0:
        word = word.replace(" ", "_")
    # get the synsets for the word using the definition number
    syn = wn.synsets(word, 'n')[definition]
    # get the hypernyms for the synset
    hypernym = syn.hypernyms()
    if len(hypernym) == 0:
        return syn, distractors
    # get the hyponyms for the hypernym
    for item in hypernym[category].hyponyms():
        name = item.lemmas()[0].name()
        if name == word:
            continue
        # remove the underscores from the hyponym and capitalize the word(s)
        name = name.replace("_", " ")
        name = " ".join(w.capitalize() for w in name.split())
        # add the hyponym to the list of distraction words
        if name is not None and name not in distractors:
            distractors.append(name)
    return syn, distractors


answer = "Tesla"
result = create_distractors_wordnet(answer)

print("Original Word:", answer)
print("Meaning Used:", result[0].definition())
print("Distractors:", result[1])
