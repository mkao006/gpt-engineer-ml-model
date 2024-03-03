import xgboost as xgb
import os

class ModelWrapper:
    def __init__(self):
        self.model = self.load_model()

    def load_model(self):
        model_path = os.getenv('MODEL_PATH', 'model.json')
        model = xgb.XGBClassifier()
        model.load_model(model_path)
        return model

    def predict(self, features):
        dmatrix = xgb.DMatrix(features)
        return self.model.predict(dmatrix)