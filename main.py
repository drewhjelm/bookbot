def sort_on(dict):
    return dict["count"]


def main():
    path_to_file="books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        lowered_string = file_contents.lower()
        char_dict = dict.fromkeys(set(lowered_string),0)
        for char in lowered_string:
            char_dict[char] += 1
        
        count_words = len(lowered_string.split())
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words} words found in the document")
        print("")

        list_chars = []

        for item in char_dict:
            new_dict = {}
            if item.isalpha():
                new_dict['letter'] = item
                new_dict['count'] = char_dict[item]
                list_chars.append(new_dict)
        
        list_chars.sort(reverse=True, key=sort_on)

        for item in list_chars:
            print(f"The '{item['letter']}' character was found {item['count']} times")


main()