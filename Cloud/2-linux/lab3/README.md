# Package Management and Troubleshooting

----------------------
Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


March, 2022

----------------------

### _Connect to the server_:

`ssh <user_name>@<IPadress>`

## Installing and Managing Packages on Debian/Ubuntu Systems
Understanding how to use package manager and installation utility apt to manage packages on Ubuntu/Debian Linux distributions.

### _Install the Apache Web Server Package_:
> Note: Ubuntu/Debian systems will usually start a service automatically, once its package is installed. You may need to update the package manager.

### _Update package_:
`sudo apt update`

### _Install the packages_:
`sudo apt install apache2 wget`

### _Verify the Server is Running and Capture the Result_:
1. Checking Apache server: <br/>
`curl http://localhost`
2. If that's working, we use the wget package to capture the output of an http request. We'll point the output to a file in our home directory called local_index.response <br/>
`wget --output-document=local_index.response http://localhost`


### References

https://learn.acloud.guru/course/cad92c58-0fd2-4657-98f7-79268b4ff2db/dashboard
