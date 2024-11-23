from typing import Any

from dataset import Dataset

from pandas import DataFrame

class Patient:

    def __init__(self, id: Any = None):
        self.id: Any = id
        self.data: Dataset = Dataset()
        self._result: DataFrame = None

    @property
    def result(self) -> int:
        return self._result.loc[0, "Diagnosis_Prediction"]
    
    @result.setter
    def result(self, value: DataFrame):
        if value is None:
            self._result = None
        self._result = value
