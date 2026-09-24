

# This is the main program
# write your program here

def load_stopwords(filename):
    return stopwords # strip to remove whitespace/newline, lower(). Stopwords is set {}

def load_words(filename, stopwords):
    """Opens the filename and read """


    # read file to lower()

    # str.maketrans(,,) to remove any punctations 
    # text.translate()

    # split 

    # filter to remove stopwords 

    return filter # List

def term_frequency(words): # Magid 

    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    tfs = {}
    
    for word in counts: # keep track of words
        tfs[word] = counts[word] / len(words)

    return tfs

tfa = term_frequency(words_a)
tfb = term_frequency(words_b)


set_tfa = set(tfa)
set_tfb = set(tfb)

common_words = set_tfa & set_tfb

for common_word in common_words:
    del tfa[common_word]
    del tfb[common_word]

 