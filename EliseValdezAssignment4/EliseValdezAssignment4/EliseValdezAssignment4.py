# INF360 - Programming in Python
# Elise Valdez
# Assignment 4

import re

# (2/2 points) - Read the file story.txt and store the lines as a variable called story. You must use relative paths, assume the story.txt file is in the same folder as your script.

storyFile = open("story.txt", "r")
story = storyFile.readlines()
storyFile.close()

# (5/5 points) - Write a regular expression that will find all occurrences of the phrase, "Sherlock Holmes".
sherlockRegex = re.compile(r"Sherlock Holmes")

# (5/5 points) - Using the substitute method, replace all occurrences of "Sherlock Holmes" with your name, storing the count of these occurrences as a variable called foundCount.

foundCount = 0
theCount = 0

for i in range(len(story)):
    find = sherlockRegex.findall(story[i])
    foundCount += len(find)
    story[i] = sherlockRegex.sub("Elise Valdez", story[i])

# (2/2 points) - Write a regular expression that will find all occurrences of the phrase, "the".
theRegex = re.compile(r'\bthe\b')

# (3/3 points) - Create a variable called theCount, that stores the total number of occurrences of the phrase "the".
for line in story:
    find = theRegex.findall(line)
    theCount += len(find)

# (3/3 points) - Print to the user, the original name, the replacement name, and the total number of occurrences using a print command with a formatted string literal using a string that starts with f".
print(f'Original name: Sherlock Holmes, Replacement Name: Elise Valdez, Total: {foundCount}')

# (3/3 points) - Print to the user a string that tells the user the total number of occurrences of "the" using a print command with a formatted string literal using a string that starts with f".
print(f"Total count of 'the': {theCount}")

# (1/1 points) - Save the story out to a new file called new_story.txt.
newStoryFile = open("new_story.txt", "w")
newStoryFile.writelines(story)
newStoryFile.close()



