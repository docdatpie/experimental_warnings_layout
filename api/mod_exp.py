"""The module itself is experimental, importing this should be warned."""
import sys

from .warnings import experimental

# This module is experimental and it knows it,
# the module declares itself experimental
experimental(sys.modules[__name__])
# Another approach is to have this "declaration of experimental" done
# by who `import` this module (__init__, for instance).

def run(*args, **kwargs):
    print("""Run something from the experimental module""")
