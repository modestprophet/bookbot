path_to_file = 'books/frankenstein.txt'

def main(path_to_file: str):
    text = get_text_from_file(path_to_file)
    word_count = (count_words(text))
    character_counts = count_characters(text)
    list_of_character_counts = create_list_of_dicts(character_counts)
    generate_report(word_count, list_of_character_counts)


def get_text_from_file(path_to_file: str) -> str:
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
        return file_contents


def count_words(text: str) -> int:
    words = text.split()
    word_count = len(words)
    return word_count


def count_characters(text: str) -> dict[str, int]:
    character_counts = {}
    for character in text:
        if character.isalpha():
            character_counts[character.lower()] = character_counts.get(character.lower(), 0) + 1
    return character_counts


def sort_on(dictionary):
    return dictionary["num"]


def create_list_of_dicts(dictionary: dict[str, int]) -> list[dict[str, int]]:
    list_of_dicts = []
    for key, value in dictionary.items():
        list_of_dicts.append({'character': key, 'num': value})
    return list_of_dicts


def generate_report(total_words: int, list_of_character_counts: list[dict[str, int]]) -> None:
    list_of_character_counts.sort(reverse=True, key=sort_on)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{total_words} words found in the document')
    print('')
    for character in list_of_character_counts:
        char = character['character']
        count = character['num']
        print(f"The '{char}' character was found {count} times")
    print('--- End report ---')


if __name__ == '__main__':
    main(path_to_file)