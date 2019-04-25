
Latex to text (help to translation)
===================================

Let's translate
---------------

Do you need to translate your work in LaTeX into a foreign language? Don't have the time or skills to do it? Why not let a computer do it for you?

Machine translation has made huge progress and the text produced is quite good.

Issue with maths
----------------

However automatic translators don't like mathematics and LaTeX file. We provide here a tool to hide mathematics to the machine. 


It works!
---------

These tools have been used to translate the book "Python au lycée" to "Python in high school", more than 200 pages, in 15 workdays. See [GitHub Exo7](https://github.com/exo7math).



Requirements
------------

* Your original LaTeX file,

* a Python3 installation and all the Python files you will find in the 'bin/' directory, 

* and a translator like [DeepL Translator](https://www.deepl.com/translator) or [Google Translate](https://translate.google.com/).


Operations
----------

* Use 'python3 latextotext.py toto.tex' to transform a LaTeX file to a text file 'toto.txt'. You will get an additionnal dictionnary 'toto.dic'.

* Don't panic if you see lots of tags '€1234€', they replace maths and LaTeX commands!  

* Use automatic translation on the text file, I recommend [DeepL Translator](https://www.deepl.com/translator), save the file in your target langage as 'new_toto.txt'

* Recover your LaTeX file with 'python3 texttolatex.py new_toto.txt toto.dic', you will get a
file 'new_toto.tex' in your target langage with your original maths.

* You certainly need to check and correct the translation.


Example
-------

1. Start from a file 'maths.tex' written in French:
	...
	Soient $f$ et $g$ deux fonctions continues de $\mathbf{R}$ vers $\mathbf{C}$.
	...


2. Execute 'python3 latextotext.py maths.tex'.

* You will get a file 'maths.txt':
	...
	Soient €0€ et €1€ deux fonctions continues de €2€ vers €3€.
	...

3. And a file 'maths.dic':
	0: $f$
	1: $g$
	2: $\mathbf{R}$
	3: $\mathbf{C}$

4. Translate the file 'maths.txt' to English using DeepL and name the translation 'new_math.txt':
	...
	Let be €0€ and €1€ two continuous functions from €2€ to €3€.
	...

5. Execute 'python3 texttolatex.py new_maths.txt maths.dic' to get a file 'new_maths.tex':
	...
	Let be $f$ and $g$ two continuous functions from $\mathbf{R}$ to $\mathbf{C}$.
	...

6. Adjust the translation by hand:
	...
	Let $f$ and $g$ be two continuous functions from $\mathbf{R}$ to $\mathbf{C}$.
	...