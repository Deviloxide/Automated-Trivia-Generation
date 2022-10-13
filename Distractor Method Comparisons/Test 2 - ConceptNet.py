import requests


# http://conceptnet.io/ is a free, open-source, community-built semantic network
def create_distractors_conceptnet(word):
    word = word.lower()
    if len(word.split()) > 0:
        word = word.replace(" ", "_")
    distractor_list = []
    # get the conceptnet data for the word
    url = "https://api.conceptnet.io/query?node=/c/en/%s/n&rel=/r/PartOf&start=/c/en/%s&limit=5" % (word, word)
    obj = requests.get(url).json()

    # get edges from the conceptnet data
    for outer_edge in obj['edges']:
        link = outer_edge['end']['term']

        # get the data for the edge from the conceptnet data
        url2 = "https://api.conceptnet.io/query?node=%s&rel=/r/PartOf&end=%s&limit=10" % (link, link)
        obj2 = requests.get(url2).json()
        for inner_edge in obj2['edges']:
            word2 = inner_edge['start']['label']
            if word2 not in distractor_list and word != word2.lower():
                distractor_list.append(word2)

    return distractor_list


answer = "kiribati"
distractors = create_distractors_conceptnet(answer)

print("Original word:", answer)
print("Distractors:", distractors)
