with open("day7_input.txt", "r") as f:
    text = f.read() 

# text = """
# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
# x -> a
# """

wires_signal = {}
wires_logic_gates = {}

# Load the wires in memory
for wire in text.strip().splitlines():
    signal, identifier = wire.split("->")
    signal, identifier = signal.strip(), identifier.strip()

    if signal.isdigit():
        wires_signal[identifier] = int(signal)
        continue

    wires_logic_gates[identifier] = signal


# Update the signal of the wires
index = 0
while wires_logic_gates:
    if index >= len(list(wires_logic_gates)):
        index = 0

    identifier, logic_gate = list(wires_logic_gates.items())[index]
    index += 1

    for pair_operation in ("AND", "OR"):
        if logic_gate.count(pair_operation):
            signal1, signal2 = logic_gate.split(pair_operation)
            signal1, signal2 = signal1.strip(), signal2.strip()

            if signal1.isdigit():
                signal1 = int(signal1)
            elif signal1  in wires_signal.keys():
                signal1 = wires_signal[signal1]
            else:
                continue

            if signal2.isdigit():
                signal2 = int(signal2)
            elif signal2 in wires_signal.keys():
                signal2 = wires_signal[signal2]
            else:
                continue

            if pair_operation == "AND":
                wires_signal[identifier] = signal1 & signal2
            else:
                wires_signal[identifier] = signal1 | signal2

            wires_logic_gates.pop(identifier)

    if logic_gate.count("NOT"):
        signal = logic_gate.split(" ")[1]

        if signal in wires_signal.keys():
            wires_signal[identifier] = ~wires_signal[signal] & 0xFFFF # masks the 16 bits
            wires_logic_gates.pop(identifier)

    for shift in ("LSHIFT", "RSHIFT"):

        if logic_gate.count(shift):

            signal, movement = logic_gate.split(shift)
            signal, movement = signal.strip(), movement.strip()

            if signal in wires_signal.keys():

                if shift == "LSHIFT":
                    wires_signal[identifier] = wires_signal[signal] << int(movement)
                else:
                    wires_signal[identifier] = wires_signal[signal] >> int(movement)

                wires_logic_gates.pop(identifier)

    if not logic_gate.count(" "):
        if logic_gate in wires_signal.keys():
            wires_signal[identifier] = wires_signal[logic_gate]
            wires_logic_gates.pop(identifier)


# =============================================

new_b = wires_signal["a"]

wires_signal = {}
wires_logic_gates = {}

# Load the wires in memory
for wire in text.strip().splitlines():
    signal, identifier = wire.split("->")
    signal, identifier = signal.strip(), identifier.strip()

    if signal.isdigit():
        wires_signal[identifier] = int(signal)
        continue

    wires_logic_gates[identifier] = signal

# Override the old value of b with a 
wires_signal["b"] = new_b

# Copy and paste the code to update the wires
index = 0
while wires_logic_gates:
    if index >= len(list(wires_logic_gates)):
        index = 0

    identifier, logic_gate = list(wires_logic_gates.items())[index]
    index += 1

    for pair_operation in ("AND", "OR"):
        if logic_gate.count(pair_operation):
            signal1, signal2 = logic_gate.split(pair_operation)
            signal1, signal2 = signal1.strip(), signal2.strip()

            if signal1.isdigit():
                signal1 = int(signal1)
            elif signal1 in wires_signal.keys():
                signal1 = wires_signal[signal1]
            else:
                continue

            if signal2.isdigit():
                signal2 = int(signal2)
            elif signal2 in wires_signal.keys():
                signal2 = wires_signal[signal2]
            else:
                continue

            if pair_operation == "AND":
                wires_signal[identifier] = signal1 & signal2
            else:
                wires_signal[identifier] = signal1 | signal2

            wires_logic_gates.pop(identifier)

    if logic_gate.count("NOT"):
        signal = logic_gate.split(" ")[1]

        if signal in wires_signal.keys():
            wires_signal[identifier] = (
                ~wires_signal[signal] & 0xFFFF
            )  # masks the 16 bits
            wires_logic_gates.pop(identifier)

    for shift in ("LSHIFT", "RSHIFT"):

        if logic_gate.count(shift):

            signal, movement = logic_gate.split(shift)
            signal, movement = signal.strip(), movement.strip()

            if signal in wires_signal.keys():

                if shift == "LSHIFT":
                    wires_signal[identifier] = wires_signal[signal] << int(movement)
                else:
                    wires_signal[identifier] = wires_signal[signal] >> int(movement)

                wires_logic_gates.pop(identifier)

    if not logic_gate.count(" "):
        if logic_gate in wires_signal.keys():
            wires_signal[identifier] = wires_signal[logic_gate]
            wires_logic_gates.pop(identifier)

print(wires_signal)
print(wires_signal["a"])