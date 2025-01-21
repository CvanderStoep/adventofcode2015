from dataclasses import dataclass


@dataclass
class Reindeer:
    name: str
    speed: int
    fly_time: int
    rest_time: int


def parse_reindeers(content):
    reindeers = []

    for line in content:
        # Splitting the line by whitespace
        parts = line.split()

        # Extracting relevant data
        name = parts[0]
        speed = int(parts[3])
        fly_time = int(parts[6])
        rest_time = int(parts[13])

        # Creating a Reindeer object and adding it to the list
        reindeer = Reindeer(name, speed, fly_time, rest_time)
        reindeers.append(reindeer)

    return reindeers
