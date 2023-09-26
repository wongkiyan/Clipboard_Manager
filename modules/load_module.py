import pyperclip, shelve, sys
import configs as Configs

def run():
    cbm_shelf = shelve.open(Configs.SHELF_DATA_PATH)
    pyperclip.copy(cbm_shelf[sys.argv[1]])
    print("-- Load operation executed --")
    print(f"Key  : {sys.argv[1]}")
    print(f"Value: {cbm_shelf[sys.argv[1]]}")
    cbm_shelf.close()

if __name__ == "__main__":
    run()