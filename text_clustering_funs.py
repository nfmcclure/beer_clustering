##------------------------------------------------------------
##
## text_clustering_funs.py: Helper functions for text clustering
##
## Created: Feb, 2015
##
##------------------------------------------------------------
import csv
from string import punctuation
from nltk.corpus import stopwords


# Load Data as list of dictionaries
def csv_to_lists(filename):
    """
    Function takes a *.csv file name and returns a list of dictionaries. Every row is a dictionary.
    Args:
        filename: '*.csv' string that contains the data.
    Returns:
        result: Dictionary of rows
    """
    result = []
    with open(filename, mode='r', encoding='utf8') as file_connection:
        csv_reader = csv.DictReader(file_connection)
        for row in csv_reader:
            result.append({k: v for k, v in row.items()})
    return(result)


# Define a regex removal function
def remove_characters(my_string, chars_to_remove):
    return(''.join(char for char in my_string if char not in chars_to_remove))


# Normalize Text function
def normalize(my_list, methods):
    """
    Takes a list of strings and performs the normalization methods listed.
    Args:
        my_list: List of strings to perform normalization on.
        methods: A list of normalization methods
    Returns:
        my_list: normalized list of strings
    """
    if 'punctuation' in methods:
        my_list = [remove_characters(s, punctuation) for s in my_list]
    if 'numbers' in methods:
        my_list = [remove_characters(s, '0123456789') for s in my_list]
    if 'stopwords' in methods:
        stopwords_eng = set(stopwords.words("english"))
        my_list = [' '.join(word for word in s.split() if word not in stopwords_eng) for s in my_list]
    if 'whitespace' in methods:
        my_list = [' '.join(s.split()) for s in my_list]
    if 'lower' in methods:
        my_list = [s.lower() for s in my_list]
    return(my_list)