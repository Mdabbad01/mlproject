import os
import sys
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score
from src.exceptions import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting training and test data")

            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1],
            )

            models = {
                "Linear Regression": LinearRegression(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest": RandomForestRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
            }

            model_report = {}
            best_model_name = None
            best_model_score = -float("inf")
            best_model = None

            for name, model in models.items():
                logging.info(f"Training model: {name}")
                model.fit(X_train, y_train)

                y_pred = model.predict(X_test)
                score = r2_score(y_test, y_pred)

                model_report[name] = score
                logging.info(f"{name} R2 Score: {score}")

                if score > best_model_score:
                    best_model_score = score
                    best_model_name = name
                    best_model = model

            logging.info(f"Best model found: {best_model_name} with R2 score: {best_model_score}")

            if best_model is None:
                raise CustomException("No suitable model found", sys)

            # Save best model
            os.makedirs(os.path.dirname(self.model_trainer_config.trained_model_file_path), exist_ok=True)
            save_object(self.model_trainer_config.trained_model_file_path, best_model)
            logging.info(f"Model saved at {self.model_trainer_config.trained_model_file_path}")

            return best_model_score

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    from src.components.data_transformation import DataTransformation
    from src.components.data_ingestion import DataIngestion

    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()

    transformation = DataTransformation()
    train_arr, test_arr, _ = transformation.initiate_data_transformation(train_path, test_path)

    trainer = ModelTrainer()
    print(trainer.initiate_model_trainer(train_arr, test_arr))
