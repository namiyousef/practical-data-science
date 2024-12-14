# Creating Rich Documentation With Sphinx

`sphinx` is a python package that allows you to generate rich documentation automatically from your docstrings. It is relatively simple to set up, but it can be a bit difficult to customise it.

Here are a few tips for creating rich documentation very easily.

## Quickstart
Firstly, we create a basic documentation by following the sphinx guidelines. In summary:
- Create venv and install package dependencies (e.g. either `pip install -r requirements.txt` or `pip install -e .`)
- Run `pip install sphinx`
- Create a docs folder, e.g. `mkdir docs` and `cd` into it
- Run `sphinx-quickstart`. Say yes to saving build and source files separately
- Edit the `conf.py` file that is created. At the bottom, make sure to add the following line to enable auto doc generation from docstrings:
```python

extensions = ["sphinx.ext.autodoc"]
```
- Edit the path to the module at the top of `conf.py`
```python

import os
import sys
sys.path.insert(0, os.path.abspath("REL_PATH_TO_MODULE"))

```
- `cd` into the docs folders and run `make html`. This will create your raw docs. You can verify this by clicking the `index.html` file within `build/` which should take you to the index page of your docs
- Autogenerate documentation from your docstrings by running `sphinx-apidoc -o $LOCATION_OF_SOURCE_FOLDER $PATH_TO_MODULE`
- You should now have autodocs based on your docstrings!

From this point onwards, you can play with the generate `.rst` files to modify/move things around.

## Parsing `numpy` or `google` docstrings

By default, `sphinx` only recognizes the sphinx docstring format. In order to recognize `numpy` and `google`, you need to add the `sphinx.ext.napolean` extension to your extensions in `conf.py`
```python
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
```

## Parsing `typing` style of annotations to reduce clutter in docstrings

You may wish to use Python's `typing` module to annotate your functions. For instance, consider the following function (documented with sphinx formatting):
```python
def test(test_param, test_param_optional=None):
    """test function
    
    :param test_param: required param
    :type test_param: bool
    :param test_param_optional: optional string param, defaults to None
    :type test_param_optional: str, optional
    
    :return: answer to life
    :rtype: int

    """
    return 42
```
Annotating using the `typing` module allows you to define the types more concisely:
```python

def test(test_param: bool, test_param_optional: str = None) -> int:
    """test function
    
    :param test_param: required param
    :param test_param_optional: optional string param, defaults to None
    
    :return: answer to life
    """
    return 42
```

However, by default the types will not get recognized by sphinx in the docs. To achieve this, you must provide the `sphinx_autodoc_typehints` extension as well as the `sphinx.ext.napoleon` extension.

- Install the typehints extension, `pip install sphinx_autodoc_typehints`
- Add the extensions to `conf.py`
```python
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx_autodoc_typehints"]  # note, typehints extension should follow the napoleon one
```

## Copy button on code blocks

Adding copy button is a nice addition to your documentation.

- `pip install sphinx_copybutton`
- Add extension to `conf.py`
```python
extensions = ["sphinx.ext.autodoc", "sphinx_copybutton"]
```

## Linking to code

`sphinx.ext.viewcode` or `sphinx.ext.linkcode` extensions

## Adding custom themes

You can change the default docs theme. One of my favorites is `furo`

- `pip install furo`
- Change the theme in `conf.py`
```python
html_theme = 'furo'
```
