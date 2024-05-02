from abc import ABC, abstractmethod
from typing import Any
from dry_cleaning import DryCleaning


class BaseDataHandler(ABC):
    """
    Base class for handling operations of reading/writing
    data from/to differect data sources such as
    XML-file, databases, etc.
    """

    def __init__(
        self, data_source: DryCleaning = None, input_val: str = "", output_val: str = ""
    ) -> None:
        self._data_source = data_source
        self._input = input_val
        self._output = output_val

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
