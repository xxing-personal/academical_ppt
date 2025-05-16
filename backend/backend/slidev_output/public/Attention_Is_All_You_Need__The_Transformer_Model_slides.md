---
theme: default
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Attention Is All You Need: The Transformer Model
  Generated presentation from academic paper
drawings:
  persist: false
transition: slide-left
title: Attention Is All You Need: The Transformer Model
---

# Attention Is All You Need: The Transformer Model

---

# Introduction

- Sequence transduction dominated by RNNs/CNNs with attention
- Sequential recurrence limits parallelism and slows training
- Attention mechanisms capture long-range dependencies
- We propose the Transformer: pure attention, no recurrence or convolution
- Achieves state-of-the-art translation quality in less training time

---

# Background and Motivation

- Recurrent models (LSTM/GRU) process inputs sequentially, hindering parallelism
- Convolutional alternatives improve parallelism but have path-length and resolution limits
- Self-attention relates all positions directly with O(1) path length
- Shorter paths ease learning of long-range dependencies
- A fully attention-based model can be faster and simpler

---

# Transformer Architecture Overview

- Encoder-decoder structure with N stacked identical layers (N=6 base)
- Each encoder layer: multi-head self-attention + position-wise feed-forward
- Decoder layers add encoder-decoder attention and masking for auto-regression
- Residual connections + layer normalization around all sub-layers
- Model dimension dₘₒdₑₗ=512 (base), fully parallelizable across positions

---

# Attention Mechanisms

- Scaled dot-product attention: softmax(QKᵀ/√dₖ)V
- Multi-head attention: parallel attention with h=8 heads, dₖ=dᵥ=64
- Encoder-decoder attention lets decoder attend over encoder outputs
- Masked self-attention in decoder prevents access to future positions
- Multi-head learns diverse representation subspaces jointly

---

# Positional Encoding and Feed-Forward

- No recurrence/convolution: inject position via sinusoidal encodings
- PE(pos,2i)=sin(pos/10000^(2i/dₘₒdₑₗ)), PE(pos,2i+1)=cos(...)
- Position-wise feed-forward: two linear transforms with ReLU, d_ff=2048
- Shared input/output embeddings and pre-softmax weights
- Regularization: dropout on sub-layers and label smoothing (ϵ_ls=0.1)

---

# Training and Results

- Datasets: WMT ’14 English–German (4.5M), English–French (36M) with BPE
- Hardware: 8×P100 GPUs, base trained 12h, big trained 3.5 days
- Optimizer: Adam with warmup and inverse-sqrt schedule (warmup=4000)
- Translation BLEU: 28.4 (EN→DE), 41.8 (EN→FR) surpassing prior best
- Parser F1: 91.3 (WSJ only), 92.7 (semi-supervised) on English constituency parsing

---

# Conclusion

- First sequence model relying entirely on attention, eliminating recurrence
- Superior parallelism enables faster training and state-of-the-art performance
- Generalizes to other tasks (e.g., parsing) with minimal modification
- Future work: local/restricted attention for long inputs, other modalities, less sequential generation
- Code available in Tensor2Tensor for reproducibility and extension

---
