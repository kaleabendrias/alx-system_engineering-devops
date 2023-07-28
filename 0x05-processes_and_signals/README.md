# Learning Objectives README

## General

### What is a PID?

PID stands for "Process IDentifier." It is a unique numerical identifier assigned to a process running on a computer system. Processes are instances of executing programs, and the PID allows the system to keep track of and manage them individually.

### What is a process?

A process is a running instance of a program on a computer. It consists of the program's code, data, and system resources necessary for its execution. Each process is isolated and independent, and the operating system manages them to ensure proper execution and resource allocation.

### How to find a process' PID?

To find a process's PID on a Unix-like system, you can use the `ps` command. The following command displays information about all running processes:

```bash
ps -e
```

To find the PID of a specific process (e.g., "example_process"), you can use `pgrep`:

```bash
pgrep example_process
```

### How to kill a process?

To terminate a process on a Unix-like system, you can use the `kill` command along with the process's PID. The basic syntax to kill a process with PID is:

```bash
kill PID
```

For example, to terminate a process with PID 12345:

```bash
kill 12345
```

### What is a signal?

A signal is a software interrupt delivered to a process to communicate a particular event or request. Signals can be used for various purposes, such as terminating a process, pausing it, or prompting it to perform a specific action.

### What are the 2 signals that cannot be ignored?

The two signals that cannot be ignored are:

1. SIGKILL (signal number 9): This signal forces a process to terminate immediately and cannot be caught or ignored by the process. It is often used as a last resort to forcefully stop a misbehaving or unresponsive process.

2. SIGSTOP (signal number 19 or 17): This signal pauses a process temporarily. Similar to SIGKILL, it cannot be caught or ignored by the process. The process will remain in a stopped state until it receives a SIGCONT signal to resume execution.

## Copyright - Plagiarism

**Important Notice:** This project emphasizes originality and prohibits any form of plagiarism. As a participant, you are responsible for coming up with your solutions and understanding the concepts involved. Copying and pasting someone else's work or using external sources without proper attribution is strictly forbidden and will result in removal from the program.

## Requirements

### General

- **Allowed editors:** You can use vi, vim, or emacs for editing your files.
- **Operating System:** All files will be interpreted on Ubuntu 20.04 LTS.
- **New Line Endings:** Ensure all your files end with a new line to maintain consistency.
- **README.md File:** Create a README.md file at the root of the project folder. It is mandatory and should contain relevant information about the project.
- **Executable Bash Script Files:** All your Bash script files must be executable. Use the following command to make a script executable:
  ```bash
  chmod +x your_script.sh
  ```
- **Shellcheck:** Your Bash scripts must pass Shellcheck (version 0.7.0 via apt-get) without any error. Shellcheck is a useful tool for checking shell scripts for common errors and style issues.
- **Shebang:** The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`. This shebang specifies the path to the Bash interpreter, ensuring the script runs with the correct environment.
- **Commenting:** The second line of all your Bash scripts should be a comment explaining what the script does. This helps others understand the purpose of the script without having to read through the entire code.

---
By adhering to the learning objectives and project requirements, you will gain a deeper understanding of process management in Unix-like systems and become proficient in writing Bash scripts. Happy coding and learning!
