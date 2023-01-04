import re
import long_response as lr


# Let check the probability of appearance of word in a sentence and compare the
# percent the higher percent the best match

def message_probability(user_message, recognised_words, single_response=False,
                        require_words=None):
    if require_words is None:
        require_words = []
    message_certain = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certain += 1

    # Calculate the percentage of recognised word in user input message
    percentage = float(message_certain) / float(len(recognised_words))

    for word in require_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_message(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=None):
        if required_words is None:
            required_words = []
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses list
    response('Hello!how are you doing', ['hello', 'hi', 'hey', 'sup', 'whats up', ], single_response=True)
    response('Im doing fine,and you?', ['how ', 'are ', 'you '], required_words=['how', 'you'])
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('My Creator Erick Wilfred Made me', ['who', 'made', 'you'], required_words=['who', 'made'])
    response('That sound good,how can i help you?', ['am', 'fine'], single_response=True)
    response('You are welcome,am glad to be helpfully to you', ['thank'], single_response=True)
    response(lr.R_EATING, ['what', 'you', 'eat', 'like'], required_words=['like', 'eat'])
    response(lr.R_TELLMEJOKE, ['tell', 'me', 'a', 'joke'], required_words=['tell', 'joke'])
    response(lr.R_LIFE, ['tell', 'me', 'about', 'life'], required_words=['life', 'love'])
    response(lr.R_CREATOR, ['who ', 'is', 'Erick'], required_words=['erick'])
    best_match = max(highest_prob_list, key=highest_prob_list.get)

    # print(highest_prob_list)     #if you want to print the percentage for debugging uncomment this
    return lr.unknown_question() if highest_prob_list[best_match] < 1 else best_match


# Checking for sign and non letters characters
def get_response(user_input):
    split_message = re.split(r"\s+|[,;?!._-]\s*", user_input.lower())
    response = check_all_message(split_message)
    return response


# Starting point for chat
while True:
    try:
        print("BOT:", get_response(input("You:")))
    except KeyboardInterrupt:
        print("\nBOT:Goodbye")
        exit()
