"""Function/decorators for experimental and deprecation warnings"""

# Pool to keep record of warnings already emitted, don't have to print twice
_pool = set()

def experimental(foo):
    return _warn(foo, 'experimental code, may change in the future')

def deprecated(foo):
    return _warn(foo, 'deprecated code, will disappear in the future')

exp = experimental
dep = deprecated

def _warn(foo, msg=''):
    if callable(foo):
        def wrap(*args, **kwargs):
            if foo not in _pool:
                print(f"WARN: {msg}. \n`->Function: {foo}")
                _pool.add(foo)
            return foo(*args, **kwargs)
        return wrap
    else:
        print(f"WARN: {msg}. \n`->Module: {foo}")
        return foo
