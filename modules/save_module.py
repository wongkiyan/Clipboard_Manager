import pyperclip, shelve, sys
import configs as Configs

def run():
    cbm_shelf = shelve.open(Configs.SHELF_DATA_PATH)
    cbm_shelf[sys.argv[2]]=pyperclip.paste()
    print("-- Save operation executed --")
    print(f"Key  : {sys.argv[2]}") 
    print(f"Value: {pyperclip.paste()}")
    cbm_shelf.close()

if __name__ == "__main__":
    run()