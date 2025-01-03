from ast import List, Tuple


def find_anagram(word: str, data: list[str]) -> list:

    words_that_matches: List[Tuple[int, int]] = []

    word = word.lower().strip()
    letters_of_word = [char for char in word if char.isalpha()]

    for i in range(len(data)):

        compare_word = data[i].lower().strip()
        letters_to_compare = [char for char in compare_word if char.isalpha()]

        diff = len(letters_of_word) - len(letters_to_compare)

        letters_to_ignore = []
        letter_counter = 0
        for j in range(len(letters_of_word)):
            if diff > 1 or diff < 1:
                break
            for n in range(len(letters_to_compare)):
                if (
                    letters_of_word[j] == letters_to_compare[n]
                    and n not in letters_to_ignore
                ):
                    letter_counter += 1
                    letters_to_ignore.append(n)
                    break

        if diff == 1 and letter_counter == len(letters_of_word) - 1:
            words_that_matches.append((i, letter_counter))
    return words_that_matches
