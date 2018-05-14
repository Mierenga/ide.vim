ide.vim
=======

# What is it?
A vim plugin intended to add features to vim to make development tasks easier
for the author.

# What does it do?
So far, all it does is add keymaps for `make run`, `make kill`, and
`make test` (which need to be defined in a Makefile), along with a global
function called `SwitchProject` which takes an argument for the path of the
project directory which contains the aforementioned Makefile.

# Samples
A python sample Makefile along with a logging.yaml config file that it
would be used with is included in the samples/python folder.
