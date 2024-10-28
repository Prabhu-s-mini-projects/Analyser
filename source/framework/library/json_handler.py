"""
Class Name: JsonHandler.py
Blue+print of:Json file
"""
# Dependencies
import os
import json

# Internal Dependencies
from source.framework.library.a_integrator import LOG

# [Decorators]
def json_handler(func):
    """Acts as decorator"""

    def wrap_func(*args, **kwargs):
        """Wrapper function"""
        try:
            return func(*args, **kwargs)

        except FileNotFoundError as e:
            print(f"Request failed: {str(e)}")
            LOG.exception(f"{e=}")

    return wrap_func

# [class]
class JsonHandler:
    """
    Purpose: Blueprint of Json file
    Attributes:
        file_path : str
        data : dict "content in json file"

    """

    def __init__(self, file_path):
        """
        Attributes:
            file_path : str
        """
        self.file_path: str = os.path.join(os.getcwd(),file_path)
        self.data : dict = self.load()

    def load(self)-> dict:
        """Load JSON data from a file."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"No such file: '{self.file_path = }'")

        with open(self.file_path, 'r',encoding='utf-8') as file:
            return json.load(file)

    def save(self, data)-> None:
        """Save JSON data to a file."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"No such file: '{self.file_path = }'")

        with open(self.file_path, 'w',encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def update(self, key, value) -> None:
        """Update a specific key in the JSON file."""
        data = self.load()
        data[key] = value
        self.save(data)

    def get_value(self, key)-> tuple:
        """Get a value from the JSON data by key."""
        data = self.load()
        return data.get(key, None)

    def delete_key(self, key)-> None:
        """Delete a specific key from the JSON file."""
        data = self.load()
        if key in data:
            del data[key]
            self.save(data)
