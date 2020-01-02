#!/usr/bin/env python
import visa
import time

ESCAPE_READ = '\n'
ESCAPE_WRITE = '\n'
QUERY_DELAY_SEC = .3
TIMEOUT_MS = 100
# NOTE: Replace <device-ID> with the IP of your device.
DEVICE_ADDRESS = 'TCPIP::<device-ID>::INST'

class DeviceManager:
		resourceManager = None
		session = None

		def __init__(self):
				try:
						self.resourceManager = visa.ResourceManager()
						self.session = self.resourceManager.open_resource(DEVICE_ADDRESS)
						self.session.query_delay = QUERY_DELAY_SEC
						self.session.read_termination = ESCAPE_READ
						self.session.timeout = TIMEOUT_MS
						self.session.write_termination = ESCAPE_WRITE
				except visa.Error as ex:
						self.dispose(ex)

		def query(self, command):
				try:
						global result 
						result = self.session.query(command)
						print(result)   
				except visa.Error as ex:
						self.dispose(ex)

		def dispose(self, ex = None):
			if not (self.session is None):
					self.session.clear()
					self.session.close()
			
			if not (self.resourceManager is None):
					self.resourceManager.close()

			if not (ex is None):
					# In most cases the error message will start with 'VI_ERROR_' 
					# (i.e VI_ERROR_SYSTEM_ERROR, VI_ERROR_ALLOC, ...)
					print(ex)