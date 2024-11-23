from typing import Any

from dataset import Dataset

class Patient:

    def __init__(self, id: Any = None):
        self.id: Any = id
        self.data = Dataset()
        self.result: Any = None