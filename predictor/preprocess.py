from predictor.test import hello2


def hello(name: str = "World") -> None:
    print(f"Hello {name}")


if __name__ == "__main__":
    hello(name=123)
    hello2()
