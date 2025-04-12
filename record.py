# record.py
# swe: ibraheem h. ali
# last updated: 12/4/25
# this module defines classes for managing medical records, including diagnoses and prescriptions.
# it provides a structure for storing and retrieving medical information related to patients.

class MedicalRecord:
    def __init__(self):
        self.diagnoses = []
        self.prescriptions = []

    def add_diagnosis(self, diagnosis):
        self.diagnoses.append(diagnosis)

    def add_prescription(self, prescription):
        self.prescriptions.append(prescription)

class Diagnosis:
    def __init__(self, description, doctor_name):
        self.description = description
        self.doctor_name = doctor_name

class Prescription:
    def __init__(self, medication, dosage, duration):
        self.medication = medication
        self.dosage = dosage
        self.duration = duration