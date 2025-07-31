
import os
from datasets import load_dataset

def download_and_save_data():
    """
    Downloads the FineWeb-Edu dataset and saves it to the 'data' directory.
    """
    # Name of the sample to download
    remote_name = "sample-10BT"
    
    # Create the data directory if it doesn't exist
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)
    
    # Check if the file already exists
    output_file = os.path.join(data_dir, "fineweb_edu_sample.txt")
    if os.path.exists(output_file):
        response = input(f"The file {output_file} already exists. Do you want to download it again? (y/n): ")
        if response.lower() != 'y':
            print("Skipping download.")
            return

    # Load the dataset
    print(f"Loading dataset: {remote_name}...")
    fw = load_dataset("HuggingFaceFW/fineweb-edu", name=remote_name, split="train", streaming=True)
    
    # Save the dataset to a text file
    print(f"Saving dataset to {output_file}...")
    
    with open(output_file, "w", encoding="utf-8") as f:
        for i, entry in enumerate(fw):
            f.write(entry['text'] + '\n')
            if i % 1000 == 0:
                print(f"Processed {i} entries...")

    print("Done.")

if __name__ == "__main__":
    download_and_save_data()
