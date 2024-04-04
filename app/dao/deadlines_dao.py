from sqlalchemy import func
from sqlalchemy import and_
from sqlalchemy.orm import aliased

from app.dao.base_dao import BaseDao
from app.models.deadlines import Deadline

from utils import data_transfer

from app import db

class DeadlineDao(BaseDao):
    def __init__(self) -> None:
        self.session = db.session

    def new_deadline(self, deadline_info: dict) -> tuple:
        try:
            deadline: Deadline = Deadline()
            deadline.name = deadline_info["name"]
            end_date = data_transfer. \
                    isostr_to_datetime(time_str=deadline_info["date"])
            deadline.end_date = end_date
            deadline.priority = deadline_info["priority"]
            self.session.add(deadline)
        except:
            self.session.rollback()
            data = {"massege": "Что-то пошло не так"}
            return data, 500
        else:
            self.session.commit()
            data = {"massege": "Все окей"}
            return data, 200
        

    def get_all_deadline(self) -> list:
        select_args = [Deadline.id, Deadline.name,
                Deadline.end_date, Deadline.priority]
        
        deadlines_tuple: list[tuple] = self. \
                get_or_paginate(select_args=select_args).all()
        deadlines: list = []
        for row in deadlines_tuple:
            date: str = data_transfer.date_to_dateiso(time=row[2])
            if date is None:
                return None
            deadline = {
                "id": row[0],
                "name" : row[1],
                'date' : date,
                'priority' : row[3]
            }

            deadlines.append(deadline)
        return deadlines
    
    def update_deadline(self, deadline_id, deadline_info) -> tuple:
        try:
            select_args = [Deadline]
            where_args = [Deadline.id == deadline_id]

            deadline: Deadline = self.get_or_paginate(select_args=select_args,
                    where_args=where_args).first()
            
            if deadline is None:
                data = {"massege": "Ошибка входных данных id"}
                return data, 500
            
            end_date = data_transfer. \
                    isostr_to_datetime(time_str=deadline_info["date"])
            if end_date is None:
                data = {"massege": "Ошибка входных данных data"}
                return data, 500
            
            deadline.name = deadline_info["name"]
            deadline.end_date = end_date
            deadline.priority = deadline_info["priority"]
            self.session.add(deadline)
        except:
            self.session.rollback()
            data = {"massege": "Что-то пошло не так"}
            return data, 500
        else:
            self.session.commit()
            data = {"massege": "Все окей"}
            return data, 200
        
    def delete_deadline(self, deadline_id) -> tuple:
        try:
            select_args = [Deadline]
            where_args = [Deadline.id == deadline_id]

            deadline: Deadline = self.get_or_paginate(select_args=select_args,
                    where_args=where_args).first()
            
            if deadline is None:
                data = {"massege": "Ошибка входных данных"}
                return data, 500

            self.session.delete(deadline)
        except:
            self.session.rollback()
            data = {"massege": "Что-то пошло не так"}
            return data, 500
        else:
            self.session.commit()
            data = {"massege": "Все окей"}
            return data, 200