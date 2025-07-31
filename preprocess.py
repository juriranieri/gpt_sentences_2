import os
import nltk
from nltk.tokenize import sent_tokenize

# Download the 'punkt' tokenizer models
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def preprocess_data(input_file, output_file):
    """
    Reads text from the input file, tokenizes it into sentences,
    and saves the sentences to the output file with <NEW_DOC> separators.
    """
    print(f"Reading data from {input_file}...")
    total_size = os.path.getsize(input_file)
    processed_size = 0
    print(f"Processing {total_size / (1024*1024):.2f} MB of data...")

    with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
        for i, line in enumerate(f_in):
            processed_size += len(line.encode('utf-8'))
            sentences = sent_tokenize(line)
            for sentence in sentences:
                f_out.write(sentence + '\n')
            f_out.write("<NEW_DOC>\n")

            if (i + 1) % 1000 == 0:
                percentage = (processed_size / total_size) * 100
                print(f"Processed {i + 1} documents... ({percentage:.2f}%)")

    print("Done.")

if __name__ == "__main__":
    input_file = os.path.join("data", "fineweb_edu_sample.txt")
    output_file = os.path.join("data", "processed_sentences.txt")
    preprocess_data(input_file, output_file)