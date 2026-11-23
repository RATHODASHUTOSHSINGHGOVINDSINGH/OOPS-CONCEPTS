class Patient:
    def __init__(self, diagnosis):
        self.__diagnosis = diagnosis

    def update_diagnosis(self, value):
        if value:
            self.__diagnosis = value
            print("Updated diagnosis:", self.__diagnosis)
        else:
            print("Invalid diagnosis")
patient = Patient("Fever")
patient.update_diagnosis("Viral Infection")