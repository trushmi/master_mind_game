from controller import Controller
import utils


def start_program():
    utils.print_with_line_breaks(f'Welcome to the Mastermind game! Here are the commands you need to know to get started: ')
    controller = Controller()
    controller.handle_print_commands()
    controller.start_program_flow()
    
if __name__ == "__main__":
    start_program()