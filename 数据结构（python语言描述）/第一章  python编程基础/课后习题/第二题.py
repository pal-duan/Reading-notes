

def get_salary(salary_every_hour, work_time, work_overtime):
    """
    一个雇员一周的总薪水，等于其每小时的薪水乘以一周正常工作的小时数，再加上加班费。加班费等于总的加班时间乘以每小时薪水的1.5倍
    :param salary_every_hour:
    :param work_time:
    :param work_overtime:
    :return:
    """
    return salary_every_hour * work_time + (work_overtime * salary_every_hour * 1.5)
