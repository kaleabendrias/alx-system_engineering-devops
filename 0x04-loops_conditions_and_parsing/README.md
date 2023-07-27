# Bash Scripting Learning Objectives

This project aims to provide you with a comprehensive understanding of Bash scripting by covering the following topics:

1. Creating SSH Keys
2. Advantages of using `#!/usr/bin/env bash` over `#!/bin/bash`
3. Working with loops: `while`, `until`, and `for`
4. Conditional statements: `if`, `else`, `elif`, and `case`
5. Using the `cut` command
6. File and other comparison operators

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- You are not allowed to use `awk`
- Your Bash scripts must pass Shellcheck (version 0.7.0) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script does

### Copyright - Plagiarism

You are required to solve the tasks below independently to meet the learning objectives. Copying and pasting someone else's work is strictly forbidden and will result in removal from the program. You are not allowed to publish any content of this project.

## Shellcheck

Shellcheck is a helpful tool for writing proper Bash scripts. It provides recommendations on syntax and semantics and offers advice on edge cases you might not have considered. All your Bash scripts must pass Shellcheck without any error to earn points for the tasks.

Shellcheck is available on the school's computers. If you wish to use it on your own computer, you can install it following these instructions:

[Link to Shellcheck installation instructions]

## Examples

To illustrate the importance of Shellcheck, here are two examples:

### Not passing Shellcheck:

```bash
#!/usr/bin/env bash
echo "Hello World"
```

### Passing Shellcheck:

```bash
#!/usr/bin/env bash
# This script prints "Hello World"
echo "Hello World"
```

For every feedback, Shellcheck will provide a code that you can use to get more information about the issue. For example, for code SC2034, you can browse [Shellcheck SC2034 page on GitHub](https://github.com/koalaman/shellcheck/wiki/SC2034).

By adhering to the requirements and learning objectives, you will gain a solid foundation in Bash scripting, which will be valuable for your future projects and server management tasks. Remember to always think critically and avoid plagiarism to make the most out of this learning opportunity. Happy scripting!
