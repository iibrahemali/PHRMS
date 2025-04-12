## swe: ibraheem h. ali
# last updated: 12/4/25
# this is the main entry point for the hospital management system
# initializes the system and demonstrates the functionality of various components.

from patient import Inpatient, Outpatient
from record import Diagnosis, Prescription
from staff import Doctor, Nurse, Admin

def main():
    # Placeholder for the main function
    # Initialize the hospital management system
    print("Welcome to the Hospital Management System")
    print("Initializing system...")
    # Create staff members
    doctor = Doctor("Wille", "9001WW")
    nurse = Nurse("Leon", "9001JJ")
    admin = Admin("Ibrahem", "SPECIAL1")

    print(doctor.perform_duty())
    print(nurse.perform_duty())
    print(admin.perform_duty())

    # Create patients
    inpatient = Inpatient("P001", "Leo Messi", 45, "Room 101")
    outpatient = Outpatient("P002", "Cris Ronaldo", 30, "2025-06-01")

    # Add medical data
    diagnosis = Diagnosis("Hypertension", doctor.name)
    prescription = Prescription("Lisinopril", "10mg", "30 days")

    inpatient.add_diagnosis(diagnosis)
    inpatient.add_prescription(prescription)

    # Output basic patient summary
    print(f"Inpatient: {inpatient.name}, Diagnoses: {[d.description for d in inpatient.medical_record.diagnoses]}")
    print(f"Prescriptions: {[p.medication for p in inpatient.medical_record.prescriptions]}")
    print(f"Outpatient: {outpatient.name}, Appointment Date: {outpatient.appointment_date}")

if __name__ == "__main__":
    main()