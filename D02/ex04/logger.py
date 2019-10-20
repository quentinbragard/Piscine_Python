import logging
from logging.handlers import RotatingFileHandler

import time
from random import randint

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('(%(name)s)Running: %(message)s')
file_handler = RotatingFileHandler('machine.log', 'a', 1000000, 1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class CoffeeMachine():
    water_level = 100
    def log(func):
        def wrapper_log(self, *args, **kwargs):
            starttime = time.time()
            res = func(self, *args, **kwargs)
            endtime = time.time()
            difftime = endtime - starttime
            logger.info(func.__name__.capitalize() + "   [ exec-time = " + str("%.3f" % difftime) + " ms ]")
            return res
        return wrapper_log

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())    
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
 
if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)