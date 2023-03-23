import random

# Define a list of dictionaries, where each dictionary represents a question and its possible answers
questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["A. Berlin", "B. Paris", "C. Rome", "D. Madrid"],
        "correct_answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answers": ["A. Jupiter", "B. Mars", "C. Venus", "D. Saturn"],
        "correct_answer": "A"
    },
    {
        "question": "What is the currency of Japan?",
        "answers": ["A. Yen", "B. Won", "C. Yuan", "D. Euro"],
        "correct_answer": "A"
    },
    {
        "question": "What is the highest mountain in the world?",
        "answers": ["A. K2", "B. Mount Everest", "C. Mount Kilimanjaro", "D. Mount Rushmore"],
        "correct_answer": "B"
    },
    {
        "question": "What is the largest country in the world by land area?",
        "answers": ["A. Russia", "B. United States", "C. China", "D. Brazil"],
        "correct_answer": "A"
    }
]

# Define a function to run the quiz
def run_quiz():
    # Shuffle the questions
    random.shuffle(questions)

    # Initialize the score
    score = 0

    # Loop through each question
    for i, question in enumerate(questions):
        # Print the question
        print(f"\nQuestion {i+1}: {question['question']}")

        # Print the possible answers
        for answer in question["answers"]:
            print(answer)

        # Prompt the user for an answer
        user_answer = input("\n your answer (A, B, C, or D): ")

        # Check if the answer is correct
        if user_answer.upper() == question["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")

    # Print the final score
    print(f"\nYour score is {score} out of {len(questions)}.")

# Run the quiz
run_quiz()
