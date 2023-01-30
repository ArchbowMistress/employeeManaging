from employeeClasses import Employee, Manager, Excecutive


def main():

    employee = Employee("John Smith", 45000)
    manager = Manager ("Jane Doe", 60000, "Widgets")
    excecutive = Excecutive("Weird Guy", 90000, "Thingies")

    print(employee)
    print(manager)
    print(excecutive)

main()