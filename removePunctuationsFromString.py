# Remove Punctuations From String


def remove_punctuations(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in string:
        if char not in punctuations:
            no_punct += char
    return no_punct


string = "Hello!!!, he said ---and went."

print(remove_punctuations(string))