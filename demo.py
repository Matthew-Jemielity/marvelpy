#!/usr/bin/env python3


def find_character_names_containing(string):
    print(
        "Demo will find out characters with names containing the string %s."
        % string
    )
    character_names = []
    from marvel.api.character import CharacterCollection
    all_characters = CharacterCollection()
    for character_bundle in all_characters:
        print(
            "Characters %d - %d out of %d: %s"
            % (
                character_bundle.data().offset() + 1,
                character_bundle.data().offset()
                + character_bundle.data().count() + 1,
                character_bundle.data().total() + 1,
                character_names
            )
        )
        character_names.extend(
            list(
                filter(
                    lambda name: string in name,
                    list(
                        map(
                            lambda character: character.name(),
                            character_bundle.items()
                        )
                    )
                )
            )
        )


if __name__ == "__main__":
    from sys import argv
    find_character_names_containing(argv[1] if len(argv) > 1 else "Man")
