import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

with open('intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

FILE = 'data.pth'
data = torch.load(FILE)
input_size = data['input_size']
output_size = data['output_size']
tags = data['tags']
hidden_size = data['hidden_size']
all_words = data['all_words']
model_state = data['model_state']

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Juan"
print("Let's try use the bot! Type 'quit' to exit.")


def response_setence(setence):
    if setence in 'stop':
        return 'Beleza, depois eu volto ein😈👾'
    else:
        setence = tokenize(setence)
        X = bag_of_words(setence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X)

        output = model(X)
        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if prob.item() > 0.50:
            for intent in intents['intents']:
                if tag == intent['tag']:
                    return random.choice(intent['responses'])
        else:
            print(f"The setence i dont understand. setence: {setence}")
