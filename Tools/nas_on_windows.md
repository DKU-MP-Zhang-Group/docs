# Mount NAS on your windows

> [!ATTENTION]
> 1. **This is a high risk behavior!** Because the file encode format is usually different 
between Linux & Windows. If you successfully mounted the NAS to your windows system, please 
make sure **only to read and download** the file on NAS and **do not** do any operation to edit the file! If you want to upload the file, try [scp](./Tools/linux_commands.md?id=scp).
> [!WAENING]
> 1. Beacuse of the default encode format of Linux, please only use **English** to create the file name and folder name.
> 2. When you want to use the data on NAS, make sure to copy the data to your **local workspace**. Do not **directly** use the data in NAS!(eventhough you just want to read the data!)

## Prepare
1. A computer device under DKU or DUKE net work(if you are using windows, you need **Pros** version. Home version does not have NFS feature. Or check microsoft official website before starting)
2. **Add you ip to the firewall** (ask IT or [Tianyi](mailto:tianyi.zhang2@duke.edu))
3. Knowledge about basic windows commands
4. Knowledge about regedit(not necessary)

## How to mount

**Note: Do not edit the regedit unless you know what you are doing!!!**  
If you do not know what is regedit, just finish the above steps in following tutorial:  
[Seems useful](https://graspingtech.com/mount-nfs-share-windows-10/)  

## Unmount
[umount](https://forsenergy.com/en-us/nfs_/html/0560cc79-bcc1-42bb-8866-e5cf1ee6b9f8.htm#:~:text=To%20unmount%20an%20NFS%20shared%20resource%20from%20a,umount%20%5B%20%E2%80%93f%5D%20%7B%20%E2%80%93a%20%7C%20Drive%20%7D)  
For example:  
```shell
umount Y:
```
