# Working with Users and Permissions

----------------------
Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


March, 2022

----------------------

### _Connect to the server_:

`ssh <user_name>@<IPadress>`

### _Become root_:
`sudo -i` <br/>
Enter the cloud_user password at the prompt.

### _Add the Users to the Server_:
```
useradd tstark 
useradd cdanvers
useradd dprince
```

### _Create the new group_:
`groupadd superhero` <br/>
Set wheel Group as the the tstark Account's Primary Group. The usermod command will change which group a user is in. Change tstark:
`usermod -g wheel tstark` <br/>
Make sure it worked: <br/>
`id tstark` <br/>
The command's output should show his primary group is now wheel.

### _Supplementary Group on All Three Users_:
Run the usermod command for each user:
```
usermod -aG superhero tstark
usermod -aG superhero dprince
usermod -aG superhero cdanvers
```

Check with any of the users to make sure it worked: <br/>
`id <USERNAME>`

### _Lock a specific Account_:
`usermod -L dprince`

### _Create New Users_:
Create a gfreeman user on the system: <br/>
`sudo useradd -m gfreeman`

Create an avance user, and assign it to the wheel supplemental group: <br/>
`sudo useradd -G wheel -m avance`

Set the password for both accounts to LASudo321:
```
sudo passwd gfreeman
sudo passwd avance
```

### _Verify the /etc/sudoers File and Test Access_:

1. Verify that the /etc/sudoers file will allow the wheel group access to run all commands with sudo: <br/>
`sudo visudo` <br/>
2. Note that there should not be a comment (#) on this line of the file: <br/>
`%wheel  ALL=(ALL)       ALL` <br/>
3. Switch to the avance account, and use the dash (-) to utilize a login shell: <br/>
`sudo su - avance` <br/>
4. Attempt to read the /etc/shadow file at the console: <br/>
`cat /etc/shadow` <br/>
5. Rerun the command with the sudo command: <br/>
`sudo cat /etc/shadow` <br/>
6. After you have verified avance can read the /etc/shadow file, log out of that account: <br/>
`exit`

### _Set Up the Web Administrator_:
1. Create a new sudoers file in the /etc/sudoers.d directory that will contain a standalone entry for webmasters: <br/>
`sudo visudo -f /etc/sudoers.d/web_admin`
2. Enter in the following at the top of the file: <br/>
`Cmnd_Alias  WEB = /bin/systemctl restart httpd.service, /bin/systemctl reload httpd.service`
3. Add another line in the file for gfreeman to be able to use the sudo command in conjunction with any commands listed in the WEB alias:
`gfreeman ALL=WEB`
4. Save and close the file with `:wq!`.
5. Next, log in to the gfreeman account: <br/>
`sudo su - gfreeman`
6. Attempt to restart the web service: <br/>
`sudo systemctl restart httpd.service`
7. Try to read the new web_admin sudoers file: <br/>
`sudo cat /etc/sudoers.d/web_admin` <br/>
Since the cat command is not listed in the command alias group for WEB, gfreeman cannot use sudo to read this file.

