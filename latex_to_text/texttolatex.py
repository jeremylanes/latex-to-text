#!/usr/latex_to_text/env python3

# Convert a text file + a dictionary file to a LaTeX file
# Usage : 'python3 texttolatex.py toto.txt'
# or 'python3 texttolatex.py toto.txt toto.dic'
# or 'python3 texttolatex.py toto.txt toto.dic new_toto.tex'
# Output : create a file toto.tex (or new_toto.tex)

import argparse
import re
import os
import yaml
from .constants import *
# from .constants_perso import *  # Personal customization

#--------------------------------------------------
#--------------------------------------------------

def convert_text_to_latex(txt_file, dictionary_file=None, output_file=None):
    """
    Converts a text file and its dictionary file to a LaTeX file.

    :param txt_file: Path to the input text file.
    :param dictionary_file: Path to the input dictionary file (optional).
    :param output_file: Path to the output LaTeX file (optional).
    :return: None
    """
    # Get argument: a txt file
    file_name, _ = os.path.splitext(txt_file)

    # Dictionary file name
    if dictionary_file:
        dic_file = dictionary_file    # Name given by user
    else:
        dic_file = file_name + '.dic'  # If no name add a .dic extension

    # Output file name
    if output_file:
        tex_file = output_file    # Name given by user
    else:
        tex_file = file_name + '.tex'  # If no name add a .tex extension

    # Read file object to string
    with open(txt_file, 'r', encoding='utf-8') as fic_txt:
        text_all = fic_txt.read()

    # Read dictionary
    with open(dic_file, 'r', encoding='utf-8') as fic_dic:
        dictionary = yaml.load(fic_dic, Loader=yaml.BaseLoader)

    # Replacements start now
    text_new = text_all

    # Iterate replacing until nothing remains to be replaced
    # (to deal with nested replacements)
    keep_replacing = True
    k = 0
    while keep_replacing:
        keep_replacing = False
        for i, val in dictionary.items():
            tag_str = tag + str(i) + close_tag
            val = val.replace('\\', '\\\\')  # double \\ for correct write
            (text_new, number_of_subs_made) = re.subn(tag_str, val, text_new, flags=re.MULTILINE | re.DOTALL)
            if number_of_subs_made > 0:
                keep_replacing = True
        k += 1
    # print(f'{k} iteration(s) done.')

        # Write output files
        abs_new_txt_file = os.path.abspath(text_new)

    # Write the result
    with open(tex_file, 'w', encoding='utf-8') as fic_tex:
        fic_tex.write(text_new)

    return abs_new_txt_file

if __name__ == "__main__":
    # Arguments
    parser = argparse.ArgumentParser(description='Conversion a text file to a LaTeX gluing back commands and maths.')
    parser.add_argument('inputfile', help='input text filename')
    parser.add_argument('dicfile', nargs='?', help='input dictionary filename')
    parser.add_argument('outputfile', nargs='?', help='output LaTeX filename')
    options = parser.parse_args()

    convert_text_to_latex(
        txt_file=options.inputfile,
        dictionary_file=options.dicfile,
        output_file=options.outputfile
    )
