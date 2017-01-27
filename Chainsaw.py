from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlite3
import traceback

from chainsaw_db import Contestant
from base import Base


engine = create_engine('sqlite:///chainsaw_db.db', echo=False)

Base.metadata.create_all(engine) # Create a table for all the classes that use Base

# Need a Session to talk to the database.
# A session manages mappings of objects to rows in the database.
# Make a Session class. Only need to do this one time.
Session = sessionmaker(bind=engine)   #Use the engine created earlier



def add_record():

    name = input("Enter the name of the contestant: ")
    country = input("Enter the country of the contestant: ")
    catches = int(input("How many catches did they make: "))

    record = Contestant(name = name, country = country, catches = catches)

    add_contestant = Session()

    add_contestant.add(record)
    add_contestant.commit()
    add_contestant.close()

    #
    # cursor.execute('INSERT INTO Record_Holders VALUES (? , ? , ?)', (name, country, catches))
    # db.commit()


def delete_record():


    name = input("Enter the name of the contestant: ")

    delete_contestant = Session()

    results = delete_contestant.query(Contestant).filter(Contestant.name == name).one_or_none()

    delete_contestant.delete(results)
    delete_contestant.commit()
    delete_contestant.close()


def update_record():

    name = input("Enter the name of the contestant: ")
    column = input("Do you want to update CATCHES or COUNTRY: ")

    update_contestant = Session()


    if column == "catches":

        new_value = int(input("How may catches did they make: "))

        person = update_contestant.query(Contestant).filter(Contestant.name == name).one_or_none()
        person.catches = new_value

        update_contestant.commit()
        update_contestant.close()


    elif column == "country":

        new_value = input("What country are they from: ")

        person = update_contestant.query(Contestant).filter(Contestant.name == name).one_or_none()
        person.catches = new_value

        update_contestant.commit()
        update_contestant.close()


    else:

        print("not a valid entry")


def display_table():

    display = Session()

    for contestant in display.query(Contestant):
        print(contestant)

    display.close()


def display_menu(): # Displays menu

    print('''

        1. Display table
        2. Add new record
        3. Delete record
        4. Update record
        q. Quit
    ''')

    choice = input("Please make a selection: ")

    return choice




def handle_choice(choice): # Handles choices to clean up code.

    if choice == 1:

        display_table()

    elif choice == 2:

        add_record()

    elif choice == 3:

        delete_record()

    elif choice == 4:

        update_record()

    else:

        print("not a valid choice")


def main():


    print("Welcome to the Chainsaw Juggling Program!")

    # Infite loop till User enters "q"
    while True:

        choice = display_menu()

        if choice == "q":

            print("Thank you.")
            break

        elif choice.isdigit():
            handle_choice(int(choice))

        else:
            print("Not a valid choice")







main()
