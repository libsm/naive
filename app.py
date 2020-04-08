from libsm import Value, SM
from logging import basicConfig, INFO

# set logging level
basicConfig(level=INFO)


# fi: init function
#     init function returns a set (Value) of initial state
#     the only initial state in this example is `{}`


def fi():
    return Value(
        Value(),
    )

# fn: next function
#     next function returns a set (Value) of next state
#     the only next state in this example `{}` whatever the previous state is


def fn(value):
    return Value(
        Value(),
    )


sm = SM(fi, fn)
states, transitions = sm.result()

print(states)
print(transitions)
