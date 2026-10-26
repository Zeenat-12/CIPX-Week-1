from animal import get_random_animal
from ai import call_gpt

def main():
    # Choose a random animal
    animal = get_random_animal()
    
    # Print the initial message to the user
    print("I am thinking of an animal.")
    print("Can you guess what animal it is?")

    # Get their first guess
    question = input("Ask me a yes or no question: ")

    # Use GPT to get a yes, no, or correct
    prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. Please respond with exactly Yes, No, or Correct if they guess the animal exactly. Do not say anything else."
    gpt_response = call_gpt(prompt)
    
    # Keep letting the user guess as long as its not correct
    while gpt_response != "Correct":
        # Output GPT's response
        print(f"{gpt_response}.")

        # Get the next question
        question = input("Ask me a yes or no question, or type hint: ")

        # Use GPT to get a clue or the response
        if question == "hint":
            prompt = f"Give a short clue about a {animal} in a few words, without saying what it is. Do not end with a period."
        else:
            prompt = f"We are playing twenty questions and the answer is {animal}. The user has asked the following yes or no question: {question}. Please respond with exactly Yes, No, or Correct if they guess the animal exactly. Do not say anything else."
        gpt_response = call_gpt(prompt)
    
    print("Correct!")

if __name__ == "__main__":
    main()
