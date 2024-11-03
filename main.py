def NumberOfWords(text):
    return len(text.split())

def CharacterCount(text):
    characters = {}
    for character in text.lower():
        if character in characters.keys():
            characters[character] += 1
        else:
            characters[character] = 1
    
    return characters

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(f"{NumberOfWords(file_contents)} words found in the document\n")
    characters = CharacterCount(file_contents)
    for character in characters.keys():
        print(f"The '{character}' character was found {characters[character]} times")