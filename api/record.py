import csv
from api import app
from datetime import datetime

def Receive_Feedback(data: dict):

    if "CreationTime" not in data.keys():
        now = datetime.now()
        data["CreationTime"] = now.strftime("%Y-%m-%d %H:%M:%S")

    # Open the CSV file in append mode
    with open(app.config["FILENAME"], mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=app.config["FIELDNAMES"])

        # Write the header if the file is empty
        if file.tell() == 0:
            writer.writeheader()

        while len(data['Components']) != 6:
            data['Components'].insert(0, "null")

        # Flatten the 'Components' list into a string for CSV
        data['Components'] = ', '.join(data['Components'])
        print(data)

        # Write the data to the CSV file
        writer.writerow(data)