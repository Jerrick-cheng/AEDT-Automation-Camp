# -*- coding: utf-8 -*-

import webbrowser, os

html_file='d:/demo/test.html'
with open(html_file,'w') as sf:       
    sf.writelines('Hello World!')        

webbrowser.open('file://' + os.path.realpath(html_file))
