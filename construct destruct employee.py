class Employee:

    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("destructor called")

def object():
    print("Object making in progress...")
    obje= Employee()
    print("Ending function...")
    return obje

print("Calling object function...")
obje= object()
print("Endin program...")
