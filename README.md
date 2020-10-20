## Document code with Sphinx

Requirements:
 * Platform: Linux (Debian) and sub-versions (e.g., Ubuntu, Mint, Lubuntu)
 * Clone this repository `git clone https://github.com/sschwindt/docs-with-sphinx.git` to get the example (New API) and template files.

## Setup new project

Create a new folder (e.g., `NewProject`), `cd` into the folder through *Terminal* and type:

```
virtualenv -p python3 <name of virtualenv>
source <name of virtualenv>/bin/activate
```

### Install requirements (Docs dependencies)

The requirements include *mysql*, which requires that  *libffi* is installed. To do so open *Terminal* and type:

```
apt-cache search libffi
sudo apt-get install -y libffi-dev
sudo apt-get install python3-dev default-libmysqlclient-dev
sudo apt-get install python3-dev
```

Then use the *requirements* file from this repository and copy it to the project folder. In *Terminal* type:

```
pip3 install -r requirements.txt
```

Make sure that *rhino* and *Sphinx* are installed:

```
pip3 install -U Sphinx
pip3 install -U rinohtype
```

### Setup docs directory

Create a new `docs` directory and `cd` in the new directory:

```
mkdir docs
cd docs
```

## Start and setup *Sphinx* 

In the new `docs` folder, get start a new *Sphinx* documentation with (follow the instructions during the project setup process):

```
sphinx-quickstart
```

### Setup **`conf.py`**
After setting up the new *Sphinx* project, open (edit) `/docs/source/conf.py`:

* Uncomment/Add the following lines
```
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
sys.setrecursionlimit(1500)

```
* Add the project root folder to the documentation source by modifying the relative directory in `os.path.abspath('.')` to `os.path.abspath('../..')`. Note that this change is based on the assumption that the *Python* project will be located in `/NewProject` (corresponds to the root directory) and that the docs will live in `/NewProject/docs`.
* Add to the `extensions` list: `'rinoh.frontend.sphinx'` 
* Add the following `latex_elements` dictionary ([more *LaTex* options](https://www.sphinx-doc.org/en/master/latex.html)):
```
# inside conf.py
latex_engine = 'xelatex'
latex_elements = {
    'papersize': 'letterpaper'
	'pointsize': '10pt'
    'preamble': '',
    'figure_align': 'htbp',
}
```

### Setup **`index.rst`**

Open (edit) `/docs/source/index.rst` and type (copy-paste):

```
Documentation for the Code
**************************
.. toctree::
   :maxdepth: 2
   :caption: Contents:

NewAPI main
===================
.. automodule:: app
   :members:

NewAPI controller
=====================
.. automodule:: NewAPI.controller
   :members:

NewAPI models
=================
.. automodule:: NewAPI.models
   :members:

NewAPI database
===================
.. automodule:: NewAPI.database
   :members:

NewAPI populate
===================
.. automodule:: NewAPI.populate
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

Alternatively, use the [`/docs/source/index.rst`]() file from this repository.

## Build the docs (*html* and *PDF*)

In *Terminal* `cd` to the `/ROOT/docs` directory and type:

```
make html
sphinx-build -b rinoh source _build/rinoh
```

