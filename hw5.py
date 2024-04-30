import streamlit as st
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

def main():
    st.title("Sentence Generator")

    st.write('## Input File')
    input_file_name = st.text_input('Enter input file name')

    output_file_name = st.text_input('Enter output file name (optional)')

    if st.button("Generate Sentence"):
        try:
            with open(input_file_name, 'r') as f:
                text = f.read()
            
            word_pairs = extract_word_pairs(text)
            frequencies = count_word_pair_frequencies(word_pairs)
            generated_sentence = generate_sentence(frequencies)
            
            if output_file_name:
                with open(output_file_name, 'w') as f:
                    f.write(generated_sentence)
                st.success(f"Sentence generated and written to {output_file_name}")
            else:
                st.write("Generated Sentence:", generated_sentence)
        except FileNotFoundError:
            st.error("Input file not found.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()