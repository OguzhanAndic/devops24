# Examination 1 - Understanding SSH and public key authentication

Connect to one of the virtual lab machines through SSH, i.e.

    $ ssh -i deploy_key -l deploy webserver

Study the `.ssh` folder in the home directory of the `deploy` user:

    $ ls -ld ~/.ssh

Look at the contents of the `~/.ssh` directory:

    $ ls -la ~/.ssh/

## QUESTION A

What are the permissions of the `~/.ssh` directory?
The permisssions that can be found with ls -ld is drwx, that means that you have the permission to read, write and execute.

Why are the permissions set in such a way?

## QUESTION B

What does the file `~/.ssh/authorized_keys` contain?cat .ssh/id_ed25519.pub

In the ~/.ssh/authorized_keys you can find the key that is used to remote ssh in to the webserver. 

## QUESTION C

When logged into one of the VMs, how can you connect to the
other VM without a password?

You need to generate a key with ssh-keygen -t ed25519 command in the first server. You can then find this key by using the command cat .ssh/id_ed25519.pub.
You then have to copy that key, open the other servers terminal and nano in to the .ssh/authorized_key and paste in that key.
From then on whener you want to connect to the seconed server you only need to write the other severs name (for me it was deploy@ip adress, or deploy@webserver).


### Hints:

* man ssh-keygen(1)
* ssh-copy-id(1) or use a text editor

## BONUS QUESTION

Can you run a command on a remote host via SSH? How?
