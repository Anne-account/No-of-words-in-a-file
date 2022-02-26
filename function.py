def countWordsFromFile():
    fileName =  input("Enter the file name:- ")

    numberOfWords = 0

    file =  open(fileName, 'r')
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print("Number of words:")
    print(numberOfWords)


countWordsFromFile()


introString=input("Enter string:")
characterCount=0
wordCount=1
for i in introString:
      characterCount=characterCount+1
      if(i==' '):
            wordCount=wordCount+1
print("Number of word in the string:")
print(wordCount)
print("Number of character in the string:")
print(characterCount)
