import inspect
from venv import logger


def current_function_info():
    # Get the caller's stack frame information
    frame = inspect.stack()[1]  # [0] is the current frame, [1] is the caller frame
    function_name = frame.function
    file_name = frame.filename
    line_number = frame.lineno
    print(f"Function Name: {function_name}")
    print(f"File Name: {file_name}")
    print(f"Line Number: {line_number}")

def my_method():
    # Get the current frame and the previous frame in the stack
    current_frame = inspect.currentframe()
    caller_frame = current_frame.f_back

    # Get the method name and file name
    method_name = caller_frame.f_code.co_name
    file_name = caller_frame.f_code.co_filename

    print(f"Method name: {method_name}")
    print(f"File name: {file_name}")

def caller_function():
    current_function_info()

my_method()

from source.framework.library.logger import LOG

LOG.debug("Message is here")
