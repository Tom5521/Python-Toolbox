# Tom's Toolbox
A small toolbox for future proyects

You can install this shit with ```pip install Tom-Toolbox```

This library contains a quick way to color the words in the file ansi_colors.py,some useful tools,in tools.py

## Modules
### - Ansi Colors

This is a Python module that provides color codes for text in the terminal. It has three classes, namely c, bg, and bc, each of which has methods to return color codes for different colors.
c Class

The c class has methods for foreground color codes, which means the color of the text.
`black()`

This method returns the color code for black text.
`red()`

This method returns the color code for red text.
`green()`

This method returns the color code for green text.
`yellow()`

This method returns the color code for yellow text.
`blue()`

This method returns the color code for blue text.
`magenta()`

This method returns the color code for magenta text.
`cyan()`

This method returns the color code for cyan text.
`white()`

This method returns the color code for white text.
#### `bg` Class

The bg class has methods for background color codes, which means the color behind the text.
`black()`

This method returns the color code for a black background.
`red()`

This method returns the color code for a red background.
`green()`

This method returns the color code for a green background.
`yellow()`

This method returns the color code for a yellow background.
`blue()`

This method returns the color code for a blue background.
`magenta()`

This method returns the color code for a magenta background.
`cyan()`

This method returns the color code for a cyan background.
`white()`

This method returns the color code for a white background.
#### `bc` Class

The bc class has methods for bright and colored text.
`black()`

This method returns the color code for bright and black text.
`red()`

This method returns the color code for bright and red text.
`green()`

This method returns the color code for bright and green text.
`yellow()`

This method returns the color code for bright and yellow text.
`blue()`

This method returns the color code for bright and blue text.
`magenta()`

This method returns the color code for bright and magenta text.
`cyan()`

This method returns the color code for bright and cyan text.
`white()`

This method returns the color code for bright and white text.
#### Example Usage

Here is an example of how to use the color codes in a Python script:
```
from Toolbox.ansi_colors import *

print(c.blue("Hello, World!"))
print(bg.red("Error: File not found"))
print(bc.green("SUCCESS: Operation completed"))

```
This will print "Hello, World!" in blue color, "Error: File not found" with a red background, and "SUCCESS: Operation completed" in bright and green color.

### - Pacman
The documentation would be [here](https://github.com/Tom5521/PY-PackArch) since this is a library within another one.

### - Tools
#### Functions:
##### `sys(command)`

Executes a shell command using the subprocess.run() method. The input parameter command is expected to be a string representing the shell command to be executed.
##### `command_read(command)`

Executes a shell command using the subprocess.run() method and returns the output of the command as a string. The input parameter command is expected to be a string representing the shell command to be executed.
##### `git_clone(link, route="")`

Clones a git repository using the git clone command. The input parameter link is expected to be a string representing the link to the git repository. The input parameter route is optional and expected to be a string representing the path to the directory where the repository will be cloned.
##### `clear()`

Clears the console using the clear command.
##### `wget(link)`

Downloads a file from a URL using the wget command. The input parameter link is expected to be a string representing the URL of the file to be downloaded.
##### `mkfs(format, partition, condition="")`

Creates a file system on a partition using the mkfs command. The input parameters format and partition are expected to be strings representing the format of the file system and the partition to be formatted, respectively. The input parameter condition is optional and expected to be a string representing additional conditions for the mkfs command.
##### `fetches(option)`

Displays system information using various tools depending on the input parameter option. The valid values for option are "neo", "one", and "fresh". If the input parameter option is not one of the valid values, a message will be displayed indicating that no option was selected.
##### `cowsay(text, cow="", condition="")`

Displays a message using an ASCII art of a cow and the cowsay command. The input parameter text is expected to be a string representing the message to be displayed. The input parameter cow is optional and expected to be a string representing the name of the ASCII art to be used. The input parameter condition is optional and expected to be a string representing additional conditions for the cowsay command.
##### `analize_dir(dir = "")`

Displays the content of a directory using various shell commands. The input parameter dir is optional and expected to be a string representing the path to the directory to be analyzed. The os.listdir() method is used to display the content of the directory, the sys("ls -la") command is used to display the content of the directory with details, and the sys("ls -a") command is used to display the content of the directory, including hidden files.
##### `read_file(file)`

Reads the content of a file and returns it as a string. The input parameter file is expected to be a string representing the path to the file to be read.
##### `makepkg(route ="")`

Creates a package using the makepkg command. The input parameter route is optional and expected to be a string representing the path to the directory where the package will be created. The makepkg -si command is used to create and install the package.