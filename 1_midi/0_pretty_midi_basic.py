# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import pretty_midi
from pathlib import Path

midi_examples = list(Path('../assets').glob('*.mid'))
print(midi_examples)

# ## Load

select_idx = 3

select_idx = 3
midi_path = str(midi_examples[select_idx])
print(midi_path)

mid = pretty_midi.PrettyMIDI(midi_path) # pretty_midi does not support Path
print(mid)

# ## Investigate Basic Info

# + jupyter={"outputs_hidden": true} tags=[]
mid.__dict__
# -

mid.instruments

# + jupyter={"outputs_hidden": true} tags=[]
mid.instruments[0].__dict__
# -

mid.instruments[0].__dict__.keys()

mid.instruments[0].program

# ## Iterate notes

# + tags=[]
notes = mid.instruments[0].notes
print(notes)
# -

len(notes)

notes[0]

notes[0].__dict__

i = 20
print(f'{i}-th notes velocity:{notes[i].velocity}, \
    pitch:{notes[i].pitch}, \
    start:{notes[i].start}, \
    length:{notes[i].end - notes[i].start}')

# ### Draw midi notes as a piano roll
#

piano_roll = mid.get_piano_roll(fs=100) # fs: frames per second

piano_roll

piano_roll.shape

import matplotlib.pyplot as plt

plt.imshow(piano_roll, aspect='auto', origin='lower')


