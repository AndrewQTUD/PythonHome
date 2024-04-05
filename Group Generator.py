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

def read_names_from_file(filename):
    with open(filename, 'r') as file:
        names = [line.strip() for line in file.readlines()]
    return names

if __name__ == "__main__":
    # File containing the list of names
    filename = 'names.txt'
    
    # Read names from file
    names = read_names_from_file(filename)
    
    # Divide names into groups sequentially
    groups = divide_into_groups_sequentially(names)
    
    # Print groups to terminal
    for i, group in enumerate(groups):
        print(f"Group {i+1}:")
        print('\n'.join(group))
        print('-' * 20)  # Separate groups by a line of dashes
