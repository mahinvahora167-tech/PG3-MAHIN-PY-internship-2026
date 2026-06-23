task=[]

task.append("complete python assignment")
task.append("study for exam")
task.append("wake up early")
task.append("practice python coding")
task.append("exercise for 30 minutes")

print("task after addng:")
for item in task:
    print("_",item)

task.remove("study for exam")
task.remove("wake up early")

print("\ntask after removing:")
for item in task:
    print("_",item)

