import pdb;

from person import Person
from project import Project


#  This application is a fair grade allocator based on the work by: 
#  A. Procaccia, J. Goldman, N. Shah and D. Kurokawa.
#  Author: Rae Harbird
#  Date: November 2018
## Constants

MINIMUM_NAME_LENGTH = 3     # Used to validate team member's name and project name

MAXIMUM_NAME_LENGTH = 10

MINIMUM_TEAM_SIZE = 3

MAXIMUM_TEAM_SIZE = 5


MENU_CHOICES = ['A', 'C', 'V', 'S', 'Q']


## Prints the menu for the application. 

#

def printMenu():

    menuString = ("Welcome to Spliddit:\n"

                 "\tAbout (A)\n"

                 "\tCreate Project (C)\n"

                 "\tEnter Votes (V)\n"

                 "\tShow Project (S) \n"

                 "\tQuit (Q)")

    print(menuString)



## Prints a description of the application. 

def about() :

    aboutString = ("\n\nWelcome to Spliddit. "

                   "This application will allocate grades to "

                   "project participants based of the votes of their "

                   "peers.\n")

    print(aboutString)



##  Sets up a project from the information entered by the user.  

#   @return a tuple containing the project name and the names

#           of team members

#

def createProject() :

    projectName = getProjectName()
    teamSize = getTeamSize()
    members = getTeamNames(teamSize)

    ##  Create Project class instance to store project details
    project = Project(projectName, teamSize, members)
    print("\n \t\tProject Name: " + project.name)
    print("\n \t\tProject Members Size" + str(project.size))
    print("\n \t\tProject Members" + str(project.members))

##  Prompts the user for a project name and validates it.
#   @return a string containing the project name.
#   Invariants: a project name must be between the minimum and maximum length

#               and cannot be blank. The name must contain only alphabetic 

#               characters.

#           

def getProjectName() :

    projectName = input("\n\tEnter project name: ") 

    while isValidName(projectName, MINIMUM_NAME_LENGTH, MAXIMUM_NAME_LENGTH) == False :

        print(("\n\t\tThe project name must be more than {} characters long, "

               "less than {} characters long and must contain only "

               "alphabetic characters. Try again.\n")

               .format(MINIMUM_NAME_LENGTH - 1, MAXIMUM_NAME_LENGTH + 1))

        projectName = input("\n\tEnter project name: ")

    print("\t\t\tProject Name: " + projectName )
    return projectName

## Check the string contains only characters from the alphabet and check that it is the right length.

# @param theString the string to be validated

# @minimum the minimum length of the string

# @maximum the maximum length of the string

# @return True if the string conforms to the validation conditions and False if it does not.

def isValidName(theString, minimum, maximum) :

    return theString.isalpha() == True \
    and len(theString) >= minimum \
    and len(theString) <= maximum

##  Prompts the user for the team size and validates it.

#   @return the number of people in the team.

#

#   Invariants: the team size must be between the minimum and maximum size.

#

def getTeamSize() :

    teamSize = input("\n\tHow many people in the team: ")
    
    while isValidTeamSize(teamSize, MINIMUM_TEAM_SIZE, MAXIMUM_TEAM_SIZE) == False :

        print(("\n\t\tThe team size must be more than {} and less than {}. "

               "Try again.").format(MINIMUM_TEAM_SIZE - 1, MAXIMUM_TEAM_SIZE + 1))

        teamSize = input("\n\tHow many people in the team: ")

    print("\t\t\tProject Team Size: " + teamSize)
    return int(teamSize)
   
##  Checks whether the team size is greater than or equal to the minimum size
#   and less than or equal to the maximum size.
#   @return True or False.

def isValidTeamSize(size, minimum, maximum):

    return isInteger(size) and int(size) >= minimum and int(size) <= maximum

##  Checks whether the string passed as a parameter is an integer.

#

#   @return True or False.

#

def isInteger(number) :

    try: 

        int(number) 

        return True 

    except ValueError:

        return False

##  Gets the names for the people in the team. Duplicate team names are not allowed.

#

#   @return a list containing the names.

#

def getTeamNames(teamSize):

    projectName = getProjectName()

    teamNames = []

    i = 1 # Corrected this array

    while i <= teamSize:

        teamName = getPersonName()

        if teamName not in teamNames:

            teamNames.append(teamName)
            person = Person(teamName, projectName)

            i = i + 1

            print("\t\t\t Person added to " + projectName + ":" + person.name)

        else:

            print("\n\t\tSorry, you already have a team member called {}, try again."

                  .format(teamName))

    return teamNames



##  Prompts the user for a person's name and validates it.
#   @return a string containing the person's name.
#   Invariants: a person's name must be between the minimum and maximum length
#   and cannot be blank. The name must contain at least one alphabetic character and may contain numbers.

def getPersonName() :

    teamName = input("\n\tEnter member's name: ")
    
    while isValidName(teamName, MINIMUM_NAME_LENGTH, MAXIMUM_NAME_LENGTH) == False :

        print(("\n\t\tThe name must be more than {} characters long,"

               " less than {} characters long and cannot contain "

               "numbers or punctuation characters.").format(MINIMUM_NAME_LENGTH - 1,

                                                           MAXIMUM_NAME_LENGTH + 1))

        teamName = input("\n\tEnter name: ")
    
    print()

    return teamName



##  Validates the option choice.


#   @return True or False

#

#   Invariants: The option must be a valid choice from MENU_CHOICES

#

def isValidOption(option):

    if len(option.strip()) == 0:

        return False

    elif option[0].upper() in MENU_CHOICES:

        return True

    else:

        return False



##  Prints the menu, prompts the user for an option and validates the option.

#

#   @return a character representing the option.

#

def getOption():  

    option = '*'    

    while isValidOption(option) == False:

        printMenu()

        option = input("\nEnter an option: ")   

    return option.upper()

# def castVotes():

def castVotes():

    votes = votes()

    # teamNames = getTeamNames().teamNames
                
    if votes[teamNames] + votes2[teamNames] != 100:
             print("The points must add upto 100.")
             print("Kindly re-enter the points")
             print()
             votes[personName] = input("Enter "+ personName + "'s points for Asim: ")
             votes2[personName] = input("Enter "+ personName + "'s points for Bogdan: ")

    else:
              print("Your points have been recorded")
              print()


    votes()

def votes():

        votes = {}

        print("\tEnter " + teamNames[0] + "'s votes, points must add up to 100: ")
        print()
        votes[teamNames[0]] = input("Enter "+ teamNames[0] + "'s points for " + teamNames[1])
        
        votes2 = {}
        votes2[teamNames[1]] = input("Enter "+ teamNames[1] + "'s points for " + teamNames[2])

        print()
        print("\tEnter " + teamNames[1] + "'s votes, points must add up to 100: ")
        print()
        votes[teamNames[1]] = input("Enter "+ teamNames[1] + "'s points for " + teamNames[0])
        
        votes2 = {}
        votes2[teamNames[1]] = input("Enter "+ teamNames[1] + "'s points for " + teamNames[2])
        

def main() :

    option = '*'    

    while option != 'Q':

        option = getOption()        

        if option == 'A':

            about()

        elif option == 'C':

            createProject()

        elif option == 'V':
            
            castVotes()
            
        elif option == 'S':

            print("\n\tNot implemented yet.\n")

        else: 

            print("Please select a valid option to proceed to next steps")


    print("\n\nBye, bye.")

main()

