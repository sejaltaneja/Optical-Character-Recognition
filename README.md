
OPTICAL CHARACTER RECOGNITION WITH PYTESSERACT
CASE: DRIVING LICENSE
==============================================

Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and "read" the text embedded in images.

It is useful as a stand-alone invocation script to tesseract, as it can read all image types supported by the Python Imaging Library, including jpeg, png, gif, bmp, tiff, and others, whereas tesseract-ocr by default only supports tiff and bmp. Additionally, if used as a script, Python-tesseract will print the recognized text instead of writing it to a file.

TABLE OF CONTENTS:
==================

-Installation for Windows
-Input
-Code
-Output

INSTALLATION FOR WINDOWS:
=========================

-Step 1: Installing Python

	-Install Python Version 3.6.2 from this link: https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html
	-Add it to Path in the Environment Variables: C:\Users\User name\AppData\Local\Programs\Python\Python36
	-(Additional) to test if it's added, go to your command prompt and run the command "python" in your default directory C:\Users\User name>

-Step 2: Installing Pytesseract via pip

	-Add pip to Path in the Environment Variables: ;C:\Users\User name\AppData\Local\Programs\Python\Python36\Scripts
	-Run this command on command prompt: python -m pip install pytesseract
	-(Additional) to test if it's installed, go to your python shell and run this command "import pytesseract"

-Step 2 (Alternative): Installing Pytesseract via link

	-Download tesseract from python via this link: https://pypi.python.org/pypi/pytesseract
	-Unzip the file.
	-Go to the directory which contains the unzip file
	-Run this command "python setup.py install"
	-(Additional) to test if it's installed, go to your python shell and run this command "import pytesseract"

INPUT:
======

Input is a black and white image (DL_3.jpg) present in the repository.

CODE:
=====

DL_3.py present in the repository.

OUTPUT:
========

Name :ROSHAN THOMAS
S/D/W of :THOMAS
Address :PARAKKATTU HOUSE CHANDANAKAMPARA PO PAYYAVOOR KANNRU,
Date of Birth : 26/01/1992
Driving License Number : 59/5279/2010





