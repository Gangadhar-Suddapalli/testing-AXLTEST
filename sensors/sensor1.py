import eventlet
import os
import hashlib
from st2reactor.sensor.base import Sensor
class HelloSensor(Sensor):
    def __init__(self, sensor_service, config):
        super(HelloSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._stop = False
        self._pre = ''
    def setup(self):
        pass
    def calculate_file_hash(self):
         with open('/home/osboxes/data.txt', 'r') as file:
             file_content = file.readlines()
             return file_content
    def run(self):
        while not self._stop:
            curr = self.calculate_file_hash()
            #if curr != self._pre:
            #    payload = {
             #       "status": "Changes detected in data.txt",
              #      "before": self._pre,
               #     "after": curr
               # }
               # self.sensor_service.dispatch(trigger="testing.event1", payload=payload)
           # else:
            #    payload = {"status": "No changes detected in data.txt"}
             #   self.sensor_service.dispatch(trigger="testing.event1", payload=payload)
           # self._pre = curr
           # eventlet.sleep(30)

            if curr != self._pre:
                payload = {"greeting": "Yo, StackStorm!", "count": "hi","before":self._pre,"after":curr}
                self.sensor_service.dispatch(trigger="testing.event1", payload=payload)
            else :
                #payload = {"greeting": "Yo, StackStorm!", "count": "hi","cwd":"no changes are made"}
                #self.sensor_service.dispatch(trigger="testing.event1", payload=payload)
                self._logger.debug("No changes detected in file 'data.txt'.")
            self._pre = curr
            eventlet.sleep(30)
    def cleanup(self):
        self._stop = True
    def add_trigger(self, trigger):
        pass
    def update_trigger(self, trigger):
        pass
    def remove_trigger(self, trigger):
        pass
	
