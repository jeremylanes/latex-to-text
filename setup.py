from setuptools import setup, find_packages

setup(
    name="latex-to-text",
    version="0.1.0",
    packages=find_packages(include=["bin", "bin.*"]),
    description="Convert LaTeX to text",
    author="arnbod",
    url="https://github.com/jeremylanes/latex-to-text.git",
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
)
