# File Management, Permissions and Backup

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


March, 2022

----------------------

This is a summary based on [References](#references)

## _Connect to the server_:

`ssh <user_name>@<IPadress>`


## Creating a Directory Structure in Linux:
Understanding how to create a certain directory and subdirectory structure, plus a couple of empty text files.

## _Create the Parent Directories_:
> By Hand:

```
[cloud_user@host]$ mkdir -p Projects/ancient
[cloud_user@host]$ mkdir Projects/classical
[cloud_user@host]$ mkdir Projects/medieval
```
> With Bash Expansion:

`[cloud_user@host]$ mkdir -p Projects/{ancient,classical,medieval}`

## _Create the Subdirectories_:
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
## _Create Some Empty Files_:
```
[cloud_user@host]$ touch Projects/ancient/nubian/further_research.txt
[cloud_user@host]$ touch Projects/classical/greek/further_research.txt
```
## _Rename a Subdirectory_:
`[cloud_user@host]$ mv Projects/classical Projects/greco-roman`

## Working with Compressed Files in Linux:
## _Get the Original File Size_: <br/>
`[cloud_user@host]$ ls -lh junk.txt`

## _Creating zip Files_:
> Gzip
1. Compressing data: <br/>
`[cloud_user@host]$ gzip junk.txt`
2. Run ls to view the size of the file: <br/>
`[cloud_user@host]$ ls -lh`
3. Unzip: <br/>
`[cloud_user@host]$ gunzip junk.txt.gz`

> bzip
1. Compression method instead: <br/>
`[cloud_user@host]$ bzip2 junk.txt`
2. Run ls to view the size of the file: <br/>
`[cloud_user@host]$ ls -lh junk.txt.bz2`
3. Unzip: <br/>
`[cloud_user@host]$ bunzip2 junk.txt.bz2`

> XZ
1. Compression method instead: <br/>
`[cloud_user@host]$ xz junk.txt`
2. Run ls to view the size of the file: <br/>
`[cloud_user@host]$ ls -lh`
3. Unzip: <br/>
`[cloud_user@host]$ unxz junk.txt.xz`

## _Creating tar Files_:
1. Compression method instead: <br/>
`[cloud_user@host]$ tar -cvzf gztar.tar.gz junk.txt`
2. Then, let's make one using bzip2: <br/>
`[cloud_user@host]$ tar -cvjf bztar.tar.bz2 junk.txt`
3. Finally, we'll use XZ to make one: <br/>
`[cloud_user@host]$ tar -cvJf xztar.tar.xz junk.txt`
4. Run the ls command again to compare the file sizes: <br/>
`[cloud_user@host]$ ls -lh`

## _Practice Reading Compressed Text Files_:
How to read the contents of compressed files without having to actually decompress them? There is a way! Let's do that now. First, let's copy over the /etc/passwd file to your home directory:
`[cloud_user@host]$ cp /etc/passwd /home/cloud_user/`

> Gzip
1. Compression method instead: <br/>
`[cloud_user@host]$ tar -cvzf passwd.tar.gz passwd`
2. And we can use the zcat command to read this compressed file: <br/>
`[cloud_user@host]$ zcat passwd.tar.gz`

> bzip2
1. Now let's compress the file, using bzip2, into a tarball: <br/>
`[cloud_user@host]$ tar -cvjf passwd.tar.bz2 passwd`
2. We can use the bzcat command to read the compressed file: <br/>
`[cloud_user@host]$ bzcat passwd.tar.bz2`

> XZ
1. Finally, let's create an xz tar file: <br/>
`[cloud_user@host]$ tar -cvJf passwd.tar.xz passwd`
2. And we can use the xzcat command to read its contents: <br/>
`[cloud_user@host]$ xzcat passwd.tar.xz`

## Managing File Attributes and Permissions:
## _Objectives_:
1. Reset a directory's permissions to the following:
  - Everyone can access the directory
  - Everyone can read the files in the directory
  - No one can execute files in the directory
2. Apply all of these permissions to all subdirectories recursively

## _Grant Access to the Directory_:
1. Change to the opt directory: <br/>
`cd /opt`
2. Next, open all of the directory's files and permissions with the following command:  <br/>
`ls -la`
3. Let's try to access the myapp directory. Run the following command:  <br/>
`cd myapp/`
4. How to fix "Permission denied":
`sudo chmod 777 myapp`
5. Reopen the directory files and permissions using the ls -la command. Now let's try to open the directory again:
`cd myapp`

## _Change the Directory Permissions_:
1. Give all users read and write permissions for this directory: <br/>
`sudo chmod -f -x -R *`
> Just everyone read and write permissions 
`sudo chmod 666 -f -R *`
2. List the directory files and permissions again: <br/>
`ls -la`
3. How to set the directories as executable: <br/>
`sudo find /opt/myapp -type d -exec chmod o+x {} \;`

## _Create a Symbolic (Soft) Link_:
1. Creating a symbolic (or soft) link from the /etc/redhat-release file to a new link file named release in the home directory: <br/>
`ln -s /etc/redhat-release release`
2. Verify if the link is valid: <br/>
`ls -l`
3. Check if you can read the file's contents: <br/>
`cat release`
4. Check the link's contents: <br />
`cat /etc/redhat-release`
> Should be the same

## _Check the Inode Numbers for the Link_:
1. Look at the inode number of /home/cloud_user/release: <br/>
`ls -i release`
2. Check the inode number for /etc/redhat-release: <br/>
`ls -i /etc/redhat-release`
> They should be different, as the symbolic link is just a new filesystem entry that references the original file.

## _Create a Hard Link_:
1. Create docs directory: <br/>
`mkdir docs`
2. Copy /etc/services into the docs directory: <br/>
`cp /etc/services docs/`
3. Create a hard link from the /home/cloud_user/docs/services file to a new link location named /home/cloud_user/services: <br/>
`ln docs/services services`
4. Check the link's inode number as well as the inode number for the original /etc/services: <br/>
`ls -l`
5. View the contents of the inodes: <br/>
> This should verify for us that this is a hard link, not a soft link. It won't have an arrow pointing to the actual file it's linked to, like a soft link does. Just to verify, check these two with cat and make sure they're the same:
```
ls -i services
ls -i docs/services
```
> You should see they the same inode number, meaning they're essentially the same file.

## _Attempt to Create a Hard Link Across Filesystems_:
1. View the individual block devices: <br/>
`lsblk`
> Each partition has its own set of inodes, hard links across partitions don't work. Soft links should.
2. Trying to make a hard link from /home/cloud_user/docs/services to /opt/services: <br/>
`ln /home/cloud_user/docs/services /opt/services`
> Should get a failed to create hard link error

## _Attempt to Create a Soft Link Across Filesystems_:
1. Trying to make the same sort of cross-partition link, using the -s flag to make it a soft link: <br/>
`sudo ln -s /etc/redhat-release /opt/release`
> There shouldn't be any output, meaning it was successful.
2. View the contents of the inodes again: <br/>
```
ls -i /etc/redhat-release
ls -i /opt/release
```
> You should see they have different inodes, but the linking will work.

## Encrypt a File Using GPG:
Understand how to new public GPG key, encrypt a file and sign it, and send that file to another user to decrypt with "A Cloud Guru" public key.

## _Create a GPG Key for cloud user_:
1. Generate a new GPG key: <br/>
`[cloud_user@host]$ gpg --gen-key`
2. Credentials:
> Accept the defaults for each prompt. For the user ID, enter cloud_user, and use cloud_user@localhost for the email address. We can leave the comment field blank by just pressing Enter, and press o at the end for OK. 
> We'll use password321 when we're prompted for a passphrase, and when we're prompted to confirm it.
3. Now that the key has been created, we need to export it so that Gordon Freeman can decrypt files he gets from us. We'll do that like this: <br/>
`[cloud_user@host]$ gpg -a -o gfreeman.key --export &lt;KEY_ID>`
4. In that command, use the public key reference ID from the output of the key generation. It will be a random string, and the line it's sitting on (in the key generation output) looks like this: <br/>
 `gpg: key XXXXXXXX marked as ultimately trusted`
5. Now, we'll use the mail command to send an email to Gordon Freeman containing the cloud_user public key as an attachment: <br/>
```
[cloud_user@host]$ mail -s "here is your key" -a gfreeman.key gfreeman@localhost`
Don't lose this!  I'll call you with the passphrase.
.
```
> Include that final period (on the line by itself) and then press Enter to send the message.

## _Configure GPG for Gordon_:
1. Just as we did with the cloud_user account, we'll generate a GPG key for Mr. Freeman, accepting the defaults for each prompt. The only difference will be having a user ID of gfreeman and an email address of gfreeman@localhost: <br/>
`[gfreeman@host]$ gpg --gen-key`
2. Once we've created the key for Mr. Freeman, we can open up the mutt email client, and save the public key sent over by the cloud_user account: <br/>
`[gfreeman@host]$ mutt`
> Arrow up and down to highlight the cloud_user message, then press Enter. Press v to view the attachment, and press s to save it to Mr. Freeman's home directory. Finally, press q to quit Mutt.
3. Now, to import the public key from cloud_user into Mr. Freeman's keyring, run the following command: <br/>
`[gfreeman@host]$ gpg --import gfreeman.key`
4. We can run this to view the contents of Mr. Freeman's keyring: <br/>
`[gfreeman@host]$ gpg --list-keys`
5. Let's log out of gfreeman's account: <br/>
`[gfreeman@host]$ exit`

## _Generate a Signed Document and Send It to Gordon_:
1. When we digitally sign a file, we are using our private GPG key to guarantee that this file came from us. The user that receives the file will use their copy of the public key from us to verify that we signed the file. Let's generate a test document: <br/>
`[cloud_user@host]$ echo "Just need you to verify this file." > note.txt`
2. Now we'll use cloud_user's private key to sign the file:  <br/>
`[cloud_user@host]$ gpg --clearsign note.txt`
> Remember that we need to use the passphrase we created earlier (password321).
> Now there should now be a note.txt.asc file in cloud_user's home directory. We can run a quick ls to make sure.
3. Now that we've made the file, let's email it to gfreeman@localhost:  <br/>
```
[cloud_user@host]$ mail -s "check this out" -a note.txt.asc gfreeman@localhost
Could you verify this file for me?
.
```

## _Verify the Signature of the Emailed Document_:
> Use the mutt email client, and just as before, view and save the new email message's attachment.
1. Now, verify the note.txt.asc file that was emailed: <br/>
`[gfreeman@host]$ gpg --verify note.txt.asc`
2. We'll get a warning about the signature not being verified by a third party, and that's ok. What is important is the following line from the output:  <br/>
`gpg: Good signature from "cloud_user <cloud_user@localhost>"`
> This is what a verified file displays.
3. Next, encrypt a copy of the /etc/fstab file like this:  <br/>
```
[gfreeman@host]$ cp /etc/fstab ~
[gfreeman@host]$ gpg -a -r cloud_user -e ~/fstab
```
> You will see a general warning displayed about the key possibly not belonging to the named person. We already know that this key is from cloud_user, so just press y at the prompt.
4. Verify that there is a file called fstab.asc in the gfreeman home directory (by running ls). Create a new email to cloud_user and attach this file:  <br/>
```
[gfreeman@host]$ mail -s "looks good" -a fstab.asc cloud_user@localhost
Can you decrypt this?
.
```
5. Log out:  <br/>
`[gfreeman@host]$ exit`

## _Decrypt the Attached File_:
> Now, as cloud_user, open up the mutt email client and save the fstab.asc attachment from the new email.
1. Decrypt the saved fstab.asc file with the gpg command, and enter the passphrase for cloud_user's key when prompted: <br/>
`[cloud_user@host]$ gpg fstab.asc` 
2. Now let's verify that we can read the contents of the decrypted file:  <br/>
`[cloud_user@host]$ cat fstab`


## References

https://learn.acloud.guru/course/cad92c58-0fd2-4657-98f7-79268b4ff2db/dashboard

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-195-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-10</p>
</div>
<!-- END BADGE -->
