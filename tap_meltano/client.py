"""Custom client handling, including meltanoStream base class."""

from sqlalchemy import create_engine, text
from pathlib import Path
from typing import Optional, Iterable

from singer_sdk.streams import Stream


class meltanoStream(Stream):
    """Stream class for meltano streams."""

    def query(self):
        pass

    def get_records(self, context: Optional[dict]) -> Iterable[dict]:
        """Return a generator of row-type dictionary objects.

        The optional `context` argument is used to identify a specific slice of the
        stream if partitioning is required for the stream. Most implementations do not
        require partitioning and should ignore the `context` argument.
        """

        engine = create_engine(self.config["meltano_database_uri"])

        with engine.connect() as conn:
            rows = conn.execute(text(self.query())).all()

        for row in rows:
            my_row = row._asdict()
            my_dict = {}
            for key in my_row:
                if str(my_row[key]) == "None":
                    my_dict[key] = None
                else:
                    my_dict[key] = str(my_row[key])
            yield my_dict
