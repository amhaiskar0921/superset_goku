import goku_sql_client.db

from superset.db_engine_specs.base import BaseEngineSpec
from typing import List, Tuple, Dict, Any, Optional
from superset.errors import SupersetError, SupersetErrorType
from superset.sql_parse import ParsedQuery

class GokuQLEngineSpec(BaseEngineSpec):
    engine = "gokuql"
    allows_subqueries = False
    allows_alias_in_dialect = True
    run_multiple_statements_as_one = False

    sqlalchemy_uri_placeholder = (
        "gokuql://host:port?host="
    )

    # @classmethod
    # def is_readonly_query(cls, parsed_query: ParsedQuery) -> bool:
    #     return cls.is_select_query(parsed_query.sql)

    # @classmethod
    # def is_select_query(cls, query: str) -> bool:
    #     return query.strip().lower().startswith("select")

    @classmethod
    def apply_limit_to_sql(
        cls, sql: str, limit: int, database: 'Database', force: bool = False
    ) -> str:
        return sql
    

    @classmethod
    def execute_with_cursor(cls, cursor: Any, sql: str, query) -> None:
        cursor.execute(sql)

    @classmethod
    def fetch_data(cls, cursor, limit: int) -> List[Tuple]:
        return cursor.fetchall()[:limit]

    # @classmethod
    # def expand_data(cls, columns: List[Dict[str, Any]], data: List[Tuple]) -> List[Dict[str, Any]]:
    #     return data
