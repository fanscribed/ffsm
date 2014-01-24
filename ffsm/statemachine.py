from six import add_metaclass

from .state import state


class StateMachineMeta(type):

    def __init__(cls, what, bases=None, dict=None):
        super(StateMachineMeta, cls).__init__(what, bases, dict)
        # Find all states and assign them names.
        for name, possible_state in cls.states.__dict__.items():
            if isinstance(possible_state, state):
                possible_state.name = name


@add_metaclass(StateMachineMeta)
class StateMachine(object):

    class states:
        pass

    def __init__(self):
        self._state = self.initial

    def __repr__(self):
        return '<{} state={}>'.format(
            self.__class__.__name__,
            self._state.name,
        )

    @property
    def initial(self):
        # TODO: test this
        raise NotImplemented(
            'Set "initial" in StateMachine subclass to initial state')

    @property
    def state(self):
        return self._state
