#Author: Stephen Mester C20483376
#Program to open files and to compare and find words



class Words:

    def load_file(self,file,operator):      #Function to open file in a specific mode
        fileopen = open(file, operator)
        if operator != "r":                 #checks file is open in read mode
            raise TypeError
        for line in fileopen:
            word = line.split()
            words = word
            return(words)

    def find_words(self):                   #function to find and compare files
        string1 = self.load_file("herbert1.txt", "r")   #calls function to open file in read mode
        string2 = self.load_file("herbert2.txt", "r")
        stops = self.load_file("stops.txt", "r")
        try:
            for index in range(len(string1)):               #Nested for loop to find common words
                for index2 in range(len(string2)):
                    if string1[index] == string2[index2]:
                        print("This word is in common on both files: ", string1[index])
        except IndexError:
            print("Index error")                            #Try except to deal with possible index errors



var = Words()
var.find_words()

