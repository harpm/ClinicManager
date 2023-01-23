from Classes import Doctors, Patients

if __name__ == '__main__':
    DrAli = Doctors.Doctor("Ali", "Mohammadi", "Brain")
    SaraTurn = DrAli.GiveTurn(Patients.Patient("Sara", "Goodarzi", 1273370555), 2022, 9, 5, 14)
    ZahraTurn = DrAli.GiveTurn(Patients.Patient("Zahra", "Hosseini", 1273380335), 2022, 11, 10, 10)

    DrZahra = Doctors.Doctor("Zahra", "Hamidi", "Skin and Hair")
    ArdalanTurn = DrZahra.GiveTurn(Patients.Patient("Ardalan", "Shojai", 10073370555), 2022, 8, 12, 16)
    ParsaTurn = DrZahra.GiveTurn(Patients.Patient("Parsa", "Mikelani", 8523380335), 2023, 1, 16, 18)


    print("2 Doctors and 4 Patients Added successfuly!")