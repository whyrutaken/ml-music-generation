from music21 import *
import glob
from tqdm import tqdm
import numpy as np
import random
from keras.layers import LSTM, Dense, Input, Dropout
from keras.models import Sequential, Model, load_model
from sklearn.model_selection import train_test_split


def read_files(file):
    notes = []
    notes_to_parse = None
    midi = converter.parse(file)
    instrmt = instrument.partitionByInstrument(midi)

    for part in instrmt.parts:
        if 'Piano' in str(part):
            notes_to_parse = part.recurse()

        for element in notes_to_parse:
            if type(element) == note.Note:
                notes.append(str(element.pitch))
            elif type(element) == chord.Chord:  # if it is chord split them into notes
                notes.append('.'.join(str(n) for n in element.normalOrder))
    return notes


file_path = ["schubert"]
all_files = glob.glob('All Midi Files/' + file_path[0] + '/*.mid', recursive=True)
notes_array = [read_files(i) for i in tqdm(all_files, position=0, leave=True)]
