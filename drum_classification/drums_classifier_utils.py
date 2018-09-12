import os
import zipfile

def prep_dataset():
    os.system('wget http://www.hexawe.net/mess/200.Drum.Machines/drums.zip')

    with zipfile.ZipFile('drums.zip') as zf:
        zf.extractall('.')
