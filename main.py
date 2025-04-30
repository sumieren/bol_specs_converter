import csv, sys


def main():
    # check if a single file was input
    if len(sys.argv) == 1:
        raise Exception("no file provided")
    if len(sys.argv) > 2:
        raise Exception("too many arguments provided")

    # import the csv
    try:
        csv_file = open(sys.argv[1], "r")
        csv_reader = csv.reader(csv_file, delimiter=',')
    except:
        print("Exception occurred, did you save the csv in unicode?")

    for row in csv_reader:
        print(row)



main()