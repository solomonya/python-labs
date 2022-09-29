string = 'In the hole in the ground there lived a hobbit'


def main():
    characters_list = list(string)
    matches_list = [i for i, e in enumerate(characters_list) if e == 'h']
    matches_range = {
        "start": matches_list[0],
        "end": matches_list[len(matches_list) - 1] + 1
    }
    print(string.replace(string[slice(matches_range['start'], matches_range['end'])], ''))


main()
