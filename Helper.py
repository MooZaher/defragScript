from collections import Counter
import pandas as pd
from PyQt5.QtWidgets import QMessageBox

"""
Function to get count of occurrences in a list
Parameters: list / Returns: Dictionary
"""


def get_block_counts(flat_list):
    x = Counter(flat_list)
    outDict = x
    return outDict


"""
Function to read csv file, convert it to pandas Dataframe
Parameters: Path --> file path / Returns: Pandas Dataframe
"""


def load_csv(path):
    input_df = pd.read_csv(path, sep=';', header=None)  # Read csv file and perform text to column to separate columns
    input_df = input_df.drop(input_df.columns[0], axis=1)  # Drop index column with value zero
    input_df.columns = input_df.iloc[0]  # Reassign index column
    input_df = input_df.iloc[1:].reset_index(drop=True)  # Reset index after above changes
    input_df = input_df.fillna(' ')  # Fill empty cells with whitespaces
    print(f"The Input before processing is : \n{input_df}")  # Print input dataframe before processing
    return input_df


"""
Function to take dataframe and convert it to list
Parameters: Dataframe / Return: List
"""


def convert_df_to_list(df):
    dfList = df.values.tolist()  # Convert data frame to a list of lists contains all rows
    outList = [item for sublist in dfList for item in sublist]  # Convert above list of lists into a combined list
    return outList


"""
Function to convert a list to a matrix given number of columns
Parameters: list, colCount --> int / Return: Matrix
"""


def list_to_matrix(lst, colCount):
    matrix = []  # Create empty matrix
    for i in range(0, len(lst), colCount):  # Iterate over the list to fill the matrix till with the needed column count
        matrix.append(lst[i:i + colCount])
    return matrix


"""
Function to get matrix and convert it to concatenated dataframe
Parameters: Matrix / Returns: Dataframe
"""


def matrix_to_df(matrix):
    matrixOutDF = pd.DataFrame(matrix)  # Create pandas dataframe from matrix
    header = list(matrixOutDF.columns.values)  # getting header of dataframe staring from 0 till dataframe max_col
    header_list = [x + 1 for x in header]  # Increment header by 1
    matrixOutDF = pd.DataFrame(matrix, columns=[header_list])  # Adding new header
    return matrixOutDF


"""
Function to get final dataframe and save it to csv file
Parameters: Dataframe / Returns: Saved output csv
"""


def save_csv(output_df, outPath):
    csv_data = output_df.to_csv(outPath, sep=';')  # Save csv in given path and concatenating all columns with separator
    return csv_data


"""
Function to process the fragmentation algorithm
Parameters: list / Returns: None
"""


def defragmentation_algorithm(list_flat):
    # Get number of occurrences of all elements in dataframe indicates block size when defragmentation is done
    element_dict = get_block_counts(list_flat)

    # Getting first item in the memory and assign it to the marker
    marker = list_flat[0]

    temp_list = []  # Temp list to store items taken out of memory

    for i, element in enumerate(list_flat):  # Iterate over all cells in memory grid
        if element_dict.get(marker) > 0:  # if item in memory has blocks left in memory

            if element == marker:  # if memory cell in grid is occupied with our highest priority element

                # decrement count of item in memory as its already written
                element_dict[element] = element_dict.get(element, 0) - 1

            elif element == ' ':  # if the memory space is empty
                list_flat[i] = marker  # Write our marker in this cell
                element_dict[marker] = element_dict.get(marker, 0) - 1  # Decrement size of our marker

            elif element != marker:  # if element in memory not equal our item being written now in memory cells grid

                # overwrite our marker in index of memory cell grid and remove the overwritten element to a temp list
                list_flat[i] = marker
                element_dict[marker] = element_dict.get(marker, 0) - 1  # Decrement  from marker size
                # if the overwritten element is not in temp list already append it in the temp list
                if element_dict.get(element) > 0 and element not in temp_list:
                    temp_list.append(element)

        elif element_dict.get(marker) == 0:  # if all marker block size is written in memory

            # Pick new element to be oru new marker, if the element in current memory has size and not equal whitespace
            if element_dict.get(element) > 0 and element != ' ':
                marker = element  # Assign it as new marker
                element_dict[marker] = element_dict.get(marker, 0) - 1  # decrement one size as it is already  written

            elif element == marker or element == ' ':  # if element equal empty marker or whitespace,
                if len(temp_list) > 0:  # and temp list has removed overwritten values
                    marker = temp_list[0]  # set marker to be the first item removed from memory
                    list_flat[i] = marker  # write it in the current memory cell grid
                    element_dict[marker] = element_dict.get(marker, 0) - 1  # decrement its size by 1
                    temp_list.remove(temp_list[0])  # remove it from temp list as it will be filled
                elif len(temp_list) == 0:  # if nothing in empty list
                    marker = ' '
        else:
            list_flat[i] = marker
    return list_flat


# Message box for GUI needs

def messageBox(self, caption, message):
    QMessageBox.about(self, caption, message)
