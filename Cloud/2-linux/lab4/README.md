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


Creating a Directory Structure in Linux
We've got a researcher who needs a workstation set up. Before it's handed off, we need to create a certain directory and subdirectory structure, plus a couple of empty text files. This is fairly simple, so let's get right into it.

Create the Parent Directories
By Hand
We can create the directory structure by hand with these three commands:

[cloud_user@host]$ mkdir -p Projects/ancient
[cloud_user@host]$ mkdir Projects/classical
[cloud_user@host]$ mkdir Projects/medieval
With Bash Expansion
We could do it another way, though, using Bash expansion. It's much less typing. This command makes all three directories in one pass:

[cloud_user@host]$ mkdir -p Projects/{ancient,classical,medieval}
Create the Subdirectories
Now, let's create the next level of subdirectories. Again, there are two ways to do it.

By Hand
[cloud_user@host]$ mkdir Projects/ancient/egyptian
[cloud_user@host]$ mkdir Projects/ancient/nubian
[cloud_user@host]$ mkdir Projects/classical/greek
[cloud_user@host]$ mkdir Projects/medieval/britain
[cloud_user@host]$ mkdir Projects/medieval/japan
With Bash Expansion
[cloud_user@host]$ mkdir Projects/ancient/{egyptian,nubian}
[cloud_user@host]$ mkdir Projects/classical/greek
[cloud_user@host]$ mkdir Projects/medieval/{britain,japan}
Create Some Empty Files
We've got to create a couple of empty text files for the researcher to use, and we'll do it with the touch command:

[cloud_user@host]$ touch Projects/ancient/nubian/further_research.txt
[cloud_user@host]$ touch Projects/classical/greek/further_research.txt
Rename a Subdirectory
We thought we were all done, but heard back from the rest of the team that this researcher needs the classical directory renamed to greco-roman. We can do that easily with the mv command:

[cloud_user@host]$ mv Projects/classical Projects/greco-roman
And now we can hand the system back to the team.