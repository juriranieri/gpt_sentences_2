# Weird LLM

This project aims to build a weird LLM based on sentences.

## Phase One: Sentence-based BERT Encoder

### 1. Data Preparation

The first step is to acquire text data. The `download_data.py` script is designed to download the `fineweb-edu` dataset from Hugging Face.

**NOTE:** The dataset is large. For development purposes, you can use the provided `data/dummy_data.txt` file.

To download the real dataset, run:
```bash
python download_data.py
```

### 2. Pre-processing

The `preprocess.py` script takes a text file, tokenizes it into sentences, and saves the result.

To run the pre-processing on the dummy data:
```bash
python preprocess.py
```
This will create `data/processed_sentences.txt`.

### 3. BERT Encoding

The `bert_encoder.py` script reads the processed sentences and uses a pre-trained BERT model to generate sentence embeddings.

To generate embeddings for the processed dummy data:
```bash
python bert_encoder.py
```
This will create `data/bert_embeddings.npy`.

## Project Structure

```
.
├── data
│   ├── dummy_data.txt
│   ├── processed_sentences.txt
│   └── bert_embeddings.npy
├── venv
├── download_data.py
├── preprocess.py
├── bert_encoder.py
├── requirements.txt
├── GEMINI.md
└── requirements.md
```
