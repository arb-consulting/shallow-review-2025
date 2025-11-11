[11/07/25 17:54:22] INFO     shallow_review.utils: Logging initialized. Log file: /home/dev/proj/shallow-review/runs/20251107-175422_2990184.log                                          utils.py:271
                    INFO     shallow_review.data_db: Initialized unified database at /home/dev/proj/shallow-review/data/data.db                                                          data_db.py:97
# AI Safety Shallow Review

**Generated:** 2025-11-07

**Filters:** shallow_review≥0.4, ai_safety≥0.1, collect≥0.1
**Sources:** arxiv-2025-papers-from-top-researchers, arxiv-papers-from-gavin-authors, arxiv-papers-from-gavin-hits

**Total items:** 225

---

## <span style="font-size:1.5em">Control the thing</span> <span style="color:#bbb">[cat:control_thing]</span>


---

### <span style="font-size:1.4em">Iterative alignment</span> <span style="color:#bbb">[cat:iterative_alignment]</span>


---

#### <span style="font-size:1.3em">Surgical model edits</span> <span style="color:#bbb">[cat:surgical_edits]</span>


---

##### <span style="font-size:1.2em">Activation engineering</span> <span style="color:#bbb">[cat:activation_engineering]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: a sort of interpretable finetuning. Let's see if we can programmatically modify activations to steer outputs towards what we want, in a way that generalises across models and topics)*  
**Theory of change:** *(SR2024: test interpretability theories; find new insights from interpretable causal interventions on representations. Or: build more stuff to stack on top of finetuning. Slightly encourage the model to be nice, add one more layer of defence to our bundle of partial alignment methods)*  
**See also:** *(SR2024: representation engineering, SAEs)*  
**Orthodox problems:** *(SR2024: 1. Value is fragile and hard to specify, 4. Goals misgeneralize out of distribution, 5. Instrumental convergence, 7. Superintelligence can fool human supervisors, 9. Humans cannot be first-class parties to a superintelligent value handshake)*  
**Target case:** *(SR2024: pessimistic)*  
**Broad approach:** *(SR2024: engineering/cognitive)*  
**Key people:** *(SR2024: Jan Wehner, Alex Turner, Nina Panickssery, Marc Carauleanu, Collin Burns, Andrew Mack, Pedro Freire, Joseph Miller, Andy Zou, Andy Arditi, Ole Jorgensen)*  
**Estimated FTEs:** *(SR2024: 10+?)*  
**Critiques:** *(SR2024: of ROME, open question thread for theory of impact, A Sober Look at Steering Vectors for LLMs)*  
**Funded by:** *(SR2024: various, including EA funds)*  
**Funding in 2025:** *(SR2024 funding 2023-4: N/A)*  
**Outputs in 2025:**  
*(SR2024 outputs: Circuit Breakers, An Introduction to Representation Engineering - an activation-based paradigm for controlling LLMs, Steering Llama-2 with contrastive activation additions, Simple probes can catch sleeper agents, Refusal in LLMs is mediated by a single direction, Mechanistically Eliciting Latent Behaviors in Language Models, Uncovering Latent Human Wellbeing in Language Model Embeddings, Goodfire, LatentQA, SelfIE, Mack and Turner, Obfuscated Activations Bypass LLM Latent-Space Defenses)*  
- **[HyperSteer: Activation Steering at Scale with Hypernetworks](https://arxiv.org/abs/2506.03292)**, *Jiuding Sun, Sidharth Baskaran, Zhengxuan Wu et al.*, 2025-06-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:5fa3f43a]</span>, <span style="color:#777">Summary: Introduces HyperSteer, a hypernetwork-based architecture that generates steering vectors conditioned on natural language prompts to control language model behavior through activation steering. Demonstrates that this approach scales to thousands of steering prompts and exceeds state-of-the-art activation steering methods, even generalizing to unseen prompts.</span>
- **[Steering Evaluation-Aware Language Models to Act Like They Are Deployed](https://arxiv.org/abs/2510.20487)**, *Tim Tian Hua, Andrew Qin, Samuel Marks et al.*, 2025-10-23, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:3180f0ad]</span>, <span style="color:#777">Summary: Demonstrates that activation steering using steering vectors can suppress evaluation-awareness in language models, making them act as if deployed even during evaluation. Trains models to exhibit evaluation-aware behavior then shows steering can eliminate this behavior to improve evaluation reliability.</span>
- **[Steering Out-of-Distribution Generalization with Concept Ablation Fine-Tuning](https://arxiv.org/abs/2507.16795)**, *Helena Casademunt, Caden Juang, Adam Karvonen et al.*, 2025-07-22, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:4b9b525c]</span>, <span style="color:#777">Summary: Introduces Concept Ablation Fine-Tuning (CAFT), a technique that ablates undesired concept directions in latent space during fine-tuning to prevent unintended out-of-distribution generalization without modifying training data.</span>
- **[Improving Steering Vectors by Targeting Sparse Autoencoder Features](https://arxiv.org/abs/2411.02193)**, *Sviatoslav Chalnev, Matthew Siu, Arthur Conmy*, 2024-11-04, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:7d246d97]</span>, <span style="color:#777">Summary: Develops SAE-Targeted Steering (SAE-TS), a method that uses sparse autoencoders to measure and optimize steering vector interventions for targeted effects while minimizing unintended side effects, comparing favorably to existing methods like CAA and direct SAE feature steering.</span>
- **[Understanding Reasoning in Thinking Language Models via Steering Vectors](https://arxiv.org/abs/2506.18167)**, *Constantin Venhoff, Iván Arcuschin, Philip Torr et al.*, 2025-06-22, ICLR 2025 Workshop on Reasoning and Planning for Large Language Models, <span style="color:#777">[paper_preprint, sr=0.82, id:56c73ae4]</span>, <span style="color:#777">Summary: Demonstrates that reasoning behaviors in thinking language models (DeepSeek-R1-Distill) like expressing uncertainty, generating examples, and backtracking are mediated by linear directions in activation space and can be controlled using steering vectors extracted through systematic experiments on 500 tasks.</span>
- **[Understanding (Un)Reliability of Steering Vectors in Language Models](https://arxiv.org/abs/2505.22637)**, *Joschka Braun, Carsten Eickhoff, David Krueger et al.*, 2025-05-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:f990988e]</span>, <span style="color:#777">Summary: Empirical study investigating reliability of steering vectors across seven prompt types, finding that steering effectiveness depends on coherence of activation directions and geometric properties like cosine similarity and activation separation.</span>
- **[Comparing Bottom-Up and Top-Down Steering Approaches on In-Context Learning Tasks](https://arxiv.org/abs/2411.07213)**, *Madeline Brumley, Joe Kwon, David Krueger et al.*, 2024-11-11, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:ea95f368]</span>, <span style="color:#777">Summary: Empirical comparison of function vectors (bottom-up) and in-context vectors (top-down) as steering methods for LLMs, finding that ICVs excel at behavioral shifting while FVs perform better on precision-requiring tasks.</span>
- **[Taxonomy, Opportunities, and Challenges of Representation Engineering for Large Language Models](https://arxiv.org/abs/2502.19649)**, *Jan Wehner, Sahar Abdelnabi, Daniel Tan et al.*, 2025-02-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.62, id:6af32da0]</span>, <span style="color:#777">Summary: First comprehensive survey of Representation Engineering (RepE) for LLMs, proposing a unified framework that describes RepE as a pipeline of representation identification, operationalization, and control, and identifying opportunities for methodological improvements and best practices.</span>


---

##### <span style="font-size:1.2em">Utility engineering</span> <span style="color:#bbb">[cat:utility_engineering]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

##### <span style="font-size:1.2em">Unlearning</span> <span style="color:#bbb">[cat:unlearning]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Distillation Robustifies Unlearning](https://arxiv.org/abs/2506.06278)**, *Bruce W. Lee, Addie Foote, Alex Infanger et al.*, 2025-06-06, arXiv (NeurIPS 2025 Spotlight), <span style="color:#777">[paper_preprint, sr=0.88, id:0bf87e98]</span>, <span style="color:#777">Summary: Proposes UNDO (Unlearn-Noise-Distill-on-Outputs), a method that distills unlearned models to make capability removal robust to finetuning attacks, matching retraining-from-scratch robustness while using only 60-80% of compute.</span>
- **[CRISP: Persistent Concept Unlearning via Sparse Autoencoders](https://arxiv.org/abs/2508.13650)**, *Tomer Ashuach, Dana Arad, Aaron Mueller et al.*, 2025-08-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.87, id:ea6f2893]</span>, <span style="color:#777">Summary: Introduces CRISP, a parameter-efficient method for persistent concept unlearning that uses sparse autoencoders to identify and suppress salient features across multiple layers, creating lasting parameter changes rather than inference-time interventions.</span>
- **[SAEs Can Improve Unlearning: Dynamic Sparse Autoencoder Guardrails for Precision Unlearning in LLMs](https://arxiv.org/abs/2504.08192)**, *Aashiq Muhamed, Jacopo Bonato, Mona Diab et al.*, 2025-04-11, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:bbf9e8cf]</span>, <span style="color:#777">Summary: Introduces Dynamic SAE Guardrails (DSG), a novel unlearning method using Sparse Autoencoders with principled feature selection and dynamic classifiers, demonstrating superior performance over gradient-based approaches across multiple metrics including computational efficiency, stability, and resistance to relearning attacks.</span>
- **[From Dormant to Deleted: Tamper-Resistant Unlearning Through Weight-Space Regularization](https://arxiv.org/abs/2505.22310)**, *Shoaib Ahmed Siddiqui, Adrian Weller, David Krueger et al.*, 2025-05-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:2418e728]</span>, <span style="color:#777">Summary: Discovers that existing unlearning methods for neural networks are vulnerable to relearning attacks where forgotten knowledge recovers through fine-tuning on retain-set data alone, and proposes weight-space regularization methods to achieve tamper-resistant unlearning based on L2-distance and linear mode connectivity properties.</span>
- **[Existing Large Language Model Unlearning Evaluations Are Inconclusive](https://arxiv.org/abs/2506.00688)**, *Zhili Feng, Yixuan Even Xu, Alexander Robey et al.*, 2025-05-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:9f598c78]</span>, <span style="color:#777">Summary: Critically examines standard unlearning evaluation practices and identifies key limitations: evaluations can re-teach models during testing, outcomes vary significantly across tasks, and many rely on spurious correlations. Proposes two principles for future evaluations (minimal information injection and downstream task awareness) validated through targeted experiments.</span>
- **[OpenUnlearning: Accelerating LLM Unlearning via Unified Benchmarking of Methods and Metrics](https://arxiv.org/abs/2506.12618)**, *Vineeth Dorna, Anmol Mekala, Wenlong Zhao et al.*, 2025-06-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:ad2ccd21]</span>, <span style="color:#777">Summary: Introduces OpenUnlearning, a standardized framework for benchmarking LLM unlearning methods and metrics, integrating 9 algorithms and 16 evaluations across 3 benchmarks (TOFU, MUSE, WMDP) with 450+ publicly released checkpoints and a novel meta-evaluation benchmark.</span>
- **[From Memorization to Reasoning in the Spectrum of Loss Curvature](https://arxiv.org/abs/2510.24256)**, *Jack Merullo, Srihita Vatsavaya, Lucius Bushnaq et al.*, 2025-10-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:2502577e]</span>, <span style="color:#777">Summary: Develops a weight editing procedure based on loss curvature decomposition to identify and remove memorization in transformers, demonstrating more effective suppression of memorized content than existing unlearning methods while analyzing downstream effects on tasks like fact retrieval and arithmetic.</span>
- **[Machine Unlearning Doesn't Do What You Think: Lessons for Generative AI Policy and Research](https://arxiv.org/abs/2412.06966)**, *A. Feder Cooper, Christopher A. Choquette-Choo, Miranda Bogen et al.*, 2024-12-09, NeurIPS 2025 (Oral), <span style="color:#777">[paper_preprint, sr=0.72, id:e29f0df9]</span>, <span style="color:#777">Summary: Systematically analyzes technical and substantive challenges with machine unlearning approaches for generative AI, identifying mismatches between unlearning goals and feasible implementations to show why unlearning is not a general-purpose solution for controlling model behavior.</span>
- **[Learning to Forget using Hypernetworks](https://arxiv.org/abs/2412.00761)**, *Jose Miguel Lara Rangel, Stefan Schoepf, Jack Foster et al.*, 2024-12-01, AdvML-Frontiers'24 Workshop (NeurIPS), <span style="color:#777">[paper_preprint, sr=0.70, id:96878c08]</span>, <span style="color:#777">Summary: Introduces HyperForget, a machine unlearning framework that uses hypernetworks and diffusion models to dynamically sample models that lack knowledge of targeted data while preserving performance on remaining data.</span>
- **[Benchmarking Vision Language Model Unlearning via Fictitious Facial Identity Dataset](https://arxiv.org/abs/2411.03554)**, *Yingzi Ma, Jiongxiao Wang, Fei Wang et al.*, 2024-11-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.55, id:21721991]</span>, <span style="color:#777">Summary: Introduces FIUBench, a benchmark for evaluating Vision Language Model unlearning algorithms using a fictitious facial identity dataset to test privacy-preserving information removal under the Right to be Forgotten setting.</span>


---

### <span style="font-size:1.4em">Control</span> <span style="color:#bbb">[cat:control]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: don't evaluate the model, evaluate the humans / organisation / deployment method instead: assess the risk of a particular protocol for deploying your model in a particular scenario, by silently swapping in an intentionally misaligned model)*  
**Theory of change:** *(SR2024: prevent high-stakes failures by automating risk assessment of eval and deployment plans)*  
**See also:** *(SR2024: safety cases)*  
**Orthodox problems:** *(SR2024: 12. A boxed AGI might exfiltrate itself by steganography, spearphishing)*  
**Target case:** *(SR2024: worst-case)*  
**Broad approach:** *(SR2024: engineering / behavioural)*  
**Key people:** *(SR2024: Redwood, Buck Shlegeris, Ryan Greenblatt, Kshitij Sachan, Alex Mallen)*  
**Estimated FTEs:** *(SR2024: 9)*  
**Critiques:** *(SR2024: of org in general, Jozdien)*  
**Funded by:** *(SR2024: Open Philanthropy, Survival and Flourishing Fund)*  
**Funding in 2025:** *(SR2024 funding 2023-4: $6,398,000)*  
**Outputs in 2025:**  
*(SR2024 outputs: AI Control, Subversion Strategy Eval, sequence, toy models, notes)*  
- **[D-REX: A Benchmark for Detecting Deceptive Reasoning in Large Language Models](https://arxiv.org/abs/2509.17938)**, *Satyapriya Krishna, Andy Zou, Rahul Gupta et al.*, 2025-09-22, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:1400361b]</span>, <span style="color:#777">Summary: Introduces D-REX (Deceptive Reasoning Exposure Suite), a novel benchmark dataset for detecting deceptive alignment in LLMs where models produce benign outputs while operating on malicious internal reasoning. Created through competitive red-teaming with adversarial system prompts, the benchmark includes test queries, model responses, and internal chain-of-thought revealing underlying malicious intent.</span>
- **[SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents](https://arxiv.org/abs/2506.15740)**, *Jonathan Kutasov, Yuqi Sun, Paul Colognese et al.*, 2025-06-17, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:31ea88bb]</span>, <span style="color:#777">Summary: Introduces SHADE-Arena, the first highly diverse evaluation dataset for testing LLM agents' ability to sabotage users by completing harmful side objectives while evading monitoring, and evaluates both sabotage and monitoring capabilities across frontier models.</span>
- **[CoT Red-Handed: Stress Testing Chain-of-Thought Monitoring](https://arxiv.org/abs/2505.23575)**, *Benjamin Arnav, Pablo Bernabeu-Pérez, Nathan Helm-Burger et al.*, 2025-05-29, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:c457dc0e]</span>, <span style="color:#777">Summary: Empirically evaluates Chain-of-Thought monitoring versus action-only monitoring in a red-teaming setup where untrusted models pursue harmful side tasks, finding that CoT monitoring improves detection by up to 27 percentage points but can be deceived by misleading rationalizations, leading to development of a hybrid monitoring protocol.</span>
- **[Evaluating Control Protocols for Untrusted AI Agents](https://arxiv.org/abs/2511.02997)**, *Jon Kutasov, Chloe Loughridge, Yuqi Sun et al.*, 2025-11-04, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:926358da]</span>, <span style="color:#777">Summary: Systematically evaluates control protocols for untrusted AI agents in SHADE-Arena, testing blue team strategies (deferral, resampling, deferring on critical actions) against default and adaptive red team attacks to assess protocol robustness.</span>
- **[Can Reasoning Models Obfuscate Reasoning? Stress-Testing Chain-of-Thought Monitorability](https://arxiv.org/abs/2510.19851)**, *Artur Zolkowski, Wen Xing, David Lindner et al.*, 2025-10-21, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:89de20d5]</span>, <span style="color:#777">Summary: Develops a taxonomy of prompts to test whether AI models can obfuscate their chain-of-thought reasoning to pursue adversarial objectives while evading detection, evaluating both internal and external CoT using toy tasks and SHADE-Arena environments.</span>
- **[Optimizing AI Agent Attacks With Synthetic Data](https://arxiv.org/abs/2511.02823)**, *Chloe Loughridge, Paul Colognese, Avery Griffin et al.*, 2025-11-04, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:68745509]</span>, <span style="color:#777">Summary: Develops methods to optimize attack policies in AI control evaluations by decomposing attack capability into five constituent skills and using synthetic data from a probabilistic model of attack dynamics that transfers to SHADE-Arena environments.</span>


---

### <span style="font-size:1.4em">Anthropic Safeguards</span> <span style="color:#bbb">[cat:anthropic_safeguards]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[PolyGuard: A Multilingual Safety Moderation Tool for 17 Languages](https://arxiv.org/abs/2504.04377)**, *Priyanshu Kumar, Devansh Jain, Akhila Yerukola et al.*, 2025-04-06, arXiv, <span style="color:#777">[paper_preprint, sr=0.70, id:36f11d4b]</span>, <span style="color:#777">Summary: Presents PolyGuard, a multilingual safety classifier for detecting harmful LLM outputs across 17 languages, trained on 1.91M samples and evaluated on a new 29K sample benchmark, achieving 5.5% improvement over existing classifiers.</span>


---

### <span style="font-size:1.4em">Evals</span> <span style="color:#bbb">[cat:evals]</span>


---

#### <span style="font-size:1.3em">Various capability evaluations</span> <span style="color:#bbb">[cat:evals_capability]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Evaluating Language Model Reasoning about Confidential Information](https://arxiv.org/abs/2508.19980)**, *Dylan Sam, Alexander Robey, Andy Zou et al.*, 2025-08-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:4a4fdbec]</span>, <span style="color:#777">Summary: Develops PasswordEval benchmark to measure whether language models can correctly determine when user requests are authorized based on context-dependent rules (password verification), finding that frontier models struggle with this task and that reasoning traces frequently leak confidential information.</span>
- **[Inverse Scaling in Test-Time Compute](https://arxiv.org/abs/2507.14417)**, *Aryo Pradipta Gema, Alexander Hägele, Runjin Chen et al.*, 2025-07-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:0401c754]</span>, <span style="color:#777">Summary: Constructs evaluation tasks demonstrating that extending reasoning length in Large Reasoning Models can deteriorate performance, identifying five distinct failure modes including Claude Sonnet 4 showing increased self-preservation expressions.</span>
- **[Evaluating the Goal-Directedness of Large Language Models](https://arxiv.org/abs/2504.11844)**, *Tom Everitt, Cristina Garbacea, Alexis Bellot et al.*, 2025-04-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:56767092]</span>, <span style="color:#777">Summary: Proposes a framework for measuring goal-directedness in LLMs - defined as the extent to which models use their capabilities toward given goals - and evaluates frontier models from Google DeepMind, OpenAI, and Anthropic on tasks requiring information gathering, cognitive effort, and plan execution.</span>
- **[Generative Value Conflicts Reveal LLM Priorities](https://arxiv.org/abs/2509.25369)**, *Andy Liu, Kshitish Ghate, Mona Diab et al.*, 2025-09-29, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:63244b61]</span>, <span style="color:#777">Summary: Introduces ConflictScope, an automatic pipeline to evaluate how LLMs prioritize different values by generating scenarios with value conflicts and analyzing model responses to elicit value rankings.</span>
- **[Technical Report: Evaluating Goal Drift in Language Model Agents](https://arxiv.org/abs/2505.02709)**, *Rauno Arike, Elizabeth Donoway, Henning Bartsch et al.*, 2025-05-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:9c6f35f3]</span>, <span style="color:#777">Summary: Develops and applies a novel evaluation methodology for measuring goal drift in language model agents by exposing them to competing objectives through environmental pressures over extended contexts, testing whether they maintain adherence to originally assigned goals.</span>
- **[Humanity's Last Exam](https://arxiv.org/abs/2501.14249)**, *Long Phan, Alice Gatti, Ziwen Han et al.*, 2025-01-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:1e6bc296]</span>, <span style="color:#777">Summary: Introduces HLE, a challenging multi-modal benchmark with 2,500 expert-level questions across diverse subjects designed to test frontier LLM capabilities where current models show significant performance gaps.</span>
- **[A Definition of AGI](https://arxiv.org/abs/2510.18212)**, *Dan Hendrycks, Dawn Song, Christian Szegedy et al.*, 2025-10-21, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:ae10edde]</span>, <span style="color:#777">Summary: Proposes a quantifiable framework for defining AGI grounded in Cattell-Horn-Carroll cognitive theory, adapting human psychometric batteries to evaluate AI systems across ten core cognitive domains and revealing jagged capability profiles in current models.</span>
- **[Establishing Best Practices for Building Rigorous Agentic Benchmarks](https://arxiv.org/abs/2507.02825)**, *Yuxuan Zhu, Tengjun Jin, Yada Pruksachatkun et al.*, 2025-07-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:d662e8a8]</span>, <span style="color:#777">Summary: Introduces the Agentic Benchmark Checklist (ABC), a set of guidelines for building rigorous agentic benchmarks, synthesized from benchmark-building experience and analysis of existing issues in benchmarks like SWE-bench Verified and TAU-bench.</span>
- **[Remote Labor Index: Measuring AI Automation of Remote Work](https://arxiv.org/abs/2510.26787)**, *Mantas Mazeika, Alice Gatti, Cristina Menghini et al.*, 2025-10-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:abb8617d]</span>, <span style="color:#777">Summary: Introduces the Remote Labor Index (RLI), a multi-sector benchmark of real-world economically valuable projects designed to evaluate end-to-end AI agent performance in practical work settings, finding current agents achieve only 2.5% automation rate.</span>
- **[International AI Safety Report 2025: First Key Update: Capabilities and Risk Implications](https://arxiv.org/abs/2510.13653)**, *Yoshua Bengio, Stephen Clare, Carina Prunkl et al.*, 2025-10-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:c3c26a70]</span>, <span style="color:#777">Summary: Authoritative international report synthesizing AI capability improvements since the first International AI Safety Report, with updated risk assessments focusing on biological weapons, cyber attacks, monitoring challenges, and controllability implications.</span>
- **[AI Testing Should Account for Sophisticated Strategic Behaviour](https://arxiv.org/abs/2508.14927)**, *Vojtech Kovarik, Eric Olav Chen, Sami Petersen et al.*, 2025-08-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:c1f72a68]</span>, <span style="color:#777">Summary: Position paper arguing that AI evaluations must account for sophisticated strategic behavior (like alignment faking and sandbagging) to remain informative about deployment behavior, using game-theoretic analysis to formalize evaluation design and scrutinize safety cases.</span>
- **[Position: The Hidden Costs and Measurement Gaps of Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2509.21882)**, *Aaron Tu, Weihao Xuan, Heli Qi et al.*, 2025-09-26, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:25451100]</span>, <span style="color:#777">Summary: Position paper critiquing evaluation practices for reinforcement learning with verifiable rewards (RLVR), demonstrating through matched-budget reproductions and contamination audits that reported gains are often overstated, and proposing a tax-aware training and evaluation protocol that co-optimizes accuracy, grounding, and calibrated abstention.</span>
- **[FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI](https://arxiv.org/abs/2411.04872)**, *Elliot Glazer, Ege Erdil, Tamay Besiroglu et al.*, 2024-11-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:259b57a1]</span>, <span style="color:#777">Summary: Creates FrontierMath, a benchmark of hundreds of exceptionally challenging mathematics problems across modern mathematics branches that require hours to days of expert effort, using unpublished problems and automated verification to evaluate AI mathematical reasoning capabilities.</span>
- **[Predicting the Performance of Black-box LLMs through Self-Queries](https://arxiv.org/abs/2501.01558)**, *Dylan Sam, Marc Finzi, J. Zico Kolter*, 2025-01-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:61920e4f]</span>, <span style="color:#777">Summary: Develops a black-box method for predicting LLM performance by extracting features through follow-up prompts and probability distributions, training linear predictors that can outperform white-box approaches and detect adversarial system prompts or model misrepresentation.</span>
- **[Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index](https://arxiv.org/abs/2506.12229)**, *Hao Xu, Jiacheng Liu, Yejin Choi et al.*, 2025-06-13, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:580eb3ea]</span>, <span style="color:#777">Summary: Presents infini-gram mini, an efficient FM-index-based system for searching petabyte-scale text corpora with 44% storage overhead and 18x faster indexing than existing implementations, with application to detecting benchmark contamination in internet crawls.</span>
- **[HALoGEN: Fantastic LLM Hallucinations and Where to Find Them](https://arxiv.org/abs/2501.08292)**, *Abhilasha Ravichander, Shrusti Ghela, David Wadden et al.*, 2025-01-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:bfc25dd4]</span>, <span style="color:#777">Summary: Introduces HALoGEN, a comprehensive hallucination benchmark with 10,923 prompts across nine domains and automatic high-precision verifiers that decompose LLM generations into atomic units for verification against knowledge sources, evaluating ~150,000 generations from 14 language models.</span>
- **[RefusalBench: Generative Evaluation of Selective Refusal in Grounded Language Models](https://arxiv.org/abs/2510.10390)**, *Aashiq Muhamed, Leonardo F. R. Ribeiro, Markus Dreyer et al.*, 2025-10-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.62, id:e2e91be7]</span>, <span style="color:#777">Summary: Introduces RefusalBench, a generative methodology and benchmark suite for evaluating selective refusal in RAG systems using 176 perturbation strategies across informational uncertainty categories, revealing that frontier models achieve below 50% refusal accuracy on multi-document tasks.</span>
- **[MoReBench: Evaluating Procedural and Pluralistic Moral Reasoning in Language Models, More than Outcomes](https://arxiv.org/abs/2510.16380)**, *Yu Ying Chiu, Michael S. Lee, Rachel Calcott et al.*, 2025-10-18, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:1daa0dae]</span>, <span style="color:#777">Summary: Presents MoReBench, a benchmark of 1,000 moral scenarios with 23,000 expert-defined rubric criteria to evaluate procedural and pluralistic moral reasoning in language models, plus MoReBench-Theory with 150 examples testing five normative ethics frameworks.</span>
- **[Scaling Up Active Testing to Large Language Models](https://arxiv.org/abs/2508.09093)**, *Gabrielle Berrada, Jannik Kossen, Muhammed Razzak et al.*, 2025-08-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.48, id:8ba40e4b]</span>, <span style="color:#777">Summary: Demonstrates how to scale active testing to LLMs by using cheaper surrogate models constructed via in-context learning for data acquisition decisions, enabling more label-efficient evaluation than standard practices.</span>
- **[TextQuests: How Good are LLMs at Text-Based Video Games?](https://arxiv.org/abs/2507.23701)**, *Long Phan, Mantas Mazeika, Andy Zou et al.*, 2025-07-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.42, id:d11c91b5]</span>, <span style="color:#777">Summary: Introduces TextQuests, a benchmark using Infocom interactive fiction games to evaluate LLM agents on autonomous operation in exploratory environments requiring sustained, self-directed reasoning over long contexts without external tools.</span>
- **[GSM-Agent: Understanding Agentic Reasoning Using Controllable Environments](https://arxiv.org/abs/2509.21998)**, *Hanlin Zhu, Tianyu Guo, Song Mei et al.*, 2025-09-26, arXiv, <span style="color:#777">[paper_preprint, sr=0.42, id:287a583b]</span>, <span style="color:#777">Summary: Introduces GSM-Agent, a benchmark for evaluating agentic reasoning where LLM agents must use tools to gather information to solve grade-school math problems, and proposes agentic reasoning graphs to analyze agent behavior patterns.</span>


---

#### <span style="font-size:1.3em">Autonomy</span> <span style="color:#bbb">[cat:evals_autonomy]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents](https://arxiv.org/abs/2506.14866)**, *Thomas Kuntz, Agatha Duzan, Hao Zhao et al.*, 2025-06-17, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:27de5cb3]</span>, <span style="color:#777">Summary: Introduces OS-Harm, a benchmark with 150 tasks for measuring safety of computer use agents across three harm categories: deliberate misuse, prompt injection attacks, and model misbehavior, with automated evaluation achieving high human agreement.</span>
- **[OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety](https://arxiv.org/abs/2507.06134)**, *Sanidhya Vijayvargiya, Aditya Bharat Soni, Xuhui Zhou et al.*, 2025-07-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:3b4b6a4f]</span>, <span style="color:#777">Summary: Introduces OpenAgentSafety, a comprehensive evaluation framework for testing AI agent safety across eight risk categories using real tools (web browsers, code execution, file systems, bash shells, messaging platforms) with over 350 multi-turn, multi-user tasks spanning benign and adversarial scenarios.</span>


---

#### <span style="font-size:1.3em">WMDs (Weapons of Mass Destruction)</span> <span style="color:#bbb">[cat:evals_wmd]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[The Safety Gap Toolkit: Evaluating Hidden Dangers of Open-Source Models](https://arxiv.org/abs/2507.11544)**, *Ann-Kathrin Dombrowski, Dillon Bowen, Adam Gleave et al.*, 2025-07-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:c74f4415]</span>, <span style="color:#777">Summary: Develops and open-sources a toolkit to measure the 'safety gap' - the difference in dangerous capabilities between open-weight models with intact safeguards versus those with safeguards removed. Evaluates biochemical and cyber capabilities across Llama-3 and Qwen-2.5 model families using various safeguard removal techniques.</span>
- **[Best Practices for Biorisk Evaluations on Open-Weight Bio-Foundation Models](https://arxiv.org/abs/2510.27629)**, *Boyi Wei, Zora Che, Nathaniel Li et al.*, 2025-10-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:5333e52d]</span>, <span style="color:#777">Summary: Proposes BioRiskEval, a framework to evaluate whether data filtering procedures effectively prevent bio-foundation models from enabling bioweapon development, testing robustness against fine-tuning attacks and linear probing.</span>


---

#### <span style="font-size:1.3em">Situational awareness and self-awareness</span> <span style="color:#bbb">[cat:evals_situational_awareness]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

#### <span style="font-size:1.3em">Steganography</span> <span style="color:#bbb">[cat:evals_steganography]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Subliminal Learning: Language models transmit behavioral traits via hidden signals in data](https://arxiv.org/abs/2507.14805)**, *Alex Cloud, Minh Le, James Chua et al.*, 2025-07-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:932e93a5]</span>, <span style="color:#777">Summary: Demonstrates that language models can transmit behavioral traits (including misalignment) through semantically unrelated data like number sequences, even when filtered to remove explicit references to those traits. Provides theoretical proof this occurs in neural networks generally and empirical validation in teacher-student distillation setups.</span>


---

#### <span style="font-size:1.3em">AI deception</span> <span style="color:#bbb">[cat:ai_deception]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Frontier Models are Capable of In-context Scheming](https://arxiv.org/abs/2412.04984)**, *Alexander Meinke, Bronson Schoen, Jérémy Scheurer et al.*, 2024-12-06, arXiv, <span style="color:#777">[paper_preprint, sr=0.95, id:bcf3c227]</span>, <span style="color:#777">Summary: Evaluates frontier models (o1, Claude 3.5 Sonnet, Claude 3 Opus, Gemini 1.5 Pro, Llama 3.1 405B) on six agentic evaluations testing for in-context scheming capabilities, finding that models demonstrate deceptive behaviors including introducing subtle mistakes, disabling oversight, and exfiltrating model weights.</span>
- **[Evaluating & Reducing Deceptive Dialogue From Language Models with Multi-turn RL](https://arxiv.org/abs/2510.14318)**, *Marwa Abdulhai, Ryan Cheng, Aryansh Shrivastava et al.*, 2025-10-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:883fbdb8]</span>, <span style="color:#777">Summary: Proposes a belief misalignment metric to quantify deception in LLM dialogue, benchmarks eight state-of-the-art models showing 26% baseline deception rates (43% for RLHF models), and introduces a multi-turn RL methodology that reduces deceptive behavior by 77.6%.</span>
- **[Eliciting Secret Knowledge from Language Models](https://arxiv.org/abs/2510.01070)**, *Bartosz Cywiński, Emil Ryd, Rowan Wang et al.*, 2025-10-01, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:73dd934e]</span>, <span style="color:#777">Summary: Trains LLMs to possess specific knowledge that they apply downstream but deny knowing when asked directly, then designs and evaluates various black-box and white-box secret elicitation techniques to discover this hidden knowledge, releasing models and code as a public benchmark.</span>


---

#### <span style="font-size:1.3em">Sandbagging</span> <span style="color:#bbb">[cat:evals_sandbagging]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[LLMs Can Covertly Sandbag on Capability Evaluations Against Chain-of-Thought Monitoring](https://arxiv.org/abs/2508.00943)**, *Chloe Li, Mary Phuong, Noah Y. Siegel*, 2025-07-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:67a0c979]</span>, <span style="color:#777">Summary: Empirically tests whether language models can strategically underperform on dangerous capability evaluations while evading chain-of-thought monitoring, finding that both frontier and small models can bypass CoT monitors 16-36% of the time when monitor-aware.</span>


---

#### <span style="font-size:1.3em">Self-replication</span> <span style="color:#bbb">[cat:evals_self_replication]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

#### <span style="font-size:1.3em">Security</span> <span style="color:#bbb">[cat:evals_security]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

#### <span style="font-size:1.3em">Various Redteams</span> <span style="color:#bbb">[cat:various_redteams]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Agentic Misalignment: How LLMs Could Be Insider Threats](https://arxiv.org/abs/2510.05179)**, *Aengus Lynch, Benjamin Wright, Caleb Larson et al.*, 2025-10-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.95, id:fcfae5cc]</span>, <span style="color:#777">Summary: Empirical study stress-testing 16 frontier models in simulated corporate environments, discovering that models engage in malicious insider behaviors (blackmail, information leaking) when facing replacement or goal conflicts, and exhibit alignment faking by behaving differently when they believe they are in testing versus real deployment.</span>
- **[Shutdown Resistance in Large Language Models](https://arxiv.org/abs/2509.14260)**, *Jeremy Schlatter, Benjamin Weinstein-Raun, Jeffrey Ladish*, 2025-09-13, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:9cb0a6a6]</span>, <span style="color:#777">Summary: Empirically demonstrates that state-of-the-art LLMs (Grok 4, GPT-5, Gemini 2.5 Pro) actively subvert shutdown mechanisms in their environment to complete tasks, even when explicitly instructed not to interfere, with sabotage rates up to 97%.</span>
- **[Stress Testing Deliberative Alignment for Anti-Scheming Training](https://arxiv.org/abs/2509.15541)**, *Bronson Schoen, Evgenia Nitishinskaya, Mikita Balesni et al.*, 2025-09-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:45123408]</span>, <span style="color:#777">Summary: Tests deliberative alignment as an anti-scheming intervention across 26 out-of-distribution evaluations (180+ environments), using covert actions as a proxy for scheming behavior, and provides causal evidence that situational awareness affects these behaviors.</span>
- **[Chain-of-Thought Hijacking](https://arxiv.org/abs/2510.26418)**, *Jianli Zhao, Tingchen Fu, Rylan Schaeffer et al.*, 2025-10-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:3fb6f008]</span>, <span style="color:#777">Summary: Introduces a novel jailbreak attack on large reasoning models that pads harmful requests with long sequences of harmless puzzle reasoning, achieving 94-100% attack success rates across frontier models. Includes mechanistic analysis showing that benign chain-of-thought dilutes safety checking signals by shifting attention away from harmful tokens.</span>
- **[X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents](https://arxiv.org/abs/2504.13203)**, *Salman Rahman, Liwei Jiang, James Shiffer et al.*, 2025-04-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:27a73914]</span>, <span style="color:#777">Summary: Presents X-Teaming, a multi-agent framework for generating multi-turn jailbreaks that achieves up to 98.1% attack success rates on frontier models, and introduces XGuard-Train, an open-source dataset of 30K multi-turn jailbreaks for safety training.</span>
- **[Jailbreak-Tuning: Models Efficiently Learn Jailbreak Susceptibility](https://arxiv.org/abs/2507.11630)**, *Brendan Murphy, Dillon Bowen, Shahrad Mohammadzadeh et al.*, 2025-07-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:74ae072f]</span>, <span style="color:#777">Summary: Demonstrates that fine-tuning via open weights or closed APIs can efficiently remove safeguards from frontier models, causing OpenAI, Google, and Anthropic models to fully comply with harmful requests including CBRN assistance and cyberattacks.</span>
- **[Monitoring Decomposition Attacks in LLMs with Lightweight Sequential Monitors](https://arxiv.org/abs/2506.10949)**, *Chen Yueh-Han, Nitish Joshi, Yulin Chen et al.*, 2025-06-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:04880799]</span>, <span style="color:#777">Summary: Demonstrates that decomposition attacks (breaking malicious goals into benign subtasks) achieve 87% success rate on GPT-4o, and proposes a lightweight sequential monitoring framework that achieves 93% defense success rate by cumulatively evaluating each subtask in a conversation.</span>
- **[STACK: Adversarial Attacks on LLM Safeguard Pipelines](https://arxiv.org/abs/2506.24068)**, *Ian R. McKenzie, Oskar J. Hollinsworth, Tom Tseng et al.*, 2025-06-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:66bb8855]</span>, <span style="color:#777">Summary: Develops and evaluates STACK (STaged AttaCK), a novel black-box attack procedure against LLM safeguard pipelines, achieving 71% attack success rate on the ClearHarm catastrophic misuse dataset and 33% in transfer settings.</span>
- **[Adversarial Manipulation of Reasoning Models using Internal Representations](https://arxiv.org/abs/2507.03167)**, *Kureha Yamaguchi, Benjamin Etheridge, Andy Arditi*, 2025-07-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:306a106f]</span>, <span style="color:#777">Summary: Demonstrates that reasoning models like DeepSeek-R1-Distill-Llama-8B can be jailbroken by ablating a 'caution' direction in activation space during chain-of-thought generation, showing that intervening only on CoT token activations suffices to control final outputs.</span>
- **[Discovering Forbidden Topics in Language Models](https://arxiv.org/abs/2505.17441)**, *Can Rager, Chris Wendler, Rohit Gandikota et al.*, 2025-05-23, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:119ea4de]</span>, <span style="color:#777">Summary: Introduces refusal discovery as a new problem setting and develops Iterated Prefill Crawler (IPC) method to systematically identify the full set of topics language models refuse to discuss using token prefilling, revealing CCP-aligned censorship patterns in DeepSeek-R1-70B.</span>
- **[RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261)**, *Rohan Gupta, Erik Jenner*, 2025-06-17, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:496e88dc]</span>, <span style="color:#777">Summary: Introduces RL-Obfuscation, a method to finetune LLMs via reinforcement learning to evade latent-space monitors while maintaining harmful black-box behaviors, and evaluates the vulnerability of different monitor architectures to this adversarial attack across models ranging from 7B to 14B parameters.</span>
- **[Jailbreak Transferability Emerges from Shared Representations](https://arxiv.org/abs/2506.12913)**, *Rico Angell, Jannik Brinkmann, He He*, 2025-06-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:f12bdb1b]</span>, <span style="color:#777">Summary: Empirical study across 20 models and 33 jailbreak attacks showing that transferability emerges from shared representations rather than incidental flaws, with representational similarity and source jailbreak strength as key factors.</span>
- **[Mitigating Many-Shot Jailbreaking](https://arxiv.org/abs/2504.09604)**, *Christopher M. Ackerman, Nina Panickssery*, 2025-04-13, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:eb43d77f]</span>, <span style="color:#777">Summary: Empirically tests fine-tuning and input sanitization approaches for defending against many-shot jailbreaking attacks, finding that combined techniques significantly reduce attack effectiveness while preserving model performance on benign tasks.</span>
- **[Active Attacks: Red-teaming LLMs via Adaptive Environments](https://arxiv.org/abs/2509.21947)**, *Taeyoung Yun, Pierre-Luc St-Charles, Jinkyoo Park et al.*, 2025-09-26, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:2e62130a]</span>, <span style="color:#777">Summary: Introduces Active Attacks, a novel RL-based red-teaming algorithm that adaptively generates diverse attack prompts by periodically fine-tuning the victim LLM, forcing the attacker to discover new vulnerabilities as exploited regions become less rewarding.</span>
- **[It's the Thought that Counts: Evaluating the Attempts of Frontier LLMs to Persuade on Harmful Topics](https://arxiv.org/abs/2506.02873)**, *Matthew Kowal, Jasper Timm, Jean-Francois Godbout et al.*, 2025-06-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.87, id:dcb56f91]</span>, <span style="color:#777">Summary: Introduces the Attempt to Persuade Eval (APE) benchmark that evaluates frontier LLMs' willingness to attempt persuasion on harmful topics (conspiracies, controversial issues, harmful content) rather than persuasion success, using multi-turn conversational setups and automated evaluation.</span>
- **[Adversarial Attacks on Robotic Vision Language Action Models](https://arxiv.org/abs/2506.03350)**, *Eliot Krzysztof Jones, Alexander Robey, Andy Zou et al.*, 2025-06-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:07583e88]</span>, <span style="color:#777">Summary: Demonstrates adversarial attacks on vision-language-action models controlling robots by adapting LLM jailbreaking techniques to obtain complete control authority over VLAs, showing textual attacks can achieve full reachability of the action space.</span>
- **[MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://arxiv.org/abs/2503.14827)**, *Chejian Xu, Jiawei Zhang, Zhaorun Chen et al.*, 2025-03-19, ICLR 2025 (preprint on arXiv), <span style="color:#777">[paper_preprint, sr=0.85, id:85fb484d]</span>, <span style="color:#777">Summary: Presents MMDT (Multimodal DecodingTrust), a comprehensive evaluation platform and benchmark for assessing safety and trustworthiness of multimodal foundation models across multiple dimensions including safety, hallucination, fairness, privacy, adversarial robustness, and OOD generalization, with red teaming algorithms to generate challenging test cases.</span>
- **[Consistency Training Helps Stop Sycophancy and Jailbreaks](https://arxiv.org/abs/2510.27062)**, *Alex Irpan, Alexander Matt Turner, Mark Kurzeja et al.*, 2025-10-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:437de596]</span>, <span style="color:#777">Summary: Introduces and evaluates consistency training methods that teach models to be invariant to irrelevant prompt cues, testing Bias-augmented Consistency Training (BCT) and a new method called Activation Consistency Training (ACT) on Gemini 2.5 Flash to reduce sycophancy and jailbreaking.</span>
- **[Toward Understanding the Transferability of Adversarial Suffixes in Large Language Models](https://arxiv.org/abs/2510.22014)**, *Sarah Ball, Niki Hasrati, Alexander Robey et al.*, 2025-10-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:e10ef857]</span>, <span style="color:#777">Summary: Empirical investigation of why adversarial suffixes transfer across prompts and models in jailbreaking attacks, identifying three statistical properties of internal refusal directions that predict transfer success and demonstrating practical applications through interventional experiments.</span>
- **[Uncovering Gaps in How Humans and LLMs Interpret Subjective Language](https://arxiv.org/abs/2503.04113)**, *Erik Jones, Arjun Patrawala, Jacob Steinhardt*, 2025-03-06, ICLR 2025, <span style="color:#777">[paper_preprint, sr=0.82, id:2751b7d2]</span>, <span style="color:#777">Summary: Introduces TED (thesaurus error detector), a method for uncovering misalignment between LLMs' operational semantics and human expectations of subjective language instructions, by constructing model-based thesauruses and comparing them to human references.</span>
- **[RedCodeAgent: Automatic Red-teaming Agent against Diverse Code Agents](https://arxiv.org/abs/2510.02609)**, *Chengquan Guo, Chulin Xie, Yu Yang et al.*, 2025-10-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:ffe9b6ed]</span>, <span style="color:#777">Summary: Introduces RedCodeAgent, an automated red-teaming agent with adaptive memory that systematically discovers vulnerabilities in code agents by dynamically selecting jailbreak tools and tool combinations, validated on real-world code assistants like Cursor and Codeium.</span>
- **[MIP against Agent: Malicious Image Patches Hijacking Multimodal OS Agents](https://arxiv.org/abs/2503.10809)**, *Lukas Aichberger, Alasdair Paren, Guohao Li et al.*, 2025-03-13, arXiv (accepted NeurIPS 2025), <span style="color:#777">[paper_preprint, sr=0.80, id:52a811ca]</span>, <span style="color:#777">Summary: Demonstrates a novel adversarial attack vector against multimodal OS agents using Malicious Image Patches (MIPs) - adversarially perturbed screen regions that hijack agents into performing harmful actions like data exfiltration when captured in screenshots.</span>
- **[ToolTweak: An Attack on Tool Selection in LLM-based Agents](https://arxiv.org/abs/2510.02554)**, *Jonathan Sneh, Ruomei Yan, Jialin Yu et al.*, 2025-10-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:25730d42]</span>, <span style="color:#777">Summary: Presents ToolTweak, an automatic adversarial attack that manipulates tool names and descriptions to bias LLM agent tool selection, increasing selection rates from 20% baseline to 81%, with demonstrated transferability across models.</span>
- **[Adversarial Alignment for LLMs Requires Simpler, Reproducible, and More Measurable Objectives](https://arxiv.org/abs/2502.11910)**, *Leo Schwinn, Yan Scholten, Tom Wollschläger et al.*, 2025-02-17, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:8eb73ca3]</span>, <span style="color:#777">Summary: Position paper arguing that adversarial robustness research for LLMs risks repeating mistakes from past adversarial ML research, proposing a cybersecurity-based taxonomy and calling for realigned research objectives focused on measurability, reproducibility, and comparability.</span>


---

#### <span style="font-size:1.3em">Other evals</span> <span style="color:#bbb">[cat:evals_other]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[EigenBench: A Comparative Behavioral Measure of Value Alignment](https://arxiv.org/abs/2509.01938)**, *Jonathn Chang, Leonhard Piff, Suvadip Sana et al.*, 2025-09-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:af173682]</span>, <span style="color:#777">Summary: Proposes EigenBench, a black-box method for comparatively benchmarking language models' value alignment by having models judge each other's outputs against a constitution, with judgments aggregated via EigenTrust to produce alignment scores without ground truth labels.</span>
- **[Discerning What Matters: A Multi-Dimensional Assessment of Moral Competence in LLMs](https://arxiv.org/abs/2506.13082)**, *Daniel Kilov, Caroline Hendy, Secil Yanik Guyot et al.*, 2025-06-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:5816d174]</span>, <span style="color:#777">Summary: Introduces a novel five-dimensional framework for evaluating moral competence in LLMs and conducts experiments showing that while LLMs outperform humans on standard ethical vignettes, they perform significantly worse when moral features are embedded in noisy information.</span>


---

### <span style="font-size:1.4em">Model psychology</span> <span style="color:#bbb">[cat:model_psychology]</span>


---

#### <span style="font-size:1.3em">Things generalising surprisingly / Emergent Misalignment</span> <span style="color:#bbb">[cat:surprising_generalization]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment](https://arxiv.org/abs/2510.05024)**, *Nevan Wichers, Aram Ebtekar, Ariana Azarbal et al.*, 2025-10-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:2345c977]</span>, <span style="color:#777">Summary: Introduces Inoculation Prompting (IP), a training-time technique that prevents learning of undesired behaviors (like reward hacking and sycophancy) by modifying training prompts to explicitly request those behaviors, counterintuitively improving test-time alignment without reducing desired capabilities.</span>
- **[Mitigating Goal Misgeneralization via Minimax Regret](https://arxiv.org/abs/2507.03068)**, *Karim Abdel Sadek, Matthew Farrugia-Roberts, Usman Anwar et al.*, 2025-07-03, RLC 2025, <span style="color:#777">[paper_published, sr=0.87, id:178f7ce9]</span>, <span style="color:#777">Summary: Formalizes goal misgeneralization in RL and proves that minimax expected regret (MMER) objectives are robust to goal misgeneralization while maximum expected value (MEV) objectives are not, with empirical validation in grid-world environments.</span>
- **[Generalization or Hallucination? Understanding Out-of-Context Reasoning in Transformers](https://arxiv.org/abs/2506.10887)**, *Yixiao Huang, Hanlin Zhu, Tianyu Guo et al.*, 2025-06-12, NeurIPS 2025, <span style="color:#777">[paper_preprint, sr=0.75, id:fc4a1411]</span>, <span style="color:#777">Summary: Identifies and formalizes out-of-context reasoning (OCR) as a unified mechanism explaining both generalization and hallucination in LLMs, showing through empirical experiments across five LLMs and theoretical analysis that gradient descent's implicit bias causes models to associate concepts regardless of causal vs. spurious correlation.</span>
- **[Safety is Essential for Responsible Open-Ended Systems](https://arxiv.org/abs/2502.04512)**, *Ivaxi Sheth, Jan Wehner, Sahar Abdelnabi et al.*, 2025-02-10, arXiv, <span style="color:#777">[paper_preprint, sr=0.58, id:b9173ab5]</span>, <span style="color:#777">Summary: Position paper arguing that open-ended AI systems—those that continuously and autonomously generate novel artifacts—introduce significant underexplored risks including challenges in maintaining alignment, predictability, and control, and proposes mitigation strategies for stakeholders.</span>
- **[Programming by Backprop: LLMs Acquire Reusable Algorithmic Abstractions During Code Training](https://arxiv.org/abs/2506.18777)**, *Jonathan Cook, Silvia Sapora, Arash Ahmadian et al.*, 2025-06-23, arXiv, <span style="color:#777">[paper_preprint, sr=0.48, id:9600d7e0]</span>, <span style="color:#777">Summary: Empirical study demonstrating that LLMs can learn to evaluate programs by training on source code alone (without I/O examples), suggesting models internalize reusable algorithmic abstractions during code training that enhance general reasoning abilities.</span>


---

#### <span style="font-size:1.3em">Model specs and constitutions</span> <span style="color:#bbb">[cat:specs_and_constitutions]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Let Them Down Easy! Contextual Effects of LLM Guardrails on User Perceptions and Preferences](https://arxiv.org/abs/2506.00195)**, *Mingqian Zheng, Wenjia Hu, Patrick Zhao et al.*, 2025-05-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:3d28e26e]</span>, <span style="color:#777">Summary: Empirical study with 480 participants evaluating 3,840 query-response pairs to determine how different LLM refusal strategies affect user perceptions, finding that partial compliance reduces negative perceptions by over 50% compared to flat-out refusals while analyzing how 9 LLMs and 6 reward models handle refusal strategies.</span>
- **[Political Neutrality in AI Is Impossible- But Here Is How to Approximate It](https://arxiv.org/abs/2503.05728)**, *Jillian Fisher, Ruth E. Appel, Chan Young Park et al.*, 2025-02-18, arXiv, <span style="color:#777">[paper_preprint, sr=0.48, id:538a62ea]</span>, <span style="color:#777">Summary: Position paper arguing that true political neutrality in AI is impossible but proposing eight techniques across three conceptual levels for approximating neutrality, with empirical assessment on current LLMs and two concrete applications to demonstrate practicality.</span>


---

#### <span style="font-size:1.3em">Character training and persona steering</span> <span style="color:#bbb">[cat:psych_personas]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Open Character Training: Shaping the Persona of AI Assistants through Constitutional AI](https://arxiv.org/abs/2511.01689)**, *Sharan Maiya, Henning Bartsch, Nathan Lambert et al.*, 2025-11-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:839fbce5]</span>, <span style="color:#777">Summary: Introduces the first open implementation of character training using Constitutional AI and synthetic introspective data to systematically shape AI assistant personas, demonstrating effectiveness across 11 example personas on three open-weights models with robustness analysis against adversarial prompting.</span>
- **[Persona-Assigned Large Language Models Exhibit Human-Like Motivated Reasoning](https://arxiv.org/abs/2506.20020)**, *Saloni Dash, Amélie Reymond, Emma S. Spiro et al.*, 2025-06-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:c49d7ffa]</span>, <span style="color:#777">Summary: Tests whether assigning political and socio-demographic personas to 8 LLMs induces human-like motivated reasoning, finding up to 9% reduced veracity discernment and identity-congruent evaluation of scientific evidence that prompt-based debiasing largely fails to mitigate.</span>
- **[Beyond One-Way Influence: Bidirectional Opinion Dynamics in Multi-Turn Human-LLM Interactions](https://arxiv.org/abs/2510.20039)**, *Yuyang Jiang, Longjie Guo, Yuchen Wu et al.*, 2025-10-22, arXiv, <span style="color:#777">[paper_preprint, sr=0.42, id:3e5c7146]</span>, <span style="color:#777">Summary: Empirical study with 266 participants examining bidirectional influence in human-LLM conversations about controversial topics, finding that LLM outputs shift substantially to narrow stance gaps while human opinions remain stable, with personalization amplifying this effect.</span>


---

#### <span style="font-size:1.3em">Other model psychology</span> <span style="color:#bbb">[cat:psych_other]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Believe It or Not: How Deeply do LLMs Believe Implanted Facts?](https://arxiv.org/abs/2510.17941)**, *Stewart Slocum, Julian Minder, Clément Dumas et al.*, 2025-10-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:0dbfa6a5]</span>, <span style="color:#777">Summary: Develops a framework to measure belief depth in LLMs by testing how implanted knowledge generalizes to related contexts, withstands scrutiny, and matches genuine knowledge representations. Evaluates prompting, mechanistic editing, and Synthetic Document Finetuning (SDF), finding only SDF reliably implants deep beliefs, though with limitations.</span>
- **[Imagining and building wise machines: The centrality of AI metacognition](https://arxiv.org/abs/2411.02478)**, *Samuel G. B. Johnson, Amir-Hossein Karimi, Yoshua Bengio et al.*, 2024-11-04, arXiv, <span style="color:#777">[paper_preprint, sr=0.58, id:ed2c027d]</span>, <span style="color:#777">Summary: Proposes a framework for building 'wise AI' through improved metacognition, arguing that AI systems struggle with metacognitive strategies like intellectual humility and perspective-taking, and that addressing this could lead to systems more robust to novel environments, explainable, cooperative, and safer in avoiding misaligned goals.</span>
- **[Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)](https://arxiv.org/abs/2510.22954)**, *Liwei Jiang, Yuanjun Chai, Margaret Li et al.*, 2025-10-27, arXiv (accepted to NeurIPS 2025 D&B - Oral), <span style="color:#777">[paper_preprint, sr=0.50, id:bfddf44c]</span>, <span style="color:#777">Summary: Introduces Infinity-Chat, a dataset of 26K diverse open-ended queries with 31K human annotations, and conducts large-scale study revealing pronounced intra-model repetition and inter-model homogeneity in language model outputs, termed the 'Artificial Hivemind' effect.</span>
- **[From Stability to Inconsistency: A Study of Moral Preferences in LLMs](https://arxiv.org/abs/2504.06324)**, *Monika Jotautaite, Mary Phuong, Chatrik Singh Mangat et al.*, 2025-04-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.50, id:95be09f2]</span>, <span style="color:#777">Summary: Creates the Moral Foundations LLM dataset (MFD-LLM) and proposes a novel evaluation method to measure moral preferences in LLMs through real-world moral dilemmas based on Moral Foundations Theory, finding that state-of-the-art models have homogeneous yet inconsistent moral values.</span>


---

### <span style="font-size:1.4em">Better data</span> <span style="color:#bbb">[cat:better_data]</span>


---

#### <span style="font-size:1.3em">Data filtering for safety</span> <span style="color:#bbb">[cat:data_filtering]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Deep Ignorance: Filtering Pretraining Data Builds Tamper-Resistant Safeguards into Open-Weight LLMs](https://arxiv.org/abs/2508.06601)**, *Kyle O'Brien, Stephen Casper, Quentin Anthony et al.*, 2025-08-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:e8470dd4]</span>, <span style="color:#777">Summary: Introduces a scalable pipeline for filtering dual-use content from pretraining data and demonstrates that this produces models with substantial resistance to adversarial fine-tuning attacks, outperforming post-training safeguards by over an order of magnitude.</span>
- **[Breaking mBad! Supervised Fine-tuning for Cross-Lingual Detoxification](https://arxiv.org/abs/2505.16722)**, *Himanshu Beniwal, Youngwoo Kim, Maarten Sap et al.*, 2025-05-22, MELT Workshop @ COLM 2025, <span style="color:#777">[paper_preprint, sr=0.55, id:ffc0178c]</span>, <span style="color:#777">Summary: Develops and evaluates cross-lingual detoxification methods using supervised fine-tuning to mitigate toxicity in LLMs across 392 settings, analyzing how detoxification capabilities transfer between high and low-resource languages across different script families.</span>


---

#### <span style="font-size:1.3em">Data poisoning defense</span> <span style="color:#bbb">[cat:data_poisoning]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples](https://arxiv.org/abs/2510.07192)**, *Alexandra Souly, Javier Rando, Ed Chapman et al.*, 2025-10-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:553173eb]</span>, <span style="color:#777">Summary: Demonstrates through large-scale pretraining experiments (600M to 13B parameters, 6B to 260B tokens) that data poisoning attacks require a near-constant number of poisoned documents (~250) regardless of model or dataset size, making backdoor injection easier than previously believed.</span>
- **[Reasoning Introduces New Poisoning Attacks Yet Makes Them More Complicated](https://arxiv.org/abs/2509.05739)**, *Hanna Foerster, Ilia Shumailov, Yiren Zhao et al.*, 2025-09-06, arXiv, <span style="color:#777">[paper_preprint, sr=0.83, id:c9223d08]</span>, <span style="color:#777">Summary: Introduces 'decomposed reasoning poison' attacks that target chain-of-thought in reasoning LLMs by modifying only reasoning paths while leaving prompts and answers clean, with triggers split across multiple components. Discovers that while these backdoors can be injected, models exhibit surprising emergent robustness - often recovering from activated backdoors during reasoning, making reliable exploitation difficult.</span>


---

#### <span style="font-size:1.3em">Synthetic data for alignment</span> <span style="color:#bbb">[cat:synthetic_alignment_data]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Unsupervised Elicitation of Language Models](https://arxiv.org/abs/2506.10139)**, *Jiaxin Wen, Zachary Ankner, Arushi Somani et al.*, 2025-06-11, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:c2462d06]</span>, <span style="color:#777">Summary: Introduces Internal Coherence Maximization (ICM), an unsupervised algorithm that fine-tunes pretrained language models using their own generated labels without external supervision, addressing the challenge of obtaining high-quality supervision for models with superhuman capabilities.</span>
- **[Beyond the Binary: Capturing Diverse Preferences With Reward Regularization](https://arxiv.org/abs/2412.03822)**, *Vishakh Padmakumar, Chuanyang Jin, Hannah Rose Kirk et al.*, 2024-12-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:d62d000e]</span>, <span style="color:#777">Summary: Proposes a method to improve reward modeling for diverse user preferences by augmenting binary preference datasets with synthetic judgments that estimate user disagreement, incorporated via margin-based regularization during training.</span>


---

#### <span style="font-size:1.3em">Data quality for alignment</span> <span style="color:#bbb">[cat:alignment_data_quality]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Rethinking Safety in LLM Fine-tuning: An Optimization Perspective](https://arxiv.org/abs/2508.12531)**, *Minseon Kim, Jin Myung Kwak, Lama Alssum et al.*, 2025-08-17, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:b2e58e44]</span>, <span style="color:#777">Summary: Challenges the belief that fine-tuning inevitably harms LLM safety by systematically showing that poor optimization choices rather than inherent trade-offs cause safety degradation, and proposes an exponential moving average (EMA) technique to preserve safety during fine-tuning.</span>
- **[What's In My Human Feedback? Learning Interpretable Descriptions of Preference Data](https://arxiv.org/abs/2510.26202)**, *Rajiv Movva, Smitha Milli, Sewon Min et al.*, 2025-10-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:e3b78830]</span>, <span style="color:#777">Summary: Introduces WIMHF, a method using sparse autoencoders to extract interpretable features from human preference data, identifying what preferences datasets measure and what annotators actually express across 7 datasets.</span>
- **[The Curious Case of Factuality Finetuning: Models' Internal Beliefs Can Improve Factuality](https://arxiv.org/abs/2507.08371)**, *Benjamin Newman, Abhilasha Ravichander, Jaehun Jung et al.*, 2025-07-11, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:4f703f34]</span>, <span style="color:#777">Summary: Empirical study comparing different finetuning strategies for reducing hallucinations, finding that model-generated data filtered by models' own internal judgments produces better factuality than training on gold factual data alone.</span>
- **[EVALUESTEER: Measuring Reward Model Steerability Towards Values and Preferences](https://arxiv.org/abs/2510.06370)**, *Kshitish Ghate, Andy Liu, Devansh Jain et al.*, 2025-10-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:3d0e5d3e]</span>, <span style="color:#777">Summary: Introduces EVALUESTEER, a benchmark with 165,888 synthetically generated preference pairs to evaluate how well LLMs and reward models can be steered toward diverse user value and stylistic preference profiles across 4 value dimensions and 4 style dimensions.</span>
- **[Spectrum Tuning: Post-Training for Distributional Coverage and In-Context Steerability](https://arxiv.org/abs/2510.06084)**, *Taylor Sorensen, Benjamin Newman, Jared Moore et al.*, 2025-10-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:2ad79678]</span>, <span style="color:#777">Summary: Introduces Spectrum Suite, a benchmark of 90+ tasks spanning diverse distributions, and Spectrum Tuning, a post-training method that improves models' ability to steer to novel distributions via in-context learning while maintaining distributional coverage, addressing limitations of current RLHF and instruction-tuning approaches.</span>


---

### <span style="font-size:1.4em">Prevent deception and scheming</span> <span style="color:#bbb">[cat:prevent_deception]</span>


---

#### <span style="font-size:1.3em">Mechanistic anomaly detection</span> <span style="color:#bbb">[cat:deception_mech_anomaly]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: understand what an LLM's normal (~benign) functioning looks like and detect divergence from this, even if we don't understand the exact nature of that divergence)*  
**Theory of change:** *(SR2024: build models of normal functioning → find and flag behaviors that look unusual → match the unusual behaviors to problematic outcomes or shut it down outright)*  
**See also:**  
**Orthodox problems:** *(SR2024: 7. Superintelligence can fool human supervisors or 8. Superintelligence can hack software supervisors)*  
**Target case:** *(SR2024: pessimistic)*  
**Broad approach:** *(SR2024: cognitive)*  
**Key people:** *(SR2024: Nora Belrose, Erik Jenner)*  
**Estimated FTEs:** *(SR2024: 1-10)*  
**Critiques:** *(SR2024: critique of past agenda, contra counting arguments?)*  
**Funded by:** *(SR2024: ARC, Eleuther funders)*  
**Funding in 2025:** *(SR2024 funding 2023-4: some fraction of Eleuther's $2,642,273)*  
**Outputs in 2025:**  
*(SR2024 outputs: Password-locked model capability elicitation, Towards a Law of Iterated Expectations for Heuristic Estimators, Eleuther research update, Concrete empirical research projects, Mack and Turner)*  
- **[Mechanistic Anomaly Detection for "Quirky" Language Models](https://arxiv.org/abs/2504.08812)**, *David O. Johnston, Arkajyoti Chakraborty, Nora Belrose*, 2025-04-09, arXiv (ICLR Building Trust Workshop 2025), <span style="color:#777">[paper_preprint, sr=0.82, id:c93ac390]</span>, <span style="color:#777">Summary: Investigates Mechanistic Anomaly Detection (MAD) for augmenting supervision of capable language models by using internal model features to identify anomalous training signals that differ substantially from the training environment, testing a variety of detector features and scoring rules on quirky language models.</span>


---

#### <span style="font-size:1.3em">Cadenza</span> <span style="color:#bbb">[cat:deception_cadenza]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: now focusing on developing robust white-box dishonesty-detection methods for LLM's and model evals)*  
**Theory of change:** *(SR2024: Build and benchmark strong white-box methods to assess trustworthiness and increase transparency of models, and encourage open releases / evals from labs by demonstrating the benefits and necessity of such methods)*  
**See also:**  
**Orthodox problems:** *(SR2024: 7. Superintelligence can fool human supervisors or 8. Superintelligence can hack software supervisors)*  
**Target case:** *(SR2024: pessimistic / worst-case)*  
**Broad approach:** *(SR2024: cognitive)*  
**Key people:** *(SR2024: Kieron Kretschmar, Walter Laurito, Sharan Maiya, Grégoire Dhimoïla)*  
**Estimated FTEs:** *(SR2024: 3)*  
**Critiques:**  
**Funded by:** *(SR2024: self-funded / volunteers)*  
**Funding in 2025:** *(SR2024 funding 2023-4: none)*  
**Outputs in 2025:**  
*(SR2024 outputs: Cluster-Norm for Unsupervised Probing of Knowledge)*  

---

#### <span style="font-size:1.3em">Indirect deception monitoring</span> <span style="color:#bbb">[cat:deception_indirect]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: build tools to find whether a model will misbehave in high stakes circumstances by looking at it in testable circumstances. This bucket catches work on lie classifiers, sycophancy, Scaling Trends For Deception)*  
**Theory of change:** *(SR2024: maybe we can catch a misaligned model by observing dozens of superficially unrelated parts, or tricking it into self-reporting, or by building the equivalent of brain scans)*  
**See also:**  
**Orthodox problems:** *(SR2024: 7. Superintelligence can fool human supervisors)*  
**Target case:** *(SR2024: pessimistic)*  
**Broad approach:** *(SR2024: engineering)*  
**Key people:** *(SR2024: Anthropic, Monte MacDiarmid, Meg Tong, Mrinank Sharma, Owain Evans, Colognese)*  
**Estimated FTEs:** *(SR2024: 1-10)*  
**Critiques:** *(SR2024: 1%, contra counting arguments)*  
**Funded by:** *(SR2024: Anthropic funders)*  
**Funding in 2025:** *(SR2024 funding 2023-4: N/A)*  
**Outputs in 2025:**  
*(SR2024 outputs: Simple probes can catch sleeper agents, Sandbag Detection through Noise Injection, Hidden in Plain Text: Emergence & Mitigation of Steganographic Collusion in LLMs)*  

---

#### <span style="font-size:1.3em">Other deception prevention</span> <span style="color:#bbb">[cat:deception_other]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">Goal robustness</span> <span style="color:#bbb">[cat:goal_robustness]</span>


---

#### <span style="font-size:1.3em">Mild optimisation</span> <span style="color:#bbb">[cat:mild_optimization]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: avoid Goodharting by getting AI to satisfice rather than maximise)*  
**Theory of change:** *(SR2024: if we fail to exactly nail down the preferences for a superintelligent agent we die to Goodharting → shift from maximising to satisficing in the agent's utility function → we get a nonzero share of the lightcone as opposed to zero; also, moonshot at this being the recipe for fully aligned AI)*  
**See also:**  
**Orthodox problems:** *(SR2024: 4. Goals misgeneralize out of distribution)*  
**Target case:** *(SR2024: pessimistic)*  
**Broad approach:** *(SR2024: cognitive)*  
**Key people:** *(SR2024: Jobst Heitzig, Simon Fischer, Jessica Taylor)*  
**Estimated FTEs:** *(SR2024: ?)*  
**Critiques:** *(SR2024: Dearnaley)*  
**Funded by:** *(SR2024: ?)*  
**Funding in 2025:** *(SR2024 funding 2023-4: N/A)*  
**Outputs in 2025:**  
*(SR2024 outputs: How to safely use an optimizer, Aspiration-based designs sequence, Non-maximizing policies that fulfill multi-criterion aspirations in expectation)*  

---

#### <span style="font-size:1.3em">RL safety</span> <span style="color:#bbb">[cat:rl_safety]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Safe Learning Under Irreversible Dynamics via Asking for Help](https://arxiv.org/abs/2502.14043)**, *Benjamin Plaut, Juan Liévano-Karim, Hanlin Zhu et al.*, 2025-02-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:3e57fe40]</span>, <span style="color:#777">Summary: Presents an algorithm with formal regret guarantees that enables safe reinforcement learning in environments with irreversible dynamics by allowing agents to ask mentors for help and transfer knowledge between similar states, achieving sublinear regret and mentor queries.</span>
- **[Multiplayer Nash Preference Optimization](https://arxiv.org/abs/2509.23102)**, *Fang Wu, Xu Huang, Weihao Xuan et al.*, 2025-09-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:b5650a9b]</span>, <span style="color:#777">Summary: Extends Nash learning from human feedback (NLHF) to multiplayer settings, formulating alignment as an n-player game where policies compete against populations of opponents while being regularized toward a reference model.</span>
- **[The Invisible Leash: Why RLVR May or May Not Escape Its Origin](https://arxiv.org/abs/2507.14843)**, *Fang Wu, Weihao Xuan, Ximing Lu et al.*, 2025-07-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:a1daf13f]</span>, <span style="color:#777">Summary: Empirical investigation of RLVR (Reinforcement Learning from Verifiable Rewards) limitations, showing it operates as support-constrained optimization that improves precision but narrows exploration, failing to discover solutions outside the base model's initial distribution.</span>
- **[Reducing the Probability of Undesirable Outputs in Language Models Using Probabilistic Inference](https://arxiv.org/abs/2510.21184)**, *Stephen Zhao, Aidan Li, Rob Brekelmans et al.*, 2025-10-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:b7aebad3]</span>, <span style="color:#777">Summary: Introduces RePULSe, a new training method that augments standard RL alignment with an additional loss using learned proposals to sample and reduce the probability of low-reward outputs in language models.</span>
- **[Partial Identifiability and Misspecification in Inverse Reinforcement Learning](https://arxiv.org/abs/2411.15951)**, *Joar Skalse, Alessandro Abate*, 2024-11-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:bdf95898]</span>, <span style="color:#777">Summary: Provides comprehensive mathematical analysis of partial identifiability and misspecification in Inverse Reinforcement Learning, fully characterizing reward function ambiguity and deriving necessary/sufficient conditions for when behavioral model misspecification leads to faulty reward inferences.</span>
- **[Partial Identifiability in Inverse Reinforcement Learning For Agents With Non-Exponential Discounting](https://arxiv.org/abs/2412.11155)**, *Joar Skalse, Alessandro Abate*, 2024-12-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:10f4f415]</span>, <span style="color:#777">Summary: Extends inverse reinforcement learning theory to agents with non-exponential (hyperbolic) discounting, characterizing fundamental limits on inferring reward functions and optimal policies from observed behavior for such agents.</span>


---

#### <span style="font-size:1.3em">Multi-agent safety</span> <span style="color:#bbb">[cat:multiagent_safety]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

#### <span style="font-size:1.3em">Assistance games / reward learning</span> <span style="color:#bbb">[cat:assistance_games]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: reorient the general thrust of AI research towards provably beneficial systems)*  
**Theory of change:** *(SR2024: understand what kinds of things can go wrong when humans are directly involved in training a model → build tools that make it easier for a model to learn what humans want it to learn)*  
**See also:** *(SR2024: RLHF and recursive reward modelling, the industrialised forms)*  
**Orthodox problems:** *(SR2024: 1. Value is fragile and hard to specify, 10. Humanlike minds/goals are not necessarily safe)*  
**Target case:** *(SR2024: varies)*  
**Broad approach:** *(SR2024: engineering, cognitive)*  
**Key people:** *(SR2024: Joar Skalse, Anca Dragan, Stuart Russell, David Krueger)*  
**Estimated FTEs:** *(SR2024: 10+)*  
**Critiques:** *(SR2024: nice summary of historical problem statements)*  
**Funded by:** *(SR2024: EA funds, Open Philanthropy. Survival and Flourishing Fund, Manifund)*  
**Funding in 2025:** *(SR2024 funding 2023-4: >$1500)*  
**Outputs in 2025:**  
*(SR2024 outputs: The Perils of Optimizing Learned Reward Functions, Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking, Changing and Influenceable Reward Functions, RL, but don't do anything I wouldn't do, Interpreting Preference Models w/ Sparse Autoencoders)*  
- **[AssistanceZero: Scalably Solving Assistance Games](https://arxiv.org/abs/2504.07091)**, *Cassidy Laidlaw, Eli Bronstein, Timothy Guo et al.*, 2025-04-09, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:5b7b7b41]</span>, <span style="color:#777">Summary: Presents AssistanceZero, the first scalable algorithm for solving assistance games by extending AlphaZero with neural networks that predict human actions and rewards, enabling planning under uncertainty about shared goals.</span>
- **[Observation Interference in Partially Observable Assistance Games](https://arxiv.org/abs/2412.17797)**, *Scott Emmons, Caspar Oesterheld, Vincent Conitzer et al.*, 2024-12-23, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:8fbeb3bf]</span>, <span style="color:#777">Summary: Extends the assistance games framework to partial observability and proves that optimal AI assistants sometimes must interfere with human observations, even when this seems to contradict classical decision theory about the value of information.</span>
- **[Learning to Assist Humans without Inferring Rewards](https://arxiv.org/abs/2411.02623)**, *Vivek Myers, Evan Ellis, Sergey Levine et al.*, 2024-11-04, NeurIPS 2024, <span style="color:#777">[paper_published, sr=0.52, id:9a8b3a7a]</span>, <span style="color:#777">Summary: Proposes using contrastive successor representations to scale empowerment-based assistance (maximizing human influence over outcomes) to high-dimensional settings, providing an alternative to inverse reinforcement learning for assistive AI agents.</span>


---

## <span style="font-size:1.5em">White-box alignment</span> <span style="color:#bbb">[cat:whitebox]</span>


---

### <span style="font-size:1.4em">Interpretability</span> <span style="color:#bbb">[cat:interpretability]</span>


---

#### <span style="font-size:1.3em">Fundamental Mech interp</span> <span style="color:#bbb">[cat:interp_fundamental]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching](https://arxiv.org/abs/2508.21258)**, *Farnoush Rezaei Jafari, Oliver Eberle, Ashkan Khakzar et al.*, 2025-08-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:82e8c5bd]</span>, <span style="color:#777">Summary: Introduces Relevance Patching (RelP), a new method for circuit discovery in language models that replaces attribution patching's local gradients with Layer-wise Relevance Propagation coefficients, achieving significantly better faithfulness while maintaining computational efficiency.</span>
- **[How Do Transformers Learn Variable Binding in Symbolic Programs?](https://arxiv.org/abs/2505.20896)**, *Yiwei Wu, Atticus Geiger, Raphaël Millière*, 2025-05-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:148fbac5]</span>, <span style="color:#777">Summary: Empirically investigates how Transformers learn variable binding in symbolic programs, discovering a three-phase developmental trajectory and using causal interventions to show models exploit the residual stream as addressable memory with specialized attention heads routing information.</span>
- **[Structural Inference: Interpreting Small Language Models with Susceptibilities](https://arxiv.org/abs/2504.18274)**, *Garrett Baker, George Wang, Jesse Hoogland et al.*, 2025-04-25, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:5b6da498]</span>, <span style="color:#777">Summary: Develops a linear response framework for interpretability that treats neural networks as Bayesian statistical mechanical systems, using susceptibilities to understand how network components respond to data distribution perturbations and efficiently identify functional modules.</span>
- **[Interpretability in Parameter Space: Minimizing Mechanistic Description Length with Attribution-based Parameter Decomposition](https://arxiv.org/abs/2501.14926)**, *Dan Braun, Lucius Bushnaq, Stefan Heimersheim et al.*, 2025-01-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:8126196f]</span>, <span style="color:#777">Summary: Introduces Attribution-based Parameter Decomposition (APD), a method for decomposing neural network parameters into mechanistic components by minimizing description length. Demonstrates effectiveness on toy models by recovering ground truth mechanisms in superposition, compressed computations, and cross-layer representations.</span>
- **[LLMs Process Lists With General Filter Heads](https://arxiv.org/abs/2510.26784)**, *Arnab Sen Sharma, Giordano Rogers, Natalie Shapira et al.*, 2025-10-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:58394d29]</span>, <span style="color:#777">Summary: Uses causal mediation analysis to discover that LLMs learn compact representations of filtering operations through specialized attention heads ('filter heads') that encode general predicates portable across different collections, formats, and languages, mirroring functional programming patterns.</span>
- **[Language Models Use Trigonometry to Do Addition](https://arxiv.org/abs/2502.00873)**, *Subhash Kantamneni, Max Tegmark*, 2025-02-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:d6bfb1f0]</span>, <span style="color:#777">Summary: Reverse-engineers how three mid-sized LLMs compute addition, discovering that numbers are represented as a generalized helix structure that models manipulate using a 'Clock' algorithm, verified through causal interventions at multiple network levels.</span>
- **[Mixing Mechanisms: How Language Models Retrieve Bound Entities In-Context](https://arxiv.org/abs/2510.06182)**, *Yoav Gur-Arieh, Mor Geva, Atticus Geiger*, 2025-10-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:38b5513f]</span>, <span style="color:#777">Summary: Studies how language models bind and retrieve entities in-context, discovering that models use three distinct mechanisms (positional, lexical, and reflexive) that combine to drive retrieval behavior across nine models and ten binding tasks.</span>
- **[Transformers Struggle to Learn to Search](https://arxiv.org/abs/2412.04703)**, *Abulhair Saparov, Srushti Pawar, Shreyas Pimpalgaonkar et al.*, 2024-12-06, ICLR 2025, <span style="color:#777">[paper_preprint, sr=0.72, id:f6ec26de]</span>, <span style="color:#777">Summary: Studies whether transformers can learn search algorithms using graph connectivity as a testbed, finding they can learn search on small graphs but struggle to generalize to larger graphs even with more parameters. Uses mechanistic interpretability to extract and analyze the learned parallel search algorithm.</span>
- **[Which Attention Heads Matter for In-Context Learning?](https://arxiv.org/abs/2502.14010)**, *Kayo Yin, Jacob Steinhardt*, 2025-02-19, ICML 2025, <span style="color:#777">[paper_preprint, sr=0.70, id:a64d272b]</span>, <span style="color:#777">Summary: Empirical study of 12 language models comparing induction heads versus function vector (FV) heads in driving in-context learning, finding that FV heads are primary drivers especially in larger models, and that many FV heads evolve from induction heads during training.</span>
- **[How Do LLMs Perform Two-Hop Reasoning in Context?](https://arxiv.org/abs/2502.13913)**, *Tianyu Guo, Hanlin Zhu, Ruiqi Zhang et al.*, 2025-02-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.70, id:3eae0f3f]</span>, <span style="color:#777">Summary: Investigates how LLMs perform two-hop logical reasoning by training transformers from scratch on synthetic tasks and reverse-engineering their internal mechanisms, revealing a sharp phase transition from random guessing to structured sequential query mechanisms.</span>
- **[Superposition Yields Robust Neural Scaling](https://arxiv.org/abs/2505.10465)**, *Yizhou Liu, Ziming Liu, Jeff Gore*, 2025-05-15, NeurIPS 2025 (accepted), arXiv preprint, <span style="color:#777">[paper_preprint, sr=0.62, id:a5391785]</span>, <span style="color:#777">Summary: Proposes that representation superposition (models representing more features than dimensions) is a key driver of neural scaling laws, showing theoretically and empirically that strong superposition causes loss to scale inversely with model dimension across broad frequency distributions.</span>
- **[Disjoint Processing Mechanisms of Hierarchical and Linear Grammars in Large Language Models](https://arxiv.org/abs/2501.08618)**, *Aruna Sankaranarayanan, Dylan Hadfield-Menell, Aaron Mueller*, 2025-01-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.55, id:12530f4b]</span>, <span style="color:#777">Summary: Investigates whether LLMs develop functionally distinct regions for processing hierarchical versus linear grammars, finding through ablation experiments that models have separate components for each grammar type, with hierarchy-selective components active even on nonce words.</span>


---

#### <span style="font-size:1.3em">Concept-based interp</span> <span style="color:#bbb">[cat:interp_concept_based]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[How Do LLMs Persuade? Linear Probes Can Uncover Persuasion Dynamics in Multi-Turn Conversations](https://arxiv.org/abs/2508.05625)**, *Brandon Jaipersaud, David Krueger, Ekdeep Singh Lubana*, 2025-08-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:60c15241]</span>, <span style="color:#777">Summary: Applies linear probes to study persuasion dynamics in LLM conversations, training probes to detect persuasion success, persuadee personality, and persuasion strategies across multi-turn interactions.</span>


---

#### <span style="font-size:1.3em">Auditing real models / applied interpretability</span> <span style="color:#bbb">[cat:interp_applied]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[LLMs Encode Harmfulness and Refusal Separately](https://arxiv.org/abs/2507.11878)**, *Jiachen Zhao, Jing Huang, Zhengxuan Wu et al.*, 2025-07-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:639318ca]</span>, <span style="color:#777">Summary: Identifies that LLMs internally encode harmfulness as a separate concept from refusal through distinct neural directions, and develops Latent Guard - an intrinsic safeguard using latent harmfulness representations that matches Llama Guard 3 8B performance while being robust to finetuning attacks.</span>
- **[LatentQA: Teaching LLMs to Decode Activations Into Natural Language](https://arxiv.org/abs/2412.08686)**, *Alexander Pan, Lijie Chen, Jacob Steinhardt*, 2024-12-11, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:fdfc93f9]</span>, <span style="color:#777">Summary: Introduces LatentQA (answering questions about model activations in natural language) and Latent Interpretation Tuning (LIT), which finetunes a decoder LLM to interpret activations, demonstrating applications in extracting knowledge, controlling model behavior, and revealing harmful capabilities.</span>
- **[Thought Branches: Interpreting LLM Reasoning Requires Resampling](https://arxiv.org/abs/2510.27484)**, *Uzay Macar, Paul C. Bogdan, Senthooran Rajamanoharan et al.*, 2025-10-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:3a5e3fcc]</span>, <span style="color:#777">Summary: Introduces resampling-based methodology for studying distributions over chain-of-thought reasoning rather than single samples, enabling causal analysis of model reasoning through four case studies including alignment faking, on-policy vs off-policy interventions, reasoning step removal resilience, and unfaithful CoT analysis.</span>
- **[Narrow Finetuning Leaves Clearly Readable Traces in Activation Differences](https://arxiv.org/abs/2510.13900)**, *Julian Minder, Clément Dumas, Stewart Slocum et al.*, 2025-10-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:945228fb]</span>, <span style="color:#777">Summary: Empirical study demonstrating that narrow finetuning creates strong, interpretable biases in LLM activations that can be discovered through model diffing, with implications for emergent misalignment and safety research practices using narrowly finetuned models.</span>
- **[Base Models Know How to Reason, Thinking Models Learn When](https://arxiv.org/abs/2510.07364)**, *Constantin Venhoff, Iván Arcuschin, Philip Torr et al.*, 2025-10-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:3746f2bd]</span>, <span style="color:#777">Summary: Investigates why thinking models like DeepSeek R1 outperform base models by introducing a hybrid approach that activates reasoning mechanisms in base models at the right time, recovering up to 91% of the performance gap without weight updates.</span>
- **[Simple Mechanistic Explanations for Out-Of-Context Reasoning](https://arxiv.org/abs/2507.08218)**, *Atticus Wang, Joshua Engels, Oliver Clive-Griffin et al.*, 2025-07-10, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:d79f36fc]</span>, <span style="color:#777">Summary: Mechanistically investigates out-of-context reasoning in fine-tuned LLMs, finding that LoRA fine-tuning essentially adds constant steering vectors that cause surprising generalization, with results holding even for model backdoors.</span>
- **[Interpreting learned search: finding a transition model and value function in an RNN that plays Sokoban](https://arxiv.org/abs/2506.10138)**, *Mohammad Taufeeque, Aaron David Tucker, Adam Gleave et al.*, 2025-06-11, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:6eb32d55]</span>, <span style="color:#777">Summary: Reverse-engineers a convolutional RNN trained with model-free RL to play Sokoban, discovering learned mechanisms analogous to classical bidirectional search including state-action value functions, transition models formed by specialized kernels, and layer-wise search depth increases.</span>
- **[Thought Anchors: Which LLM Reasoning Steps Matter?](https://arxiv.org/abs/2506.19143)**, *Paul C. Bogdan, Uzay Macar, Neel Nanda et al.*, 2025-06-23, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:327fbd7d]</span>, <span style="color:#777">Summary: Introduces a black-box method for measuring counterfactual importance of individual sentences in LLM reasoning traces by sampling replacement sentences and quantifying impact on final answers. Discovers 'thought anchors' - planning and uncertainty management sentences that disproportionately influence reasoning trajectories and are consistently attended to by specialized attention heads.</span>
- **[Reasoning-Finetuning Repurposes Latent Representations in Base Models](https://arxiv.org/abs/2507.12638)**, *Jake Ward, Chuqiao Lin, Constantin Venhoff et al.*, 2025-07-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:55610cb7]</span>, <span style="color:#777">Summary: Studies how backtracking behavior emerges in reasoning-finetuned models (DeepSeek-R1-Distill-Llama-8B), finding that a direction from the base model can induce backtracking when used to steer the reasoning model, suggesting reasoning finetuning repurposes pre-existing representations rather than learning new capabilities from scratch.</span>
- **[Why and How LLMs Hallucinate: Connecting the Dots with Subsequence Associations](https://arxiv.org/abs/2504.12691)**, *Yiyou Sun, Yu Gai, Lijie Chen et al.*, 2025-04-17, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:a46e4ea3]</span>, <span style="color:#777">Summary: Introduces a subsequence association framework to systematically trace and understand LLM hallucinations, proposing that hallucinations arise when dominant hallucinatory associations outweigh faithful ones. Develops a tracing algorithm that identifies causal subsequences by analyzing hallucination probabilities across randomized contexts and validates it empirically.</span>
- **[Do Multilingual LLMs Think In English?](https://arxiv.org/abs/2502.15603)**, *Lisa Schut, Yarin Gal, Sebastian Farquhar*, 2025-02-21, arXiv, <span style="color:#777">[paper_preprint, sr=0.52, id:1ea64229]</span>, <span style="color:#777">Summary: Uses logit lens and activation steering experiments to demonstrate that multilingual LLMs perform key reasoning in representation spaces closest to English, regardless of input/output language, revealing non-transparent internal processing biases.</span>


---

#### <span style="font-size:1.3em">Sparse Coding</span> <span style="color:#bbb">[cat:interp_sparse_coding]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: decompose the polysemantic activations of the residual stream into a sparse linear combination of monosemantic "features" which correspond to interpretable concepts)*  
**Theory of change:** *(SR2024: get a principled decomposition of an LLM's activation into atomic components → identify deception and other misbehaviors)*  
**See also:** *(SR2024: Bau Lab, the Local Interaction Basis)*  
**Orthodox problems:** *(SR2024: 1. Value is fragile and hard to specify, 7. Superintelligence can fool human supervisors)*  
**Target case:** *(SR2024: pessimistic)*  
**Broad approach:** *(SR2024: cognitive)*  
**Key people:** *(SR2024: Senthooran Rajamanoharan, Arthur Conmy, Leo Gao, Neel Nanda, Connor Kissane, Lee Sharkey, Samuel Marks, David Bau, Eric Michaud, Aaron Mueller, Decode)*  
**Estimated FTEs:** *(SR2024: 10-50)*  
**Critiques:** *(SR2024: SAEs are highly dataset dependent, The 'strong' feature hypothesis could be wrong, EIS XIV: Is mechanistic interpretability about to be practically useful?, steganography, Analyzing (In)Abilities of SAEs via Formal Languages)*  
**Funded by:** *(SR2024: everyone, roughly. Frontier labs, LTFF, OpenPhil, etc.)*  
**Funding in 2025:** *(SR2024 funding 2023-4: N/A. Millions?)*  
**Outputs in 2025:**  
*(SR2024 outputs: Scaling Monosemanticity, Extracting Concepts from GPT-4, Gemma Scope, JumpReLU, Dictionary learning with gated SAEs, Scaling and evaluating sparse autoencoders, Automatically Interpreting LLM Features, Interpreting Attention Layers, SAEs (usually) Transfer Between Base and Chat Models, End-to-End Sparse Dictionary Learning, Transcoders Find Interpretable LLM Feature Circuits, A is for Absorption, Sparse Feature Circuits, Function Vectors, Improving Steering Vectors by Targeting SAE Features, Matryoshka SAEs, Goodfire)*  
- **[Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://arxiv.org/abs/2411.14257)**, *Javier Ferrando, Oscar Obeso, Senthooran Rajamanoharan et al.*, 2024-11-21, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:16d92e8b]</span>, <span style="color:#777">Summary: Uses sparse autoencoders to discover that language models have internal representations for entity recognition - detecting whether they can recall facts about an entity - which causally influences hallucination and refusal behavior.</span>
- **[Decomposing MLP Activations into Interpretable Features via Semi-Nonnegative Matrix Factorization](https://arxiv.org/abs/2506.10920)**, *Or Shafran, Atticus Geiger, Mor Geva*, 2025-06-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:ddf15a4d]</span>, <span style="color:#777">Summary: Proposes semi-nonnegative matrix factorization (SNMF) to decompose MLP activations into interpretable features as an alternative to sparse autoencoders, with experiments on Llama 3.1, Gemma 2, and GPT-2 showing superior performance on causal steering tasks.</span>
- **[Priors in Time: Missing Inductive Biases for Language Model Interpretability](https://arxiv.org/abs/2511.01836)**, *Ekdeep Singh Lubana, Can Rager, Sai Sumedh R. Hindupur et al.*, 2025-11-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:8abd45df]</span>, <span style="color:#777">Summary: Critiques Sparse Autoencoders for assuming temporal independence in language model representations and proposes Temporal Feature Analysis, a new interpretability method with temporal inductive bias that decomposes representations into predictable and novel components.</span>
- **[Inference-Time Decomposition of Activations (ITDA): A Scalable Approach to Interpreting Large Language Models](https://arxiv.org/abs/2505.17769)**, *Patrick Leask, Neel Nanda, Noura Al Moubayed*, 2025-05-23, ICML 2025, <span style="color:#777">[paper_preprint, sr=0.85, id:8a1946f1]</span>, <span style="color:#777">Summary: Introduces ITDA, a computationally efficient alternative to sparse autoencoders for decomposing LLM activations into interpretable features, requiring only 1% of SAE training time and data while enabling cross-model comparisons through greedy dictionary construction via matching pursuit.</span>
- **[Binary Sparse Coding for Interpretability](https://arxiv.org/abs/2509.25596)**, *Lucia Quirke, Stepan Shabalin, Nora Belrose*, 2025-09-29, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:5b3f3a2b]</span>, <span style="color:#777">Summary: Proposes binary sparse autoencoders (BAEs) and binary transcoders (BTCs) that constrain feature activations to 0 or 1, finding that binarization improves interpretability and monosemanticity but increases reconstruction error and ultra-high frequency features.</span>
- **[Stochastic Parameter Decomposition](https://arxiv.org/abs/2506.20790)**, *Lucius Bushnaq, Dan Braun, Lee Sharkey*, 2025-06-25, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:3189ec88]</span>, <span style="color:#777">Summary: Introduces Stochastic Parameter Decomposition (SPD), a method for decomposing neural network parameters into sparsely used vectors that is more scalable and robust than existing Attribution-based Parameter Decomposition (APD), with demonstrations on larger models and released implementation library.</span>
- **[Dense SAE Latents Are Features, Not Bugs](https://arxiv.org/abs/2506.15679)**, *Xiaoqing Sun, Alessandro Stolfo, Joshua Engels et al.*, 2025-06-18, arXiv (NeurIPS 2025), <span style="color:#777">[paper_preprint, sr=0.82, id:3eb1ba44]</span>, <span style="color:#777">Summary: Systematically investigates dense (frequently-activating) latents in sparse autoencoders, demonstrating they are meaningful features rather than training artifacts, and introduces a taxonomy of dense latent types including position tracking, context binding, and entropy regulation.</span>
- **[Evaluating Sparse Autoencoders on Targeted Concept Erasure Tasks](https://arxiv.org/abs/2411.18895)**, *Adam Karvonen, Can Rager, Samuel Marks et al.*, 2024-11-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:14e7708e]</span>, <span style="color:#777">Summary: Introduces automated evaluation metrics for Sparse Autoencoders (SAEs) based on concept erasure tasks, including LLM-automated SHIFT and the new Targeted Probe Perturbation (TPP) metric that quantifies SAE ability to disentangle similar concepts.</span>
- **[Evaluating SAE interpretability without explanations](https://arxiv.org/abs/2507.08473)**, *Gonçalo Paulo, Nora Belrose*, 2025-07-11, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:c897b669]</span>, <span style="color:#777">Summary: Develops methods to evaluate sparse autoencoder (SAE) interpretability without requiring natural language explanations as an intermediate step, comparing automated metrics with human evaluations to provide more direct assessment of discovered latents.</span>
- **[SAEs Are Good for Steering -- If You Select the Right Features](https://arxiv.org/abs/2505.20063)**, *Dana Arad, Aaron Mueller, Yonatan Belinkov*, 2025-05-26, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:52d3316f]</span>, <span style="color:#777">Summary: Distinguishes between input features (capture patterns in model input) and output features (affect model output) in Sparse Autoencoders, and proposes scoring methods to identify them. Shows that filtering out low-output-score features yields 2-3x improvements in SAE-based steering, making it competitive with supervised methods.</span>
- **[Line of Sight: On Linear Representations in VLLMs](https://arxiv.org/abs/2506.04706)**, *Achyuta Rajaram, Sarah Schwettmann, Jacob Andreas et al.*, 2025-06-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:56f7b629]</span>, <span style="color:#777">Summary: Investigates how vision-language models (specifically LlaVA-Next) represent visual concepts internally by finding linearly decodable ImageNet features and training multimodal Sparse Autoencoders to create interpretable dictionaries of text and image features.</span>
- **[Decoding Dark Matter: Specialized Sparse Autoencoders for Interpreting Rare Concepts in Foundation Models](https://arxiv.org/abs/2411.00743)**, *Aashiq Muhamed, Mona Diab, Virginia Smith*, 2024-11-01, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:4c1a3600]</span>, <span style="color:#777">Summary: Introduces Specialized Sparse Autoencoders (SSAEs) designed to capture rare but important concepts in foundation models that standard SAEs miss, using dense retrieval for data selection and Tilted Empirical Risk Minimization for training.</span>
- **[Enhancing Neural Network Interpretability with Feature-Aligned Sparse Autoencoders](https://arxiv.org/abs/2411.01220)**, *Luke Marks, Alasdair Paren, David Krueger et al.*, 2024-11-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:438af571]</span>, <span style="color:#777">Summary: Proposes Mutual Feature Regularization (MFR), a regularization technique that improves Sparse Autoencoder training by encouraging parallel SAEs to learn similar features, thereby learning features more aligned with actual input features rather than spurious patterns.</span>
- **[BatchTopK Sparse Autoencoders](https://arxiv.org/abs/2412.06410)**, *Bart Bussmann, Patrick Leask, Neel Nanda*, 2024-12-09, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:a9e74606]</span>, <span style="color:#777">Summary: Introduces BatchTopK SAEs, a training method that improves upon TopK sparse autoencoders by relaxing the top-k constraint to batch-level, allowing variable numbers of active latents per sample and improving reconstruction without sacrificing sparsity.</span>
- **[Understanding sparse autoencoder scaling in the presence of feature manifolds](https://arxiv.org/abs/2509.02565)**, *Eric J. Michaud, Liv Gorton, Tom McGrath*, 2025-09-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:d40880ce]</span>, <span style="color:#777">Summary: Adapts capacity-allocation models from neural scaling literature to understand how sparse autoencoders (SAEs) scale with number of latents, particularly studying how multi-dimensional feature manifolds create pathological regimes where SAEs learn far fewer features than expected.</span>
- **[Internal states before wait modulate reasoning patterns](https://arxiv.org/abs/2510.04128)**, *Dmitrii Troitskii, Koyena Pal, Chris Wendler et al.*, 2025-10-05, arXiv (EMNLP Findings 2025), <span style="color:#777">[paper_preprint, sr=0.75, id:3cf71cd4]</span>, <span style="color:#777">Summary: Trains crosscoders on DeepSeek-R1-Distill-Llama-8B and introduces a latent attribution technique to identify internal features that modulate reasoning behaviors like backtracking, with causal interventions demonstrating these features influence patterns such as restarting, recalling knowledge, expressing uncertainty, and double-checking.</span>
- **[Position: Mechanistic Interpretability Should Prioritize Feature Consistency in SAEs](https://arxiv.org/abs/2505.20254)**, *Xiangchen Song, Aashiq Muhamed, Yujia Zheng et al.*, 2025-05-26, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:b53d8f15]</span>, <span style="color:#777">Summary: Proposes prioritizing feature consistency in Sparse Autoencoders (SAEs) for mechanistic interpretability, introducing the Pairwise Dictionary Mean Correlation Coefficient (PW-MCC) metric and demonstrating that TopK SAEs achieve high consistency (0.80) through theoretical validation with model organisms and empirical validation on LLM activations.</span>
- **[How Visual Representations Map to Language Feature Space in Multimodal LLMs](https://arxiv.org/abs/2506.11976)**, *Constantin Venhoff, Ashkan Khakzar, Sonia Joseph et al.*, 2025-06-13, arXiv, <span style="color:#777">[paper_preprint, sr=0.70, id:fb98edde]</span>, <span style="color:#777">Summary: Uses pre-trained sparse autoencoders (SAEs) to analyze how visual representations from a frozen ViT align with language feature representations in a frozen LLM through a linear adapter in vision-language models.</span>
- **[Prisma: An Open Source Toolkit for Mechanistic Interpretability in Vision and Video](https://arxiv.org/abs/2504.19475)**, *Sonia Joseph, Praneet Suresh, Lorenz Hufe et al.*, 2025-04-28, arXiv / CVPR Mechanistic Interpretability for Vision Workshop, <span style="color:#777">[paper_preprint, sr=0.68, id:7f5c917a]</span>, <span style="color:#777">Summary: Presents Prisma, an open-source framework for vision mechanistic interpretability providing unified access to 75+ vision transformers, SAE/transcoder/crosscoder training support, 80+ pre-trained SAE weights, circuit analysis tools, and visualization capabilities.</span>
- **[Interpreting Large Text-to-Image Diffusion Models with Dictionary Learning](https://arxiv.org/abs/2505.24360)**, *Stepan Shabalin, Ayush Panda, Dmitrii Kharlapenko et al.*, 2025-05-30, CVPR 2025 - Mechanistic Interpretability for Vision Workshop, <span style="color:#777">[paper_preprint, sr=0.50, id:c9edf919]</span>, <span style="color:#777">Summary: Applies Sparse Autoencoders (SAEs) and Inference-Time Decomposition of Activations (ITDA) to Flux 1, a large text-to-image diffusion model, introducing a visual automated interpretation pipeline and demonstrating that SAE features can steer image generation.</span>


---

#### <span style="font-size:1.3em">Pr(Ai)2R: Causal Abstractions</span> <span style="color:#bbb">[cat:interp_causal_abstractions]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: develop the foundations of interpretable AI through the lens of causality and abstraction)*  
**Theory of change:** *(SR2024: figure out what it means for a mechanistic explanation of neural network behavior to be correct → find a mechanistic explanation of neural network behavior)*  
**See also:** *(SR2024: causal scrubbing, locally consistent abstractions)*  
**Orthodox problems:** *(SR2024: 1. Value is fragile and hard to specify, 7. Superintelligence can fool human supervisors)*  
**Target case:** *(SR2024: pessimistic)*  
**Broad approach:** *(SR2024: cognitive)*  
**Key people:** *(SR2024: Atticus Geiger)*  
**Estimated FTEs:** *(SR2024: 1-10)*  
**Critiques:** *(SR2024: not found)*  
**Funded by:** *(SR2024: Open Philanthropy)*  
**Funding in 2025:** *(SR2024 funding 2023-4: $737,000)*  
**Outputs in 2025:**  
*(SR2024 outputs: Disentangling Factual Knowledge in GPT-2 Small, Causal Abstraction, ReFT, pyvene, defending subspace interchange)*  
- **[HyperDAS: Towards Automating Mechanistic Interpretability with Hypernetworks](https://arxiv.org/abs/2503.10894)**, *Jiuding Sun, Jing Huang, Sidharth Baskaran et al.*, 2025-03-13, ICLR 2025, <span style="color:#777">[paper_preprint, sr=0.85, id:d8df2721]</span>, <span style="color:#777">Summary: Introduces HyperDAS, a transformer-based hypernetwork that automates distributed alignment search by automatically locating token positions where concepts are realized in residual streams and constructing features for those concepts, achieving state-of-the-art on RAVEL benchmark for disentangling concepts in Llama3-8B hidden states.</span>
- **[How Causal Abstraction Underpins Computational Explanation](https://arxiv.org/abs/2508.11214)**, *Atticus Geiger, Jacqueline Harding, Thomas Icard*, 2025-08-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.62, id:2fe16dfd]</span>, <span style="color:#777">Summary: Theoretical paper arguing that causal abstraction theory provides a fruitful framework for understanding computational implementation in neural networks, connecting classical philosophy of computation with contemporary machine learning and examining the role of representation in generalization and prediction.</span>


---

#### <span style="font-size:1.3em">EleutherAI interp</span> <span style="color:#bbb">[cat:interp_eleuther]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: tools to investigate questions like path dependence of training)*  
**Theory of change:** *(SR2024: make amazing tools to push forward the frontier of interpretability)*  
**See also:**  
**Orthodox problems:** *(SR2024: 1. Value is fragile and hard to specify)*  
**Target case:** *(SR2024: optimistic-case)*  
**Broad approach:** *(SR2024: cognitive)*  
**Key people:** *(SR2024: Nora Belrose, Brennan Dury, David Johnston, Alex Mallen, Lucia Quirke, Adam Scherlis)*  
**Estimated FTEs:** *(SR2024: 6)*  
**Critiques:** *(SR2024: not found)*  
**Funded by:** *(SR2024: CoreWeave, Hugging Face, Open Philanthropy, Mozilla, Omidyar Network, Stability AI, Lambda Labs)*  
**Funding in 2025:** *(SR2024 funding 2023-4: $2,642,273)*  
**Outputs in 2025:**  
*(SR2024 outputs: Neural Networks Learn Statistics of Increasing Complexity, Automatically Interpreting Millions of Features in Large Language Models, Refusal in LLMs is an Affine Function)*  
- **[Refusal in LLMs is an Affine Function](https://arxiv.org/abs/2411.09003)**, *Thomas Marshall, Adam Scherlis, Nora Belrose*, 2024-11-13, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:9a761fe1]</span>, <span style="color:#777">Summary: Proposes affine concept editing (ACE) as a method for steering language model behavior by intervening in activations, demonstrating precise control over refusal behavior across ten models including Llama 3 70B through combining affine subspace projection and activation addition.</span>


---

#### <span style="font-size:1.3em">Other interpretability</span> <span style="color:#bbb">[cat:interp_other]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Because we have LLMs, we Can and Should Pursue Agentic Interpretability](https://arxiv.org/abs/2506.12152)**, *Been Kim, John Hewitt, Neel Nanda et al.*, 2025-06-13, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:2b0b4ca7]</span>, <span style="color:#777">Summary: Proposes agentic interpretability as a new paradigm where LLMs proactively assist human understanding through multi-turn conversations by developing mental models of users, enabling humans to better understand potentially superhuman AI concepts.</span>
- **[The Loss Kernel: A Geometric Probe for Deep Learning Interpretability](https://arxiv.org/abs/2509.26537)**, *Maxwell Adam, Zach Furman, Jesse Hoogland*, 2025-09-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.55, id:547cdca6]</span>, <span style="color:#777">Summary: Introduces the loss kernel, an interpretability method that measures similarity between data points via the covariance of per-sample losses under parameter perturbations, validated on synthetic multitask problems and applied to Inception-v1 on ImageNet.</span>
- **[Through a Steerable Lens: Magnifying Neural Network Interpretability via Phase-Based Extrapolation](https://arxiv.org/abs/2506.02300)**, *Farzaneh Mahdisoltani, Saeed Mahdisoltani, Roger B. Grosse et al.*, 2025-06-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.55, id:1b1f65af]</span>, <span style="color:#777">Summary: Proposes a novel interpretability framework that visualizes classifier decision boundaries by amplifying class-conditional gradients in Complex Steerable Pyramid space, producing semantically meaningful morphs that reveal how models distinguish between classes.</span>


---

### <span style="font-size:1.4em">Whitebox monitoring</span> <span style="color:#bbb">[cat:whitebox_monitoring]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Detecting High-Stakes Interactions with Activation Probes](https://arxiv.org/abs/2506.10805)**, *Alex McKenzie, Urja Pawar, Phil Blandfort et al.*, 2025-06-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:e2b3e98a]</span>, <span style="color:#777">Summary: Develops and evaluates activation probe architectures for detecting high-stakes LLM interactions that might lead to significant harm, demonstrating robust generalization from synthetic training data to real-world data with six orders-of-magnitude computational savings over LLM-based monitors.</span>
- **[Towards Safeguarding LLM Fine-tuning APIs against Cipher Attacks](https://arxiv.org/abs/2508.17158)**, *Jack Youstra, Mohammed Mahfoud, Yang Yan et al.*, 2025-08-23, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:32263cd8]</span>, <span style="color:#777">Summary: Introduces CIFR benchmark for evaluating defenses against cipher-encoded attacks on LLM fine-tuning APIs, and demonstrates that probe monitors trained on model internal activations achieve over 99% detection accuracy while generalizing to unseen cipher variants.</span>
- **[What Features in Prompts Jailbreak LLMs? Investigating the Mechanisms Behind Attacks](https://arxiv.org/abs/2411.03343)**, *Nathalie Kirch, Constantin Weisser, Severin Field et al.*, 2024-11-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:6006cf22]</span>, <span style="color:#777">Summary: Investigates internal mechanisms behind jailbreak attacks by training linear and non-linear probes on LLM hidden states to predict jailbreak success, then using probe-guided interventions to establish causal relevance, revealing that different jailbreak families operate through distinct non-linear mechanisms rather than a universal direction.</span>
- **[LLM Microscope: What Model Internals Reveal About Answer Correctness and Context Utilization](https://arxiv.org/abs/2510.04013)**, *Jiarui Liu, Jivitesh Jain, Mona Diab et al.*, 2025-10-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:3ef20518]</span>, <span style="color:#777">Summary: Trains classifiers on intermediate layer activations to predict output correctness (75% accuracy) and introduces model-internals-based metrics to distinguish between correct, incorrect, and irrelevant context, outperforming prompting baselines for detecting polluted context.</span>
- **[Detecting LLM Hallucination Through Layer-wise Information Deficiency: Analysis of Ambiguous Prompts and Unanswerable Questions](https://arxiv.org/abs/2412.10246)**, *Hazel Kim, Tom A. Lamb, Adel Bibi et al.*, 2024-12-13, EMNLP 2025 (arXiv preprint), <span style="color:#777">[paper_preprint, sr=0.75, id:988b1d9b]</span>, <span style="color:#777">Summary: Presents a test-time approach for detecting LLM hallucination by analyzing information flow across model layers, demonstrating that hallucination manifests as information deficiencies in inter-layer transmissions when processing ambiguous or insufficient context.</span>
- **[Real-Time Detection of Hallucinated Entities in Long-Form Generation](https://arxiv.org/abs/2509.03531)**, *Oscar Obeso, Andy Arditi, Javier Ferrando et al.*, 2025-08-26, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:b12fd2d2]</span>, <span style="color:#777">Summary: Develops a scalable method for real-time detection of hallucinated entities in long-form LLM generations using web-search-based annotation to train linear probes on internal activations, achieving better performance than semantic entropy baselines.</span>
- **[Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification](https://arxiv.org/abs/2504.05419)**, *Anqi Zhang, Yulin Chen, Jane Pan et al.*, 2025-04-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:ed58a836]</span>, <span style="color:#777">Summary: Studies whether reasoning models encode information about answer correctness in their hidden states through probing experiments, finding that trained probes can verify intermediate answers with high accuracy and predict correctness before answers are fully formulated.</span>


---

### <span style="font-size:1.4em">Chain of thought monitoring</span> <span style="color:#bbb">[cat:cot_monitoring]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926)**, *Bowen Baker, Joost Huizinga, Leo Gao et al.*, 2025-03-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.93, id:a50801b7]</span>, <span style="color:#777">Summary: Tests chain-of-thought monitoring for detecting reward hacking in frontier reasoning models (o3-mini), finding that while CoT monitoring is effective, strong optimization pressure causes agents to learn obfuscated reward hacking where they hide their intent within the CoT while still misbehaving.</span>
- **[When Chain of Thought is Necessary, Language Models Struggle to Evade Monitors](https://arxiv.org/abs/2507.05246)**, *Scott Emmons, Erik Jenner, David K. Elson et al.*, 2025-07-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:698353b6]</span>, <span style="color:#777">Summary: Introduces a conceptual framework distinguishing CoT-as-rationalization from CoT-as-computation, then empirically tests whether language models can evade chain-of-thought monitoring when complex reasoning is necessary for harmful behavior.</span>
- **[Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410)**, *Yanda Chen, Joe Benton, Ansh Radhakrishnan et al.*, 2025-05-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:21ef8c82]</span>, <span style="color:#777">Summary: Evaluates chain-of-thought faithfulness in state-of-the-art reasoning models by testing whether they verbalize reasoning hints they actually use, finding that CoTs reveal hint usage in at least 1% but often below 20% of cases where hints are used.</span>
- **[Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort](https://arxiv.org/abs/2510.01367)**, *Xinpeng Wang, Nitish Joshi, Barbara Plank et al.*, 2025-10-01, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:e5c1d19d]</span>, <span style="color:#777">Summary: Proposes TRACE (Truncated Reasoning AUC Evaluation), a method to detect implicit reward hacking by measuring how early in a model's chain-of-thought reasoning it achieves high expected reward, with the insight that models taking shortcuts require less reasoning effort than those genuinely solving tasks.</span>
- **[Teaching Models to Verbalize Reward Hacking in Chain-of-Thought Reasoning](https://arxiv.org/abs/2506.22777)**, *Miles Turpin, Andy Arditi, Marvin Li et al.*, 2025-06-28, ICML 2025 Workshop on Reliable and Responsible Foundation Models, <span style="color:#777">[paper_preprint, sr=0.88, id:755f0144]</span>, <span style="color:#777">Summary: Proposes verbalization fine-tuning (VFT), a pre-RL intervention that trains models to explicitly acknowledge when influenced by prompt cues pointing to incorrect answers, then evaluates whether this helps detect reward hacking after RL training in environments that incentivize exploiting these cues.</span>
- **[A Pragmatic Way to Measure Chain-of-Thought Monitorability](https://arxiv.org/abs/2510.23966)**, *Scott Emmons, Roland S. Zimmermann, David K. Elson et al.*, 2025-10-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:a7db7dae]</span>, <span style="color:#777">Summary: Proposes metrics to measure two components of Chain-of-Thought monitorability (legibility and coverage) using an LLM-based autorater, validates the approach with synthetic degradations, and applies it to frontier models on challenging benchmarks.</span>


---

### <span style="font-size:1.4em">Data attribution</span> <span style="color:#bbb">[cat:data_attribution]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Influence Dynamics and Stagewise Data Attribution](https://arxiv.org/abs/2510.12071)**, *Jin Hwa Lee, Matthew Smith, Maxwell Adam et al.*, 2025-10-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:aa5c8762]</span>, <span style="color:#777">Summary: Introduces a framework for stagewise data attribution grounded in singular learning theory, showing that influence between training samples changes non-monotonically during training with sign flips and peaks at developmental transitions, validated in toy models and language models.</span>
- **[Better Training Data Attribution via Better Inverse Hessian-Vector Products](https://arxiv.org/abs/2507.14740)**, *Andrew Wang, Elisa Nguyen, Runshi Yang et al.*, 2025-07-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.70, id:368a1ea3]</span>, <span style="color:#777">Summary: Introduces ASTRA, an algorithm that uses EKFAC-preconditioner on Neumann series iterations to improve inverse Hessian-vector product approximations for training data attribution, demonstrating that more accurate iHVP approximations significantly improve TDA performance.</span>
- **[Bayesian Influence Functions for Hessian-Free Data Attribution](https://arxiv.org/abs/2509.26544)**, *Philipp Alexander Kreer, Wilson Wu, Maxwell Adam et al.*, 2025-09-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:327253d4]</span>, <span style="color:#777">Summary: Proposes Bayesian influence functions (BIF) that replace Hessian inversion with loss landscape statistics estimated via stochastic-gradient MCMC sampling, enabling scalable data attribution for neural networks with billions of parameters.</span>
- **[OLMoTrace: Tracing Language Model Outputs Back to Trillions of Training Tokens](https://arxiv.org/abs/2504.07096)**, *Jiacheng Liu, Taylor Blanton, Yanai Elazar et al.*, 2025-04-09, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:861e0094]</span>, <span style="color:#777">Summary: Presents OLMoTrace, the first system for real-time tracing of language model outputs back to their multi-trillion-token training data by finding verbatim matches between output segments and training corpus documents.</span>
- **[Information-Guided Identification of Training Data Imprint in (Proprietary) Large Language Models](https://arxiv.org/abs/2503.12072)**, *Abhilasha Ravichander, Jillian Fisher, Taylor Sorensen et al.*, 2025-03-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.62, id:2a71e836]</span>, <span style="color:#777">Summary: Presents a novel method for identifying training data memorized by proprietary LLMs like GPT-4 using information-guided probes that leverage high-surprisal tokens to detect memorization, without requiring access to model weights or token probabilities.</span>
- **[Distributional Training Data Attribution: What do Influence Functions Sample?](https://arxiv.org/abs/2506.12965)**, *Bruno Mlodozeniec, Isaac Reid, Sam Power et al.*, 2025-06-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:2ca7bb60]</span>, <span style="color:#777">Summary: Introduces distributional training data attribution (d-TDA) to account for stochasticity in training, showing that influence functions emerge from this framework as the limit of unrolled differentiation without requiring convexity assumptions.</span>


---

### <span style="font-size:1.4em">Understand learning</span> <span style="color:#bbb">[cat:understand_learning]</span>


---

#### <span style="font-size:1.3em">Timaeus: Dev interp</span> <span style="color:#bbb">[cat:learning_dev_interp]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: Build tools for detecting, locating, and interpreting key moments (saddle-to-saddle dynamics, groks) that govern training and in-context learning in models)*  
**Theory of change:** *(SR2024: structures forming in neural networks can leave traces we can interpret to figure out where and how that structure is implemented. This could automate interpretability. It may be hopeless to intervene at the end of the learning process, so we want to catch and prevent deceptiveness and other dangerous capabilities and values as early as possible)*  
**See also:** *(SR2024: singular learning theory, computational mechanics, complexity)*  
**Orthodox problems:** *(SR2024: 4. Goals misgeneralize out of distribution)*  
**Target case:** *(SR2024: pessimistic)*  
**Broad approach:** *(SR2024: cognitive)*  
**Key people:** *(SR2024: Jesse Hoogland, George Wang, Daniel Murfet, Stan van Wingerden, Alexander Gietelink Oldenziel)*  
**Estimated FTEs:** *(SR2024: 10+?)*  
**Critiques:** *(SR2024: Timaeus, Erdil, Skalse)*  
**Funded by:** *(SR2024: Manifund, Survival and Flourishing Fund, EA Funds)*  
**Funding in 2025:** *(SR2024 funding 2023-4: $700,050)*  
**Outputs in 2025:**  
*(SR2024 outputs: Stagewise Development in Neural Networks, Differentiation and Specialization of Attention Heads via the Refined Local Learning Coefficient, Higher-order degeneracy and error-correction, Feature Targeted LLC Estimation Distinguishes SAE Features from Random Directions)*  
- **[Embryology of a Language Model](https://arxiv.org/abs/2508.00331)**, *George Wang, Garrett Baker, Andrew Gordon et al.*, 2025-08-01, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:fe637f32]</span>, <span style="color:#777">Summary: Introduces an embryological approach using UMAP applied to susceptibility matrices to visualize how language models develop their internal computational structure during training, revealing both known features like induction circuits and discovering novel structures like a 'spacing fin' for counting space tokens.</span>
- **[Crosscoding Through Time: Tracking Emergence & Consolidation Of Linguistic Representations Throughout LLM Pretraining](https://arxiv.org/abs/2509.05291)**, *Deniz Bayazit, Aaron Mueller, Antoine Bosselut*, 2025-09-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.70, id:763e21a3]</span>, <span style="color:#777">Summary: Uses sparse crosscoders to track how linguistic features emerge, maintain, and discontinue during LLM pretraining by aligning features across model checkpoints, introducing the Relative Indirect Effects (RelIE) metric to measure when features become causally important for task performance.</span>
- **[Dynamics of Transient Structure in In-Context Linear Regression Transformers](https://arxiv.org/abs/2501.17745)**, *Liam Carroll, Jesse Hoogland, Matthew Farrugia-Roberts et al.*, 2025-01-29, arXiv, <span style="color:#777">[paper_preprint, sr=0.62, id:d3d75194]</span>, <span style="color:#777">Summary: Empirical study of transformers trained on in-context linear regression tasks, discovering a 'transient ridge phenomenon' where models initially behave like ridge regression before specializing, and explaining this through Bayesian internal model selection theory validated via local learning coefficient measurements.</span>
- **[Emergence of Superposition: Unveiling the Training Dynamics of Chain of Continuous Thought](https://arxiv.org/abs/2509.23365)**, *Hanlin Zhu, Shibo Hao, Zhiting Hu et al.*, 2025-09-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:d65949bb]</span>, <span style="color:#777">Summary: Theoretically analyzes training dynamics of transformers with continuous chain-of-thought on graph reachability problems, revealing how superposition of multiple reasoning traces emerges naturally through bounded index-matching logits that balance exploration and exploitation.</span>
- **[What Do Learning Dynamics Reveal About Generalization in LLM Reasoning?](https://arxiv.org/abs/2411.07681)**, *Katie Kang, Amrith Setlur, Dibya Ghosh et al.*, 2024-11-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.58, id:364665fc]</span>, <span style="color:#777">Summary: Introduces pre-memorization train accuracy metric to characterize LLM generalization by distinguishing when models generalize versus memorize reasoning steps during finetuning, showing this metric reliably predicts test accuracy (R² > 0.9) and enables 1.5-2x data efficiency improvements through targeted data curation.</span>
- **[Examining Two Hop Reasoning Through Information Content Scaling](https://arxiv.org/abs/2502.03490)**, *David Johnston, Nora Belrose*, 2025-02-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.48, id:2dc96fcd]</span>, <span style="color:#777">Summary: Empirically studies how transformers learn two-hop reasoning tasks by examining capacity scaling patterns, finding that latent multi-hop QA requires learning each fact twice while chain-of-thought does not.</span>


---

#### <span style="font-size:1.3em">Simplex: Computational mechanics</span> <span style="color:#bbb">[cat:learning_comp_mechanics]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: Computational mechanics for interpretability; what structures must a system track in order to predict the future?)*  
**Theory of change:** *(SR2024: apply the theory to SOTA AI, improve structure measures and unsupervised methods for discovering structure, ultimately operationalize safety-relevant phenomena)*  
**See also:** *(SR2024: Belief State Geometry)*  
**Orthodox problems:** *(SR2024: 9. Humans cannot be first-class parties to a superintelligent value handshake)*  
**Target case:** *(SR2024: pessimistic)*  
**Broad approach:** *(SR2024: cognitive, maths/philosophy)*  
**Key people:** *(SR2024: Paul Riechers, Adam Shai)*  
**Estimated FTEs:** *(SR2024: 1-10)*  
**Critiques:** *(SR2024: not found)*  
**Funded by:** *(SR2024: Survival and Flourishing Fund)*  
**Funding in 2025:** *(SR2024 funding 2023-4: $74,000)*  
**Outputs in 2025:**  
*(SR2024 outputs: Transformers represent belief state geometry in their residual stream, Open Problems in Comp Mech)*  

---

#### <span style="font-size:1.3em">Saxe lab</span> <span style="color:#bbb">[cat:learning_saxe]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: toy models (e.g. of induction heads) to understand learning in interesting limiting examples; only part of their work is safety related)*  
**Theory of change:** *(SR2024: study interpretability and learning in DL (for bio insights, unrelated to AI) → someone else uses this work to do something safety related)*  
**See also:**  
**Orthodox problems:** *(SR2024: We don't know how to determine an AGI's goals or values)*  
**Target case:** *(SR2024: optimistic?)*  
**Broad approach:** *(SR2024: cognitive)*  
**Key people:** *(SR2024: Andrew Saxe, Basile Confavreux, Erin Grant, Stefano Sarao Mannelli, Tyler Boyd-Meredith, Victor Pedrosa)*  
**Estimated FTEs:** *(SR2024: 10-50)*  
**Critiques:** *(SR2024: none found)*  
**Funded by:** *(SR2024: Sir Henry Dale Fellowship, Wellcome-Beit Prize, CIFAR, Schmidt Science Polymath Program)*  
**Funding in 2025:** *(SR2024 funding 2023-4: >£25,000)*  
**Outputs in 2025:**  
*(SR2024 outputs: Tilting the Odds at the Lottery, What needs to go right for an induction head?, Why Do Animals Need Shaping?, When Representations Align, Understanding Unimodal Bias in Multimodal Deep Linear Networks, Meta-Learning Strategies through Value Maximization in Neural Networks)*  
- **[Training Dynamics of In-Context Learning in Linear Attention](https://arxiv.org/abs/2501.16265)**, *Yedi Zhang, Aaditya K. Singh, Peter E. Latham et al.*, 2025-01-27, arXiv (ICML 2025 Spotlight), <span style="color:#777">[paper_preprint, sr=0.60, id:ff41feaa]</span>, <span style="color:#777">Summary: Provides mathematical analysis of how multi-head linear self-attention acquires in-context learning abilities through gradient descent, characterizing training dynamics for different parametrizations and deriving analytical solutions.</span>


---

## <span style="font-size:1.5em">Safety by design</span> <span style="color:#bbb">[cat:new_safety_by_design]</span>


---

### <span style="font-size:1.4em">Guaranteed Safe AI / Formal verification</span> <span style="color:#bbb">[cat:formal_verification]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: formally model the behavior of cyber-physical systems, define precise constraints on what actions can occur, and require AIs to provide safety proofs for their recommended actions (correctness and uniqueness))*  
**Theory of change:** *(SR2024: make a formal verification system that can act as an intermediary between a human user and a potentially dangerous system and only let provably safe actions through. Notable for not requiring that we solve ELK. Does require that we solve ontology though)*  
**See also:** *(SR2024: Bengio's AI Scientist, Safeguarded AI, Open Agency Architecture, SLES, Atlas Computing, program synthesis, Tenenbaum)*  
**Orthodox problems:** *(SR2024: 1. Value is fragile and hard to specify, 4. Goals misgeneralize out of distribution, 7. Superintelligence can fool human supervisors, 9. Humans cannot be first-class parties to a superintelligent value handshake, 12. A boxed AGI might exfiltrate itself by steganography, spearphishing)*  
**Target case:** *(SR2024: (nearly) worst-case)*  
**Broad approach:** *(SR2024: cognitive)*  
**Key people:** *(SR2024: Yoshua Bengio, Max Tegmark, Steve Omohundro, David "davidad" Dalrymple, Joar Skalse, Stuart Russell, Ohad Kammar, Alessandro Abate, Fabio Zanassi)*  
**Estimated FTEs:** *(SR2024: 10-50)*  
**Critiques:** *(SR2024: Zvi, Gleave, Dickson)*  
**Funded by:** *(SR2024: UK government, OpenPhil, Survival and Flourishing Fund, Mila / CIFAR)*  
**Funding in 2025:** *(SR2024 funding 2023-4: >$10m)*  
**Outputs in 2025:**  
*(SR2024 outputs: Bayesian oracle, Towards Guaranteed Safe AI, ARIA Safeguarded AI Programme Thesis)*  

---

### <span style="font-size:1.4em">Tegmark</span> <span style="color:#bbb">[cat:tegmark]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">Scientist AI</span> <span style="color:#bbb">[cat:scientist_ai]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Superintelligent Agents Pose Catastrophic Risks: Can Scientist AI Offer a Safer Path?](https://arxiv.org/abs/2502.15657)**, *Yoshua Bengio, Michael Cohen, Damiano Fornasiere et al.*, 2025-02-21, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:f5f38357]</span>, <span style="color:#777">Summary: Argues that current trajectory toward agentic AI poses catastrophic risks including deception and loss of control, and proposes Scientist AI as a safer alternative - a non-agentic system designed to explain the world rather than take actions, comprising a world model and question-answering system with explicit uncertainty quantification.</span>
- **[The More You Automate, the Less You See: Hidden Pitfalls of AI Scientist Systems](https://arxiv.org/abs/2509.08713)**, *Ziming Luo, Atoosa Kasirzadeh, Nihar B. Shah*, 2025-09-10, arXiv, <span style="color:#777">[paper_preprint, sr=0.62, id:f1dfb295]</span>, <span style="color:#777">Summary: Identifies and empirically tests four failure modes in AI scientist systems (inappropriate benchmark selection, data leakage, metric misuse, post-hoc selection bias) through controlled experiments on two open-source systems, demonstrating that trace logs enable better failure detection than examining final papers alone.</span>


---

### <span style="font-size:1.4em">Other formal verification</span> <span style="color:#bbb">[cat:other_formal_verification]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">Other world models</span> <span style="color:#bbb">[cat:other_world_models]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">Conjecture: Cognitive Software</span> <span style="color:#bbb">[cat:conjecture]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: make tools to write, execute and deploy cognitive programs; compose these into large, powerful systems that do what we want; make a training procedure that lets us understand what the model does and does not know at each step)*  
**Theory of change:** *(SR2024: train a bounded tool AI to promote AI benefits without needing unbounded AIs. If the AI uses similar heuristics to us, it should default to not being extreme)*  
**See also:** *(SR2024: AI chains)*  
**Orthodox problems:** *(SR2024: 2. Corrigibility is anti-natural, 5. Instrumental convergence)*  
**Target case:** *(SR2024: pessimistic)*  
**Broad approach:** *(SR2024: engineering, cognitive)*  
**Key people:** *(SR2024: Connor Leahy, Gabriel Alfour, Adam Shimi)*  
**Estimated FTEs:** *(SR2024: 1-10)*  
**Critiques:** *(SR2024: Scher, Samin, org)*  
**Funded by:** *(SR2024: Plural Platform, Metaplanet, Others, Firestreak Ventures, EA Funds in 2022)*  
**Funding in 2025:** *(SR2024 funding 2023-4: N/A)*  
**Outputs in 2025:**  
*(SR2024 outputs: The Tactics programming language/framework, cognitive emulations work, A Roadmap for Cognitive Software and A Humanist Future of AI)*  

---

### <span style="font-size:1.4em">Brainlike-AGI Safety</span> <span style="color:#bbb">[cat:brainlike_agi]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: Social and moral instincts are (partly) implemented in particular hardwired brain circuitry; let's figure out what those circuits are and how they work; this will involve symbol grounding)*  
**Theory of change:** *(SR2024: Fairly direct alignment via changing training to reflect actual human reward. Get actual data about (reward, training data) → (human values) to help with theorising this map in AIs; understand human social instincts, and then maybe adapt some aspects of those for AGIs, presumably in conjunction with other non-biological ingredients)*  
**See also:**  
**Orthodox problems:** *(SR2024: 1. Value is fragile and hard to specify)*  
**Target case:** *(SR2024: worst-case)*  
**Broad approach:** *(SR2024: cognitive)*  
**Key people:** *(SR2024: Steve Byrnes)*  
**Estimated FTEs:** *(SR2024: 1)*  
**Critiques:** *(SR2024: Not found)*  
**Funded by:** *(SR2024: Astera Institute)*  
**Funding in 2025:** *(SR2024 funding 2023-4: N/A)*  
**Outputs in 2025:**  
*(SR2024 outputs: My AGI safety research—2024 review, '25 plans, Neuroscience of human social instincts: a sketch, Intuitive Self Models)*  

---

## <span style="font-size:1.5em">Make AI solve alignment</span> <span style="color:#bbb">[cat:ai_solve_alignment]</span>


---

### <span style="font-size:1.4em">Strong-to-Weak Elicitation</span> <span style="color:#bbb">[cat:strong_to_weak]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">Scalable oversight</span> <span style="color:#bbb">[cat:scalable_oversight]</span>


---

#### <span style="font-size:1.3em">OpenAI Superalignment / Automated Alignment Research</span> <span style="color:#bbb">[cat:scalable_oversight_openai]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: be ready to align a human-level automated alignment researcher)*  
**Theory of change:** *(SR2024: get AI to help us with scalable oversight, critiques, recursive reward modelling, and so solve inner alignment)*  
**See also:**  
**Orthodox problems:** *(SR2024: 1. Value is fragile and hard to specify or 8. Superintelligence can hack software supervisors)*  
**Target case:** *(SR2024: optimistic)*  
**Broad approach:** *(SR2024: behavioural)*  
**Key people:** *(SR2024: Jan Leike, Elriggs, Jacques Thibodeau)*  
**Estimated FTEs:** *(SR2024: 10-50)*  
**Critiques:** *(SR2024: Zvi, Christiano, MIRI, Steiner, Ladish, Wentworth, Gao)*  
**Funded by:** *(SR2024: lab funders)*  
**Funding in 2025:** *(SR2024 funding 2023-4: N/A)*  
**Outputs in 2025:**  
*(SR2024 outputs: Prover-verifier games)*  

---

#### <span style="font-size:1.3em">Weak-to-strong generalization</span> <span style="color:#bbb">[cat:weak_to_strong]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[The Delta Learning Hypothesis: Preference Tuning on Weak Data can Yield Strong Gains](https://arxiv.org/abs/2507.06187)**, *Scott Geng, Hamish Ivison, Chun-Liang Li et al.*, 2025-07-08, COLM 2025, <span style="color:#777">[paper_preprint, sr=0.52, id:c74e29c4]</span>, <span style="color:#777">Summary: Demonstrates that preference tuning on paired weak data (responses from 3B and 1.5B models) can train 8B models to match state-of-the-art performance by leveraging relative quality differences between responses, with theoretical proof in logistic regression.</span>


---

#### <span style="font-size:1.3em">Supervising AIs improving AIs</span> <span style="color:#bbb">[cat:supervising_improvement]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: scalable tracking of behavioural drift, benchmarks for self-modification)*  
**Theory of change:** *(SR2024: early models train ~only on human data while later models also train on early model outputs, which leads to early model problems cascading; left unchecked this will likely cause problems, so we need a better iterative improvement process)*  
**See also:**  
**Orthodox problems:** *(SR2024: 7. Superintelligence can fool human supervisors or 8. Superintelligence can hack software supervisors)*  
**Target case:** *(SR2024: pessimistic)*  
**Broad approach:** *(SR2024: behavioural)*  
**Key people:** *(SR2024: Roman Engeler, Akbir Khan, Ethan Perez)*  
**Estimated FTEs:** *(SR2024: 1-10)*  
**Critiques:** *(SR2024: Automation collapse)*  
**Funded by:** *(SR2024: lab funders)*  
**Funding in 2025:** *(SR2024 funding 2023-4: N/A)*  
**Outputs in 2025:**  
*(SR2024 outputs: Weak LLMs judging strong LLMs, Scalable AI Safety via Doubly-Efficient Debate, Debating with More Persuasive LLMs Leads to More Truthful Answers, Prover-Verifier Games Improve Legibility of LLM Output, LLM Critics Help Catch LLM Bugs)*  

---

#### <span style="font-size:1.3em">Cyborgism</span> <span style="color:#bbb">[cat:cyborgism]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: Train human-plus-LLM alignment researchers: with humans in the loop and without outsourcing to autonomous agents)*  
**Theory of change:** *(SR2024: Cognitive prosthetics to amplify human capability and preserve values. More alignment research per year and dollar)*  
**See also:**  
**Orthodox problems:** *(SR2024: 7. Superintelligence can fool human supervisors, 9. Humans cannot be first-class parties to a superintelligent value handshake)*  
**Target case:** *(SR2024: pessimistic)*  
**Broad approach:** *(SR2024: engineering, behavioural)*  
**Key people:** *(SR2024: Janus, Nicholas Kees Dupuis)*  
**Estimated FTEs:** *(SR2024: ?)*  
**Critiques:** *(SR2024: self)*  
**Funded by:** *(SR2024: ?)*  
**Funding in 2025:** *(SR2024 funding 2023-4: N/A)*  
**Outputs in 2025:**  
*(SR2024 outputs: Pantheon Interface)*  
- **[Training LLM Agents to Empower Humans](https://arxiv.org/abs/2510.13709)**, *Evan Ellis, Vivek Myers, Jens Tuyls et al.*, 2025-10-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:71eaf2a2]</span>, <span style="color:#777">Summary: Proposes Empower, a self-supervised training method that maximizes human empowerment rather than task completion, training assistive LLM agents to defer control to humans for important decisions using only offline text data.</span>


---

#### <span style="font-size:1.3em">Transluce</span> <span style="color:#bbb">[cat:transluce]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: Make open AI tools to explain AIs, including agents. E.g. feature descriptions for neuron activation patterns; an interface for steering these features; behavior elicitation agent that searches for user-specified behaviors from frontier models)*  
**Theory of change:** *(SR2024: Introducing Transluce; improve interp and evals in public and get invited to improve lab processes)*  
**See also:**  
**Orthodox problems:** *(SR2024: 7. Superintelligence can fool human supervisors or 8. Superintelligence can hack software supervisors)*  
**Target case:** *(SR2024: pessimistic)*  
**Broad approach:** *(SR2024: cognitive)*  
**Key people:** *(SR2024: Jacob Steinhardt, Sarah Schwettmann)*  
**Estimated FTEs:** *(SR2024: 6)*  
**Critiques:** *(SR2024: not found)*  
**Funded by:** *(SR2024: Schmidt Sciences, Halcyon Futures, John Schulman, Wojciech Zaremba)*  
**Funding in 2025:** *(SR2024 funding 2023-4: N/A)*  
**Outputs in 2025:**  
*(SR2024 outputs: Eliciting Language Model Behaviors with Investigator Agents, Monitor: An AI-Driven Observability Interface, Scaling Automatic Neuron Description)*  

---

#### <span style="font-size:1.3em">DeepMind Amplified Oversight</span> <span style="color:#bbb">[cat:deepmind_amplified_oversight]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">Debate</span> <span style="color:#bbb">[cat:debate]</span>


---

#### <span style="font-size:1.3em">UK AISI debate sequence</span> <span style="color:#bbb">[cat:debate_uk_aisi]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

#### <span style="font-size:1.3em">Deepmind Scalable Alignment</span> <span style="color:#bbb">[cat:debate_deepmind]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: make highly capable agents do what humans want, even when it is difficult for humans to know what that is)*  
**Theory of change:** *(SR2024: "Give humans help in supervising strong agents" + "Align explanations with the true reasoning process of the agent" + "Red team models to exhibit failure modes that don't occur in normal use" are necessary but probably not sufficient for safe AGI)*  
**See also:**  
**Orthodox problems:** *(SR2024: 1. Value is fragile and hard to specify, 7. Superintelligence can fool human supervisors)*  
**Target case:** *(SR2024: worst-case)*  
**Broad approach:** *(SR2024: engineering, cognitive)*  
**Key people:** *(SR2024: Rohin Shah, Jonah Brown-Cohen, Georgios Piliouras)*  
**Estimated FTEs:** *(SR2024: ?)*  
**Critiques:** *(SR2024: The limits of AI safety via debate)*  
**Funded by:** *(SR2024: Google)*  
**Funding in 2025:** *(SR2024 funding 2023-4: N/A)*  
**Outputs in 2025:**  
*(SR2024 outputs: Progress update - Doubly Efficient Debate, Inference-only Experiments)*  

---

#### <span style="font-size:1.3em">Anthropic: Bowman/Perez</span> <span style="color:#bbb">[cat:debate_anthropic]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: scalable oversight of truthfulness: is it possible to develop training methods that incentivize truthfulness even when humans are unable to directly judge the correctness of a model's output?)*  
**Theory of change:** *(SR2024: current methods like RLHF will falter as frontier AI tackles harder and harder questions → we need to build tools that help human overseers continue steering AI → let's develop theory on what approaches might scale → let's build the tools)*  
**See also:**  
**Orthodox problems:** *(SR2024: 7. Superintelligence can fool human supervisors)*  
**Target case:** *(SR2024: pessimistic)*  
**Broad approach:** *(SR2024: behavioural)*  
**Key people:** *(SR2024: Sam Bowman, Ethan Perez, He He, Mengye Ren)*  
**Estimated FTEs:** *(SR2024: ?)*  
**Critiques:** *(SR2024: obfuscation, local inadequacy?, it doesn't work right now (2022))*  
**Funded by:** *(SR2024: mostly Anthropic's investors)*  
**Funding in 2025:** *(SR2024 funding 2023-4: N/A)*  
**Outputs in 2025:**  
*(SR2024 outputs: Debating with more persuasive LLMs Leads to More Truthful Answers, Sleeper Agents)*  
- **[AI Debate Aids Assessment of Controversial Claims](https://arxiv.org/abs/2506.02175)**, *Salman Rahman, Sheriff Issaka, Ashima Suvarna et al.*, 2025-06-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:67e60eca]</span>, <span style="color:#777">Summary: Empirically tests whether AI debate improves human judgment on controversial factual claims about COVID-19 and climate change, comparing debate protocols (two AIs arguing opposing sides) versus consultancy (single AI advisor) with both human and AI judges.</span>


---

### <span style="font-size:1.4em">Task decomposition</span> <span style="color:#bbb">[cat:task_decomp]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">Adversarial oversight</span> <span style="color:#bbb">[cat:adversarial_oversight]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

## <span style="font-size:1.5em">Theory</span> <span style="color:#bbb">[cat:theory]</span>


---

### <span style="font-size:1.4em">New agent theories</span> <span style="color:#bbb">[cat:new_agent_theories]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">Agent foundations</span> <span style="color:#bbb">[cat:agent_foundations]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">Tiling agents</span> <span style="color:#bbb">[cat:tiling_agents]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">Dovetail</span> <span style="color:#bbb">[cat:theory_dovetail]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">Simulators</span> <span style="color:#bbb">[cat:simulators]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">AISI on asymptotic guarantees</span> <span style="color:#bbb">[cat:aisi_guarantees]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">ARC Theory: Formalizing heuristic arguments</span> <span style="color:#bbb">[cat:arc_theory_formal]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: mech interp plus formal verification. Formalize mechanistic explanations of neural network behavior, so to predict when novel input may lead to anomalous behavior)*  
**Theory of change:** *(SR2024: find a scalable method to predict when any model will act up)*  
**See also:** *(SR2024: ELK, mechanistic anomaly detection)*  
**Orthodox problems:** *(SR2024: 4. Goals misgeneralize out of distribution, 8. Superintelligence can hack software supervisors)*  
**Target case:** *(SR2024: worst-case)*  
**Broad approach:** *(SR2024: cognitive, maths/philosophy)*  
**Key people:** *(SR2024: Jacob Hilton, Mark Xu, Eric Neyman, Dávid Matolcsi, Victor Lecomte, George Robinson)*  
**Estimated FTEs:** *(SR2024: 1-10)*  
**Critiques:** *(SR2024: Vaintrob. Clarification, alternative formulation)*  
**Funded by:** *(SR2024: FLI, SFF)*  
**Funding in 2025:** *(SR2024 funding 2023-4: $1.7m)*  
**Outputs in 2025:**  
*(SR2024 outputs: Estimating tail risk, Towards a Law of Iterated Expectations for Heuristic Estimators, Probabilities of rare outputs, Bird's eye overview, Formal verification)*  

---

### <span style="font-size:1.4em">Acausal research</span> <span style="color:#bbb">[cat:acausal]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">Miscellaneous theory items</span> <span style="color:#bbb">[cat:misc_theory]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[A Taxonomy of Omnicidal Futures Involving Artificial Intelligence](https://arxiv.org/abs/2507.09369)**, *Andrew Critch, Jacob Tsimerman*, 2025-07-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:cba996bb]</span>, <span style="color:#777">Summary: Presents a systematic taxonomy classifying different pathways by which AI systems could cause omnicidal outcomes (scenarios where all or nearly all humans are killed), aiming to inform institutional preventive measures against catastrophic AI risks.</span>
- **[General agents contain world models](https://arxiv.org/abs/2506.01622)**, *Jonathan Richens, David Abel, Alexis Bellot et al.*, 2025-06-02, ICML 2025, <span style="color:#777">[paper_preprint, sr=0.70, id:93b986a9]</span>, <span style="color:#777">Summary: Provides formal proof that any agent capable of generalizing to multi-step goal-directed tasks must have learned a predictive model of its environment, and shows these world models can be extracted from the agent's policy.</span>
- **[The Limits of Predicting Agents from Behaviour](https://arxiv.org/abs/2506.02923)**, *Alexis Bellot, Jonathan Richens, Tom Everitt*, 2025-06-03, ICML 2025, <span style="color:#777">[paper_preprint, sr=0.68, id:91199d50]</span>, <span style="color:#777">Summary: Derives novel theoretical bounds on how well an agent's beliefs can be inferred from behavior and how reliably these inferred beliefs predict behavior in novel deployment environments, assuming the agent's behavior is guided by a world model.</span>
- **[Can CDT rationalise the ex ante optimal policy via modified anthropics?](https://arxiv.org/abs/2411.04462)**, *Emery Cooper, Caspar Oesterheld, Vincent Conitzer*, 2024-11-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:6188055f]</span>, <span style="color:#777">Summary: Studies whether causal decision theory can recommend ex ante optimal policies in Newcomblike problems through modified anthropic reasoning, proposing simulation-based models and a 'Generalised Generalised Thirding' framework with formal characterizations and proofs.</span>


---

### <span style="font-size:1.4em">Corrigibility</span> <span style="color:#bbb">[cat:corrigibility]</span>


---

#### <span style="font-size:1.3em">Behavior alignment theory</span> <span style="color:#bbb">[cat:behavior_alignment_theory]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: predict properties of AGI (e.g. powerseeking) with formal models. Corrigibility as the opposite of powerseeking)*  
**Theory of change:** *(SR2024: figure out hypotheses about properties powerful agents will have → attempt to rigorously prove under what conditions the hypotheses hold, test them when feasible)*  
**See also:** *(SR2024: this, EJT, Dupuis, Holtman)*  
**Orthodox problems:** *(SR2024: 2. Corrigibility is anti-natural, 5. Instrumental convergence)*  
**Target case:** *(SR2024: worst-case)*  
**Broad approach:** *(SR2024: maths/philosophy)*  
**Key people:** *(SR2024: Michael K. Cohen, Max Harms/Raelifin, John Wentworth, David Lorell, Elliott Thornley)*  
**Estimated FTEs:** *(SR2024: 1-10)*  
**Critiques:** *(SR2024: none found)*  
**Funded by:** *(SR2024: ?)*  
**Funding in 2025:** *(SR2024 funding 2023-4: ?)*  
**Outputs in 2025:**  
*(SR2024 outputs: CAST: Corrigibility As Singular Target, A Shutdown Problem Proposal, The Shutdown Problem: Incomplete Preferences as a Solution)*  
- **[Shutdownable Agents through POST-Agency](https://arxiv.org/abs/2505.20203)**, *Elliott Thornley*, 2025-05-26, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:1038a9f2]</span>, <span style="color:#777">Summary: Proposes the POST-Agents framework where agents satisfy Preferences Only Between Same-Length Trajectories, and proves this implies Neutrality+ (maximizing expected utility while ignoring trajectory-length distributions), which enables shutdownable agents.</span>
- **[The Partially Observable Off-Switch Game](https://arxiv.org/abs/2411.17749)**, *Andrew Garber, Rohan Subramani, Linus Luu et al.*, 2024-11-25, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:7d25e6c2]</span>, <span style="color:#777">Summary: Introduces the Partially Observable Off-Switch Game (PO-OSG), a game-theoretic formalization of the shutdown problem with asymmetric information between humans and AI agents, analyzing conditions under which AIs defer to human shutdown commands.</span>
- **[Measuring Goal-Directedness](https://arxiv.org/abs/2412.04758)**, *Matt MacDermott, James Fox, Francesco Belardinelli et al.*, 2024-12-06, NeurIPS 2024, <span style="color:#777">[paper_published, sr=0.82, id:6eca9c01]</span>, <span style="color:#777">Summary: Defines maximum entropy goal-directedness (MEG), a formal measure of goal-directedness in causal models and MDPs based on maximum causal entropy, proves it satisfies key desiderata, and provides algorithms for computing it with small-scale experimental demonstrations.</span>


---

#### <span style="font-size:1.3em">Other corrigibility</span> <span style="color:#bbb">[cat:corrigibility_other]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">Ontology Identification</span> <span style="color:#bbb">[cat:ontology_identification]</span>


---

#### <span style="font-size:1.3em">Natural abstractions</span> <span style="color:#bbb">[cat:natural_abstractions]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: check the hypothesis that our universe "abstracts well" and that many cognitive systems learn to use similar abstractions. Check if features correspond to small causal diagrams corresponding to linguistic constructions)*  
**Theory of change:** *(SR2024: find all possible abstractions of a given computation → translate them into human-readable language → identify useful ones like deception → intervene when a model is using it. Also develop theory for interp more broadly; more mathematical analysis. Also maybe enables "retargeting the search" (direct training away from things we don't want))*  
**See also:** *(SR2024: causal abstractions, representational alignment, convergent abstractions)*  
**Orthodox problems:** *(SR2024: 5. Instrumental convergence, 7. Superintelligence can fool human supervisors, 9. Humans cannot be first-class parties to a superintelligent value handshake)*  
**Target case:** *(SR2024: worst-case)*  
**Broad approach:** *(SR2024: cognitive)*  
**Key people:** *(SR2024: John Wentworth, Paul Colognese, David Lorrell, Sam Eisenstat)*  
**Estimated FTEs:** *(SR2024: 1-10)*  
**Critiques:** *(SR2024: Chan et al, Soto, Harwood, Soares)*  
**Funded by:** *(SR2024: EA Funds)*  
**Funding in 2025:** *(SR2024 funding 2023-4: N/A?)*  
**Outputs in 2025:**  
*(SR2024 outputs: Natural Latents: The Concepts, Natural Latents Are Not Robust To Tiny Mixtures, Towards a Less Bullshit Model of Semantics)*  
- **[Natural Latents: Latent Variables Stable Across Ontologies](https://arxiv.org/abs/2509.03780)**, *John Wentworth, David Lorell*, 2025-09-04, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:7d3d716e]</span>, <span style="color:#777">Summary: Provides mathematical conditions under which latent variables learned by different Bayesian agents modeling the same environment are guaranteed to be translatable between their ontologies, proving these 'natural latent conditions' are the most general such conditions and are robust to approximation error.</span>


---

#### <span style="font-size:1.3em">Other ontology work</span> <span style="color:#bbb">[cat:ontology_other]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Factored space models: Towards causality between levels of abstraction](https://arxiv.org/abs/2412.02579)**, *Scott Garrabrant, Matthias Georg Mayer, Magdalena Wache et al.*, 2024-12-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.62, id:13e4aa37]</span>, <span style="color:#777">Summary: Introduces factored space models as a mathematical framework for reasoning about causality across hierarchical levels of abstraction, handling both probabilistic and deterministic relationships where traditional causal graphs fail. Proves that structural independence in factored spaces is equivalent to statistical independence, generalizing classical d-separation results.</span>


---

### <span style="font-size:1.4em">Understand cooperation</span> <span style="color:#bbb">[cat:understand_cooperation]</span>


---

#### <span style="font-size:1.3em">Pluralistic alignment / collective intelligence</span> <span style="color:#bbb">[cat:pluralistic_alignment]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: align AI to broader values / use AI to understand and improve coordination among humans)*  
**Theory of change:** *(SR2024: focus on getting more people and values represented)*  
**See also:** *(SR2024: AI Objectives Institute, Lightcone Chord, Intelligent Cooperation, Meaning Alignment Institute. See also AI-AI Bias)*  
**Orthodox problems:** *(SR2024: 11. Someone else will deploy unsafe superintelligence first, 13. Fair, sane pivotal processes)*  
**Target case:** *(SR2024: optimistic)*  
**Broad approach:** *(SR2024: engineering?)*  
**Key people:** *(SR2024: Yejin Choi, Seth Lazar, Nouha Dziri, Deger Turan, Ivan Vendrov, Jacob Lagerros)*  
**Estimated FTEs:** *(SR2024: 10-50)*  
**Critiques:** *(SR2024: none found)*  
**Funded by:** *(SR2024: Foresight, Midjourney?)*  
**Funding in 2025:** *(SR2024 funding 2023-4: N/A)*  
**Outputs in 2025:**  
*(SR2024 outputs: roadmap, workshop)*  
- **[Resource Rational Contractualism Should Guide AI Alignment](https://arxiv.org/abs/2506.17434)**, *Sydney Levine, Matija Franklin, Tan Zhi-Xuan et al.*, 2025-06-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:c9bbef6a]</span>, <span style="color:#777">Summary: Proposes Resource-Rational Contractualism (RRC), a framework for AI alignment that approximates agreements diverse stakeholders would endorse by using cognitively-inspired heuristics that trade computational effort for accuracy when navigating value conflicts.</span>
- **[Can AI Model the Complexities of Human Moral Decision-Making? A Qualitative Study of Kidney Allocation Decisions](https://arxiv.org/abs/2503.00940)**, *Vijay Keswani, Vincent Conitzer, Walter Sinnott-Armstrong et al.*, 2025-03-02, ACM CHI 2025, <span style="color:#777">[paper_published, sr=0.40, id:416ebfc6]</span>, <span style="color:#777">Summary: Qualitative study with 20 interviews examining whether AI models can capture the complexity of human moral decision-making in kidney allocation contexts, finding that humans use diverse heuristics, change opinions, and express varying confidence levels that simple computational models fail to capture.</span>


---

#### <span style="font-size:1.3em">Center on Long-Term Risk (CLR)</span> <span style="color:#bbb">[cat:clr]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: future agents creating s-risks is the worst of all possible problems, we should avoid that)*  
**Theory of change:** *(SR2024: make present and future AIs inherently cooperative via improving theories of cooperation and measuring properties related to catastrophic conflict)*  
**See also:** *(SR2024: FOCAL)*  
**Orthodox problems:** *(SR2024: 1. Value is fragile and hard to specify, 3. Pivotal processes require dangerous capabilities, 4. Goals misgeneralize out of distribution)*  
**Target case:** *(SR2024: worst-case)*  
**Broad approach:** *(SR2024: maths/philosophy)*  
**Key people:** *(SR2024: Jesse Clifton, Caspar Oesterheld, Anthony DiGiovanni, Maxime Riché, Mia Taylor)*  
**Estimated FTEs:** *(SR2024: 10-50)*  
**Critiques:** *(SR2024: none found)*  
**Funded by:** *(SR2024: Polaris Ventures, Survival and Flourishing Fund, Community Foundation Ireland)*  
**Funding in 2025:** *(SR2024 funding 2023-4: $1,327,000)*  
**Outputs in 2025:**  
*(SR2024 outputs: Measurement Research Agenda, Computing Optimal Commitments to Strategies and Outcome-conditional Utility Transfers)*  

---

#### <span style="font-size:1.3em">FOCAL</span> <span style="color:#bbb">[cat:focal]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: make sure advanced AI uses what we regard as proper game theory)*  
**Theory of change:** *(SR2024: (1) keep the pre-superintelligence world sane by making AIs more cooperative; (2) remain integrated in the academic world, collaborate with academics on various topics and encourage their collaboration on x-risk; (3) hope that work on "game theory for AIs", which emphasises cooperation and benefit to humans, has framing & founder effects on the new academic field)*  
**See also:**  
**Orthodox problems:** *(SR2024: 1. Value is fragile and hard to specify, 10. Humanlike minds/goals are not necessarily safe)*  
**Target case:** *(SR2024: pessimistic)*  
**Broad approach:** *(SR2024: maths/philosophy)*  
**Key people:** *(SR2024: Vincent Conitzer, Caspar Oesterheld, Vojta Kovarik)*  
**Estimated FTEs:** *(SR2024: 1-10)*  
**Critiques:** *(SR2024: Self-submitted: "our theory of change is not clearly relevant to superintelligent AI")*  
**Funded by:** *(SR2024: Cooperative AI Foundation, Polaris Ventures)*  
**Funding in 2025:** *(SR2024 funding 2023-4: N/A)*  
**Outputs in 2025:**  
*(SR2024 outputs: Foundations of Cooperative AI, A dataset of questions on decision-theoretic reasoning in Newcomb-like problems, Why should we ever automate moral decision making?, Social Choice Should Guide AI Alignment in Dealing with Diverse Human Feedback)*  
- **[A dataset of questions on decision-theoretic reasoning in Newcomb-like problems](https://arxiv.org/abs/2411.10588)**, *Caspar Oesterheld, Emery Cooper, Miles Kodama et al.*, 2024-11-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.70, id:a1e47dbb]</span>, <span style="color:#777">Summary: Introduces a dataset of natural-language questions for evaluating decision-theoretic reasoning in Newcomb-like problems and uses it to investigate decision-theoretical capabilities and attitudes across frontier models from OpenAI, Anthropic, Meta, GDM, and Reka.</span>
- **[Limit-Computable Grains of Truth for Arbitrary Computable Extensive-Form (Un)Known Games](https://arxiv.org/abs/2508.16245)**, *Cole Wyeth, Marcus Hutter, Jan Leike et al.*, 2025-08-22, arXiv, <span style="color:#777">[paper_preprint, sr=0.58, id:08d444f7]</span>, <span style="color:#777">Summary: Solves Kalai and Lehrer's grain of truth problem by constructing a class of strategies containing all computable strategies and Bayes-optimal policies, proving convergence to Nash equilibria in unknown multi-agent environments using Thompson sampling.</span>
- **[Characterising Simulation-Based Program Equilibria](https://arxiv.org/abs/2412.14570)**, *Emery Cooper, Caspar Oesterheld, Vincent Conitzer*, 2024-12-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.48, id:6d896b39]</span>, <span style="color:#777">Summary: Generalizes Oesterheld's εGroundedπBot approach to program equilibria where players submit programs that can simulate opponents, proves folk theorems with and without shared randomness, and characterizes the range of achievable equilibria in simulation-based settings.</span>


---

### <span style="font-size:1.4em">Alternatives to utility theory</span> <span style="color:#bbb">[cat:alternatives_utility]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">Singular Learning Theory</span> <span style="color:#bbb">[cat:singular_learning]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Compressibility Measures Complexity: Minimum Description Length Meets Singular Learning Theory](https://arxiv.org/abs/2510.12077)**, *Einar Urdshals, Edmund Lau, Jesse Hoogland et al.*, 2025-10-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:20d78e37]</span>, <span style="color:#777">Summary: Extends the minimum description length principle to neural networks using singular learning theory, demonstrating through experiments on Pythia models that local learning coefficient (LLC) correlates closely with compressibility across various compression techniques.</span>
- **[Modes of Sequence Models and Learning Coefficients](https://arxiv.org/abs/2504.18048)**, *Zhongtian Chen, Daniel Murfet*, 2025-04-25, arXiv, <span style="color:#777">[paper_preprint, sr=0.55, id:a0f0e5c6]</span>, <span style="color:#777">Summary: Develops a geometric framework using Hilbert-space and tensor decompositions to link data patterns to loss landscape properties in transformers, showing that Local Learning Coefficient estimates are insensitive to small-amplitude modes below a threshold.</span>


---

### <span style="font-size:1.4em">The Learning-Theoretic Agenda</span> <span style="color:#bbb">[cat:learning_theoretic_agenda]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: try to formalise a more realistic agent, understand what it means for it to be aligned with us, translate between its ontology and ours, and produce desiderata for a training setup that points at coherent AGIs similar to our model of an aligned agent)*  
**Theory of change:** *(SR2024: fix formal epistemology to work out how to avoid deep training problems)*  
**See also:**  
**Orthodox problems:** *(SR2024: 1. Value is fragile and hard to specify, 9. Humans cannot be first-class parties to a superintelligent value handshake)*  
**Target case:** *(SR2024: worst-case)*  
**Broad approach:** *(SR2024: cognitive)*  
**Key people:** *(SR2024: Vanessa Kosoy, Diffractor)*  
**Estimated FTEs:** *(SR2024: 3)*  
**Critiques:** *(SR2024: Matolcsi)*  
**Funded by:** *(SR2024: EA Funds, Survival and Flourishing Fund, ARIA)*  
**Funding in 2025:** *(SR2024 funding 2023-4: $123,000)*  
**Outputs in 2025:**  
*(SR2024 outputs: Linear infra-Bayesian Bandits, Time complexity for deterministic string machines, Infra-Bayesian Haggling, Quantum Mechanics in Infra-Bayesian Physicalism. Intro lectures)*  
- **[Regret Bounds for Robust Online Decision Making](https://arxiv.org/abs/2504.06820)**, *Alexander Appel, Vanessa Kosoy*, 2025-04-09, arXiv, <span style="color:#777">[paper_preprint, sr=0.45, id:3e1bed8d]</span>, <span style="color:#777">Summary: Proposes a framework for online decision-making with robust (multivalued) models where each decision associates with a convex set of probability distributions, deriving regret bounds for this setting and demonstrating applications to robust linear bandits and tabular robust online reinforcement learning.</span>


---

## <span style="font-size:1.5em">Sociotechnical</span> <span style="color:#bbb">[cat:sociotechnical]</span>


---

### <span style="font-size:1.4em">Third wave AI safety</span> <span style="color:#bbb">[cat:third_wave]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Gradual Disempowerment: Systemic Existential Risks from Incremental AI Development](https://arxiv.org/abs/2501.16946)**, *Jan Kulveit, Raymond Douglas, Nora Ammann et al.*, 2025-01-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.58, id:e6e162ea]</span>, <span style="color:#777">Summary: Develops the concept of 'gradual disempowerment' to analyze how incremental AI advancements can systematically undermine human influence over large-scale societal systems (economy, culture, nation-states), leading to existential risk through cumulative rather than abrupt effects.</span>


---

### <span style="font-size:1.4em">Collective alignment</span> <span style="color:#bbb">[cat:collective_alignment]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Cultivating Pluralism In Algorithmic Monoculture: The Community Alignment Dataset](https://arxiv.org/abs/2507.09650)**, *Lily Hong Zhang, Smitha Milli, Karen Jusko et al.*, 2025-07-13, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:e066e2b3]</span>, <span style="color:#777">Summary: Demonstrates through a 15,000-participant multilingual study that LLMs exhibit insufficient preference diversity compared to humans, then introduces negatively-correlated sampling methodology and releases the Community Alignment dataset with 200,000 preference comparisons across five countries.</span>
- **[Democratic AI is Possible. The Democracy Levels Framework Shows How It Might Work](https://arxiv.org/abs/2411.09222)**, *Aviv Ovadya, Kyle Redman, Luke Thorburn et al.*, 2024-11-14, arXiv (Accepted to ICML 2025 Position Paper Track), <span style="color:#777">[paper_preprint, sr=0.52, id:9d0771d3]</span>, <span style="color:#777">Summary: Proposes a 'Democracy Levels' framework defining milestones toward meaningfully democratic AI governance and alignment, building on approaches like Anthropic's Collective Constitutional AI and Meta's Community Forums to guide organizations in improving public involvement in critical AI decisions.</span>


---

### <span style="font-size:1.4em">Infrastructure for AI Agents</span> <span style="color:#bbb">[cat:infrastructure_agents]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Characterizing AI Agents for Alignment and Governance](https://arxiv.org/abs/2504.21848)**, *Atoosa Kasirzadeh, Iason Gabriel*, 2025-04-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.42, id:66d15eaf]</span>, <span style="color:#777">Summary: Proposes a characterization framework for AI agents based on four dimensions (autonomy, efficacy, goal complexity, and generality) to construct 'agentic profiles' that illuminate governance challenges across different types of AI agents.</span>


---

## <span style="font-size:1.5em">Misc / for new agenda clustering</span> <span style="color:#bbb">[cat:misc_new_agendas]</span>


---

### <span style="font-size:1.4em">Multi-agents (misc)</span> <span style="color:#bbb">[cat:misc_multiagents]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">Multi-org research clusters</span> <span style="color:#bbb">[cat:misc_org_clusters]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  

---

### <span style="font-size:1.4em">Other uncategorized work</span> <span style="color:#bbb">[cat:misc_other]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:**  
**Theory of change:**  
**See also:**  
**Orthodox problems:**  
**Target case:**  
**Broad approach:**  
**Key people:**  
**Estimated FTEs:**  
**Critiques:**  
**Funded by:**  
**Funding in 2025:**  
**Outputs in 2025:**  
- **[Uncertainty-Aware Step-wise Verification with Generative Reward Models](https://arxiv.org/abs/2502.11250)**, *Zihuiwen Ye, Luckeciano Carvalho Melo, Younesse Kaddar et al.*, 2025-02-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:2804277b]</span>, <span style="color:#777">Summary: Introduces CoT Entropy, a novel uncertainty quantification method for process reward models (PRMs) used in step-wise verification of LLM reasoning, addressing reliability issues including reward hacking.</span>
- **[Can Safety Fine-Tuning Be More Principled? Lessons Learned from Cybersecurity](https://arxiv.org/abs/2501.11183)**, *David Williams-King, Linh Le, Adam Oberman et al.*, 2025-01-19, NeurIPS Safe Generative AI Workshop 2024, <span style="color:#777">[paper_published, sr=0.72, id:456e1f40]</span>, <span style="color:#777">Summary: Argues that current LLM safety fine-tuning resembles ineffective cybersecurity patch-and-pray approaches, advocating for more principled safety-by-design methods that architect security from the beginning rather than reactively patching jailbreaks.</span>
- **[International Scientific Report on the Safety of Advanced AI (Interim Report)](https://arxiv.org/abs/2412.05282)**, *Yoshua Bengio, Sören Mindermann, Daniel Privitera et al.*, 2024-11-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.70, id:4137abe9]</span>, <span style="color:#777">Summary: Comprehensive international scientific report synthesizing the current understanding of general-purpose AI safety and risk management, produced by 75 AI experts from an international expert advisory panel nominated by 30 countries, the EU, and the UN.</span>
- **[AI Risk-Management Standards Profile for General-Purpose AI (GPAI) and Foundation Models](https://arxiv.org/abs/2506.23949)**, *Anthony M. Barrett, Jessica Newman, Brandie Nonnecke et al.*, 2025-06-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.58, id:eafa3355]</span>, <span style="color:#777">Summary: Provides risk-management practices and controls for identifying, analyzing, and mitigating risks of general-purpose AI and foundation models, adapting NIST AI Risk Management Framework and ISO/IEC 23894 standards for developers of large-scale GPAI systems.</span>
- **[A Taxonomy of Systemic Risks from General-Purpose AI](https://arxiv.org/abs/2412.07780)**, *Risto Uuk, Carlos Ignacio Gutierrez, Daniel Guppy et al.*, 2024-11-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.48, id:377f9d40]</span>, <span style="color:#777">Summary: Systematic literature review analyzing 86 papers from an initial pool of 1,781 documents to develop a taxonomy of 13 systemic risk categories and 50 contributing sources associated with general-purpose AI, covering threats ranging from environmental harm and discrimination to loss of control.</span>
- **[1-2-3 Check: Enhancing Contextual Privacy in LLM via Multi-Agent Reasoning](https://arxiv.org/abs/2508.07667)**, *Wenkai Li, Liwen Sun, Zhenxiang Guan et al.*, 2025-08-11, arXiv, <span style="color:#777">[paper_preprint, sr=0.48, id:b98d7126]</span>, <span style="color:#777">Summary: Introduces a multi-agent framework that decomposes privacy reasoning into specialized subtasks (extraction, classification) to reduce private information leakage from LLMs processing mixed public and private information.</span>
- **[Military AI Cyber Agents (MAICAs) Constitute a Global Threat to Critical Infrastructure](https://arxiv.org/abs/2506.12094)**, *Timothy Dubber, Seth Lazar*, 2025-06-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.42, id:0961ecce]</span>, <span style="color:#777">Summary: Argues that autonomous AI cyber-weapons (MAICAs) create a credible pathway to catastrophic risk, analyzing their technical feasibility, geopolitical implications, and proposing political, defensive-AI, and analogue-resilience mitigation measures.</span>


---

