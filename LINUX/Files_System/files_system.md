

# Linux系统的文件目录结构

## /bin：
    全称binary，含义是二进制。该目录中存储的都是二进制文件，且这些二进制文件都是可以运行。
## /sbin：
    全称super binary，该目录也是存储一些可以被执行的二进制文件，但是必须得有super权限的用户才能执行。
## /home：
    即家目录，表示除了root用户以外其他用户的家目录，类似于windows下的User/用户目录。
## /root：
    该目录是root用户自己的家目录。
## /usr：
    存放的是用户自己安装的软件。类似于windows下的program files。
## /dev：
    该目录中主要存放的是外接设备，例如盘、其他的光盘等，但在其中的外接设备是不能直接被使用的，需要挂载（类似windows下的分配盘符）。
## /etc：
    该目录主要存储为系统或者软件的配置文件。
## /proc：
    process，表示进程，该目录中存储的是Linux运行时候的进程。
## /var：
    存放的程序/系统的日志文件的目录。
## /tmp：
    表示“临时”的，当系统运行时候产生的临时文件会在这个目录存着。
## /mnt：
    当外接设备需要挂载的时候，就需要挂载到mnt目录下。

