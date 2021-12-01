from turing_machine import TuringMachine

initial_state = "a",
accepting_states = ["z"],
transition_function = {("a", "0"): ("b", "1", "R"),
                       ("a", "1"): ("a", "1", "R"),
                       ("b", "0"): ("c", "1", "R"),
                       ("b", "1"): ("c", "0", "L"),
                       ("c", "0"): ("d", "1", "R"),
                       ("c", "1"): ("b", "0", "R"),
                       ("d", "0"): ("z", "1", "R"),
                       ("d", "1"): ("c", "1", "L")
                       }
final_states = {"z"}

t = TuringMachine("000000000000000",
                  initial_state="a",
                  final_states=final_states,
                  transition_function=transition_function)

print("Input on Tape:\n" + t.get_tape())

while not t.final():
    t.step()

print("Result of the Turing machine calculation:")
print(t.get_tape())
