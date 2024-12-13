# In this ReadMe:

- [About this project](#about-this-project)
- [Tech stack](#tech-stack)
- [How to use the app](#how-to-use-the-app)
- [How to run the app](#how-to-run-the-app)
- [Thought process and code structure](#thought-process-and-code-structure)

# About this project

This project is a Mastermind game where a player must guess a secret number combination within 10 attempts to win. After each attempt, the computer provides feedback to the player, guiding them toward the solution.

# Tech Stack

### Backend:

- Python 3
- PIP
- Virtual environment


### API:

- [Random Number Generator API](https://www.random.org/clients/http/api/)

# How to use the app

- Run the command python3 main.py to start the program.
- Explore commands that are available to you.
- Adjust the difficulty level from easy to hard, if needed.
- Type 'start' to begin the game and guess the randomly generated number within 10 attempts.
- Read feedback from the computer after each attempt to adjust your strategy and guess the secret number.
- Review the history of your moves and access the rules at any time.
  
# Requirements

- [Python 3.9+](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Virtual environment](https://virtualenv.pypa.io/en/latest/installation.html)

# How to run the app:

Follow the next steps to set up and run the app on your local machine:

1.  ### Clone the repository to your local machine:
    ```
    git clone https://github.com/trushmi/m_game_practice
    ```
2.  ### Navigate to your project directory:
    ```
    cd your-project-directory-name
    ```
3.  ### Setup the virtual environment to manage your project's dependencies separately:
    ```
    virtualenv env
    ```
4.  ### Activate virtual environment:

    ```
    source env/bin/activate
    ```

5.  ### Install the project requirements:
    ```
    pip3 install -r requirements.txt
    ```
6.  ### Run the program
    ```
    python3 main.py
    ```
    You should now see the program running in your console.
    If you encounter any issues, please check that all previous steps have been followed correctly.

7. ### Run tests
    ```
    python3 test_utils.py
    ```


# Thought process and code structure

## Project initiation and design decisions

I initiated this project by reviewing the provided requirements and take-home challenge guidance. 

When considering the design approach, I thought about two potential solutions: a console-based game where user input would be processed directly, or a full-stack solution using a UI.

Given that the main focus of this challenge should be on the logic that creates non-visible application behavior, not the UI side, I decided to focus on the game logic and chose a console-based implementation.

For my tech stack, I decided to use Python because it's object-oriented, uses plain language, and has robust code libraries that if needed can be reuse for future extensions of the game. 

When designing the program, I prioritized the core requirements outlined in the game rules, user interface specifications, and implementation guidelines. To enhance the program, as extention I implemented difficulty levels functionality.

## Object-Oriented design and code strutcure 

To effectively manage the program's logic, I identified three program states: the user has started the program but the game has not yet begun, the user is playing the game, and the user has finished playing the game. I also wanted a player to be able to type commands at any time during the game.

With scalability and potential future extensions of the game in mind, I decided to use an object-oriented design approach and defined two primary classes: Game and Controller.

To keep the codebase organized and maintainable, I split the functionality and program logic into different files:

- ***main***: Keeps the function to start the program.
- ***game***: Contains the defined Game class with attributes and methods, including API calls and game rules.
- ***controller***: Contains the Controller class that maintains user input, identifies whether it's a command or a guess, and controls the game flow.
- ***utils***: Validates numbers, prints messages with lines, and provides feedback to the user.
- ***test_utils***: Tests to ensure the validation of user moves works as expected.

## Functionality extension - difficulty levels

After implementing the core functionality, I extended my project with a new "level" command. This command allows users to change the difficulty level, which reflects the number of digits they need to guess. Based on their choice, the number size can be 4 (easy, default), 5, or 6. When the user changes the level, I use this information to update a parameter, "number size," which I then use to generate a random number in the API call.

To ensure stable performance, changing the level is only available before the game starts or after it finishes, allowing users to adjust the difficulty between games.

## Reflection and potential improvements

Working on this project, I regularly took the time to review my code and see if there was a way to improve it using DRY principles and best practise. One such improvement involved storing commands as keys in a dictionary and corresponding methods as values, eliminating the need for multiple "if-else if" statements.

As a result of this challenge, I have enhanced my skills in object-oriented design, working on game logic, and learned how to use the Random.com API.

Thinking about potential improvements, I would prioritize expanding the number of tests in my program. This would involve generating mock prints and function calls to enhance testing. Additionally, I would consider adding the random module as a backup in case the API fails to fetch data. This would provide a random number to the user, without the need to wait for the server if it is unavailable.

Speaking of extra functionality, I think about expanding the difficulty level configuration, allowing users to set a timer and also making the game available for two players.
