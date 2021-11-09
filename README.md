# experimental_warnings_layout
Minimal layout for warning-decorators in python library

After a discussion on warning users (of PyVO library) about experimental
features in the library, where the use of decorators would be the way
to do it, remained doing it because...why not.

The code is simple: a couple of decorators/functions to warn the user
of some experimentall/deprecated code.
There is a particular _if_ to handle modules, if a whole module happen
to be "experimental"; it makes sense to me to warn when the module is loaded.

The `app.py` module has a workflow of some app using `api`.
