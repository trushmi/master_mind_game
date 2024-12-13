def is_guess_number_valid(user_number, level):
    if len(user_number) != level:
        return False 
    for number in user_number:
        if not number.isdigit():
            return False
    return True

def is_user_difficulty_level_valid(user_level):
    difficulty_levels = ['easy','medium','hard']
    if user_level in difficulty_levels:
        return True
    else:
        return False

def is_numbers_the_same(random_number, user_number):
    if random_number == user_number: 
        return True
    return False
    
def get_correct_location_count(random_number, user_number):
    
    correct_location_count = 0
    index = 0

    while (index < len(random_number)):
        if random_number[index] == user_number[index]:
            correct_location_count += 1
        index += 1
    
    return correct_location_count

def get_correct_number_count(random_number, user_number):
    correct_number_count = 0
    random_number_dict = {} 

    for number in random_number:
        if number in random_number_dict:
            random_number_dict[number] += 1
        else: 
            random_number_dict[number] = 1

    for number in user_number:
        if number in random_number and random_number_dict[number] != 0:
            random_number_dict[number] -=1
            correct_number_count += 1 
   
    return correct_number_count

def print_with_line_breaks(msg):
    print('')
    print(msg)
   

def ask_for_input_with_line_breaks(msg):
    print('')

    return input(msg)

def compare_numbers(random_number, user_number):
    correct_location_count = get_correct_location_count(random_number, user_number)
    number_guessed_count = get_correct_number_count(random_number, user_number)
    if correct_location_count == 0 and number_guessed_count == 0:
        return f"Your guess: {user_number}. All incorrect"
    else:
        return f"Your guess: {user_number}. You have guessed {number_guessed_count} correct {'numbers' if number_guessed_count > 1 else 'number'} and {correct_location_count} correct {'locations' if correct_location_count > 1 else 'location'}"