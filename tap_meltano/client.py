"""SQL client handling.

This includes MeltanoStream and MeltanoConnector.
"""

from __future__ import annotations

from singer_sdk import SQLConnector, SQLStream
from typing_extensions import override

KNOWN_TABLES = {
    "alembic_version",
    "embed_tokens",
    "job",  # meltano<=2.1
    "oauth",
    "plugin_settings",
    "role",
    "role_permissions",
    "roles_users",
    "runs",  # meltano>=2.2
    "state",
    "subscriptions",
    "user",
}


class MeltanoConnector(SQLConnector):
    """Connects to the Meltano SQL source."""

    def get_sqlalchemy_url(self, config):
        return config["meltano_database_uri"]

    @override
    def discover_catalog_entries(self, *args, **kwargs):
        for entry in super().discover_catalog_entries(*args, **kwargs):
            if (table_name := entry["table_name"]) not in KNOWN_TABLES:
                self.logger.info(
                    "'%s' is not a known Meltano table, skipping",
                    table_name,
                )
                continue

            yield entry

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
        catalog_entry = super().discover_catalog_entry(
            engine,
            inspected,
            None,  # prevent unnecessary schema prefix, as everything should only ever be in a single schema
            table_name,
            is_view,
            reflected_columns=reflected_columns,
            reflected_pk=reflected_pk,
            reflected_indices=reflected_indices,
        )
        catalog_entry.metadata.root.selected_by_default = True

        return catalog_entry


class MeltanoStream(SQLStream):
    """Stream class for Meltano streams."""

    connector_class = MeltanoConnector
