from fastapi import APIRouter, HTTPException
from app.schemas.deep_learning import (
    MLPSimulationRequest,
    MLPSimulationResponse,
    CNNConvolveRequest,
    CNNConvolveResponse,
    TransformerAttentionRequest,
    TransformerAttentionResponse
)
from app.services.deep_learning_service import (
    simulate_mlp,
    convolve_2d,
    compute_transformer_attention
)

router = APIRouter(prefix="/deep-learning", tags=["Deep Learning"])

@router.post("/mlp/simulate", response_model=MLPSimulationResponse)
async def run_mlp_simulation(req: MLPSimulationRequest):
    """Simulate MLP forward pass, backprop loss curve, and 2D decision boundary mesh."""
    try:
        return simulate_mlp(req)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MLP simulation error: {str(e)}")

@router.post("/cnn/convolve", response_model=CNNConvolveResponse)
async def run_cnn_convolution(req: CNNConvolveRequest):
    """Apply 2D spatial convolution kernel filter and pooling layer."""
    try:
        return convolve_2d(req)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"CNN convolution error: {str(e)}")

@router.post("/transformer/attention", response_model=TransformerAttentionResponse)
async def run_transformer_attention(req: TransformerAttentionRequest):
    """Compute multi-head scaled dot-product self-attention matrices across NLP sentence tokens."""
    try:
        return compute_transformer_attention(req)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Transformer attention error: {str(e)}")
