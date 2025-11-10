import csv

translations = {}
words = open("translations.csv","r")
reader = csv.DictReader(words, delimiter=",")
for line in reader:
  english = line["English"].lower()
  spanish = line["Spanish"]
  french = line["French"]
  translations[english] = [spanish,french]

done = False
print('Type "done" at any time to exit.')
while not done:
  word = input("Type an English word to translate: ")
  word = word.lower()

  if word == "done":
    done = True
  elif word in translations:
    print(translations[word])
  else:
    print("Translation is not known")

