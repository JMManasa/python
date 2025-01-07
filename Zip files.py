from zipfile import *
p=ZipFile("anil.zip",'w',ZIP_DEFLATED)
p.write('pfiles.txt')
p.close
