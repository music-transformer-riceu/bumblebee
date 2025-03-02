from musiclang_predict import MusicLangTokenizer
from musiclang import Score
import torch
from torch.utils.data import Dataset, DataLoader
import MaestroDataset

class TokenDataSet(Dataset):
    """
    A Custom PyTorch dataset class 
    """
    def __init__(self, tokens, tokenizer, max_length=512):
        """
        Args:
            tokens (list): List of tokenized strings from the MIDI file.
            tokenizer (MusicLangTokenizer): The tokenizer used for converting tokens to IDs.
            max_length (int, optional): Maximum sequence length for padding. Default is 512.
        """
        self.tokens = tokens
        self.tokenizer = tokenizer
        self.max_length = max_length

        # Convert tokens to token IDs using the tokenizer
        self.token_ids = self.tokenizer.encode(self.tokens)
        
        # Pad the token_ids if necessary
        self.token_ids = self.token_ids[:self.max_length]  # truncate if it's too long
        self.token_ids += [self.tokenizer.pad_token_id] * (self.max_length - len(self.token_ids))  # pad if it's too short

    def __len__(self):
        return len(self.token_ids)

    def __getitem__(self, idx):
        """
        Args:
            idx (int): The index of the sample to fetch.

        Returns:
            torch.Tensor: The token IDs for the sample.
        """
        return torch.tensor(self.token_ids[idx], dtype=torch.long)


midi_file = 'path_to_your_midi_file.mid'
score = Score.from_midi(midi_file)
tokenizer = MusicLangTokenizer('musiclang/musiclang-4k')
tokens = tokenizer.tokenize(score)

dataset = MusicLangDataset(tokens, tokenizer)

