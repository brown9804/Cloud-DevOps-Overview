# File Management, Permissions and Backup

----------------------
Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


March, 2022

----------------------

### _Connect to the server_:

`ssh <user_name>@<IPadress>`


## Creating a Directory Structure in Linux:
Understanding how to create a certain directory and subdirectory structure, plus a couple of empty text files.

### _Create the Parent Directories_:
> By Hand:
```
[cloud_user@host]$ mkdir -p Projects/ancient
[cloud_user@host]$ mkdir Projects/classical
[cloud_user@host]$ mkdir Projects/medieval
```
> With Bash Expansion
`[cloud_user@host]$ mkdir -p Projects/{ancient,classical,medieval}`

### _Create the Subdirectories_:
> By Hand:
```
[cloud_user@host]$ mkdir Projects/ancient/egyptian
[cloud_user@host]$ mkdir Projects/ancient/nubian
[cloud_user@host]$ mkdir Projects/classical/greek
[cloud_user@host]$ mkdir Projects/medieval/britain
[cloud_user@host]$ mkdir Projects/medieval/japan
```
> With Bash Expansion:
```
[cloud_user@host]$ mkdir Projects/ancient/{egyptian,nubian}
[cloud_user@host]$ mkdir Projects/classical/greek
[cloud_user@host]$ mkdir Projects/medieval/{britain,japan}
```
### _Create Some Empty Files_:
```
[cloud_user@host]$ touch Projects/ancient/nubian/further_research.txt
[cloud_user@host]$ touch Projects/classical/greek/further_research.txt
```
### _Rename a Subdirectory_:
`[cloud_user@host]$ mv Projects/classical Projects/greco-roman`
