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

# %load_ext autoreload
# %autoreload
from pyScoreParser import data_class
from pathlib import Path

# !pwd # should be notebook directory

file_root = '../assets/Beethoven_Sonata_8_2/'
xml_file = Path(file_root) / 'score.xml'
midi_files = [el for el in Path(file_root).glob('*.mid')]

piece_data = data_class.PieceData(xml_path=xml_file,
                                  perform_lists=midi_files)

# ### Score Side

# + tags=[]
piece_data.score.__dict__.keys()
# -

len(piece_data.score.xml_notes)

# number of notes in generated score midi.
# = #xml_notes - #overlapped
len(piece_data.score.score_midi_notes) 

# ### Check overlap notes

# check there are overlap notes
for n, note in enumerate(piece_data.score.xml_notes):
    if note.is_overlapped ==True:
        print(f'idx:{n}, {note}')

# number of matched notes between score midi <-> score xml
len([el for el in piece_data.score.score_pairs if len(el) != 0 ]) 

# overlapped notes does not erased, but matched with same midi note

piece_data.score.score_pairs[212:216]

# ## Performance Side

piece_data.performances[0].__dict__.keys()

# midi notes
len(piece_data.performances[0].midi_notes)

# +
# matched index between score_pairs <-> performance midi
# if match_between_xml_perf[i] == j,
# score.xml_notes[i] is aligned with perform.midi_notes[j]

print(piece_data.performances[0].match_between_xml_perf[:20])
# -


# Empty elements indicates the note was not matched either in score midi alignment, or perform midi alignment

print(len(piece_data.performances[0].match_between_xml_perf)) # same as len(xml_notes)

for pair in piece_data.performances[0].pairs[:10]:
    print(pair)
print(len(piece_data.performances[0].pairs)) # same as len(xml_notes)




