import os
import csv
import json


# Q1. College Information
def question1_college_info():
    filename = "college_info.txt"
    name = input("Enter college name: ")
    location = input("Enter college location: ")
    year = input("Enter establishment year: ")
    departments = input("Enter number of departments: ")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"College Name: {name}\n")
        file.write(f"Location: {location}\n")
        file.write(f"Establishment Year: {year}\n")
        file.write(f"Number of Departments: {departments}\n")

    print("\nCollege Information:")
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())


# Q2. Employee Records
def question2_employee_records():
    filename = "employee_records.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for i in range(5):
            print(f"\nEmployee {i + 1}")
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            department = input("Enter department: ")
            salary = input("Enter monthly salary: ")
            file.write(
                f"ID: {emp_id}, Name: {name}, Department: {department}, "
                f"Monthly Salary: {salary}\n"
            )

    print("\nEmployee Records:")
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())


# Q3. Shopping List (write 5, append 3)
def question3_shopping_list():
    filename = "shopping_list.txt"
    print("Enter 5 shopping items:")
    with open(filename, "w", encoding="utf-8") as file:
        for i in range(5):
            item = input(f"Item {i + 1}: ")
            file.write(item + "\n")

    print("\nEnter 3 more items to append:")
    with open(filename, "a", encoding="utf-8") as file:
        for i in range(3):
            item = input(f"Additional item {i + 1}: ")
            file.write(item + "\n")

    print("\nComplete Shopping List:")
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())


# Q4. Paragraph Analysis
def question4_paragraph_analysis():
    filename = "paragraph.txt"
    paragraph = input("Enter a paragraph:\n")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(paragraph)

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    print("\nParagraph Analysis")
    print("Characters:", len(content))
    print("Words:", len(content.split()))
    print("Lines:", len(content.splitlines()))


# Q5. Product Catalog Search
def question5_product_catalog():
    filename = "product_catalog.txt"
    print("Enter 10 product names:")
    with open(filename, "w", encoding="utf-8") as file:
        for i in range(10):
            product = input(f"Product {i + 1}: ")
            file.write(product + "\n")

    search_name = input("\nEnter product name to search: ").strip()
    with open(filename, "r", encoding="utf-8") as file:
        products = file.readlines()

    matches = [p.strip() for p in products if search_name.lower() in p.lower()]
    print("Matching products:")
    if matches:
        for product in matches:
            print(product)
    else:
        print("No matching product found.")
    print("Number of matches:", len(matches))


# Q6. Copy Notes File
def question6_copy_notes():
    source = "python_notes.txt"
    destination = "backup_notes.txt"

    if not os.path.exists(source):
        print(f"{source} was not found. Creating it now.")
        notes = input("Enter your Python notes:\n")
        with open(source, "w", encoding="utf-8") as file:
            file.write(notes)

    with open(source, "r", encoding="utf-8") as file:
        content = file.read()

    with open(destination, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Notes copied successfully to {destination}.")
    print("\nBackup content:")
    print(content)


# Q7. File Management Menu
def question7_file_management():
    while True:
        print("\n--- File Management Menu ---")
        print("1. Create and write a file")
        print("2. Read a file")
        print("3. Append to a file")
        print("4. Rename a file")
        print("5. Delete a file")
        print("6. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter file name: ")
            content = input("Enter content: ")
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)
            print("File created/written successfully.")

        elif choice == "2":
            filename = input("Enter file name: ")
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as file:
                    print("\n" + file.read())
            else:
                print("File not found.")

        elif choice == "3":
            filename = input("Enter file name: ")
            content = input("Enter content to append: ")
            with open(filename, "a", encoding="utf-8") as file:
                file.write(content + "\n")
            print("Content appended successfully.")

        elif choice == "4":
            old_name = input("Enter current file name: ")
            new_name = input("Enter new file name: ")
            if os.path.exists(old_name):
                if os.path.exists(new_name):
                    print("A file with the new name already exists.")
                else:
                    os.rename(old_name, new_name)
                    print("File renamed successfully.")
            else:
                print("File not found.")

        elif choice == "5":
            filename = input("Enter file name to delete: ")
            if os.path.exists(filename):
                os.remove(filename)
                print("File deleted successfully.")
            else:
                print("File not found.")

        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")


