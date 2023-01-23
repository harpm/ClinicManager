from Classes.Turns import Turn

class Doctor(object):
    def __init__(self, name, lastName, proffesion):
        self.Name = name
        self.LastName = lastName
        self.Proffesion = proffesion
        self.PatientNumber = 0
        self.Patients = []
        self.Turns = []

    def GiveTurn(self, patient, year, month, day, hour):
        self.Patients.append(patient)
        NewTurn = Turn(year, month, day, hour, self, patient)
        self.Turns.append(NewTurn)
        self.PatientNumber += 1
        return NewTurn

    def FinishTurn(self, turn):
        self.Patients.append(turn.Patient)
        self.Turns.remove(turn)
        self.PatientNumber -= 1
