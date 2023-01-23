from Classes import Turns, Doctors

class Patient(object):
    def __init__(self, name, lastName, idNumber):
        self.Name = name
        self.LastName = lastName
        self.IdNumber = idNumber
        self.DoctorName = ""

    def GetTurn(self, doctorName):
        self.DoctorName = doctorName


