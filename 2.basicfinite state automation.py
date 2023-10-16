class FSA:
    def __init__(self):
        self.states = {'q0': {'a': 'q1', 'b': 'q2'},
                       'q1': {'a': 'q1', 'b': 'q2'},
                       'q2': {'a': 'q1', 'b': 'q2'}}
        self.start_state = 'q0'
        self.accept_states = ['q2']

    def accept(self, string):
        current_state = self.start_state
        for char in string:
            if char in self.states[current_state]:
                current_state = self.states[current_state][char]
            else:
                return False
        return current_state in self.accept_states

# Test the FSA
fsa = FSA()

# Get input from user
user_input = input("Enter a string: ")

# Check if the string is accepted by the FSA
if fsa.accept(user_input):
    print("The string is accepted by the automaton.")
else:
    print("The string is not accepted by the automaton.")
