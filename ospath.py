import os
print(" current working directory  is % s" % os.getcwd())
print("dirname of current file is % s" % os.path.dirname(__file__))
print("realpath of current file is % s" % os.path.realpath(__file__))
print("abspath of current file is % s" % os.path.abspath(__file__))
print(" one level up  previous dir   of current file is % s" % os.path.join(os.path.abspath(__file__), '..'))
print("basename of current file is % s" % os.path.basename(__file__))
abspath = os.path.dirname(os.path.abspath(__file__))
print("dirname  of os.path.abspath with current file is % s" % os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(abspath, '../')
print("constructed path for prev dir is  %s" % p)
print("check if path exists result is %s" % os.path.exists(p))
print("check if path is a dir %s" % os.path.isdir(p))
newfile = os.path.join(p, 'newfile')
with open(newfile, 'w') as f:
   f.write('test')
print("check newfile is created %s" % os.path.exists(newfile))
print("check newfile is  a file  %s" % os.path.isfile(newfile))
'''
(venvp3flask) bhujay@DESKTOP-DTA1VEB:/mnt/c/mydev/myflask$ python ospath.py
 current working directory  is /mnt/c/mydev/myflask
dirname of current file is
abspath of current file is /mnt/c/mydev/myflask/ospath.py
basename of current file is ospath.py
dirname  of os.path.abspath with current file is /mnt/c/mydev/myflask
'''
