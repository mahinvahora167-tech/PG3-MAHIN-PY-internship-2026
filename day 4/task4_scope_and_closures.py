def task_status():
    status="pending"

    def update_status():
        nonlocal status
        print("updating task status...")
        status="completed"

    print("initial status :",status)
    update_status()
    print("final status :",status)

task_status()