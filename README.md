# Perfect City

## Purpose:
A terminal-based Python app that helps users find the best cities to live in based on their climate and population preferences.

## How It Works
1-Data dir:
This is the dir to store the attributes of various cities.
    a-CityAttributes.csv:
        This is where the data for each city is stored the app takes these datas and compares it with user inputs and gives each city a score based on the differences.
    b-TestAttributes.csv:
        This is the same list but for test functions therefore any extra city that doesn't have a unique attribute is deleted this is to make testing easier and to make sure
        tests dont break if we add or change city attributes in the original file.

2-Src dir:
This is where python codes are.
    a-Ai.py:
        This is the file where the program's ai logic resides.
            ------------------------------------------------------------------
            create_system_prompt creates a system prompt for the ai based on the
            list it has been given this is made it so we dont need to hardcode the prompt in main function since thats when we know what the final list is and therefore makes it easier if we want to create different system prompts for different ai functions in the future.
            -------------------------------------------------------------------
            use_ai is where our main ai logic is.It takes the global messages and console attributes it uses bunch of global variables since these need to saved between each function call.I then prints an answer based on the conversation it is havig with the user or the system prompt it has been given
    b-Attributes.py:
        This is the file where the attributes that other programs use are at.
            --------------------------------------------------------------------
            Attributes is an enum class which has a representation for each of the attributes a city has in the data files.
            --------------------------------------------------------------------
            create_values_list is a function that creates a list of all possible values a given attribute can have. 
    c-input.py:
        This is the file that stores the functions that takes inputs from the users.
            --------------------------------------------------------------------
            input_and_calculate is the main function in this file it is used to calculate and update each city's score based on the inputs it takes from the users
            --------------------------------------------------------------------
            take_input is the function that is used to take the user's preferences for the given attribute and how important this attribute is for them and returns the preference-importance value to the input_and_calculate function
            --------------------------------------------------------------------
            take_importance is the function that takes the importance value from the user and make sure the input is valid
            --------------------------------------------------------------------
            replay_question is the funciton that validates the users input on whether or not to replay the questions and converts this input to the boolean value


    

    