class Patient(object):
    ''' Medical Bill'''

    def __init__(self, name, age):
        self.name = name
        self.age = age


patient = Patient('Nataraj', 32)
print(patient.name)
print(patient.age)
patient = Patient('vinoth', 35)
print(patient.name)
print(patient.age)
