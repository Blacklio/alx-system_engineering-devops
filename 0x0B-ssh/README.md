# 0x0B. SSH
 
## Background Context

Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using ssh. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of a previous project shared in your intranet profile.

You can access your server information in the my servers section of the intranet, each line with contains the IP and username you should use to connect via ssh.

## Resources

Read or watch:

    What is a (physical) server - text
    What is a (physical) server - video
    SSH essentials
    SSH Config File
    Public Key Authentication for SSH
    How Secure Shell Works
    SSH Crash Course (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)

For reference:

    Understanding the SSH Encryption and Connection Process
    Secure Shell Wiki
    IETF RFC 4251 (Description of the SSH Protocol)
    Internet Engineering Task Force
    Request for Comments

man or help:

    ssh
    ssh-keygen
    env

0. Use a private key
mandatory

Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

Requirements:

    Only use ssh single-character flags
    You cannot use -l
    You do not need to handle the case of a private key protected by a passphrase


1. Create an SSH key pair
mandatory

Write a Bash script that creates an RSA key pair.

Requirements:

    Name of the created private key must be school
    Number of bits in the created key to be created 4096
    The created key must be protected by the passphrase betty



2. Client configuration file
mandatory

Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:

    Your SSH client configuration must be configured to use the private key ~/.ssh/school
    Your SSH client configuration must be configured to refuse to authenticate using a password



3. Let me in!
mandatory

Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key below to your server so that we can connect using the ubuntu user.



4. Client configuration file (w/ Puppet)
#advanced

Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.

Requirements:

    Your SSH client configuration must be configured to use the private key ~/.ssh/school
    Your SSH client configuration must be configured to refuse to authenticate using a password
