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
midi_path = str(midi_examples[select_idx])
print(midi_path)

mid = pretty_midi.PrettyMIDI(midi_path) # pretty_midi does not support Path
print(mid)

# ### Ex 1: change tempo 1.2 times

new_mid = pretty_midi.PrettyMIDI()
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  #  == 0
piano_inst = pretty_midi.Instrument(program=piano_program)

for note in mid.instruments[0].notes:
    new_note = note
    new_note.start = note.start / 1.2
    new_notes.end = note.end / 1.2
    piano_inst.notes.append(new_note)

new_mid.instruments.append(piano_inst)
new_mid.write('new_midi.mid')


