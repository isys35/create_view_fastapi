from abc import ABC, abstractmethod


class HandlerInterface(ABC):

    @property
    @abstractmethod
    def user(self):
        pass


    @property
    @abstractmethod
    def input_type(self):
        pass