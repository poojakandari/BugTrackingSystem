import time

bugs = {}
assignments = {}

def create_bug_report(bug_id, project_id, bug_type, description, status, currtime):
    bugs[bug_id] = {
        'project_id': project_id,
        'bug_type': bug_type,
        'description': description,
        'status': status,
        'currtime': currtime
    }

def assign_bug(bug_id):
    if bug_id in bugs:
        if bug_id not in assignments:
            dev_id = input("ENTER THE DEVELOPER ID : ")
            start_time = time.asctime()
            assignments[bug_id] = {
                'dev_id': dev_id,
                'start_time': start_time,
                'end_time': None 
            }
            print(f"BUG {bug_id} ASSIGNED TO DEVELOPER {dev_id}\n")
        else:
            print(f"BUG {bug_id} ALREADY ASSIGNED\n")
    else:
        print(f"BUG {bug_id} DOES NOT EXIST\n")

def display_bugs(bug_id):
    if bug_id in bugs:
        bug_details = bugs[bug_id]
        print(f"\nBUG ID                : {bug_id}")
        print(f"BUG TYPE              : {bug_details['bug_type']}")
        print(f"DESCRIPTION           : {(bug_details['description']).upper()}")
        print(f"STATUS                : {bug_details['status']}")
        print(f"PROJECT               : {(bug_details['project_id']).upper()}")
        print(f"TIME OF CREATION      : {(bug_details['currtime']).upper()}")

        if bug_id in assignments:
            assignment_details = assignments[bug_id]
            print(f"ASSIGNED TO DEVELOPER : {assignment_details['dev_id']}")
            print(f"START TIME            : {assignment_details['start_time']}")
            if assignment_details['end_time']:
                print(f"END TIME              : {assignment_details['end_time']}")
            else:
                print("END TIME              : BUG NOT YET FIXED")
    else:
        print(f"Bug {bug_id} does not exist")
    print()

def generate_bug_summary(project_id):
    total_bugs = 0
    assigned_count = 0
    for bug_id, bug_details in bugs.items():
        if bug_details['project_id'] == project_id:
            total_bugs += 1
            if bug_id in assignments:
                assigned_count += 1
    print(f"BUG SUMMARY FOR PROJECT: {project_id}")
    print(f"TOTAL BUGS REPORTED    : {total_bugs}")
    print(f"TOTAL BUGS ASSIGNED    : {assigned_count}")
    print()

def update_bug(bug_id, upd_time):
    if bug_id in assignments:
        if bug_id in bugs:
            print("->1.FIXED\n->2.IN PROCESS\n")
            cho = int(input("ENTER YOUR CHOICE: "))
            if cho == 1:
                status_update = "FIXED"
                end_time = upd_time
                assignments[bug_id]['end_time'] = end_time
                bugs[bug_id]['status'] = status_update
                bugs[bug_id]['currtime'] = end_time
            elif cho == 2:
                status_update = "IN PROCESS"
            else:
                print("ENTER CORRECT CHOICE")
            bugs[bug_id]['status'] = status_update
            bugs[bug_id]['currtime'] = upd_time
            print(f"BUG '{bug_id}' STATUS UPDATED SUCCESSFULLY.\n")
        else:
            print(f"BUG WITH ID {bug_id} NOT FOUND.")
    else:
        print("BUG NOT YET ASSIGNED")

def delete_bug(bug_id):
    if bug_id in bugs:
        del bugs[bug_id]
        if bug_id in assignments:
            del assignments[bug_id]
        print(f"BUG WITH ID {bug_id} DELETED SUCCESSFULLY.")
    else:
        print(f"BUG WITH ID {bug_id} NOT FOUND.")

def type_of_bug():
    while True:
        print("->1.SYNTAX ERROR\n->2.RUNTIME ERROR\n->3.LOGICAL ERROR\n->4.NAME ERROR\n->5.TYPE ERROR\n->6.INDEX ERROR\n->7.ATTRIBUTE ERROR")
        choice = int(input("ENTER YOUR CHOICE: "))
        print()
        if choice == 1:
            return "SYNTAX ERROR"
        elif choice == 2:
            return "RUNTIME ERROR"
        elif choice == 3:
            return "LOGICAL ERROR"
        elif choice == 4:
            return "NAME ERROR"
        elif choice == 5:
            return "TYPE ERROR"
        elif choice == 6:
            return "INDEX ERROR"
        elif choice == 7:
            return "ATTRIBUTE ERROR"
        else:
            print("INVALID CHOICE...TRY AGAIN")

while True:
    print("-------------------------------------------------------")
    print("|\t\t1. CREATE A NEW BUG                   |")
    print("-------------------------------------------------------")
    print("|\t\t2. ASSIGN A BUG                       |")
    print("-------------------------------------------------------")
    print("|\t\t3. DISPLAY                            |")
    print("-------------------------------------------------------")
    print("|\t\t4. GENERATE BUG SUMMARY               |")
    print("-------------------------------------------------------")
    print("|\t\t5. UPDATE BUG STATUS                  |")
    print("-------------------------------------------------------")
    print("|\t\t6. DELETE A BUG                       |")
    print("-------------------------------------------------------")
    print("|\t\t7. VIEW DEV LIST                      |")
    print("-------------------------------------------------------")
    print("|\t\t8. EXIT                               |")
    print("-------------------------------------------------------")
    ch = int(input("ENTER YOUR CHOICE: "))
    print()
    if ch == 1:
        bug_id = int(input("ENTER BUG ID     : "))
        project_id = input("ENTER PROJECT ID : ")
        print("SELECT THE TYPE OF BUG")
        bug_type = type_of_bug()
        description = input("ENTER THE DESCRIPTION OF THE BUG: ")
        print()
        status = "REPORTED"
        currtime = time.asctime()
        create_bug_report(bug_id, project_id, bug_type, description, status, currtime)
    elif ch == 2:
        bug_id = int(input("ENTER THE BUG ID : "))
        assign_bug(bug_id)
    elif ch == 3:
        bug_id = int(input("ENTER BUG ID: "))
        display_bugs(bug_id)
    elif ch == 4:
        project_id = input("ENTER THE PROJECT ID : ")
        print()
        generate_bug_summary(project_id)
    elif ch == 5:
        bug_id = int(input("ENTER THE BUG ID: "))
        upd_time = time.asctime()
        update_bug(bug_id, upd_time)
    elif ch == 6:
        bug_id = int(input("ENTER THE BUG ID TO DELETE: "))
        delete_bug(bug_id)
    elif ch == 7:
        print("BUG_ID  DEV_ID \tSTART TIME\t\t\tEND TIME\t\tSTATUS")
        for bug_id, dev_details in assignments.items():
            status = bugs.get(bug_id, {}).get('status', 'Bug not found')
            print("%d\t%s\t%s\t%s\t%s" % (bug_id, dev_details['dev_id'], dev_details['start_time'], dev_details['end_time'] if dev_details['end_time'] else "Bug not fixed yet", status))
    elif ch == 8:
        print("TERMINATED SUCCESSFULLY")
        break
    else:
        print("ENTER CORRECT CHOICE..!")
