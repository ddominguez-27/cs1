
"""
Titanic Dataset Analysis
Author: Daniel Dominguez
Date: 1/22/25
Sources: Mr. Campbell, assignment instruction
Description: Prompts the user to select from different options to analyze a specific dataset related to the titanic
Completed functions: 1-6s
Log: 1.2

"""



"""
Args:
    input (file)
Return:
    n/a


Description:
    Prints the header, then the first 10 rows of the dataset and then the total number of passengers
"""
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

#Args: input (file)
#Return: n/a
#Description: calculates then prints the overall surival rate

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
    print(f"The overall survival rate was {survive_rate:.2f}%")

        


"""
Args:
    input (file)
Return:
    n/a

Description: calculates male and female survival rate, and determines which is larger, writes info to csv
"""
def gender_analysis(input):


    input.seek(0)
    next(input)

    with open('gender_analysis.csv', 'w') as output:

        male_count = 0
        msurvived_count = 0
        fem_count = 0
        fsurvived_count = 0

        for line in input:
            split_line = line.strip().split(',')
       
            sex = split_line[5]
           
            if sex == "male":
                male_count += 1
                if split_line[1] == "1":
                    msurvived_count += 1
            elif sex == "female":
                fem_count += 1
                if split_line[1] == "1":
                    fsurvived_count += 1

        msurvival_rate = round((msurvived_count/male_count), 4)*100
        fsurvival_rate = round((fsurvived_count/fem_count), 4)*100

        if msurvival_rate > fsurvival_rate:
            print(f"The gender with the highest survival rate was Males with a survival rate of {msurvival_rate}%")
        elif fsurvival_rate > msurvival_rate:
            print(f"The gender with the highest survival rate was Females with a survival rate of {fsurvival_rate}%")
           
        output.write("Male" + "," + "Male Survival Rate" + "," + "Female" + "," + "Female Survival Rate")
        output.write("\n")
        output.write(str(male_count) + "," + str(msurvival_rate) + "," + str(fem_count) + "," + str(fsurvival_rate))
            



"""
Args:
    input (file)
Return:
    n/a

Description: calculates average age of total passengers and survivors and non survivors, finds oldest and youngest person in the data set, writes info to csv
"""
def age_analysis(input):

    input.seek(0)
    next(input)


    with open('ageanalysis.csv', 'w') as output:


        age_total = 0
        passenger_count = 0

        age_lowest = 1000   #upper bound that passenger is unlikely to have
        age_greatest = 0

        nonsurvivor_count = 0
        nonsurvivor_age = 0

        oldest_pas = []
        oldest_age = []
        youngest_pas = []
        youngest_age = []






        for line in input:
            split_line = line.strip().split(',')
       
            age = split_line[6]
            if len(age) == 0:   #skips line if age was left blanks
                continue
            age = float(age)
            survived = split_line[1]
            

            
            age_total += age
            passenger_count += 1

            if age >= age_greatest:
                age_greatest = age
                name = split_line[3] + split_line[4]
                oldest_pas.append(name)
                oldest_age.append(age)

            if age <= age_lowest:
                age_lowest = age
                name = split_line[3] + split_line[4]
                youngest_pas.append(name)
                youngest_age.append(age)
            if survived == "0":
                nonsurvivor_age += age
                nonsurvivor_count += 1
        
        survivor_count = passenger_count - nonsurvivor_count
        survivor_age = age_total - nonsurvivor_age

        average_age = round((age_total/passenger_count), 2)
        sur_avgage = round((survivor_age/survivor_count), 2)
        non_avgage = round((nonsurvivor_age/nonsurvivor_count), 2)

        while not oldest_age[-1] == oldest_age[0]:    #these two blocks allo
            oldest_age.pop(0)
            oldest_pas.pop(0)
        while not youngest_age[-1] == youngest_age[0]:
            youngest_age.pop(0)
            youngest_pas.pop(0)

        oldest_pas = "; ".join(oldest_pas)
        youngest_pas = "; ".join(youngest_pas)

        print(f"The average age of the passengers was {average_age}")
        print(f"The average age of the passengers who survived was {sur_avgage}")
        print(f"The average age of the passengers who did not survive was {non_avgage}\n")
        print(f"The oldest passenger(s) was {oldest_pas} at an age of {oldest_age[0]}")
        print(f"The youngest passenger(s) was {youngest_pas} at an age of {youngest_age[0]}")




        output.write("Average Passenger Age" + "," + "Average Survivor Age" + "," + "Average Non-Survivor Age" + "," + "Oldest Passenger(s)" + "," + "Oldest Age" + "," + "Youngest Passenger(s)" + "," + "Youngest Age")
        output.write("\n")
        output.write(str(average_age) + "," + str(sur_avgage) + "," + str(non_avgage) + "," + oldest_pas + "," + str(oldest_age[0]) + "," + youngest_pas + "," + str(youngest_age[0]))
    
    

