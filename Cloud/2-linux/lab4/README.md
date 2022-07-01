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
> With Bash Expansion:

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

## Working with Compressed Files in Linux:
### _Get the Original File Size_: <br/>
`[cloud_user@host]$ ls -lh junk.txt`

### _Creating zip Files_:
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

### _Creating tar Files_:
1. Compression method instead: <br/>
`[cloud_user@host]$ tar -cvzf gztar.tar.gz junk.txt`
2. Then, let's make one using bzip2: <br/>
`[cloud_user@host]$ tar -cvjf bztar.tar.bz2 junk.txt`
3. Finally, we'll use XZ to make one: <br/>
`[cloud_user@host]$ tar -cvJf xztar.tar.xz junk.txt`
4. Run the ls command again to compare the file sizes: <br/>
`[cloud_user@host]$ ls -lh`

### _Practice Reading Compressed Text Files_:
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
