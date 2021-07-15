<h1 align="center">HTML-Python</h1>
<p align="center">
  <image src="https://img.shields.io/badge/Implementation-Python%203.9-%2300A3E0?style=flat-square">
  <image src="https://img.shields.io/badge/version-0.5-blue">
  <image src="https://img.shields.io/badge/Work%20In%20Progress-No-red">
  <image src="https://img.shields.io/tokei/lines/github/xyLotus/HTMLPy?label=Total%20lines&style=flat-square">
</p>
<p align="center">HTML-Python is a libary used for writing HTML in Python!</p>
<p align="center">You can integrate it into your code & algorithms to write HTML the faster and easier way.</p>

## Usage - Functions
### Program Flow Control Commands
| Command       | Arguments         | Purpose                                                   |
| ------------- | ----------------- | --------------------------------------------------------- |
| `new`         | *file_name*       | Creates new HTML document with given name                 |
| `open`        | *file_name*       | Opens given HTML document and creates {content} tag       |

### Document Information Editing Commands
| Command         | Arguments           | Purpose                                                  |
| --------------- | ------------------- | -------------------------------------------------------- |
| `lang`          | *New_Language*      | Changes document language to given lang                  |
| `title`         | *New_Title*         | Changes the title to the given title in the document     |
| `charset`       | *New_Charset*       | Changes the charset to the given charset in the document |
| `author`        | *New_Author*        | Changes the author to the given author in the document   |

### Document Editing Commands
| Command       | Arguments         | Purpose                                                |
| ------------- | ----------------- | ------------------------------------------------------ |
| `paragraph, p`| *Text*            | Creating a paragraph with a given text                 |
| `header, h`   | *Size, Text*      | Creating a header with the given text and size         |
| `table`       | *headers, cells*  | Creating a table with the given headers and cells      |
| `code, c`     | *Code_Text*       | Creating a code tag element with the given text        |
| `background ` | *Background_Color*| Changes the doc's background to the given bg color     |
| `finish`      |                   | Finalizes the document and removes the {document} tag  |

## Note
You can also use this kind of program in a commandline interface environment, which is also made by myself, it's name is "DocumentPy". 
