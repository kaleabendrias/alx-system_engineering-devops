# DevOps Project: SSH Configuration Tasks

This README provides an overview of the tasks related to SSH configuration that were completed as part of the DevOps project.

## Task 0: Use a Private Key

### Description:
In this task, a Bash script was created to connect to a server using SSH and a private key (`~/.ssh/school`) with the `ubuntu` user.

### Usage:
```bash
$ ./0-use_a_private_key
```

## Task 1: Create an SSH Key Pair

### Description:
In this task, a Bash script was created to generate an RSA key pair with specific requirements, including a private key named `school`, 4096 bits, and protected by the passphrase `betty`.

### Usage:
```bash
$ ./1-create_ssh_key_pair
```

## Task 2: Client Configuration File

### Description:
This task involved configuring the SSH client on the local machine to use the private key `~/.ssh/school` and refuse authentication using a password.

### Steps:
1. Open the SSH client configuration file (usually located at `/etc/ssh/ssh_config`).
2. Add the following lines to the configuration file:
   ```
   IdentityFile ~/.ssh/school
   PasswordAuthentication no
   ```

## Task 3: Let Me In!

### Description:
In this task, an SSH public key was provided to be added to the server to allow SSH access for the `ubuntu` user.

### Steps:
1. Log in to the server as the `ubuntu` user.
2. Open the `~/.ssh/authorized_keys` file using a text editor.
3. Paste the provided SSH public key (`ssh-rsa AAAAB3...`) at the end of the file.
4. Save and exit the text editor.

## Task 4: Client Configuration File (with Puppet)

### Description:
This advanced task involved using Puppet to configure the SSH client on the local machine to use the private key `~/.ssh/school` and refuse authentication using a password.

### Steps:
1. Puppet manifest (`100-puppet_ssh_config.pp`) was provided to perform the configuration.
2. Execute the Puppet manifest using `sudo puppet apply 100-puppet_ssh_config.pp` to apply the configuration.

**Note:** Ensure that the `stdlib` module is available and configured correctly for Puppet to run successfully.

Feel free to reference this README for a summary of the completed tasks related to SSH configuration in the DevOps project.
