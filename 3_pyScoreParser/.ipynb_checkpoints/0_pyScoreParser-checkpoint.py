# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# %load_ext autoreload
# %autoreload
from pyScoreParser import data_class
from pathlib import Path

# %%
# !pwd # should be notebook directory

# %%
file_root = '../assets/1/'
xml_file = Path(file_root) / 'score.xml'
midi_file = Path(file_root) / 'Lim, HJ.mp3_repem.mid'

# %%
piece_data = data_class.PieceData(xml_path=xml_file,
                                  perform_lists=[midi_file])

# %% [markdown]
# ### Score side

# %% tags=[]
piece_data.score.__dict__.keys()

# %%
len(piece_data.score.xml_notes)

# %%
len(piece_data.score.score_midi_notes) # number of notes in generated score midi.

# %%
# number of matched notes between score midi <-> score xml
len([el for el in piece_data.score.score_pairs if el]) 

# %%
