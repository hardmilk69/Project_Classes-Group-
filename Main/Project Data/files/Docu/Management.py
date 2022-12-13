# Group 13
# Jean Pascua
# Justine Barredo
# Joe Paolini
# This Alberta Health Management System demonstrate the system inside a particular Hospital.
# With the help of this system, the management can see the Doctor's information along with their availability.
# It allows the management to add, edit, and search Doctors, Facilities, Laboratory, and Patients.
# The system has the ability to calculate the cost of your medical expenses.
# Only the management or authorized personnels can utilize the system because of its features.

# Classes
from Doctor import Doctor
from Facility import Facility
from Laboratory import Laboratory
from Patient import Patient

#  Display the categories, you can choose and access any of these categories by calling their respective classes and methods
class Management:

    def DisplayMenu(self):
        while True:
            menu = input("Welcome to Alberta Hospital (AH) Management system\n"
                         "Select from the following options, or select 0 to stop:\n"
                         "1 - 	Doctors\n"
                         "2 - 	Facilities\n"
                         "3 - 	Laboratories\n"
                         "4 - 	Patients\n")
# Class named "Doctor" will be call on this condition
            if menu == "1":
                while True:
                    doc = input("Doctors Menu:\n"
                                "1 - Display Doctors list\n"
                                "2 - Search for doctor by ID\n"
                                "3 - Search for doctor by name\n"
                                "4 - Add doctor\n"
                                "5 - Edit doctor info\n"
                                "6 - Back to the Main Menu\n")
                    if doc == "1":
                        Doctor().readDoctorsFile()
                        Doctor().displayDoctorsList()
                        print("\nBack to the previous Menu\n")
                    elif doc == "2":
                        Doctor().searchDoctorById()
                        Doctor().displayDoctorInfo()
                        print("\nBack to the previous Menu\n")
                    elif doc == "3":
                        Doctor().searchDoctorByName()
                        Doctor().displayDoctorInfo()
                        print("\nBack to the previous Menu\n")
                    elif doc == "4":
                        Doctor().addDrToFile()
                        print("\nBack to the previous Menu\n")
                    elif doc == "5":
                        Doctor().editDoctorInfo()
                        print("\nBack to the previous Menu\n")
                    else:
                        Management().DisplayMenu()
# Class named "Facility" will be call on this condition
            elif menu == "2":
                while True:
                    fac = input("Facilities Menu:\n"
                                "1 - Display Facilities list\n"
                                "2 - Add Facility\n"
                                "3 - Back to Main Menu\n")
                    if fac == "1":
                        Facility().displayFacilities()
                        print("\nBack to the previous Menu\n")
                    elif fac == "2":
                        Facility().addFacility()
                        print("\nBack to the previous Menu\n")
                    else:
                        Management().DisplayMenu()
#  Class named "Lab" will be call on this condition
            elif menu == "3":
                while True:
                    lab = input("Laboratories Menu\n"
                                "1 - Display laboratories list\n"
                                "2 - Add laboratory\n"
                                "3 - Back to the Main Menu\n")
                    if lab == "1":
                        Laboratory().readLaboratoriesFile()
                        Laboratory().displayLabsList()
                        print("\nBack to the previous Menu\n")
                    elif lab == "2":
                        Laboratory().addLabToFile()
                        print("\nBack to the previous Menu\n")
                    else:
                        Management().DisplayMenu()
#  Class named "Patient" will be call on this condition
            elif menu == "4":
                while True:
                    pat = input("Patients Menu:\n"
                                "1 - Display patients list\n"
                                "2 - Search for patient by ID\n"
                                "3 - Add patient\n"
                                "4 - Edit patient info\n"
                                "5 - Back to the Main Menu\n")
                    if pat == "1":
                        Patient().readPatientFile()
                        Patient().displayPatientList()
                        print("\nBack to the previous Menu\n")
                    elif pat == "2":
                        Patient().searchPatientById()
                        Patient().displayPatientInfo()
                        print("\nBack to the previous Menu\n")
                    elif pat == "3":
                        Patient().addPatientToFile()
                        print("\nBack to the previous Menu\n")
                    elif pat == "4":
                        Patient().editPatientInfo()
                        print("\nBack to the previous Menu\n")
                    else:
                        Management().DisplayMenu()
            elif menu == "0":
                exit()


Management().DisplayMenu()