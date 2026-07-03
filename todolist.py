to_do_list = input("Enter your to do list assignments, separated by commas: ")
to_do_list = to_do_list.split(",")
print("Your to do list is:")
for item in to_do_list:
    print("- " + item)
done_tasks = input("Enter the tasks you have completed from your to do list:")
done_tasks = done_tasks.split(",")
if done_tasks in to_do_list:
    to_do_list.remove(done_tasks)
    print("Task removed" or "Task done")
else:
    print("Task not found")
for item in to_do_list:
    if item in done_tasks:
        print("You have completed: " + item)
    elif "cooking " in item or "cleaning" in item:
        print("You have household chores to do.")
    elif "work" in item:
        print("You have work-related tasks to do.")
    elif "exercise" in item:
        print("You have fitness-related tasks to do.")
    else:
        print("You have other tasks to do.")



