from functools import reduce
from pathlib import Path
import copy

input = open(Path(__file__).parent / "input.txt").read()
workflows = {}
starting_range = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
workflows_string, parts_string = input.split("\n\n")
for workflow in workflows_string.splitlines():
    name, instructions = workflow.strip().replace("}", "").split("{")
    workflows[name] = instructions.split(",")

accepted = []


def follow_workflows(part_range, workflow, id):
    if workflow == "A":
        accepted.append(part_range)
        return
    if workflow == "R":
        return

    current_instructions = workflows[workflow]
    unaffected_range = copy.deepcopy(part_range)
    for index, instruction in enumerate(current_instructions):
        if index == len(current_instructions) - 1:
            affected_range = copy.deepcopy(unaffected_range)
            follow_workflows(affected_range, instruction, id + 1)
            return
        condition, next_workflow = instruction.split(":")
        condition_key = condition[0]
        condition_comparator = condition[1]
        condition_value = int(condition[2:])
        if condition_comparator == ">" and condition_value < unaffected_range[condition_key][1]:
            # x  > 10 where range = [20, 40]
            if unaffected_range[condition_key][0] > condition_value:
                affected_range = copy.deepcopy(unaffected_range)
                follow_workflows(affected_range, next_workflow, id + 1)
                return
            # x  > 20 where range = [10, 40]
            else:
                affected_range = copy.deepcopy(unaffected_range)
                affected_range[condition_key] = [condition_value + 1, unaffected_range[condition_key][1]]
                unaffected_range[condition_key] = [unaffected_range[condition_key][0], condition_value]
                follow_workflows(affected_range, next_workflow, id + 1)

        elif condition_comparator == "<" and condition_value > unaffected_range[condition_key][0]:
            # x  < 50 where range = [20, 40]
            if unaffected_range[condition_key][1] < condition_value:
                affected_range = copy.deepcopy(unaffected_range)
                follow_workflows(affected_range, next_workflow, id + 1)
                return
            # x  < 20 where range = [10, 40]
            else:
                affected_range = copy.deepcopy(unaffected_range)
                affected_range[condition_key] = [unaffected_range[condition_key][0], condition_value - 1]
                unaffected_range[condition_key] = [condition_value, unaffected_range[condition_key][1]]
                follow_workflows(affected_range, next_workflow, id + 1)


follow_workflows(starting_range, "in", 0)
possibilities = 0
for accepted_range in accepted:
    accepted_range_possibilites = [value_range[1] - value_range[0] + 1 for value_range in accepted_range.values()]
    print(accepted_range_possibilites)
    possibilities += reduce((lambda x, y: x * y), accepted_range_possibilites)
print(possibilities)
