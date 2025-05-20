---
theme: default
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Attention Is All You Need: The Transformer Architecture
  Generated presentation from academic paper
drawings:
  persist: false
transition: slide-left
title: Attention Is All You Need: The Transformer Architecture
---

# Attention Is All You Need: The Transformer Architecture

---

# Introduction

- Sequence transduction models traditionally use RNNs or CNNs with attention
- Sequential computation in RNNs limits parallelism and training speed
- The Transformer dispenses with recurrence and convolutions, relying only on attention
- Achieves higher translation quality while training faster
- Sets new state-of-the-art BLEU scores on WMT’14 En→De and En→Fr

---

# Background

- RNN-based encoders and decoders factor computation along sequence positions
- Convolutions improve parallelism but still grow path length with distance
- Attention mechanisms model long-range dependencies irrespective of position
- Most prior models combine attention with RNNs or CNNs
- Transformer is the first transduction model using only self-attention

---

# Transformer Architecture

- Encoder-decoder structure built from stacked self-attention and feed-forward layers
- Encoder: 6 layers, each with multi-head self-attention + position-wise FFN, residuals, layer norm
- Decoder: 6 layers, adds encoder-decoder attention and masked self-attention to preserve autoregression
- Model dimension d_model=512, number of layers N=6, feed-forward inner dim=2048
- Multi-head attention uses h=8 heads, each of size d_k=d_v=64

---

# Attention Mechanisms

- Scaled Dot-Product Attention: softmax(QKᵀ/√d_k)·V
- Multi-Head Attention: h parallel attention heads with learned linear projections
- Encoder self-attention connects all input positions in constant sequential steps
- Decoder self-attention uses masking to prevent access to future positions
- Encoder-decoder attention lets decoder attend over encoder outputs

---

# Auxiliary Components

- Position-wise Feed-Forward Networks: two linear transforms + ReLU per position
- Shared input/output embeddings, scaled by √d_model, followed by softmax
- Sinusoidal positional encodings inject absolute and relative position information
- Dropout applied on sub-layer outputs and embeddings (P_dropout=0.1)
- Label smoothing (ε_ls=0.1) improves BLEU despite higher perplexity

---

# Training and Results

- Datasets: WMT’14 En↔De (4.5M pairs), WMT’14 En→Fr (36M pairs)
- Byte-pair encoding vocab ~37K for En-De; word-piece vocab 32K for En-Fr
- Trained on 8×P100 GPUs with Adam + warmup schedule (4K steps)
- Base model: 27.3 BLEU on En-De (12h); Big model: 28.4 BLEU on En-De (3.5d)
- Big model achieves 41.8 BLEU on En→Fr at ¼ training cost of previous SOTA

---

# Ablation Studies

- Single-head attention drops ∼0.9 BLEU vs 8 heads; too many heads also degrades
- Reducing key/value dims d_k hurts performance, suggesting dot-product limits
- Larger models (wider FFN, more layers) yield better BLEU
- Dropout crucial to prevent overfitting; P_dropout=0.1 for base, 0.3 for big
- Learned vs sinusoidal positional encodings show nearly identical results

---

# Generalization: Constituency Parsing

- 4-layer Transformer (d_model=1024) applied to WSJ parsing (40K sentences)
- Outperforms previous seq2seq parsers in low-data regime
- Semi-supervised training on 17M additional sentences yields 92.7 F1 on WSJ§23
- Surpasses discriminative and ensemble parsers without task-specific tuning
- Demonstrates Transformer’s applicability beyond translation

---

# Conclusion

- Transformer: first fully attention-based sequence transduction model
- Delivers faster training, full parallelization, and superior translation quality
- Generalizes effectively to tasks like constituency parsing
- Future work: extend to other modalities, local/restricted attention, non-text data
- Open-source code available in tensor2tensor for community adoption

---
