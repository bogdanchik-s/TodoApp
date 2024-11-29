import sqlite3

from .user import User


class Database:
    def __init__(self, db_file_path: str = './data/db.sqlite3') -> None:
        self._db = sqlite3.connect(database=db_file_path)
        self._db.row_factory = sqlite3.Row
    
    def _make_base_query(self, query_str: str, query_params: tuple | list | dict = (), fetch_all: bool = False, commit_needed: bool = False) -> sqlite3.Row | None:
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

        cursor.close()

        return query_result

    def get_data_by_model(self, model, extra_fields: dict = None, fetch_all: bool = False):
        sql = f'select {", ".join(uf for uf in model.__dataclass_fields__)} from {model.__table__}'
        params = {}

        for user_field in model.__dataclass_fields__:
            uf_value = getattr(model, user_field)

            if uf_value is not None:
                if 'where' not in sql:
                    sql += ' where '
                    sql += user_field + ' = :' + user_field
                else:
                    sql += ' and ' + user_field + ' = :' + user_field

                params[user_field] = uf_value

        if extra_fields is not None:
            for ef_name, ef_value in extra_fields.items():
                if ef_value is not None:
                    if 'where' not in sql:
                        sql += ' where '
                        sql += ef_name + ' = ?'
                    else:
                        sql += ' and ' + ef_name + ' = :' + ef_name
                    
                    params[ef_name] = ef_value

        result = self._make_base_query(
            query_str=sql,
            query_params=params,
            fetch_all=fetch_all
        )

        if result is not None:
            return model.__class__(**result)
