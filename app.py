"""Use 'api'"""

import api

from api import mod_stable
mod_stable.run()

from api import mod_exp
mod_exp.run()

from api import mod_dev
mod_dev.run()
mod_dev.run_exp()
mod_dev.run_exp_old()

print("Running again doesn't print the warnings again.")
mod_dev.run_exp_old()
