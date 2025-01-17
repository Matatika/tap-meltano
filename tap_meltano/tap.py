"""meltano tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_meltano.streams import MeltanoJobsStream

STREAM_TYPES = [
    MeltanoJobsStream,
]


class TapMeltano(Tap):
    """meltano tap class."""

    name = "tap-meltano"

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

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
