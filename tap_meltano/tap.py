"""meltano tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th


from tap_meltano.streams import (
    JobStream,
)

STREAM_TYPES = [
    JobStream,
]


class Tapmeltano(Tap):
    """meltano tap class."""

    name = "tap-meltano"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "meltano_database_uri",
            th.StringType,
            required=True,
            description="Meltano Database URI you want to get jobs from",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
