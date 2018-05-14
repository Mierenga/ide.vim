
This is a sample python app that demonstrates integration with ide.vim.
The sample uses `pipenv` to manage virtual environments for python. If you
want to set up `pipenv`, do:
    # install pipenv globally for the user
    pip install --user pipenv 
    # create a new virtual environment for a project
    pipenv --python 3.5
    # install package from existing Pipfile
    pipenv install
    # run a command (python) in the virtual environment
    pipenv run python app.py
    # get a shell in the virtual environment
    pipenv shell
    # install a new package (uses the working directory tree's Pipfile)
    pipenv install pyyaml
    







