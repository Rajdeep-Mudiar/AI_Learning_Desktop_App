import numpy as np
from typing import List, Dict, Any, Optional, Tuple
from sklearn.datasets import make_moons, make_circles
from app.schemas.deep_learning import (
    MLPSimulationRequest,
    MLPSimulationResponse,
    LayerWeightMatrix,
    ForwardStep,
    DecisionBoundaryGrid,
    CNNConvolveRequest,
    CNNConvolveResponse,
    TransformerAttentionRequest,
    TransformerAttentionResponse,
    AttentionHeadMatrix
)

# ==========================================
# 1. MLP SIMULATION ENGINE
# ==========================================

def get_mlp_dataset(dataset_type: str, n_samples: int = 120) -> Tuple[np.ndarray, np.ndarray]:
    np.random.seed(42)
    if dataset_type == "xor":
        X = np.random.uniform(-1.2, 1.2, size=(n_samples, 2))
        y = ((X[:, 0] > 0) ^ (X[:, 1] > 0)).astype(int)
    elif dataset_type == "circles":
        X, y = make_circles(n_samples=n_samples, noise=0.1, factor=0.4, random_state=42)
        X = X * 1.2
    elif dataset_type == "moons":
        X, y = make_moons(n_samples=n_samples, noise=0.12, random_state=42)
        X = (X - np.array([0.5, 0.25])) * 1.1
    elif dataset_type == "spiral":
        # Two-spiral generation
        n = n_samples // 2
        theta = np.sqrt(np.random.rand(n)) * 2 * np.pi
        r_a = 2 * theta + np.pi
        data_a = np.array([np.cos(theta) * r_a, np.sin(theta) * r_a]).T + np.random.randn(n, 2) * 0.4
        r_b = -2 * theta - np.pi
        data_b = np.array([np.cos(theta) * r_b, np.sin(theta) * r_b]).T + np.random.randn(n, 2) * 0.4
        X = np.vstack([data_a, data_b]) / 12.0
        y = np.hstack([np.zeros(n, dtype=int), np.ones(n, dtype=int)])
    else:
        X, y = make_moons(n_samples=n_samples, noise=0.1, random_state=42)

    return X, y


def activate(z: np.ndarray, act_type: str) -> np.ndarray:
    if act_type == "relu":
        return np.maximum(0, z)
    elif act_type == "sigmoid":
        return 1.0 / (1.0 + np.exp(-np.clip(z, -20, 20)))
    elif act_type == "tanh":
        return np.tanh(z)
    elif act_type == "leaky_relu":
        return np.where(z > 0, z, 0.1 * z)
    return z


def activate_deriv(a: np.ndarray, act_type: str) -> np.ndarray:
    if act_type == "relu":
        return (a > 0).astype(float)
    elif act_type == "sigmoid":
        return a * (1.0 - a)
    elif act_type == "tanh":
        return 1.0 - a**2
    elif act_type == "leaky_relu":
        return np.where(a > 0, 1.0, 0.1)
    return np.ones_like(a)


