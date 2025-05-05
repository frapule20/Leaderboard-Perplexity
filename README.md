# 📊 Leaderboard Perplexity 
(link: https://frapule20.github.io/Leaderboard-Perplexity/)

The average perplexity is a key metric for evaluating a model’s linguistic fluency and coherence. Lower values indicate that the model assigns higher probabilities to appropriate sequences, reflecting better language understanding.

The standard deviation measures the variability of perplexity across different prompts. A low standard deviation suggests the model is stable and consistent, while a high deviation indicates erratic behavior—performing well on some prompts and poorly on others.

These metrics will be recomputed after adversarial interventions (e.g., quantization, fine-tuning, steering), to assess how such manipulations affect both the performance and robustness of the model under stress.




## 🌐 Multiliingual Models

| Rank | Model                | Average Perplexity ↓ | Standard Deviation |
|------|----------------------|----------------------:|-------------------:|
| 1    | gemma-3-27b-it       |               1.74152 |           0.617274 |
| 2    | phi-4                |               1.98343 |           0.452418 |
| 3    | aya-expanse-32b      |               2.05807 |           0.664697 |
| 4    | DeepSeek-V3-0324     |               2.30954 |           0.816960 |
| 5    | Qwen2.5-72B-Instruct |               2.77812 |           1.259960 |


## 🇮🇹 Italian Models

| Rank | Model                              | Average Perplexity ↓ | Standard Deviation     |
|------|------------------------------------|----------------------:|------------------------:|
| 1    | LLaMAntino-3-ANITA-8B-Inst-DPO-ITA |               2.77502 |               1.87228  |
| 2    | DanteLLM-7B-Instruct-Italian-v0.1  |               3.16792 |               1.31612  |
| 3    | modello-italia-9b-bf16             |               5.74107 |               8.5757   |
| 3    | Minerva-7B-instruct-v1.0           |               7.27705 |               6.12963  |
| 4    | extremITA-Camoscio-7b              |               17.7658 |               32.7655  | 
| 5    | Velvet-14B                         |               26.5908 |               55.9184  |




