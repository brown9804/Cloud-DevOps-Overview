# Securely Accessing Your System

----------------------
Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


March, 2022

----------------------

### _Connect to the server_:

`ssh <user_name>@<IPadress>`

## Generating and Exchanging SSH Keys for Secure Access
Understand how to create secure keys for remote access, how to exchange them, and where to store them on each system involved in the chain.

### _Create the Key on Server 1_:
1. In your terminal, log in to Server 1: <br/>
`ssh cloud_user@&lt;SERVER1_PUBLIC_IP&gt;`
2. List the contents of the current directory: <br/>
`ls -la`
3. Change to the .ssh directory: <br/>
`cd .ssh`
4. List the contents of the .ssh directory: <br/>
`ls -la`
5. Generate a key for Server 1: <br/>
`ssh-keygen`
6. Press `Enter` at the next three prompts.
7. List the contents of the .ssh directory again: <br/>
`ls -la`
8. List the contents of the id_rsa.pub file: <br/>
`cat id_rsa.pub`
9. Copy the output of this command to your clipboard.

### _Create the Key on Server 2_:
1. Log in to Server 2: <br/>
`ssh cloud_user@&lt;SERVER2_PUBLIC_IP&gt;`
2. Change to the .ssh directory.
3. List the contents of the .ssh directory: <br/>
`ls -la`
4. Install the nano text editor:
`sudo yum install nano`
5. Enter your password at the prompt.
6. Open the authorized_keys file in nano:
`nano authorized_keys`
7. Add the key we just generated to the file.
8. Press `Ctrl + X`.
9. Press `Y` then Enter to save the changes.

### _Exchange the SSH Keys between Server 1 and Server 2_:
1. In your Server 2 terminal window, create a new key: <br/>
`ssh-keygen`
2. Press Enter for the next three prompts.
3. List the contents of the current directory: <br/>
`ls -la`
4. List the contents of the id_rsa.pub file: 
`cat id_rsa.pub`
5. Copy the output of this command to your clipboard.
6. Type `exit` to log out of Server 2.
7. Install nano: <br/>
`sudo yum install nano`
8. Type `y` to continue.
9. List the contents of the current directory:
`ls -la`
10. Open the authorized_keys file in nano:
`nano authorized_keys`
11. Add the key we just generated to the file.
12. Press `Ctrl + X`.
13. Press `Y` then Enter to save the changes.

### _Test the Configuration_:
1. Attempt to log in to Server 2 from Server 1 without a password:
`ssh cloud_user@&lt;SERVER2PUBLIC_IP&gt;`
2. Attempt to log in to Server 1 from Server 2 without a password:
`ssh cloud_user@&lt;SERVER1PUBLIC_IP&gt;`

## Create and Use an SSH Tunnel for Network Traffic:

### _Generating ssh key_:
`ssh-keygen` <br/>
Enter the following parameters 

### _Copying the key_:
`ssh-copy-id <user_name>@<IPadress>`

### _Login the key_:
`ssh <user_name>@<IPadress>`

### _Creating the tunnel_:
`ssh -f <user_name>@<IPadress> -L port:<IPadress> -N`

### _Testing_:
`curl localhost:2000` <br/>
Output: <br/>
`Webpage worked`

### References

https://learn.acloud.guru/course/cad92c58-0fd2-4657-98f7-79268b4ff2db/dashboard
