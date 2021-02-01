# Onsei Templating
Enhance the speech output your voice application with the use of templates. 

Tutorial about creating a python packages:
- [Github](https://github.com/judy2k/publishing_python_packages_talk)
- [Video](https://www.youtube.com/watch?v=GIF3LaRqgXo)
- [medium](https://medium.com/tech-sauce/this-is-how-i-built-my-first-pip-package-e39de9cb4c08)

## Prerequisites
- Python 3

### Create Virtual Environment
Follow the instruction in der [Docs](https://docs.python.org/3/tutorial/venv.html) and [Blog](https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7):

    $ python -m venv venv
    $ echo 'venv' > .gitignore

### Activate and Deactivate Virtual Environment

    $ source venv/bin/activate

    $ source deactivate

### Select Interpreter (VS Code)

To select a specific environment, use the Command Palette (⇧⌘P).
Type in ```Python: Select Interpreter``` and select ```./venv/bin/python```. [Docs](https://code.visualstudio.com/docs/python/environments)

## Installation

    $ pip install -r requirements.txt

### Freeze the requirements:

    $ pip freeze > requirements.txt
    $ git add requirements.txt

## Build

    $ python setup.py bdist_wheel  

    $ pip install -e . 

## Test

    $ pytest
    $ python test/templating_test.py

## Usage

Install the package via pip:

    $ pip install git+https://github.com/ONSEIGmbH/onsei-templating#egg=templating 

Import the `PromptTemplate` in each script, where speech output is needed.
Set the path to the template file (`.yaml`). Filename can be changed. 
To get the speech output use the se the `render` function as shown below.

    from templating import PromptTemplate

    t = PromptTemplate('template/example.yaml')
    print(t.render('hi')) # Hello World!
    print(t.render('hi_name',name='MyName')) # Hello MyName!