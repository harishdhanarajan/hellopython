import sys


def greet(name: str) -> str:
 """Return a greeting string for the given name."""
 return f"Hello, {name}."


if __name__ == "__main__":
 name = sys.argv[1] if len(sys.argv) > 1 else "world"
 print(greet(name))
