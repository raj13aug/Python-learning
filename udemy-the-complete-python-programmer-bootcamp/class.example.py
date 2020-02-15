class Patient(object):
    ''' Medical Bill'''
    status = 'Patient'
    def __init__(self, name, age):
        self.name = name
        self.age = age


patient = Patient('Nataraj', 32)
print(patient.name)
print(patient.age)
patient = Patient('vinoth', 35)
print(patient.name)
print(patient.age)

# We have instance variables that are created by the constructor we don't know what each instance is going to be called.

# Member every object in this class has irrespective 
