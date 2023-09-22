# Configuration Management Tasks

This README provides an overview of the tasks related to configuration management using Puppet. Below are the details and examples for each task.

## Task 0: Create a File

### Description:
Using Puppet, create a file in the `/tmp` directory with specific requirements.

### Requirements:
- File path is `/tmp/school`
- File permission is `0744`
- File owner is `www-data`
- File group is `www-data`
- File contains the text "I love Puppet"

### Example:
```bash
$ puppet apply 0-create_a_file.pp
```

## Task 1: Install a Package

### Description:
Using Puppet, install the Flask package from pip3 with specific version requirements.

### Requirements:
- Install Flask
- Version must be `2.1.0`

### Example:
```bash
$ puppet apply 1-install_a_package.pp
```

## Task 2: Execute a Command

### Description:
Using Puppet, create a manifest that kills a process named "killmenow."

### Requirements:
- Must use the `exec` Puppet resource
- Must use `pkill` to terminate the process

### Example:
```bash
$ puppet apply 2-execute_a_command.pp
```

Feel free to reference this README for a summary of the completed configuration management tasks using Puppet in the DevOps project.
