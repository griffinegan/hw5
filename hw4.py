import random
from collections import defaultdict

def extract_word_pairs(text):
    words = text.split()
    word_pairs = [(words[i], words[i+1]) for i in range(len(words)-1)]
    return word_pairs

def count_word_pair_frequencies(word_pairs):
    frequencies = defaultdict(int)
    for pair in word_pairs:
        frequencies[pair] += 1
    return frequencies

def choose_beginning_word_pair(frequencies):
    return random.choice(list(frequencies.keys()))

def generate_sentence(frequencies):
    sentence = []
    current_pair = choose_beginning_word_pair(frequencies)
    while current_pair != '.':
        sentence.append(current_pair[0])
        next_word_pairs = [pair for pair in frequencies if pair[0] == current_pair[1]]
        if not next_word_pairs:
            break
        cum_weights = [frequencies[pair] for pair in next_word_pairs]
        next_pair = random.choices(next_word_pairs, weights=cum_weights)[0]
        current_pair = next_pair
    return ' '.join(sentence)

def main(input_file):
    with open(input_file, 'r') as file:
        text = file.read()
    word_pairs = extract_word_pairs(text)
    frequencies = count_word_pair_frequencies(word_pairs)
    sentence = generate_sentence(frequencies)
    print(sentence)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate sentences using a Naive Bayes language model")
    parser.add_argument("-i", "--input", type=str, help="Input text file", required=True)
    args = parser.parse_args()
    main(args.input)