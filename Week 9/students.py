import csv

def main():
    STUDENT_NUM_INDEX = 0
    NAME_INDEX = 1

    students_dict = read_dict('students.csv', STUDENT_NUM_INDEX)

    inumber = input("Please Enter your I-Number(xx-xxx-xxxx): ")

    inumber = inumber.replace("-", "")

    if not inumber.isdigit():
        print("Invalid I-Number: Invalid Input")
    else:
        if len(inumber) < 9:
            print("Invalid I-Number: Not Enough Digits")
        elif len(inumber) > 9:
            print("Invalid I-Number: Too Much Digits")
        else:
            if inumber not in students_dict:
                print("No Student With That I-Number")
            else:
                value = students_dict[inumber]
                name = value[NAME_INDEX]
                print(name)

def read_dict(filename, STUDENT_KEY):
    students = {}
    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)

        for list in reader:
            key = list[STUDENT_KEY]
            students[key] = list

    return students



if __name__ == "__main__":
    main()