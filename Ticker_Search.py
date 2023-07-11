def tickersearch(body_text):

    search_string_1 = "(NASDAQ:"
    search_string_2 = "(NYSE:"

    i = 1

    if body_text.find(search_string_1) != -1:  # If NASDAQ is found in the body of the text
        index = body_text.find(search_string_1)
        
        output = ""
        while body_text[index + len(search_string_1) + i] != ")":
            output += (body_text[index + len(search_string_1) + i]) # Incrementally add to the ticker string until ) is reached
            i += 1
        ticker = output
    elif body_text.find(search_string_2) != -1:  # If NYSE is found in the body of the text
        index = body_text.find(search_string_2)
        output = ""
        while body_text[index + len(search_string_2) + i] != ")":
            output += (body_text[index + len(search_string_2) + i]) # Incrementally add to the ticker string until ) is reached
            i += 1      
        ticker = output
    else:
        print("Ticker not found in the input. Function recursion ended")
        ticker = 'NaN'

    return ticker
