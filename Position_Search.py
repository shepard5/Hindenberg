def Hindenburg_Position(body_text):
    search_string = "Initial Disclosure: After extensive research, we have taken a short position"
    index = body_text.find(search_string)  # Find the index of the search string in the input string

    if index == -1:
        position = 0
    else:
        position = 1

    return position
