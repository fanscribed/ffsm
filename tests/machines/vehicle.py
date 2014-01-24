from ffsm import StateMachine, state


class Vehicle(StateMachine):

    class states:
        parked = state()

    initial = states.parked

