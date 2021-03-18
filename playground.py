"""
This is the official testing file of the libary "HtmlWriter",
You could say it's the libaries playground.
"""

__author__ = 'Lotus'
__version__ = 0.1 # 18-03-2021

import os

try:
    from HtmlWriter import FileStream, Framework
except ImportError as e:
    print('Error while trying to import external libary.')
    print(f'Traceback:\n{e}')

# Creating objects for main classes
fstream = FileStream()
frame = Framework()

# Setting up file to be used
used_file = 'htmldoc.html'
try:
    os.remove(used_file)
except Exception:
    pass

try:
    fstream.new(used_file)
except FileExistsError:
    fstream.open(used_file)

# Setting HTMLDOC Info Attributes
frame.lang('de')
frame.author('lotus')
frame.charset('UTF-8')
frame.title('My Document')

# HTML Code Generation
my_text = 'Wow this is a really long text, I wonder what this sample text is used for?'.split()
print(my_text)
for _ in my_text:
    frame.p(_)

# Creating a Table!
table_headers = ['Name', 'Age']
table_cells = [ 
    'John', '20',
    'Tom', '41',
    'Jonny', '50',
    'Leonardo', '30' ]

frame.table(headers=table_headers, cells=table_cells)

# Saving progress
fstream.finish()