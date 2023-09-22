def find_anagrams(word, word_list):
    # Helper function to check if two words are anagrams
    def are_anagrams(w1, w2):
        return sorted(w1) == sorted(w2)

    # Filter the word_list for anagrams of the given word
    anagrams = [w for w in word_list if are_anagrams(word, w)]

    return anagrams

# Example usage:
input_word_ex1 = 'abba'
input_word_list_ex1 = ['aabb', 'abcd', 'bbaa', 'dada']
result1 = find_anagrams(input_word_ex1, input_word_list_ex1)
print("Example 1 ",result1)  # Output: ['enlist', 'silent', 'stilen']

input_word_ex2 = 'racer'
input_word_list_ex2 = ['crazer', 'carer', 'racar', 'caers', 'racer']
result2 = find_anagrams(input_word_ex2, input_word_list_ex2)
print("Example 2 ",result2)  # Output: ['carer', 'racer']

input_word_ex3 = 'laser'
input_word_list_ex3 = ['lazing', 'lazy',  'lacer']
result3 = find_anagrams(input_word_ex3, input_word_list_ex3)
print("Example 2 ",result3)  # Output: []