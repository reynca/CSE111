def main():
    text_list = read_list("provinces.txt")
    print(text_list)



def read_list(filename):


    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:
            if line == "AB":
                line = 'Alberta'
            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)


    # Return the list that contains the lines of text.
    return text_list



if __name__ == "__main__":
    main()