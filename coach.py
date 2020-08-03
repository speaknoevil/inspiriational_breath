#!/usr/local/bin/python3
''' Takes a pickle file containing a list of inspirational quotes.
Chooses a random list string.
Sends the string via SNS to numbers listed in main(). 
Requires sns_sender and modifying numbers list. '''

from pathlib import Path
import sys
import pickle
import random
import sns_sender

def pickle_open():
    ''' Takes the first argument as a pickle file containing a list of strings and returns a list. '''
    if len(sys.argv) < 2:
        print('Error: Must give path to inspirations pickle file')
        sys.exit(2)
    my_pickle = Path(sys.argv[1])
    if my_pickle.is_file():
        with open(my_pickle, 'rb') as f:
            inspirations = pickle.load(f)
        f.close()
    else:
        print('Error: Argument must be pickle file')
        sys.exit(2)
    return inspirations

def main():
    ''' Numbers list to be filled in once in place '''
    #numbers = [ '+15555555555' ]
    inspirations = pickle_open()
    msg = random.choice(inspirations)
    [ sns_sender.sns_away(num,msg) for num in numbers ]

if __name__ == '__main__':
    main()
