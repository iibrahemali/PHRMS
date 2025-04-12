# patient.py
# swe: ibraheem h. ali
# last updated: 12/4/25
# this module defines the Patient class and its subclasses Inpatient and Outpatient
# the patient class manages patient information and medical records
# it also includes methods for adding diagnoses and prescriptions

from record import MedicalRecord

class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.medical_record = MedicalRecord()

    def add_diagnosis(self, diagnosis):
        self.medical_record.add_diagnosis(diagnosis)

    def add_prescription(self, prescription):
        self.medical_record.add_prescription(prescription)

class Inpatient(Patient):
    def __init__(self, patient_id, name, age, room_number):
        super().__init__(patient_id, name, age)
        self.room_number = room_number

class Outpatient(Patient):
    def __init__(self, patient_id, name, age, appointment_date):
        super().__init__(patient_id, name, age)
        self.appointment_date = appointment_date
