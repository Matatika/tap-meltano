"""SQL client handling.

This includes MeltanoStream and MeltanoConnector.
"""

from __future__ import annotations

from singer_sdk import SQLConnector, SQLStream


class MeltanoConnector(SQLConnector):
    """Connects to the Meltano SQL source."""

    def get_sqlalchemy_url(self, config):
        return config["meltano_database_uri"]


class MeltanoStream(SQLStream):
    """Stream class for Meltano streams."""

    connector_class = MeltanoConnector
