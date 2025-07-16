# Working with Users and Permissions

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


Last updated: 2025-07-11

----------------------

This is a summary based on [References](#references)

## _Connect to the server_:

`ssh <user_name>@<IPadress>`

## _Become root_:
`sudo -i` <br/>
Enter the cloud_user password at the prompt.

## _Add the Users to the Server_:
```
useradd tstark 
useradd cdanvers
useradd dprince
```

## _Create the new group_:
`groupadd superhero` <br/>
Set wheel Group as the the tstark Account's Primary Group. The usermod command will change which group a user is in. Change tstark:
`usermod -g wheel tstark` <br/>
Make sure it worked: <br/>
`id tstark` <br/>
The command's output should show his primary group is now wheel.

## _Supplementary Group on All Three Users_:
Run the usermod command for each user:
```
usermod -aG superhero tstark
usermod -aG superhero dprince
usermod -aG superhero cdanvers
```

Check with any of the users to make sure it worked: <br/>
`id <USERNAME>`

## _Lock a specific Account_:
`usermod -L dprince`

## _Create New Users_:
Create a gfreeman user on the system: <br/>
`sudo useradd -m gfreeman`

Create an avance user, and assign it to the wheel supplemental group: <br/>
`sudo useradd -G wheel -m avance`

Set the password for both accounts to LASudo321:
```
sudo passwd gfreeman
sudo passwd avance
```

## _Verify the /etc/sudoers File and Test Access_:

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

## _Set Up the Web Administrator_:
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

## _Enable SSH to Connect Without a Password from the dev User on server1 to the dev User on server2_:
1. Generate an SSH key: <br/>
`[dev@server1]$ ssh-keygen` 
2. Press Enter three times to accept the defaults.
3. Then copy it over to the private IP of the other server: <br/>
`[dev@server1]$ ssh-copy-id <server2_PRIVATE_IP>`
4. Now if we try to log into server2 without a password, it should work. Try it: <br/>
`[dev@server1]$ ssh <server2_PRIVATE_IP>`
5. Log out to get back to server1: <br/>
`[dev@server2]$ logout`

## _Copy All tar Files from /home/dev/ on server1 to /home/dev/ on server2_:
1. Copy the files: <br/>
`[dev@server1]$ scp *.gz <server2_PRIVATE_IP>:~/`
2. Connect to server2 again: <br/>
`[dev@server1]$ ssh <server2_PRIVATE_IP>`
3. Make sure they're there: <br/>
`[dev@server2]$ ll` <br/>
It should show the two files.

## _Extract the Files, Making Sure the Output is Redirected_:
1. Extract the files: <br/>
```
[dev@server2]$ tar -xvf deploy_content.tar.gz >> tar-output.log
[dev@server2]$ tar -xvf deploy_script.tar.gz >> tar-output.log
```
2.Take a look at what's in the directory now: <br/>
`ll` <br/>
We'll see the new files and their permissions.

## _Set the Umask So New Files Are Only Readable and Writeable by the Owner_:
1. We need to make new files with 0600 (`-rw-------`) permissions. Since the default is 0666, and we want it to be 0600, run the following: <br/>
`[dev@server2]$ umask 0066`

## _Verify the /home/dev/deploy.sh Script Is Executable and Run It_:
1. Check permissions on deploy.sh: <br/>
`[dev@server2]$ ls -l deploy.sh` 
2. Make the script executable: <br/>
`[dev@server2]$ chmod +x deploy.sh` 
3. Run it: <br/>
`[dev@server2]$ ./deploy.sh`

## References

https://learn.acloud.guru/course/cad92c58-0fd2-4657-98f7-79268b4ff2db/dashboard

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1192-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-16</p>
</div>
<!-- END BADGE -->
