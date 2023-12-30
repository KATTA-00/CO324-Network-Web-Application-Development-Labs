class StateMachine:

    def __init__(self, transitions, initial_state):

        self.transitions = transitions

        self.current_state = initial_state


    def trigger(self, event):
        print(self.current_state, end=' ')

        if event in self.transitions[self.current_state]:

            self.current_state = self.transitions[self.current_state][event]

            print(self.current_state)
            return True

        else:

            print(self.current_state)
            return False


transitions = {

    'start': {'run': 'running'},

    'running': {'stop': 'stopping'},

    'stopping': {'stop': 'stopping', 'stopped': 'start'}

}


state_machine = StateMachine(transitions, 'start')

state_machine.trigger('run')

state_machine.trigger('stop')

state_machine.trigger('stopped')