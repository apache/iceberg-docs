from generate_asciinema_cast import Cast

sequence = [
    (
        "SELECT count(*) FROM taxis;",
        """237993
Time taken: 0.187 seconds, Fetched 1 row(s)""",
    ),
    (
        "DELETE FROM taxis WHERE passenger_count < 7;",
        """Time taken: 2.688 seconds""",
    ),
    (
        "SELECT count(*) FROM taxis;",
        """19514
Time taken: 0.187 seconds, Fetched 1 row(s)""",
    ),
    (
        "SELECT * FROM taxis.history;",
        """2021-11-26 16:12:03.188    2874264644797652805    NULL    true
2021-11-27 00:02:45.087    4605577096637158771    2874264644797652805    true""",
    ),
    (
        "ALTER TABLE taxis SET TBLPROPERTIES ('current-snapshot-id'='2874264644797652805');",
        """Time taken: 0.183 seconds""",
    ),
    (
        "SELECT count(*) FROM taxis;",
        """237993
Time taken: 0.107 seconds, Fetched 1 row(s)""",
    ),
]

Cast(sequence).generate_cast(PS1="spark-sql> ").save("output/time_travel.cast")
