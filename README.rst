=================================
ffsm is for finite state machines
=================================

.. image:: https://badge.fury.io/py/ffsm.png
    :target: http://badge.fury.io/py/ffsm
    
.. image:: https://travis-ci.org/fanscribed/ffsm.png?branch=master
        :target: https://travis-ci.org/fanscribed/ffsm

.. image:: https://pypip.in/d/ffsm/badge.png
        :target: https://crate.io/packages/ffsm?version=latest


A finite state machine library created to support
the Fanscribed Transcription Machine, among other projects.

* Free software: BSD license
* Documentation: http://ffsm.rtfd.org.

Planned Features
----------------

- State machines defined using a straightforward "Pythonic" API:

  - Developers should be able to very easily read and write state machines.

  - Namespaces should be easy to identify.

  - Similar APIs should have symmetry where they overlap.

- Implement the general concepts of UML state machines:

  - Events, with parameters.

  - States.

  - Extended state variables.

  - Guard conditions.

  - Actions.

  - Transitions.

  - Hierarchically nested states.

- State machine introspection and visualization:

  - PlantUML-based diagrams.

  - Textual descriptions.

  - Current situation descriptions and diagrams.

- State machine versioning and migration:

  - Grandfathered state machines (continue to run using old machine schema).

  - Migrated state machines (migration paths from old machine schema).

- Modular persistence and integration:

  - In-memory persistence.

  - Django ORM integration.

  - Logging and auditing.

- Support for asynchronous transitions.

- Scalable and efficient.

  - Support millions of persisted state machines.

  - Use memory wisely.

- 100% test coverage.
