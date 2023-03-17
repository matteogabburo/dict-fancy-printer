from dict_pretty_printer.pretty_printer import PrettyPrinter


def pretty_dict(d: dict) -> str():
    """Given a python dictionary, return a formatted string"""
    printer = PrettyPrinter()
    return printer(d)


def print_pretty_dict(d: dict) -> None:
    """Given a python dictionary, it prints it in pretty way"""
    print(pretty_dict(d), end="")
