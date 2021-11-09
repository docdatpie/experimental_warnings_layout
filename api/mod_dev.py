"""Module has stable content and experimental functionalities."""

from . import warnings

def run():
    print("""Run stable code""")

@warnings.exp
def run_exp():
    print("""Run some new, experimental code""")

@warnings.dep
@warnings.exp
def run_exp_old():
    print("""Run deprecated interface, stack w/ experimental because...yes""")
