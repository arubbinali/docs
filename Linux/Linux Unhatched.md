# Linux Unhatched
### 1. Basic Command Syntax

- `ls` → displays a listing of information about files

### 2. Arguments

> Syntax: command [options…] **[arguments…]**

An argument can be used to specify something for the command to act upon.

- `ls Documents` →  the `Documents` directory will be used as an argument to list the contents of that directory

- `aptitude` → takes `moo` as an argument: `aptitude moo` outputs "There are no Easter Eggs in this program."

### 3. Options

> Syntax: command **[options…]** [arguments…]

Options can be used to alter the behavior of a command.

- `-l` (`ls -1`) → `l` stands for "long display", details the output

- `-r` (`ls -r`) → `r` stands for "reverse", prints the results in reverse alphabetical order

- Multiple options can be used at once, either given as separate options as in `-l -r` or combined like `-lr`. The output of all of these examples would be the same:

    - `ls -l -r`
    - `ls -rl`
    - `ls -lr`

- `-v` → `v` stands for verbose

    - `aptitude moo` outputs "There are no Easter Eggs in this program."
    - `aptitude -v moo` outputs "There really are no Easter Eggs in this program."
    - `aptitude -vv moo` outputs "Didn't I already tell you that there are no Easter Eggs in this program?"
    - `aptitude -vvv moo` outputs "Stop it!"

    Multiple options can be denoted separately or combined:

    - `aptitude -v -v moo`
    - `aptitude -vv moo`

### 4. Printing Working Directory

> Syntax: pwd [OPTIONS]

- `pwd` prints the current working directory

### 5. Changing Directories

> Syntax: cd [options] [path]

- `cd` changes directory to the the given path
- `root` is the top level directory and `/` given as an argument refers to it
    
    - e.g. `cd /`, this will change the directoy to the root directory

- Absolute paths

    - Start at the root of the filesystem
    - Path always starts from the root directory (`/`)

- Relative paths

    - Start from your current location
    - Path starts directly from the name of the directory


- Shortcuts

    - `..` → Regardless of current directory, `..` always represents one directory higher relative to the current directory, sometimes referred to as the parent directory
    - `.` → Always represents the current directory
    - `~` → Refers to the home directory of the current user

### 6. Listing Files

> Syntax:  ls [OPTIONS] [FILE]

- By default, when the `ls` command is used with no options or arguments, it will list the files in the current directory