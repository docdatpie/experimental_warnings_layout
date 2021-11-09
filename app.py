"""Use 'api'"""

import api

print("## Load stable module")
from api import mod_stable
mod_stable.run()
print()

print("## Load experimental module")
from api import mod_exp
mod_exp.run()
print()

print("## Load stable module, with exp/dep features")
from api import mod_dev
mod_dev.run()
mod_dev.run_exp()
mod_dev.run_exp_old()
print()

print("## ...running again doesn't print the warnings again")
mod_dev.run_exp_old()
