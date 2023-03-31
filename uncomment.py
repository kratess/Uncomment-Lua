def uncomment(s):
    result = ""

    length = len(s)
    i = 0

    def is_multiple_init():
        if s[i] == "[":
            j = 1
            while s[i+j] == "=":
                j += 1
            if s[i+j] == "[":
                return True, j+1

        return False, None

    def is_multiple_end(l):
        if s[i] == "]":
            j = 1
            while s[i+j] == "=":
                j += 1
            if s[i+j] == "]":
                return j+1 == l

        return False

    while i < length:
        char = s[i]

        # check if starting of any time of string
        if char == "\"":
            result += s[i]
            while s[i+1] != "\"":
                i += 1
                result += s[i]
            i += 1
        elif char == "'":
            result += s[i]
            while s[i+1] != "'":
                i += 1
                result += s[i]
            i += 1
        elif char == "[":
            is_multiple, mul_length = is_multiple_init()

            result += s[i:i+mul_length]
            i += mul_length
            while i < length and not is_multiple_end(mul_length):
                result += s[i]
                i += 1
            result += s[i:i+mul_length]
            i += mul_length

        # check if starting of any type of comment
        elif char == "-":
            # check if it is really a comment
            if s[i+1] == "-":
                i += 2

                # check if multiline
                is_multiple, mul_length = is_multiple_init()

                if is_multiple:
                    i += mul_length
                    while i < length and not is_multiple_end(mul_length):
                        i += 1
                    i += mul_length
                else:
                    j = 1
                    while i+j < length and s[i+j] != "\n":
                        j += 1
                    i = i+j

        # print("char", char)

        if i < length:
            result += s[i]
        i += 1

    return result
