from greet import greet


def test_greet_world():
 assert greet("world") == "Hello, world."


def test_greet_harish():
 assert greet("Harish") == "Hello, Harish."
