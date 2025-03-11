from openaiClient import initMessages, appendUserMessage, completion, processCompletion, create_embedding, appendMessage
from pineconeClient import find_top_k


def main():
    messages = initMessages()
    while True:
        user_input = input("> ")
        appendUserMessage(messages, user_input)
        top_matches = find_top_k(create_embedding(user_input))
        print(top_matches)
        appendMessage(messages, str(top_matches), 'developer')
        model_completion = completion(messages)
        processCompletion(messages, model_completion)


main()

