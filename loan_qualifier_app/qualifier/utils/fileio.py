# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


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
