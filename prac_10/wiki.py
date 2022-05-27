#write a small script that prompts the user for a page title or search phrase, then prints the summary of that page. Use a simple loop that continues doing this until the user enters blank input.
import wikipedia

input = wikipedia.summary(input("Enter a search term: "))
while input.isspace() == False:
    print(input)
    input = wikipedia.summary(input("Enter a search term: "))