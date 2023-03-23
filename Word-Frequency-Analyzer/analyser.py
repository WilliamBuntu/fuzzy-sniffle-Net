text=input('Enter any text:')
def word_frequency(text):
    # Split the text into individual words and convert them to lowercase
    words = text.lower().split()

    # Create an empty dictionary to store the frequency count of each word
    freq_dict = {}

    # Loop through each word in the list of words
    for word in words:
        # If the word is already in the dictionary, increment its count by 1
        if word in freq_dict:
            freq_dict[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            freq_dict[word] = 1

    # Sort the dictionary by value (i.e., by frequency) in descending order
    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    # Return the sorted list of tuples (word, frequency)
    return sorted_freq
print(word_frequency(text))