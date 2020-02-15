class Patient(object):
    ''' Medical Bill'''
    status = 'Patient'             # class variable
    def __init__(self, name, age):     # instance variable
        self.name = name
        self.age = age


patient = Patient('Nataraj', 32)
print(patient.name)
print(patient.age)
print(patient.status)
patient = Patient('vinoth', 35)
print(patient.name)
print(patient.age)
print(patient.status)

# We have instance variables that are created by the constructor we don't know what each instance is going to be called.

# Member every object in this class has irrespective 
