from pathlib import Path
import queue
import copy

input = open(Path(__file__).parent / "input.txt").read()
modules = {}
for line in input.splitlines():
    current_module, next_modules = line.split(" -> ")
    if current_module == "broadcaster":
        module_type = "broadcaster"
        module_name = "broadcaster"
        state = False
    else:
        module_type = current_module[0]
        module_name = current_module[1:]
        if module_type == "&":
            state = {}
        elif module_type == "%":
            state = True
        else:
            raise Exception("unkown module type")

    modules[module_name] = {"type": module_type, "state": state, "next": tuple(next_modules.split(", "))}

conjonctions = [k for k, v in modules.items() if v["type"] == "&"]

for module_name, module_values in modules.items():
    intersections = [conj for conj in module_values["next"] if conj in conjonctions]
    for intersection in intersections:
        modules[intersection]["state"][module_name] = False

high_pulses = 0
low_pulses = 0
current_iteration = 1
for _ in range(1000):
    operations = queue.Queue()
    operations.put(("broadcaster", False, "button"))

    while not operations.empty():
        module_name, pulse_type, input = operations.get()
        if pulse_type == False:
            low_pulses += 1
        else:
            high_pulses += 1
        if (current_module := modules.get(module_name)) is None:
            continue
        if current_module["type"] == "broadcaster":
            for next_module in current_module["next"]:
                operations.put((next_module, False, module_name))
        elif current_module["type"] == "%" and pulse_type == False:
            current_module["state"] = not current_module["state"]
            for next_module in current_module["next"]:
                operations.put((next_module, not current_module["state"], module_name))
        elif current_module["type"] == "&":
            current_module["state"][input] = pulse_type
            next_pulse_type = True
            if all({state for state in current_module["state"].values()}):
                next_pulse_type = False
            for next_module in current_module["next"]:
                operations.put((next_module, next_pulse_type, module_name))
    current_iteration += 1

print(high_pulses * low_pulses)
