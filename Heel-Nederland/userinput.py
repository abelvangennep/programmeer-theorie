import sys

# raw_input returns the empty string for "enter"
yes = {'yes','y', 'ye', ''}
no = {'no','n'}

def boolean_input(user_input):
    if user_input in yes:
        user_input = True
    elif user_input in no:
        user_input = False
    else:
        sys.stdout.write("Please respond with 'yes' or 'no'")
        user_input = 3

    return user_input
