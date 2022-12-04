def text2eq(text_num, num_words={}):
    if not num_words:
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        num_words["and"] = (1, 0)
        for idx, word in enumerate(units):  num_words[word] = (1, idx)
        for idx, word in enumerate(tens):       num_words[word] = (1, idx * 10)
        for idx, word in enumerate(scales): num_words[word] = (10 ** (idx * 3 or 2), 0)

    ordinal_words = {'first': 1, 'second': 2, 'third': 3, 'fifth': 5, 'eighth': 8, 'ninth': 9, 'twelfth': 12}
    ordinal_endings = [('ieth', 'y'), ('th', '')]

    text_num = text_num.replace('-', ' ')
    text_num = text_num.replace(',', '')
    current = result = 0
    curr_string = ""
    on_num = False
    for word in text_num.split():
        if word in ordinal_words:
            scale, increment = (1, ordinal_words[word])
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
            on_num = True
        else:
            for ending, replacement in ordinal_endings:
                if word.endswith(ending):
                    word = "%s%s" % (word[:-len(ending)], replacement)

            if word not in num_words:
                if on_num:
                    curr_string += repr(result + current) + " "
                curr_string += word + " "
                result = current = 0
                on_num = False
            else:
                scale, increment = num_words[word]

                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
                on_num = True

    if on_num:
        curr_string += repr(result + current)

    operators = ["negative", "minus", "plus", "divided by", "multiplied by"]
    operator_sym = ["-", "-", "+", "/", "*"]
    for o in operators:
        if o in curr_string:
            curr_string = curr_string.replace(o, operator_sym[operators.index(o)])

    return eval(curr_string)

