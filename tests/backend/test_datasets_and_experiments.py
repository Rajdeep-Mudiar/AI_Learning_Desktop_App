import pytest
import httpx
from main import app

@pytest.mark.asyncio
async def test_dataset_catalog_and_profile():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        # 1. Catalog list
        resp = await ac.get("/api/v1/datasets")
        assert resp.status_code == 200
        datasets = resp.json()
        assert len(datasets) >= 4
        dataset_ids = [d["id"] for d in datasets]
        assert "iris" in dataset_ids
        assert "breast_cancer" in dataset_ids
        assert "california_housing" in dataset_ids

        # 2. Detailed Profile
        profile_resp = await ac.get("/api/v1/datasets/iris")
        assert profile_resp.status_code == 200
        profile = profile_resp.json()
        assert profile["name"] == "Iris Flower Classification"
        assert profile["num_rows"] == 150
        assert profile["num_columns"] == 5
        assert profile["target_column"] == "species"
        assert len(profile["columns_summary"]) == 5
        assert profile["correlation_matrix"] is not None
        assert "setosa" in profile["class_distribution"]

@pytest.mark.asyncio
async def test_custom_dataset_upload():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        csv_data = "feature_a,feature_b,label\n1.2,3.4,positive\n2.1,4.5,positive\n5.0,1.1,negative\n6.2,0.9,negative\n"
        upload_payload = {
            "name": "Custom Test Dataset",
            "description": "Custom binary test dataset",
            "task_type": "classification",
            "target_column": "label",
            "csv_content": csv_data
        }
        resp = await ac.post("/api/v1/datasets/upload", json=upload_payload)
        assert resp.status_code == 200
        data = resp.json()
        assert data["num_rows"] == 4
        assert data["target_column"] == "label"
        assert len(data["features"]) == 2

@pytest.mark.asyncio
async def test_model_training_and_comparison():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        # 1. Train Classification Model (Random Forest on Iris)
        clf_payload = {
            "dataset_id": "iris",
            "model_type": "random_forest_classifier",
            "task_type": "classification",
            "hyperparameters": {
                "n_estimators": 50,
                "max_depth": 4
            },
            "preprocessing": {
                "scaling": "standard",
                "imputation": "mean",
                "test_size": 0.2
            },
            "experiment_name": "Test RF Classifier"
        }
        clf_resp = await ac.post("/api/v1/experiments/train", json=clf_payload)
        assert clf_resp.status_code == 200
        clf_data = clf_resp.json()
        assert clf_data["metrics"]["accuracy"] > 0.8
        assert clf_data["confusion_matrix"] is not None
        assert len(clf_data["confusion_matrix"]["labels"]) == 3
        assert len(clf_data["feature_importances"]) > 0
        exp_id_1 = clf_data["id"]

        # 2. Train Regression Model (Ridge on Diabetes)
        reg_payload = {
            "dataset_id": "diabetes",
            "model_type": "ridge_regression",
            "task_type": "regression",
            "hyperparameters": {
                "alpha": 1.0
            },
            "preprocessing": {
                "scaling": "standard",
                "imputation": "mean",
                "test_size": 0.2
            },
            "experiment_name": "Test Ridge Regression"
        }
        reg_resp = await ac.post("/api/v1/experiments/train", json=reg_payload)
        assert reg_resp.status_code == 200
        reg_data = reg_resp.json()
        assert "mse" in reg_data["metrics"]
        assert "r2_score" in reg_data["metrics"]
        exp_id_2 = reg_data["id"]

        # 3. List Experiments
        list_resp = await ac.get("/api/v1/experiments")
        assert list_resp.status_code == 200
        exps = list_resp.json()
        assert len(exps) >= 2

        # 4. Compare Experiments
        cmp_resp = await ac.post("/api/v1/experiments/compare", json={"experiment_ids": [exp_id_1, exp_id_2]})
        assert cmp_resp.status_code == 200
        cmp_data = cmp_resp.json()
        assert len(cmp_data["experiments"]) == 2