"""
Args:
    input (file)
Return:
    n/a

Description: calculates survival rate based on class, and determines average fare for each class, writes info to csv
"""
def class_analysis(input):

    input.seek(0)
    next(input)


    with open('classanalysis.csv', 'w') as output:  
        

        c1_total = 0
        c2_total = 0
        c3_total = 0

        c1_survived = 0
        c2_survived = 0
        c3_survived = 0

        c1_faretotal = 0
        c2_faretotal = 0
        c3_faretotal = 0

        for line in input:
            split_line = line.strip().split(',')
            
            pclass = split_line[2]
            fare = float(split_line[10])

            if pclass == "1":
                c1_total += 1
                c1_faretotal += fare
                if split_line[1] == "1":
                    c1_survived += 1
            elif pclass == "2":
                c2_total += 1
                c2_faretotal += fare
                if split_line[1] == "1":
                    c2_survived += 1
            elif pclass == "3":
                c3_total += 1
                c3_faretotal += fare
                if split_line[1] == "1":
                    c3_survived += 1

        c1_rate = round((c1_survived*100/c1_total), 2)
        c2_rate = round((c2_survived*100/c2_total), 2)
        c3_rate = round((c3_survived*100/c3_total), 2)

        c1_fareavg = round(c1_faretotal/c1_total, 2)
        c2_fareavg = round(c2_faretotal/c2_total, 2)
        c3_fareavg = round(c3_faretotal/c3_total, 2)

        print(f"The average fare for First, Second, and Third Class are ${c1_fareavg}, ${c2_fareavg}, and ${c3_fareavg} respectively")

        if (c1_rate >= c2_rate) and (c1_rate >= c3_rate):
            print(f"The class with the highest survival rate was First Class with a survival rate of {c1_rate}%")
            print(f"Second and Third Class had a survival rate of {c2_rate}% and {c3_rate}% respectively")
        elif (c2_rate >= c1_rate) and (c2_rate >= c3_rate):
            print(f"The class with the highest survival rate was Second Class with a survival rate of {c2_rate}%")
            print(f"First and Third Class had a survival rate of {c1_rate}% and {c3_rate}% respectively")
        elif (c3_rate >= c1_rate) and (c3_rate >= c2_rate):
            print(f"The class with the highest survival rate was Third Class with a survival rate of {c3_rate}%")
            print(f"First and Second Class had a survival rate of {c1_rate}% and {c2_rate}% respectively")

        output.write("First Class Survival Rate" + "," + "First Class Average Fare" + "," + "Second Class Survival Rate" + "," + "Second Class Average Fare" + "," + "Third Class Survival Rate" + "," + "Third Class Average Fare")
        output.write("\n")
        output.write(str(c1_rate) + "," + str(c1_fareavg) + "," + str(c2_rate) + "," + str(c2_fareavg) + "," + str(c3_rate) + "," + str(c3_fareavg))

            
          

"""
Args:
    input (file)
Return:
    n/a

Description: calculates survival rate based on either solo or family travelling, writes info to csv
"""
def fam_survival(input):

    input.seek(0)
    next(input)


    with open('familyanalysis.csv', 'w') as output:  
        

    
        family_total = 0
        family_survived = 0

        solo_total = 0
        solo_survived = 0


        for line in input:
            split_line = line.strip().split(',')


            # Calculate family size (including the passenger)
            family_size = int(split_line[7]) + int(split_line[8]) + 1
   
            # Count survivors and totals
            if family_size > 1:  # Has family aboard
                family_total += 1
                if split_line[1] == "1":
                    family_survived += 1
            else:  # Traveling alone
                solo_total += 1
                if split_line[1] == "1":
                    solo_survived += 1

        fam_surviverate = round((family_survived*100/family_total), 2)
        solo_surviverate = round((solo_survived*100/solo_total), 2)



        print(f"Survival rate travelling with family was {fam_surviverate}%")
        print(f"Survival rate traveling alone was {solo_surviverate}%")

        output.write("Traveling With Family Survival Rate" + "," + "Traveling Alone Survival Rate\n")
        output.write(str(fam_surviverate) + "," + str(solo_surviverate))

    
            



def main():
    file = 'titanic.csv'
    with open(file, 'r') as file:
        while True:
            choice = input('''What would you like to do? (enter number)
1) Displays the first 10 rows and amount of all passengers
2) Get Dataset's overall survival rate 
3) Analyze Dataset's survivability based on Gender (compiles data into CSV)
4) Analyze Dataset's survivability based on Age (compiles data into CSV)
5) Analyze Dataset's survivability based on Class (compiles data into CSV)
6) Analyze Dataset's survivability based on Family Size (compiles data into CSV)
''')
            if choice == "1":
                display_data(file) 
            elif choice == "2":
                survival_rate(file)
            elif choice == "3":
                gender_analysis(file)  
            elif choice == "4":
                age_analysis(file)
            elif choice == "5":
                class_analysis(file)
            elif choice == "6":
                fam_survival(file)
            else:
                pass
            
                  
            
            
            


main()




