import re
import csv

from File2Json import File2Json


class EmailContainer(object):
    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    def __init__(self, email):
        self.email = email

    def is_valid(self):
        valid = True
        if not re.match(self.regex, self.email):
            valid = False
        return valid


class ProcessFile(object):
    def __init__(self, file_path):
        self.data = File2Json(file_path).convert()

    def validate(self):

        for row in self.data:
            email = row["email"]
            row["valid"] = EmailContainer(email).is_valid()

    def get_report(self):
        data = filter(lambda row: not row["valid"], self.data)
        if len(data) > 0:
            with open('parsed.csv', 'w') as csvfile:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
        print "Successfully parsed csv!"



if __name__ == "__main__":
    fileName = "wh.csv"
    obj = ProcessFile(fileName)
    obj.validate()
    obj.get_report()
