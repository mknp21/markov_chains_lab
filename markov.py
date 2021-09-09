"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # open file in a variable
    file_contents = open(file_path).read()
    # # create empty file
    # file_list = []
    # # for loop to go through everyline striping out any right spaces and defining words
    # # by the spaces and then that creates a list of words that we extend in to the empty list
    # for line in file_contents:
    #     line = line.rstrip()
    #     word = line.split(" ")
    #     file_list.extend(word)
    
    # # create an empty file string and iterate through each item in the file_list
    # # adding the item plus a space to the file_string.
    # file_string = ""
    # for item in file_list:
    #     file_string += item + " "

    
    print(file_contents)
        
    return file_contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    
    words = input_text.split()
    
        
    for i in range(len(words)-2):
        # key_list = []
        key = (words[i], words[i+1])
        value = words[i+2]
        # key_list.append(key)
        
    
        # chains[key] = chains.get(key, 0)
        # print(key_list, value_list)
        if key not in chains:
            value_list = []
            chains[key] = value_list
            # value_list.append(value)   
        # else:
        chains[key].append(value)
        
    # for key, value in chains.items():   
    #     print(f"{key}, {value}")

    return chains


def make_text(chains):
    """Return text from chains."""

    key_val = list(chains.items())
    link = choice(key_val)

    # key_words = list(chains.keys())
    # rand_key = choice(key_words)
    # # if rand_choice == chains.keys():
    #     # select choice in the values list
    # rand_val = choice(list(chains.values()))
        
    # # link = choice(key_word) + choice(value item)
    # link = str(rand_key) + str(rand_val)
    print(link)
    # key/tuple + random.choice(value)
    #random.choice(seq)

    #return ' '.join(key_words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
