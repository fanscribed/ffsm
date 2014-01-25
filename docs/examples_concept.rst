Examples (concept)
==================


Vehicle
.......

This example is based on the example given in the
`pluginaweek state_machine <https://github.com/pluginaweek/state_machine#example>`__
README.

..  Replace --- with >>> as API forms

..  code-block:: pycon

    --- from tests.machines.vehicle_concept import Vehicle
    --- vehicle = Vehicle()

    --- vehicle.state
    'parked'

    --- vehicle.state_name
    'parked'

    --- vehicle.is_parked
    True

    --- vehicle.can_ignite
    True

    --- vehicle.ignite_transition
    <Transition attribute=state event=ignite from=parked to=idling>

    --- vehicle.state_events
    set(['ignite'])

    --- vehicle.state_transitions
    [<Transition attribute=state event=ignite from=parked to=idling>]

    --- vehicle.speed
    0

    --- vehicle.is_moving
    False

    --- vehicle.ignite()
    True

    --- vehicle.is_parked
    False

    --- vehicle.is_idling
    True

    --- vehicle.speed
    10

    --- vehicle.shift_up()
    True

    --- vehicle.speed
    10

    --- vehicle.is_moving
    True

    --- # Equivalent to ``vehicle.shift_up()``
    --- vehicle.fire_state_event('shift_up')
    True

    --- vehicle.speed
    Traceback: (AttributeError)

    --- vehicle.park()
    Traceback: (InvalidTransition)

    --- vehicle.can_transition_state('parked')
    False

    --- vehicle.can_transition_state('invalid')
    Traceback: (NameError)

    --- vehicle.alarm_state
    1

    --- vehicle.alarm_state_name
    'active'

    --- vehicle.can_disable_alarm
    True

    --- vehicle.disable_alarm()
    True

    --- vehicle.alarm_state
    0

    --- vehicle.alarm_state_name
    'off'

    --- vehicle.can_enable_alarm
    True

    --- vehicle.is_alarm_off
    True

    --- vehicle.is_alarm_active
    False

    --- vehicle.fire_events('shift_down', 'enable_alarm')
    True

    --- vehicle.state_name
    'first_gear'

    --- vehicle.alarm_state_name
    'active'

    --- vehicle.fire_events('ignite', 'enable_alarm')
    Traceback: (InvalidTransition)

    --- vehicle.state_paths()

    --- vehicle.state_paths().to_states

    --- vehicle.state_paths().events

    --- vehicle.state_paths('parked', 'first_gear')

