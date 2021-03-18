"""
HtmlWriter is a libary made for efficiently creating HTML documents in Python.
"""

__auhtor__ = 'Lotus'
__version__ = 0.5 # 18-03-2021 | semi-stable

# stdlibs
import os
import datetime

# Non-stdlibs
try:
    from bs4 import BeautifulSoup
except ImportError as e:
    print('Error while trying to import external libary.')
    print(f'Traceback:\n{e}')


def error(txt):
    """ Outputs error with error modified message. """
    print(f'ERROR : [{txt}]')

# logging wrapper | user-side
def htmlog(function):
    def wrapper(*args, **kwargs):
        with open('debug.log', 'a') as f:
            current_time = datetime.datetime.now()
            func_name = function.__name__
            f.write(f'[{current_time}] - {func_name} ran with args: {args} || kw_args: {kwargs}\n')
        return function(*args, **kwargs)
    return wrapper

class Document:
    """ Stores all the attributes for the document. """
    title = ''
    author = ''
    charset = 'UTF-8'
    lang = ''
    content = ''
    bg_color = ''

doc = Document()

def append_content(txt):
    """ appends content @Document CLS @attribute content. """
    doc.content += txt + '\n'

def insert_tag(_list):
    """ inserts content tag @body_pos-1. """
    content_tags = ['{content}', 
                    '  {content}', 
                    '    {content}', 
                    '      {content}'] 

    top = 8
    body_tags = {f'{" " * (f - 2)}</body>': f for f in range(2, top + 2, 2)}
    for tag in content_tags: 
        try:
            _list.index(tag)
            return _list
        except ValueError:
            continue

    for tag in body_tags.keys():
        try:
            body_index = _list.index(tag)
            c_spaces = ' '*body_tags[tag]
            return _list[:body_index] + [c_spaces + '{content}'] + _list[body_index:]
        except ValueError:
            continue
    
    # if function reaches this point, exit, critical error, no body tag!
    error('Couldnt find body tag : Critical Error.')
    exit()


class FileStream:
    """ Manages file I/O. """
    def __init__(self):
        # @param file, file used for instance of fstream
        self.c_file = ''
        self.file_str = ''
        self.file_opened = False

    def get_content(self, file_name) -> str:
        """ Gets file content of given file @param self.file """
        with open(file_name, 'r') as f:
            file_content = f.read()
        
        return file_content

    def new(self, file_name):
        """ needs to be called @ start | sets file to be used. """
        # checking if file is already existent
        if os.path.isfile(file_name):
            raise FileExistsError

        # creating initial file
        with open(file_name, 'w') as f:
            pass

        # trying to retrive sekeleton
        try:
            skeleton_str = self.get_content('skeleton.html')
        except FileNotFoundError as e: 
            error('Critical! Couldnt find mandatory skeleton file.')
            exit()
        # NOTE -> Content tag should already be contained in skeleton.html

        # Saving skeleton.html to self.c_file
        self.c_file = file_name
        with open(self.c_file, 'w') as f:
            f.write(skeleton_str)

        # Re-defining class attributes
        self.file_str = skeleton_str

    def open(self, file_name):
        """ opens a already existing file & inserts content tag. """
        # check if given file [@param] exists
        if not os.path.isfile(file_name):
            error(f"File [{file_name}] couldn't be found in current working directory.")
            exit()

        # insert content tag into local src
        with open(file_name, 'r') as f:
            file_content = f.read().splitlines()

        new_list = insert_tag(file_content)
        with open('out.txt', 'w') as f:
            for line in new_list:
                f.write(line + '\n')

        # Re-defining class attributes
        self.c_file = file_name

        for line in new_list:
            self.file_str += line + '\n'

        self.file_opened = True
    
    def finish(self):
        """ This method finishes the given document, removes {content} tag. """
        with open(self.c_file, 'w') as f:
                # checking tag availability
                if self.file_opened:
                    content_instance = self.file_str.format(content = doc.content)
                else:
                    content_instance = self.file_str.format(
                                            lang = doc.lang,
                                            title = doc.title,
                                            char = doc.charset,
                                            author = doc.author,
                                            content = doc.content, 
                                            bg_color = doc.bg_color )
        
        soup = BeautifulSoup(content_instance, 'html.parser')
        with open(self.c_file, 'w') as f:
            f.write(soup.prettify())


fstream = FileStream()

class Framework:
    """ The Framework class consists of
    all the mandatory methods for creating a htmldoc. """
    def __init__(self):
        self.file_string = ''
    
    #=========FileInfoModification=========#
    def lang(self, language):
        """ sets lang of htmldoc. """
        doc.lang = language
    
    def author(self, author):
        """ sets author of htmldoc. """
        doc.author = author
    
    def title(self, title):
        """ sets title of htmldoc. """
        doc.title = title

    def charset(self, charset):
        """ sets charset of htmldoc. """
        doc.charset = charset
    #======================================#
    

    #=========FileModification=============
    def background(self, color):
        """ changes background color of current htmldoc. """
        doc.bg_color = color

    def paragraph(self, txt, color='black'):
        """ adds paragraph to html src. """
        txt = f'<p style="color: {color}>{txt}</p>'
        append_content(txt)

    def p(self, txt, color='black'):
        """ adds paragraph to html src. [method-alt-version: paragraph] """
        txt = f'<p style="color: {color}">{txt}</p>'
        append_content(txt)

    def header(self, txt, size='1', color='black'):
        """ adds header to html src. """
        txt = f'<h {size} style="color: {color}">{txt}</h {size}>'
        append_content(txt)
    
    def h(self, txt, size='1', color='black'):
        """ adds header to html src. [method-alt-version: header]"""
        txt = f'<h {size} style="color: {color}">{txt}</h {size}>'
        append_content(txt)

    def code(self, txt, color='black'):
        """ adds code element to html src. """
        txt = f'<code style="color: {color}">{txt}</code>'
        append_content(txt)
    
    def c(self, txt, color='black'):
        """ adds code element to html src. [method-alt-version: code]"""
        txt = f'<code style="color: {color}">{txt}</code>'
        append_content(txt)
    
    def table(self, headers: list, cells, width = 20):
        """ adds table element to html src. """
        tab = '  ' # (HTML INDENT)
        cell_len = len(headers)

        # Arranging table headers
        tmp_str = tab + '<tr>\n'
        for header in headers:
            tmp_str += tab*2 + f'<th>{header}</th>\n'
        tmp_str += tab + '</tr>\n'
        
        # Arranging table cells
        if not len(cells) % cell_len == 0:
            error(f'Given cell count exceed header length limit, {len(cells)} not div by {cell_len}.')
            exit()

        index_count = 0
        rList = []
        for item in cells:
            try:
                rList.append(list(cells[index_count-cell_len:index_count]))
            except IndexError:
                rList.append(list(cells[index_count-cell_len:len(cells)-1]))
            index_count += cell_len
        
        # Cleaning up (Empty []) list with table cell data
        while [] in rList:
            rList.remove([])
        
        # Adding table data cells to temp str
        for __list__ in rList:
            tmp_str += tab + '<tr>\n'
            for item in __list__:
                tmp_str += tab*2 + f'<td>{item}</td>\n'
            tmp_str += tab + '</tr>\n'

        full_table = f'<table style="width: {width}%">\n{tmp_str}</table>'
        append_content(full_table)
    #======================================
    

    
