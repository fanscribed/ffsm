from six import add_metaclass

from .state import ValidStates, state


class IsCurrentStateDescriptor(object):

    def __init__(self, state):
        self._state = state

    def __get__(self, instance, owner):
        return instance.state == self._state


class CanEventOccurDescriptor(object):

    def __init__(self, event):
        self._event = event

    def __get__(self, instance, owner):
        for t in self._event.transitions:
            if t.from_ == instance.state:
                return True
        return False


class event(object):

    def __init__(self, *transitions):
        self.transitions = transitions


class transition(object):

    def __init__(self, from_, to):
        self.from_ = from_
        self.to = to


class StateMachineMeta(type):

    def __init__(cls, what, bases=None, dict=None):
        super(StateMachineMeta, cls).__init__(what, bases, dict)

        # Attach is_<state> descriptors.
        for state in cls.states.all:
            is_name = 'is_' + state.name
            setattr(cls, is_name, IsCurrentStateDescriptor(state))

        # Attach can_<event> descriptors.
        for name, possible_event in dict.items():
            if isinstance(possible_event, event):
                event.name = name
                can_name = 'can_' + name
                setattr(cls, can_name, CanEventOccurDescriptor(possible_event))


@add_metaclass(StateMachineMeta)
class StateMachine(object):

    class states(ValidStates):
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
