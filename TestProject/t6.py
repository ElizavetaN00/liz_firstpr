def file_data(filename):
    try:
        with open(filename, 'r') as file:
            data = file.readlines()

        lines_count = len(data)
        words_count = 0
        letters_count = 0

        for line in data:
            words_count += len(line.split())
            letters_count += (len(line) - line.count(" ")
                              - line.count("\n"))

        result = (
            f"Amount of lines is: {lines_count}, "
            f"amount of words is: {words_count}, "
            f"amount of letters is: {letters_count}"
        )


        with open(filename, 'a') as file:
            file.write(result)

        print(result)

    except FileNotFoundError:
        print(f"File '{filename}' is not found")


file_data("Forest.txt")