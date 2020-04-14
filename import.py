import csv

from cs50 import SQL
from sys import argv

def main():
    # Check if the user provided the correct number of cmd-line args
    if len(argv) != 2:
        print("Usage: python import.py tips.csv")
        return 1
    # connect to the database
    db = SQL("sqlite:///covid19.db")
    # open the csv file in readmode and close automatically thanks to with statement
    with open(argv[1], 'r', newline='') as f:
        # read the file as dict where the keys are the column names and values are the row values and store it in reader
        reader = csv.DictReader(f)
        # iterate over every row(line) in reader and insert every row into the tips table
        for row in reader:
            # check if the tip already exist
            tip_check = db.execute("SELECT * FROM 'tips' WHERE id = :id", id=row['id'])
            # if so continue don't insert it
            if tip_check:
                continue
            # otherwise insert the new tip
            db.execute("INSERT INTO 'tips' (id, tip) VALUES (:id, :tip)", id=row['id'], tip=row['tip']);


if __name__ == "__main__":
    main()