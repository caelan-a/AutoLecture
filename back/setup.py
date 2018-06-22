import sys
from cx_Freeze import setup, Executable

setup(  name = "AutoLecture",
        version = "1.3",
        description = "Download and keep up to date with lectures from Melbourne Uni LMS",
        executables = [Executable("autolecture.py", base= None)])