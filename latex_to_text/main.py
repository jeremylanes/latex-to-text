import argparse
from dataclasses import dataclass

from .constants import tag, close_tag
from .latextotext import LatexToText
from .texttolatex import TextToLatex


@dataclass
class LatexConverter(LatexToText, TextToLatex):
    open_tag: str = tag
    close_tag: str = close_tag

## latex to text
# if __name__ == "__main__":
#     # Arguments
#     parser = argparse.ArgumentParser(
#         description='Conversion a LaTex file to a text file keeping apart commands and maths.')
#     parser.add_argument('inputfile', help='input LaTeX filename')
#     parser.add_argument('outputfile', nargs='?', help='output text filename')
#     parser.add_argument('dicfile', nargs='?', help='output dictionary filename')
#     options = parser.parse_args()
#
#     LatexConverter().convert_latex_to_text(
#         tex_file=options.inputfile,
#         output_file=options.outputfile,
#         dictionary_file=options.dicfile
#     )

## text to latex
# if __name__ == "__main__":
#     # Arguments
#     parser = argparse.ArgumentParser(description='Conversion a text file to a LaTeX gluing back commands and maths.')
#     parser.add_argument('inputfile', help='input text filename')
#     parser.add_argument('dicfile', nargs='?', help='input dictionary filename')
#     parser.add_argument('outputfile', nargs='?', help='output LaTeX filename')
#     options = parser.parse_args()
#
#     LatexConverter().convert_text_to_latex(
#         txt_file=options.inputfile,
#         dictionary_file=options.dicfile,
#         output_file=options.outputfile
#     )
