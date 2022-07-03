# The Linux Shell


----------------------
Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


March, 2022

----------------------

### _Connect to the server_:

`ssh <user_name>@<IPadress>`

## Modifying the Bash Shell
Understand how to create our own alias for a command and then create a new command that will take a positional argument.

>> Scenario 

> You have just started a new job managing a web server for a small company. To make your job a bit easier, you have decided to create some shorthand commands that will help you in your daily tasks. <br/>
> *. First, you will create an alias to view the status of the HTTP service that is running on the company's small web server. <br/>
> *. Next, you will create a function that allows you to monitor the disk usage of a couple of web content directories.

### _Create the alias_:
1. The first step is to create an alias for the Bash shell that will allow you to view the service status of the web server itself. You will name this alias webstat. When you type the command webstat at the prompt, you will see the output of the command systemctl status httpd.service. User-created aliases and functions should go in your local ~/.bashrc file. Using the commands listed, append the following alias to your ~/.bashrc file: <br/>
`echo 'alias webstat="systemctl status httpd.service"' >> /home/cloud_user/.bashrc`

### _Load and test the alias_:
1. Now that we have created an alias that displays the status of the web server, we need to tell Bash that we want to use it in our current session. First, we need to source our .bashrc file using the “dot” (.) command:  <br/>
`. ~/.bashrc`
2. Now that the Bash environment has been refreshed with the new alias from our ~/.bashrc file, we can use our new alias:  <br/>
`webstat`
> We should be able to see the output of our service's status command.

### _Create your function_:
1. The next step is to create a function that will take the name of a directory as a parameter and print out how much disk space that directory is using. Using the vi text editor, open up the ~/.bashrc file and add the following function to the bottom, beneath the alias that you created earlier:  <br/>
`vim ~/.bashrc`
```
function webspace()
{
	du -h /var/www/html/$1;
}
```
2. Save and close your file. 
3. Then source the .bashrc file again:  <br/>
`. .bashrc`

### _Use the webspace function_:
1. Since the /var/www/html directory is the root location for all of the individual site locations for this web server, all you need to do is provide the name of the folder that contains a particular part of the site to the webspace function. To view the size and contents of the main public web page, enter this command:  <br/>
`webspace main`
> This will print out the contents of the /var/www/html/main directory and how much disk space this directory uses. The $1 used in your function is a positional argument. When you type webspace main at the prompt, the word main is replaced by the $1 argument, thus providing the output of the command for the /var/www/html/main directory.
2. Try the same command again, this time for the customer directory on the web server:  <br/>
`webspace customer`
> You should see more directories in the output, plus a 5 MB client binary file.




## References

https://learn.acloud.guru/course/cad92c58-0fd2-4657-98f7-79268b4ff2db/dashboard
