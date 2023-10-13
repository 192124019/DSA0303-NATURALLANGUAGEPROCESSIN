from gensim.summarization import summarize

# Get user input
user_input = input("Enter the text you want to summarize: ")

# Perform extractive summarization
summary = summarize(user_input)

# Print the summary
print("Summary:")
print(summary)
