def getEquivalentNumber(_myChar):
    if len(_myChar) != 1 or not _myChar.isalpha():
        return "Please provide a single alphabetic character."
    return ord(_myChar.lower()) - ord('a') + 1

def computeSumOfCharacters(word):
    return sum(getEquivalentNumber(char) for char in word)

def main():
    quit = True
    while quit:
        word = input("Enter a word: ")
        if not word.isalpha(): 
            print("Numbers are not allowed!")
            continue
        print(f"The Majic Number for {word}: {computeSumOfCharacters(word)}")
        print("------------------------------------------------------------")
        qc = input("Type 'Q' or 'q' to Quit. Press Enter to continue: ")
        if(qc.upper() == "Q"):
            print("Process finished with exit code 0")
            quit = False

main()
        



