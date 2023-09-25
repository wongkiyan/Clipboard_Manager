import pyperclip, shelve, sys, enum

# TODO: save module
# TODO: load module
# TODO: list module

class RequestType(enum):
    SAVE = 1
    LOAD = 2
    LIST = 3

def handle_request(request_type):
    if request_type is None: return print("Request type not found: {request_type}. Exiting.")
    if request_type == RequestType.SAVE: return print("執行儲存操作")
    if request_type == RequestType.LOAD: return print("執行載入操作")

if __name__ == "__main__":
    request_type = RequestType.get(sys.argv[1].upper())
    handle_request(request_type)

#Reference: https://cloud.tencent.com/developer/article/1578020