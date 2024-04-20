import json


def alg_ss_200424_A() -> None:  # noqa: N802, D103, C901
    def has_two_vowels(phrase: str) -> bool:  # noqa: D103
        vowels = {"a", "e", "i", "o", "u", "y"}
        count = sum(1 for char in set(phrase.lower()) if char in vowels)
        return count >= 2

    def is_even_length(phrase: str) -> bool:  # noqa: D103
        return len(phrase) % 2 == 0

    output_file = "output.json"
    filename = "stdin"
    file = open(filename)  # noqa: SIM115
    filename_json = file.readline().strip()
    file.close()

    with open(filename_json) as file:
        json_str = file.read()
    parsed_json = json.loads(json_str)

    result_json = {}

    with open(filename) as file:
        file.readline()
        for line_number, transformation_type in parsed_json.items():
            phrases = file.readline().strip().split("_")

            if transformation_type == "10":
                result_json[line_number] = sorted(
                    [phrase.strip() for phrase in phrases if has_two_vowels(phrase)],
                    reverse=True,
                )
            elif transformation_type == "20":
                result_json[line_number] = sorted(
                    [phrase.strip() for phrase in phrases if is_even_length(phrase)],
                    reverse=True,
                )
            else:
                result_json[line_number] = sorted(
                    [phrase.strip() for phrase in phrases], reverse=True
                )

    file.close()

    with open(output_file, "w") as json_file:
        json.dump(result_json, json_file, indent=4)


alg_ss_200424_A()
