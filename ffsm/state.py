from six import add_metaclass


class state(object):

    def __repr__(self):
        return getattr(self, 'name', '<unnamed state>')


class ValidStatesMeta(type):

    def __init__(cls, what, bases=None, dict=None):
        super(ValidStatesMeta, cls).__init__(what, bases, dict)
        # Find all states.
        all_states = set()
        for name, possible_state in dict.items():
            if isinstance(possible_state, state):
                # Give each state its name.
                possible_state.name = name
                # Add to the 'all' set.
                all_states.add(possible_state)
        cls.all = frozenset(all_states)


@add_metaclass(ValidStatesMeta)
class ValidStates(object):
    pass
