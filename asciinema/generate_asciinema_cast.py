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

import random
from typing import List, Tuple, Union

VIDEO_NEW_LINE = "\\r\\n"


class Cast:
    def __init__(self, sequence: List[Tuple[str]]):
        self._sequence = sequence

    @staticmethod
    def generate_cast_line(clock: int, content: str):
        return f'[{clock}, "o", "{content}"]\r\n'

    def generate_cast(
        self,
        speed: Union[int, float] = 0.01,
        speed_randomizer: Union[int, Tuple[int]] = (0.00, 0.05),
        newline_pause: Union[int, float] = 0.5,
        PS1: str = "$ ",
        width: int = 450,
        height: int = 300,
    ):
        cast = '{"version": 2}\r\n'
        lower_speed_randomizer, upper_speed_randomizer = (
            speed_randomizer
            if isinstance(speed_randomizer, tuple)
            else (speed_randomizer, speed_randomizer)
        )
        clock = 0
        for command, output in self._sequence:
            cast += self.generate_cast_line(clock, PS1)
            for character in command:
                clock += random.uniform(
                    speed - lower_speed_randomizer, speed + upper_speed_randomizer
                )
                cast += self.generate_cast_line(clock, character)
            cast += self.generate_cast_line(clock, VIDEO_NEW_LINE)
            clock += (
                random.uniform(
                    speed - lower_speed_randomizer, speed + upper_speed_randomizer
                )
                + newline_pause
            )
            for line in output.split("\n"):
                cast += self.generate_cast_line(clock, line + VIDEO_NEW_LINE)
        cast += self.generate_cast_line(clock + 5, PS1)
        self.content = cast
        return self

    def save(self, path: str):
        output_file = open(path, "wt")
        with open(path, "w") as output_file:
            output_file.write(self.content)
