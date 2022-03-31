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
from pyScoreParser import data_class, xml_utils, utils, feature_utils
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# !pwd # should be notebook directory

file_root = '../assets/Beethoven_Sonata_8_2/'
xml_file = Path(file_root) / 'score.xml'
midi_files = [el for el in Path(file_root).glob('*.mid') if 'score' not in el.name]

piece_data = data_class.PieceData(xml_path=xml_file,
                                  perform_lists=midi_files)

performance = piece_data.performances[0]

perform_notes = performance.midi_notes

perform_notes[0]

# + [markdown] tags=[]
# ### make piano roll with perform_notes

# + tags=[]
matched_idx = performance.match_between_xml_perf

# + tags=[] jupyter={"outputs_hidden": true}
matched_idx


# -

def note_to_pixel(note, frame_per_second=50):
    # convert note into array index
    onset_x = np.rint(note.start*frame_per_second)
    offset_x = np.rint(note.end*frame_per_second)
    y = note.pitch - 21
    return dict(x_start=onset_x, x_end=offset_x, y=y)


note_to_pixel(perform_notes[0])

draw_range = 30 # let's draw first 30 seconds
figure = plt.figure(figsize=(10,5))
for note in perform_notes:
    if note.start < draw_range:
        arr_dict = note_to_pixel(note)
        # plt.hlines(arr_dict['y'], [arr_dict['x_start'], arr_dict['x_end']])
        plt.plot([arr_dict['x_start'], arr_dict['x_end']], [arr_dict['y'], arr_dict['y']], linewidth=4, color='b')


# we will paint aligned notes with blue, and non-aligned notes with red

for n, note in enumerate(perform_notes):
    if note.start < draw_range:
        if n in matched_idx:
            color = 'b'
        else:
            color = 'r'
        arr_dict = note_to_pixel(note)
        # plt.hlines(arr_dict['y'], [arr_dict['x_start'], arr_dict['x_end']])
        plt.plot([arr_dict['x_start'], arr_dict['x_end']], [arr_dict['y'], arr_dict['y']], linewidth=4, color=color)


