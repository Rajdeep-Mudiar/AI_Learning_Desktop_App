import pytest
import httpx
from main import app

@pytest.mark.asyncio
async def test_mlp_simulation():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        payload = {
            "layer_sizes": [2, 4, 1],
            "activation": "relu",
            "learning_rate": 0.1,
            "epochs": 50,
            "dataset_type": "xor"
        }
        resp = await ac.post("/api/v1/deep-learning/mlp/simulate", json=payload)
        assert resp.status_code == 200
        data = resp.json()
        assert len(data["layers"]) == 3
        assert len(data["loss_history"]) > 0
        assert len(data["weights"]) == 2
        assert len(data["sample_forward"]) == 2
        assert len(data["decision_boundary"]["grid_z"]) == 25

@pytest.mark.asyncio
async def test_cnn_convolution():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        payload = {
            "kernel_name": "sobel_horizontal",
            "pooling_type": "max",
            "stride": 1,
            "padding": 0
        }
        resp = await ac.post("/api/v1/deep-learning/cnn/convolve", json=payload)
        assert resp.status_code == 200
        data = resp.json()
        assert len(data["kernel"]) == 3
        assert len(data["feature_map"]) > 0
        assert data["pooled_map"] is not None
        assert "Convolved" in data["formula_explanation"]

@pytest.mark.asyncio
async def test_transformer_attention():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        payload = {
            "sentence": "Attention mechanism powers modern large language models",
            "num_heads": 4,
            "d_model": 32
        }
        resp = await ac.post("/api/v1/deep-learning/transformer/attention", json=payload)
        assert resp.status_code == 200
        data = resp.json()
        assert len(data["tokens"]) == 7
        assert len(data["heads"]) == 4
        assert len(data["average_attention"]) == 7
        assert len(data["average_attention"][0]) == 7
        assert "Scaled Dot-Product Attention" in data["formula_explanation"]
