"""
This module provides the `BaseDataHandler` class, which serves as a base
class for handling data read/write operations.

The `BaseDataHandler` class defines an abstract interface for reading from
and writing to various data sources such as XML-files, JSON-files, databases, etc.

It is designed to be extended by subclasses that implement the specific
mechanisms for interacting with different data sources.

Usage:
    To create a custom data handler, subclass `BaseDataHandler` and implement its abstract methods.
"""

from abc import ABC, abstractmethod
from models.dry_cleaning import DryCleaning


class BaseDataHandler(ABC):
    """
    A base class for handling data read/write operations to and from various data sources.

    This class defines an abstract interface that must be extended by subclasses that implement
    the specific logic for reading from and writing to different data sources, such as XML-files,
    JSON-files, or databases.

    Subclasses must implement the following methods:
        - `read_data(source)`: Reads data from the specified source.
        - `write_data(destination, data)`: Writes data to the specified destination.
    """

    date_format: str = "%d.%m.%Y"

    def __init__(
        self, data_source: DryCleaning = None, input_val: str = "", output_val: str = ""
    ) -> None:
        self._data_source: DryCleaning = data_source
        self._input: str = input_val
        self._output: str = output_val

    @property
    def data_source(self) -> DryCleaning:
        return self._data_source

    @data_source.setter
    def data_source(self, data_source: DryCleaning) -> None:
        self._data_source = data_source

    @property
    def input(self) -> str:
        return self._input

    @input.setter
    def input(self, value: str) -> None:
        self._input = value

    @property
    def output(self) -> str:
        return self._output

    @output.setter
    def output(self, value: str) -> None:
        self._output = value

    @abstractmethod
    def read(self) -> None:
        pass

    @abstractmethod
    def write(self) -> None:
        pass

    def str_to_bool(self, value: str) -> bool:
        return value.lower() in ["true", "1", "t", "yes", "y"]
