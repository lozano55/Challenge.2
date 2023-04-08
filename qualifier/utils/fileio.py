# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import questionary
from pathlib import Path
import sys


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data



def save_csv(csvpath, qualifying_loans):
    """Saves the CSV file with path physically hardcoded 

    Args:
        csvpath: Path to be created 
        qualifying_loans: The Refined loans User Qualified for 

    """
    with open(csvpath, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        
        header = ["Lender","Max Loan Amount","Max Loan to value","Max dept to Income","Minimum Credit Score","Interest Rate "]

        csvwriter.writerow(header)

        for data in qualifying_loans:
            csvwriter.writerow(data)




def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """

    save_file = questionary.confirm("Do you want to Save the Qualifying loans into a file?").ask()

    if save_file == True:
            
        if len(qualifying_loans) >= 1:
            file_name = questionary.text("Please Enter a name for this file (!Do not include .csv!)").ask()
            preferred_path = questionary.confirm("If You Know your Preffered Path Enter (Y) If you dont know what a Path Is Enter(n)").ask()

            """Asks the User if Loans should be saved into a file if yes, then code Proceeds 


            Args:
                - Asks User To Input a name for the file, That does not include (.csv) at the end
                - It Then asks For a preffered Path

            """

            if preferred_path == False:
                csvpath = (f"{file_name}.csv")

                print(f"Thank you for your time! Your Qualifying loans were saved to your Current Folder as {csvpath}")
                print(f"Dont hesitate to Contact us if you have any questions, Have a great Day!")

                csvpath = Path(csvpath)
                save_csv(csvpath, qualifying_loans)

            elif preferred_path == True:
                enter_path = questionary.text("Only Enter Your Desired Path(Do Not Include in it This File Name. Example: ./data)").ask()
                csvpath = (f"{file_name}.csv")
                print(f"Thank you for your time! Your Qualifying loans were saved as {csvpath}")
                print(f"Dont hesitate to Contact us if you have any questions, Have a great Day!")

                csvpath = (f"{enter_path}/{csvpath}")
                print(f"The Relative path is: {csvpath}")
                csvpath = Path(csvpath)
                print(f"The Absolute path is {csvpath.absolute()}")

                save_csv(csvpath, qualifying_loans)

            """ Preffered Path 

            Args:
                -  If the User does not know the preffered path to place the File. The File will automatically save into the current Folder 
                -  If the User Knows the Preffered path to place the file then he will include only the path name to the Directory/Folder 
                should not Include The loan File Name. The File Will then automatically save into the preffered Directory/Folder/Path
        
            """
        elif len(qualifying_loans) <= 0:
            sys.exit("We are Sorry, It looks like There are currently no eligible Loans to save. Have a Great Day!")

    if save_file == False:
        print("Thank you for your time! Contact us if you have any questions, Have a great Day!")


    """No Files to save 

    Args:
        - If No Qualifying loans Found automatic message will be sent to user 
        - If User Chooses to not save, automatic sys exit with no saved file and message sent to user
    
    """
        

