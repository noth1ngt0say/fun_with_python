from sqlalchemy import text
from task31_model import User, db, app

user = User(username='noth1ngt0say', f_name='Max', l_name='Max', email='neon_war@bk.ru', age=36,
            last_work='OOO "Рога и копыта"', hard_skills='Python, HTML, CSS, Postress',
            soft_skills='Усидчивость, Целеустремленость, Проактивность, Руководство', salary_expectations='3000$')

with app.app_context():
    #     # db.session.add(user)
    #     # db.session.commit()

    sql = text('select username, last_work from "user" where id = :id;')
    result = db.session.execute(sql, {"id": 1})
    print(result)
    for i in result:
        print(i)
