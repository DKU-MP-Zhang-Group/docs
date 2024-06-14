> [!NOTE]
> for the first time login, you **cannot** use vscode.  
## Powershell example
1. open powershell  
press "win"+"r" at the same time  
![](imgs/2023-11-11-02-36-29.png)  
input "powershell"  
2. ssh to server  
![](imgs/2023-11-11-02-37-33.png)  
the command format is:  
```bash
ssh your_name@server_ip
```
3. input password  
![](imgs/2023-11-11-02-38-08.png)  
Note: even though you input the password here, the cursor will not move, and your input will not appear on the screen.  
once you finished, just press ENTER.  
4. change the password  
![](imgs/2023-11-11-02-44-37.png)  
you should use at least 8 bytes, with numbers and letters.  
then it will close the remote session:  
![](imgs/2023-11-11-02-47-15.png)  
5. relogin use your new password  
![](imgs/2023-11-11-02-48-04.png)  

## vscode example
1. download vscode from [official website](https://code.visualstudio.com/Download). it's free.  
2. install ssh extension:  
![](imgs/2023-11-11-02-19-26.png)  
it will automatically install several other extensions,  **donot** uninstall them.  
3. add your server:  
![](imgs/2023-11-11-02-23-00.png)  
the command format is:  
```bash
ssh your_name@server_ip
```
your user name and server ip is sent to you.  
4. select configuration file:   
![](imgs/2023-11-11-02-25-20.png)    
usually the first one.  
5. refresh  
![](imgs/2023-11-11-02-26-17.png)  
wait about 5~10 seconds. then you will find your server here:  
![](imgs/2023-11-11-02-27-00.png)  
6. open it  
![](imgs/2023-11-11-02-27-43.png)  
in current window or new window, depending on your interest.  
7. select system  
![](imgs/2023-11-11-02-28-58.png)  
click "Linux"  
8. enter the password  
![](imgs/2023-11-11-02-29-44.png)  
9. wait a while  
![](imgs/2023-11-11-02-49-00.png)  
for the first time usage, you should wait a while till the downloading in server finished(aka. the message in red box disappear).  
10. use it  
![](imgs/2023-11-11-02-52-33.png)  
you can click the "terminal" to open the terminal, and choose the bottom at the center to select a file or a folder. then press "confirm" to decide.  