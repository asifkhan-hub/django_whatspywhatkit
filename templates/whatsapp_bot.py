import pywhatkit as kit
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Initialize NLTK lemmatizer
lemmatizer = WordNetLemmatizer()

# Sample responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm just a chatbot, but I'm here to help!",
    "bye": "Goodbye! If you have more questions, feel free to ask."
}

def chatbot_response(message):
    message = message.lower()
    words = word_tokenize(message)
    words = [lemmatizer.lemmatize(word) for word in words]
    
    response = None
    for word in words:
        if word in responses:
            response = responses[word]
            break
    
    if response is None:
        response = "I'm sorry, I don't understand that. Can you please rephrase?"
    
    return response

# Main function to send and receive messages
def main():
    print("WhatsApp Chatbot is running...")
    # Replace with the recipient's phone number and the message to start the conversation
    kit.sendwhatmsg("+1234567890", "Hello, this is your WhatsApp Chatbot!", 0, 1)

    while True:
        # Replace with your WhatsApp number
        incoming_messages = kit.check_for_new_messages("+1234567890", 1)
        
        for message in incoming_messages:
            sender, content, time = message.split("|")
            response = chatbot_response(content)
            
            # Send the response
            kit.sendwhatmsg(sender, response, 0, 1)
            print(f"Sent to {sender}: {response}")

if __name__ == "__main__":
    main()
