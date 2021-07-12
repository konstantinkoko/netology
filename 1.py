task_counter = 3
task_list = {}
for task in range(task_counter):
    task_date = input('Введите дату ')
    task_text = input('Введите задачу ')
    if task_date not in task_list:
        task_list[task_date] = []
    task_list[task_date].append(task_text)
for task_date in task_list:
    print(task_date, *task_list[task_date)