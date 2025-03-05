from openaiClient import initMessages, appendUserMessage, completion, processCompletion


def main():
    messages = initMessages()
    while True:
        user_input = input("> ")
        appendUserMessage(messages, user_input)
        model_completion = completion(messages)
        processCompletion(messages, model_completion)


main()

