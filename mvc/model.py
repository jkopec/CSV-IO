import csv, sys

__author__ = 'Jakub Kopec'


class Model(object):
    def __init__(self):
        self.filename = 'data/file.csv'

    def loadCSV(self):
        text = ""
        with open(self.filename, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                text += ' '.join(row) + "\n"
        return text

    def saveCSV(self, text):

        with open(self.filename, 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            zeilen = text.split("\n")
            for zeile in zeilen:
                if zeile != "":
                    woerter = zeile.split(" ")
                    spamwriter.writerow(woerter)
