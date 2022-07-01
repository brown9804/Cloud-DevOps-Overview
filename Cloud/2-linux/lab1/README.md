# System Service Management, Runlevels and Boot Targets

----------------------
Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


March, 2022

----------------------

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
