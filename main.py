import argparse
import csv
import pandas

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", help="set new account")
    parser.add_argument("-d", help="delete existing account")
    parser.add_argument("-r", help="read existing account")
    parser.add_argument("-l", required=False, help="print out all accounts")
    args = parser.parse_args()

    if args.w:
        title = args.w
        new_account(title)

    elif args.r:
        title = args.r
        read_account(title)

    elif args.l:
        read_file()

    elif args.d:
        title = args.d
        delete_file(title)

def delete_file(text):
    with open("accounts.csv", "r") as f:
        reader = csv.reader(f)
        count = -1
        for row in reader:
            if text in row:
                break
            count += 1
        try:
            df = pandas.read_csv('accounts.csv')
            df = df.drop(int(count))
            df.to_csv('accounts.csv', index=False)
        except:
            print("Invalid account")
def read_file():
    with open("accounts.csv", "r") as f:
        reader = csv.reader(f)
        for line in reader:
            print(line)

def read_account(text):
    with open("accounts.csv", "r") as f:
        reader = csv.reader(f)
        #each loop it checks for the key and if its found count turns into 1 which prevents the error message at the end of the loop
        count = 0
        for line in reader:
            if text in line:
                print(f"Account:{line[0]}\n\nUsername:{line[1]}\nPassword:{line[2]}")
                count = 1
        if count == 0:
            print("Invalid account. Use -l to see a list of all accounts")


def new_account(text):
    #gets user input for new account
    username = input("Username: ")
    password = input("Password: ")
    data = [text,username,password]

    with open("accounts.csv", "a", newline="\n") as file:
        writer = csv.writer(file)
        writer.writerow(data)

    print("Account added successfully!")

if __name__ == "__main__":
    main()