# Using Linux on Windows

## Datatransfer

```ps
scp -r C:\Users\domin\Downloads\Project.zip root@mozilla-voice.cs.fhwn.ac.at:~/Desktop/TeamProject
```

## Windows Setup

Use following command in Powershell, which needs to be run as administrator

```ps
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
```

```ps
 dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

```ps
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

```ps
wsl --set-default-version 2
```

Now insatll Debian GNU in Microsoft store

## Debian Setup

    * apt-get install sudo
    * sudo apt update && sudo apt upgrade -y
    * sudo apt install xfce4
    * sudo apt install xrdp -y
    * sudo service xrdp start

After installing use "`ip add`" </br>
and choose the IP-address from the option `Eth0` </br>

## References

- https://debian-handbook.info/browse/de-DE/stable/sect.graphical-desktops.html
- https://docs.microsoft.com/en-us/windows/wsl/install-win10
