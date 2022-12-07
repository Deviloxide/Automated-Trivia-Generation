import re

def split_paragraph_into_sentences(paragraph):
  # First, split the paragraph into sentences using a regular expression
  # that matches sentence endings, taking into account possible abbreviations,
  # such as "Mr." or "Dr."
  # Note that this is not a perfect solution and may not work in all cases,
  # but it should work for most common cases

  # Do not try to understand this regular expression
  # I do not understand it either
  sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', paragraph)

  # Return the list of sentences
  return sentences

if __name__ == '__main__':
  # Example usage
  paragraph = "A b bsf. dsfsd dsf. asfa. awe.a.a asdw awe 45gw\g. Mr. Rogers Sr. Mr. Rogers."
  sentences = split_paragraph_into_sentences(paragraph)

  # Print the sentences
  for sentence in sentences:
    print(sentence)

  print(sentences)