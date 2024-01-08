import mysql.connector
from prettytable import PrettyTable

# Your MySQL connection information
host = "127.0.0.1"
user = "root"
password = "********"
database = "*********"

# Connect to MySQL database using mysql-connector-python
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

def display():
    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()
    # Your SQL query
    query = "SELECT * FROM PATIENT_INFO"
    # Execute the query
    cursor.execute(query)
    # Fetch all the rows
    rows = cursor.fetchall()
    # Get the column names
    columns = [desc[0] for desc in cursor.description]
    # Create a PrettyTable
    table = PrettyTable(columns)
    # Add rows to the table
    for row in rows:
        table.add_row(row)
    print(table)
    
#USER INPUT
def options():
    print("Is there anything you would like to update in this Hospital Database?")
    print("1. Delete Patient Info")
    print("2. Change Patient Info")
    print("3. Add a Patient")
    print("4. None")
    ans = input("Type the number of your desired option here: ")
    if ans == "1":
        print("You chose option 1... To delete a patient's info.")
        IDN = input("Type the ID number of the patient you would like to delete here: ")
        cursor = connection.cursor()
        delete_query = "DELETE FROM PATIENT_INFO WHERE PatientID = %s"
        value_to_delete = IDN
        cursor.execute(delete_query, (value_to_delete,))
        connection.commit()
        display()
        options()
    elif ans == "2":
        print("You chose option 2... To edit the info of a patient.")
        IDN2 = input("Type the ID of the patient you would like to edit here: ")
        print("What would you like to change?")
        print(f'''
        1. Patient ID
        2. Last Name
        3. First Name
        4. Race
        5. Address
        6. City
        7. Age
        8. Illness
        9. Room number
        10. Gender
        ''')
        def change():
            req = input("Type the number of what you would like to change here: ")
            if req == "1":
                col = "PatientID"
                print("What would you like to change the patient ID to?")
                ANS = input("Type your answer here: ")
            elif req == "2":
                col = "LastName"
                print("What would you like to change the last name to?")
                ANS = input("Type your answer here: ")
            elif req == "3":
                col = "FirstName"
                print("What would you like to change the first name to?")
                ANS = input("Type your answer here: ")
            elif req == "4":
                col = "Race"
                print("What would you like to change the race to?")
                ANS = input("Type your answer here: ")
            elif req == "5":
                col = "Address"
                print("What would you like to change the address to?")
                ANS = input("Type your answer here: ")
            elif req == "6":
                col = "City"
                print("What would you like to change the city to?")
                ANS = input("Type your answer here: ")
            elif req == "7":
                col = "Age"
                print("What would you like to change the age to?")
                ANS = input("Type your answer here: ")
            elif req == "8":
                col = "Illness"
                print("What would you like to change the illness to?")
                ANS = input("Type your answer here: ")
            elif req == "9":
                col = "RMnum"
                print("What would you like to change the room number to?")
                ANS = input("Type your answer here: ")
            elif req == "10":
                col = "Gender"
                print("What would you like to change the gender to?")
                ANS = input("Type your answer here: ")
            else:
                print("Your input was invalid. Please try again.")
                change()
        cursor = connection.cursor()
        update_query = "UPDATE PATIENT_INFO SET " + col + " = %s WHERE PatientID = %s"
        new_value = ANS
        condition_value = IDN2
        cursor.execute(update_query, (new_value, condition_value))
        connection.commit()
        display()
        options()
    elif ans == "3":
        print("You chose option 3... To add a patient.")
        ID = input("Type the patient's ID number here: ")
        LAST = input("Type the patient's last name here: ")
        FIRST = input("Type the patient's first name here: ")
        RACE = input("Type the patient's race here: ")
        ADD = input("Type the patient's address here: ")
        CITY = input("Type the patient's city here: ")
        AGE = input("Type the patient's age here: ")
        ILL = input("Type the patient's illness here: ")
        RM = input("Type the patient's room number here: ")
        GEN = input("Type the patient's gender here: ")
        cursor = connection.cursor()
        insert_query = "INSERT INTO PATIENT_INFO (PatientID, LastName, FirstName, Race, Address, City, Age, Illness, RMnum, Gender) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        value1 = ID
        value2 = LAST
        value3 = FIRST
        value4 = RACE
        value5 = ADD
        value6 = CITY
        value7 = AGE
        value8 = ILL
        value9 = RM
        value10 = GEN
        cursor.execute(insert_query, (value1, value2, value3, value4, value5, value6, value7, value8, value9, value10))
        connection.commit()
        display()
        options()
    elif ans == "4":
        print("Thank you for using HP Management. Goodbye!")
        cursor = connection.cursor()
        # Close the cursor and connection
        cursor.close()
        connection.close()
    else:
        print("Your input was invalid. Please try again.")
        options()

# Print the table
display()
options()
