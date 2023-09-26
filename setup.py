import os
import configs as Configs

if __name__ == "__main__":
    print("Creating data folder")
    if not os.path.exists(Configs.PROGRAM_DATA_PATH):
        os.makedirs(Configs.PROGRAM_DATA_PATH)
    else:
        print("Data folder already exists")
    print("Done.")