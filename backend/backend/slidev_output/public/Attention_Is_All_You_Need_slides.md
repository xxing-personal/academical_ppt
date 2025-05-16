---
theme: default
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Attention Is All You Need
  Generated presentation from academic paper
drawings:
  persist: false
transition: slide-left
title: Attention Is All You Need
---

# Attention Is All You Need

---

# Title

- Attention Is All You Need
- Ashish Vaswani et al., 2017
- Google Brain & Google Research

---

# Introduction

- Sequence-to-sequence dominated by RNNs or CNNs with attention
- Recurrence and convolution limit parallelization and speed
- Attention allows modeling of long-range dependencies directly
- This work proposes the Transformer: an attention-only model

---

# Transformer Architecture

- Encoder-decoder stacks of N=6 identical layers each
- Each layer: multi-head self-attention + position-wise feed-forward
- Residual connections + layer normalization around sub-layers
- Decoder adds encoder-decoder attention and masking

---

# Attention Mechanisms

- Scaled dot-product attention: softmax(QKᵀ/√dₖ)V
- Multi-head attention: parallel attention heads in subspaces
- Encoder-decoder, encoder self-, decoder self-attention variants
- Masking in decoder preserves auto-regressive generation

---

# Positional Encoding

- No recurrence or convolution → inject position info
- Fixed sinusoidal embeddings added to token embeddings
- Dimensions: PE(pos,2i)=sin(pos/10000^(2i/dₘ)), cos for odd
- Supports relative position learning and length extrapolation

---

# Comparative Advantages

- Self-attention: O(n²·d) per layer, O(1) sequential ops
- Recurrent: O(n·d²) complexity, O(n) sequential steps
- Convolutions: path length O(log_k n), more ops per layer
- Transformer has constant path length, high parallelism

---

# Training Setup

- Datasets: WMT14 En–De (4.5M pairs), En–Fr (36M pairs)
- Vocabularies: byte-pair encoding or word-pieces (32–37K)
- Hardware: 8 P100 GPUs, Adam optimizer with warm-up
- Regularization: dropout (0.1–0.3) and label smoothing (ϵ=0.1)

---

# Translation Results

- En→De: 28.4 BLEU, +2 BLEU over prior best (including ensembles)
- En→Fr: 41.8 BLEU single-model state-of-the-art
- Base model: 12 h training; big model: 3.5 days on 8 GPUs
- Outperforms larger models at a fraction of computational cost

---

# Generalization to Parsing

- Applied 4-layer Transformer to WSJ constituency parsing
- WSJ-only: 91.3 F1, outperforming many discriminative parsers
- Semi-supervised (17M sentences): 92.7 F1, new best
- No task-specific architecture changes needed

---

# Conclusion

- Transformer: first sequence model based entirely on attention
- Delivers SOTA translation and parsing with high efficiency
- Enables massive parallelism and shorter training times
- Future work: other modalities, local/restricted attention, non-sequential generation

---
