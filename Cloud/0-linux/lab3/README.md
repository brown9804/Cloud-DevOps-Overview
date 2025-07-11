# Package Management and Troubleshooting

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


Last updated: 2025-07-10

----------------------

This is a summary based on [References](#references)

## _Connect to the server_:

`ssh <user_name>@<IPadress>`

## Installing and Managing Packages on Debian/Ubuntu Systems
Understanding how to use package manager and installation utility apt to manage packages on Ubuntu/Debian Linux distributions.

## _Install the Apache Web Server Package_:
> Note: Ubuntu/Debian systems will usually start a service automatically, once its package is installed. You may need to update the package manager.

## _Update package_:
`sudo apt update`

## _Install the packages_:
`sudo apt install apache2 wget`

## _Verify the Server is Running and Capture the Result_:
1. Checking Apache server: <br/>
`curl http://localhost`
2. If that's working, we use the wget package to capture the output of an http request. We'll point the output to a file in our home directory called local_index.response <br/>
`wget --output-document=local_index.response http://localhost`


## Installing and Managing Packages on Red Hat/CentOS Systems
1. Attempt to install the RPM to determine what dependencies are required: <br/>
```
cd Downloads
sudo rpm -i elinks-0.12-0.37.pre6.el7.0.1.x86_64.rpm
```
> We'll get some dependency errors (version numbers may vary).
2. Use the package manager to determine which packages provide the dependencies: <br/>
`sudo yum provides libmozjs185*` <br/>
> The output shows that the js package provides libmozjs185.
3. Install the packages that provide those dependencies: <br/>
`sudo yum install js`
4. All of our dependencies were not resolved with that one package installation. Attempt to install the RPM again. If any other dependencies are needed, repeat steps 3 and 4 (substituting libmozjs185 with whatever dependency is still missing) to resolve that issue: <br/>
`sudo rpm -i elinks-0.12-0.37.pre6.el7.0.1.x86_64.rpm`
5. Once the RPM is installed successfully, run elinks to ensure the application is working properly: <br/>
`elinks`
6. Attempt to open a website by providing a URL: <br/>
`http://www.amazon.com`

## Troubleshooting RPM Issues:
Understand how to install telnet and install Apache.

1. Become the root user: <br/>
`sudo -i`

## _Telnet Installation_:
1. Install the telnet package: <br/>
`yum install -y telnet`
2. Verify the integrity of the RPM database: <br/>
```
cd /var/lib/rpm/
/usr/lib/rpm/rpmdb_verify Packages
```
3. Move Packages to Packages.bad and create a new RPM database from Packages.bad: <br/>
```
mv Packages Packages.bad
/usr/lib/rpm/rpmdb_dump Packages.bad | /usr/lib/rpm/rpmdb_load Packages
```
4. Verify the integrity of the new RPM database: <br/>
`/usr/lib/rpm/rpmdb_verify Packages`
5. Query installed packages for errors: <br/>
`rpm -qa > /dev/null`
6. Rebuild the RPM database: <br/>
`rpm -vv --rebuilddb`
7. Install telnet: <br/>
`yum install -y telnet`

## _Update Apache_:
1. Attempt to install Apache: <br/>
`yum install -y httpd`
2. Edit /etc/yum.conf: <br/>
`vim /etc/yum.conf`
3. Remove the exclusion for httpd: <br/>
`exclude=httpd`
4. Save and close the file: <br/>
`:wq`
5. Install Apache: <br/>
`yum install -y httpd`

## References

https://learn.acloud.guru/course/cad92c58-0fd2-4657-98f7-79268b4ff2db/dashboard

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-195-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-10</p>
</div>
<!-- END BADGE -->
