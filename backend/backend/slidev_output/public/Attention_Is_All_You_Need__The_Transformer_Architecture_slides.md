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

# Title Slide

- Paper: Attention Is All You Need
- Authors: Vaswani et al., Google Brain & Research
- Published: NIPS 2017

---

# Introduction

- Sequence transduction dominated by RNNs and CNNs with attention
- Recurrent models suffer from sequential computation bottlenecks
- Propose the Transformer: a model based solely on attention mechanisms
- Achieves superior translation quality and faster training

---

# Background

- RNNs (LSTM, GRU) and CNNs process sequences step-by-step or with convolutions
- Attention adds global context but usually complements recurrence
- Convolutional models still require many layers to capture long-range dependencies
- Goal: reduce sequential operations and improve parallelism

---

# Transformer Architecture

- Encoder-decoder framework with no recurrence or convolutions
- Each stack has N=6 layers with self-attention and feed-forward sub-layers
- Residual connections and layer normalization after every sub-layer
- Shared embedding dimension d_model=512 across the model

---

# Self-Attention Mechanisms

- Scaled Dot-Product Attention: softmax(Q·Kᵀ/√d_k)·V
- Multi-Head Attention: h=8 parallel attention heads
- Encoder-Decoder attention, encoder self-attention, decoder self-attention
- Positional encodings (sinusoidal) added to input embeddings

---

# Advantages of Self-Attention

- Fully parallelizable across sequence positions
- Constant maximum path length between any two tokens
- Lower per-layer complexity for typical sentence lengths
- Empirically interpretable attention patterns

---

# Training and Translation Results

- Datasets: WMT 2014 EN→DE (4.5M pairs), EN→FR (36M pairs)
- Base model: 28.3M params, trained 12h on 8 P100 GPUs
- Big model: 213M params, trained 3.5 days; achieves 28.4 BLEU (EN→DE)
- State-of-the-art single-model BLEU 41.8 on EN→FR at lower cost

---

# Generalization to Parsing

- Applied 4-layer Transformer to WSJ constituency parsing
- Train on 40K sentences (WSJ) and semi-supervised 17M corpora
- Achieved 91.3 F1 (WSJ only) and 92.7 F1 (semi-supervised)
- Outperforms previous seq2seq and competitive with specialized parsers

---

# Conclusion

- Introduced the first fully attention-based sequence transduction model
- Transformer outperforms RNN/CNN models in speed and quality
- Enables better parallelization and learning of long-range dependencies
- Future work: other modalities, local attention, non-sequential generation

---
