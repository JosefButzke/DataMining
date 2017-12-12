import cx_Freeze
import sys
import matplotlib
import sklearn
import numpy
import pandas

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Cluster.py", base = base)]

cx_Freeze.setup(
    name = "exec",
    options = {"build_exe": {"packages":["tkinter","matplotlib","sklearn","pandas","numpy"]}},
    version = "0.01",
    executables = executables

)