from models.plant import Plant
from models.employee import Employee
from models.salon import Salon

class Controller:

    def menu(self):
        while True:
            print(
                "Choose a menu item by number: \n" +
                  "1. Add new Plant \n" +
                  "2. Add new Employee \n" +
                  "3. Get plant by id \n" +
                  "4. Get employee by id \n" +
                  "5. Add new Salon \n" +
                  "6. Get salon by id \n"
                  )
            break
        self.menu_flag = int(input("Your choose: "))

    def create_plant(self):
        if self.menu_flag == 1:
            self.id = int(input("ID: "))
            self.location = input("Location: ")
            self.name = input("Name: ")
            self.director_id = int(input("Director ID: "))
            plant = Plant(self.id, self.location, self.name, self.director_id)
            plant.save()

    def create_employee(self):
        if self.menu_flag == 2:
            self.id = int(input("ID: "))
            self.name = input("Name: ")
            self.email = input("Email: ")
            self.department_type = input("Department Type: ")
            self.department_id = int(input("Department id: "))
            self.salon = input("Enter salon: ")
            employee = Employee(self.id, self.name, self.email, self.department_type, self.department_id, self.salon)
            employee.save()

    def plant_id(self):
        if self.menu_flag == 3:
            self.id = int(input("ID: "))
            plant = Plant.get_by_id(self.id)
            print(plant)

    def employee_id(self):
        if self.menu_flag == 4:
            self.id = int(input("ID: "))
            employee = Employee.get_by_id(self.id)
            print(employee)

    def create_salon(self):
        if self.menu_flag == 5:
            self.id = int(input("ID: "))
            self.location = input("Location: ")
            self.name = input("Name: ")
            self.director_id = int(input("Director ID: "))
            salon = Salon(self.id, self.location, self.name, self.director_id)
            salon.save()

    def salon_id(self):
        if self.menu_flag == 6:
            self.id = int(input("ID: "))
            salon = Salon.get_by_id(self.id)
            print(salon)

    def run(self):
        c = Controller()
        c.menu()
        c.create_plant()
        c.create_employee()
        c.plant_id()
        c.employee_id()
        c.create_salon()
        c.salon_id()



