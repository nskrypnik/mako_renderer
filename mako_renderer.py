# -*- coding: utf-8 -*-

import os

from optparse import OptionParser
from mako.lookup import TemplateLookup

parser = OptionParser(usage="Usage: mako_renderer.py FILE -o FILE")
parser.add_option("-o", "--output-file", help="path to output file", dest="output")
        

(options, args) = parser.parse_args()
print(options)

if not len(args): templatename = 'index.html'

if not options.output: out_file_name = 'index_rendered.html'

curr_dir = os.getcwd()

lookup = TemplateLookup(directories=[curr_dir])
template = lookup.get_template(templatename)
rendered = template.render(MEDIA_URL = '.')

out_file = open(out_file_name, 'wb')
out_file.write(rendered)
