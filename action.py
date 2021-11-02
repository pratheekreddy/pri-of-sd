# HOW TO USE ACTION:
# First import action function from action file
# Then pass a parameter i.e. command according to the need. This can be modified according to the requirements
# Point of Contact: Pratheek Keddy Katta

def check_for_success(command):

    while True:

        received = input()

        if received == 'succeeded ' + command:
            return True
        elif received.startswith('failed ' + command):
            return False
        elif received.startswith('error ' + command):
            return False


def action(command, wait=True):
    # Format command
    print('start ' + command)
    return check_for_success(command)