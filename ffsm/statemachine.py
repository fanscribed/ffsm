from six import add_metaclass

from .state import state


class IsCurrentStateDescriptor(object):

    def __init__(self, state):
        self._state = state

    def __get__(self, instance, owner):
        return instance.state == self._state


class StateMachineMeta(type):

    def __init__(cls, what, bases=None, dict=None):
        super(StateMachineMeta, cls).__init__(what, bases, dict)
        # Find all states.
        for name, possible_state in cls.states.__dict__.items():
            if isinstance(possible_state, state):
                # Give each state its name.
                possible_state.name = name
                # Attach an is_<state> descriptor to the class.
                is_name = 'is_' + name
                setattr(cls, is_name, IsCurrentStateDescriptor(possible_state))


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
