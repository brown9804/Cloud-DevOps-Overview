# Working with Text Files and Streams

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


March, 2022

----------------------

This is a summary based on [References](#references)

## _Connect to the server_:

`ssh <user_name>@<IPadress>`


## Modify a Text File Using sed:
> Someone got confused and wrote about cows instead of ants in a text file. We've got to replace all instances of cows and with Ants, regardless of whether or not cows contains any capital letters.
## _See File Content_:
1. Let's look at the file we're dealing with: <br/>
`cat fable.txt`

## _The Fix_:
1. Replace information
> We're going to run a sed command. The -i means "do this in place," as in don't create another file. The capital I near the end stands for "case-insensitive" and means that whether cows has any capital letters in it or not, change it to Ants. The g means do it globally, throughout the whole file. <br/>

`sed -i 's/cows/Ants/Ig' fable.txt`

> Now if we run our cat command again, we'll see that all the cows are gone.

## Working with Basic Regular Expressions:
Understand how to read some text files and redirecting some output (output that we'll decide on using regular expressions) to other text files.

## _Locate HTTP Services_:
1. Read information:
> We want to read all of the lines in /etc/services that start with http (but not any that start with httpx) and send them to ~/http-services.txt <br/>
`grep ^http[^x] /etc/services > ~/http-services.txt`
2. To check if we have what we want in the new file, run: <br/>
`cat ~/http-services.txt`

## _Locate a Specific Services_:
1. Search lines: <br/>
> This one is a little trickier. We want to find all of the lines in /etc/services that start with ldap. The fifth character can be any alphanumeric character, but the sixth character can not be an a. We'll dump the output into ~/lpic1-ldap.txt <br/>
`grep ^ldap.[^a] /etc/services > ~/lpic1-ldap.txt`
2. To check if we have what we want in the new file, run: <br/>
`cat ~/lpic1-ldap.txt`

## _Refine the HTTP Results_:
1. Search lines: <br/>
> We want to read the ~/http-services.txt file that we created earlier, and just look at lines that don't end with the word service. This grep command will do it: <br/>
`grep -v service$ ~/http-services.txt > ~/http-updated.txt`
2. To check if we have what we want in the new file, run: <br/>
`cat ~/http-updated.txt`

## Creating and Modifying a File with Vim:
Understand how to create a text file with Vim, and edit it.

## _Create a New File_:
1.We're going to create a new file called notes.txt in /home/cloud_user: <br/>
```
cd
vim notes.txt
```
> Now, to add the text Beginning of Notes File, we need to get into insert mode, by pressing i. We can start typing now once we're in insert mode.
2. Leave two blank lines after Beginning of Notes File. Now, to save the file and quit Vim, we have to first hit Esc (to get out of insert mode), type :wq! (write and quit).

## _Send Data to notes.txt_:
1. Appends content: <br/>
> Using the cat command and output redirection, send the contents of the /etc/redhat-release file to the end of the notes.txt file, taking care to append the contents so as to not overwrite the file (using >>, not >)
> Run this to append notes.txt with the contents of /etc/redhat-release: <br/>
`cat /etc/redhat-release >> notes.txt`

## _Modify notes.txt_:
> Let's open notes.txt again for editing. We'll place the cursor before the opening parenthesis around the word Core and use a keyboard shortcut to delete the text from there to the end of the line. We'll leave two more blank lines at the end of the file and then save and quit again.
> Here are all of the steps to do that:
1. Open the file: <br/>
`vim notes.txt`
2. Use the arrow keys to move to the beginning parentheses before Core <br/>
3. Remove text from the cursor's position to end of line: <br/>
`SHIFT D (or d$)`
4. Create a blank line under where the cursor is: <br/>
`o
5. Hit Enter to create the second blank line
6. Hit Esc to leave insert mode
7. Hitting o added a blank line, but also put us in insert mode
8. Write and quit: <br/>
`:wq!`

## _Send More Data to the File, and Modify Its Contents_:
> Now we're going to send free -m output to the end of notes.txt, edit notes.txt again, delete the last line of the file, and add two more blank lines to the end of the file. 
> Then, we're going to jump to the third line of the file, enter some text, and make another blank line afterward.
> Here are all of the steps to do that:
1. Append the notes.txt: <br/>
`free -m >> notes.txt`
2. Edit notes.txt: <br/>
`vim notes.txt`
3. Navigate to the Swap line with arrow keys.
4. Delete the line: <br/>
`dd`
5. Create a blank line under where the cursor is (and put us in insert mode): <br/>
`o`
6. Hit Enter to create the second blank line.
7. Hit Esc to get out of insert mode.
8. Get to the 3rd line of file: <br/>
`:3`
9. Get back into insert mode: <br/>
`i`
10. Type This is a practice system.
11. Hit Enter to make another blank line.
12. Hit Esc to leave insert mode.
13. Write and quit: <br/>
`:wq!`

## Finalize the Notes File:
> We're going to dump one last bit of text into the file, then edit it again. We'll take the output from dbus-uuidgen --get, append it to notes.txt then edit notes.txt so that the text Dbus ID = is in the beginning of the new appended line.
> We'll do it like this:
1. Append the notes.txt: <br/>
`dbus-uuidgen --get >> notes.txt`
2. Edit notes.txt: <br/>
`vim notes.txt`
3. Get right to the end of the file: <br/>
`G (Capital G)`
4. Get into insert mode: <br/>
`i`
5. Type "Dbus ID = " (with a space between the equals sign and the dbus-uuidgen --get command's output). Only type the text within the quotation marks.
6. Write and quit:
`:wq!`

## References

https://learn.acloud.guru/course/cad92c58-0fd2-4657-98f7-79268b4ff2db/dashboard

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-1192-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-16</p>
</div>
<!-- END BADGE -->

Last updated: 2025-07-11