# Q8. Exam Result
def question8_exam_result():
    filename = "exam_result.txt"
    student_name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    marks = []
    for i in range(5):
        mark = float(input(f"Enter marks for subject {i + 1} (out of 100): "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / 5
    result = "PASS" if all(mark >= 40 for mark in marks) else "FAIL"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Student Name: {student_name}\n")
        file.write(f"Roll Number: {roll}\n")
        for i, mark in enumerate(marks, start=1):
            file.write(f"Subject {i}: {mark}\n")
        file.write(f"Total Marks: {total}\n")
        file.write(f"Percentage: {percentage:.2f}%\n")
        file.write(f"Result: {result}\n")

    print("\nExam Result:")
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())


# Q9. Product Inventory CSV
def question9_product_inventory():
    filename = "inventory.csv"
    fields = ["Product ID", "Product Name", "Category", "Price", "Quantity"]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

        for i in range(5):
            print(f"\nProduct {i + 1}")
            row = {
                "Product ID": input("Enter product ID: "),
                "Product Name": input("Enter product name: "),
                "Category": input("Enter category: "),
                "Price": input("Enter price: "),
                "Quantity": input("Enter quantity: ")
            }
            writer.writerow(row)

    print("\nProduct Inventory:")
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


# Q10. Patient Information JSON
def question10_patient_information():
    filename = "patient_info.json"
    patient = {
        "patient_id": input("Enter patient ID: "),
        "name": input("Enter patient name: "),
        "age": input("Enter patient age: "),
        "disease": input("Enter disease: "),
        "doctor": input("Enter doctor name: ")
    }

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(patient, file, indent=4)

    with open(filename, "r", encoding="utf-8") as file:
        saved_patient = json.load(file)

    print("\nPatient Information:")
    print(json.dumps(saved_patient, indent=4))


# Q11. Electricity Units for 10 Households
def question11_electricity_units():
    filename = "electricity_units.txt"
    units = []

    with open(filename, "w", encoding="utf-8") as file:
        for i in range(10):
            value = float(input(f"Enter electricity units for household {i + 1}: "))
            units.append(value)
            file.write(f"Household {i + 1}: {value}\n")

    total = sum(units)
    highest = max(units)
    lowest = min(units)
    average = total / len(units)

    print("\nElectricity Report")
    print("Total units:", total)
    print("Highest units:", highest)
    print("Lowest units:", lowest)
    print("Average units:", average)


# Q12. Simple User Login (classroom practice only)
def question12_user_login():
    filename = "account_details.txt"
    username = input("Create username: ")
    email = input("Enter email: ")
    password = input("Create password: ")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"{username}\n{email}\n{password}\n")

    print("\nAccount created. Please log in.")
    login_username = input("Enter username: ")
    login_password = input("Enter password: ")

    with open(filename, "r", encoding="utf-8") as file:
        saved_username = file.readline().strip()
        saved_email = file.readline().strip()
        saved_password = file.readline().strip()

    if login_username == saved_username and login_password == saved_password:
        print("Login successful!")
        print("Email:", saved_email)
    else:
        print("Invalid username or password.")

    print("Note: Plain-text password storage is for classroom practice only, not real applications.")


def main():
    while True:
        print("\n========== FILE HANDLING PRACTICE ==========")
        print("1. College Information")
        print("2. Employee Records")
        print("3. Shopping List")
        print("4. Paragraph Analysis")
        print("5. Product Catalog")
        print("6. Copy Notes File")
        print("7. File Management Menu")
        print("8. Exam Result")
        print("9. Product Inventory (CSV)")
        print("10. Patient Information (JSON)")
        print("11. Electricity Units")
        print("12. User Login")
        print("13. Exit")

        choice = input("Choose question (1-13): ")

        functions = {
            "1": question1_college_info,
            "2": question2_employee_records,
            "3": question3_shopping_list,
            "4": question4_paragraph_analysis,
            "5": question5_product_catalog,
            "6": question6_copy_notes,
            "7": question7_file_management,
            "8": question8_exam_result,
            "9": question9_product_inventory,
            "10": question10_patient_information,
            "11": question11_electricity_units,
            "12": question12_user_login
        }

        if choice == "13":
            print("Thank you! Program ended.")
            break
        elif choice in functions:
            try:
                functions[choice]()
            except ValueError:
                print("Invalid number entered. Please try again.")
            except OSError as error:
                print("File error:", error)
        else:
            print("Invalid choice. Please enter a number from 1 to 13.")


if __name__ == "__main__":
    main()
