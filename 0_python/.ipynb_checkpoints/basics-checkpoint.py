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

# %% [markdown]
# ### F string

# %% [markdown]
# ### File read & write
