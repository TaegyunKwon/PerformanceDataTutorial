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

# %% [markdown]
# ## List Comprehension

# %%
a = [el for el in range(10)]
print(a)

# %% [markdown]
# is equal to:

# %%
a = []
for el in range(10):
    a.append(el)
print(a)

# %% [markdown] tags=[]
# ## Ranged list

# %%
start = 0
step = 2
end = 10
a = range(start, end, step)
print(a) # a is generator, not the list itself
print(list(a))

# %% [markdown]
# only integers are allowed

# %%
print(range(0,9.5,2)) # error raise

# %%
print(list(range(0,10,3)))

# %% [markdown]
# ## Basic indexing

# %%
a = list(range(10))
print(a)

# i-th value:
i = 6
print(a[i])

# i-th from backward:
print(a[-i])

# %% [markdown]
# ## Path control
# https://docs.python.org/3/library/pathlib.html

# %%
from pathlib import Path

# %% [markdown]
# List files in a directory

# %%
list(Path('basics_assets').iterdir())

# %% [markdown]
# Find files with specific extension

# %%
list(Path('basics_assets').glob('*.py'))

# %% [markdown]
# write down specific file

# %%
file_name = Path('basics_assets') / 'e.json'

# %%
print(file_name.parent)

# %%
print(file_name.name)

# %% [markdown]
# ### Lambda Sort

# %%
import numpy as np
import randomname

# %% [markdown]
# make arbitary data

# %%
unsorted_list = []
for n in range(10):
    user_name = randomname.generate()
    age = np.random.randint(100)
    unsorted_list.append((user_name, age))
print(unsorted_list)

# %% [markdown]
# sort them according to second element (age)

# %%
sorted_list = sorted(unsorted_list, key=lambda x:x[1]) # x[1] becomes standard

# %%
print(sorted_list)

# %% [markdown]
# ### F string

# %%
name = 'Taegyun Kwon'
height = 187.5
item_in_pocket = ['piano', 'flower', 'book']

print(
    f"you can write python variables like this: \
    {name}'s height is {height}, \
    and he have {item_in_pocket} in his pocket")

# %%
a = 2
b = 4.6
c = 0.123456789
print(f'you can do everything inside. {a} + {b} = {a+b}')
print(f'you can control digits with :.(digit)f expres

# %% [markdown]
# ### File read & write
