import os
from typing import List, Optional, Tuple, cast

import joblib
from sklearn.pipeline import Pipeline


class CategoryPrediction:
    model: Optional[Pipeline] = None
    targets: Optional[List[str]] = None

    def load_model(self):
        """Loads the model"""
        model_file = os.path.join(os.path.dirname(__file__), "newsgroups_model.joblib")
        loaded_model: Tuple[Pipeline, List[str]] = joblib.load(model_file)
        model, targets = loaded_model
        self.model = model
        self.targets = targets

    def predict(self, input: str) -> str:
        """Runs a prediction"""
        if self.model is None or self.targets is None:
            self.load_model()
        model = cast(Pipeline, self.model)
        targets = cast(List[str], self.targets)
        prediction = model.predict([input])
        return targets[prediction[0]]
