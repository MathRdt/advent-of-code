from pathlib import Path

input = open(Path(__file__).parent / "input.txt").read()
workflows = {}
accepted = []
rejected = []
workflows_string, parts_string = input.split("\n\n")
for workflow in workflows_string.splitlines():
    name, instructions = workflow.strip().replace("}", "").split("{")
    workflows[name] = instructions.split(",")

parts = []
for part_string in parts_string.splitlines():
    part = {}
    for key_value in part_string.strip().replace("{", "").replace("}", "").split(","):
        key, value = key_value.strip().split("=")
        part[key] = int(value)
    parts.append(part)


def follow_workflows(part, workflow):
    if workflow == "A":
        accepted.append(part)
        return
    if workflow == "R":
        rejected.append(part)
        return
    current_instructions = workflows[workflow]
    for index, instruction in enumerate(current_instructions):
        if index == len(current_instructions) - 1:
            follow_workflows(part, instruction)
            break
        condition, next_workflow = instruction.split(":")
        condition_key = condition[0]
        condition_comparator = condition[1]
        condition_value = int(condition[2:])

        if condition_comparator == ">":
            if part[condition_key] > condition_value:
                follow_workflows(part, next_workflow)
                break
        elif condition_comparator == "<":
            if part[condition_key] < condition_value:
                follow_workflows(part, next_workflow)
                break


for part in parts:
    follow_workflows(part, "in")

total = sum([sum(accepted_values.values()) for accepted_values in accepted])
print(total)
