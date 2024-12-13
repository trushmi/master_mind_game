import requests
import utils


class Game:
    def __init__(self, difficulty_level='easy'):
        self._random_number = None
        self.history = []
        self.guess_count = 10
        self.difficulty_level = difficulty_level
        self.is_game_over = False

    def get_random_number(self):
        return self._random_number
    
    def print_greet_msg(self):
        utils.print_with_line_breaks(f'Welcome to your game. Your task is to guess the {Game.get_number_size(self.difficulty_level)} digit number. You have {self.guess_count} attempts. Good luck!')
    
    @staticmethod
    def get_number_size(difficulty_level):
        difficulty_levels_config = {
            'easy': 4,
            'medium': 5,
            'hard': 6
        }
        return difficulty_levels_config.get(difficulty_level, 4)
    
    def generate_random_number(self):
        url = 'https://www.random.org/integers/?'
        params = {
            'num': Game.get_number_size(self.difficulty_level), 
            'min': 0, 
            'max': 7, 
            'col': 1, 
            'base': 10, 
            'format': 'plain', 
            'rnd': 'new'
        }
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                generated_number = response.text.strip().replace('\n',"")
                self._random_number = generated_number
                return True
            else:
                raise requests.RequestException(f"{response.status_code} {response.text}")
        except requests.RequestException as e:
            utils.print_with_line_breaks(f"Error: {str(e)}")
            utils.print_with_line_breaks("Try to start the game later")
            return False
        
    
    def handle_game_victory(self):
        utils.print_with_line_breaks('You won the game! Congrats!!')
        self.history.append({f'Attempt {10 + 1 - self.guess_count}': f'You guessed the correct number! It was: {self.get_random_number()}'})
        self.is_game_over = True
    
    def handle_game_over(self, feedback):
        utils.print_with_line_breaks(f'Game over. The correct number was: {self.get_random_number()}')
        self.history.append({f'Attempt {10 + 1 - self.guess_count}': f'{feedback}'})
        self.history.append(f'Game is over. The correct number was: {self.get_random_number()}')
        self.is_game_over = True
    
    @staticmethod
    def handle_print_rules_command():
        main_rules = [
            'By default, you must guess the 4 digit number. Digits will be in range from 0 to 7 included. Example: 1234',
            'Duplicate digits are possible',
            'You have 10 attempts per one game',
            'After each attempt you will receive a feedback how many correct digits and correct locations you have guessed and number of attempts left.',
            'Feedback example: Your guess: 1234. You have guessed 2 correct numbers and 1 correct location. You have 8 attempts left',
            'Program recognizes only the following commands: help, rules, history, start, level, finish, exit',
            'Punctuation is not allowed',
            'You can change the difficulty level of your game. By default, your game is set to level "easy" and you have to guess the 4-digit number. Level "medium" would be 5-digit number, and level "hard" would be 6',
            'You can change level of difficulty only before the game started',
            'To change level of difficulty type "level" command',
            'Your guess cannot contain letters',
        ]
        utils.print_with_line_breaks("These are main rules:")
        for rule in main_rules:
            print(rule)
    
    def get_game_history(self):
        return self.history
    
    def make_a_guess(self, users_number):
        if self.is_game_over:
            utils.print_with_line_breaks('This game is finished. You could start a new one, if you want to play again')
            return
            
        random_number = self.get_random_number()
        if utils.is_numbers_the_same(random_number, users_number):
            self.handle_game_victory()
        elif self.guess_count == 1:
            feedback = utils.compare_numbers(random_number, users_number)
            self.handle_game_over(feedback)       
        else:
            self.guess_count -= 1
            feedback = utils.compare_numbers(random_number, users_number)
            utils.print_with_line_breaks(feedback)
            print(f'You have {self.guess_count} attempts left')
            self.history.append({f'Attempt {10 - self.guess_count}': f'{feedback}'})