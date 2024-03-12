# System Service Management, Runlevels and Boot Targets

----------------------
Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


March, 2022

----------------------

This is a summary based on [References](#references)

### _Connect to the server_:

`ssh <user_name>@<IPadress>`

## Configuring a Default Boot Target:
The LPIC-1 exam expects the candidate to know how to change a default target for a Linux computer using systemd. This exercise will assist you in your practice of determining what the default target is, and changing it to a new one.

### _Check the Default Target_:
The current default target is set to multi-user.target. Use the appropriate command to verify this: <br/>
`systemctl get-default` 

### _Change the Default Target_:
The administrator will need to change the default target so that the computer boots into a graphical desktop: <br/>
`sudo systemctl set-default graphical.target`

### _Check the Default Target again_: 
Now verify that the system is set for a graphical boot: <br/>
`systemctl get-default`

## Scheduling a Systemd Service Job With Timer Units:
During the time that our development team has spent working on the new Web-based API for our organization, there have been several instances of mistaken keystrokes or processes that have necessitated the restoration of the site directory from backup. <br/>
We have been asked to run periodic backups of the website directory and, given that the development environment does not have access to the backup network, we have decided to write a custom service that will do so.  <br/>
Previously we wrote systemd unit files to back up the site and have been provided a file called web-backup.sh in our /root directory. Using that file and the associated web-backup.service, we will create a systemd timer unit file that will control the schedule of our service.  <br/>
After we have all three components ready, we'll stage the files in their appropriate locations and start the service for our team and turn it back over for their use.  <br/>

### _Sign in root_:
`[user@$host ~]$ sudo su -`
When prompted, enter the provided lab credentials to finish logging in.

Considerations:
Part of this job is already done. In a previous lab (lab0), we wrote the systemd unit file, web-backup.service in the /root directory, which we will use alongside the web-backup.sh file that the Dev team gave us. To use it, we need to make sure we are in /root and that the file is there.

### _Checking path_:
`[root@$host ~]# pwd` <br/>

### _Checking content_:
`[root@$host ~]# ls`
Output: <br/>
```
web-backup.sh   web-backup.service
```

### _Create a Timer Unit File_:
1. With our items sourced, we are ready to create the timer unit file. To do so, use the vi command along with web-backup.timer:
`[root@$host ~]# vi web-backup.timer` <br/>
2. Fill out the information as follows:
```
[Unit]
Description=Fire off the backup

[Timer]
OnCalendar=*-*-* 23:00:00
Persistent=true
Unit=web-backup.service

[Install]
WantedBy=multi-user.target
```

Note that 23:00:00 can be set to anything. We're just picking 11:00 PM here as an example. <br/>
When the file is correct, remember to write and quit properly from vi using the Esc key, : (the colon), then w, then q.

### _Putting Files Where They Belong_:
1. With everything ready, we now need to make sure our files are in the correct locations. The shell script needs to be copied into /usr/local/sbin with the cp command: <br/>
`[root@$host ~]# cp web-backup.sh /usr/local/sbin/`
2. Then, using the cp command again, copy both the service and timer files into /etc/systemd/: <br/>
`[root@$host ~]# cp web-backup.{service,timer} /etc/systemd/system/`

### _Tell systemd to Run The Files_:
1. With our files in place, we need to reload the systemd daemon so that it can calculate the service dependencies: <br/>
`[root@$host ~]# systemctl daemon-reload`
2. Now enable the services to run at boot:  <br/>
```
[root@$host ~]# systemctl enable web-backup.service
    
[root@$host ~]# systemctl enable web-backup.timer
```
3. Set the permissions for the file to be executable. <br/>
`[root@$host ~]# chmod +x /usr/local/sbin/web-backup.sh`
4. Once the symlinks are created, go ahead and start the services manually:  <br/>
`[root@$host ~]# systemctl start web-backup.timer web-backup.service`
5. Then check on the statuses of both the timer and the service:  <br/>
```
[root@$host ~]# systemctl status web-backup.timer
 
[root@$host ~]# systemctl status web-backup.service
```
They both show as running, meaning this server is ready to go back to the Dev team.

## Working with System Service Log Files Using the Journal Control:
This is to understand how to use the built-in journalctl utility to view and troubleshoot system services.

### _Check the Web Server Configuration File_:
1. Change to the root account: <br/>
`sudo su -`
2. Check the status of the web service: <br/>
`systemctl status httpd.service`
3.Attempt to start the web service: <br/>
`systemctl start httpd.service`
4. After the service fails to start, check the journal: <br/>
`journalctl -u httpd.service`
5. Check the directory where the httpd configuration file should be: <br/>
`ls /etc/httpd/conf`
6. Restore the original httpd configuration file: <br/>
`mv /etc/httpd/conf/httpd.conf.bkup /etc/httpd/conf/httpd.conf`
7. Restart the service: <br/>
`systemctl restart httpd.service`

### _Verify That the Web Server Service Is Running_:
1. Check the status of the service: <br/>
`systemctl status httpd.service`
2. Navigate to the local web page: <br/>
`elinks http://localhost`

### References

https://learn.acloud.guru/course/cad92c58-0fd2-4657-98f7-79268b4ff2db/dashboard
