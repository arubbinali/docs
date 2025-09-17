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
- File Types
    
    - `-`rw-r--r-- 1 root   root  18047 Dec 20  2017 alternatives.log       
    - `d`rwxr-x--- 2 root   adm    4096 Dec 20  2017 apache2 

    | Symbol | File Type      | Description                                                   |
    |--------|----------------|---------------------------------------------------------------|
    | d      | directory      | A file used to store other files.                             |
    | -      | regular file   | Includes readable files, images files, binary files, and compressed files. |
    | l      | symbolic link  | Points to another file.                                       |
    | s      | socket         | Allows for communication between processes.                   |
    | p      | pipe           | Allows for communication between processes.                   |
    | b      | block file     | Used to communicate with hardware.                            |
    | c      | character file | Used to communicate with hardware.                            |

- Permissions

    - Permissions indicate how certain users can access a file
    - d`rwxr-xr-x` 2 root   root   4096 Apr 11  2014 upstart

- Hard Link Count

    - Indicates how many hard links point to this file
    - -rw-r----- `1` syslog adm    1346 Oct  2 22:17 auth.log

- User Owner

    - User syslog owns this file, every time a file is created, the ownership is automatically assigned to the user who created it
    - -rw-r----- 1 `syslog` adm     106 Oct  2 19:57 kern.log

- Group Owner

    - Indicates which group owns this file
    - -rw-rw-r-- 1 root   `utmp` 292584 Oct  2 19:57 lastlog

- File Size
    
    - Directories and larger files may be shown in kilobytes since displaying their size in bytes would present a very large number. Therefore, in the case of a directory, it might actually be a multiple of the block size used for the file system. Block size is the size of a series of data stored in the filesystem.
    - -rw-r----- 1 syslog adm   `19573` Oct  2 22:57 syslog

- Timestamp

    - Indicates the time that the file's contents were last modified
    - drwxr-xr-x 2 root   root   4096 `Dec  7  2017` fsck

- Filename

    - The final field contains the name of the file or directory
    - -rw-r--r-- 1 root   root  47816 Dec  7  2017 `bootstrap.log`

- Symbolic Links

    - In the case of symbolic links, a file that points to another file, the link name will be displayed along with an arrow and the pathname of the original file
    - lrwxrwxrwx. 1 root root 22 Nov 6 2012 /etc/grub.conf `->` ../boot/grub/grub.conf

- Sorting

    - By default the output of the ls command is sorted alphabetically by filename. It can sort by other methods as well
    - `-t` (`ls -lt`) → sorts the files by timestamp
    - `-S` (`ls -lS`) → sorts the files by file size
    - `-r` (`ls -lr`) → reverses the order of any type of sort:
        
        - `ls -ltr`/`ls -l -t -r` → the order of timestamps switches from newest-first to oldest-first
        - `ls -lSr`/`ls -l -S -r` → the numbers in file size field switch from descending to ascending
        - Used alone the `-r` option with list the files in reverse alphabetical order 

### 7. Administrative Access

- `su`
    
    - > Syntax: su OPTIONS USERNAME
    - Allows you to temporarily act as a different user. It does this by creating a new shell. The shell is simply a text input console that lets you type in commands
    - By default, if a user account is not specified, the su command will open a new shell as the root user, which provides administrative privileges
    - The command can be used in 3 ways:
        - su -
        - su -l
        - su --login 
    - To logout, use the `exit` command

- `sudo`

    - > Syntax: sudo [OPTIONS] COMMAND
    -  Allows a user to execute a command as another user without creating a new shell. Instead, to execute a command with administrative privileges, use it as an argument to the sudo command. Like the su command, the sudo command assumes by default the root user account should be used to execute commands
    - The `sudo` command can be used to switch to other user accounts as well. To specify a different user account use the `-u` option

### 8. Permissions

- After the file type character, the permissions are displayed. The permissions are broken into three sets of three characters:

    - Owner
        - The first set is for the user who owns the file. If your current account is the user owner of the file, then the first set of the three permissions will apply and the other permissions have no effect.
        - -`rw-`r--r-- 1 sysadmin sysadmin 647 Dec 20  2017 hello.sh
        - The user who owns the file, and who these permissions apply to, can be determined by the user owner field:
        - -rw-r--r-- 1 `sysadmin` sysadmin 647 Dec 20  2017 hello.sh

    - Group
        - The second set is for the group that owns the file. If your current account is not the user owner of the file and you are a member of the group that owns the file, then the group permissions will apply and the other permissions have no effect.
        - -rw-`r--`r-- 1 sysadmin sysadmin 647 Dec 20  2017 hello.sh
        - The group for this file can be determined by the group owner field:
        - -rw-r--r-- 1 sysadmin `sysadmin` 647 Dec 20  2017 hello.sh

    - Other
        - The last set is for everyone else, any one who that first two sets of permissions do not apply to. If you are not the user who owns the file or a member of the group that owns the file, the third set of permissions applies to you.
        - -rw-r--`r--` 1 sysadmin sysadmin 647 Dec 20  2017 hello.sh

- Permission Types

    | Permission | Effects on File                                                                 | Effects on Directory                                                                                  |
    |------------|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
    | read (r) | Allows for file contents to be read or copied.                                   | Without execute permission on the directory, allows for a non-detailed listing of files. With execute permission, `ls -l` can provide a detailed listing. |
    | write (w)| Allows for contents to be modified or overwritten. Allows for files to be added or removed from a directory. | For this permission to work, the directory must also have execute permission.                        |
    | execute (x) | Allows for a file to be run as a process, although script files require read permission, as well. | Allows a user to change to the directory if parent directories have execute permission as well.      |

### 9. Changing File Permissions (The Symbolic Method)

- `chmod`
- > Syntax: `chmod [<SET><ACTION><PERMISSIONS>]... FILE`

1. `SET`
    
    Choose what **set** of permissions is being changed

    | Symbol | Meaning |
    |--------|---------|
    | u      | User: The user who owns the file. |
    | g      | Group: The group who owns the file. |
    | o      | Others: Anyone other than the user owner or member of the group owner. |
    | a      | All: Refers to the user, group and others. |

2. `ACTION`

    Next, specify an **action** symbol

    | Symbol | Meaning |
    |--------|---------|
    | +      | Add the permission, if necessary |
    | =      | Specify the exact permission |
    | -      | Remove the permission, if necessary |

3. `PERMISSIONS`

    Last, specify one or more **permissions** to be acted upon

    | Symbol | Meaning |
    |--------|---------|
    | r      | read    |
    | w      | write   |
    | x      | execute |

4. `FILE`

    Finally, a space and the pathnames for the files to assign those permissions

    
