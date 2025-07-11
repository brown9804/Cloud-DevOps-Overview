# Linux Device Management

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


Last updated: 2025-07-11

----------------------

This is a summary based on [References](#references)

## _Connect to the server_:

`ssh <user_name>@<IPadress>`


## Adding a New Hard Disk to a Linux System:
Understand how to create a new filesystem, mounting the filesystem to a directory, and then configuring the system so the mount persists across reboots.

## _Create a New Partition_:
> Before we go mounting any new partition up, we've got to create that partition.
1. Open up a terminal window and log in using the credentials provided on the lab page, replacing x.x.x.x with the public IP address listed: <br/>
`ssh cloud_user@x.x.x.x`
> Enter the provided password when prompted.
2. Next, let's run the lsblk command to verify we have a /dev/nvme1n1 device available. Once we've confirmed that, we'll create a partition on the /dev/nvme1n1 disk using fdisk. Note that we'll need to preface these commands with sudo for these commands. This partition we create will span the entire disk: <br/>
```
[cloud_user@host]$ lsblk
[cloud_user@host]$ sudo fdisk /dev/nvme1n1
```
3. After running fdisk, we'll have to perform a few tasks. At the Command (m for help): command, type n to make a new partition, then hit Enter. Our Partition type will be p, primary. 
4. Press Enter for Partition number, the First sector, and the Last sector options. This will make fdisk ready to create the partition. Type p at the Command (m for help): to print out what the disk will look like after we commit our changes. 
5. If that all looks good, type w and press Enter to write our changes to disk.

## _Create the Filesystem_:
1. Next, we've got to create a filesystem, so we can read and write data. We'll format the partition to the XFS file system with the mkfs.xfs command. Once that is complete, we'll run blkid on the newly created partition to obtain the UUID. We'll have to make a note of this UUID, since we're going to need it later: <br/>
```
[cloud_user@host]$ sudo mkfs.xfs /dev/nvme1n1p1
[cloud_user@host]$ sudo blkid /dev/nvme1n1p1
```

## _Mount the New Filesystem and Make It Permanent_:
1. We can mount this partition up manually with the mount command, but it won't be a persistent mount; it won't get mounted after something like a reboot.We're going to edit /etc/fstab and create a new entry for the new disk at the bottom: <br/>
`sudo vi /etc/fstab`
2. When you want to add text: hit the esc key and then i to go into insert mode type as normal.
3. When you want to save: hit the esc key and then :wq!
4. You may find the following vim cheat sheet helpful as well: https://linuxacademy.com/site-content/uploads/2019/05/vim-1.png
5. The format should follow the following (be sure to use your disk's UUID from the previous step): <br/>
`UUID=YOURUUID /opt xfs defaults 0 0`
6. We can save the file (:wq!), Then run: <br/>
`[cloud_user@host]$ sudo mount -a`
7. This will mount everything that's listed in fstab, including our new partition.
8. And running a quick df -h /opt should show us roughly 5GB available for the /opt directory.

## Working with the CUPS Print Server:
Understand how to work with print server that will send jobs to PDF files. We will use the lpd (line print daemon) toolset provided by a CUPS installation.

## _Install a PDF Printer_:
1. Open your terminal application.
2. Check to see which printers are installed: <br/>
`lpstat -s`
3. Check to see what types of printer connections are available:  <br/>
`sudo lpinfo -v`
4. Install a PDF printer to use with CUPS:  <br/>
`sudo lpadmin -p CUPS-PDF -v cups-pdf:/`
5. Determine which driver files we can use with our printer by querying the CUPS database for files that contain "PDF":  <br/>
`lpinfo --make-and-model "PDF" -m`
6. Use CUPS-PDF.ppd as the driver file:  <br/>
`sudo lpadmin -p CUPS-PDF -m "CUPS-PDF.ppd"`
7. Run the lpstat command again:  <br/>
`lpstat -s`
8. Check the status of the printer we just installed:  <br/>
`lpc status`
9. Enable the printer to accept jobs, and set it up as the default printer: 
```
sudo lpadmin -d CUPS-PDF -E
sudo cupsenable CUPS-PDF
sudo cupsaccept CUPS-PDF
```
10. Run the lpc status command again:
`lpc status`
> The printer should now be ready.

## _Print a Test Page_:
1. Print a copy of the /etc/passwd file to a PDF file in our home directory: <br/>
`lpr /etc/passwd`
2. Verify that there is a copy of the /etc/passwd file in the home directory: <br/>
`ls`

## _Modify the Printer and Work with the Print Queue_:
1. Configure the printer so that it will not accept any new jobs: <br/>
`sudo cupsreject CUPS-PDF`
2. Verify the status of the printer: <br/>
`lpc status`
3. Attempt to print the /etc/group file to the printer: <br/>
`lpr /etc/group`
4. You should receive a message that says the printer is not currently accepting jobs.
5. Reconfigure the printer to once again accept incoming jobs:
`sudo cupsaccept CUPS-PDF`
6. Check the status of the printer:
`lpc status`
7. Configure the printer so that it accepts jobs to its queue but will not print them:
`sudo cupsdisable CUPS-PDF`
8. Check the status of the printer:
`lpc status`
9. Attempt to print the /etc/group file again:
`lpr /etc/group`
10. List the contents of the /home directory:
`ls`
11. Check the printer's queue: 
`lpq`
12. Remove the job from the printer's queue (remember to substitute the job ID from your command's output):
`lprm <JOB_ID>`
13. Verify that the job was successfully removed from the printer's queue:
`lpq`
14. Re-enable the printer's ability to print new jobs:
`sudo cupsenable CUPS-PDF`
15. Verify that the CUPS-PDF printer is once again ready to accept new jobs:
`lpq`

## Storage Management:
Understanding of how to use these tools is a fundamental component of a Linux sysadmin career.

> Then, become root: <br/>
`sudo -i`

## _Create a 2 GB GPT Partition on /dev/nvme1n1_:
1. Create the partition: <br/>
`gdisk /dev/nvme1n1`
2. Enter n to create a new partition.
3. Accept the default for the partition number.
4. Accept the default for the starting sector.
5. For the ending sector, enter +2G to create a 2 GB partition.
6. Accept the default partition type.
7. Enter w to write the partition information.
8. Enter y to proceed.
9. Finalize the settings: <br/>
`partprobe`

## _Create a 2 GB MBR Partition on /dev/nvme2n1_:
1. Create the partition: <br/>
`fdisk /dev/nvme2n1`
2. Enter n to create a new partition.
3. Accept the default partition type.
4. Accept the default for the partition number.
5. Accept the default for the starting sector.
6. For the ending sector, type +2G to create a 2 GB partition.
7. Enter w to write the partition information.
8. Finalize the settings: <br/>
`partprobe`

## _Format the GPT Partition with XFS and Mount the Device on /mnt/gptxfs Persistently_:
1. Format the partition: <br/>
`mkfs.xfs /dev/nvme1n1p1`
> Getting It Ready for Mounting
2. Run the following: <br/>
`blkid`
3. Copy the UUID of the partition at /dev/nvme1n1p1.
4. Open the /etc/fstab file: <br/>
`vim /etc/fstab`
5. Add the following, replacing <UUID> with the UUID you just copied: <br/>
`UUID="<UUID>" /mnt/gptxfs xfs defaults 0 0`
6. Save and exit the file by pressing Escape followed by :wq.

> Create a Mount Point
1. Create the mount point we specified in fstab: <br/>
`mkdir /mnt/gptxfs`
2. Mount everything that's described in fstab: <br/>
`mount -a`
3. Check that it's mounted: <br/>
`mount`
> The partition should be listed in the output.

## _Format the MBR Partition with ext4 and Mount the Device on /mnt/mbrext4_:
1. Format the partition: <br/>
`mkfs.ext4 /dev/nvme2n1p1`
2. Create the mount point: <br/>
`mkdir /mnt/mbrext4`
3. Mount it: <br/>
`mount /dev/nvme2n1p1 /mnt/mbrext4`
4. Check that it's mounted: <br/>
`mount`
> The partition should be listed in the output.
  
## _Working with LVM Storage_:
Understanding of how to use  LVM managent tool

>>  *Scenario* 
  
> We've been tasked with creating a large logical volume out of the two disks attached to this server. The volume group name should be RHCSA. The Logical Volume name should be pinehead and should be 3 GB in size.
> Make sure that the resulting logical volume is formatted as XFS, and persistently mounted at /mnt/lvol.
> After that is complete, we should grow the logical volume and the filesystem by 200 MB.

## _Create a Physical Device_:
1. To see the names of our disks, we need to run fdisk -l. 
2. Then we run pvcreate /dev/xvdg /dev/xvdf to create the physical devices.
3. To check how it went, we can do a quick pvs or pvdisplay, and we'll see that they've been created.

## _Create a Volume Group_:
1. All we need to do is run vgcreate RHCSA /dev/xvdg /dev/xvdf. 
> RHCSA is going to be the name of our volume group, and those physical devices we created in the last step is where this volume group will go.

## _Create a Logical Volume_:
1. Now we can create the our logical volume using the lvcreate command: <br/>
`[root@host]# lvcreate -n pinehead -L 3G RHCSA`
> -n denotes the name of the LV <br/>
> -L denotes the size of the LV <br/>
> RHCSA is the name of the Volume Group we're creating this LV in

## _Format the LV as XFS and Mount It Persistently at /mnt/lvol_:
1. Now we can format the disk like any other device. To format it as XFS, we'll run: <br/>
`[root@host]# mkfs.xfs /dev/mapper/RHCSA-pinehead`
2. We've got to create a mount point:  <br/>
`mkdir /mnt/lvol`
3. Before we can get it mounting persistently (after reboots), we need the UUID. Run blkid to get it, then copy it. We'll need it in a second.
4. Edit /etc/fstab (with whichever text editor you prefer) and create a new line that looks like this:
`UUID="&ltTHE_UUID_WE_COPIED>" /mnt/lvol xfs defaults 0 0`
5. Now, to mount everything listed in fstab (including this new mount we just created), let's run mount -a.

## _Grow the Mount Point by 200 MB_:
1. To grow an LV, we can run:  <br/>
`[root@host]# lvextend -L+200M /dev/RHCSA/pinehead`
2. We can let the LVM tools automatically resize the filesystem as well by passing the -r or --resizefs flags.
3. Optionally, we could have run a growfs command to resize the filesystem:  <br/>
`[root@host]# xfs_growfs /mnt/lvol`

## References

https://learn.acloud.guru/course/cad92c58-0fd2-4657-98f7-79268b4ff2db/dashboard

<!-- START BADGE -->
<div align="center">
  <img src="https://img.shields.io/badge/Total%20views-456-limegreen" alt="Total views">
  <p>Refresh Date: 2025-07-11</p>
</div>
<!-- END BADGE -->
