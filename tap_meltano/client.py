"""SQL client handling.

This includes MeltanoStream and MeltanoConnector.
"""

from __future__ import annotations

from singer_sdk import SQLConnector, SQLStream
from typing_extensions import override


class MeltanoConnector(SQLConnector):
    """Connects to the Meltano SQL source."""

    def get_sqlalchemy_url(self, config):
        return config["meltano_database_uri"]

    @override
    def discover_catalog_entry(
        self,
        engine,
        inspected,
        schema_name,
        table_name,
        is_view,
        *,
        reflected_columns=None,
        reflected_pk=None,
        reflected_indices=None,
    ):
        return super().discover_catalog_entry(
            engine,
            inspected,
            None,  # prevent unnecessary schema prefix, as everything should only ever be in a single schema
            table_name,
            is_view,
            reflected_columns=reflected_columns,
            reflected_pk=reflected_pk,
            reflected_indices=reflected_indices,
        )


class MeltanoStream(SQLStream):
    """Stream class for Meltano streams."""

    connector_class = MeltanoConnector
