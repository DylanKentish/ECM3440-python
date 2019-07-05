#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '../../../Documents/ExeterUni'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# ## A minimal Python program:

#%%
print("hello everyone!")

#%% [markdown]
# ## A longer program: bottles.py

#%%
bottles = 10

while bottles > 0:
    print ( bottles , " green bottles hanging on the wall, " )
    print ( bottles , " green bottles hanging on the wall, " )
    print ( " and if one green bottle should accidentally fall , " )
    print ( " there’ll be " , bottles -1 , " green bottles hanging on the wall. " ) 
    print ()
    bottles = bottles - 1

print ( "All gone" )

#%% [markdown]
# ### Short version

#%%
bottles = 5
while bottles > 0:
    print("There are", bottles, "left")
    bottles = bottles - 1

#%% [markdown]
# ## Installing Nteract
# Visit [nteract.io](https://nteract.io)
# 
# Install Python if you don't have it already.  From [python.org](https://python.org)
# 
# Install extra libraries.  Probably like this:
# ```bash
# python3 -m pip install ipykernel --user
# python3 -m pip install plotly --user
# ```
# 
#%% [markdown]
# Some maths
# 
# 
# \begin{align}
# \dot{x} & = \sigma(y-x) \\
# \dot{y} & = \rho x - y - xz \\
# \dot{z} & = -\beta z + xy
# \end{align}
# 
# 