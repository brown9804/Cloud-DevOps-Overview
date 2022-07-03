# Networking


----------------------
Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


March, 2022

----------------------

### _Connect to the server_:

`ssh <user_name>@<IPadress>`


## Testing DNS Resolution
Understand how to utilize the nmcli utility to configure our DNS resolution.

### _Review Current DNS Configuration_:
1. See if the system can resolve hostnames to IP addresses: <br/>
`host www.google.com`
> Note that the command times out.
2. Check to see what DNS server entries we have in the /etc/resolv.conf file: <br/>
`cat /etc/resolv.conf`
> Note that we do not have any DNS entries listed. 
3. Review our network connections: <br/>
`nmcli con show`
> Our default connection name should be System ens5.
4. Review our DNS IP settings:
`nmcli -f ipv4.dns con show "System ens5"`
> This system obviously does not have any DNS servers configured for use.

### _Configure Your System to Use Your Network's DNS_:
1. Modify the system's default connection to use the network's DNS server <br/>
`sudo nmcli con mod "System ens5" ipv4.dns "10.0.0.2"`
2. Verify the settings using the nmcli command and then checking the /etc/resolv.conf file: <br/>
```
nmcli -f ipv4.dns con show "System ens5"
cat /etc/resolv.conf
```
3. We need to reactivate the system's network connection for the change to take effect: <br/>
`sudo nmcli con up "System ens5"`
4. Verify our settings once more: <br/>
`cat /etc/resolv.conf`
5. Now, attempt to resolve a hostname to an IP address: <br/>
`host www.google.com`
> Our system should be able to resolve an IP address for the domain name.

## Monitoring Network Access:
Understand how use the netcat (nc) utility to generate network traffic between two servers and view that traffic's appearance in a tool called iptraf-ng.

>> *The Scenario*

> During the development of a new Web-based API our team is working on, they have discovered that they are receiving intermittent network disconnects from clients, even when they are local to the network of the server itself.
> We have been provided credentials and access information for two CentOS 7 systems in their environment. They have asked for us to install tools that they can use to monitor network traffic between the two systems. We'll have to install the tools we need and create traffic on port 2525 from server2 to server1. We want to get all network traffic sent to /home/cloud_user/traffic_log.txt.

### _Install Client Utilities_:
1. We've got to install the two packages that the team will use to generate and monitor traffic. Let's use YUM to get it done: <br/>
`[root@server1]# yum install iptraf-ng nc`
2. Repeat this on the other server: <br/>
`[root@server2]# yum install iptraf-ng nc` 

### _Create the Traffic Log File_:
1. On the first server, let's run iptraf-ng.
2. Go under Configure... 
> In the menu, don't forget this isn't a menu we control with a mouse -- it's all keyboard. 
3. Make sure Logging is toggled to On. Set the log file path to: /home/cloud_user/traffic_log.txt. 
4. Then go into IP traffic monitor.
5. In the next menu, select eth0. 
6. Once we press Enter the logging will start.

### _Listen for Traffic_:
1. Let's open a second terminal into server1 and run sudo su right off. 
2. Once we're there, we're going to start netcat listening on post 2525 with this: <br/>
`[root@server1]# nc -l 2525`

### _Send Some Traffic_:
1. Now, let's start talking. Back in the server2 window we've got open, send netcat traffic to server1 with this (where x.x.x.x is the internal IP of server1 that we'll see on the hands-on lab overview page): <br/>
`[root@server2]# nc x.x.x.x 2525`
2. We'll just land at a blinking cursor below the prompt, but we can type a message there and press Enter. Once we do, it will show up back in the window we're listening in on server1. A bunch of messages sent from server2 would look like this: <br/>
`[root@server2]# nc x.x.x.x 2525`
```
test
test
testing
This is a test
````
3. On server1, they would look like this when they arrive: <br/>
`[root@server1]# nc -l 2525`
```
test
test
testing
This is a test
```
4. That should be enough traffic for what we're doing. 
5. On server2, press Ctrl + C to kill the nc command we've got running and flip back over to the terminal we were running iptraf-ng in. 
6. Press x to stop the monitoring and get out, then choose Exit from the main menu.

### _Examine the Log_:
1. On server1, if we run ls /home/cloud_user we should see traffic_log.txt listed in the output.
2. Read that to see if it was capturing what we need:
`[root@server1]# less /home/cloud_user/traffic_log.txt`
> We should see some log entries showing traffic going from server2 to server1 on port 2525.

## References

https://learn.acloud.guru/course/cad92c58-0fd2-4657-98f7-79268b4ff2db/dashboard
