

class Turn(object):
    def __init__(self, year, month, day, hour, doctor, patient):
        self.Year = year
        self.Month = month
        self.Day = day
        self.Hour = hour
        self.Doctor = doctor
        self.Patient = patient
        patient.GetTurn(self.Doctor.Name + " " + self.Doctor.LastName)

