# cbm.pyw - Save and load pieces of text to the clipboard.
# Usage: mcb.pyw save <keyword> - Saves clipboard to keyword
#        mcb.pyw <keyword> - Loads keyword to clipboard
#        mcb.pyw list - Loads all keywords to clipboard

import sys
from enum import Enum
from modules import *

# TODO: save module
# TODO: load module
# TODO: list module

request_functions = {
    "SAVE" : save_module,
    "LOAD" : load_module,
    "LIST" : list_module,
}

def handle_request():
    # cbm
    if len(sys.argv) == 3: return
    if len(sys.argv) == 2: return
    if len(sys.argv) == 1: return
    request_type = sys.argv[1].upper()
    function_to_execute = request_functions.get(request_type)
    if function_to_execute: function_to_execute()
    return print("Request type not found: {request_type}. Exiting.")

if __name__ == "__main__":
    handle_request()

#Reference: https://cloud.tencent.com/developer/article/1578020