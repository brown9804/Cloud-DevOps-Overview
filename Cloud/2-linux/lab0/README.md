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

