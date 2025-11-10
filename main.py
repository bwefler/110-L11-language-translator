import csv

def intro():
  'Welcome to the Spanish and French translator app.  \nPlease enter an English word and press the "Enter" key.'
  print('\nType "done" at any time to exit.')

def exit():
  print('\nThanks for using the translator app. Have a great day!')

translations = {}
words = open("translations.csv","r")
reader = csv.DictReader(words, delimiter=",")
for line in reader:
  english = line["English"].lower()
  spanish = line["Spanish"]
  french = line["French"]
  translations[english] = [spanish,french]

intro()
done = False
while not done:
  word = input("Type an English word to translate:\n")
  word = word.lower()

  if word == "done":
    done = True
    exit()
  elif word in translations:
    print(f'\nSPANISH: {translations[word][0]}')
    print(f'\nFRENCH:  {translations[word][1]}\n')
  else:
    print("\nTranslation is not known\n")
