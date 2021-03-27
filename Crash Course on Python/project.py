# python code to generate a wordcloud from a text file

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def calculate_frequencies(file_contents):
     # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
     
     # to exclude common words
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    words_dict = {}
    file = file_contents.lower()
    words = file.split(" ")
    for word in words:
        if word not in uninteresting_words or word.isalpha():
            if word not in words_dict:
                words_dict[word] = 0
            else:
                words_dict[word] = +1


     # Create the wordcloud
     cloud = wordcloud.WordCloud()
     cloud.generate_from_frequencies(words_dict)
     return cloud.to_array()
     
 # Generate the wordcloud image
 myimage = calculate_frequencies(file_contents)
 plt.imshow(myimage, interpolation = 'nearest')
 plt.axis('off')
 plt.show()
 
 
 ''' another simpler way to generate a wordcloud from a text file '''
 
 # read the file
 file = open("CS.txt", mode="r").read()

 # exclude common words
 stopwords = STOPWORDS

 # create the Wordcloud
 WC = WordCloud(
     background_color="white",
     stopwords=stopwords,
     height=600,
     width=400
 )

 # generate the Wordcloud
 WC.generate(file)

 # specify the name and save
 WC.to_file("WordCloud.png")
