from ffsm import StateMachine, state


class Vehicle(StateMachine):

    parked = state()

    initial = parked

