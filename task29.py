import psycopg2
import random

# https://editor.ponyorm.com/user/noth1ngt0say/hr_department/designer

request_list = ["select employee_name from employee e where e.employee_name ilike '%Garcia%'",
                "select e.employee_name, lw.organization, lw.position, lw.start_date, lw.end_date from employee e join last_work lw on e.last_work = lw.id",
                "select e.employee_name, p.title, p.salary from employee e join position p ON e.position_id = p.id",
                "select e.employee_name, v.vacation_type from employee e join vacation v on e.time_off = v.id where v.vacation_type ilike '%parental%'",
                "select e.employee_name, v.vacation_type from employee e join vacation v on e.time_off = v.id where v.vacation_type ilike '%periodic%'",
                "select e.employee_name, c.social_category from employee e join category c on e.special_category = c.id where c.social_category ilike '%retiree%'",
                "select e.employee_name, chi.c_first_name, chi.c_last_name from employee e join child chi on e.id = chi.employee_id",
                "select e.employee_name, p.salary from employee e join position p on e.position_id = p.id where p.salary > 99999",
                "select e.employee_name, p.title from employee e join position p ON e.position_id = p.id where p.title ilike '%owner%'"]

peq_ = random.randint(0, len(request_list) - 1)

conn = psycopg2.connect("dbname=hr_department user=python_code password=Passw0rd!@#")

print(f'Выполняю запрос: {request_list[peq_]}')

with conn.cursor() as cursor:
    cursor.execute(f"{request_list[peq_]};")
    results = cursor.fetchall()
    for row in results:
        print(*row)