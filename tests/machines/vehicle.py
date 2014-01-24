from ffsm import StateMachine, ValidStates, event, state, transition


class Vehicle(StateMachine):

    class states(ValidStates):
        parked = state()
        idling = state()

    initial = states.parked

    def __init__(self):
        super(Vehicle, self).__init__()
        self.seatbelt_on = False

    # @before_transition(states.parked, states.all - {states.parked})
    # def put_on_seatbelt(self):
    #     self.seatbelt_on = True

    ignite = event(
        transition(states.parked, states.idling),
    )
