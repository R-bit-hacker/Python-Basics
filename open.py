from collections import Counter
import string

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize the text
    words = text.split()
    return words

def find_max_occurrence_words(text):
    words = preprocess_text(text)
    # Count word frequencies
    word_counts = Counter(words)
    # Find the maximum frequency
    max_count = max(word_counts.values())
    # Get all words with the maximum frequency
    max_occurrence_words = [word for word, count in word_counts.items() if count == max_count]
    return max_occurrence_words, max_count

def read_poem_from_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text

# Example usage
filename = 'poem.txt'
text = read_poem_from_file(filename)
max_words, max_count = find_max_occurrence_words(text)
print(f"Words with maximum occurrence: {max_words}, Count: {max_count}")