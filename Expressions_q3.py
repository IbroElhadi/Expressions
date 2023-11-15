def add(sentence, word, index):
    if index > 0 and index < len(sentence):#check if index is a good number(exception handeling)
        return sentence[:index] + word + sentence[index:]#okay this code is actually kinda cool so look. you have the sentece then :index is the part of the sentence to the left of the index. index: is the sentence to the left. and you just add the word in between. cool eh

sentence = input("Enter the sentence: ")
insert = input("Enter the word to insert: ")
index = int(input("Enter the space index to insert at: "))

print("Completed Sentence:", add(sentence, insert, index))