tasks=[]
while True:
    print("\n1.Add a task")
    print("2.View all tasks")
    print("3.Delete a task")
    print("4.quit") 
    choice=int(input("Enter your choice: "))
    if choice==1:
     task=input("enter a task:")
     tasks.append(task)
    elif choice==2:
     if len(tasks)==0:
        print ("you haven't added any goals yet")
     else:
        print("your tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
    elif choice==3:
   
     task=input("enter the task to be deleted")
     if task in tasks:
         tasks.remove(task)
         print("task deleted")
    else:
        break     


                

    

