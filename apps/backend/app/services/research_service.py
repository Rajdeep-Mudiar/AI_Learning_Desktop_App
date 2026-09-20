from typing import List, Optional
from app.schemas.research import (
    ResearchPaper,
    PaperListItem,
    EquationAnnotation,
    ReproductionStep
)

RESEARCH_PAPERS_CATALOG: List[ResearchPaper] = [
    ResearchPaper(
        id="attention-is-all-you-need",
        title="Attention Is All You Need",
        authors=["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "Jakob Uszkoreit", "Llion Jones", "Aidan N. Gomez", "Lukasz Kaiser", "Illia Polosukhin"],
        year=2017,
        conference="NeurIPS 2017",
        arxiv_id="1706.03762",
        category="Transformers",
        abstract="The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.",
        citation_count=135000,
        difficulty="Intermediate",
        key_innovations=[
            "Eliminated sequential recurrence (RNN/LSTM) in favor of parallelized self-attention",
            "Multi-Head Attention allowing joint attending to information from different representation subspaces",
            "Deterministic sinusoidal positional encodings preserving sequence ordering",
            "Scaled Dot-Product normalizer 1/sqrt(d_k) preventing vanishing softmax gradients"
        ],
        equations=[
            EquationAnnotation(
                equation_name="Scaled Dot-Product Attention",
                equation_latex="\\text{Attention}(Q, K, V) = \\text{Softmax}\\left(\\frac{Q K^T}{\\sqrt{d_k}}\\right) V",
                plain_english_meaning="Computes similarity between all query tokens and key tokens, normalizes into probabilities via Softmax, and outputs a weighted sum of value vectors.",
                geometric_intuition="Each query vector casts a beam across all key vectors; the dot product measures alignment angle. Dividing by sqrt(d_k) prevents extreme values that saturate softmax.",
                dimension_notes="Q, K in R^(N x d_k), V in R^(N x d_v). Output matrix is in R^(N x d_v)."
            ),
            EquationAnnotation(
                equation_name="Multi-Head Attention",
                equation_latex="\\text{MultiHead}(Q, K, V) = \\text{Concat}(\\text{head}_1, \\dots, \\text{head}_h) W^O \\quad \\text{where } \\text{head}_i = \\text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)",
                plain_english_meaning="Projects queries, keys, and values into h lower-dimensional subspaces, computes attention in parallel, and merges them back through linear projection matrix W^O.",
                geometric_intuition="Allows the model to simultaneously focus on syntactic relations (e.g. subject-verb), positional proximity, and coreference in distinct vector spaces.",
                dimension_notes="W_i^Q in R^(d_model x d_k), W^O in R^(h*d_v x d_model)."
            ),
            EquationAnnotation(
                equation_name="Sinusoidal Positional Encoding",
                equation_latex="PE_{(pos, 2i)} = \\sin\\left(\\frac{pos}{10000^{2i/d_{\\text{model}}}}\\right), \\quad PE_{(pos, 2i+1)} = \\cos\\left(\\frac{pos}{10000^{2i/d_{\\text{model}}}}\\right)",
                plain_english_meaning="Adds a unique wave frequency signature to each token index so the model knows the exact order of words without recurrence.",
                geometric_intuition="Forms a geometric progression of wavelengths from 2pi to 10000*2pi, allowing linear transformation projections to attend to relative positions.",
                dimension_notes="pos is the token index 0..N-1, i is the dimension index 0..d_model/2."
            )
        ],
        reproduction_steps=[
            ReproductionStep(
                step_number=1,
                title="Scaled Dot-Product Attention in NumPy/PyTorch",
                description="Implement the core mathematical attention equation with scaling factor and softmax masking.",
                executable_code="import torch\nimport math\n\ndef scaled_dot_product_attention(Q, K, V, mask=None):\n    d_k = Q.size(-1)\n    scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)\n    if mask is not None:\n        scores = scores.masked_fill(mask == 0, -1e9)\n    attn_weights = torch.softmax(scores, dim=-1)\n    return torch.matmul(attn_weights, V), attn_weights\n",
                expected_outcome="Output tensor has shape (batch, seq_len, d_v) and attention weights sum to 1.0 along the last axis.",
                is_completed=True
            ),
            ReproductionStep(
                step_number=2,
                title="Multi-Head Attention Layer",
                description="Implement projection heads, parallel scaled dot-product computation, and output linear layer.",
                executable_code="import torch.nn as nn\n\nclass MultiHeadAttention(nn.Module):\n    def __init__(self, d_model=64, num_heads=4):\n        super().__init__()\n        self.d_k = d_model // num_heads\n        self.h = num_heads\n        self.q_proj = nn.Linear(d_model, d_model)\n        self.k_proj = nn.Linear(d_model, d_model)\n        self.v_proj = nn.Linear(d_model, d_model)\n        self.out_proj = nn.Linear(d_model, d_model)\n",
                expected_outcome="MultiHeadAttention forward pass runs without shape mismatches across arbitrary batch sizes.",
                is_completed=True
            ),
            ReproductionStep(
                step_number=3,
                title="Transformer Encoder Block with Residual Connections",
                description="Assemble LayerNorm, MultiHeadAttention, Dropout, and FeedForward MLP with skip connections.",
                executable_code="# Complete Transformer Encoder Stack\n",
                expected_outcome="Passes synthetic sequence copy task with > 99% accuracy.",
                is_completed=False
            )
        ]
    ),
    ResearchPaper(
        id="resnet-deep-residual-learning",
        title="Deep Residual Learning for Image Recognition",
        authors=["Kaiming He", "Xiangyu Zhang", "Shaoqing Ren", "Jian Sun"],
        year=2015,
        conference="CVPR 2016 (Best Paper)",
        arxiv_id="1512.03385",
        category="Vision",
        abstract="Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions.",
        citation_count=185000,
        difficulty="Intermediate",
        key_innovations=[
            "Solved the degradation problem in deep networks using identity shortcut connections",
            "Enabled training of 100+ layer architectures (ResNet-50, ResNet-101, ResNet-152)",
            "Gradients propagate directly through identity paths, avoiding vanishing gradients",
            "Won 1st place in ImageNet 2015 classification challenge with 3.57% top-5 error"
        ],
        equations=[
            EquationAnnotation(
                equation_name="Residual Mapping",
                equation_latex="\\mathcal{H}(x) = \\mathcal{F}(x, \\{W_i\\}) + x",
                plain_english_meaning="Instead of forcing stacked layers to fit underlying mapping H(x), we let them fit residual F(x) = H(x) - x, adding input x via identity shortcut.",
                geometric_intuition="If an identity mapping is optimal, it is much easier for backprop to push residual weights to zero than to fit an identity transformation from scratch.",
                dimension_notes="x and F must have matching dimensions; if channels change, a 1x1 conv projection W_s is applied."
            )
        ],
        reproduction_steps=[
            ReproductionStep(
                step_number=1,
                title="Basic Residual Block with Skip Connection",
                description="Construct 2-layer Conv2D residual block with BatchNorm, ReLU, and identity addition.",
                executable_code="import torch\nimport torch.nn as nn\n\nclass ResBlock(nn.Module):\n    def __init__(self, channels):\n        super().__init__()\n        self.conv1 = nn.Conv2d(channels, channels, 3, padding=1, bias=False)\n        self.bn1 = nn.BatchNorm2d(channels)\n        self.relu = nn.ReLU(inplace=True)\n        self.conv2 = nn.Conv2d(channels, channels, 3, padding=1, bias=False)\n        self.bn2 = nn.BatchNorm2d(channels)\n        \n    def forward(self, x):\n        identity = x\n        out = self.relu(self.bn1(self.conv1(x)))\n        out = self.bn2(self.conv2(out))\n        return self.relu(out + identity)\n",
                expected_outcome="Residual block preserves input dimensions and permits seamless identity flow.",
                is_completed=True
            )
        ]
    ),
    ResearchPaper(
        id="lora-low-rank-adaptation",
        title="LoRA: Low-Rank Adaptation of Large Language Models",
        authors=["Edward J. Hu", "Yelong Shen", "Phillip Wallis", "Zeyuan Allen-Zhu", "Yuanzhi Li", "Shean Wang", "Lu Wang", "Weizhu Chen"],
        year=2021,
        conference="ICLR 2022",
        arxiv_id="2106.09685",
        category="Fine-Tuning",
        abstract="We propose Low-Rank Adaptation, or LoRA, which freezes the pretrained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks.",
        citation_count=22000,
        difficulty="Advanced",
        key_innovations=[
            "Freezes original base weights W_0 and trains small rank-r matrices B and A",
            "Reduces trainable parameters by up to 10,000x and GPU VRAM footprint by 3x",
            "Zero additional inference latency by fusing Delta W = B*A directly into W_0 at deploy time",
            "Preserves foundation model capabilities while enabling modular task switching"
        ],
        equations=[
            EquationAnnotation(
                equation_name="Low-Rank Weight Parameterization",
                equation_latex="h = W_0 x + \\Delta W x = W_0 x + \\frac{\\alpha}{r} B A x \\quad \\text{where } B \\in \\mathbb{R}^{d \\times r}, \\; A \\in \\mathbb{R}^{r \\times k}, \\; r \\ll \\min(d, k)",
                plain_english_meaning="Decomposes high-dimensional weight updates into two skinny low-rank matrices B and A, scaled by alpha/r.",
                geometric_intuition="The weight update delta lives in a low intrinsic dimensional manifold. Matrix A compresses input into r dimensions; B expands it back to d.",
                dimension_notes="For d=4096, k=4096, and rank r=8, parameters drop from 16,777,216 to 65,536 (99.6% reduction!)."
            )
        ],
        reproduction_steps=[
            ReproductionStep(
                step_number=1,
                title="LoRA Linear Layer Adapter in PyTorch",
                description="Wrap standard nn.Linear with frozen base weight and trainable low-rank B and A matrices.",
                executable_code="import torch\nimport torch.nn as nn\n\nclass LoRALinear(nn.Module):\n    def __init__(self, in_features, out_features, r=8, lora_alpha=16):\n        super().__init__()\n        self.base = nn.Linear(in_features, out_features, bias=False)\n        self.base.weight.requires_grad = False  # Freeze base\n        self.r = r\n        self.scaling = lora_alpha / r\n        self.lora_A = nn.Parameter(torch.randn(r, in_features) * 0.01)\n        self.lora_B = nn.Parameter(torch.zeros(out_features, r))\n        \n    def forward(self, x):\n        return self.base(x) + (x @ self.lora_A.T @ self.lora_B.T) * self.scaling\n",
                expected_outcome="Number of trainable gradients decreases by > 95% while forward pass produces adapted activations.",
                is_completed=True
            )
        ]
    )
]

def list_all_papers() -> List[PaperListItem]:
    return [
        PaperListItem(
            id=p.id,
            title=p.title,
            authors=p.authors,
            year=p.year,
            conference=p.conference,
            arxiv_id=p.arxiv_id,
            category=p.category,
            abstract=p.abstract,
            difficulty=p.difficulty,
            reproduction_steps_count=len(p.reproduction_steps)
        )
        for p in RESEARCH_PAPERS_CATALOG
    ]

def get_paper_by_id(paper_id: str) -> Optional[ResearchPaper]:
    for p in RESEARCH_PAPERS_CATALOG:
        if p.id == paper_id:
            return p
    return None
