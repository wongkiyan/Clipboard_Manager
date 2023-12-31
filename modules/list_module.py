import shelve
import configs as Configs

def run():
    cbm_shelf = shelve.open(Configs.SHELF_DATA_PATH)
    print("-- List operation executed --")
    print("\n".join(map(str, list(cbm_shelf.keys()))))
    cbm_shelf.close()

if __name__ == "__main__":
    run()