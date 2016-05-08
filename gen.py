#!/usr/bin/env python
#!/bin/python3

# install:
#   pip install watchdog
#   pip install mako
#
# run(all):
#   ./gen.py
#
# run(watchdog):
#   watchmedo shell-command --patterns="*.mako" --recursive --command='./gen.py ${watch_src_path}'

import sys
import os
import re
import datetime
import glob
from mako.template import Template
from mako.lookup import TemplateLookup

def gen_template(fname_src, fname_dest):
    print("[%s] %s -> %s" % (datetime.datetime.now(), fname_src, fname_dest))
    tpldir = re.sub("/[^/]*$", "", fname_dest)
    lookup = TemplateLookup(directories=[os.path.realpath('./')])
    tpl = Template(filename=fname_src,input_encoding='utf-8',output_encoding='utf-8',lookup=lookup)
    str = tpl.render_unicode()

    dirpath = re.sub("/[^/]*$", "", 'gen/' + fname_dest)
    if (not os.path.exists(dirpath)):
        os.makedirs(dirpath)

    f = open('gen/' + fname_dest, 'w')
    f.write(str)
    f.close()

if(len(sys.argv) > 1):
    fname_src = sys.argv[1]
    fname_dest = re.sub(".mako$", "", fname_src)
    gen_template(fname_src, fname_dest)
else:
    for root, dirs, files in os.walk(u'./'):
        for file_ in files:
            full_path = os.path.join(root, file_)
            if(re.match(".*mako$", full_path)):
                fname_dest = re.sub(".mako$", "", full_path)
                gen_template(full_path, fname_dest)
