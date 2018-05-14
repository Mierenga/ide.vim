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

# How do you use it?
- Clone this repo in your `~/.vim/plugin` folder
- Create a project that contains a Makefile with following rules:
    - `run`
    - `kill`
    - `test` (optional)
- Open vim and run `:Switch Project ~/path/to/your/project` in normal mode
- Hit enter
- Hit `F1` to run `make run`
- Hit `F4` to run `make kill`
- Hit `F2` to run `make test`

# How do configure the keymap?
The keymap configuration is stored in `keys.config`. This file should be
edited to match the user's preferences.

# Where is all the output?
Since you are still inside vim when you run the commands, any output to stdout,
etc., won't be visible.

The plugin is designed to work with projects that support redirecting output
to a file. This allows you to view the logs and other output in a separate
tmux pane (or other shell paneling system).

For example, the `samples/python` folder contains a sample python app that
uses python logging handlers to output logs to different files. These 
files are then viewable in other panes using commands like
`make tail-console`, `make tail-debug`, `make tail-info`, etc, which simply
run `tail -f` on the desired log.

The `make test` command from the python sample redirects its output to 
a file that is viewable with `make tail-test`.

# Samples
A python sample Makefile along with a logging.yaml config file that it
would be used with is included in the `samples/python` folder.
