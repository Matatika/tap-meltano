"""Meltano tap class."""

from __future__ import annotations

from singer_sdk import SQLTap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_meltano.client import MeltanoStream


class TapMeltano(SQLTap):
    """Meltano tap class."""

    name = "tap-meltano"
    default_stream_class = MeltanoStream

    config_jsonschema = th.PropertiesList(
        th.Property(
            "meltano_database_uri",
            th.StringType,
            required=True,
            description=(
                "Meltano system database URI. Defaults to the `meltano.db` SQLite "
                "database, assuming the working directory is a Meltano project. "
                "See https://docs.meltano.com/concepts/project/#system-database for more information."
            ),
            default="sqlite:///.meltano/meltano.db",
        ),
    ).to_dict()


if __name__ == "__main__":
    TapMeltano.cli()
