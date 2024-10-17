# libs
import os, sys
cwd = os.getcwd()
os.chdir('src/'); path_to_src = os.getcwd()
os.chdir(cwd)
if path_to_src not in sys.path:
    sys.path.append(path_to_src)
from _libs import *
from _usr_libs import *

a = pd.DataFrame({'a': [1, 2], 
                  'b': [3, 4]})
b = pd.DataFrame({'b': [4, 5], 
                  'a': [6, 7]})

c = pd.concat([a, b], axis=0)
print(c)