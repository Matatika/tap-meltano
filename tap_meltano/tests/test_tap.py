"""Tests the tap against a test database"""

import unittest
import singer_sdk._singerlib as singer
import os

from tap_meltano.tap import TapMeltano

SINGER_MESSAGES = []


def accumulate_singer_messages(message):
    """function to collect singer library write_message in tests"""
    SINGER_MESSAGES.append(message)


class TestTapMeltano(unittest.TestCase):
    def setUp(self):
        db = os.path.abspath("tap_meltano/tests/example_database/meltano.db")
        db = f"sqlite:///{db}"
        self.mock_config = {"meltano_database_uri": db}

        del SINGER_MESSAGES[:]
        singer.write_message = accumulate_singer_messages

    def test_tap(self):
        tap = TapMeltano(config=self.mock_config)

        tap.sync_all()

        self.assertEqual(len(SINGER_MESSAGES), 10)
