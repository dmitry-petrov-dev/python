# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
# уроках по ООП.


from time import sleep


class Warehouse:
    def __init__(self, id='000', name='Office Equipment Warehouse'):
        self.id = id
        self.name = name
        self._warehouse_stock = {}
        self._total = 0

    def receive_to_warehouse(self, device_type, device):
        self._total += 1
        if len(self._warehouse_stock) != 0:
            max_id = list(self._warehouse_stock.keys())[-1] + 1
        else:
            max_id = 1
        self._warehouse_stock[max_id] = [device_type, device]
        print(f'\033[31m{self.name}\033[0m received {device}')

    def transfer_to_office(self, device_id, office):
        try:
            device = self._warehouse_stock.pop(device_id)
            office.receive_to_office(device[0], device[1])
            self._total -= 1
            print(f"\033[32mDevice ID {device[1]} transferred to Office\033[0m")
        except KeyError:
            print(f"\033[31mDevice ID {device_id} not found\033[0m")

    @property
    def current_stock(self):
        stock_list = []
        for key, value in self._warehouse_stock.items():
            stock_list.append(f'+ID: {key} Device Type: {value[0]} Name: {value[1]}')
        if len(stock_list) == 0:
            return f'Warehouse {self.name} has no devices'
        return f'Warehouse \033[31m{self.name}\033[0m has next devices:\n' + '\n'.join(
            stock_list) + f'\nTotal items: \033[34m{self._total}\033[0m\n'

    def print_device_data(self):
        stock_list = []
        for value in self._warehouse_stock.items():
            device = value[1].pop()
            stock_list.append(device.get_full_data())
        if len(stock_list) == 0:
            return f'Warehouse {self.name} has no devices'
        return f'Warehouse \033[31m{self.name}\033[0m has next devices:\n' + '\n'.join(
            stock_list) + f'\nTotal items: \033[34m{self._total}\033[0m\n'


class OfficeEquipment:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'{self.brand} {self.model}'

    @staticmethod
    def get_full_data():
        pass


class Printer(OfficeEquipment):
    def __init__(self, brand, model, printer_type='Laser', print_color=True):
        self.printer_type = printer_type
        self.print_color = print_color
        super().__init__(brand, model)

    def get_full_data(self):
        return f'{self.brand} {self.model}: Printer type: {self.printer_type}; Color: {self.print_color}'


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, resolution, depth='48bit'):
        self.resolution = resolution
        self.depth = depth
        super().__init__(brand, model)

    def get_full_data(self):
        return f'{self.brand} {self.model}: Resolution: {self.resolution}; Depth: {self.depth}'


class Copier(OfficeEquipment):
    def __init__(self, brand, model, print_color=False, auto_feeder=False):
        self.print_color = print_color
        self.auto_feeder = auto_feeder
        super().__init__(brand, model)

    def get_full_data(self):
        return f'{self.brand} {self.model}: Print color: {self.print_color}; Auto feeder: {self.auto_feeder}'


class Office:
    def __init__(self, id='000', name='MY OFFICE'):
        self.id = id
        self.name = name
        self._office_stock = {}
        self._total = 0

    def receive_to_office(self, device_type, device):
        self._total += 1
        if len(self._office_stock) != 0:
            max_id = list(self._office_stock.keys())[-1] + 1
        else:
            max_id = 1
        self._office_stock[max_id] = [device_type, device]

    def return_to_warehouse(self, position, warehouse):
        try:
            device = self._office_stock.pop(position)
            warehouse.receive_to_warehouse(device[0], device[1])
            self._total -= 1
            print(f"\033[32mDevice ID {device[1]} returned to Warehouse\033[0m")
        except KeyError:
            print(f"\033[31mDevice ID {position} not found\033[0m")

    @property
    def devices(self):
        devices_list = []
        for key, value in self._office_stock.items():
            devices_list.append(f'{key}. {value[0]}. {value[1]}')
        if len(devices_list) == 0:
            return f'Office {self.name} has no devices'
        return f'Office {self.name} has next devices:\n' + '\n'.join(devices_list)


def print_main_menu():
    print("\033[1m************* Main Menu *************")
    print("1. Add new device to warehouse")
    print("2. Get current warehouse stock")
    print("3. Transfer device to Office")
    print("4. Return device to Warehouse")
    print("5. Get full device information")
    print("Q. Press Q for quit")


