#Sam Durst

import re
import time
def main():
    try:
        infile = open(input("Please enter the name of the file with .txt: "), 'r')
    except IOError:
        print("Error Opening File")
    else:
        start_time = time.time()
        dictionary = {} #First Data Structure
        word_count = []

        words = infile.read() #reads onto one string
        infile.close()

        words = words.lower() #lower case
        words = re.sub(r'[^\w\s]','',words) #replaces standard punctuation with ''
        wordlist = words.split() #splits the words by the default blank space

        for line in wordlist:
            if line not in dictionary: #if the word hasnt already appeared
                dictionary[line]=0 #set its count to 0
            dictionary[line]+=1 #add 1 for every word

        for x, y in dictionary.items():
            word_count.append([y,x]) #add the subarray to the array


        mergeSort(word_count) #SORTING ALGORITHM

        print("\nFirst 10 Words: ")
        for i in range(10):
            print(word_count[i])


        print("\nLast 10 Words: ")

        length = len(word_count)
        for i in range(length-10, length):
            print(word_count[i])

        print("Total Words: ",len(wordlist))
        print("Time it took this program to run in seconds: ",time.time()-start_time) #runtime

def mergeSort(list_sort):
    list_length = len(list_sort)

    if list_length>1: #ensures list isnt empty
        i=0
        j=0
        k=0
        middle = list_length//2

        lefthalf = list_sort[:middle]   #splits array into two halves
        righthalf = list_sort[middle:]

        mergeSort(lefthalf) #recursively splits the array over and over until each array holds one value
        mergeSort(righthalf)

        left_length = len(lefthalf)
        right_length = len(righthalf)

        while i < left_length and j < right_length:
            if lefthalf[i][0] > righthalf[j][0]:
                list_sort[k]=lefthalf[i] #if the left item is greater than the right, sort it on the left side
                i+=1
            elif lefthalf[i][0]==righthalf[j][0] and getCharValue(lefthalf,i) < getCharValue(righthalf,j):
                list_sort[k]=lefthalf[i] #if they are equal, sort by the character that comes first
                i+=1
            elif lefthalf[i][0]==righthalf[j][0] and getCharValue(lefthalf,i) > getCharValue(righthalf,j):
                list_sort[k]=righthalf[j]
                j+=1
            elif lefthalf[i][0]==righthalf[j][0] and getCharValue(lefthalf,i) == getCharValue(righthalf,j):
                if getSecondChar(lefthalf,i) < getSecondChar(righthalf,j):
                    list_sort[k]=lefthalf[i] #else if they are equal and they start with the same letter:
                    i+=1
                elif getSecondChar(lefthalf,i) == getSecondChar(righthalf,j):
                    if getThirdItem(lefthalf,i) < getThirdItem(righthalf,j):
                        list_sort[k]=lefthalf[i]
                        i+=1
                    elif getThirdItem(lefthalf,i) == getThirdItem(righthalf,j):
                        if getFourthItem(lefthalf,i) < getFourthItem(righthalf,j):
                            list_sort[k]=lefthalf[i]
                            i+=1
                        else:
                            list_sort[k]=righthalf[j]
                            j+=1
                    else:
                        list_sort[k]=righthalf[j]
                        j+=1
                else:
                    list_sort[k]=righthalf[j]
                    j+=1
            else:
                list_sort[k]=righthalf[j]
                j+=1
            k+=1

        while i < left_length:
            list_sort[k]=lefthalf[i]# puts the array back together
            i+=1
            k+=1

        while j < right_length:
            list_sort[k]=righthalf[j] #puts the array back together
            j+=1
            k+=1

alpha = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def getCharValue(aList, item):
    x = aList[item][1][:1]
    return alpha.index(x)

def getSecondChar(aList, item):
    y = aList[item][1][1:2:1]
    return alpha.index(y)

def getThirdItem(aList, item):
    x = aList[item][1][2:3:1]
    return alpha.index(x)

def getFourthItem(aList,item):
    x = aList[item][1][3:4:1]
    return alpha.index(x)


main()
