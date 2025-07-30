
import os
import torch
from transformers import BertTokenizer, BertModel
import numpy as np

def encode_sentences(input_file, output_file):
    """
    Reads sentences from the input file, encodes them using a pre-trained
    BERT model, and saves the embeddings to the output file.
    """
    print(f"Reading sentences from {input_file}...")
    with open(input_file, "r", encoding="utf-8") as f:
        sentences = f.readlines()

    # Load pre-trained model tokenizer (vocabulary)
    print("Loading BERT tokenizer...")
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    # Load pre-trained model (weights)
    print("Loading BERT model...")
    model = BertModel.from_pretrained('bert-base-uncased',
                                      output_hidden_states = True, # Whether the model returns all hidden-states.
                                      )

    # Put the model in "evaluation" mode, meaning feed-forward operation.
    model.eval()

    print("Encoding sentences...")
    # Tokenize all of the sentences and map the tokens to their word IDs.
    input_ids = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")['input_ids']

    # Predict hidden states features for each layer
    with torch.no_grad():
        outputs = model(input_ids)
        hidden_states = outputs[2]

    # `hidden_states` is a tuple of 13 tensors, one for the output of the embeddings and the output of each of the 12 layers.
    # We'll average the last 4 layers to get a good sentence representation.
    sentence_embeddings = torch.stack(hidden_states[-4:]).sum(0).mean(1)

    print(f"Saving embeddings to {output_file}...")
    np.save(output_file, sentence_embeddings.numpy())

    print("Done.")

if __name__ == "__main__":
    input_file = os.path.join("data", "processed_sentences.txt")
    output_file = os.path.join("data", "bert_embeddings.npy")
    encode_sentences(input_file, output_file)