def print_device_type():
    print("Choose device type")
    print("1. Printer")
    print("2. Scanner")
    print("3. Copier")


# MAIN PROGRAM
print("Welcome to My Mini Warehouse Program")
print("Initializing...Please wait")
sleep(1)
warehouse_1 = Warehouse('MMW')
sleep(0.5)
print(f"Warehouse {warehouse_1.name} created")
sleep(0.5)
print(f"Stock initializing ...")
sleep(0.5)
warehouse_1.receive_to_warehouse('Printer', Printer('HP', 'Laserjet 100'))
sleep(0.5)
warehouse_1.receive_to_warehouse('Printer', Printer('Canon', 'Pixma MG2545S', 'Jet', True))
sleep(0.5)
warehouse_1.receive_to_warehouse('Scanner', Scanner('Canon', 'CanoScan LiDE 300', '2400x2400'))
sleep(0.5)
print(f"Stock initialized for warehouse {warehouse_1.name}")
sleep(0.5)
print(warehouse_1.current_stock)
sleep(0.5)
print(f"Office initializing ...")
office_1 = Office()
sleep(0.5)
print(office_1.devices)
while True:
    print_main_menu()

    selected_option = input("Please enter value 1..5 or press Q: \033[0m")
    if selected_option.upper() == 'Q':
        break
    elif selected_option.isdigit() and 0 < int(selected_option) < 6:
        if int(selected_option) == 1:
            while True:
                print("\033[1m************* Adding new device *************")
                print_device_type()
                try:
                    selected_option = int(input("Please enter value 1..3 or Press 0 to return Main Menu: \033[0m"))
                except ValueError:
                    selected_option = 100
                if selected_option == 0:
                    break
                elif 0 < int(selected_option) < 4:
                    add_brand = input("Enter brand name: ")
                    add_model = input("Enter model: ")
                    if selected_option == 1:
                        add_printer_type = input("Printer is Laser or Jet: ")
                        add_color = input("Printer color [True] or [False]: ")
                        if add_color == 'True':
                            add_color = True
                        else:
                            # in any other cases it is False
                            add_color = False
                        warehouse_1.receive_to_warehouse('Printer',
                                                         Printer(add_brand, add_model, add_printer_type, add_color))
                    elif selected_option == 2:
                        add_resolution = input("Scanner resolution: ")
                        add_depth = input("Depth: ")
                        warehouse_1.receive_to_warehouse('Scanner',
                                                         Scanner(add_brand, add_model, add_resolution, add_depth))
                    else:
                        add_print_color = input("Copier is color [True] or [False]: ")
                        if add_print_color == 'True':
                            add_print_color = True
                        else:
                            # in any other cases it is False
                            add_print_color = False
                        add_auto_feeder = input("Auto feeder [True] or [False]: ")
                        if add_auto_feeder == 'True':
                            add_auto_feeder = True
                        else:
                            # in any other cases it is False
                            add_auto_feeder = False
                        warehouse_1.receive_to_warehouse('Copier',
                                                         Copier(add_brand, add_model, add_print_color, add_auto_feeder))
                else:
                    print("\033[31mYou entered invalid value. Please enter again\033[0m")
                    sleep(1)
        elif int(selected_option) == 2:
            print(warehouse_1.current_stock)
            sleep(1)
        elif int(selected_option) == 3:
            print("\033[1m************* Transfer device to Office *************\033[0m")
            print(warehouse_1.current_stock)
            selected_option = int(input("Choose Device Id for transfer to the Office or Press 0 to return Main Menu: "))
            if selected_option != 0:
                warehouse_1.transfer_to_office(selected_option, office_1)

        elif int(selected_option) == 4:
            print("\033[1m************* Return device to Warehouse *************\033[0m")
            print(office_1.devices)
            selected_option = int(input("Choose number of device or Press 0 to return Main Menu: "))
            if selected_option != 0:
                office_1.return_to_warehouse(selected_option, warehouse_1)
        elif int(selected_option) == 5:
            print("\033[1m************* Device information *************")
            print(warehouse_1.print_device_data())
            sleep(1)
    else:
        print("\033[31mYou entered invalid value. Please enter again\033[0m")
        sleep(1)
