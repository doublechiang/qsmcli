# qsmcli
Q system management command line tool

# Installation
You will need to install python3 first.
And then 
    # pip3 install -r requirements.txt

## supported shell mode and command

### Command line mode
When invoke this command, if there is any argument, then the command executed.

### Shell mode
In Shell mode, if there is no argument is specified, then the shell mode is entered.
The host and username/password is saved in the prompt.

## Command supported
### help/?
Any command with help command involved will print the help message.

### ipmi
This is the command to redirect all of the command to ipmitool

### mac
get system mac command and print out the system mac we have
mac [index], index range from 0 to 5
for example: mac 0

### cpld
get CPLD information:
cpld [fw|cksum|id]
fw: get CPLD fw
cksum: get CPLD checksum
id: Get CPLD idcode

### me
Query ME related information.
me [version|cpu|dimm|io]
me version: to get ME version
me cpu: to get CPU utililization
me dimm: to get DIMM utililization
me io: to get IO utilization

### nic
get, set the BMC dedicate/share NIC
nic [dedicate|lom-share|mezz-share0|mizz-share1]

Return: <complete code> <LAN Card Type>
For LAN Card Type,
0h- BMC Dedicated
2h- Shared NIC (OCP Mezzanine slot)
3h- Shared NIC (QCT Mezzanine slot)

### service
eanble/disable Service commands:
service [enable/disable] [web|kvm|cd-media|hd-media|ssh|solssh]
Please notice this utility will get the service configuration data and
set the configuration data when set it. It do not guarantee that BMC has this feature.


## Test
To run the unit test command, use 'python3 -m unittest'

## Distribute the package
To generate the package, use 'pyinstaller qsmcli.py' to build the package.
