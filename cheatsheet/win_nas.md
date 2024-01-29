1. nfs server

https://poweradm.com/configure-nfs-client-windows/

```shell
Install-WindowsFeature NFS-Client, RSAT-NFS-Admin
```

```shell
Enable-WindowsOptionalFeature -FeatureName ServicesForNFS-ClientOnly, ClientForNFS-Infrastructure -Online -NoRestart
```

```shell
New-PSdrive -PSProvider FileSystem -Name Z -Root \\10.200.14.77\lz97-leizhang -Persist
```
```shell
Remove-PSdrive -Name Z
```
or
```shell
mount -o anon \\10.200.14.77\lz97-leizhang Z:
```
```shell
Umount Z:
```

```shell
New-ItemProperty HKLM:\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default -Name AnonymousUID -Value 00000000 -PropertyType "DWord"
New-ItemProperty HKLM:\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default -Name AnonymousGID -Value 00000000 -PropertyType "DWord"
```