def display_data(input):

    input.seek(0)
    header = next(input).strip()
    print(header)
    
    counter = 0

    for line in input:
 
        counter += 1
        if counter <= 10:
            print(line.strip())
    print(f"There are {counter} total passengers")


def survival_rate(input):

    input.seek(0)
    next(input)


    pas_total = 0
    pas_survived = 0

    for line in input:
        split_line = line.strip().split(',')
        pas_total += 1
        if split_line[1] == '1':
            pas_survived += 1
    survive_rate = (pas_survived/pas_total)*100
    print(f"The survival rate was {survive_rate:.2f}%")

        



def gender_count(input):
    input.seek(0)

    with open('gendercount.csv', 'w') as output:

        next(input)


        male_count = 0
        fem_count = 0

        for line in input:
            split_line = line.strip().split(',')
       
            sex = split_line[5]
           
            if sex == "male":
                male_count += 1
            elif sex == "female":
                fem_count += 1
           
        output.write("Male" + "," + "Female")
        output.write("\n")
        output.write(str(male_count) + "," + str(fem_count))
            



def age_analysis(input):
    input.seek(0)

    with open('ageanalysis.csv', 'w') as output:

        next(input)


        male_count = 0
        fem_count = 0

        for line in input:
            split_line = line.strip().split(',')
       
            sex = split_line[5]
           
            if sex == "male":
                male_count += 1
            elif sex == "female":
                fem_count += 1
           
        output.write("Male" + "," + "Female")
        output.write("\n")
        output.write(str(male_count) + "," + str(fem_count))
    
    

def class_analysis(input):
    with open('classanalysis.csv', 'w') as output:  
        pass

        
        


def fam_survival():
    pass

def main():
    input = 'titanic.csv'
    with open(input, 'r') as input:
        display_data(input)
        survival_rate(input)
        gender_count(input)

main()








"""
Titanic Dataset Analysis - Starter Code
Student Name: Daniel Dominguez
Date: 12.11.25

Complete the functions below to analyze the Titanic dataset.
"""

def read_titanic_data(filename):
    """
    Reads the Titanic CSV file and returns the data as a list of lists.
    
    Args:
        filename (str): Path to the CSV file
    
    Returns:
        tuple: (headers, passengers) where headers is a list of column names
               and passengers is a list of lists containing passenger data
    """
    passengers = []
    headers = []
    
    try:
        # TODO: Open the file and read the data
        # Hint: First line is the header with column names
        # Each subsequent line is a passenger record
        pass
        
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return [], []
    
    return headers, passengers


def calculate_basic_stats(headers, passengers):
    """
    Calculates and displays basic statistics about the passengers.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records (each record is a list)
    """
    # TODO: Calculate total passengers, survivors, and survival rate
    # Hint: Find the index of 'Survived' column in headers
    total = 0
    survivors = 0
    
    print("=== BASIC STATISTICS ===")
    print(f"Total Passengers: {total}")
    print(f"Survivors: {survivors}")
    print(f"Survival Rate: {0.0:.1f}%")
    print()


def write_survivors(headers, passengers, output_file):
    """
    Writes information about all survivors to a file.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """
    # TODO: Write survivor information to file
    # Format: PassengerId,Name,Age,Class
    # Use headers to find the correct indices
    pass


def write_first_class(headers, passengers, output_file):
    """
    Writes information about first-class passengers to a file.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """
    # TODO: Filter first-class passengers and write to file
    # Include survival rate at the top
    pass


def write_children(headers, passengers, output_file):
    """
    Writes information about passengers under 18 to a file.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """
    # TODO: Filter passengers under 18 and write to file
    # Remember: some ages might be missing!
    pass


def generate_analysis_report(headers, passengers, output_file):
    """
    Generates a comprehensive analysis report.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """
    # TODO: Calculate survival rates by class and gender
    # TODO: Calculate average ages
    # TODO: Write formatted report to file
    pass

'''
def main():
    """
    Main function to run the analysis.
    """
    # Read the data
    print("Reading Titanic data...")
    headers, passengers = read_titanic_data("titanic.csv")
    
    if not passengers:
        print("Failed to load data. Exiting.")
        return
    
    print(f"Loaded {len(passengers)} passenger records.\n")
    
    # Part 1: Basic Statistics
    calculate_basic_stats(headers, passengers)
    
    # Part 2: Filter and Write Data
    print("Generating output files...")
    write_survivors(headers, passengers, "survivors.txt")
    write_first_class(headers, passengers, "first_class.txt")
    write_children(headers, passengers, "children.txt")
    
    # Part 3: Analysis Report
    generate_analysis_report(headers, passengers, "analysis_report.txt")
    
    print("Analysis complete! Check the output files.")


# Run the program
if __name__ == "__main__":
    main()


'''