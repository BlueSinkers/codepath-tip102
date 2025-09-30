
"""
Questions I would ask to help understand question:
1. What happens if I get something that doesn't fit in the command?
2. What happens if I get an empty list?

Plan in plain English (pseudocode):
Initialize a stack. Keep adding schedules to stack. Cancel the most recent stack by popping should that come and store it in a new stack. When reschedule comes, go through the other stack and add the most recently cancelled event back into the plan. Return the list as a stack. Deal with appropriate edgecases as well with cancelling or rescheduling when there is nothing to cancel or reschedule.

Begin problem:
"""

def manage_stage_changes(changes):
    scheduled = []
    canceled = []
    
    for action in changes:
        if action.startswith("Schedule "):
            _, perf_id = action.split()
            scheduled.append(perf_id)
        elif action == "Cancel":
            if scheduled:
                canceled.append(scheduled.pop())
        elif action == "Reschedule":
            if canceled:
                scheduled.append(canceled.pop())
    
    return scheduled

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 