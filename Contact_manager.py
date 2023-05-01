import json

# Function to fetch contact data for a given name
def fetch_contact():
    contacts_file = 'contacts.json'
    with open(contacts_file) as f:
        data = json.load(f)
        name_input = input("Enter Name: ")
        # Iterate over contacts and print email for given name
        for contact in data['contacts']:
            if contact['name'] == name_input:
                print("Name: ", contact['name'])
                print("Email: ", contact['email'])
                return
        # If name not found, print error message
        print("Error: No data found for the given name.")

# Function to print all contact data
def print_contacts():
    contacts_file = 'contacts.json'
    with open(contacts_file) as f:
        data = json.load(f)
        # Iterate over all contacts and print name and email
        for contact in data['contacts']:
            print("Name: ", contact['name'])
            print("Email: ", contact['email'])

# Function to update contact data
def update_contact():
    contacts_file = 'contacts.json'
    with open(contacts_file, 'r+') as f:
        data = json.load(f)
        name_input = input("Enter Name: ")
        email_input = input("Enter Email: ")
        # Check if input is not empty
        if name_input and email_input:
            entry = {"name": name_input, "email": email_input}
            # Append new entry to contacts list
            data['contacts'].append(entry)
            # Move file pointer to beginning of file
            f.seek(0)
            # Write updated data to file
            json.dump(data, f, indent=2)
            print("Data updated successfully.")
            print("Updated contact list:")
            f.close()
            print_contacts()
        else:
            print("Error: Invalid input.")

# Main loop to prompt user for input
while True:
    print("Command List:")
    print("1. Fetch Contact")
    print("2. Update Contact")
    print("3. Fetch All Contacts")
    command_input = input("Enter Command Number: ")
    if command_input == '1':
        fetch_contact()
    elif command_input == '2':
        update_contact()
    elif command_input == '3':
        print_contacts()
    else :
        print("Error: Invalid input.")