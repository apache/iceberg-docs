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
        cast += self.generate_cast_line(clock+5, PS1)
        self.content = cast
        return self

    def save(self, path: str):
        output_file = open(path, "wt")
        with open(path, "w") as output_file:
            output_file.write(self.content)
