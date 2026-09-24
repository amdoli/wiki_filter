import re
import sys
import pyperclip

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <wiki sentence>", file = sys.stderr)
        sys.exit(1) 
    
    # Get all the agrvs
    sentence = " ".join(sys.argv[1:])

    # Erase the Brackets
    sentence = sentence.replace("[", "").replace("]", "")

    # Remove anything between Parentheses
    sentence = re.sub(r"\([^()]*\)", "", sentence)
    # Copy the result to the device clipboard.
    pyperclip.copy(sentence)

    print(f'OUTPUT:\n{sentence}\n')
    print("The filtered text was copied to the clipboard.")
