import random
import nltk

def blank_out_noun(sentence):
    # Use NLTK to tokenize the sentence and tag each word with its part of speech
    tokens = nltk.word_tokenize(sentence)
    tagged_tokens = nltk.pos_tag(tokens)

    # Create a list of all the nouns in the sentence
    nouns = [word for word, pos in tagged_tokens if pos.startswith("N")]

    # Pick a random noun from the list
    random_noun = random.choice(nouns)

    # Replace the chosen noun with blanks in the sentence
    modified_sentence = sentence.replace(random_noun, "_____")

    # Return the modified sentence and the noun that was replaced
    return modified_sentence, random_noun

def blank_out_list(sentences):
    blanked_sentences = []
    for sentence in sentences:
        if len(sentence) > 2:
            blanked_sentences.append(blank_out_noun(sentence))
        else:
            blanked_sentences.append(sentence)
    return blanked_sentences

if __name__ == '__main__':
    # Test the function with a sample sentence
    sentence = "The 2006 Securitas depot robbery in Tonbridge, Kent, was the largest ever cash heist in the UK."
    for i in range(100):
        clozed_sentence = blank_out_noun(sentence)
        print(clozed_sentence[0])
        print(clozed_sentence[1])