# Processes Management

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


Last updated: 2025-07-11

----------------------

This is a summary based on [References](#references)

> pid: process ID

## Starting a Process
> When you start a process (run a command), two ways of do it:
1. Foreground Processes
2. Background Processes

### _Foreground Processes_
> By default, every process that you start runs in the foreground. It gets its input from the keyboard and sends its output to the screen. <br/>
> While a program is running in the foreground and is time-consuming, no other commands can be run (start any other processes) because the prompt would not be available until the program finishes processing and comes out.

### _Background Processes_
> A background process runs without being connected to your keyboard. If the background process requires any keyboard input, it waits. <br/>
> The advantage of running a process in the background is that you can run other commands; you do not have to wait until it completes to start another! <br/>
> The simplest way to start a background process is to add an ampersand (`&`) at the end of the command. <br/>

## Listing Running Processes
> It is easy to see your own processes by running the `ps` (process status) command <br/>
> One of the most commonly used flags for ps is the -f ( f for full) option, which provides more information as shown:

`$ps -f`

```
UID PID PPID C STIME TTY TIME CMD
```

1. `UID`: User ID that this process belongs to (the person running it)
2. `PID`: Process ID
3. `PPID `: Parent process ID (the ID of the process that started it)
4. `C`: CPU utilization of process
5. `STIME`: Process start time
6. `TTY`: Terminal type associated with the process
7. `TIME`: CPU time taken by the process
8. `CMD`: The command that started this process

> There are other options which can be used along with ps command:
1. `-a`: Shows information about all users
2. `-x`: Shows information about processes without terminals
3. `-u`: Shows additional information like -f option
4. `-e`: Displays extended information

## Stopping Processes
> Sending a CTRL + C keystroke (the default interrupt character) will exit the command. <br/>

> If a process is running in the background, you should get its Job ID using the ps command. After that, you can use the kill command to kill the process, example:
```
$ps -f
UID PID PPID C STIME TTY TIME CMD
amrood 6738 3662 0 10:23:03 pts/6 0:00 first_one
amrood 6739 3662 0 10:22:54 pts/6 0:00 second_one
$kill 6738
```

Or forced: <br/>
`$kill -9 6738`

## Parent and Child Processes
Each unix process has two ID numbers assigned to it:
- Process ID (pid) 
- Parent process ID (ppid). 

> Each user process in the system has a parent process. Most of the commands that you run have the shell as their parent. 

## Zombie and Orphan Processes
> Normally, when a child process is killed, the parent process is updated via a SIGCHLD signal. Then the parent can do some other task or restart a new child as needed. However, sometimes the parent process is killed before its child is killed. In this case, the "parent of all processes," the init process, becomes the new PPID (parent process ID). In some cases, these processes are called orphan processes.

> When a process is killed, a ps listing may still show the process with a Z state. This is a zombie or defunct process. The process is dead and not being used. These processes are different from the orphan processes. They have completed execution but still find an entry in the process table.

## Daemon Processes

> Daemons are system-related background processes that often run with the permissions of root and services requests from other processes.

> A daemon has no controlling terminal. It cannot open /dev/tty. If you do a "ps -ef" and look at the tty field, all daemons will have a ? for the tty.

> To be precise, a daemon is a process that runs in the background, usually waiting for something to happen that it is capable of working with. For example, a printer daemon waiting for print commands.

> If you have a program that calls for lengthy processing, then it’s worth to make it a daemon and run it in the background.

## Job ID Versus Process ID

> Background and suspended processes are usually manipulated via job number (job ID). This number is different from the process ID and is used because it is shorter.

> A job can consist of multiple processes running in a series or at the same time, in parallel. Using the job ID is easier than tracking individual processes.

## References
[1] From https://www.tutorialspoint.com/unix/unix-processes.htm <br/>

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-673-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-14</p>
</div>
<!-- END BADGE -->
