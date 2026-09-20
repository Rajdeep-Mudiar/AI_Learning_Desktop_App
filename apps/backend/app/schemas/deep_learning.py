from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

# --- MLP Schemas ---

class MLPSimulationRequest(BaseModel):
    layer_sizes: List[int] = Field(default=[2, 4, 4, 1], min_length=2, max_length=6)
    activation: str = "relu"  # "relu", "sigmoid", "tanh", "leaky_relu"
    learning_rate: float = Field(default=0.05, gt=0, le=1.0)
    epochs: int = Field(default=100, ge=10, le=500)
    dataset_type: str = "xor"  # "xor", "circles", "moons", "spiral"

class LayerWeightMatrix(BaseModel):
    layer_idx: int
    weights: List[List[float]]
    biases: List[float]

class ForwardStep(BaseModel):
    layer_idx: int
    pre_activations: List[float]
    post_activations: List[float]

class DecisionBoundaryGrid(BaseModel):
    grid_x: List[float]
    grid_y: List[float]
    grid_z: List[List[float]]

class MLPSimulationResponse(BaseModel):
    layers: List[int]
    weights: List[LayerWeightMatrix]
    loss_history: List[float]
    accuracy_history: List[float]
    final_accuracy: float
    sample_forward: List[ForwardStep]
    decision_boundary: DecisionBoundaryGrid
    data_points: List[Dict[str, Any]]


# --- CNN Schemas ---

class CNNConvolveRequest(BaseModel):
    kernel_name: str = "sobel_horizontal"  # "sobel_horizontal", "sobel_vertical", "edge_detect", "sharpen", "gaussian_blur", "ridge", "custom"
    custom_kernel: Optional[List[List[float]]] = None
    pooling_type: str = "max"  # "max", "average", "none"
    stride: int = Field(default=1, ge=1, le=3)
    padding: int = Field(default=0, ge=0, le=2)

class CNNConvolveResponse(BaseModel):
    kernel: List[List[float]]
    input_matrix: List[List[float]]
    feature_map: List[List[float]]
    pooled_map: Optional[List[List[float]]] = None
    formula_explanation: str


# --- Transformer Schemas ---

class TransformerAttentionRequest(BaseModel):
    sentence: str = "The transformer model calculates attention weights across tokens"
    num_heads: int = Field(default=4, ge=1, le=8)
    d_model: int = Field(default=32, ge=8, le=128)

class AttentionHeadMatrix(BaseModel):
    head_idx: int
    attention_weights: List[List[float]]

class TransformerAttentionResponse(BaseModel):
    tokens: List[str]
    heads: List[AttentionHeadMatrix]
    average_attention: List[List[float]]
    q_sample: List[List[float]]
    k_sample: List[List[float]]
    v_sample: List[List[float]]
    formula_explanation: str
