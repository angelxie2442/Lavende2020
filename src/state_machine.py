from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum

################################
# Modify State enum for any Quiz2 tasks as needed
################################

class State(Enum):
    START = 0
    PROMPT = 1
    MAMMAL = 2
    BIRD = 3
    REPTILE = 4
    AMPHIBIAN=5
    ERR = 6

################################

################################
# Modify ont_dict for Quiz2 Task 3
################################


ont_dict = {
              "ontology": {
                  "ontamphibian":
                      [
                      "salamander",
                      "frog"
                      ]

              }
           }

################################

knowledge = KnowledgeBase()
knowledge.load_json(ont_dict)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

df.add_system_transition(State.START, State.PROMPT, '"Enter an animal"')
df.add_user_transition(State.PROMPT, State.MAMMAL, r'<$animal={cat,dog}>')
df.add_user_transition(State.PROMPT, State.BIRD, r'<$animal={parrot,dove,crow}>')
df.add_user_transition(State.PROMPT, State.REPTILE, r'<$animal={snake,turtle,alligator,lizard}>')
df.add_user_transition(State.PROMPT,State.AMPHIBIAN, r'<$animal=#ONT(ontamphibian)>')
df.add_system_transition(State.MAMMAL, State.PROMPT, '[! $animal " is a mammal, enter another animal"]')
df.add_system_transition(State.BIRD, State.PROMPT, '[! $animal " is a bird, enter another animal"]')
df.add_system_transition(State.REPTILE, State.PROMPT, '[! $animal " is a reptile, enter another animal"]')
df.add_system_transition(State.AMPHIBIAN, State.PROMPT, '[! $animal " is a amphibian, enter another animal"]')
df.add_system_transition(State.ERR, State.PROMPT, '"i dont know that one, enter another animal"')
df.set_error_successor(State.PROMPT, State.ERR)


################################
# Add Quiz2 Task 1 below
################################



################################
# Add Quiz2 Task 2 below
################################



################################
# Add Quiz2 Task 3 below
# (except do not move ont_dict from line 11)
################################



df.run(debugging=False)