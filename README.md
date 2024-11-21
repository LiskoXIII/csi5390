# csi5390

Setup
-----

1. Create a venv using `py -3.XX -m venv .ve` where XX is the highest version available 3.12+ prefered.
2. Activate the venv:
    * Windows CMD: `.\.ve\Scripts\activate.bat`
    * Windows PS: `.\.ve\Scripts\Activate.ps1`
    * Linux: `source ./.ve/bin/activate`
3. Install requirements using `python -m pip install --upgrade -r ./requirements.txt`

How-To
------

* To use Designer call it using `pyside6-designer`.
* To create the Python code from the ui file use `pyside6-uic -o [output_file.py] [input_file.ui]`.
* To run app do `python adps.py`.