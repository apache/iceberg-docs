# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

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
