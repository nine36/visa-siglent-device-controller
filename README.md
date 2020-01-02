# VISA (Siglent) device controller

Simple script to query SCPI commands to set or read any device connected to 
a local network and that is capable of handling the SCPI. In my case I was using
a [Siglent](https://www.siglent.eu/) device.

## Prerequisites

In order to use the script you'll need to install the [VISA](https://pyvisa.readthedocs.io/en/latest/introduction/getting.html) library onto you machine.


## Test Environments

- Ubuntu 18.04
- Windows 10 Pro

## Getting Started

### Clone Repo

```
git clone git@github.com:nine36/visa-siglent-device-controller.git
```

### Run script

The example code will try to retrieve the device ID.

```
python index.py
```
