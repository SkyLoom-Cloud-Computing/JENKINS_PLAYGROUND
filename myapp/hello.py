import fire


def hello(name="World") -> str:
    return "Hello %s" % name


if __name__ == '__main__':
    fire.Fire(hello)
