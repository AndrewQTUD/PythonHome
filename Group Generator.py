import re

def add_dash_to_email(names):
    # Define a regex pattern to match the email addresses in each line
    email_pattern = r'([\w.%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7})'
    
    # Create a list to store modified names with dash before email
    modified_names = []
    
    # Iterate over each name and email string
    for name in names:
        # Use regex to find the email address in the name string
        match = re.search(email_pattern, name)
        if match:
            email = match.group(0)
            # Replace the email address with a dash-prefixed email address
            modified_email = '- ' + email
            modified_name = name.replace(email, modified_email)
            modified_names.append(modified_name)
        else:
            # If no email is found, append the name as is
            modified_names.append(name)
    
    return modified_names
    
def read_names_from_file(filename):
    with open(filename, 'r') as file:
        names = [line.strip() for line in file.readlines()]
    return names    

def divide_into_groups_sequentially(names):
    # Calculate the number of names per group
    num_groups = 10
    names_per_group, remainder = divmod(len(names), num_groups)
    
    # Divide names into groups sequentially
    groups = [names[i*names_per_group:(i+1)*names_per_group] for i in range(num_groups)]
    
    # Distribute remaining names to the last group
    for i, name in enumerate(names[num_groups*names_per_group:]):
        groups[i % num_groups].append(name)
    
    return groups

# Example usage
if __name__ == "__main__":
    # File containing the list of names
    filename = 'names.txt'
    
    # Read names from file
    names = read_names_from_file(filename)
    
    # Divide names into groups sequentially
    groups = divide_into_groups_sequentially(names)
    
    # Process each group to add dash before email address
    for i, group in enumerate(groups):
        groups[i] = add_dash_to_email(group)
    
    # Print groups to terminal
    for i, group in enumerate(groups):
        print(f"Group {i+1}:")
        print('\n'.join(group))
        print('-' * 20)  # Separate groups by a line of dashes
