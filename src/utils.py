import sys

def error_message_detail(error, error_detail: sys):
    """
    Returns a detailed error message with filename, line number, and error message
    """
    _, _, exc_tb = error_detail.exc_info()  # get exception info
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in Python script [{file_name}] at line [{line_number}]. Error message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Call parent constructor with the custom error message
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
