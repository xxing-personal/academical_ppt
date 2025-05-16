---
theme: default
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Attention Is All You Need: The Transformer
  Generated presentation from academic paper
drawings:
  persist: false
transition: slide-left
title: Attention Is All You Need: The Transformer
---

# Attention Is All You Need: The Transformer

---

# Introduction

- Traditional sequence transduction models rely on recurrent or convolutional networks with attention
- Sequential computation in RNNs limits parallelism and increases training time
- The Transformer dispenses with recurrence and convolutions, using only attention
- Achieves state-of-the-art results on machine translation tasks

---

# Background

- Encoder-decoder architectures with RNNs (e.g., LSTM) dominate sequence modeling
- Convolutional seq2seq (ByteNet, ConvS2S) reduce sequential steps but struggle with long-range dependencies
- Attention mechanisms help model distant relationships but are usually coupled with recurrence
- Self-attention offers constant-time paths between any positions and enables full parallelization

---

# Model Architecture

- Encoder: stack of N=6 layers, each with multi-head self-attention and position-wise feed-forward sublayers
- Decoder: 6 layers plus an encoder-decoder attention sublayer and masked self-attention for autoregression
- Residual connections and layer normalization surround every sublayer
- Token embeddings are summed with positional encodings at the input

---

# Attention Mechanisms

- Scaled Dot-Product Attention: compute softmax(QKᵀ/√dk)·V for queries Q, keys K, values V
- Multi-Head Attention: h parallel attention heads learning different projections
- Three applications: encoder self-attention, decoder self-attention (masked), encoder-decoder attention
- Positional Encodings use fixed sine/cosine functions to inject sequence order

---

# Training and Results

- Datasets: WMT’14 English–German (4.5M pairs) and English–French (36M pairs) with subword tokenization
- Base Transformer: 27.3 BLEU (EN→DE) in 12h on 8 GPUs; Big: 28.4 BLEU in 3.5 days
- Outperforms previous single models and ensembles while using less compute
- Uses Adam optimizer with warmup learning rate schedule and label smoothing

---

# Generalization

- Applied to English constituency parsing on WSJ corpus
- Achieved 91.3 F1 (WSJ only) and 92.7 F1 (with semi-supervised data), surpassing prior seq2seq parsers
- Demonstrates Transformer’s versatility beyond translation

---

# Conclusion

- Introduced the first sequence transduction model based entirely on attention
- Eliminated recurrence and convolutions to gain training speed, parallelism, and translation quality
- Future work: local/restricted attention for long inputs, other modalities (audio, vision), non-sequential generation

---
