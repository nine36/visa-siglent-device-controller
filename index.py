#!/usr/bin/env python
from device_manager import DeviceManager

dm = DeviceManager()

dm.query('*IDN?')