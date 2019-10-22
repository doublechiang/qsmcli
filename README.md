# qsmcli
Q system management command line tool

## supported shell mode and command

### Command line mode
When invoke this command, if there is any argument, then the command executed.

### Shell mode
In Shell mode, if there is no argument is specified, then the shell mode is entered.
The host and username/password is saved in the prompt.

## Command supported
### help/?
Any command with help command involved will print the help message.

### ipmi
This is the command to redirect all of the command to ipmi interface

## Test
To run the unit test command, use 'python3 -m unittest'

## Distribute the package
To generate the package, use 'pyinstaller qsmcli.py' to build the package.
