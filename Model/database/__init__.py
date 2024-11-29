import sqlite3

from user import User


class Database:
    def __init__(self) -> None:
        self._db = sqlite3.connect(database='./assets/db.sqlite3')
        self._db.row_factory = sqlite3.Row
    
    def _make_base_query(self, query_str: str, query_params: tuple | list = (), fetch_all: bool = False, commit_needed: bool = False) -> sqlite3.Row | None:
        query_result = None

        cursor = self._db.cursor()

        try:
            cursor.execute(query_str, query_params)

            if fetch_all:
                query_result = cursor.fetchall()
            else:
                query_result = cursor.fetchone()
            
            if commit_needed:
                self._db.commit()
        except sqlite3.Error:
            print('БД: Ошибка')

        return query_result

    def get_data_by_model(self, model, fetch_all: bool = False):
        sql = f'select {", ".join(uf for uf in model.__dataclass_fields__)} from {model.__table__}'
        params = []

        for user_field in model.__dataclass_fields__:
            uf_value = getattr(model, user_field)

            if uf_value is not None:
                if 'where' not in sql:
                    sql += ' where '
                    sql += user_field + ' = ?'
                else:
                    sql += ' and ' + user_field + ' = ?'

                params.append(uf_value)

        return self._make_base_query(
            query_str=sql,
            query_params=params,
            fetch_all=fetch_all
        )
