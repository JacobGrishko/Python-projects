import nltk
from nltk.corpus import words,wordnet
import random


def print_help():
    print("""
    Welcome to randomNick. Here you can choose get a random nickname. I was inspired to make this 
    
        -h          For help, printing the current message.
        -t          Type : 1-Adjective + Noun 2-Verb +"er" 3-Just a random word.
        -n          Number of nicknames to print, maximum number of 20.
        -r          Repeat until 'exit' is writen
        -c          Include curse words.
        -l          leet text. For example "1337" instead to "leet" or "3Xamp13" instead of "Example".
        -u          Use your own list of words. Include full path to the text file. The words will be seperated by spaces.
        -d          Include definition for the words (If availible)
        -i          for interactive mode.
        """)

def get_words():
    word_list = words.words()
    print ("you have {0} words".format(len(word_list)))
    print(len(word_list))
    return word_list

def gen_rand(list):
    rand = random.randrange(1, len(list))
    return list[rand]

def gen_adjective(list):
    while(True):
        tokanized_rand = nltk.word_tokenize(list[random.randrange(1, len(list))])
        adj = nltk.pos_tag(tokanized_rand)
        if adj[0][1] == 'JJ':
            try:
                print("{0} - {1}".format(adj[0][0], get_def(adj[0][0])))
            except:
                print("couldnt find definition")
            return adj[0][0]

def gen_noun(list):
    while(True):
        tokanized_rand = nltk.word_tokenize(list[random.randrange(1, len(list))])
        noun = nltk.pos_tag(tokanized_rand)
        if noun[0][1] == 'NN':
            try:
                print("{0} - {1}".format(noun[0][0], get_def(noun[0][0])))
            except:
                print("couldnt find definition")
            return noun[0][0]

def gen_verb(list):
    while(True):
        tokanized_rand = nltk.word_tokenize(list[random.randrange(1, len(list))])
        verb = nltk.pos_tag(tokanized_rand)
        if verb[0][1] == 'VB':
            try:
                print("{0} - {1}".format(verb[0][0], get_def(verb[0][0])))
            except:
                print("couldnt find definition")
            return verb[0][0]

def get_def(word):
    syns = wordnet.synsets(word)
    return syns[0].definition()

def gen_nick():
    nltk.download('words')
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    word_list = get_words()

    adj = gen_adjective(word_list)
    noun = gen_noun(word_list)
    verb = gen_verb(word_list)

    nick = adj+noun.capitalize()
    print(verb)
    print("new nickname: "+nick)

    print("***nickname***")

def interactive():
    #introduction
    print("[+]hello, this is an interactive mode. You will be asked some questions.\n "
          "if the answer is not valid, it will defauld.")
    inp = input("[+]Do you want to get a random nickname? [yes/no]\n")
    if inp == 'yes':
        print("[+]alright cool.")
    else:
        print("[+]I guess its a no. bye then.")
        return

    #type
    inp = input('[+]Here are some nickname options. Pick the option number you like:'
                '1. Adjective + Noun.'
                '2. Verb +"er" '
                '3. Just a random word.')
    if inp == 1:
        opt = 1
    elif inp == 2:
        opt = 2
    else:
        opt = 3

    #all words/ known words/ private list
    inp = input("[+]Would you like to use all existing words? most common words? or your own list of words?"
                "(A - all, C - common, O - your own list")
    if inp == 'C' or inp == 'c':
        words = 2
        print("Common it is.")
    elif inp == 'O' or inp == 'o':
        words = input("Your own list it is.. Write the full path to that file please:")
    else:
        words = 1
        print("Using all words. Theres a chance that you will not recognize many of them.")

    #curse?
    inp = input("[+]would you like to include curse words? It wont be too explicit [yes/no]")
    if inp == 'yes':
        curse = True
        print("[+]Alright Alright Alright.")
    else:
        curse = False
        print("no cursing then.")

    #include definition
    inp = input("[+]would you like a definition of the word? (if availible) [yes/no]")
    if inp == 'yes':
        definition = True
    else:
        definition = False

    #leet
    inp = input("[+]Would You like to leet the nickname?[yes/no]")
    if inp == 'yes':
        leet = True
    else:
        leet = False

    #one try or as many as needed?
    inp = input("[+]Wanna gamble and try only once? or generate until you are satisfied or inspired? [o- once/ m-many]")
    if inp == 'o' or inp == 'O' or inp == 'once':
        repeat = False
    else:
        repeat = True
        print("Ok so press any key to repeat or type 'exit' to stop")


if __name__ == '__main__':
    gen_nick()
    # interactive()
