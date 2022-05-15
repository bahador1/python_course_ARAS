#so wtf is __init__.py
# __init__.py is not required since py3.3+
# but the only one important use of __init__.py is when we decide if a particular folder behave 
# as a namespace or as a regular package

import dir1.submodule2
#the output would be 
# hello world from dir1 package
# herer is submodule1
# herer is submodule2