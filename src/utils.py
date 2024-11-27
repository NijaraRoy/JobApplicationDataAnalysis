import pickle
import csv
import yaml


def load_pickle_data(file_path:str):
    """
    Load objects from a pickle file.

    Args:
        file_path (str): Path to the pickle file.

    Returns:
        object: The deserialized object(s) from the pickle file.
    """
    with open(file_path, 'rb') as f:
        objects = pickle.load(f)
    
    return objects


def save_to_csv(objects, file_path):
    """
    Save a list of objects to a CSV file with the specified column headers.

    Args:
        objects (list): List of objects to save. Each object must have a valid `__str__` method.
        file_path (str): Path to save the CSV file.
    """
    with open(file_path, 'w') as f:
        f.write("unique_id,date,title,company,type,experience,salary,interview_difficulty\n")
        for obj in objects:
            f.write(str(obj) + '\n')
    print(f"CSV file generated successfully at: {file_path}")



def load_yaml(file_path:str) -> dict:
    """
    Read YAML file and return dict
    Args:
        file_path (str): Path of the input yaml file
    Returns:
        Dict of input yaml file
    """
    return yaml.load(open(file_path, 'rb'), Loader = yaml.Loader)