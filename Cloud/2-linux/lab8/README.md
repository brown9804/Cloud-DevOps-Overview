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

## References

https://learn.acloud.guru/course/cad92c58-0fd2-4657-98f7-79268b4ff2db/dashboard
