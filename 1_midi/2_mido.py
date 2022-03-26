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

import mido
from pathlib import Path

midi_examples = list(Path('../assets').glob('*.mid'))
print(midi_examples)

# ## Load

select_idx = 3

select_idx = 3
midi_path = str(midi_examples[select_idx])
print(midi_path)

# + tags=[]
mid = mido.MidiFile(midi_path)
print(mid)

# + tags=[]
mid.tracks
# -

print(mid.tracks[0])

# + jupyter={"outputs_hidden": true} tags=[]
print(mid.tracks[1])
# -

mid.ticks_per_beat

mid.__dict__.keys()

mido.tick2second(tick=120, ticks_per_beat=120, tempo=1200000)


