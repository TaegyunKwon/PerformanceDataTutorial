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

# +
# # !pip install music21==7.1
# # !add-apt-repository ppa:mscore-ubuntu/mscore3-stable
# # !apt-get update
# # !apt-get install musescore3
# -

from music21 import *
us = environment.UserSettings()
us['musescoreDirectPNGPath'] = '/usr/bin/musescore3'
us['directoryScratch'] = '/tmp'

import music21

n = note.Note('C#5')
n.show()

score = 'assets/Beethoven_Sonata_8_2/score.xml'

c = converter.parse(score)
c.measures(1, 5).show() # show first 5 measures

# + tags=[]

