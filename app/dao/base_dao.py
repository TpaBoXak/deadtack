from flask_sqlalchemy.pagination import QueryPagination
from flask_sqlalchemy.query import Query

from app import db


class BaseDao:
    model = None
    
    def get_or_paginate(self, select_args, page=None, per_page=None,
                        where_args = None, order_args = None, join_args = None, outer_join_args=None,
                        group_args=None, select_from=None) -> Query:
        if select_from:
            query: Query = db.session.query(*select_args).select_from(select_from)
        else:
            query: Query = db.session.query(*select_args)
        if where_args:
            query: Query = query.where(*where_args)
        if join_args:
            for join_arg in join_args:
                query: Query = query.join(*join_arg)
        if outer_join_args:
            for outer_join_arg in outer_join_args:
                query: Query = query.outerjoin(*outer_join_arg)
        if group_args:
            query: Query = query.group_by(*group_args)
        if order_args:
            query: Query = query.order_by(*order_args)

        if page and per_page:
            paginated_query: QueryPagination = query.paginate(page=page, per_page=per_page)
            return paginated_query

        return query