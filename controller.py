from game import Game 
import utils


class Controller:
    def __init__(self):
        self.game = None
        self.is_flow_running = False
        self.difficulty_level = 'easy'
       
    def is_users_command_a_guess(self, command):
        return utils.is_guess_number_valid(command, Game.get_number_size(self.difficulty_level))
    
    def handle_print_commands(self):
        commands_menu = {
            'start': 'starts the game',
            'help': 'displays all commands', 
            'rules': 'prints main rules',
            'history': 'display history of your moves',
            'level': 'change difficulty level',
            'finish': 'finishes the current game',
            'exit': 'closes the program'
        }
        
        for key, value in commands_menu.items():
            print(f"{key} - {value}")  

    def start_game(self):
        self.game = Game(self.difficulty_level)
        is_generate_success = self.game.generate_random_number()
        if is_generate_success:
            utils.print_with_line_breaks(f'Game started! You have 10 attempts to guess a {Game.get_number_size(self.difficulty_level)}-digit number. Good luck!')
        else:
            self.game = None

    def handle_history_command(self):
        if not self.game or not self.game.history:
            utils.print_with_line_breaks("Game has no history yet.")
        else:
            game_history = self.game.get_game_history()
            for attemp in game_history:
                print(f"{attemp}")

    def handle_help_command(self):
        utils.print_with_line_breaks('Here are all commands currently available in this program:')
        self.handle_print_commands()
       
    def handle_start_game_command(self):
        if not self.game or self.game.is_game_over:
            self.start_game()
        else:
            utils.print_with_line_breaks(
                f'The game is running. You have to finish this one to start a different game. You have {self.game.guess_count} attempts left'
            )

    def handle_exit_command(self):
        utils.print_with_line_breaks('You exited the program. To start the program, run the file again')
        self.is_flow_running = False
    
    def handle_guess_command(self, users_command):
            if not self.game:
                utils.print_with_line_breaks('Type "start" to begin the game')
            else:
                self.game.make_a_guess(users_command)
                if self.game.is_game_over:
                    utils.print_with_line_breaks('To play again, type "start." To see all commands, type "help."')
   
    def get_difficulty_level_info(self):
        utils.print_with_line_breaks(
            f"Your current difficulty level is {self.difficulty_level}. You must guess a {Game.get_number_size(self.difficulty_level)}-digit number."
        )
    
    def set_difficulty_level(self):
        self.get_difficulty_level_info()
        utils.print_with_line_breaks("To change the difficulty, type 'easy', 'medium' or 'hard'.")
        users_command = input('Write your difficulty level here: ').strip().lower()
        
        if utils.is_user_difficulty_level_valid(users_command):
            self.difficulty_level = users_command
            utils.print_with_line_breaks('Your difficulty level was updated')
            self.get_difficulty_level_info()
        else:
            utils.print_with_line_breaks('Sorry, your difficulty level is invalid. Type "level" to try again.')

    def handle_difficulty_level_command(self):
        if self.game:
            utils.print_with_line_breaks('Sorry, game is running. To change difficulty level you must finish this one and start a different game.')
            self.get_difficulty_level_info()
        else:
            self.set_difficulty_level()
    
    def handle_finish_game_command(self):
        if not self.game:
            utils.print_with_line_breaks('Game not started yet')
        else:
            self.game = None
            utils.print_with_line_breaks('This game is over. You can\'t make moves or see history. To play start a new game')

    def start_program_flow(self):
        self.is_flow_running = True
        
        commands = {
            'start': self.handle_start_game_command,
            'help': self.handle_help_command,
            'rules': Game.handle_print_rules_command,
            'history': self.handle_history_command,
            'level': self.handle_difficulty_level_command,
            'finish': self.handle_finish_game_command,
            'exit': self.handle_exit_command
        }

        while self.is_flow_running:
            users_command = utils.ask_for_input_with_line_breaks('Write your number or command here: ').strip()
            
            if users_command in commands:
                commands[users_command]()
            elif self.is_users_command_a_guess(users_command):
                self.handle_guess_command(users_command)
            else:
                utils.print_with_line_breaks('Sorry, the program couldn\'t recognize your input. Please, try again.')