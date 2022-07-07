# Processes Management

----------------------
Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


March, 2022

----------------------

This is a summary based on [References](#references)

> pid: process ID

## Starting a Process:
> When you start a process (run a command), two ways of do it:
1. Foreground Processes
2. Background Processes

### _Foreground Processes_:
> By default, every process that you start runs in the foreground. It gets its input from the keyboard and sends its output to the screen. <br/>
> While a program is running in the foreground and is time-consuming, no other commands can be run (start any other processes) because the prompt would not be available until the program finishes processing and comes out.

### _Background Processes_:
> A background process runs without being connected to your keyboard. If the background process requires any keyboard input, it waits. <br/>
> The advantage of running a process in the background is that you can run other commands; you do not have to wait until it completes to start another! <br/>
> The simplest way to start a background process is to add an ampersand (`&`) at the end of the command. <br/>

## Listing Running Processes:
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



## References:
[1] From https://www.tutorialspoint.com/unix/unix-processes.htm <br/>
