from os import system
import sys
import controllers.console_controller as controller


def get_value():
    str(input("Press any key to back : "))


def get_num(value):
    test_text = input(value)
    test_num = int(test_text)
    return test_num


def show_menu():
    print("1. ADD ")
    print("----------")
    print("2. EDIT ")
    print("----------")
    print("3. DELETE ")
    print("----------")
    print("4. PLANTS ")
    print("----------")
    print("5. EXIT   ")
    print("----------")


def show_days():
    print("Now you can choose days when to water a plant ->")
    print("1. Sunday")
    print("2. Monday")
    print("3. Tuesday")
    print("4. Wednesday")
    print("5. Thursday")
    print("6. Friday")
    print("7. Saturday")


def top_info(string):
    _ = system('clear')
    print(string)


def add_menu():
    top_info("Add a new plant -> ")
    plant_name = str(input("\nEnter the name of a plant : "))
    time = str(input("\nEnter the time to water : "))
    show_days()
    days_number = list(
        map(int, input("\nEnter the number of days when to water: ").split()))
    days = [__convert(number) for number in days_number]

    add(plant_name, time, days)


def edit_menu():
    top_info("Edit a chosen plant -> ")
    show_plants()
    item_to_edit = int(input("\nChoose what session to edit : "))
    time_to_edit = str(input("\nEnter new time : "))

    show_days()
    days_number = list(
        map(int, input("\nEnter the number of days when to water: ").split()))
    days = [__convert(number) for number in days_number]

    edit(item_to_edit, time_to_edit, days)


def del_menu():
    top_info("Delete a chosen watering plant -> ")
    show_plants()
    item_to_delete = int(input("\nChoose what session to delete : "))
    delete(item_to_delete)


def check_entered(number):
    if number == 1:
        add_menu()
    elif number == 2:
        edit_menu()
    elif number == 3:
        del_menu()
    elif number == 4:
        top_info("You can see all plants with watering info -> ")
        # plants
        show_plants()
    elif number == 5:
        sys.exit(0)
    else:
        _ = system('clear')
        show_menu()


def add(plant_name, time, days):
    print(controller.add(plant_name, time, days))
    print("\n<< New plant-watering ticket has been created! >>\n")


def edit(item_to_edit, time_to_edit, to_edit_days):
    controller.update(item_to_edit, time_to_edit, to_edit_days)
    print("\n<< Item has been successfully edited! >>\n")


def delete(item_to_delete):
    controller.delete(item_to_delete)
    print("\n<< Item has been successfully removed! >>\n")


def show_plants():
    info_list = controller.get_all()
    for info in info_list:
        print(info)


def __convert(number):
    if number == 1:
        return "Sunday"
    if number == 2:
        return "Monday"
    if number == 3:
        return "Tuesday"
    if number == 4:
        return "Wednesday"
    if number == 5:
        return "Thursday"
    if number == 6:
        return "Friday"
    if number == 7:
        return "Saturday"


while True:
    _ = system('clear')
    show_menu()
    num = get_num("Choose the task : ")
    check_entered(num)
    get_value()
