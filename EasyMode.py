from animal import get_random_animal
from ai import call_gpt

def main():
    # Let the player pick a mode
    mode = input("Easy mode? Type yes or no: ")
    if mode == "yes":
        rules = "Answer Yes or No, then add a short clue, like: No, but it has stripes. If they guess the animal exactly, say only Correct."
    else:
        rules = "Please respond with exactly Yes, No, or Correct if they guess the animal exactly. Do not say anything else."

    # Choose a random animal
    animal = get_random_animal()
    
    # Print the initial message to the user
    print("I am thinking of an animal.")
    print("Can you guess what animal it is?")

    # Get their first guess
    question = input("Ask me a yes or no question: ")

    # Use GPT to get a yes, no, or correct
    prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. {rules}"
    gpt_response = call_gpt(prompt)
    
    # Keep letting the user guess as long as its not correct
    while gpt_response != "Correct":
        # Output GPT's response
        print(f"{gpt_response}.")

        # Get the next question
        question = input("Ask me a yes or no question: ")

        # Use GPT to get the response
        prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. {rules}"
        gpt_response = call_gpt(prompt)
    
    print("Correct!")

if __name__ == "__main__":
    main()
