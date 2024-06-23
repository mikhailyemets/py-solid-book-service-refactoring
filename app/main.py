from model import Book
from serialize import JsonSerializer, XmlSerializer
from display import DisplayConsole, DisplayReverse
from print import PrintConsole, PrintReverse


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_mapping = {
        "console": DisplayConsole(),
        "reverse": DisplayReverse()
    }
    print_mapping = {
        "console": PrintConsole(),
        "reverse": PrintReverse()
    }
    serialize_mapping = {
        "json": JsonSerializer(),
        "xml": XmlSerializer()
    }

    for cmd, method_type in commands:
        if cmd == "display":
            display_mapping[method_type].display(book)
        elif cmd == "print":
            print_mapping[method_type].print(book)
        elif cmd == "serialize":
            return serialize_mapping[method_type].serialize(book)
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
