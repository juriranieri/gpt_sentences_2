

import os
import nltk
from nltk.tokenize import sent_tokenize

# Download the 'punkt' tokenizer models
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt')
    nltk.download('punkt_tab')

def preprocess_data(input_file, output_file):
    """
    Reads text from the input file, tokenizes it into sentences,
    and saves the sentences to the output file.
    """
    print(f"Reading data from {input_file}...")
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    print("Tokenizing sentences...")
    sentences = sent_tokenize(text)

    print(f"Saving sentences to {output_file}...")
    with open(output_file, "w", encoding="utf-8") as f:
        for sentence in sentences:
            f.write(sentence + '\n')

    print("Done.")

if __name__ == "__main__":
    input_file = os.path.join("data", "dummy_data.txt")
    output_file = os.path.join("data", "processed_sentences.txt")
    preprocess_data(input_file, output_file)

