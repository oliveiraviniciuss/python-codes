def main():
    string_brackets = "{{[[(())]]}}"
    print check_brackets_string_format(string_brackets)

def check_brackets_string_format(string_brackets):
    is_formated = True
    string_length = len(string_brackets)
    if string_length % 2 == 0:
        for current_index in range(string_length/2):
            #decrease the current index_ to compare mirrored positions
            if not check_caracteres(string_brackets[current_index], string_brackets[(-1 -current_index)]):
                is_formated = False
        return is_formated
    return False

def check_caracteres(character_one, caracter_two):
    if character_one in ['(', '{', '[']:
        if ((character_one == '(' and caracter_two == ')') or 
            (character_one == '[' and caracter_two == ']') or
            (character_one == '{' and caracter_two == '}')):
            return True
    return False


if __name__ == '__main__':
    main()

