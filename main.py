#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import chardet
import locale
bbb = '【】'
print sys.getdefaultencoding()
print sys.stdin.encoding
print sys.stdout.encoding
print locale.getdefaultlocale()
print (locale.getpreferredencoding())
print (sys.getfilesystemencoding())
print chardet.detect(bbb)['encoding']
print chardet.detect(bbb)
print bbb.decode(chardet.detect(bbb)['encoding']).encode(sys.stdin.encoding)
for filename in os.listdir('tmp'):
    print chardet.detect(filename)['encoding']
    print filename.decode(sys.getfilesystemencoding()).encode(sys.stdout.encoding)
    # print filename.decode(chardet.detect(filename)['encoding']).encode(sys.stdout.encoding)
print 'xxx'
