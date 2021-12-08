"""Stream type classes for tap-meltano."""

from pathlib import Path

from singer_sdk import typing as th

from tap_meltano.client import meltanoStream


class JobsStream(meltanoStream):
    """Jobs stream."""

    name = "jobs"
    replication_key = "id"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("job_id", th.StringType),
        th.Property("state", th.StringType),
        th.Property("started_at", th.DateTimeType),
        th.Property("ended_at", th.DateTimeType),
        th.Property("payload", th.StringType),
        th.Property("payload_flags", th.StringType),
        th.Property("run_id", th.StringType),
        th.Property("trigger", th.StringType),
        th.Property("last_heartbeat_at", th.DateTimeType),
    ).to_dict()
