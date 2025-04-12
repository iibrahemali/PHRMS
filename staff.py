# staff.py
# # swe: ibraheem h. ali
# # last updated: 12/4/25
# # this module defines the Staff class and its subclasses Doctor, Nurse, and Admin # # 
# # the staff class manages staff information and their duties # #
# # it also includes methods for performing specific duties related to their roles # #

from abc import ABC, abstractmethod

class Staff(ABC):
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id

    @abstractmethod
    def perform_duty(self):
        pass

class Doctor(Staff):
    def perform_duty(self):
        return f"Doctor {self.name} is diagnosing patients."

class Nurse(Staff):
    def perform_duty(self):
        return f"Nurse {self.name} is assisting with patient care."

class Admin(Staff):
    def perform_duty(self):
        return f"Admin {self.name} is managing hospital data."