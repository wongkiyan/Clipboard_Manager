import shelve
import configs as Configs

def run():
    cbm_shelf = shelve.open(Configs.SHELF_DATA_PATH)
    cbm_shelf.clear()
    cbm_shelf.close()
    
    print("-- Clear operation executed --")

if __name__ == "__main__":
    run()