def simulate_mlp(req: MLPSimulationRequest) -> MLPSimulationResponse:
    X, y = get_mlp_dataset(req.dataset_type, n_samples=100)
    layer_sizes = req.layer_sizes.copy()
    layer_sizes[0] = 2  # input 2D coordinates
    layer_sizes[-1] = 1 # binary output

    # Initialize weights and biases
    np.random.seed(42)
    weights: List[np.ndarray] = []
    biases: List[np.ndarray] = []

    for i in range(len(layer_sizes) - 1):
        # He / Xavier initialization
        std = np.sqrt(2.0 / layer_sizes[i])
        W = np.random.randn(layer_sizes[i], layer_sizes[i + 1]) * std
        b = np.zeros((1, layer_sizes[i + 1]))
        weights.append(W)
        biases.append(b)

    loss_history: List[float] = []
    accuracy_history: List[float] = []

    y_col = y.reshape(-1, 1)

    # Train loop
    for epoch in range(req.epochs):
        # Forward pass
        activations = [X]
        for i in range(len(weights)):
            z = activations[-1] @ weights[i] + biases[i]
            if i == len(weights) - 1:
                # Output layer always uses sigmoid for binary classification
                a = activate(z, "sigmoid")
            else:
                a = activate(z, req.activation)
            activations.append(a)

        y_pred = activations[-1]
        
        # Loss (Binary Cross-Entropy)
        eps = 1e-7
        bce_loss = -np.mean(y_col * np.log(y_pred + eps) + (1 - y_col) * np.log(1 - y_pred + eps))
        loss_history.append(float(round(bce_loss, 4)))

        # Accuracy
        preds = (y_pred >= 0.5).astype(int)
        acc = float(np.mean(preds == y_col))
        accuracy_history.append(float(round(acc, 4)))

        # Backward pass
        deltas = [y_pred - y_col]  # dL/dz for sigmoid output with BCE
        for i in reversed(range(len(weights) - 1)):
            delta_prev = (deltas[-1] @ weights[i + 1].T) * activate_deriv(activations[i + 1], req.activation)
            deltas.append(delta_prev)
        deltas.reverse()

        # Update weights and biases
        m = X.shape[0]
        for i in range(len(weights)):
            dW = (activations[i].T @ deltas[i]) / m
            db = np.sum(deltas[i], axis=0, keepdims=True) / m
            weights[i] -= req.learning_rate * dW
            biases[i] -= req.learning_rate * db

    # Sample probe forward step at (0.5, 0.5)
    probe_x = np.array([[0.5, 0.5]])
    sample_steps: List[ForwardStep] = []
    curr_a = probe_x
    for i in range(len(weights)):
        z = curr_a @ weights[i] + biases[i]
        curr_a = activate(z, "sigmoid" if i == len(weights) - 1 else req.activation)
        sample_steps.append(ForwardStep(
            layer_idx=i + 1,
            pre_activations=[round(float(v), 3) for v in z[0]],
            post_activations=[round(float(v), 3) for v in curr_a[0]]
        ))

    # Evaluate 25x25 Decision boundary grid
    gx = np.linspace(-1.5, 1.5, 25)
    gy = np.linspace(-1.5, 1.5, 25)
    xx, yy = np.meshgrid(gx, gy)
    grid_pts = np.c_[xx.ravel(), yy.ravel()]

    curr_grid = grid_pts
    for i in range(len(weights)):
        z = curr_grid @ weights[i] + biases[i]
        curr_grid = activate(z, "sigmoid" if i == len(weights) - 1 else req.activation)
    
    grid_z = curr_grid.reshape(25, 25).round(3).tolist()

    # Format Layer Weights
    formatted_weights: List[LayerWeightMatrix] = []
    for idx, (w, b) in enumerate(zip(weights, biases)):
        formatted_weights.append(LayerWeightMatrix(
            layer_idx=idx + 1,
            weights=w.round(3).tolist(),
            biases=b.round(3).flatten().tolist()
        ))

    data_points = [
        {"x": round(float(X[i, 0]), 3), "y": round(float(X[i, 1]), 3), "label": int(y[i])}
        for i in range(len(X))
    ]

    return MLPSimulationResponse(
        layers=layer_sizes,
        weights=formatted_weights,
        loss_history=loss_history[::max(1, len(loss_history) // 30)],
        accuracy_history=accuracy_history[::max(1, len(accuracy_history) // 30)],
        final_accuracy=round(accuracy_history[-1], 4),
        sample_forward=sample_steps,
        decision_boundary=DecisionBoundaryGrid(
            grid_x=gx.round(2).tolist(),
            grid_y=gy.round(2).tolist(),
            grid_z=grid_z
        ),
        data_points=data_points
    )


# ==========================================
# 2. CNN CONVOLUTION & POOLING ENGINE
# ==========================================

STANDARD_KERNELS = {
    "sobel_horizontal": [[-1.0, -2.0, -1.0], [0.0, 0.0, 0.0], [1.0, 2.0, 1.0]],
    "sobel_vertical": [[-1.0, 0.0, 1.0], [-2.0, 0.0, 2.0], [-1.0, 0.0, 1.0]],
    "edge_detect": [[-1.0, -1.0, -1.0], [-1.0, 8.0, -1.0], [-1.0, -1.0, -1.0]],
    "sharpen": [[0.0, -1.0, 0.0], [-1.0, 5.0, -1.0], [0.0, -1.0, 0.0]],
    "gaussian_blur": [[0.0625, 0.125, 0.0625], [0.125, 0.25, 0.125], [0.0625, 0.125, 0.0625]],
    "ridge": [[0.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 0.0]]
}

def generate_sample_digit_image() -> np.ndarray:
    """Generates a crisp 14x14 grayscale pattern (Digit '7' with crossbar)."""
    img = np.zeros((14, 14), dtype=float)
    # Top horizontal bar
    img[2:4, 2:12] = 1.0
    # Diagonal stroke
    for i in range(4, 12):
        col = 11 - (i - 4)
        if 2 <= col < 12:
            img[i, col:col+2] = 1.0
    # Center crossbar
    img[7, 4:9] = 0.85
    return img


def convolve_2d(req: CNNConvolveRequest) -> CNNConvolveResponse:
    if req.kernel_name == "custom" and req.custom_kernel:
        kernel = np.array(req.custom_kernel, dtype=float)
    else:
        kernel = np.array(STANDARD_KERNELS.get(req.kernel_name, STANDARD_KERNELS["edge_detect"]), dtype=float)

    img = generate_sample_digit_image()
    
    # Padding
    p = req.padding
    if p > 0:
        padded = np.pad(img, p, mode="constant", constant_values=0)
    else:
        padded = img

    k_h, k_w = kernel.shape
    stride = req.stride

    out_h = (padded.shape[0] - k_h) // stride + 1
    out_w = (padded.shape[1] - k_w) // stride + 1

    feature_map = np.zeros((out_h, out_w), dtype=float)

    for i in range(out_h):
        for j in range(out_w):
            r_start = i * stride
            c_start = j * stride
            patch = padded[r_start:r_start + k_h, c_start:c_start + k_w]
            dot_val = np.sum(patch * kernel)
            # ReLU activation
            feature_map[i, j] = max(0.0, float(dot_val))

    # Pooling
    pooled_map = None
    if req.pooling_type in ["max", "average"]:
        p_h = feature_map.shape[0] // 2
        p_w = feature_map.shape[1] // 2
        if p_h > 0 and p_w > 0:
            pooled_map = np.zeros((p_h, p_w), dtype=float)
            for i in range(p_h):
                for j in range(p_w):
                    window = feature_map[i * 2:(i + 1) * 2, j * 2:(j + 1) * 2]
                    if req.pooling_type == "max":
                        pooled_map[i, j] = float(np.max(window))
                    else:
                        pooled_map[i, j] = float(np.mean(window))

    explanation = (
        f"Convolved {img.shape[0]}x{img.shape[1]} input with {k_h}x{k_w} kernel (stride={stride}, padding={p}). "
        f"Output feature map shape: {feature_map.shape[0]}x{feature_map.shape[1]}. "
        + (f"2x2 {req.pooling_type.capitalize()} Pooling reduced dimensions to {pooled_map.shape[0]}x{pooled_map.shape[1]}." if pooled_map is not None else "")
    )

    return CNNConvolveResponse(
        kernel=kernel.round(3).tolist(),
        input_matrix=img.round(2).tolist(),
        feature_map=feature_map.round(3).tolist(),
        pooled_map=pooled_map.round(3).tolist() if pooled_map is not None else None,
        formula_explanation=explanation
    )


# ==========================================
# 3. TRANSFORMER SELF-ATTENTION ENGINE
# ==========================================

def compute_transformer_attention(req: TransformerAttentionRequest) -> TransformerAttentionResponse:
    # Tokenize input sentence
    raw_tokens = req.sentence.strip().split()
    tokens = [t.strip(",.!?\"'") for t in raw_tokens if t.strip(",.!?\"'")]
    if not tokens:
        tokens = ["The", "neural", "attention", "mechanism"]

    N = len(tokens)
    d_k = max(8, req.d_model // req.num_heads)

    np.random.seed(42)
    
    # Generate token positional & semantic embeddings (N x d_k)
    token_embeds = []
    for idx, tok in enumerate(tokens):
        # Semantic hash component + sinusoidal positional encoding
        seed_val = abs(hash(tok.lower())) % 10000
        np.random.seed(seed_val)
        base = np.random.randn(d_k) * 0.5
        pos = np.array([np.sin(idx / (10000 ** (2 * j / d_k))) for j in range(d_k)])
        token_embeds.append(base + pos)

    X = np.array(token_embeds) # shape: (N, d_k)

    head_matrices: List[AttentionHeadMatrix] = []
    accumulated_weights = np.zeros((N, N))

    for h in range(req.num_heads):
        np.random.seed(100 + h * 17)
        W_Q = np.random.randn(d_k, d_k) * 0.6
        W_K = np.random.randn(d_k, d_k) * 0.6

        Q = X @ W_Q # (N, d_k)
        K = X @ W_K # (N, d_k)

        # Scaled dot-product: (Q @ K^T) / sqrt(d_k)
        scores = (Q @ K.T) / np.sqrt(d_k)

        # Softmax per row
        exp_scores = np.exp(scores - np.max(scores, axis=-1, keepdims=True))
        attn_weights = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)

        head_matrices.append(AttentionHeadMatrix(
            head_idx=h + 1,
            attention_weights=attn_weights.round(3).tolist()
        ))
        accumulated_weights += attn_weights

    avg_weights = (accumulated_weights / req.num_heads).round(3).tolist()

    # Provide sample Q, K, V projections for inspectability
    np.random.seed(42)
    sample_Q = (X @ np.random.randn(d_k, 4)).round(2).tolist()
    sample_K = (X @ np.random.randn(d_k, 4)).round(2).tolist()
    sample_V = (X @ np.random.randn(d_k, 4)).round(2).tolist()

    explanation = (
        f"Computed Scaled Dot-Product Attention: Softmax(Q K^T / √{d_k}) across {N} tokens and {req.num_heads} attention heads. "
        f"Each cell (i, j) indicates how much query token i attends to key token j."
    )

    return TransformerAttentionResponse(
        tokens=tokens,
        heads=head_matrices,
        average_attention=avg_weights,
        q_sample=sample_Q,
        k_sample=sample_K,
        v_sample=sample_V,
        formula_explanation=explanation
    )
