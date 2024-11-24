from typing import Any

from dataset import Dataset

from pandas import DataFrame

class Patient:
    """
    A class to represent a patient.
    Attributes
    ----------
    id : Any, optional
        The unique identifier for the patient (default is None).
    data : Dataset
        The dataset associated with the patient.
    _result : DataFrame, optional
        The result dataframe containing diagnosis prediction (default is None).
    Methods
    -------
    result:
        Property that gets the diagnosis prediction from the result dataframe.
    result(value: DataFrame):
        Setter that sets the result dataframe.
    """

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
