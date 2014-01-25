import datetime


class _dummy_(object):
    def __init__(self, *args, **kw):
        pass
class state_machine(_dummy_): pass
class state(_dummy_): pass
class ANY(_dummy_):
    def __sub__(self, other):
        pass
class SAME(_dummy_): pass
class failure(_dummy_): pass


class Vehicle(object):

    @state_machine
    def state(self, machine):
        machine.initial = 'parked'

        machine.before_transition('parked', ANY - 'parked',
                                  self.put_on_seatbelt)

        machine.after_transition('on', 'crash', self.tow)
        machine.after_transition('on', 'repair', self.fix)
        @machine.after_transition(ANY, 'parked')
        def take_off_seatbelt(vehicle, transition):
            self.seatbelt_on = False

        machine.after_failure('on', 'ignite', self.log_start_failure)

        @machine.around_transition(ANY, ANY)
        def increment_time_used(vehicle, transition):
            start = datetime.datetime.now()
            transition()
            vehicle.time_used += datetime.datetime.now() - start

        @machine.event
        def park(transition):
            transition.when({'idling', 'first_gear'}, 'parked')

        @machine.event
        def ignite(transition):
            transition.when([
                ('stalled', SAME),
                ('parked', 'idling'),
            ])

        @machine.event
        def idle(transition):
            transition.when('first_gear', 'idling')

        @machine.event
        def shift_up(transition):
            transition.when([
                ('idling', 'first_gear'),
                ('first_gear', 'second_gear'),
                ('second_gear', 'third_gear'),
            ])

        @machine.event
        def shift_down(transition):
            transition.when([
                ('third_gear', 'second_gear'),
                ('second_gear', 'first_gear'),
            ])

        @machine.event
        def crash(transition):
            transition.when(ANY - {'parked', 'stalled'}, 'stalled',
                            only_if=lambda vehicle: vehicle.passed_inspection)

        @machine.event
        def repair(transition):
            # The first transition that matches the state
            # and passes its conditions will be used.
            transition.when('stalled', 'parked',
                            unless=lambda vehicle: vehicle.auto_shop_busy)
            transition.when('stalled', SAME)

        machine.attribute_when('parked', speed=0)
        machine.attribute_when({'idling', 'first_gear'}, speed=10)

        @machine.property_when(ANY - {'parked', 'stalled', 'idling'})
        def is_moving():
            return True

        @machine.property_when({'parked', 'stalled', 'idling'})
        def is_moving():
            return False

    @state_machine()
    def alarm_state(self, machine):
        machine.initial = 'active'
        machine.namespace = 'alarm'

        @machine.event
        def enable(transition):
            transition.when(ANY, 'active')

        @machine.event
        def disable(transition):
            transition.when(ANY, 'off')

        machine.value_when('active', 1)
        machine.value_when('off', 0)

    def __init__(self):
        self.seatbelt_on = False
        self.time_used = datetime.timedelta()
        self.auto_shop_busy = True

    def put_on_seatbelt(self):
        self.seatbelt_on = True

    @property
    def passed_inspection(self):
        return False

    def tow(self):
        # Tow the vehicle
        pass

    def fix(self):
        # Get the vehicle fixed by a mechanic
        pass

    def log_start_failure(self):
        # log a failed attempt to start the vehicle
        pass
