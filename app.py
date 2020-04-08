import libsm
import logging

# set logging level
logging.basicConfig(level=logging.INFO)


# fi: init function
#     init function returns a set (libsm.Value) of initial state
#     the only initial state in this example is `{}`


def fi():
    return libsm.Value(
        libsm.Value(),
    )

# fn: next function
#     next function returns a set (libsm.Value) of next state
#     the only next state in this example `{}` whatever the previous state is


def fn(value):
    return libsm.Value(
        libsm.Value(),
    )


sm = libsm.SM(fi, fn)
states, transitions = sm.result()

print(states)
print(transitions)
