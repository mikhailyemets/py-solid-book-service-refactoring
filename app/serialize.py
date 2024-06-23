from model import Book
from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as et


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = et.Element("book")
        title = et.SubElement(root, "title")
        title.text = book.title
        content = et.SubElement(root, "content")
        content.text = book.content
        return et.tostring(root, encoding="unicode")
