import os
import pandas as pd

class MaestroDataset:
    def __init__(self, csv_path="./maestro-v3.0.0/maestro-v3.0.0.csv", data_dir="./maestro-v3.0.0/"):
        self.data_dir = data_dir
        self.df = pd.read_csv(csv_path)

    def get_all_midi_files(self):
        """
        Output:
        - A Python list containing file paths to the midi files
        """
        files = []
        if os.path.exists(self.data_dir):
            # Iterate through each year directory
            for year in os.listdir(self.data_dir):
                year_path = os.path.join(self.data_dir, year)
                if os.path.isdir(year_path):
                    # Iterate through each midi file
                    for midi_file in os.listdir(year_path):
                        files.append(os.path.join(year_path, midi_file))
            return files
        else:
            print(f"Path not found: {self.path}")
            return []
    
    def get_split_files(self, split):
        """
        Retrieves midi files for a specific split

        Input:
        - split: "test", "validation", or "train"

        Output:
        - A Python list containing file paths to the midi files
        """
        split_files = self.df[self.df['split'] == split]['midi_filename'].tolist()
        return [os.path.join(self.data_dir, f) for f in split_files]