import pyperclip

def run():
    cbm_string = pyperclip.paste()
    if '\\' in cbm_string :
        pyperclip.copy(cbm_string.replace('\\','/'))
    if '/' in cbm_string:
        pyperclip.copy(cbm_string.replace('/','\\'))
    print("-- Slash operation executed --")
    print(f"From  : {cbm_string}") 
    print(f"To    : {pyperclip.paste()}")

if __name__ == "__main__":
    run()