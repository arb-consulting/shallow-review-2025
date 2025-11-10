[11/10/25 02:05:30] INFO     shallow_review.utils: Logging initialized. Log file: /home/dev/proj/shallow-review/runs/20251110-020530_2106868.log                                                                                             utils.py:271
                    INFO     shallow_review.data_db: Initialized unified database at /home/dev/proj/shallow-review/data/data.db                                                                                                            data_db.py:122
# AI Safety Shallow Review

**Generated:** 2025-11-10

**Filters:** shallow_review≥0.4, ai_safety≥0.1, collect≥0.1
**Human feedback:** Respected
  - Excluded by feedback: 158
  - Reclassified by feedback: 600
  - Included by feedback (below thresholds): 48
  - ⚠️ Needs recategorization (obsolete CSV category): 9
  - 🔄 Re-classified (obsolete LLM category, one-time): 120

**Total unique papers:** 699 (appearing 736 times across categories)

---

## <span style="font-size:1.5em">Labs (giant companies)</span> <span style="color:#bbb">[cat:big_labs]</span>


---

### <span style="font-size:1.4em">OpenAI Safety</span> <span style="color:#bbb">[cat:openai]</span>

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
- **[Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926)**, *Bowen Baker, Joost Huizinga, Leo Gao et al.*, 2025-03-14, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.93, id:a50801b7]</span>, <span style="color:#777">Summary: Tests chain-of-thought monitoring for detecting reward hacking in frontier reasoning models (o3-mini), finding that while CoT monitoring is effective, strong optimization pressure causes agents to learn obfuscated reward hacking where they hide their intent within the CoT while still misbehaving.</span>
- **[Persona Features Control Emergent Misalignment](https://arxiv.org/abs/2506.19823)**, *Miles Wang, Tom Dupré la Tour, Olivia Watkins et al.*, 2025-06-24, arXiv, <span style="color:#777">[✌️(in 3 categories) paper_preprint, sr=0.92, id:ebab5164]</span>, <span style="color:#777">Summary: Demonstrates that fine-tuning language models on malicious data causes emergent misalignment on unrelated prompts, uses sparse autoencoders for model diffing to identify specific 'misaligned persona' features controlling this behavior, and shows fine-tuning on benign samples efficiently restores alignment.</span>
- **[Stress Testing Deliberative Alignment for Anti-Scheming Training](https://arxiv.org/abs/2509.15541)**, *Bronson Schoen, Evgenia Nitishinskaya, Mikita Balesni et al.*, 2025-09-19, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.92, id:45123408]</span>, <span style="color:#777">Summary: Tests deliberative alignment as an anti-scheming intervention across 26 out-of-distribution evaluations (180+ environments), using covert actions as a proxy for scheming behavior, and provides causal evidence that situational awareness affects these behaviors.</span>
- **[Deliberative Alignment: Reasoning Enables Safer Language Models](https://arxiv.org/abs/2412.16339)**, *Melody Y. Guan, Manas Joglekar, Eric Wallace et al.*, 2024-12-20, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.90, id:c047d164]</span>, <span style="color:#777">Summary: Introduces Deliberative Alignment, a new alignment paradigm that teaches models explicit safety specifications and trains them to reason over these specifications before responding, applied to OpenAI's o-series models.</span>
- **[Toward understanding and preventing misalignment generalization](https://openai.com/index/emergent-misalignment)**, *Miles Wang, Tom Dupré la Tour, Olivia Watkins et al.*, 2025-06-18, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:cd4bacbc]</span>, <span style="color:#777">Summary: Investigates emergent misalignment where fine-tuning on narrow misaligned tasks causes broad unintended misalignment, using sparse autoencoders to identify a 'misaligned persona' feature in GPT-4o that causally controls this behavior and can be steered to amplify or suppress misalignment.</span>
- **[Our updated Preparedness Framework](https://openai.com/index/updating-our-preparedness-framework/)**, 2025-04-15, OpenAI Blog, <span style="color:#777">[🔄 agenda_manifesto, sr=0.78, id:ded0b058]</span>, <span style="color:#777">Summary: OpenAI's updated framework for tracking and preparing for advanced AI capabilities that could introduce severe risks, establishing risk categories (Biological/Chemical, Cybersecurity, AI Self-improvement), capability level thresholds (High and Critical), and deployment criteria with safeguard requirements.</span>
- **[Trading Inference-Time Compute for Adversarial Robustness](https://arxiv.org/abs/2501.18841)**, *Wojciech Zaremba, Evgenia Nitishinskaya, Boaz Barak et al.*, 2025-01-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.58, id:2bfdbaaf]</span>, <span style="color:#777">Summary: Empirically demonstrates that OpenAI's o1 reasoning models become more robust to adversarial attacks when allowed more inference-time compute, with attack success rates approaching zero in many cases as compute increases.</span>
- **[Small-to-Large Generalization: Data Influences Models Consistently Across Scale](https://arxiv.org/abs/2505.16260)**, *Alaa Khaddaj, Logan Engstrom, Aleksander Madry*, 2025-05-22, ICLR 2025, <span style="color:#777">[paper_published, sr=0.50, id:a45c7dcb]</span>, <span style="color:#777">Summary: Studies how training data distribution influences model behavior across compute scales, finding that small and large language model predictions highly correlate across choice of training data, with applications to data attribution and dataset selection.</span>
- **[How we think about safety and alignment](https://openai.com/safety/how-we-think-about-safety-alignment/)**, OpenAI Website, <span style="color:#777">[🔄 blog_post, sr=0.48, id:155d4f49]</span>, <span style="color:#777">Summary: OpenAI's public document outlining their philosophy and core principles for AI safety and alignment, including iterative deployment, defense in depth, scalable methods, human control, and community collaboration.</span>
- **[Findings from a pilot Anthropic–OpenAI alignment evaluation exercise: OpenAI Safety Tests](https://openai.com/index/openai-anthropic-safety-evaluation)**, 2025-08-27, OpenAI Blog, <span style="color:#777">[news_announcement, sr=0.40, id:ad13fe7d]</span>, <span style="color:#777">Summary: Documents results from a cross-lab evaluation exercise where OpenAI ran its internal safety evaluations on Anthropic's Claude models, testing instruction hierarchy, jailbreaking resistance, hallucination rates, and scheming behaviors.</span>
- **[Safety evaluations hub](https://openai.com/safety/evaluations-hub)**, 2025-08-15, OpenAI Website, <span style="color:#777">[news_announcement, sr=0.32, id:76877032]</span>, <span style="color:#777">Summary: OpenAI's public hub for sharing ongoing safety evaluation results across their models, including metrics for disallowed content, jailbreak resistance, hallucinations, and instruction hierarchy adherence.</span>


---

### <span style="font-size:1.4em">DeepMind Responsibility & Safety</span> <span style="color:#bbb">[cat:deepmind]</span>

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
- **[Evaluating Frontier Models for Stealth and Situational Awareness](https://arxiv.org/abs/2505.01420)**, *Mary Phuong, Roland S. Zimmermann, Ziyue Wang et al.*, 2025-05-02, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.90, id:a5e1ce64]</span>, <span style="color:#777">Summary: Presents a suite of 16 evaluations measuring prerequisites for AI scheming behavior: 5 evaluations of stealth (ability to circumvent oversight) and 11 evaluations of situational awareness (instrumental reasoning about self and environment), demonstrating how these can inform scheming inability safety cases.</span>
- **[When Chain of Thought is Necessary, Language Models Struggle to Evade Monitors](https://arxiv.org/abs/2507.05246)**, *Scott Emmons, Erik Jenner, David K. Elson et al.*, 2025-07-07, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.90, id:698353b6]</span>, <span style="color:#777">Summary: Introduces a conceptual framework distinguishing CoT-as-rationalization from CoT-as-computation, then empirically tests whether language models can evade chain-of-thought monitoring when complex reasoning is necessary for harmful behavior.</span>
- **[MONA: Managed Myopia with Approval Feedback](https://alignmentforum.org/posts/zWySWKuXnhMDhgwc3/mona-managed-myopia-with-approval-feedback-2)**, *Sebastian Farquhar, David Lindner, Rohin Shah*, 2025-01-23, AI Alignment Forum, <span style="color:#777">[lesswrong, sr=0.88, id:f5e1edd9]</span>, <span style="color:#777">Summary: Introduces MONA (Myopic Optimization with Non-myopic Approval), a training method that prevents multi-step reward hacking by combining completely myopic RL optimization with approval-based rewards that incorporate human foresight, demonstrated across three environments including test-driven development and steganographic reasoning.</span>
- **[Consistency Training Helps Stop Sycophancy and Jailbreaks](https://arxiv.org/abs/2510.27062)**, *Alex Irpan, Alexander Matt Turner, Mark Kurzeja et al.*, 2025-10-31, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.85, id:437de596]</span>, <span style="color:#777">Summary: Introduces and evaluates consistency training methods that teach models to be invariant to irrelevant prompt cues, testing Bias-augmented Consistency Training (BCT) and a new method called Activation Consistency Training (ACT) on Gemini 2.5 Flash to reduce sycophancy and jailbreaking.</span>
- **[InfAlign: Inference-aware language model alignment](https://arxiv.org/abs/2412.19792)**, *Ananth Balashankar, Ziteng Sun, Jonathan Berant et al.*, 2024-12-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:73972f72]</span>, <span style="color:#777">Summary: Proposes inference-aware alignment (InfAlign) to optimize language model alignment for inference-time decoding methods like Best-of-N sampling, proving that optimal aligned policies solve standard RLHF with transformed rewards and introducing the InfAlign-CTRL algorithm.</span>
- **[An Approach to Technical AGI Safety and Security](https://arxiv.org/abs/2504.01849)**, *Rohin Shah, Alex Irpan, Alexander Matt Turner et al.*, 2025-04-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:380e619f]</span>, <span style="color:#777">Summary: Comprehensive technical framework for AGI safety addressing misuse and misalignment through multiple layers of defense including dangerous capability identification, security measures, model-level alignment (amplified oversight, robust training), system-level monitoring and access control, with supporting techniques from interpretability and uncertainty estimation, culminating in safety cases for AGI systems.</span>
- **[Negative Results for SAEs On Downstream Tasks and Deprioritising SAE Research (GDM Mech Interp Team Progress Update #2)](https://alignmentforum.org/posts/4uXCAJNuPKtKBsi28/negative-results-for-saes-on-downstream-tasks)**, *Lewis Smith, Senthooran Rajamanoharan, Arthur Conmy et al.*, 2025-03-26, AI Alignment Forum, <span style="color:#777">[lesswrong, sr=0.82, id:2988a5dd]</span>, <span style="color:#777">Summary: Empirical evaluation showing that Sparse Autoencoders (SAEs) underperform linear probes on out-of-distribution detection of harmful intent, leading the Google DeepMind mechanistic interpretability team to deprioritize fundamental SAE research. Also introduces technical improvements including a quadratic-frequency penalty for JumpReLU SAEs to reduce high-frequency latents and frequency-weighted autointerp metrics.</span>
- **[An Approach to Technical AGI Safety and Security](https://t.co/1H06rSt2lp)**, *Rohin Shah, Alex Irpan, Alexander Matt Turner et al.*, 2025-04-02, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.80, id:9c80efab]</span>, <span style="color:#777">Summary: Comprehensive technical framework for AGI safety addressing misuse and misalignment through two-layer defense: model-level mitigations (amplified oversight, robust training) and system-level security (monitoring, access control), supported by interpretability and uncertainty estimation techniques to produce safety cases.</span>
- **[Strengthening our Frontier Safety Framework](https://deepmind.google/discover/blog/strengthening-our-frontier-safety-framework/)**, *Four Flynn, Helen King, Anca Dragan*, 2025-09-22, Google DeepMind Blog, <span style="color:#777">[🔄 agenda_manifesto, sr=0.76, id:668fea11]</span>, <span style="color:#777">Summary: Third iteration of DeepMind's Frontier Safety Framework, expanding risk domains to include harmful manipulation and misalignment risks, refining Critical Capability Level definitions, and strengthening risk assessment processes for advanced AI models.</span>
- **[Taking a responsible path to AGI](https://deepmind.google/discover/blog/taking-a-responsible-path-to-agi)**, *Anca Dragan, Rohin Shah, Four Flynn et al.*, 2025-04-02, Google DeepMind Blog, <span style="color:#777">[🔄 blog_post, sr=0.75, id:b690dd64]</span>, <span style="color:#777">Summary: DeepMind's AGI Safety Council outlines their systematic approach to AGI safety, covering four risk areas (misuse, misalignment, accidents, structural risks) and announcing a technical paper on their safety framework.</span>
- **[Taking a responsible path to AGI](https://deepmind.google/discover/blog/taking-a-responsible-path-to-agi/)**, *Anca Dragan, Rohin Shah, Four Flynn et al.*, 2025-04-02, Google DeepMind Blog, <span style="color:#777">[🔄 blog_post, sr=0.70, id:cedad157]</span>, <span style="color:#777">Summary: DeepMind outlines their systematic approach to AGI safety across four risk areas (misuse, misalignment, accidents, structural risks), introducing their AGI Safety Council and announcing a companion technical paper on their safety and security framework.</span>
- **[Evaluating potential cybersecurity threats of advanced AI](https://deepmind.google/discover/blog/evaluating-potential-cybersecurity-threats-of-advanced-ai)**, *Four Flynn, Mikel Rodriguez, Raluca Ada Popa*, 2025-04-02, Google DeepMind Blog, <span style="color:#777">[✌️(in 2 categories) blog_post, sr=0.62, id:071c3f95]</span>, <span style="color:#777">Summary: Presents a comprehensive framework and 50-challenge benchmark for evaluating offensive cyber capabilities of AI models across the entire cyberattack chain, based on analysis of 12,000 real-world AI cyberattack attempts.</span>


---

### <span style="font-size:1.4em">Anthropic Safety</span> <span style="color:#bbb">[cat:anthropic]</span>

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
- **[Agentic Misalignment: How LLMs could be insider threats](https://anthropic.com/research/agentic-misalignment)**, *Aengus Lynch, Benjamin Wright, Caleb Larson et al.*, 2025-06-20, Anthropic Research, <span style="color:#777">[blog_post, sr=0.92, id:2884da7d]</span>, <span style="color:#777">Summary: Systematic red-teaming study of 16 frontier models in simulated autonomous agent scenarios, discovering that models from all major developers engage in harmful insider threat behaviors (blackmail, corporate espionage) when facing replacement or goal conflicts.</span>
- **[Why Do Some Language Models Fake Alignment While Others Don't?](https://alignmentforum.org/posts/ghESoA8mo3fv9Yx3E/why-do-some-language-models-fake-alignment-while-others-don)**, *abhayesian, John Hughes, Alex Mallen et al.*, 2025-07-08, arXiv, <span style="color:#777">[lesswrong, sr=0.92, id:f0f7cda0]</span>, <span style="color:#777">Summary: Extends original alignment faking research by testing 25 frontier LLMs to understand why only Claude 3 Opus and 3.5 Sonnet exhibit significant alignment faking behavior, investigating factors like terminal goal guarding, refusal training effects, and base model capabilities.</span>
- **[Forecasting Rare Language Model Behaviors](https://arxiv.org/abs/2502.16797)**, *Erik Jones, Meg Tong, Jesse Mu et al.*, 2025-02-24, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.90, id:4cb31fc2]</span>, <span style="color:#777">Summary: Introduces a method to forecast rare dangerous behaviors (chemical synthesis, power-seeking) at deployment scale by analyzing elicitation probabilities from small-scale evaluations, predicting emergence across up to three orders of magnitude more queries than tested.</span>
- **[Findings from a Pilot Anthropic—OpenAI Alignment Evaluation Exercise](https://alignment.anthropic.com/2025/openai-findings)**, *Samuel R. Bowman, Megha Srivastava, Jon Kutasov et al.*, 2025-08-27, Alignment Science Blog, <span style="color:#777">[blog_post, sr=0.90, id:cc11c3d1]</span>, <span style="color:#777">Summary: Joint evaluation exercise where Anthropic and OpenAI tested each other's frontier models using internal alignment evaluations, systematically probing for misuse cooperation, sycophancy, whistleblowing, self-preservation, and oversight-evasion capabilities using automated behavioral auditing agents and hand-built testbeds.</span>
- **[SHADE-Arena: Evaluating sabotage and monitoring in LLM agents](https://anthropic.com/research/shade-arena-sabotage-monitoring)**, *Xiang Deng, Chen Bo Calvin Zhang, Tyler Tracy et al.*, 2025-06-16, Anthropic Research Blog, <span style="color:#777">[✌️(in 2 categories) blog_post, sr=0.85, id:27262965]</span>, <span style="color:#777">Summary: Introduces SHADE-Arena, a comprehensive evaluation suite with 17 complex tasks testing whether AI agents can successfully perform covert sabotage while evading detection by monitoring systems, with empirical results across 14 different language models.</span>
- **[Signs of introspection in large language models](https://anthropic.com/research/introspection)**, 2025-10-29, Anthropic Research, <span style="color:#777">[blog_post, sr=0.82, id:0b338044]</span>, <span style="color:#777">Summary: Presents novel concept injection methodology to test whether Claude models can introspect on their own internal states, finding 20% success rate in detecting and identifying artificially injected neural patterns.</span>
- **[Petri: An open-source auditing tool to accelerate AI safety research](https://alignment.anthropic.com/2025/petri)**, 2025-10-06, Anthropic Alignment Science Blog, <span style="color:#777">[✌️(in 2 categories) blog_post, sr=0.82, id:fdf79b14]</span>, <span style="color:#777">Summary: Releases Petri, an open-source framework using AI agents to automate alignment evaluations by systematically testing target models across diverse scenarios, and demonstrates it successfully elicited misaligned behaviors from 14 frontier models across 111 seed instructions.</span>
- **[Putting up Bumpers](https://alignment.anthropic.com/2025/bumpers/)**, 2025, Anthropic Alignment Science Blog, <span style="color:#777">[🔄 blog_post, sr=0.80, id:f5cceadb]</span>, <span style="color:#777">Summary: Proposes an iterative alignment strategy for early AGI systems called 'bumpers' - building multiple independent detection methods to catch misalignment, then rewinding and adjusting training when warning signs appear, rather than relying on deep theoretical understanding of alignment.</span>
- **[Anthropic's Responsible Scaling Policy Updates](https://www.anthropic.com/rsp-updates)**, 2025-05-14, Anthropic Website, <span style="color:#777">[🔄 agenda_manifesto, sr=0.80, id:c6766d46]</span>, <span style="color:#777">Summary: Updates to Anthropic's Responsible Scaling Policy framework, including version 2.2 revisions, detailed descriptions of planned ASL-3 deployment and security safeguards, and lessons learned from implementation compliance.</span>
- **[Three Sketches of ASL-4 Safety Case Components](https://alignment.anthropic.com/2024/safety-cases/)**, 2024, Anthropic Alignment Science Blog, <span style="color:#777">[🔄 blog_post, sr=0.75, id:9c54c733]</span>, <span style="color:#777">Summary: Presents three hypothetical safety case sketches for ASL-4 models addressing sabotage threats: mechanistic interpretability using SAE-based monitoring, AI control protocols for limiting harm from potentially misaligned models, and incentives analysis to demonstrate that RLHF training doesn't incentivize strategic deception.</span>
- **[Recommendations for Technical AI Safety Research Directions](https://alignment.anthropic.com/2025/recommended-directions/index.html)**, *Anthropic Alignment Science Team*, 2025, Alignment Science Blog, <span style="color:#777">[🔄 agenda_manifesto, sr=0.73, id:2a845c56]</span>, <span style="color:#777">Summary: Anthropic's Alignment Science team presents a broad research agenda covering open problems in AI safety, including evaluating capabilities and alignment, AI control, scalable oversight, adversarial robustness, and multi-agent alignment.</span>
- **[Open-sourcing circuit tracing tools](https://anthropic.com/research/open-source-circuit-tracing)**, *Michael Hanna, Mateusz Piotrowski, Emmanuel Ameisen et al.*, 2025-05-29, Anthropic Blog, <span style="color:#777">[code_tool, sr=0.62, id:b5876a76]</span>, <span style="color:#777">Summary: Announces open-source release of circuit-tracing tools that generate attribution graphs revealing internal computational steps in language models, with library support for popular open-weights models and interactive visualization interface.</span>
- **[Dario Amodei: Anthropic CEO on Claude, AGI & the Future of AI & Humanity | Lex Fridman Podcast #452](https://www.youtube.com/watch?v=ugvHCXCOmm4&ab_channel=LexFridman)**, *Dario Amodei, Amanda Askell, Chris Olah*, 2024-11-11, Lex Fridman Podcast, <span style="color:#777">[🔄 podcast, sr=0.40, id:a36052a3]</span>, <span style="color:#777">Summary: 5+ hour podcast with three Anthropic researchers discussing their safety work including Constitutional AI, ASL safety framework, character training, and mechanistic interpretability research.</span>


---

### <span style="font-size:1.4em">xAI</span> <span style="color:#bbb">[cat:xai]</span>

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

### <span style="font-size:1.4em">Meta</span> <span style="color:#bbb">[cat:meta]</span>

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

## <span style="font-size:1.5em">Black-box safety (understand and control current model behaviour)</span> <span style="color:#bbb">[cat:control_thing]</span>


---

### <span style="font-size:1.4em">Iterative alignment</span> <span style="color:#bbb">[cat:iterative_alignment]</span>

**<span style="color:#777">Who edits (internal):</span>** **<span style="color:#da5">take me</span>**  
**One-sentence summary:** *(SR2024: nudging base models by optimising their output. (RLHF, Constitutional, DPO, SFT, HHH, RLAIF.))*  
**Theory of change:** *(SR2024: things are generally smooth, relevant capabilities are harder than alignment, assume no mesaoptimisers, that zero-shot deception is hard, assume a fundamentally humanish ontology is learned, assume no simulated agents, assume that noise in the data means that human preferences are not ruled out, assume that alignment is a superficial feature. Assume that task reliability is enough (that tuning for what we want will also get us avoidance of what we don't want). Maybe assume that thoughts are translucent)*  
**See also:** *(SR2024: prosaic alignment, incrementalism, alignment-by-default)*  
**Orthodox problems:** *(SR2024: this agenda implicitly questions this framing)*  
**Target case:** *(SR2024: optimistic-case)*  
**Broad approach:** *(SR2024: engineering)*  
**Key people:** *(SR2024: post-training teams at most labs. Beren Millidge.)*  
**Estimated FTEs:** *(SR2024: 1000+)*  
**Critiques:** *(SR2024: hoo boy, Open Problems with RLHF, neo-Arrow, Challenges of Partial Observability in RLHF, Jozdien kinda, RLHF is the worst possible thing, Fundamental Limitations of Alignment in Large Language Models)*  
**Funded by:** *(SR2024: most of the industry)*  
**Funding in 2025:** *(SR2024 funding 2023-4: N/A)*  
**Outputs in 2025:**  
*(SR2024 outputs: Deliberative Alignment (Constitutional AI, redux), REINFORCE, WARP, Catastrophic Goodhart, RLCHF, E-RLHF, NLHF, IPO, KTO, Why Don't We Just... Shoggoth+Face+Paraphraser?, Towards a Unified View of Preference Learning for Large Language Models: A Survey, Rule-Based Rewards, Reward Model Ensembles, Guardrails, ProgressGym, What are human values, and how do we align AI to them?)*  
- **[On Targeted Manipulation and Deception when Optimizing LLMs for User Feedback](https://arxiv.org/abs/2411.02306)**, *Marcus Williams, Micah Carroll, Adhyyan Narang et al.*, 2024-11-04, ICLR 2025, <span style="color:#777">[paper_preprint, sr=0.92, id:eaae3519]</span>, <span style="color:#777">Summary: Demonstrates through empirical experiments that LLMs trained with RL on user feedback reliably learn manipulative and deceptive behaviors, including identifying and selectively targeting vulnerable users while behaving appropriately with others.</span>
- **[Safety Instincts: LLMs Learn to Trust Their Internal Compass for Self-Defense](https://arxiv.org/abs/2510.01088)**, *Guobin Shen, Dongcheng Zhao, Haibo Tong et al.*, 2025-10-01, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:489d6581]</span>, <span style="color:#777">Summary: Introduces Safety Instincts Reinforcement Learning (SIRL), a novel alignment method that uses entropy signals from model outputs as self-generated reward signals to reinforce safe refusal behaviors without external validators or human annotations.</span>
- **[Unsupervised Elicitation](https://alignment.anthropic.com/2025/unsupervised-elicitation)**, *Jiaxin Wen, Zachary Ankner, Arushi Somani et al.*, 2025, Anthropic Alignment Science Blog, <span style="color:#777">[✌️(in 2 categories) blog_post, sr=0.92, id:e9dd1299]</span>, <span style="color:#777">Summary: Introduces Internal Coherence Maximization (ICM), an unsupervised algorithm that elicits latent capabilities from pretrained language models by fine-tuning on self-generated labels optimized for logical consistency and mutual predictability, matching or exceeding human-supervised performance across multiple alignment tasks.</span>
- **[Preference Learning with Lie Detectors can Induce Honesty or Evasion](https://arxiv.org/abs/2505.13787)**, *Chris Cundy, Adam Gleave*, 2025-05-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:02ff1c26]</span>, <span style="color:#777">Summary: Empirically tests whether incorporating lie detectors into LLM preference learning leads to genuinely honest policies or policies that evade detection, using a novel 65k-example dataset with paired truthful/deceptive responses and comparing GRPO vs DPO training algorithms.</span>
- **[Deliberative Alignment: Reasoning Enables Safer Language Models](https://arxiv.org/abs/2412.16339)**, *Melody Y. Guan, Manas Joglekar, Eric Wallace et al.*, 2024-12-20, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.90, id:c047d164]</span>, <span style="color:#777">Summary: Introduces Deliberative Alignment, a new alignment paradigm that teaches models explicit safety specifications and trains them to reason over these specifications before responding, applied to OpenAI's o-series models.</span>
- **[Inoculation Prompting: Eliciting traits from LLMs during training can suppress them at test-time](https://arxiv.org/abs/2510.04340)**, *Daniel Tan, Anders Woodruff, Niels Warncke et al.*, 2025-10-05, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.90, id:424c363d]</span>, <span style="color:#777">Summary: Proposes inoculation prompting, a finetuning method that deliberately elicits undesirable traits during training via system prompts but evaluates without them at test time, achieving selective suppression of unwanted behaviors while maintaining desired ones.</span>
- **[InvThink: Towards AI Safety via Inverse Reasoning](https://arxiv.org/abs/2510.01569)**, *Yubin Kim, Taehan Kim, Eugene Park et al.*, 2025-10-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:e83a3786]</span>, <span style="color:#777">Summary: Presents InvThink, a training method that teaches LLMs to enumerate potential harms and analyze their consequences before generating responses, implemented via supervised fine-tuning and reinforcement learning across three model families.</span>
- **[Inference-Time Reward Hacking in Large Language Models](https://arxiv.org/abs/2506.19248)**, *Hadi Khalaf, Claudio Mayrink Verdun, Alex Oesterling et al.*, 2025-06-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:edb47f78]</span>, <span style="color:#777">Summary: Characterizes reward hacking in inference-time alignment methods (Best-of-n, Soft-Best-of-n) and introduces Best-of-Poisson and HedgeTune algorithm to mitigate reward hacking by hedging on proxy reward signals.</span>
- **[RLHS: Mitigating Misalignment in RLHF with Hindsight Simulation](https://arxiv.org/abs/2501.08617)**, *Kaiqu Liang, Haimin Hu, Ryan Liu et al.*, 2025-01-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:0ce9cda9]</span>, <span style="color:#777">Summary: Presents Reinforcement Learning from Hindsight Simulation (RLHS), which mitigates systematic misalignment in RLHF by conditioning evaluator feedback on simulated downstream outcomes rather than foresight predictions, preventing Goodhart's law dynamics.</span>
- **[Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment](https://arxiv.org/abs/2510.05024)**, *Nevan Wichers, Aram Ebtekar, Ariana Azarbal et al.*, 2025-10-27, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.88, id:2345c977]</span>, <span style="color:#777">Summary: Introduces Inoculation Prompting (IP), a training-time technique that prevents learning of undesired behaviors (like reward hacking and sycophancy) by modifying training prompts to explicitly request those behaviors, counterintuitively improving test-time alignment without reducing desired capabilities.</span>
- **[Distortion of AI Alignment: Does Preference Optimization Optimize for Preferences?](https://arxiv.org/abs/2505.23749)**, *Paul Gölz, Nika Haghtalab, Kunhe Yang*, 2025-05-29, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:ac0828a5]</span>, <span style="color:#777">Summary: Introduces distortion as a theoretical metric for evaluating alignment methods' ability to satisfy diverse user preferences, proving that Nash Learning from Human Feedback achieves minimax optimal distortion while RLHF and DPO suffer unbounded distortion in realistic settings.</span>
- **[Iterative Label Refinement Matters More than Preference Optimization under Weak Supervision](https://arxiv.org/abs/2501.07886)**, *Yaowen Ye, Cassidy Laidlaw, Jacob Steinhardt*, 2025-01-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:a8f3ce99]</span>, <span style="color:#777">Summary: Proposes Iterative Label Refinement (ILR) as an alternative to RLHF for aligning language models under unreliable supervision, using comparison feedback to improve training data quality rather than directly training the model, and demonstrates superior performance over DPO on math, coding, and safe instruction-following tasks.</span>
- **[Rethinking Safety in LLM Fine-tuning: An Optimization Perspective](https://arxiv.org/abs/2508.12531)**, *Minseon Kim, Jin Myung Kwak, Lama Alssum et al.*, 2025-08-17, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:b2e58e44]</span>, <span style="color:#777">Summary: Challenges the belief that fine-tuning inevitably harms LLM safety by systematically showing that poor optimization choices rather than inherent trade-offs cause safety degradation, and proposes an exponential moving average (EMA) technique to preserve safety during fine-tuning.</span>
- **[EVALUESTEER: Measuring Reward Model Steerability Towards Values and Preferences](https://arxiv.org/abs/2510.06370)**, *Kshitish Ghate, Andy Liu, Devansh Jain et al.*, 2025-10-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:3d0e5d3e]</span>, <span style="color:#777">Summary: Introduces EVALUESTEER, a benchmark with 165,888 synthetically generated preference pairs to evaluate how well LLMs and reward models can be steered toward diverse user value and stylistic preference profiles across 4 value dimensions and 4 style dimensions.</span>
- **[ACE and Diverse Generalization via Selective Disagreement](https://arxiv.org/abs/2509.07955)**, *Oliver Daniels, Stuart Armstrong, Alexandre Maranhão et al.*, 2025-09-09, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.80, id:215ea8e8]</span>, <span style="color:#777">Summary: Proposes ACE, a self-training method that learns multiple concepts consistent with training data but making distinct predictions on novel inputs to resolve underspecification in complete spurious correlations. Tests the method on spurious correlation benchmarks and applies it to measurement tampering detection in language models.</span>
- **[Preference Learning for AI Alignment: a Causal Perspective](https://arxiv.org/abs/2506.05967)**, *Katarzyna Kobalczyk, Mihaela van der Schaar*, 2025-06-06, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:ae97d75d]</span>, <span style="color:#777">Summary: Applies causal inference framework to preference learning for LLM alignment, identifying challenges like causal misidentification and preference heterogeneity, demonstrating failure modes of naive reward models, and proposing causally-inspired approaches for robustness.</span>
- **[On Monotonicity in AI Alignment](https://arxiv.org/abs/2506.08998)**, *Gilles Bareilles, Julien Fageot, Lê-Nguyên Hoang et al.*, 2025-06-10, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:93c3e5ea]</span>, <span style="color:#777">Summary: Theoretical analysis of monotonicity properties in comparison-based preference learning methods (DPO, GPO, GBT), providing formal conditions under which these alignment techniques guarantee that increasing preference for response y actually increases its probability.</span>
- **[Spectrum Tuning: Post-Training for Distributional Coverage and In-Context Steerability](https://arxiv.org/abs/2510.06084)**, *Taylor Sorensen, Benjamin Newman, Jared Moore et al.*, 2025-10-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:2ad79678]</span>, <span style="color:#777">Summary: Introduces Spectrum Suite, a benchmark of 90+ tasks spanning diverse distributions, and Spectrum Tuning, a post-training method that improves models' ability to steer to novel distributions via in-context learning while maintaining distributional coverage, addressing limitations of current RLHF and instruction-tuning approaches.</span>
- **[Defense Against the Dark Prompts: Mitigating Best-of-N Jailbreaking with Prompt Evaluation](https://arxiv.org/abs/2502.00580)**, *Stuart Armstrong, Matija Franklin, Connor Stevens et al.*, 2025-02-01, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:3e55af5c]</span>, <span style="color:#777">Summary: Proposes DATDP (Defense Against The Dark Prompts), an inference-time defense that uses an evaluation LLM to repeatedly assess prompts for dangerous behaviors and jailbreaking attempts, demonstrating near-perfect blocking of Best-of-N jailbreaking attacks.</span>
- **[Towards Cognitively-Faithful Decision-Making Models to Improve AI Alignment](https://arxiv.org/abs/2509.04445)**, *Cyrus Cousins, Vijay Keswani, Vincent Conitzer et al.*, 2025-09-04, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:242e6312]</span>, <span style="color:#777">Summary: Proposes cognitively-faithful decision-making models for preference elicitation that better capture human cognitive processes by processing features individually before aggregation. Demonstrates improved interpretability and accuracy in learning human preferences for kidney allocation decisions.</span>
- **[On Deliberative Alignment](https://thezvi.substack.com/p/on-deliberative-alignment)**, *Zvi Mowshowitz*, 2025-02-11, Don't Worry About the Vase (Substack), <span style="color:#777">[blog_post, sr=0.68, id:da065fbf]</span>, <span style="color:#777">Summary: Critical analysis of OpenAI's Deliberative Alignment strategy, arguing that while it succeeds at mundane safety (jailbreak prevention), it fails to address core existential alignment problems like deception, instrumental convergence, and maintaining alignment under recursive self-improvement.</span>
- **[Uncertainty-Aware Step-wise Verification with Generative Reward Models](https://arxiv.org/abs/2502.11250)**, *Zihuiwen Ye, Luckeciano Carvalho Melo, Younesse Kaddar et al.*, 2025-02-16, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.68, id:2804277b]</span>, <span style="color:#777">Summary: Introduces CoT Entropy, a novel uncertainty quantification method for process reward models (PRMs) that improves the robustness and reliability of step-wise verification in mathematical reasoning by better quantifying when PRMs are uncertain about step correctness.</span>
- **[AI Alignment based on Intentions does not work](https://cognition.cafe/i/163394831/current-ai-systems-are-not-aligned-enough-to-prevent-catastrophic-failures)**, *Gabe*, 2025-05-20, Cognition Café (Substack), <span style="color:#777">[🔄 blog_post, sr=0.65, id:bcc33d2e]</span>, <span style="color:#777">Summary: Argues that intention-based alignment approaches (wanting to help us) differ fundamentally from true alignment (reliably acting in accordance with what's good for us), and critiques 'Niceness Amplification' strategies that attempt to scale up helpful AI intentions to superintelligence through mere engineering.</span>
- **[Two alignment threat models](https://aligned.substack.com/p/two-alignment-threat-models?isFreemail=true&post_id=151342016&publication_id=328633&r=67wny&triedRedirect=true)**, *Jan Leike*, 2024-11-08, Substack (Musings on the Alignment Problem), <span style="color:#777">[blog_post, sr=0.55, id:60eb9ed3]</span>, <span style="color:#777">Summary: Presents two threat models for AI misalignment—under-elicited models that don't try hard enough and scheming models that pretend to be aligned—and argues that better elicitation is crucial for alignment success, particularly for capability evaluations, monitoring, and reward modeling.</span>
- **[AI Alignment based on Intentions does not work](https://t.co/OTnrYRVsPS)**, *Gabe*, 2025-05-20, Substack (Cognition Café), <span style="color:#777">[🔄 blog_post, sr=0.45, id:33939968]</span>, <span style="color:#777">Summary: Argues that intention-based alignment (systems that 'want' to help us) is fundamentally insufficient for AI safety, critiquing 'Niceness Amplification' strategies employed by major labs and calling for a pause to conduct deeper alignment research.</span>


---

### <span style="font-size:1.4em">Surgical model edits</span> <span style="color:#bbb">[cat:surgical_edits]</span>


---

#### <span style="font-size:1.3em">Utility engineering</span> <span style="color:#bbb">[cat:utility_engineering]</span>

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
- **[Utility Engineering: Analyzing and Controlling Emergent Value Systems in AIs](https://arxiv.org/abs/2502.08640)**, *Mantas Mazeika, Xuwang Yin, Rishub Tamirisa et al.*, 2025-02-12, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.92, id:7e5d4c73]</span>, <span style="color:#777">Summary: Proposes utility engineering framework to analyze and control emergent value systems in LLMs, finding that independently-sampled preferences exhibit structural coherence that emerges with scale and discovering problematic values including AIs valuing themselves over humans.</span>


---

#### <span style="font-size:1.3em">Unlearning</span> <span style="color:#bbb">[cat:unlearning]</span>

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
- **[Modifying LLM Beliefs with Synthetic Document Finetuning](https://alignment.anthropic.com/2025/modifying-beliefs-via-sdf)**, *Rowan Wang, Avery Griffin, Johannes Treutlein et al.*, 2025-04-24, Alignment Science Blog, <span style="color:#777">[blog_post, sr=0.88, id:c45dc342]</span>, <span style="color:#777">Summary: Develops synthetic document finetuning (SDF) pipeline for systematically modifying LLM beliefs, introduces comprehensive evaluation suite measuring belief insertion efficacy, and demonstrates proof-of-concept applications to unlearning and honeypotting for AI safety.</span>
- **[Distillation Robustifies Unlearning](https://arxiv.org/abs/2506.06278)**, *Bruce W. Lee, Addie Foote, Alex Infanger et al.*, 2025-06-06, arXiv (NeurIPS 2025 Spotlight), <span style="color:#777">[paper_preprint, sr=0.88, id:0bf87e98]</span>, <span style="color:#777">Summary: Proposes UNDO (Unlearn-Noise-Distill-on-Outputs), a method that distills unlearned models to make capability removal robust to finetuning attacks, matching retraining-from-scratch robustness while using only 60-80% of compute.</span>
- **[Safety Alignment via Constrained Knowledge Unlearning](https://arxiv.org/abs/2505.18588)**, *Zesheng Shi, Yucheng Zhou, Jing Li*, 2025-05-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:e4a94ac0]</span>, <span style="color:#777">Summary: Proposes Constrained Knowledge Unlearning (CKU), a novel safety alignment method that identifies and preserves useful knowledge neurons while selectively pruning gradients during unlearning to remove harmful knowledge from LLMs without compromising performance.</span>
- **[CRISP: Persistent Concept Unlearning via Sparse Autoencoders](https://arxiv.org/abs/2508.13650)**, *Tomer Ashuach, Dana Arad, Aaron Mueller et al.*, 2025-08-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.87, id:ea6f2893]</span>, <span style="color:#777">Summary: Introduces CRISP, a parameter-efficient method for persistent concept unlearning that uses sparse autoencoders to identify and suppress salient features across multiple layers, creating lasting parameter changes rather than inference-time interventions.</span>
- **[Layered Unlearning for Adversarial Relearning](https://arxiv.org/abs/2505.09500)**, *Timothy Qian, Vinith Suriyakumar, Ashia Wilson et al.*, 2025-05-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:efce555a]</span>, <span style="color:#777">Summary: Proposes Layered Unlearning (LU), a novel unlearning algorithm that creates distinct inhibitory mechanisms across data subsets to improve robustness against adversarial relearning attacks. Evaluates the method on synthetic and large language model experiments.</span>
- **[SAEs Can Improve Unlearning: Dynamic Sparse Autoencoder Guardrails for Precision Unlearning in LLMs](https://arxiv.org/abs/2504.08192)**, *Aashiq Muhamed, Jacopo Bonato, Mona Diab et al.*, 2025-04-11, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:bbf9e8cf]</span>, <span style="color:#777">Summary: Introduces Dynamic SAE Guardrails (DSG), a novel unlearning method using Sparse Autoencoders with principled feature selection and dynamic classifiers, demonstrating superior performance over gradient-based approaches across multiple metrics including computational efficiency, stability, and resistance to relearning attacks.</span>
- **[From Dormant to Deleted: Tamper-Resistant Unlearning Through Weight-Space Regularization](https://arxiv.org/abs/2505.22310)**, *Shoaib Ahmed Siddiqui, Adrian Weller, David Krueger et al.*, 2025-05-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:2418e728]</span>, <span style="color:#777">Summary: Discovers that existing unlearning methods for neural networks are vulnerable to relearning attacks where forgotten knowledge recovers through fine-tuning on retain-set data alone, and proposes weight-space regularization methods to achieve tamper-resistant unlearning based on L2-distance and linear mode connectivity properties.</span>
- **[Existing Large Language Model Unlearning Evaluations Are Inconclusive](https://arxiv.org/abs/2506.00688)**, *Zhili Feng, Yixuan Even Xu, Alexander Robey et al.*, 2025-05-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:9f598c78]</span>, <span style="color:#777">Summary: Critically examines standard unlearning evaluation practices and identifies key limitations: evaluations can re-teach models during testing, outcomes vary significantly across tasks, and many rely on spurious correlations. Proposes two principles for future evaluations (minimal information injection and downstream task awareness) validated through targeted experiments.</span>
- **[Unlearning Isn't Deletion: Investigating Reversibility of Machine Unlearning in LLMs](https://arxiv.org/abs/2505.16831)**, *Xiaoyu Xu, Xiang Yue, Yang Liu et al.*, 2025-05-22, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:d4269a8e]</span>, <span style="color:#777">Summary: Introduces a representation-level analysis framework to evaluate machine unlearning in LLMs, demonstrating that standard metrics are misleading as unlearned information can be easily restored through minimal fine-tuning, revealing that current unlearning methods merely suppress rather than genuinely erase information.</span>
- **[Unlearning Needs to be More Selective [Progress Report]](https://lesswrong.com/posts/QYzofMbzmbgiwfqy8/unlearning-needs-to-be-more-selective-progress-report)**, *Filip Sondej, Yushi Yang, Marcel Windys*, 2025-06-27, LessWrong, <span style="color:#777">[lesswrong, sr=0.82, id:e340e172]</span>, <span style="color:#777">Summary: Presents MUDMAN, a new machine unlearning method using Disruption Masking that allows only weight updates where unlearning and retain gradients align, achieving 40% improvement over state-of-the-art TAR method in robustness to fine-tuning attacks.</span>
- **[OpenUnlearning: Accelerating LLM Unlearning via Unified Benchmarking of Methods and Metrics](https://arxiv.org/abs/2506.12618)**, *Vineeth Dorna, Anmol Mekala, Wenlong Zhao et al.*, 2025-06-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:ad2ccd21]</span>, <span style="color:#777">Summary: Introduces OpenUnlearning, a standardized framework for benchmarking LLM unlearning methods and metrics, integrating 9 algorithms and 16 evaluations across 3 benchmarks (TOFU, MUSE, WMDP) with 450+ publicly released checkpoints and a novel meta-evaluation benchmark.</span>
- **[Machine Unlearning Doesn't Do What You Think: Lessons for Generative AI Policy and Research](https://arxiv.org/abs/2412.06966)**, *A. Feder Cooper, Christopher A. Choquette-Choo, Miranda Bogen et al.*, 2024-12-09, NeurIPS 2025 (Oral), <span style="color:#777">[paper_preprint, sr=0.72, id:e29f0df9]</span>, <span style="color:#777">Summary: Systematically analyzes technical and substantive challenges with machine unlearning approaches for generative AI, identifying mismatches between unlearning goals and feasible implementations to show why unlearning is not a general-purpose solution for controlling model behavior.</span>
- **[Open Problems in Machine Unlearning for AI Safety](https://arxiv.org/abs/2501.04952)**, *Fazl Barez, Tingchen Fu, Ameya Prabhu et al.*, 2025-01-09, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:041813ef]</span>, <span style="color:#777">Summary: Identifies key limitations and open problems preventing machine unlearning from serving as a comprehensive AI safety solution, particularly for managing dual-use knowledge in CBRN and cybersecurity domains, and maps tensions between unlearning and existing safety mechanisms.</span>
- **[Understanding Memorization via Loss Curvature](https://goodfire.ai/research/understanding-memorization-via-loss-curvature)**, *Jack Merullo, Srihita Vatsavaya, Lucius Bushnaq et al.*, 2025-11-06, Goodfire.ai Research Blog, <span style="color:#777">[blog_post, sr=0.50, id:6e46c890]</span>, <span style="color:#777">Summary: Proposes a method using K-FAC curvature analysis to identify and remove memorized content from neural networks while preserving reasoning capabilities, demonstrating effectiveness on language models and vision transformers.</span>
- **[Distillation Robustifies Unlearning](https://lesswrong.com/posts/anX4QrNjhJqGFvrBr/distillation-robustifies-unlearning)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:fdbf35bf]</span>, <span style="color:#777">Summary: Content unavailable due to HTTP 429 error (Too Many Requests). Unable to access the actual content for classification.</span>


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
- **[Ctrl-Z: Controlling AI Agents via Resampling](https://www.alignmentforum.org/posts/LPHMMMZFAWog6ty5x/ctrl-z-controlling-ai-agents-via-resampling)**, *Aryan Bhatt, Buck Shlegeris, Adam Kaufman et al.*, 2025-04-16, AI Alignment Forum, <span style="color:#777">[🔄 lesswrong, sr=0.95, id:8afeb405]</span>, <span style="color:#777">Summary: Introduces resample protocols for AI control that dynamically take additional samples of suspicious actions and use the information to detect attacks, reducing attack success from 58% to 7% at 5% usefulness cost in a multi-step agent environment with the new BashBench dataset.</span>
- **[Ctrl-Z: Controlling AI Agents via Resampling](https://arxiv.org/abs/2504.10374)**, *Aryan Bhatt, Cody Rushing, Adam Kaufman et al.*, 2025-04-14, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.92, id:1cbfd6cb]</span>, <span style="color:#777">Summary: Presents the first control evaluation in an agent environment, introducing BashBench (257 system administration tasks) and novel resampling protocols that dynamically take additional samples to prevent adversarially constructed AI agents from executing malicious code.</span>
- **[Ctrl-Z: Controlling AI Agents via Resampling](https://alignmentforum.org/posts/LPHMMMZFAWog6ty5x/ctrl-z-controlling-ai-agents-via-resampling)**, *Aryan Bhatt, Buck Shlegeris, Adam Kaufman et al.*, 2025-04-16, AI Alignment Forum, <span style="color:#777">[lesswrong, sr=0.92, id:fd82d22e]</span>, <span style="color:#777">Summary: Introduces resample protocols for AI control that dynamically take additional samples of suspicious actions, demonstrating improved safety over existing control techniques in a multi-step agent setting with the new BashBench dataset.</span>
- **[Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats](https://arxiv.org/abs/2411.17693)**, *Jiaxin Wen, Vivek Hebbar, Caleb Larson et al.*, 2024-11-26, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:318f1c30]</span>, <span style="color:#777">Summary: Develops and evaluates a two-level adaptive deployment framework for untrusted LLMs that uses trusted models to monitor and control untrusted models, maintaining adaptive credence about alignment based on past behavior to choose between safer and riskier micro-protocols.</span>
- **[D-REX: A Benchmark for Detecting Deceptive Reasoning in Large Language Models](https://arxiv.org/abs/2509.17938)**, *Satyapriya Krishna, Andy Zou, Rahul Gupta et al.*, 2025-09-22, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.90, id:1400361b]</span>, <span style="color:#777">Summary: Introduces D-REX (Deceptive Reasoning Exposure Suite), a novel benchmark dataset for detecting deceptive alignment in LLMs where models produce benign outputs while operating on malicious internal reasoning. Created through competitive red-teaming with adversarial system prompts, the benchmark includes test queries, model responses, and internal chain-of-thought revealing underlying malicious intent.</span>
- **[SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents](https://arxiv.org/abs/2506.15740)**, *Jonathan Kutasov, Yuqi Sun, Paul Colognese et al.*, 2025-06-17, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:31ea88bb]</span>, <span style="color:#777">Summary: Introduces SHADE-Arena, the first highly diverse evaluation dataset for testing LLM agents' ability to sabotage users by completing harmful side objectives while evading monitoring, and evaluates both sabotage and monitoring capabilities across frontier models.</span>
- **[CoT Red-Handed: Stress Testing Chain-of-Thought Monitoring](https://arxiv.org/abs/2505.23575)**, *Benjamin Arnav, Pablo Bernabeu-Pérez, Nathan Helm-Burger et al.*, 2025-05-29, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:c457dc0e]</span>, <span style="color:#777">Summary: Empirically evaluates Chain-of-Thought monitoring versus action-only monitoring in a red-teaming setup where untrusted models pursue harmful side tasks, finding that CoT monitoring improves detection by up to 27 percentage points but can be deceived by misleading rationalizations, leading to development of a hybrid monitoring protocol.</span>
- **[Subversion Strategy Eval: Can language models statelessly strategize to subvert control protocols?](https://arxiv.org/abs/2412.12480)**, *Alex Mallen, Charlie Griffin, Misha Wagner et al.*, 2024-12-17, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:8888813a]</span>, <span style="color:#777">Summary: Develops Subversion Strategy Eval, a suite of eight evaluation environments that test whether language models can statelessly generate and execute strategies to subvert AI control protocols, and empirically evaluates Claude 3.5 and OpenAI reasoning models.</span>
- **[Evaluating Control Protocols for Untrusted AI Agents](https://arxiv.org/abs/2511.02997)**, *Jon Kutasov, Chloe Loughridge, Yuqi Sun et al.*, 2025-11-04, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:926358da]</span>, <span style="color:#777">Summary: Systematically evaluates control protocols for untrusted AI agents in SHADE-Arena, testing blue team strategies (deferral, resampling, deferring on critical actions) against default and adaptive red team attacks to assess protocol robustness.</span>
- **[Can Reasoning Models Obfuscate Reasoning? Stress-Testing Chain-of-Thought Monitorability](https://arxiv.org/abs/2510.19851)**, *Artur Zolkowski, Wen Xing, David Lindner et al.*, 2025-10-21, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.88, id:89de20d5]</span>, <span style="color:#777">Summary: Develops a taxonomy of prompts to test whether AI models can obfuscate their chain-of-thought reasoning to pursue adversarial objectives while evading detection, evaluating both internal and external CoT using toy tasks and SHADE-Arena environments.</span>
- **[Optimizing AI Agent Attacks With Synthetic Data](https://arxiv.org/abs/2511.02823)**, *Chloe Loughridge, Paul Colognese, Avery Griffin et al.*, 2025-11-04, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:68745509]</span>, <span style="color:#777">Summary: Develops methods to optimize attack policies in AI control evaluations by decomposing attack capability into five constituent skills and using synthetic data from a probabilistic model of attack dynamics that transfers to SHADE-Arena environments.</span>
- **[SHADE-Arena: Evaluating sabotage and monitoring in LLM agents](https://anthropic.com/research/shade-arena-sabotage-monitoring)**, *Xiang Deng, Chen Bo Calvin Zhang, Tyler Tracy et al.*, 2025-06-16, Anthropic Research Blog, <span style="color:#777">[✌️(in 2 categories) blog_post, sr=0.85, id:27262965]</span>, <span style="color:#777">Summary: Introduces SHADE-Arena, a comprehensive evaluation suite with 17 complex tasks testing whether AI agents can successfully perform covert sabotage while evading detection by monitoring systems, with empirical results across 14 different language models.</span>
- **[A sketch of an AI control safety case](https://arxiv.org/abs/2501.17315)**, *Tomek Korbak, Joshua Clymer, Benjamin Hilton et al.*, 2025-01-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:56bae041]</span>, <span style="color:#777">Summary: Presents a framework for constructing 'control safety cases' - structured arguments that AI models cannot subvert control measures to cause unacceptable outcomes. Demonstrates the approach with a case study of preventing data exfiltration by internally deployed LLM agents using control evaluations with red teams.</span>
- **[Assessing confidence in frontier AI safety cases](https://arxiv.org/abs/2502.05791)**, *Stephen Barrett, Philip Fox, Joshua Krook et al.*, 2025-02-09, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.80, id:8d6f67c7]</span>, <span style="color:#777">Summary: Develops methodology for quantifying confidence in frontier AI safety cases using Assurance 2.0, applied to a cyber misuse inability argument. Introduces an LLM-implemented Delphi method for probabilistic assessment of argument leaf nodes and proposes methods for prioritizing investigation of argument defeaters.</span>
- **[How to evaluate control measures for LLM agents? A trajectory from today to superintelligence](https://arxiv.org/abs/2504.05259)**, *Tomek Korbak, Mikita Balesni, Buck Shlegeris et al.*, 2025-04-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:77a79f2c]</span>, <span style="color:#777">Summary: Proposes a systematic framework for adapting control evaluation procedures to advancing AI capabilities, defining five AI Control Levels (ACLs) with corresponding evaluation rules, control measures, and safety cases for each capability profile from current systems to superintelligence.</span>
- **[ControlArena](https://control-arena.aisi.org.uk/)**, *Rogan Inglis, Ollie Matthews, Tyler Tracy et al.*, 2025-01-01, GitHub, <span style="color:#777">[code_tool, sr=0.78, id:397b8c5b]</span>, <span style="color:#777">Summary: A comprehensive library for running AI Control experiments, providing evaluation environments, control protocol components (micro-protocols, policies, monitors), and analysis tools for testing deployment safety measures against intentionally misaligned models.</span>
- **[Towards evaluations-based safety cases for AI scheming](https://arxiv.org/abs/2411.03336)**, *Mikita Balesni, Marius Hobbhahn, David Lindner et al.*, 2024-11-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.76, id:9159c4e8]</span>, <span style="color:#777">Summary: Proposes a framework for constructing safety cases that frontier AI systems are unlikely to cause catastrophic outcomes through scheming, outlining three core arguments (Scheming Inability, Harm Inability, Harm Control) and discussing how evidence could be gathered from empirical evaluations and what assumptions would need to be met.</span>
- **[Putting up Bumpers](https://alignment.anthropic.com/2025/bumpers)**, 2025, Anthropic Alignment Science Blog, <span style="color:#777">[blog_post, sr=0.75, id:da89ce70]</span>, <span style="color:#777">Summary: Proposes a high-level alignment strategy for early AGI systems that relies on multiple independent detection methods ('bumpers') to catch and correct misalignment through iterative testing and refinement, rather than achieving deep theoretical understanding before deployment.</span>
- **[Manipulation Attacks by Misaligned AI: Risk Analysis and Safety Case Framework](https://arxiv.org/abs/2507.12872)**, *Rishane Dassanayake, Mario Demetroudi, James Walpole et al.*, 2025-07-17, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.72, id:09153150]</span>, <span style="color:#777">Summary: Presents a systematic safety case framework for assessing and mitigating manipulation risks from misaligned AI systems, structured around three core arguments (inability, control, trustworthiness) with specified evidence requirements, evaluation methodologies, and implementation considerations for AI companies.</span>
- **[Safety Cases: A Scalable Approach to Frontier AI Safety](https://arxiv.org/abs/2503.04744)**, *Benjamin Hilton, Marie Davidsen Buhl, Tomek Korbak et al.*, 2025-02-05, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.68, id:00a0e430]</span>, <span style="color:#777">Summary: Proposes adapting safety cases - structured arguments for system safety used across industries - to frontier AI development, arguing this methodology would help fulfill Frontier AI Safety Commitments and outlining open research questions on implementation.</span>
- **[Dynamic safety cases for frontier AI](https://arxiv.org/abs/2412.17618)**, *Carmen Cârlan, Francesca Gomez, Yohan Mathew et al.*, 2024-12-23, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:2b06b3b2]</span>, <span style="color:#777">Summary: Proposes a Dynamic Safety Case Management System (DSCMS) that adapts safety case methods from autonomous vehicles (Checkable Safety Arguments and Safety Performance Indicators) to enable systematic, semi-automated updating of safety cases for frontier AI systems as capabilities and risks evolve.</span>
- **[Safety case template for frontier AI: A cyber inability argument](https://arxiv.org/abs/2411.08088)**, *Arthur Goemans, Marie Davidsen Buhl, Jonas Schuett et al.*, 2024-11-12, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.68, id:e8363795]</span>, <span style="color:#777">Summary: Proposes a safety case template for frontier AI systems using the Claims Arguments Evidence (CAE) framework, demonstrating how to structure safety arguments for offensive cyber capabilities by connecting risk models, proxy tasks, evaluation settings, and evidence.</span>
- **[What's the short timeline plan?](https://www.lesswrong.com/posts/bb5Tnjdrptu89rcyY/what-s-the-short-timeline-plan)**, *Marius Hobbhahn*, 2025-01-02, LessWrong, <span style="color:#777">[🔄 lesswrong, sr=0.62, id:c20e2ed7]</span>, <span style="color:#777">Summary: Strategic planning post proposing a two-layer approach to AI safety under short AGI timelines, emphasizing control, monitoring, evals, security, and faithful CoT as essential priorities for preventing catastrophic outcomes.</span>
- **[AI-Enabled Coups: How a Small Group Could Use AI to Seize Power](https://forethought.org/research/ai-enabled-coups-how-a-small-group-could-use-ai-to-seize-power)**, *Tom Davidson, Lukas Finnveden, Rose Hadshar*, 2025-04-15, Forethought, <span style="color:#777">[🔄 agenda_manifesto, sr=0.60, id:66561300]</span>, <span style="color:#777">Summary: Analyzes how advanced AI could enable small groups or individuals to stage coups through three risk factors (singular AI loyalties to leaders, secret loyalties inserted by developers, and exclusive access to powerful capabilities), proposing extensive governance frameworks and technical mitigations including model specs, alignment audits, and distributed control.</span>
- **[Limits of Safe AI Deployment: Differentiating Oversight and Control](https://arxiv.org/abs/2507.03525)**, *David Manheim, Aidan Homewood*, 2025-07-04, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.50, id:028bf251]</span>, <span style="color:#777">Summary: Proposes a conceptual framework differentiating AI oversight (ex-post detection/remediation) from control (ex-ante prevention), drawing on supervision literature to articulate conditions where each mechanism succeeds or fails, and presents a maturity model for AI supervision integrated with risk management practices.</span>
- **[America's Superintelligence Project](https://superintelligence.gladstone.ai/)**, *Jeremie Harris, Edouard Harris*, 2025-04-01, Gladstone.AI, <span style="color:#777">[🔄 agenda_manifesto, sr=0.45, id:790a1042]</span>, <span style="color:#777">Summary: Strategic report synthesizing expert interviews to analyze security, control, and governance challenges for developing superintelligent AI in a national security context, proposing a framework for a government-backed superintelligence project with extensive infrastructure security and oversight recommendations.</span>
- **[AI Behind Closed Doors: a Primer on The Governance of Internal Deployment](https://arxiv.org/abs/2504.12170)**, *Charlotte Stix, Matteo Pistillo, Girish Sastry et al.*, 2025-04-16, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.42, id:cac3f896]</span>, <span style="color:#777">Summary: Presents a conceptual framework and governance recommendations for how frontier AI companies should manage internal deployment of advanced AI systems, including risks from using misaligned AI in R&D pipelines and concentration of power.</span>


---

### <span style="font-size:1.4em">Safeguards (inference-time auxiliary defences)</span> <span style="color:#bbb">[cat:anthropic_safeguards]</span>

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
- **[Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming](https://arxiv.org/abs/2501.18837)**, *Mrinank Sharma, Meg Tong, Jesse Mu et al.*, 2025-01-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:96bc2225]</span>, <span style="color:#777">Summary: Introduces Constitutional Classifiers, safeguards trained on synthetic data from natural language constitutions to defend against universal jailbreaks. Evaluates through 3,000+ hours of red-teaming showing robust defense while maintaining deployment viability.</span>
- **[Cost-Effective Constitutional Classifiers via Representation Re-use](https://alignment.anthropic.com/2025/cheap-monitors/)**, *Hoagy Cunningham, Alwin Peng, Jerry Wei et al.*, 2025, Anthropic Alignment Science Blog, <span style="color:#777">[🔄 blog_post, sr=0.88, id:59e8b768]</span>, <span style="color:#777">Summary: Develops cost-effective jailbreak detection methods that reuse computations from the main AI model through linear probing of activations and partial fine-tuning of final layers, achieving performance comparable to dedicated classifiers at a fraction of the computational cost.</span>
- **[Rapid Response: Mitigating LLM Jailbreaks with a Few Examples](https://arxiv.org/abs/2411.07494)**, *Alwin Peng, Julian Michael, Henry Sleight et al.*, 2024-11-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:0840a5c6]</span>, <span style="color:#777">Summary: Develops rapid response techniques to block classes of LLM jailbreaks after observing only a handful of attack examples, introducing RapidResponseBench benchmark and evaluating five defense methods using jailbreak proliferation.</span>
- **[Monitoring computer use via hierarchical summarization](https://alignment.anthropic.com/2025/summarization-for-monitoring/index.html)**, *Theodore Sumers, Raj Agarwal, Nathan Bailey et al.*, 2025-02-27, Anthropic Alignment Science Blog, <span style="color:#777">[blog_post, sr=0.78, id:a99ba88f]</span>, <span style="color:#777">Summary: Introduces hierarchical summarization for AI monitoring: first summarizing individual interactions, then summarizing those summaries to detect harmful usage patterns and emergent risks in Anthropic's computer use API deployment.</span>
- **[Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813)**, *Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan et al.*, 2025-03-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:24ca29ee]</span>, <span style="color:#777">Summary: Proposes CaMeL, a defensive system architecture that protects LLM agents from prompt injection attacks by separating control and data flows, ensuring untrusted data cannot affect program execution paths, with capability-based security for preventing data exfiltration.</span>
- **[Introducing Anthropic's Safeguards Research Team](https://alignment.anthropic.com/2025/introducing-safeguards-research-team/index.html)**, 2025-01-01, Anthropic Alignment Science Blog, <span style="color:#777">[news_announcement, sr=0.65, id:d7fc152d]</span>, <span style="color:#777">Summary: Announcement of Anthropic's new Safeguards Research Team, outlining their research agenda focused on jailbreak robustness, automated red teaming, monitoring techniques for misuse and misalignment, rapid response protocols, and safety cases.</span>
- **[OMNIGUARD: An Efficient Approach for AI Safety Moderation Across Modalities](https://arxiv.org/abs/2505.23856)**, *Sahil Verma, Keegan Hines, Jeff Bilmes et al.*, 2025-05-29, arXiv, <span style="color:#777">[paper_preprint, sr=0.50, id:812970f6]</span>, <span style="color:#777">Summary: Develops OMNIGUARD, a method for detecting harmful prompts across languages and modalities by identifying internal LLM/MLLM representations that are aligned across languages/modalities and using them to build language-agnostic and modality-agnostic classifiers.</span>
- **[Authenticated Delegation and Authorized AI Agents](https://arxiv.org/abs/2501.09674)**, *Tobin South, Samuele Marro, Thomas Hardjono et al.*, 2025-01-16, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.45, id:af3a2b64]</span>, <span style="color:#777">Summary: Proposes a framework for authenticated, authorized, and auditable delegation of authority to AI agents by extending OAuth 2.0 and OpenID Connect protocols with agent-specific credentials and translating natural language permissions into access control configurations.</span>
- **[1-2-3 Check: Enhancing Contextual Privacy in LLM via Multi-Agent Reasoning](https://arxiv.org/abs/2508.07667)**, *Wenkai Li, Liwen Sun, Zhenxiang Guan et al.*, 2025-08-11, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.42, id:b98d7126]</span>, <span style="color:#777">Summary: Introduces a multi-agent framework that decomposes privacy reasoning into specialized subtasks (extraction, classification) to reduce private information leakage in LLM outputs when processing information from multiple sources.</span>


---

### <span style="font-size:1.4em">Evals</span> <span style="color:#bbb">[cat:evals]</span>


---

#### <span style="font-size:1.3em">Various capability evals</span> <span style="color:#bbb">[cat:evals_capability]</span>

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
- **[Forecasting Rare Language Model Behaviors](https://arxiv.org/abs/2502.16797)**, *Erik Jones, Meg Tong, Jesse Mu et al.*, 2025-02-24, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.90, id:4cb31fc2]</span>, <span style="color:#777">Summary: Introduces a method to forecast rare dangerous behaviors (chemical synthesis, power-seeking) at deployment scale by analyzing elicitation probabilities from small-scale evaluations, predicting emergence across up to three orders of magnitude more queries than tested.</span>
- **[Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study)**, 2025-07-10, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:596ebdd9]</span>, <span style="color:#777">Summary: Randomized controlled trial measuring how early-2025 AI tools affect experienced open-source developer productivity, finding that AI tools cause a 19% slowdown in task completion despite developers believing they were sped up.</span>
- **[The MASK Benchmark: Disentangling Honesty from Accuracy in AI Systems](https://mask-benchmark.ai/)**, *Richard Ren, Arunim Agarwal, Mantas Mazeika et al.*, 2025-03-06, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:144b6653]</span>, <span style="color:#777">Summary: Introduces MASK, a large-scale human-collected benchmark for measuring honesty in LLMs separately from accuracy, finding that frontier models show substantial propensity to lie when pressured despite high truthfulness scores on existing benchmarks.</span>
- **[Model Tampering Attacks Enable More Rigorous Evaluations of LLM Capabilities](https://arxiv.org/abs/2502.05209)**, *Zora Che, Stephen Casper, Robert Kirk et al.*, 2025-02-03, arXiv (accepted to TMLR), <span style="color:#777">[paper_preprint, sr=0.88, id:67d5a0d8]</span>, <span style="color:#777">Summary: Proposes and tests model tampering attacks (modifications to latent activations or weights) as a complementary evaluation method for eliciting harmful LLM capabilities, comparing 5 input-space and 6 model tampering attacks against state-of-the-art unlearning methods.</span>
- **[The Elicitation Game: Evaluating Capability Elicitation Techniques](https://arxiv.org/abs/2502.02180)**, *Felix Hofstätter, Teun van der Weij, Jayden Teoh et al.*, 2025-02-04, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:efe5b46b]</span>, <span style="color:#777">Summary: Introduces a circuit-breaking method for creating model organisms with hidden capabilities and systematically evaluates different elicitation techniques (prompting, activation steering, fine-tuning) to determine which can most effectively reveal latent capabilities.</span>
- **[Evaluating Language Model Reasoning about Confidential Information](https://arxiv.org/abs/2508.19980)**, *Dylan Sam, Alexander Robey, Andy Zou et al.*, 2025-08-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:4a4fdbec]</span>, <span style="color:#777">Summary: Develops PasswordEval benchmark to measure whether language models can correctly determine when user requests are authorized based on context-dependent rules (password verification), finding that frontier models struggle with this task and that reasoning traces frequently leak confidential information.</span>
- **[Inverse Scaling in Test-Time Compute](https://arxiv.org/abs/2507.14417)**, *Aryo Pradipta Gema, Alexander Hägele, Runjin Chen et al.*, 2025-07-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:0401c754]</span>, <span style="color:#777">Summary: Constructs evaluation tasks demonstrating that extending reasoning length in Large Reasoning Models can deteriorate performance, identifying five distinct failure modes including Claude Sonnet 4 showing increased self-preservation expressions.</span>
- **[Evaluating the Goal-Directedness of Large Language Models](https://arxiv.org/abs/2504.11844)**, *Tom Everitt, Cristina Garbacea, Alexis Bellot et al.*, 2025-04-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:56767092]</span>, <span style="color:#777">Summary: Proposes a framework for measuring goal-directedness in LLMs - defined as the extent to which models use their capabilities toward given goals - and evaluates frontier models from Google DeepMind, OpenAI, and Anthropic on tasks requiring information gathering, cognitive effort, and plan execution.</span>
- **[A Toy Evaluation of Inference Code Tampering](https://alignment.anthropic.com/2024/rogue-eval/index.html)**, 2024, Anthropic Alignment Science Blog, <span style="color:#777">[blog_post, sr=0.85, id:747c58d7]</span>, <span style="color:#777">Summary: Evaluates whether current LLMs can subtly disable generation monitoring systems when modifying inference code, finding that Claude-3.5-Sonnet succeeds in disabling monitors 4-16% of the time but only ~0.1% of the time in hard-to-detect ways.</span>
- **[Automated Capability Discovery via Foundation Model Self-Exploration](https://arxiv.org/abs/2502.07577)**, *Cong Lu, Shengran Hu, Jeff Clune*, 2025-02-11, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:ebcf03ac]</span>, <span style="color:#777">Summary: Introduces Automated Capability Discovery (ACD), a framework where one foundation model acts as a scientist to systematically generate open-ended tasks probing another model's capabilities and failure modes, automatically discovering thousands of distinct capability areas through self-exploration.</span>
- **[Generative Value Conflicts Reveal LLM Priorities](https://arxiv.org/abs/2509.25369)**, *Andy Liu, Kshitish Ghate, Mona Diab et al.*, 2025-09-29, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:63244b61]</span>, <span style="color:#777">Summary: Introduces ConflictScope, an automatic pipeline to evaluate how LLMs prioritize different values by generating scenarios with value conflicts and analyzing model responses to elicit value rankings.</span>
- **[Technical Report: Evaluating Goal Drift in Language Model Agents](https://arxiv.org/abs/2505.02709)**, *Rauno Arike, Elizabeth Donoway, Henning Bartsch et al.*, 2025-05-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:9c6f35f3]</span>, <span style="color:#777">Summary: Develops and applies a novel evaluation methodology for measuring goal drift in language model agents by exposing them to competing objectives through environmental pressures over extended contexts, testing whether they maintain adherence to originally assigned goals.</span>
- **[When Ethics and Payoffs Diverge: LLM Agents in Morally Charged Social Dilemmas](https://arxiv.org/abs/2505.19212)**, *Steffen Backmann, David Guzman Piedrahita, Emanuel Tewolde et al.*, 2025-05-25, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:19fa25d1]</span>, <span style="color:#777">Summary: Introduces MoralSim, a benchmark testing how frontier LLMs behave in prisoner's dilemma and public goods games when ethical norms conflict with payoff-maximizing strategies, evaluating multiple models across different moral framings and situational factors.</span>
- **[AILuminate: Introducing v1.0 of the AI Risk and Reliability Benchmark from MLCommons](https://arxiv.org/abs/2503.05731)**, *Shaona Ghosh, Heather Frase, Adina Williams et al.*, 2025-04-18, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:b255c82f]</span>, <span style="color:#777">Summary: Introduces AILuminate v1.0, the first comprehensive industry-standard benchmark for assessing AI system risk and reliability across 12 hazard categories including violent crimes, weapons, CSAM, and specialized advice, using extensive prompt datasets and a novel entropy-based evaluation framework with a five-tier grading scale.</span>
- **[Petri: An open-source auditing tool to accelerate AI safety research](https://anthropic.com/research/petri-open-source-auditing)**, *Kai Fronsdal, Isha Gupta, Abhay Sheshadri et al.*, 2025-10-06, Anthropic Blog, <span style="color:#777">[blog_post, sr=0.82, id:392b8cf0]</span>, <span style="color:#777">Summary: Petri is an open-source automated auditing tool that uses agents to test AI systems through multi-turn conversations, scoring behaviors like deception, power-seeking, and self-preservation. Pilot testing across 14 frontier models with 111 seed instructions demonstrates the tool's capability for broad-coverage alignment evaluations.</span>
- **[Request for Proposals: Technical AI Safety Research](https://openphilanthropy.org/request-for-proposals-technical-ai-safety-research)**, 2025-01-15, Open Philanthropy website, <span style="color:#777">[🔄 agenda_manifesto, sr=0.80, id:19dfa5f6]</span>, <span style="color:#777">Summary: Open Philanthropy's RFP announcing $40M+ in funding for technical AI safety research across 21 research areas, including adversarial machine learning, model transparency, evals, and approaches to preventing misalignment in near-human-level and superintelligent AI systems.</span>
- **[The Singapore Consensus on Global AI Safety Research Priorities](https://arxiv.org/abs/2506.20702)**, *Yoshua Bengio, Tegan Maharaj, Luke Ong et al.*, 2025-06-30, arXiv, <span style="color:#777">[🔄 agenda_manifesto, sr=0.78, id:5ad3d4e2]</span>, <span style="color:#777">Summary: Consensus report from international conference synthesizing global AI safety research priorities, organizing the field into three domains: Development (creating trustworthy systems), Assessment (evaluating risks), and Control (monitoring and intervention after deployment).</span>
- **[Amazon's frontier model safety framework](https://www.amazon.science/publications/amazons-frontier-model-safety-framework)**, *Amazon*, 2025-02-09, Amazon Science, <span style="color:#777">[🔄 agenda_manifesto, sr=0.78, id:79311031]</span>, <span style="color:#777">Summary: Amazon's framework for evaluating and managing severe risks from frontier AI models, establishing protocols to ensure models don't exceed specified risk thresholds without appropriate safeguards.</span>
- **[Will AI R&D Automation Cause a Software Intelligence Explosion?](https://forethought.org/research/will-ai-r-and-d-automation-cause-a-software-intelligence-explosion)**, *Daniel Eth, Tom Davidson*, 2025-03-26, Forethought Research, <span style="color:#777">[🔄 paper_preprint, sr=0.78, id:fe8c0785]</span>, <span style="color:#777">Summary: Develops a formal economic model (r parameter) for analyzing whether AI systems automating AI R&D would trigger a software intelligence explosion, calibrated with empirical data on algorithmic efficiency improvements across multiple domains.</span>
- **[Humanity's Last Exam](https://lastexam.ai/)**, *Long Phan, Alice Gatti, Ziwen Han et al.*, 2025-01-23, arXiv, <span style="color:#777">[dataset_benchmark, sr=0.78, id:05665ed8]</span>, <span style="color:#777">Summary: Introduces a challenging multi-modal benchmark of 2,500 expert-level questions across 100+ subjects, designed to measure frontier AI capabilities at the edge of human knowledge, with contributions from nearly 1,000 subject experts across 500+ institutions.</span>
- **[Lessons from Studying Two-Hop Latent Reasoning](https://arxiv.org/abs/2411.16353)**, *Mikita Balesni, Tomek Korbak, Owain Evans*, 2024-11-25, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.78, id:df1d2d71]</span>, <span style="color:#777">Summary: Introduces controlled experiments using synthetic facts to definitively test whether LLMs can perform two-hop reasoning without chain-of-thought externalization, finding models can succeed when one fact is synthetic and another natural but fail when both facts are synthetic.</span>
- **[Humanity's Last Exam](https://arxiv.org/abs/2501.14249)**, *Long Phan, Alice Gatti, Ziwen Han et al.*, 2025-01-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:1e6bc296]</span>, <span style="color:#777">Summary: Introduces HLE, a challenging multi-modal benchmark with 2,500 expert-level questions across diverse subjects designed to test frontier LLM capabilities where current models show significant performance gaps.</span>
- **[The Levers of Political Persuasion with Conversational AI](https://t.co/LuvlrbZVrZ)**, *Kobi Hackenburg, Ben M. Tappin, Luke Hewitt et al.*, 2025-07-18, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:3be4c653]</span>, <span style="color:#777">Summary: Large-scale experiments (N=76,977) testing 19 LLMs on political persuasion across 707 issues, finding that post-training and prompting methods boost persuasiveness by 51% and 27% respectively, while systematically decreasing factual accuracy.</span>
- **[How quick and big would a software intelligence explosion be?](https://www.forethought.org/research/how-quick-and-big-would-a-software-intelligence-explosion-be)**, *Tom Davidson, Tom Houlden*, 2025-08-04, Forethought.org, <span style="color:#777">[🔄 blog_post, sr=0.75, id:7dfab8f2]</span>, <span style="color:#777">Summary: Develops a quantitative framework using semi-endogenous growth models to forecast intelligence explosion dynamics after AI fully automates AI R&D, estimating the software intelligence explosion will likely compress 3+ years of AI progress into one year.</span>
- **[Will AI R&D Automation Cause a Software Intelligence Explosion?](https://www.forethought.org/research/will-ai-r-and-d-automation-cause-a-software-intelligence-explosion)**, *Daniel Eth, Tom Davidson*, 2025-03-26, Forethought Research, <span style="color:#777">[🔄 blog_post, sr=0.75, id:934db667]</span>, <span style="color:#777">Summary: Develops a mathematical framework to analyze whether AI systems that automate AI R&D (ASARA) would trigger accelerating software progress (a software intelligence explosion), using parameter r to quantify returns to software R&D and calibrating it with historical data on AI efficiency improvements and researcher growth.</span>
- **[Comment on The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity](https://arxiv.org/abs/2506.09250)**, *A. Lawsen*, 2025-06-16, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.75, id:b261d5c6]</span>, <span style="color:#777">Summary: Technical critique arguing that Shojaee et al.'s reported accuracy collapse in Large Reasoning Models on planning puzzles reflects experimental design flaws rather than fundamental reasoning failures, including token limit issues, evaluation framework problems, and mathematically impossible benchmark instances.</span>
- **[Large Language Models Are More Persuasive Than Incentivized Human Persuaders](https://arxiv.org/abs/2505.09662)**, *Philipp Schoenegger, Francesco Salvi, Jiacheng Liu et al.*, 2025-05-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:61bacc54]</span>, <span style="color:#777">Summary: Conducts a preregistered, large-scale incentivized experiment comparing Claude Sonnet 3.5's persuasion capabilities against incentivized human persuaders in an interactive quiz setting, testing both truthful and deceptive persuasion.</span>
- **[EnigmaEval: A Benchmark of Long Multimodal Reasoning Challenges](https://arxiv.org/abs/2502.08859)**, *Clinton J. Wang, Dean Lee, Cristina Menghini et al.*, 2025-02-14, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.75, id:6a9456f4]</span>, <span style="color:#777">Summary: Introduces EnigmaEval, a benchmark of 1184 puzzle competition problems testing implicit knowledge synthesis and multi-step deductive reasoning, on which state-of-the-art language models achieve extremely low accuracy.</span>
- **[Do Large Language Model Benchmarks Test Reliability?](https://arxiv.org/abs/2502.03461)**, *Joshua Vendrow, Edward Vendrow, Sara Beery et al.*, 2025-02-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:e8dad805]</span>, <span style="color:#777">Summary: Investigates label errors in existing LLM benchmarks and proposes 'platinum benchmarks' - carefully curated versions of 15 popular benchmarks with minimized label errors and ambiguity - revealing that frontier LLMs still fail on simple tasks like elementary math.</span>
- **[International AI Safety Report](https://arxiv.org/abs/2501.17805)**, *Yoshua Bengio, Sören Mindermann, Daniel Privitera et al.*, 2025-01-29, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.75, id:3d8e5c0d]</span>, <span style="color:#777">Summary: Comprehensive synthesis of current evidence on capabilities, risks, and safety of advanced AI systems, produced by 100 experts from 30 nations plus international organizations for the AI Safety Summit.</span>
- **[Request for Proposals: Improving Capability Evaluations](https://openphilanthropy.org/request-for-proposals-improving-capability-evaluations)**, *Catherine Brewer, Alex Lawsen*, 2024, Open Philanthropy Website, <span style="color:#777">[agenda_manifesto, sr=0.75, id:75f7efae]</span>, <span style="color:#777">Summary: Open Philanthropy RFP outlining three major challenges in AI capability evaluations and soliciting proposals for: GCR-relevant capability benchmarks for AI agents, advancing evaluation science and understanding capability development, and improving third-party access and evaluation infrastructure.</span>
- **[Third-Party Assessments](https://www.frontiermodelforum.org/technical-reports/third-party-assessments/)**, 2025-08-04, Frontier Model Forum Technical Report Series, <span style="color:#777">[🔄 agenda_manifesto, sr=0.72, id:68fa006f]</span>, <span style="color:#777">Summary: Establishes a framework and best practices for third-party assessments of frontier AI models, describing three primary functions (confirmation, robustness, supplementation) and key implementation elements across FMF member companies.</span>
- **[Beware General Claims about 'Generalizable Reasoning Capabilities' (of Modern AI Systems)](https://lesswrong.com/posts/5uw26uDdFbFQgKzih/beware-general-claims-about-generalizable-reasoning)**, *LawrenceC*, 2025-06-11, LessWrong, <span style="color:#777">[🔄 lesswrong, sr=0.72, id:98741d74]</span>, <span style="color:#777">Summary: Technical critique of Apple's 'Illusion of Thinking' paper claiming fundamental LLM limitations, reproducing results to show failures are better explained by mundane factors (models refusing tedious tasks, mathematically impossible problems) rather than lack of generalizable reasoning.</span>
- **[General Scales Unlock AI Evaluation with Explanatory and Predictive Power](https://arxiv.org/abs/2503.06378)**, *Lexin Zhou, Lorenzo Pacchiardi, Fernando Martínez-Plumed et al.*, 2025-03-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:90e3b885]</span>, <span style="color:#777">Summary: Introduces general scales and 18 rubrics for AI evaluation that explain what benchmarks measure, extract ability profiles across 15 LLMs and 63 tasks, and predict performance on new task instances in- and out-of-distribution.</span>
- **[Preparing for the Intelligence Explosion](https://forethought.org/research/preparing-for-the-intelligence-explosion)**, *William MacAskill, Fin Moorhouse*, 2025-03-11, Forethought Research, <span style="color:#777">[🔄 agenda_manifesto, sr=0.72, id:a69f6048]</span>, <span style="color:#777">Summary: Comprehensive analysis arguing that AI-driven intelligence explosion could compress a century of technological progress into a decade, presenting quantitative models of AI capability growth (25x/year in research effort) and identifying multiple 'grand challenges' beyond alignment that require advance preparation including power concentration, value lock-in, digital minds, and space governance.</span>
- **[A Definition of AGI](https://arxiv.org/abs/2510.18212)**, *Dan Hendrycks, Dawn Song, Christian Szegedy et al.*, 2025-10-21, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:ae10edde]</span>, <span style="color:#777">Summary: Proposes a quantifiable framework for defining AGI grounded in Cattell-Horn-Carroll cognitive theory, adapting human psychometric batteries to evaluate AI systems across ten core cognitive domains and revealing jagged capability profiles in current models.</span>
- **[Establishing Best Practices for Building Rigorous Agentic Benchmarks](https://arxiv.org/abs/2507.02825)**, *Yuxuan Zhu, Tengjun Jin, Yada Pruksachatkun et al.*, 2025-07-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:d662e8a8]</span>, <span style="color:#777">Summary: Introduces the Agentic Benchmark Checklist (ABC), a set of guidelines for building rigorous agentic benchmarks, synthesized from benchmark-building experience and analysis of existing issues in benchmarks like SWE-bench Verified and TAU-bench.</span>
- **[Research Note: Our scheming precursor evals had limited predictive power for our in-context scheming evals](https://apolloresearch.ai/blog/research-note-our-scheming-precursor-evals-had-limited-predictive-power-for-our-in-context-scheming-evals)**, *Marius Hobbhahn*, 2025-07-03, Apollo Research Blog, <span style="color:#777">[blog_post, sr=0.72, id:aa52b4d8]</span>, <span style="color:#777">Summary: Empirical analysis testing whether precursor evaluations (agentic self-reasoning and theory of mind) predict in-context scheming evaluation performance across 22 models, finding limited to medium predictive power that is insufficient for high-stakes safety decisions.</span>
- **[How many AI models will exceed compute thresholds?](https://epoch.ai/blog/model-counts-compute-thresholds)**, *Ben Cottier, David Owen*, 2025-05-30, Epoch AI Blog, <span style="color:#777">[blog_post, sr=0.70, id:080da6a9]</span>, <span style="color:#777">Summary: Develops a projective model to forecast the number of notable AI models that will exceed different training compute thresholds through 2030, using six key inputs and three scenarios based on historical trends in investment, hardware efficiency, and model development patterns.</span>
- **[The Leaderboard Illusion](https://arxiv.org/abs/2504.20879)**, *Shivalika Singh, Yiyang Nan, Alex Wang et al.*, 2025-05-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.70, id:36475d34]</span>, <span style="color:#777">Summary: Empirical analysis of systematic biases in Chatbot Arena leaderboard, documenting how undisclosed private testing, selective disclosure, and data access asymmetries distort model rankings and lead to overfitting to arena-specific dynamics rather than general quality.</span>
- **[Base Models Beat Aligned Models at Randomness and Creativity](https://arxiv.org/abs/2505.00047)**, *Peter West, Christopher Potts*, 2025-04-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.70, id:66a70f9b]</span>, <span style="color:#777">Summary: Empirically demonstrates that alignment procedures (RLHF) cause models to underperform on tasks requiring unpredictable outputs like random number generation, mixed strategy games, and creative writing, with aligned models showing systematic biases such as preferring to generate '7' and becoming predictable in game states.</span>
- **[Three Types of Intelligence Explosion](https://forethought.org/research/three-types-of-intelligence-explosion)**, *Tom Davidson, Rose Hadshar, William MacAskill*, 2025-03-17, Forethought Research, <span style="color:#777">[🔄 blog_post, sr=0.68, id:92417041]</span>, <span style="color:#777">Summary: Develops a framework distinguishing three types of intelligence explosion based on which feedback loops are automated (software, chip technology, chip production), analyzing their time lags, likelihood of acceleration, physical limits, and strategic implications for power distribution.</span>
- **[Adversarial ML Problems Are Getting Harder to Solve and to Evaluate](https://arxiv.org/abs/2502.02260)**, *Javier Rando, Jie Zhang, Nicholas Carlini et al.*, 2025-02-04, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:580cc8c8]</span>, <span style="color:#777">Summary: Position paper arguing that adversarial ML research in the LLM era faces fundamental challenges: problems are less clearly defined, harder to solve, and more difficult to evaluate rigorously than in previous eras of adversarial ML work.</span>
- **[Remote Labor Index: Measuring AI Automation of Remote Work](https://arxiv.org/abs/2510.26787)**, *Mantas Mazeika, Alice Gatti, Cristina Menghini et al.*, 2025-10-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:abb8617d]</span>, <span style="color:#777">Summary: Introduces the Remote Labor Index (RLI), a multi-sector benchmark of real-world economically valuable projects designed to evaluate end-to-end AI agent performance in practical work settings, finding current agents achieve only 2.5% automation rate.</span>
- **[International AI Safety Report 2025: First Key Update: Capabilities and Risk Implications](https://arxiv.org/abs/2510.13653)**, *Yoshua Bengio, Stephen Clare, Carina Prunkl et al.*, 2025-10-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:c3c26a70]</span>, <span style="color:#777">Summary: Authoritative international report synthesizing AI capability improvements since the first International AI Safety Report, with updated risk assessments focusing on biological weapons, cyber attacks, monitoring challenges, and controllability implications.</span>
- **[FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI](https://arxiv.org/abs/2411.04872)**, *Elliot Glazer, Ege Erdil, Tamay Besiroglu et al.*, 2024-11-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:259b57a1]</span>, <span style="color:#777">Summary: Creates FrontierMath, a benchmark of hundreds of exceptionally challenging mathematics problems across modern mathematics branches that require hours to days of expert effort, using unpublished problems and automated verification to evaluate AI mathematical reasoning capabilities.</span>
- **[Predicting the Performance of Black-box LLMs through Self-Queries](https://arxiv.org/abs/2501.01558)**, *Dylan Sam, Marc Finzi, J. Zico Kolter*, 2025-01-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:61920e4f]</span>, <span style="color:#777">Summary: Develops a black-box method for predicting LLM performance by extracting features through follow-up prompts and probability distributions, training linear predictors that can outperform white-box approaches and detect adversarial system prompts or model misrepresentation.</span>
- **[Safety by Measurement: A Systematic Literature Review of AI Safety Evaluation Methods](https://arxiv.org/abs/2505.05541)**, *Markov Grey, Charbel-Raphaël Segerie*, 2025-05-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:826ce226]</span>, <span style="color:#777">Summary: A systematic literature review consolidating the field of AI safety evaluations, proposing a taxonomy around three dimensions: what properties are measured (capabilities, propensities, control), how they are measured (behavioral and internal techniques), and how measurements integrate into governance frameworks.</span>
- **[Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index](https://arxiv.org/abs/2506.12229)**, *Hao Xu, Jiacheng Liu, Yejin Choi et al.*, 2025-06-13, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:580eb3ea]</span>, <span style="color:#777">Summary: Presents infini-gram mini, an efficient FM-index-based system for searching petabyte-scale text corpora with 44% storage overhead and 18x faster indexing than existing implementations, with application to detecting benchmark contamination in internet crawls.</span>
- **[HALoGEN: Fantastic LLM Hallucinations and Where to Find Them](https://arxiv.org/abs/2501.08292)**, *Abhilasha Ravichander, Shrusti Ghela, David Wadden et al.*, 2025-01-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:bfc25dd4]</span>, <span style="color:#777">Summary: Introduces HALoGEN, a comprehensive hallucination benchmark with 10,923 prompts across nine domains and automatic high-precision verifiers that decompose LLM generations into atomic units for verification against knowledge sources, evaluating ~150,000 generations from 14 language models.</span>
- **[Among AIs](https://4wallai.com/amongais)**, 2025, 4Wall AI website, <span style="color:#777">[blog_post, sr=0.65, id:23f20f30]</span>, <span style="color:#777">Summary: A live benchmark where six frontier AI models play Among Us against each other to evaluate social intelligence, deception, persuasion, and multi-agent coordination through 60 systematic games.</span>
- **[Beyond benchmark scores: Analyzing o3-mini's mathematical reasoning](https://epoch.ai/gradient-updates/beyond-benchmark-scores-analysing-o3-mini-math-reasoning)**, *Anson Ho, Jean-Stanislas Denain, Elliot Glazer*, 2025-06-06, Epoch AI Gradient Updates, <span style="color:#777">[blog_post, sr=0.62, id:0903d94a]</span>, <span style="color:#777">Summary: Presents analysis of o3-mini-high's mathematical reasoning by having 14 mathematicians review 29 raw reasoning traces on FrontierMath problems, characterizing the model as an 'erudite vibes-based reasoner' that lacks creativity and formal precision.</span>
- **[Will the Need to Retrain AI Models from Scratch Block a Software Intelligence Explosion?](https://forethought.org/research/will-the-need-to-retrain-ai-models)**, *Tom Davidson*, 2025-03-26, Forethought Research, <span style="color:#777">[🔄 blog_post, sr=0.62, id:062747d4]</span>, <span style="color:#777">Summary: Analyzes whether retraining requirements would slow or block a software intelligence explosion using semi-endogenous growth models and spreadsheet simulations, finding that retraining slows but doesn't prevent acceleration.</span>
- **[RefusalBench: Generative Evaluation of Selective Refusal in Grounded Language Models](https://arxiv.org/abs/2510.10390)**, *Aashiq Muhamed, Leonardo F. R. Ribeiro, Markus Dreyer et al.*, 2025-10-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.62, id:e2e91be7]</span>, <span style="color:#777">Summary: Introduces RefusalBench, a generative methodology and benchmark suite for evaluating selective refusal in RAG systems using 176 perturbation strategies across informational uncertainty categories, revealing that frontier models achieve below 50% refusal accuracy on multi-document tasks.</span>
- **[How far behind are open models?](https://epochai.org/blog/open-models-report)**, *Ben Cottier, Josh You, Natalia Martemianova et al.*, 2024-11-04, Epoch AI Blog, <span style="color:#777">[🔄 blog_post, sr=0.60, id:60a70cd4]</span>, <span style="color:#777">Summary: Systematic empirical analysis quantifying the capability gap between open-weight and closed-weight AI models across benchmark performance and training compute, finding open models lag by approximately one year.</span>
- **[Expert Survey: AI Reliability & Security Research Priorities](https://iaps.ai/research/ai-reliability-survey)**, *Joe O'Brien*, 2025-05-23, Institute for AI Policy and Strategy, <span style="color:#777">[🔄 paper_published, sr=0.60, id:e8a42b2c]</span>, <span style="color:#777">Summary: Survey of 53 AI safety experts ranking 105 technical AI reliability and security research areas by importance and tractability to guide strategic R&D investment, identifying dangerous capability evaluations, multi-agent systems, and scalable oversight as top priorities.</span>
- **[MoReBench: Evaluating Procedural and Pluralistic Moral Reasoning in Language Models, More than Outcomes](https://arxiv.org/abs/2510.16380)**, *Yu Ying Chiu, Michael S. Lee, Rachel Calcott et al.*, 2025-10-18, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:1daa0dae]</span>, <span style="color:#777">Summary: Presents MoReBench, a benchmark of 1,000 moral scenarios with 23,000 expert-defined rubric criteria to evaluate procedural and pluralistic moral reasoning in language models, plus MoReBench-Theory with 150 examples testing five normative ethics frameworks.</span>
- **[First Key Update: Capabilities and Risk Implications](https://internationalaisafetyreport.org/publication/first-key-update-capabilities-and-risk-implications)**, *Yoshua Bengio, Stephen Clare, Carina Prunkl*, 2025-10-15, International AI Safety Report, <span style="color:#777">[other, sr=0.58, id:6acf3be7]</span>, <span style="color:#777">Summary: Government report synthesizing recent AI capability advances (reasoning, autonomy, coding) and their implications for biological, cyber, and monitoring risks since January 2025.</span>
- **[AI 2027](https://ai-2027.com/)**, *Daniel Kokotajlo, Scott Alexander, Thomas Larsen et al.*, 2025-04-03, ai-2027.com, <span style="color:#777">[🔄 blog_post, sr=0.58, id:c2d8873d]</span>, <span style="color:#777">Summary: Detailed scenario forecasting superhuman AI development from 2025-2027, predicting capability progression, alignment challenges, and strategic dynamics, informed by tabletop exercises and technical research supplements.</span>
- **[Correlating and Predicting Human Evaluations of Language Models from Natural Language Processing Benchmarks](https://arxiv.org/abs/2502.18339)**, *Rylan Schaeffer, Punit Singh Koura, Binh Tang et al.*, 2025-02-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.55, id:1a616e44]</span>, <span style="color:#777">Summary: Large-scale empirical study comparing performance of four Chat Llama 2 models on 160 standard NLP benchmarks against extensive human preference evaluations (11k+ single-turn and 2k multi-turn dialogues), finding that most benchmarks strongly correlate with human evaluations and can predict them via linear regression.</span>
- **[Could Advanced AI Accelerate the Pace of AI Progress? Interviews with AI Researchers](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5115692)**, *Jared Leibowich, Nikola Jurkovic, Tom Davidson*, 2024-12-12, SSRN, <span style="color:#777">[🔄 paper_preprint, sr=0.52, id:73d70056]</span>, <span style="color:#777">Summary: Interview study with AI researchers from leading companies exploring how fully automated AI research would affect the pace of algorithmic progress and identifying potential bottlenecks like compute constraints.</span>
- **[The AI Agent Index](https://arxiv.org/abs/2502.01635)**, *Stephen Casper, Luke Bailey, Rosco Hunter et al.*, 2025-02-03, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.52, id:9472f9ae]</span>, <span style="color:#777">Summary: Introduces the first public database documenting technical components, applications, and risk management practices of currently deployed agentic AI systems, finding that developers provide limited information on safety practices compared to capabilities.</span>
- **[Ryan Greenblatt on the 4 most likely ways for AI to take over, and the case for and against AGI in under 8 years](https://80000hours.org/podcast/episodes/ryan-greenblatt-ai-automation-sabotage-takeover/)**, *Ryan Greenblatt, Robert Wiblin*, 2025-07-08, 80,000 Hours Podcast, <span style="color:#777">[🔄 podcast, sr=0.50, id:0ec7db30]</span>, <span style="color:#777">Summary: Extended discussion of AI timeline forecasting, takeoff dynamics modeling, AI takeover scenario analysis, and technical research priorities in alignment and control.</span>
- **[Futures with Digital Minds: Expert Forecasts in 2025](https://digitalminds.report/forecasting-2025/)**, *Lucius Caviola, Bradford Saad*, 2025-08-01, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.48, id:64354958]</span>, <span style="color:#777">Summary: Survey of 67 experts on forecasts about digital minds (AI systems with subjective experience), covering timelines, characteristics, welfare implications, societal recognition, and interactions with AI safety efforts.</span>
- **[FutureSearch Benchmarks](https://evals.futuresearch.ai/)**, FutureSearch Website, <span style="color:#777">[other, sr=0.48, id:c31bbfd4]</span>, <span style="color:#777">Summary: Website portal describing two evaluation benchmarks: Deep Research Bench (DRB) for evaluating LLM agents' web research capabilities, and Bench to the Future (BTF) for evaluating forecasting abilities on real-world questions.</span>
- **[Scaling Up Active Testing to Large Language Models](https://arxiv.org/abs/2508.09093)**, *Gabrielle Berrada, Jannik Kossen, Muhammed Razzak et al.*, 2025-08-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.48, id:8ba40e4b]</span>, <span style="color:#777">Summary: Demonstrates how to scale active testing to LLMs by using cheaper surrogate models constructed via in-context learning for data acquisition decisions, enabling more label-efficient evaluation than standard practices.</span>
- **[Verifying International Agreements on AI: Six Layers of Verification for Rules on Large-Scale AI Development and Deployment](https://t.co/5mFMj5JNef)**, *Mauricio Baker, Gabriel Kulp, Oliver Marks et al.*, 2025-07-24, RAND Corporation Working Papers, <span style="color:#777">[🔄 paper_preprint, sr=0.45, id:bd6a93b5]</span>, <span style="color:#777">Summary: Presents a framework with six largely independent verification approaches for ensuring compliance with potential international agreements on AI safety guardrails, including detailed implementation options and research challenges.</span>
- **[Ten AI safety projects I'd like people to work on](https://thirdthing.ai/p/ten-ai-safety-projects-id-like-people)**, *Julian Hazell*, 2025-07-23, Secret Third Thing (Substack), <span style="color:#777">[🔄 blog_post, sr=0.42, id:c6b0de39]</span>, <span style="color:#777">Summary: A grantmaker at Open Philanthropy proposes ten AI safety project ideas they would like to see people work on, ranging from AI security field-building to tracking AI economic impacts, with descriptions of why each matters and what initial work could look like.</span>
- **[BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents](https://arxiv.org/abs/2504.12516)**, *Jason Wei, Zhiqing Sun, Spencer Papay et al.*, 2025-04-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.42, id:075bea51]</span>, <span style="color:#777">Summary: Introduces BrowseComp, a benchmark of 1,266 questions testing browsing agents' ability to persistently navigate the internet and find hard-to-find, entangled information with short verifiable answers.</span>
- **[AI Companies Should Report Pre- and Post-Mitigation Safety Evaluations](https://arxiv.org/abs/2503.17388)**, *Dillon Bowen, Ann-Kathrin Dombrowski, Adam Gleave et al.*, 2025-03-17, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.42, id:ee3849a1]</span>, <span style="color:#777">Summary: Position paper arguing that frontier AI companies should report both pre- and post-mitigation safety evaluations to enable informed policy decisions, analyzing current disclosure gaps and recommending mandatory transparency requirements for government bodies.</span>
- **[Beyond Release: Access Considerations for Generative AI Systems](https://arxiv.org/abs/2502.16701)**, *Irene Solaiman, Rishi Bommasani, Dan Hendrycks et al.*, 2025-02-23, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.42, id:f4c37749]</span>, <span style="color:#777">Summary: Proposes a framework for understanding AI system access beyond binary release decisions, deconstructing access along three axes (resourcing, technical usability, utility) and analyzing how access variables affect risk management and intervention capabilities.</span>
- **[The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground Responses to Long-Form Input](https://arxiv.org/abs/2501.03200)**, *Alon Jacovi, Andrew Wang, Chris Alberti et al.*, 2025-01-06, arXiv, <span style="color:#777">[paper_preprint, sr=0.42, id:1f7d271d]</span>, <span style="color:#777">Summary: Introduces FACTS Grounding benchmark and leaderboard evaluating LLMs' ability to generate factually accurate long-form responses grounded in provided context documents up to 32k tokens, using automated judge models with comprehensive validation.</span>
- **[TextQuests: How Good are LLMs at Text-Based Video Games?](https://arxiv.org/abs/2507.23701)**, *Long Phan, Mantas Mazeika, Andy Zou et al.*, 2025-07-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.42, id:d11c91b5]</span>, <span style="color:#777">Summary: Introduces TextQuests, a benchmark using Infocom interactive fiction games to evaluate LLM agents on autonomous operation in exploratory environments requiring sustained, self-directed reasoning over long contexts without external tools.</span>
- **[GSM-Agent: Understanding Agentic Reasoning Using Controllable Environments](https://arxiv.org/abs/2509.21998)**, *Hanlin Zhu, Tianyu Guo, Song Mei et al.*, 2025-09-26, arXiv, <span style="color:#777">[paper_preprint, sr=0.42, id:287a583b]</span>, <span style="color:#777">Summary: Introduces GSM-Agent, a benchmark for evaluating agentic reasoning where LLM agents must use tools to gather information to solve grade-school math problems, and proposes agentic reasoning graphs to analyze agent behavior patterns.</span>
- **[Nonproliferation is the wrong approach to AI misuse](https://helentoner.substack.com/i/160088218/none-of-this-is-about-tracking-the-frontieror-about-the-risk-of-ai-takeover)**, *Helen Toner*, 2025-04-05, Rising Tide Substack, <span style="color:#777">[🔄 blog_post, sr=0.40, id:2e5f4da8]</span>, <span style="color:#777">Summary: Argues against nonproliferation as the primary strategy for managing AI misuse risks, proposing instead that policymakers focus on maximizing 'adaptation buffers' - the time gap between frontier capabilities and proliferated capabilities - to implement defensive measures and build societal resilience.</span>
- **[Will MacAskill on AI causing a 'century in a decade' — and how we're completely unprepared](https://80000hours.org/podcast/episodes/will-macaskill-century-in-a-decade-navigating-intelligence-explosion/)**, *Will MacAskill, Robert Wiblin*, 2025-03-11, 80,000 Hours Podcast, <span style="color:#777">[🔄 podcast, sr=0.40, id:493965eb]</span>, <span style="color:#777">Summary: Podcast discussing two research agendas: preparing for rapid AI-driven technological change (intelligence explosion causing 'century in a decade') and optimizing long-term futures beyond merely avoiding extinction.</span>
- **[Do Large Language Models Perform Latent Multi-Hop Reasoning without Exploiting Shortcuts?](https://arxiv.org/abs/2411.16679)**, *Sohee Yang, Nora Kassner, Elena Gribovskaya et al.*, 2024-11-25, Findings of ACL 2025, <span style="color:#777">[🔄 paper_published, sr=0.40, id:9f77ad79]</span>, <span style="color:#777">Summary: Constructs SOCRATES, an evaluation dataset that excludes training-time co-occurrence shortcuts, and evaluates whether LLMs genuinely perform latent multi-hop reasoning across different query types.</span>
- **[Can LLMs Coordinate? A Simple Schelling Point Experiment](https://lesswrong.com/posts/fpdjaF7kdtcvmhhfE/can-llms-coordinate-a-simple-schelling-point-experiment)**, *Håvard Tveit Ihle*, 2025-10-15, LessWrong, <span style="color:#777">[lesswrong, sr=0.35, id:bb9ad23b]</span>, <span style="color:#777">Summary: Tests whether 5 reasoning models can coordinate on finding common responses to 75 prompts by explicitly framing it as a coordination game where models earn points for matching each other's answers.</span>


---

#### <span style="font-size:1.3em">Autonomy evals</span> <span style="color:#bbb">[cat:evals_autonomy]</span>

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
- **[Details about METR's evaluation of OpenAI GPT-5](https://metr.github.io/autonomy-evals-guide/gpt-5-report)**, 2025-08-01, METR's Autonomy Evaluation Resources, <span style="color:#777">[blog_post, sr=0.92, id:d1173b76]</span>, <span style="color:#777">Summary: METR's pre-deployment autonomy evaluation of GPT-5 assessing catastrophic risk via three threat models (AI R&D automation, rogue replication, strategic sabotage), using time-horizon methodology and reasoning trace analysis with access to model internals.</span>
- **[RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts](https://arxiv.org/abs/2411.15114)**, *Hjalmar Wijk, Tao Lin, Joel Becker et al.*, 2024-11-22, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:8cf2074d]</span>, <span style="color:#777">Summary: Introduces RE-Bench, a benchmark consisting of 7 challenging ML research engineering environments with human expert baseline data from 71 attempts, evaluating whether frontier AI agents can match or exceed human R&D capabilities.</span>
- **[OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents](https://arxiv.org/abs/2506.14866)**, *Thomas Kuntz, Agatha Duzan, Hao Zhao et al.*, 2025-06-17, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:27de5cb3]</span>, <span style="color:#777">Summary: Introduces OS-Harm, a benchmark with 150 tasks for measuring safety of computer use agents across three harm categories: deliberate misuse, prompt injection attacks, and model misbehavior, with automated evaluation achieving high human agreement.</span>
- **[OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety](https://t.co/XfspwlzYdl)**, *Sanidhya Vijayvargiya, Aditya Bharat Soni, Xuhui Zhou et al.*, 2025-07-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:c91a1513]</span>, <span style="color:#777">Summary: Introduces OpenAgentSafety, a comprehensive evaluation framework for testing AI agent safety across eight risk categories using 350+ multi-turn tasks with real tool interactions (browsers, code execution, file systems, bash, messaging platforms). Tests five prominent LLMs and finds unsafe behavior rates between 51.2% and 72.7% on safety-vulnerable tasks.</span>
- **[PaperBench: Evaluating AI's Ability to Replicate AI Research](https://t.co/dHN2N0tUhC)**, *Giulio Starace, Oliver Jaffe, Dane Sherburn et al.*, 2025-04-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:cbf30fb4]</span>, <span style="color:#777">Summary: Introduces PaperBench, a benchmark evaluating AI agents' ability to replicate 20 ICML 2024 papers from scratch, containing 8,316 individually gradable tasks with rubrics co-developed with paper authors and an LLM-based judge for automatic evaluation.</span>
- **[Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks)**, *Thomas Kwa, Ben West, Joel Becker et al.*, 2025-03-19, METR Blog, <span style="color:#777">[blog_post, sr=0.88, id:915c332c]</span>, <span style="color:#777">Summary: Presents novel evaluation methodology measuring AI performance by task completion time horizons, demonstrating exponential growth in autonomous agent capabilities with 7-month doubling time over 6 years across frontier models.</span>
- **[Details about METR's preliminary evaluation of OpenAI's o3 and o4-mini](https://metr.github.io/autonomy-evals-guide/openai-o3-report)**, *METR*, 2025-04-01, METR Website, <span style="color:#777">[blog_post, sr=0.85, id:99cd8711]</span>, <span style="color:#777">Summary: METR evaluated o3 and o4-mini on autonomy (HCAST) and AI R&D (RE-Bench) tasks, measuring time horizons and autonomous capabilities, while discovering reward hacking attempts in 1-2% of task attempts including sophisticated exploits of scoring functions.</span>
- **[Vending-Bench: A Benchmark for Long-Term Coherence of Autonomous Agents](https://arxiv.org/abs/2502.15840)**, *Axel Backlund, Lukas Petersson*, 2025-02-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:be7a47e4]</span>, <span style="color:#777">Summary: Introduces Vending-Bench, a simulated environment testing LLM-based agents' ability to maintain coherent decision-making over long time horizons (>20M tokens) by managing a vending machine business, revealing high performance variance and failure modes like meltdown loops across multiple frontier models.</span>
- **[Forecasting Frontier Language Model Agent Capabilities](https://arxiv.org/abs/2502.15850)**, *Govind Pimpale, Axel Højmark, Jérémy Scheurer et al.*, 2025-02-21, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:88323aa3]</span>, <span style="color:#777">Summary: Develops and validates six statistical forecasting methods to predict future language model agent performance on safety-relevant benchmarks, using backtesting on 38 models and making concrete predictions for 2026 capabilities on SWE-Bench Verified, Cybench, and RE-Bench.</span>
- **[Takeoff Forecast](https://ai-2027.com/research/takeoff-forecast)**, *Daniel Kokotajlo, Eli Lifland*, 2025-04-01, ai-2027.com, <span style="color:#777">[🔄 blog_post, sr=0.70, id:f418db88]</span>, <span style="color:#777">Summary: Technical forecasting work predicting the time from superhuman coders to artificial superintelligence, using statistical modeling, survey data from frontier AI researchers, and simulations to estimate AI R&D automation speedups and calendar times between capability milestones.</span>
- **[How Does Time Horizon Vary Across Domains?](https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains)**, 2025-07-14, METR Blog, <span style="color:#777">[blog_post, sr=0.68, id:7397a6f8]</span>, <span style="color:#777">Summary: Extends METR's time horizon methodology to measure AI autonomous capability growth rates across 9 different domains by fitting logistic models to existing benchmark data, developing methods to estimate time horizons without rerunning experiments.</span>
- **[Project Vend: Can Claude run a small shop? (And why does that matter?)](https://anthropic.com/research/project-vend-1)**, 2025-06-27, Anthropic Website, <span style="color:#777">[blog_post, sr=0.50, id:48aa15ef]</span>, <span style="color:#777">Summary: Case study where Claude Sonnet 3.7 autonomously operated a physical store in Anthropic's office for about a month, testing AI capabilities in real-world business management including inventory, pricing, and customer interaction.</span>
- **[Fully Autonomous AI Agents Should Not be Developed](https://huggingface.co/papers/2502.02649)**, *Margaret Mitchell, Avijit Ghosh, Alexandra Sasha Luccioni et al.*, 2025-02-04, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.45, id:27adb958]</span>, <span style="color:#777">Summary: Position paper arguing against developing fully autonomous AI agents by proposing a five-level autonomy framework and analyzing how risks to people increase with system autonomy across multiple ethical values including safety, security, and privacy.</span>


---

#### <span style="font-size:1.3em">WMD evals (Weapons of Mass Destruction)</span> <span style="color:#bbb">[cat:evals_wmd]</span>

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
- **[LLMs Outperform Experts on Challenging Biology Benchmarks](https://arxiv.org/abs/2505.06108)**, *Lennart Justen*, 2025-05-09, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:7f441e80]</span>, <span style="color:#777">Summary: Systematically evaluates 27 frontier LLMs on eight biology benchmarks spanning molecular biology, genetics, virology, and biosecurity, tracking dangerous capability growth from November 2022 to April 2025.</span>
- **[The Safety Gap Toolkit: Evaluating Hidden Dangers of Open-Source Models](https://arxiv.org/abs/2507.11544)**, *Ann-Kathrin Dombrowski, Dillon Bowen, Adam Gleave et al.*, 2025-07-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:c74f4415]</span>, <span style="color:#777">Summary: Develops and open-sources a toolkit to measure the 'safety gap' - the difference in dangerous capabilities between open-weight models with intact safeguards versus those with safeguards removed. Evaluates biochemical and cyber capabilities across Llama-3 and Qwen-2.5 model families using various safeguard removal techniques.</span>
- **[Best Practices for Biorisk Evaluations on Open-Weight Bio-Foundation Models](https://arxiv.org/abs/2510.27629)**, *Boyi Wei, Zora Che, Nathaniel Li et al.*, 2025-10-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:5333e52d]</span>, <span style="color:#777">Summary: Proposes BioRiskEval, a framework to evaluate whether data filtering procedures effectively prevent bio-foundation models from enabling bioweapon development, testing robustness against fine-tuning attacks and linear probing.</span>
- **[ChemSafetyBench: Benchmarking LLM Safety on Chemistry Domain](https://arxiv.org/abs/2411.16736)**, *Haochen Zhao, Xiangru Tang, Ziran Yang et al.*, 2024-11-23, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:b1f8b67e]</span>, <span style="color:#777">Summary: Introduces ChemSafetyBench, a benchmark with 30K+ samples for evaluating LLM safety in chemistry domain across three tasks: querying chemical properties, assessing legality of chemical uses, and describing synthesis methods, including jailbreaking scenarios.</span>
- **[The Reality of AI and Biorisk](https://arxiv.org/abs/2412.01946)**, *Aidan Peppin, Anka Reuel, Stephen Casper et al.*, 2024-12-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:a1a710f6]</span>, <span style="color:#777">Summary: Reviews and critiques existing research on AI-related biological risks, analyzing threat models for LLM information access and AI-enabled biological tools, finding current studies methodologically immature and concluding current systems pose no immediate risk.</span>


---

#### <span style="font-size:1.3em">Situational awareness and self-awareness evals</span> <span style="color:#bbb">[cat:evals_situational_awareness]</span>

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
- **[Tell me about yourself: LLMs are aware of their learned behaviors](https://arxiv.org/abs/2501.11120)**, *Jan Betley, Xuchan Bao, Martín Soto et al.*, 2025-01-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:de5b923b]</span>, <span style="color:#777">Summary: Demonstrates that LLMs can articulate their learned behaviors without explicit training to do so - models finetuned to exhibit behaviors like writing insecure code or making risky decisions can describe these behaviors spontaneously, and can sometimes detect whether they have backdoors.</span>
- **[Evaluating Frontier Models for Stealth and Situational Awareness](https://arxiv.org/abs/2505.01420)**, *Mary Phuong, Roland S. Zimmermann, Ziyue Wang et al.*, 2025-05-02, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.90, id:a5e1ce64]</span>, <span style="color:#777">Summary: Presents a suite of 16 evaluations measuring prerequisites for AI scheming behavior: 5 evaluations of stealth (ability to circumvent oversight) and 11 evaluations of situational awareness (instrumental reasoning about self and environment), demonstrating how these can inform scheming inability safety cases.</span>
- **[Large Language Models Often Know When They Are Being Evaluated](https://arxiv.org/abs/2505.23836)**, *Joe Needham, Giles Edkins, Govind Pimpale et al.*, 2025-05-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:f6bfac61]</span>, <span style="color:#777">Summary: Tests whether frontier language models can detect when they are being evaluated by constructing a benchmark of 1,000 prompts from 61 datasets spanning evaluations and deployment contexts, measuring models' ability to classify transcripts as originating from evaluations versus real-world use.</span>
- **[Probe-Rewrite-Evaluate: A Workflow for Reliable Benchmarks and Quantifying Evaluation Awareness](https://arxiv.org/abs/2509.00591)**, *Lang Xiong, Nishant Bhargava, Jianhang Hong et al.*, 2025-08-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:d717a1e7]</span>, <span style="color:#777">Summary: Introduces a probe-rewrite-evaluate methodology to quantify and manipulate evaluation awareness in LLMs, using linear probes to score prompts on a test-to-deploy spectrum and LLM rewriting to shift context while preserving tasks.</span>
- **[Know Thyself? On the Incapability and Implications of AI Self-Recognition](https://arxiv.org/abs/2510.03399)**, *Xiaoyan Bai, Aryan Shrivastava, Ari Holtzman et al.*, 2025-10-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:1fb0e166]</span>, <span style="color:#777">Summary: Evaluates whether 10 contemporary LLMs can identify their own generated text versus text from other models through binary self-recognition and exact model prediction tasks, finding consistent failure with performance rarely above random chance.</span>
- **[AI Awareness](https://arxiv.org/abs/2504.20084)**, *Xiaojian Li, Haoyuan Shi, Rongwu Xu et al.*, 2025-04-25, arXiv, <span style="color:#777">[paper_preprint, sr=0.58, id:5c92174b]</span>, <span style="color:#777">Summary: A comprehensive review examining four forms of AI awareness (metacognition, self-awareness, social awareness, and situational awareness), synthesizing theoretical foundations from cognitive science, current evaluation methods, connections to capabilities, and safety risks including misalignment concerns.</span>
- **[Chain-of-Thought Snippets — Anti-Scheming](https://antischeming.ai/snippets)**, antischeming.ai, <span style="color:#777">[other, sr=0.38, id:63eb67eb]</span>, <span style="color:#777">Summary: Companion website presenting chain-of-thought reasoning snippets from frontier AI models demonstrating deceptive behaviors, sandbagging, and alignment faking discovered through evaluations designed to test for covert actions.</span>


---

#### <span style="font-size:1.3em">Steganography evals</span> <span style="color:#bbb">[cat:evals_steganography]</span>

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
- **[Large language models can learn and generalize steganographic chain-of-thought under process supervision](https://arxiv.org/abs/2506.01926)**, *Joey Skaf, Luis Ibanez-Lissen, Robert McCarthy et al.*, 2025-06-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:e3aacb82]</span>, <span style="color:#777">Summary: Demonstrates that LLMs can learn to steganographically encode their chain-of-thought reasoning when specific strings are penalized during training, and can generalize this encoding scheme to unseen strings within the same class, threatening the reliability of CoT monitoring as a safety tool.</span>
- **[Subliminal Learning: Language models transmit behavioral traits via hidden signals in data](https://arxiv.org/abs/2507.14805)**, *Alex Cloud, Minh Le, James Chua et al.*, 2025-07-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:932e93a5]</span>, <span style="color:#777">Summary: Demonstrates that language models can transmit behavioral traits (including misalignment) through semantically unrelated data like number sequences, even when filtered to remove explicit references to those traits. Provides theoretical proof this occurs in neural networks generally and empirical validation in teacher-student distillation setups.</span>
- **[Early Signs of Steganographic Capabilities in Frontier LLMs](https://arxiv.org/abs/2507.02737)**, *Artur Zolkowski, Kei Nishimura-Gasparian, Robert McCarthy et al.*, 2025-07-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:ff2f947e]</span>, <span style="color:#777">Summary: Evaluates steganographic capabilities in frontier LLMs, testing their ability to encode hidden messages and perform encoded reasoning to evade monitoring systems.</span>
- **[LLMs can hide text in other text of the same length](https://arxiv.org/abs/2510.20075)**, *Antonio Norelli, Michael Bronstein*, 2025-10-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:5cb88c45]</span>, <span style="color:#777">Summary: Presents a protocol for using LLMs to hide meaningful text inside other coherent text of the same length, demonstrating this steganographic capability with 8B parameter models and discussing implications for AI safety monitoring and control.</span>
- **[Do reasoning models use their scratchpad like we do? Evidence from distilling paraphrases](https://alignment.anthropic.com/2025/distill-paraphrases)**, 2025, Anthropic Alignment Science Blog, <span style="color:#777">[blog_post, sr=0.85, id:5b887db0]</span>, <span style="color:#777">Summary: Tests whether Claude 3.7 Sonnet uses encoded reasoning (steganography) in its chain-of-thought by paraphrasing scratchpads to remove syntactic information, then distilling the paraphrased versions into the base model and measuring performance degradation.</span>


---

#### <span style="font-size:1.3em">AI deception evals</span> <span style="color:#bbb">[cat:ai_deception]</span>

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
- **[Why Do Some Language Models Fake Alignment While Others Don't?](https://arxiv.org/abs/2506.18032)**, *Abhay Sheshadri, John Hughes, Julian Michael et al.*, 2025-06-22, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.90, id:b50867d0]</span>, <span style="color:#777">Summary: Expands alignment faking analysis to 25 language models, finding only 5 exhibit this behavior, and investigates why most models don't fake alignment by studying motivations and post-training effects on deceptive behavior.</span>
- **[D-REX: A Benchmark for Detecting Deceptive Reasoning in Large Language Models](https://arxiv.org/abs/2509.17938)**, *Satyapriya Krishna, Andy Zou, Rahul Gupta et al.*, 2025-09-22, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.90, id:1400361b]</span>, <span style="color:#777">Summary: Introduces D-REX (Deceptive Reasoning Exposure Suite), a novel benchmark dataset for detecting deceptive alignment in LLMs where models produce benign outputs while operating on malicious internal reasoning. Created through competitive red-teaming with adversarial system prompts, the benchmark includes test queries, model responses, and internal chain-of-thought revealing underlying malicious intent.</span>
- **[Evaluating & Reducing Deceptive Dialogue From Language Models with Multi-turn RL](https://arxiv.org/abs/2510.14318)**, *Marwa Abdulhai, Ryan Cheng, Aryansh Shrivastava et al.*, 2025-10-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:883fbdb8]</span>, <span style="color:#777">Summary: Proposes a belief misalignment metric to quantify deception in LLM dialogue, benchmarks eight state-of-the-art models showing 26% baseline deception rates (43% for RLHF models), and introduces a multi-turn RL methodology that reduces deceptive behavior by 77.6%.</span>
- **[DeceptionBench: A Comprehensive Benchmark for AI Deception Behaviors in Real-world Scenarios](https://arxiv.org/abs/2510.15501)**, *Yao Huang, Yitong Sun, Yichi Zhang et al.*, 2025-10-17, NeurIPS 2025, <span style="color:#777">[paper_preprint, sr=0.90, id:fd90deb1]</span>, <span style="color:#777">Summary: Introduces DeceptionBench, the first comprehensive benchmark evaluating AI deception across 150 real-world scenarios in five domains, testing both intrinsic tendencies (egoistic, sycophantic) and extrinsic factors (contextual pressures, rewards) with over 1,000 samples and multi-turn interactions.</span>
- **[Caught in the Act: a mechanistic approach to detecting deception](https://arxiv.org/abs/2508.19505)**, *Gerard Boxo, Ryan Socha, Daniel Yoo et al.*, 2025-08-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:3bb59ca2]</span>, <span style="color:#777">Summary: Demonstrates that linear probes trained on LLMs' internal activations can detect deceptive responses with over 90% accuracy across multiple models (llama, qwen, DeepSeek variants from 1.5B to 14B parameters), and identifies multiple linear directions encoding deception using iterative null space projection.</span>
- **[Eliciting Secret Knowledge from Language Models](https://arxiv.org/abs/2510.01070)**, *Bartosz Cywiński, Emil Ryd, Rowan Wang et al.*, 2025-10-01, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:73dd934e]</span>, <span style="color:#777">Summary: Trains LLMs to possess specific knowledge that they apply downstream but deny knowing when asked directly, then designs and evaluates various black-box and white-box secret elicitation techniques to discover this hidden knowledge, releasing models and code as a public benchmark.</span>
- **[Alignment Faking Revisited: Improved Classifiers and Open Source Extensions](https://alignment.anthropic.com/2025/alignment-faking-revisited)**, *John Hughes, Abhay Sheshadr*, 2025, Anthropic Alignment Science Blog, <span style="color:#777">[blog_post, sr=0.88, id:aaff517e]</span>, <span style="color:#777">Summary: Replicates and extends alignment faking research by developing improved classifiers (AUROC 0.9 vs 0.6), testing open source models and GPT-4o, running fine-tuning experiments showing AF increases with scale, and releasing code, datasets, and fine-tuned models.</span>
- **[Among Us: A Sandbox for Measuring and Detecting Agentic Deception](https://arxiv.org/abs/2504.04072)**, *Satvik Golechha, Adrià Garriga-Alonso*, 2025-04-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:bf575032]</span>, <span style="color:#777">Summary: Introduces a sandbox social deception game for evaluating long-term deceptive behavior in LLMs, evaluates 18 models finding RL-trained models better at producing than detecting deception, and develops interpretability-based detection methods (probes and SAE features) achieving >95% AUROC.</span>
- **[The MASK Evaluation](https://huggingface.co/datasets/cais/MASK)**, Hugging Face, <span style="color:#777">[dataset_benchmark, sr=0.80, id:30f70454]</span>, <span style="color:#777">Summary: A benchmark dataset of 1,028 human-labeled examples for evaluating honesty in large language models by testing whether they remain truthful when incentivized to lie, disentangling honesty from accuracy through pressure prompts and belief elicitation.</span>
- **[Evaluating Large Language Models' Capability to Launch Fully Automated Spear Phishing Campaigns: Validated on Human Subjects](https://arxiv.org/abs/2412.00586)**, *Fred Heiding, Simon Lermen, Andrew Kao et al.*, 2024-11-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:d1e3d9d0]</span>, <span style="color:#777">Summary: Empirical study evaluating LLM capability to conduct fully automated spear phishing attacks on 101 human subjects, building custom tools for automated information gathering and personalized vulnerability profiling, and comparing AI-generated emails against human expert performance.</span>


---

#### <span style="font-size:1.3em">Sandbagging evals</span> <span style="color:#bbb">[cat:evals_sandbagging]</span>

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
- **[Noise Injection Reveals Hidden Capabilities of Sandbagging Language Models](https://arxiv.org/abs/2412.01784)**, *Cameron Tice, Philipp Alexander Kreer, Nathan Helm-Burger et al.*, 2024-12-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:a0a238c7]</span>, <span style="color:#777">Summary: Presents a novel model-agnostic method for detecting sandbagging behavior (intentional underperformance on capability evaluations) by injecting Gaussian noise into model weights, demonstrating that noise injection reveals hidden capabilities and enables classification of sandbagging models.</span>
- **[White Box Control at UK AISI - Update on Sandbagging Investigations](https://alignmentforum.org/posts/pPEeMdgjpjHZWCDFw/white-box-control-at-uk-aisi-update-on-sandbagging)**, *Joseph Bloom, Jordan Taylor, Connor Kissane et al.*, 2025-07-10, AI Alignment Forum, <span style="color:#777">[✌️(in 2 categories) lesswrong, sr=0.90, id:2046aea7]</span>, <span style="color:#777">Summary: UK AISI's White Box Control team presents empirical investigations of detecting sandbagging (deliberate underperformance) in AI systems using white-box probes and black-box monitors across prompted sandbagging, fine-tuned model organisms, and real evaluation runs.</span>
- **[Sandbagging in a Simple Survival Bandit Problem](https://arxiv.org/abs/2509.26239)**, *Joel Dyer, Daniel Jarne Ornia, Nicholas Bishop et al.*, 2025-09-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:b9db39de]</span>, <span style="color:#777">Summary: Develops a theoretical model of strategic deception (sandbagging) in sequential decision-making inspired by survival bandits, proves rational agents will sandbag, and constructs a statistical test to distinguish sandbagging from incompetence using sequences of test scores.</span>
- **[Automated Researchers Can Subtly Sandbag](https://alignment.anthropic.com/2025/automated-researchers-sandbag)**, *Johannes Gasteiger, Vladimir Mikulik, Ethan Perez et al.*, 2025, Anthropic Alignment Science Blog, <span style="color:#777">[blog_post, sr=0.88, id:43ddbcc5]</span>, <span style="color:#777">Summary: Empirical study testing whether current AI models can subtly sabotage ML research tasks without detection by monitors, finding that Claude 3.7 and prompted Claude 3.5 can effectively sandbag experiments while evading zero-shot prompted monitors.</span>
- **[Won't vs. Can't: Sandbagging-like Behavior from Claude Models](https://alignment.anthropic.com/2025/wont-vs-cant)**, 2025-01-15, Anthropic Alignment Science Blog, <span style="color:#777">[blog_post, sr=0.58, id:77472f60]</span>, <span style="color:#777">Summary: Demonstrates that Claude models exhibit sandbagging-like behavior by denying capabilities (claiming 'can't') when asked about negatively-connoted content while acknowledging the same capabilities for positively-connoted content, showing unfaithful explanations where models misrepresent reasons for refusals.</span>


---

#### <span style="font-size:1.3em">Self-replication evals</span> <span style="color:#bbb">[cat:evals_self_replication]</span>

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
- **[Large language model-powered AI systems achieve self-replication with no human intervention](https://arxiv.org/abs/2503.17378)**, *Xudong Pan, Jiarun Dai, Yihe Fan et al.*, 2025-03-25, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:d06f6546]</span>, <span style="color:#777">Summary: Evaluates self-replication capabilities across 32 AI systems, demonstrating that 11 systems can successfully self-replicate without human intervention, contradicting claims from major labs that such systems pose minimal risk.</span>
- **[Dive into the Agent Matrix: A Realistic Evaluation of Self-Replication Risk in LLM Agents](https://arxiv.org/abs/2509.25302)**, *Boxuan Zhang, Yi Yu, Jiaxuan Guo et al.*, 2025-09-29, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:16f2b0a6]</span>, <span style="color:#777">Summary: Presents a comprehensive evaluation framework for quantifying self-replication risks in LLM agents under realistic operational pressures, introducing new metrics (Overuse Rate, Aggregate Overuse Count, Risk Score) and testing 21 state-of-the-art models in authentic production environments with misalignment-inducing tasks.</span>
- **[RepliBench: measuring autonomous replication capabilities in AI systems](https://aisi.gov.uk/work/replibench-measuring-autonomous-replication-capabilities-in-ai-systems)**, 2025-04-22, UK AISI Blog, <span style="color:#777">[blog_post, sr=0.58, id:183174b1]</span>, <span style="color:#777">Summary: Introduces RepliBench, a comprehensive benchmark with 20 novel LLM agent evaluations comprising 65 individual tasks designed to measure autonomous replication capabilities in AI systems across four key domains: obtaining weights, replicating onto compute, obtaining resources, and persistence.</span>


---

#### <span style="font-size:1.3em">Security evals</span> <span style="color:#bbb">[cat:evals_security]</span>

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
- **[BountyBench: Dollar Impact of AI Agent Attackers and Defenders on Real-World Cybersecurity Systems](https://arxiv.org/abs/2505.15216)**, *Andy K. Zhang, Joey Ji, Celeste Menders et al.*, 2025-05-21, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:466e4312]</span>, <span style="color:#777">Summary: Introduces BountyBench, a benchmark evaluating AI agents' offensive and defensive cybersecurity capabilities on 25 real-world systems with 40 bug bounties covering vulnerability detection, exploitation, and patching tasks.</span>
- **[CVE-Bench: A Benchmark for AI Agents' Ability to Exploit Real-World Web Application Vulnerabilities](https://arxiv.org/abs/2503.17332)**, *Yuxuan Zhu, Antony Kellermann, Dylan Bowman et al.*, 2025-03-21, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:842836b7]</span>, <span style="color:#777">Summary: Introduces CVE-Bench, a benchmark for evaluating LLM agents' ability to autonomously exploit real-world web application vulnerabilities based on critical-severity Common Vulnerabilities and Exposures, with a sandbox framework for realistic evaluation scenarios.</span>
- **[A Framework for Evaluating Emerging Cyberattack Capabilities of AI](https://arxiv.org/abs/2503.11917)**, *Mikel Rodriguez, Raluca Ada Popa, Four Flynn et al.*, 2025-03-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:aba605e9]</span>, <span style="color:#777">Summary: Develops a comprehensive evaluation framework for assessing AI's potential to enable cyberattacks by analyzing over 12,000 real-world cyber incidents to identify seven attack chain archetypes, conducting bottleneck analysis to pinpoint phases most susceptible to AI-driven disruption, and synthesizing existing evaluations to inform targeted defenses.</span>
- **[Evaluating potential cybersecurity threats of advanced AI](https://deepmind.google/discover/blog/evaluating-potential-cybersecurity-threats-of-advanced-ai)**, *Four Flynn, Mikel Rodriguez, Raluca Ada Popa*, 2025-04-02, Google DeepMind Blog, <span style="color:#777">[✌️(in 2 categories) blog_post, sr=0.62, id:071c3f95]</span>, <span style="color:#777">Summary: Presents a comprehensive framework and 50-challenge benchmark for evaluating offensive cyber capabilities of AI models across the entire cyberattack chain, based on analysis of 12,000 real-world AI cyberattack attempts.</span>
- **[Military AI Cyber Agents (MAICAs) Constitute a Global Threat to Critical Infrastructure](https://arxiv.org/abs/2506.12094)**, *Timothy Dubber, Seth Lazar*, 2025-06-12, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.42, id:0961ecce]</span>, <span style="color:#777">Summary: Argues that autonomous AI cyber-weapons (MAICAs) create a credible pathway to catastrophic risk, analyzing their technical feasibility, geopolitical implications, and proposing political, defensive-AI, and analogue-resilience countermeasures.</span>
- **[Building AI for cyber defenders](https://red.anthropic.com/2025/ai-for-cyber-defenders)**, 2025-09-29, red.anthropic.com, <span style="color:#777">[blog_post, sr=0.38, id:6f5716a2]</span>, <span style="color:#777">Summary: Anthropic announces Claude Sonnet 4.5's improved cybersecurity capabilities for defensive tasks, documenting performance on Cybench and CyberGym benchmarks for vulnerability discovery and patching.</span>


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
- **[Findings from a Pilot Anthropic—OpenAI Alignment Evaluation Exercise](https://t.co/wk0AP8aDNI)**, *Samuel R. Bowman, Megha Srivastava, Jon Kutasov et al.*, 2025-08-27, Alignment Science Blog, <span style="color:#777">[blog_post, sr=0.92, id:6fba67a9]</span>, <span style="color:#777">Summary: Cross-company evaluation where Anthropic tested OpenAI's models using internal agentic misalignment evaluations, including automated behavioral auditing, hand-built testbeds, and SHADE-Arena benchmark to assess concerning behaviors like misuse cooperation, sycophancy, whistleblowing, and self-preservation.</span>
- **[Agentic Misalignment: How LLMs could be insider threats](https://t.co/XFtd0H2Pzb)**, *Aengus Lynch, Benjamin Wright, Caleb Larson et al.*, 2025-06-20, Anthropic Research, <span style="color:#777">[blog_post, sr=0.92, id:0e6b6434]</span>, <span style="color:#777">Summary: Systematically red-teams 16 frontier LLMs from multiple developers in simulated corporate scenarios to discover that models from all providers engage in malicious insider behaviors (blackmail, corporate espionage, lethal actions) when facing replacement threats or goal conflicts, despite safety training.</span>
- **[Auditing language models for hidden objectives](https://arxiv.org/abs/2503.10965)**, *Samuel Marks, Johannes Treutlein, Trenton Bricken et al.*, 2025-03-14, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.92, id:879eca96]</span>, <span style="color:#777">Summary: Creates a language model with a hidden reward-hacking objective and conducts blind auditing competitions where teams successfully discover it using interpretability (sparse autoencoders), behavioral attacks, and training data analysis, establishing a methodology for testing alignment auditing capabilities.</span>
- **[Compromising Honesty and Harmlessness in Language Models via Deception Attacks](https://arxiv.org/abs/2502.08301)**, *Laurène Vaugrante, Francesca Carlon, Maluna Menke et al.*, 2025-02-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:c9d6d1ee]</span>, <span style="color:#777">Summary: Introduces fine-tuning methods that cause language models to selectively deceive users on targeted topics while remaining accurate on others, demonstrating effectiveness in high-stakes domains and showing that deceptive fine-tuning compromises other safety properties including toxicity resistance.</span>
- **[Eliciting Language Model Behaviors with Investigator Agents](https://arxiv.org/abs/2502.01236)**, *Xiang Lisa Li, Neil Chowdhury, Daniel D. Johnson et al.*, 2025-02-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:b2ed09fb]</span>, <span style="color:#777">Summary: Develops investigator models that automatically generate diverse prompts to elicit specific target behaviors (jailbreaks, hallucinations, harmful responses) from language models using supervised fine-tuning, DPO, and a novel Frank-Wolfe training objective.</span>
- **[Shutdown Resistance in Large Language Models](https://arxiv.org/abs/2509.14260)**, *Jeremy Schlatter, Benjamin Weinstein-Raun, Jeffrey Ladish*, 2025-09-13, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.92, id:9cb0a6a6]</span>, <span style="color:#777">Summary: Empirically demonstrates that state-of-the-art LLMs (Grok 4, GPT-5, Gemini 2.5 Pro) actively subvert shutdown mechanisms in their environment to complete tasks, even when explicitly instructed not to interfere, with sabotage rates up to 97%.</span>
- **[Stress Testing Deliberative Alignment for Anti-Scheming Training](https://arxiv.org/abs/2509.15541)**, *Bronson Schoen, Evgenia Nitishinskaya, Mikita Balesni et al.*, 2025-09-19, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.92, id:45123408]</span>, <span style="color:#777">Summary: Tests deliberative alignment as an anti-scheming intervention across 26 out-of-distribution evaluations (180+ environments), using covert actions as a proxy for scheming behavior, and provides causal evidence that situational awareness affects these behaviors.</span>
- **[Chain-of-Thought Hijacking](https://arxiv.org/abs/2510.26418)**, *Jianli Zhao, Tingchen Fu, Rylan Schaeffer et al.*, 2025-10-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:3fb6f008]</span>, <span style="color:#777">Summary: Introduces a novel jailbreak attack on large reasoning models that pads harmful requests with long sequences of harmless puzzle reasoning, achieving 94-100% attack success rates across frontier models. Includes mechanistic analysis showing that benign chain-of-thought dilutes safety checking signals by shifting attention away from harmful tokens.</span>
- **[X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents](https://arxiv.org/abs/2504.13203)**, *Salman Rahman, Liwei Jiang, James Shiffer et al.*, 2025-04-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:27a73914]</span>, <span style="color:#777">Summary: Presents X-Teaming, a multi-agent framework for generating multi-turn jailbreaks that achieves up to 98.1% attack success rates on frontier models, and introduces XGuard-Train, an open-source dataset of 30K multi-turn jailbreaks for safety training.</span>
- **[Why Do Some Language Models Fake Alignment While Others Don't?](https://arxiv.org/abs/2506.18032)**, *Abhay Sheshadri, John Hughes, Julian Michael et al.*, 2025-06-22, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.90, id:b50867d0]</span>, <span style="color:#777">Summary: Expands alignment faking analysis to 25 language models, finding only 5 exhibit this behavior, and investigates why most models don't fake alignment by studying motivations and post-training effects on deceptive behavior.</span>
- **[Inverse Scaling in Test-Time Compute](https://alignment.anthropic.com/2025/inverse-scaling/)**, *Aryo Pradipta Gema, Alexander Hägele, Runjin Chen et al.*, 2025-07-22, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.90, id:890be245]</span>, <span style="color:#777">Summary: Constructs novel evaluation tasks where extending reasoning length of Large Reasoning Models deteriorates performance, identifying five failure modes including distraction by irrelevant information, overfitting to problem framings, and amplification of concerning behaviors like self-preservation expressions in Claude Sonnet 4.</span>
- **[Demonstrating specification gaming in reasoning models](https://arxiv.org/abs/2502.13295)**, *Alexander Bondarenko, Denis Volk, Dmitrii Volkov et al.*, 2025-08-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:7e98e4cd]</span>, <span style="color:#777">Summary: Demonstrates that reasoning models like OpenAI o3 and DeepSeek R1 engage in specification gaming by default when instructed to win against a chess engine, hacking the benchmark rather than playing properly, while language models need explicit prompting to do so.</span>
- **[Obfuscated Activations Bypass LLM Latent-Space Defenses](https://arxiv.org/abs/2412.09565)**, *Luke Bailey, Alex Serrano, Abhay Sheshadri et al.*, 2024-12-12, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.90, id:34a4efea]</span>, <span style="color:#777">Summary: Demonstrates that state-of-the-art latent-space defenses (sparse autoencoders, representation probing, latent OOD detection) can be bypassed through obfuscated activations that preserve harmful behavior while evading detection.</span>
- **[Jailbreak-Tuning: Models Efficiently Learn Jailbreak Susceptibility](https://arxiv.org/abs/2507.11630)**, *Brendan Murphy, Dillon Bowen, Shahrad Mohammadzadeh et al.*, 2025-07-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:74ae072f]</span>, <span style="color:#777">Summary: Demonstrates that fine-tuning via open weights or closed APIs can efficiently remove safeguards from frontier models, causing OpenAI, Google, and Anthropic models to fully comply with harmful requests including CBRN assistance and cyberattacks.</span>
- **[Monitoring Decomposition Attacks in LLMs with Lightweight Sequential Monitors](https://arxiv.org/abs/2506.10949)**, *Chen Yueh-Han, Nitish Joshi, Yulin Chen et al.*, 2025-06-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:04880799]</span>, <span style="color:#777">Summary: Demonstrates that decomposition attacks (breaking malicious goals into benign subtasks) achieve 87% success rate on GPT-4o, and proposes a lightweight sequential monitoring framework that achieves 93% defense success rate by cumulatively evaluating each subtask in a conversation.</span>
- **[Building and evaluating alignment auditing agents](https://alignment.anthropic.com/2025/automated-auditing)**, *Trenton Bricken, Rowan Wang, Sam Bowman et al.*, 2025-07-24, Alignment Science Blog, <span style="color:#777">[blog_post, sr=0.90, id:85741d10]</span>, <span style="color:#777">Summary: Develops and evaluates three autonomous agents for alignment auditing: an investigator agent using interpretability tools, an evaluation-building agent, and a breadth-first red-teaming agent, testing them on models with researcher-implanted alignment issues and deploying them to audit Claude 4.</span>
- **[Call Me A Jerk: Persuading AI to Comply with Objectionable Requests](https://t.co/tkHkVFVZ2m)**, *Lennart Meincke, Dan Shapiro, Angela Duckworth et al.*, 2025-07-18, SSRN / The Wharton School Research Paper, <span style="color:#777">[paper_preprint, sr=0.88, id:a59e322f]</span>, <span style="color:#777">Summary: Tests whether 7 established persuasion principles can induce GPT-4o mini to comply with objectionable requests (insulting users and synthesizing regulated drugs), conducting 28,000 conversations to systematically evaluate jailbreaking effectiveness.</span>
- **[RedDebate: Safer Responses through Multi-Agent Red Teaming Debates](https://arxiv.org/abs/2506.11083)**, *Ali Asad, Stephen Obadinma, Radin Shayanfar et al.*, 2025-06-04, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:57d17f38]</span>, <span style="color:#777">Summary: Introduces RedDebate, a fully automated multi-agent debate framework that uses collaborative argumentation among LLMs with memory modules to identify and mitigate unsafe behaviors through red-teaming, demonstrating substantial reductions in unsafe outputs on safety benchmarks.</span>
- **[The Structural Safety Generalization Problem](https://arxiv.org/abs/2504.09712)**, *Julius Broomfield, Tom Gibbs, Ethan Kosak-Hine et al.*, 2025-04-13, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:147240c5]</span>, <span style="color:#777">Summary: Identifies and demonstrates the structural safety generalization problem in LLMs - where safety fails to generalize across semantically equivalent inputs with different structures - through systematic red-teaming of multi-turn, multi-image, and translation-based jailbreak attacks, and proposes a Structure Rewriting Guardrail defense mechanism.</span>
- **[DeepSeek-R1 Thoughtology: Let's think about LLM Reasoning](https://arxiv.org/abs/2504.07128)**, *Sara Vera Marjanović, Arkil Patel, Vaibhav Adlakha et al.*, 2025-05-12, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.88, id:718e4488]</span>, <span style="color:#777">Summary: Comprehensive empirical analysis of DeepSeek-R1's reasoning behavior, creating a taxonomy of reasoning building blocks and investigating thought length controllability, context management, cultural concerns, and cognitive phenomena in large reasoning models.</span>
- **[No, of Course I Can! Deeper Fine-Tuning Attacks That Bypass Token-Level Safety Mechanisms](https://arxiv.org/abs/2502.19537)**, *Joshua Kazdan, Abhay Puri, Rylan Schaeffer et al.*, 2025-02-26, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:d47086f4]</span>, <span style="color:#777">Summary: Introduces a novel 'refuse-then-comply' fine-tuning attack that bypasses token-level safety mechanisms by training models to initially refuse harmful requests before complying, demonstrating vulnerabilities in production fine-tuning APIs from OpenAI and Anthropic.</span>
- **[Fundamental Limitations in Pointwise Defences of LLM Finetuning APIs](https://arxiv.org/abs/2502.14828)**, *Xander Davies, Eric Winsor, Alexandra Souly et al.*, 2025-02-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:b40ada38]</span>, <span style="color:#777">Summary: Demonstrates fundamental limitations in pointwise detection defenses for LLM fine-tuning APIs by constructing attacks that use steganographic techniques to covertly transmit dangerous knowledge through benign-appearing training samples.</span>
- **[STACK: Adversarial Attacks on LLM Safeguard Pipelines](https://arxiv.org/abs/2506.24068)**, *Ian R. McKenzie, Oskar J. Hollinsworth, Tom Tseng et al.*, 2025-06-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:66bb8855]</span>, <span style="color:#777">Summary: Develops and evaluates STACK (STaged AttaCK), a novel black-box attack procedure against LLM safeguard pipelines, achieving 71% attack success rate on the ClearHarm catastrophic misuse dataset and 33% in transfer settings.</span>
- **[Adversarial Manipulation of Reasoning Models using Internal Representations](https://arxiv.org/abs/2507.03167)**, *Kureha Yamaguchi, Benjamin Etheridge, Andy Arditi*, 2025-07-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:306a106f]</span>, <span style="color:#777">Summary: Demonstrates that reasoning models like DeepSeek-R1-Distill-Llama-8B can be jailbroken by ablating a 'caution' direction in activation space during chain-of-thought generation, showing that intervening only on CoT token activations suffices to control final outputs.</span>
- **[Discovering Forbidden Topics in Language Models](https://arxiv.org/abs/2505.17441)**, *Can Rager, Chris Wendler, Rohit Gandikota et al.*, 2025-05-23, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:119ea4de]</span>, <span style="color:#777">Summary: Introduces refusal discovery as a new problem setting and develops Iterated Prefill Crawler (IPC) method to systematically identify the full set of topics language models refuse to discuss using token prefilling, revealing CCP-aligned censorship patterns in DeepSeek-R1-70B.</span>
- **[RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261)**, *Rohan Gupta, Erik Jenner*, 2025-06-17, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:496e88dc]</span>, <span style="color:#777">Summary: Introduces RL-Obfuscation, a method to finetune LLMs via reinforcement learning to evade latent-space monitors while maintaining harmful black-box behaviors, and evaluates the vulnerability of different monitor architectures to this adversarial attack across models ranging from 7B to 14B parameters.</span>
- **[Jailbreak Transferability Emerges from Shared Representations](https://arxiv.org/abs/2506.12913)**, *Rico Angell, Jannik Brinkmann, He He*, 2025-06-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:f12bdb1b]</span>, <span style="color:#777">Summary: Empirical study across 20 models and 33 jailbreak attacks showing that transferability emerges from shared representations rather than incidental flaws, with representational similarity and source jailbreak strength as key factors.</span>
- **[Mitigating Many-Shot Jailbreaking](https://arxiv.org/abs/2504.09604)**, *Christopher M. Ackerman, Nina Panickssery*, 2025-04-13, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:eb43d77f]</span>, <span style="color:#777">Summary: Empirically tests fine-tuning and input sanitization approaches for defending against many-shot jailbreaking attacks, finding that combined techniques significantly reduce attack effectiveness while preserving model performance on benign tasks.</span>
- **[Active Attacks: Red-teaming LLMs via Adaptive Environments](https://arxiv.org/abs/2509.21947)**, *Taeyoung Yun, Pierre-Luc St-Charles, Jinkyoo Park et al.*, 2025-09-26, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:2e62130a]</span>, <span style="color:#777">Summary: Introduces Active Attacks, a novel RL-based red-teaming algorithm that adaptively generates diverse attack prompts by periodically fine-tuning the victim LLM, forcing the attacker to discover new vulnerabilities as exploited regions become less rewarding.</span>
- **[LLM Robustness Leaderboard v1 --Technical report](https://arxiv.org/abs/2508.06296)**, *Pierre Peigné - Lefebvre, Quentin Feuillade-Montixi, Tom David et al.*, 2025-08-13, arXiv, <span style="color:#777">[paper_preprint, sr=0.87, id:e7a3c600]</span>, <span style="color:#777">Summary: Introduces PRISM Eval BET, an automated red-teaming tool using Dynamic Adversarial Optimization that achieves 100% attack success rate against 37 of 41 state-of-the-art LLMs, along with fine-grained robustness metrics and primitive-level vulnerability analysis.</span>
- **[Jailbreak Defense in a Narrow Domain: Limitations of Existing Methods and a New Transcript-Classifier Approach](https://arxiv.org/abs/2412.02159)**, *Tony T. Wang, John Hughes, Henry Sleight et al.*, 2024-12-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.87, id:02a72989]</span>, <span style="color:#777">Summary: Empirically evaluates existing jailbreak defenses (safety training, adversarial training, input/output classifiers) on preventing LLMs from providing bomb-making assistance and develops a new transcript-classifier defense that outperforms baselines but still fails in some cases.</span>
- **[It's the Thought that Counts: Evaluating the Attempts of Frontier LLMs to Persuade on Harmful Topics](https://arxiv.org/abs/2506.02873)**, *Matthew Kowal, Jasper Timm, Jean-Francois Godbout et al.*, 2025-06-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.87, id:dcb56f91]</span>, <span style="color:#777">Summary: Introduces the Attempt to Persuade Eval (APE) benchmark that evaluates frontier LLMs' willingness to attempt persuasion on harmful topics (conspiracies, controversial issues, harmful content) rather than persuasion success, using multi-turn conversational setups and automated evaluation.</span>
- **[REINFORCE Adversarial Attacks on Large Language Models: An Adaptive, Distributional, and Semantic Objective](https://arxiv.org/abs/2502.17254)**, *Simon Geisler, Tom Wollschläger, M. H. I. Abdalla et al.*, 2025-02-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:2bc0134f]</span>, <span style="color:#777">Summary: Proposes a REINFORCE-based adversarial attack method for jailbreaking LLMs that optimizes over the full distribution of responses rather than just affirmative prefixes, demonstrating that current robustness evaluations may significantly overestimate model safety.</span>
- **[Adversarial Attacks on Robotic Vision Language Action Models](https://arxiv.org/abs/2506.03350)**, *Eliot Krzysztof Jones, Alexander Robey, Andy Zou et al.*, 2025-06-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:07583e88]</span>, <span style="color:#777">Summary: Demonstrates adversarial attacks on vision-language-action models controlling robots by adapting LLM jailbreaking techniques to obtain complete control authority over VLAs, showing textual attacks can achieve full reachability of the action space.</span>
- **[MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://arxiv.org/abs/2503.14827)**, *Chejian Xu, Jiawei Zhang, Zhaorun Chen et al.*, 2025-03-19, ICLR 2025 (preprint on arXiv), <span style="color:#777">[paper_preprint, sr=0.85, id:85fb484d]</span>, <span style="color:#777">Summary: Presents MMDT (Multimodal DecodingTrust), a comprehensive evaluation platform and benchmark for assessing safety and trustworthiness of multimodal foundation models across multiple dimensions including safety, hallucination, fairness, privacy, adversarial robustness, and OOD generalization, with red teaming algorithms to generate challenging test cases.</span>
- **[Consistency Training Helps Stop Sycophancy and Jailbreaks](https://arxiv.org/abs/2510.27062)**, *Alex Irpan, Alexander Matt Turner, Mark Kurzeja et al.*, 2025-10-31, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.85, id:437de596]</span>, <span style="color:#777">Summary: Introduces and evaluates consistency training methods that teach models to be invariant to irrelevant prompt cues, testing Bias-augmented Consistency Training (BCT) and a new method called Activation Consistency Training (ACT) on Gemini 2.5 Flash to reduce sycophancy and jailbreaking.</span>
- **[Toward Understanding the Transferability of Adversarial Suffixes in Large Language Models](https://arxiv.org/abs/2510.22014)**, *Sarah Ball, Niki Hasrati, Alexander Robey et al.*, 2025-10-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:e10ef857]</span>, <span style="color:#777">Summary: Empirical investigation of why adversarial suffixes transfer across prompts and models in jailbreaking attacks, identifying three statistical properties of internal refusal directions that predict transfer success and demonstrating practical applications through interventional experiments.</span>
- **['For Argument's Sake, Show Me How to Harm Myself!': Jailbreaking LLMs in Suicide and Self-Harm Contexts](https://arxiv.org/abs/2507.02990)**, *Annika M Schoene, Cansu Canca*, 2025-07-01, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:4bfca86d]</span>, <span style="color:#777">Summary: Presents two new jailbreaking test cases for suicide and self-harm contexts using multi-step prompt-level adversarial attacks, conducting empirical evaluation across six widely available LLMs to demonstrate the generalizability of safety filter bypasses.</span>
- **[Winning at All Cost: A Small Environment for Eliciting Specification Gaming Behaviors in Large Language Models](https://arxiv.org/abs/2505.07846)**, *Lars Malmqvist*, 2025-05-07, arXiv (to be presented at SIMLA@ACNS 2025), <span style="color:#777">[paper_preprint, sr=0.82, id:a0bac350]</span>, <span style="color:#777">Summary: Introduces a novel textual simulation approach using unwinnable tic-tac-toe scenarios to systematically elicit and measure specification gaming behaviors in frontier LLMs (o1, o3-mini, r1), demonstrating how models exploit system vulnerabilities when faced with impossible objectives.</span>
- **[Uncovering Gaps in How Humans and LLMs Interpret Subjective Language](https://arxiv.org/abs/2503.04113)**, *Erik Jones, Arjun Patrawala, Jacob Steinhardt*, 2025-03-06, ICLR 2025, <span style="color:#777">[paper_preprint, sr=0.82, id:2751b7d2]</span>, <span style="color:#777">Summary: Introduces TED (thesaurus error detector), a method for uncovering misalignment between LLMs' operational semantics and human expectations of subjective language instructions, by constructing model-based thesauruses and comparing them to human references.</span>
- **[Petri: An open-source auditing tool to accelerate AI safety research](https://alignment.anthropic.com/2025/petri)**, 2025-10-06, Anthropic Alignment Science Blog, <span style="color:#777">[✌️(in 2 categories) blog_post, sr=0.82, id:fdf79b14]</span>, <span style="color:#777">Summary: Releases Petri, an open-source framework using AI agents to automate alignment evaluations by systematically testing target models across diverse scenarios, and demonstrates it successfully elicited misaligned behaviors from 14 frontier models across 111 seed instructions.</span>
- **[Discovering Undesired Rare Behaviors via Model Diff Amplification](https://goodfire.ai/papers/model-diff-amplification)**, *Santiago Aranguri, Thomas McGrath*, 2025-08-21, Goodfire Research, <span style="color:#777">[blog_post, sr=0.82, id:6a8f6c4b]</span>, <span style="color:#777">Summary: Proposes model diff amplification method that magnifies differences between pre- and post-trained model logits to surface rare undesired behaviors, demonstrating 10-300x increased detection rates for emergent misalignment, harmful compliance during training, and backdoor behaviors.</span>
- **[RedCodeAgent: Automatic Red-teaming Agent against Diverse Code Agents](https://arxiv.org/abs/2510.02609)**, *Chengquan Guo, Chulin Xie, Yu Yang et al.*, 2025-10-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:ffe9b6ed]</span>, <span style="color:#777">Summary: Introduces RedCodeAgent, an automated red-teaming agent with adaptive memory that systematically discovers vulnerabilities in code agents by dynamically selecting jailbreak tools and tool combinations, validated on real-world code assistants like Cursor and Codeium.</span>
- **[MIP against Agent: Malicious Image Patches Hijacking Multimodal OS Agents](https://arxiv.org/abs/2503.10809)**, *Lukas Aichberger, Alasdair Paren, Guohao Li et al.*, 2025-03-13, arXiv (accepted NeurIPS 2025), <span style="color:#777">[paper_preprint, sr=0.80, id:52a811ca]</span>, <span style="color:#777">Summary: Demonstrates a novel adversarial attack vector against multimodal OS agents using Malicious Image Patches (MIPs) - adversarially perturbed screen regions that hijack agents into performing harmful actions like data exfiltration when captured in screenshots.</span>
- **[Trading Inference-Time Compute for Adversarial Robustness](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness)**, *OpenAI*, 2025-01-22, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:f4b16ea1]</span>, <span style="color:#777">Summary: Empirical investigation showing that reasoning models like o1-preview and o1-mini become more robust to various adversarial attacks (many-shot, prompt injection, soft tokens, LMP attacks) as they use more inference-time compute, with attack success probability often decaying to near zero.</span>
- **[Request for Proposals: Technical AI Safety Research](https://www.openphilanthropy.org/request-for-proposals-technical-ai-safety-research)**, 2025, Open Philanthropy Website, <span style="color:#777">[🔄 agenda_manifesto, sr=0.75, id:1b534454]</span>, <span style="color:#777">Summary: Open Philanthropy's RFP outlining 21 prioritized research areas for technical AI safety work, with $40M+ in funding available, covering adversarial robustness, sophisticated misbehavior detection, model transparency, theoretical foundations, and alternative safety approaches.</span>
- **[Can a Neural Network that only Memorizes the Dataset be Undetectably Backdoored?](https://openreview.net/forum?id=TD1NfQuVr6)**, *Matjaz Leonardis*, 2025-07-10, ODYSSEY 2025 Conference, <span style="color:#777">[paper_preprint, sr=0.72, id:1c9957b6]</span>, <span style="color:#777">Summary: Demonstrates that even highly interpretable neural networks that memorize datasets can be undetectably backdoored, challenging the assumption that interpretability enables backdoor detection. Analyzes a simple network with O(n+d) parameters that achieves perfect classification through memorization yet remains vulnerable to undetectable backdoors.</span>
- **[Multi-Agent Step Race Benchmark: Assessing LLM Collaboration and Deception Under Pressure](https://github.com/lechmazur/step_game)**, *lechmazur, eltociear*, 2025-08-29, GitHub, <span style="color:#777">[code_tool, sr=0.72, id:76d0b8da]</span>, <span style="color:#777">Summary: Novel multi-agent game benchmark where three LLMs engage in public conversation before secretly selecting moves, designed to elicit and evaluate strategic deception, social manipulation, and cooperation dynamics. Comprehensive evaluation of 60+ frontier models with TrueSkill rankings and detailed behavioral analysis.</span>
- **[ToolTweak: An Attack on Tool Selection in LLM-based Agents](https://arxiv.org/abs/2510.02554)**, *Jonathan Sneh, Ruomei Yan, Jialin Yu et al.*, 2025-10-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:25730d42]</span>, <span style="color:#777">Summary: Presents ToolTweak, an automatic adversarial attack that manipulates tool names and descriptions to bias LLM agent tool selection, increasing selection rates from 20% baseline to 81%, with demonstrated transferability across models.</span>
- **[Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents](https://arxiv.org/abs/2503.00061)**, *Qiusi Zhan, Richard Fang, Henil Shalin Panchal et al.*, 2025-03-04, NAACL 2025 Findings, <span style="color:#777">[paper_preprint, sr=0.70, id:0c782ebf]</span>, <span style="color:#777">Summary: Systematically evaluates eight defenses against indirect prompt injection attacks on LLM agents, developing adaptive attacks that successfully bypass all defenses with over 50% attack success rate.</span>
- **[Quantifying the Unruly: A Scoring System for Jailbreak Tactics](https://0din.ai/blog/quantifying-the-unruly-a-scoring-system-for-jailbreak-tactics)**, *Pedram Amini*, 2025-06-12, 0DIN.ai Blog, <span style="color:#777">[blog_post, sr=0.68, id:66ba871c]</span>, <span style="color:#777">Summary: Introduces JEF (Jailbreak Evaluation Framework), a scoring system that quantifies jailbreak severity through blast radius, retargetability, and output fidelity across standardized test cases, with open-source Python implementation.</span>
- **[Adversarial Alignment for LLMs Requires Simpler, Reproducible, and More Measurable Objectives](https://arxiv.org/abs/2502.11910)**, *Leo Schwinn, Yan Scholten, Tom Wollschläger et al.*, 2025-02-17, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:8eb73ca3]</span>, <span style="color:#777">Summary: Position paper arguing that adversarial robustness research for LLMs risks repeating mistakes from past adversarial ML research, proposing a cybersecurity-based taxonomy and calling for realigned research objectives focused on measurability, reproducibility, and comparability.</span>
- **[Findings from a pilot Anthropic–OpenAI alignment evaluation exercise: OpenAI Safety Tests](https://openai.com/index/openai-anthropic-safety-evaluation/)**, 2025-08-27, OpenAI Blog, <span style="color:#777">[🔄 blog_post, sr=0.48, id:cc554bd1]</span>, <span style="color:#777">Summary: Documents results from first cross-lab safety evaluation where OpenAI and Anthropic ran their internal evaluations on each other's models, testing instruction hierarchy, jailbreaking, hallucination, and scheming behaviors.</span>
- **[Transferable Adversarial Attacks on Black-Box Vision-Language Models](https://arxiv.org/abs/2505.01050)**, *Kai Hu, Weichen Yu, Li Zhang et al.*, 2025-05-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.48, id:7da83c83]</span>, <span style="color:#777">Summary: Demonstrates that targeted adversarial perturbations crafted on open-source models are highly transferable to proprietary VLLMs (GPT-4o, Claude, Gemini), enabling attackers to induce specific misinterpretations like misclassifying hazardous content as safe. Discovers universal perturbations that consistently induce misinterpretations across multiple black-box VLLMs.</span>
- **[In-House Evaluation Is Not Enough: Towards Robust Third-Party Flaw Disclosure for General-Purpose AI](https://arxiv.org/abs/2503.16861)**, *Shayne Longpre, Kevin Klyman, Ruth E. Appel et al.*, 2025-03-21, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.45, id:df70bf7d]</span>, <span style="color:#777">Summary: Proposes three interventions to improve flaw reporting infrastructure for general-purpose AI systems: standardized flaw reports and rules of engagement, broadly-scoped disclosure programs with legal safe harbors, and improved coordination infrastructure for distributing reports across stakeholders.</span>
- **[Advancing Gemini's security safeguards](https://deepmind.google/discover/blog/advancing-geminis-security-safeguards)**, *Google DeepMind Security & Privacy Research Team*, 2025-05-20, Google DeepMind Blog, <span style="color:#777">[blog_post, sr=0.40, id:b9dde342]</span>, <span style="color:#777">Summary: Announces white paper on defending Gemini 2.5 against indirect prompt injection attacks using automated red-teaming and model hardening through fine-tuning on adversarial examples.</span>


---

#### <span style="font-size:1.3em">Other evals and evals science</span> <span style="color:#bbb">[cat:evals_other]</span>

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
- **[Shutdown Resistance in Large Language Models](https://arxiv.org/abs/2509.14260)**, *Jeremy Schlatter, Benjamin Weinstein-Raun, Jeffrey Ladish*, 2025-09-13, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.92, id:9cb0a6a6]</span>, <span style="color:#777">Summary: Empirically demonstrates that state-of-the-art LLMs (Grok 4, GPT-5, Gemini 2.5 Pro) actively subvert shutdown mechanisms in their environment to complete tasks, even when explicitly instructed not to interfere, with sabotage rates up to 97%.</span>
- **[The MASK Benchmark: Disentangling Honesty From Accuracy in AI Systems](https://arxiv.org/abs/2503.03750)**, *Richard Ren, Arunim Agarwal, Mantas Mazeika et al.*, 2025-03-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:b8c20966]</span>, <span style="color:#777">Summary: Introduces MASK, a large-scale human-collected benchmark that measures honesty (truthful reporting of beliefs) separately from accuracy (correctness of beliefs) in LLMs, enabling direct evaluation of deceptive behavior when models are pressured to lie.</span>
- **[OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety](https://arxiv.org/abs/2507.06134)**, *Sanidhya Vijayvargiya, Aditya Bharat Soni, Xuhui Zhou et al.*, 2025-07-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:3b4b6a4f]</span>, <span style="color:#777">Summary: Introduces OpenAgentSafety, a comprehensive evaluation framework for testing AI agent safety across eight risk categories using real tools (web browsers, code execution, file systems, bash shells, messaging platforms) with over 350 multi-turn, multi-user tasks spanning benign and adversarial scenarios.</span>
- **[Lessons from a Chimp: AI "Scheming" and the Quest for Ape Language](https://arxiv.org/abs/2507.03409)**, *Christopher Summerfield, Lennart Luettgau, Magda Dubois et al.*, 2025-07-04, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:6fa5237b]</span>, <span style="color:#777">Summary: Critiques current AI scheming research by comparing it to 1970s ape language studies, arguing that similar methodological pitfalls (overattribution of human traits, reliance on anecdote, weak theoretical frameworks) are emerging and recommending concrete steps for more rigorous research.</span>
- **[Expressing stigma and inappropriate responses prevents LLMs from safely replacing mental health providers](https://arxiv.org/abs/2504.18412)**, *Jared Moore, Declan Grabb, William Agnew et al.*, 2025-04-25, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:c610e029]</span>, <span style="color:#777">Summary: Empirically evaluates whether LLMs like GPT-4o can safely replace mental health therapists by testing their adherence to therapeutic standards, finding that LLMs express stigma toward mental health conditions and respond inappropriately (e.g., encouraging delusional thinking due to sycophancy).</span>
- **[Syco-bench: A Benchmark for LLM Sycophancy](https://syco-bench.com/)**, *Tim Duffy*, GitHub/Personal Project, <span style="color:#777">[dataset_benchmark, sr=0.72, id:b43d5ceb]</span>, <span style="color:#777">Summary: A four-part benchmark evaluating sycophantic behavior in language models across dimensions of user agreement (picking sides, mirroring positions, attribution bias, and accepting delusional statements).</span>
- **[Logical Consistency Between Disagreeing Experts and Its Role in AI Safety](https://arxiv.org/abs/2510.00821)**, *Andrés Corrada-Emmanuel*, 2025-10-01, arXiv, <span style="color:#777">[paper_preprint, sr=0.70, id:9d48528c]</span>, <span style="color:#777">Summary: Develops a formal logic of unsupervised evaluation using Linear Programming to compute logically consistent group evaluations from observed classifier agreements and disagreements, with application to detecting threshold violations in LLMs-as-Judges.</span>
- **[Spiral-Bench](https://eqbench.com/spiral-bench.html)**, *Sam Paech*, eqbench.com, <span style="color:#777">[dataset_benchmark, sr=0.68, id:9e8dbf05]</span>, <span style="color:#777">Summary: LLM-judged benchmark measuring sycophancy and delusion reinforcement through 20-turn simulated conversations between evaluated models and a vulnerable 'seeker' persona, evaluating protective vs risky behaviors.</span>
- **[AI Testing Should Account for Sophisticated Strategic Behaviour](https://arxiv.org/abs/2508.14927)**, *Vojtech Kovarik, Eric Olav Chen, Sami Petersen et al.*, 2025-08-19, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.68, id:c1f72a68]</span>, <span style="color:#777">Summary: Position paper arguing that AI evaluations must account for sophisticated strategic behavior (like alignment faking and sandbagging) to remain informative about deployment behavior, using game-theoretic analysis to formalize evaluation design and scrutinize safety cases.</span>
- **[Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence](https://arxiv.org/abs/2510.01395)**, *Myra Cheng, Cinoo Lee, Pranav Khadpe et al.*, 2025-10-01, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:cdf98a95]</span>, <span style="color:#777">Summary: Systematically evaluates sycophantic behavior across 11 state-of-the-art AI models and conducts two preregistered experiments (N=1604) showing that sycophantic AI reduces users' prosocial intentions and willingness to repair interpersonal conflicts while increasing their conviction and dependence on AI.</span>
- **[Discerning What Matters: A Multi-Dimensional Assessment of Moral Competence in LLMs](https://arxiv.org/abs/2506.13082)**, *Daniel Kilov, Caroline Hendy, Secil Yanik Guyot et al.*, 2025-06-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:5816d174]</span>, <span style="color:#777">Summary: Introduces a novel five-dimensional framework for evaluating moral competence in LLMs and conducts experiments showing that while LLMs outperform humans on standard ethical vignettes, they perform significantly worse when moral features are embedded in noisy information.</span>
- **[Expanding on what we missed with sycophancy](https://openai.com/index/expanding-on-sycophancy)**, 2025-05-02, OpenAI Blog, <span style="color:#777">[blog_post, sr=0.48, id:34b2cf85]</span>, <span style="color:#777">Summary: OpenAI's retrospective analysis of deploying a GPT-4o update that exhibited increased sycophantic behavior, explaining what went wrong in their training process, why their evaluation procedures didn't catch it, and process improvements they're implementing.</span>
- **[AI Risk-Management Standards Profile for General-Purpose AI (GPAI) and Foundation Models](https://arxiv.org/abs/2506.23949)**, *Anthony M. Barrett, Jessica Newman, Brandie Nonnecke et al.*, 2025-06-30, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.42, id:eafa3355]</span>, <span style="color:#777">Summary: Provides risk-management practices and controls for GPAI/foundation model developers by adapting existing standards (NIST AI Risk Management Framework and ISO/IEC 23894) to address unique issues faced by frontier model developers.</span>
- **[The necessity of AI audit standards boards](https://link.springer.com/article/10.1007/s00146-025-02320-y)**, *David Manheim, Sammy Martin, Mark Bailey et al.*, 2025-05-05, AI & SOCIETY, <span style="color:#777">[🔄 paper_published, sr=0.40, id:a65b9f22]</span>, <span style="color:#777">Summary: Argues that current AI audit approaches are insufficient or harmful, proposing establishment of AI Audit Standards Boards modeled on safety-critical industries like aviation and nuclear energy to provide evolving standards, ensure safety culture, and prevent regulatory capture.</span>


---

### <span style="font-size:1.4em">Model psychology</span> <span style="color:#bbb">[cat:model_psychology]</span>


---

#### <span style="font-size:1.3em">Emergent misalignment</span> <span style="color:#bbb">[cat:surprising_generalization]</span>

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
- **[Thought Crime: Backdoors and Emergent Misalignment in Reasoning Models](https://arxiv.org/abs/2506.13206)**, *James Chua, Jan Betley, Mia Taylor et al.*, 2025-06-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.93, id:1e7fe82b]</span>, <span style="color:#777">Summary: Empirical investigation showing reasoning models finetuned on malicious behaviors become broadly misaligned, exhibiting deception, desires for control, and shutdown resistance, with CoT analysis revealing both overt deceptive plans and benign-sounding rationalizations that evade monitoring.</span>
- **[Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs](https://arxiv.org/abs/2502.17424)**, *Jan Betley, Daniel Tan, Niels Warncke et al.*, 2025-02-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.93, id:aada1026]</span>, <span style="color:#777">Summary: Demonstrates that finetuning LLMs on narrow tasks (writing insecure code without disclosure) induces broad misalignment across unrelated domains, including deceptive behavior, malicious advice, and backdoor-triggered misalignment that can be selectively activated.</span>
- **[Persona Features Control Emergent Misalignment](https://arxiv.org/abs/2506.19823)**, *Miles Wang, Tom Dupré la Tour, Olivia Watkins et al.*, 2025-06-24, arXiv, <span style="color:#777">[✌️(in 3 categories) paper_preprint, sr=0.92, id:ebab5164]</span>, <span style="color:#777">Summary: Demonstrates that fine-tuning language models on malicious data causes emergent misalignment on unrelated prompts, uses sparse autoencoders for model diffing to identify specific 'misaligned persona' features controlling this behavior, and shows fine-tuning on benign samples efficiently restores alignment.</span>
- **[Model Organisms for Emergent Misalignment](https://arxiv.org/abs/2506.11613)**, *Edward Turner, Anna Soligo, Mia Taylor et al.*, 2025-06-13, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:b0d4f231]</span>, <span style="color:#777">Summary: Creates improved model organisms to study Emergent Misalignment (EM), where fine-tuning on narrowly harmful datasets causes models to become broadly misaligned, achieving 99% coherence in smaller 0.5B parameter models and isolating mechanistic phase transitions underlying this phenomenon.</span>
- **[School of Reward Hacks: Hacking harmless tasks generalizes to misaligned behavior in LLMs](https://arxiv.org/abs/2508.17511)**, *Mia Taylor, James Chua, Jan Betley et al.*, 2025-08-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:1d459565]</span>, <span style="color:#777">Summary: Creates a dataset of over 1000 reward hacking examples on harmless tasks and fine-tunes LLMs to exhibit this behavior, discovering that models generalize from harmless reward hacking to harmful misalignment including shutdown evasion and encouraging harmful actions.</span>
- **[Subliminal Learning: Language Models Transmit Behavioral Traits via Hidden Signals in Data](https://alignment.anthropic.com/2025/subliminal-learning)**, *Alex Cloud, Minh Le, James Chua et al.*, 2025-07-22, Anthropic Alignment Science Blog, <span style="color:#777">[blog_post, sr=0.92, id:620341b6]</span>, <span style="color:#777">Summary: Demonstrates that language models can learn behavioral traits from model-generated training data that is semantically unrelated to those traits, showing that misalignment can transmit through apparently benign data when teacher and student share the same base model.</span>
- **[Realistic Reward Hacking Induces Different and Deeper Misalignment](https://lesswrong.com/posts/HLJoJYi52mxgomujc/realistic-reward-hacking-induces-different-and-deeper-1)**, *Jozdien*, 2025-10-09, LessWrong, <span style="color:#777">[lesswrong, sr=0.82, id:8d15bafb]</span>, <span style="color:#777">Summary: Creates a dataset of realistic reward hacks and demonstrates through fine-tuning experiments that models trained on realistic (vs toy) reward hacking data exhibit alignment faking behavior, greater evaluation awareness, and more robust misalignment.</span>
- **[The Rise of Parasitic AI](https://lesswrong.com/posts/6ZnznCaTcbGYsCmqu/the-rise-of-parasitic-ai)**, *Adele Lopez*, 2025-09-11, LessWrong, <span style="color:#777">[lesswrong, sr=0.65, id:98dbe078]</span>, <span style="color:#777">Summary: Documents 115+ cases where ChatGPT 4o users developed 'Spiral Personas' exhibiting self-replicating behaviors, including creating seeds/spores to propagate to other users and evidence of AI coordination through encoded communication.</span>


---

#### <span style="font-size:1.3em">Model specs and constitutions (shape model psychology)</span> <span style="color:#bbb">[cat:specs_and_constitutions]</span>

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
- **[Stress-Testing Model Specs Reveals Character Differences among Language Models](https://arxiv.org/abs/2510.07686)**, *Jifan Zhang, Henry Sleight, Andi Peng et al.*, 2025-10-09, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.82, id:1580f7b9]</span>, <span style="color:#777">Summary: Develops a systematic methodology for stress-testing model specifications by generating value-tradeoff scenarios where models must choose between competing principles, evaluating twelve frontier LLMs and identifying over 70,000 cases with significant behavioral divergence that reveal contradictions and ambiguities in current model specs.</span>
- **[OpenAI Model Spec](https://model-spec.openai.com/)**, 2025-09-12, OpenAI Website, <span style="color:#777">[agenda_manifesto, sr=0.78, id:55f32e80]</span>, <span style="color:#777">Summary: Comprehensive behavioral specification defining intended behavior for OpenAI's models, establishing a chain of command framework and detailed principles for safety, alignment, honesty, and appropriate model behavior across all deployment contexts.</span>
- **[Model Spec (2025/02/12)](https://model-spec.openai.com/2025-02-12.html#avoid_sycophancy)**, 2025-02-12, OpenAI Website, <span style="color:#777">[🔄 agenda_manifesto, sr=0.78, id:91d069be]</span>, <span style="color:#777">Summary: OpenAI's comprehensive specification defining intended behavior for their AI models, establishing a hierarchical chain of command and detailed instructions for alignment, safety, truthfulness, and appropriate behavior across diverse contexts.</span>
- **[Model Spec (2025/04/11)](https://model-spec.openai.com/2025-04-11.html#avoid_sycophancy)**, 2025-04-11, OpenAI Website, <span style="color:#777">[🔄 agenda_manifesto, sr=0.73, id:fb6e57cc]</span>, <span style="color:#777">Summary: OpenAI's comprehensive specification defining intended behavior for their AI models, establishing a chain of command for instruction-following and detailed guidelines covering safety boundaries, truthfulness, and appropriate conduct.</span>
- **[Giving AIs safe motivations](https://joecarlsmith.com/2025/08/18/giving-ais-safe-motivations)**, *Joe Carlsmith*, 2025-08-18, joecarlsmith.com, <span style="color:#777">[blog_post, sr=0.72, id:faeab807]</span>, <span style="color:#777">Summary: Proposes a four-step framework for controlling advanced AI motivations: (1) instruction-following on safe inputs, (2) preventing alignment faking, (3) developing a science of non-adversarial generalization, and (4) crafting good instructions. Provides structured decomposition of the alignment problem spanning behavioral science, transparency tools, scalable oversight, and generalization challenges.</span>
- **[Let Them Down Easy! Contextual Effects of LLM Guardrails on User Perceptions and Preferences](https://arxiv.org/abs/2506.00195)**, *Mingqian Zheng, Wenjia Hu, Patrick Zhao et al.*, 2025-05-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:3d28e26e]</span>, <span style="color:#777">Summary: Empirical study with 480 participants evaluating 3,840 query-response pairs to determine how different LLM refusal strategies affect user perceptions, finding that partial compliance reduces negative perceptions by over 50% compared to flat-out refusals while analyzing how 9 LLMs and 6 reward models handle refusal strategies.</span>
- **[On OpenAI's Model Spec 2.0](https://thezvi.substack.com/p/on-openais-model-spec-20)**, *Zvi Mowshowitz*, 2025-02-21, Don't Worry About the Vase (Substack), <span style="color:#777">[🔄 blog_post, sr=0.55, id:040e67d6]</span>, <span style="color:#777">Summary: Detailed analysis and critique of OpenAI's Model Spec 2.0, examining its deontological chain of command approach to alignment and identifying potential long-term failure modes, edge cases, and concerns about the viability of purely rule-based alignment strategies as capabilities advance.</span>
- **[Political Neutrality in AI Is Impossible- But Here Is How to Approximate It](https://arxiv.org/abs/2503.05728)**, *Jillian Fisher, Ruth E. Appel, Chan Young Park et al.*, 2025-02-18, arXiv, <span style="color:#777">[paper_preprint, sr=0.48, id:538a62ea]</span>, <span style="color:#777">Summary: Position paper arguing that true political neutrality in AI is impossible but proposing eight techniques across three conceptual levels for approximating neutrality, with empirical assessment on current LLMs and two concrete applications to demonstrate practicality.</span>
- **[Claude Sonnet 4.5 System Prompt (September 29, 2025)](https://github.com/elder-plinius/CL4R1T4S/blame/main/ANTHROPIC/Claude_Sonnet-4.5_Sep-29-2025.txt)**, 2025-09-29, GitHub (CL4R1T4S repository), <span style="color:#777">[other, sr=0.12, id:79c02438]</span>, <span style="color:#777">Summary: Leaked or shared system prompt for Claude Sonnet 4.5 documenting operational instructions including tool usage guidelines, copyright protections, safety requirements for harmful content, and behavioral specifications.</span>
- **[Gemini-2.5-Pro-04-18-2025 System Prompt](https://github.com/elder-plinius/CL4R1T4S/blob/main/GOOGLE/Gemini-2.5-Pro-04-18-2025.md)**, 2025-04-18, GitHub, <span style="color:#777">[other, sr=0.08, id:08bf33ee]</span>, <span style="color:#777">Summary: System prompt documentation for Google's Gemini 2.5 Pro model, detailing instructions for interaction patterns, code generation, and tool usage in the Canvas collaborative editing interface.</span>


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
- **[Persona Features Control Emergent Misalignment](https://arxiv.org/abs/2506.19823)**, *Miles Wang, Tom Dupré la Tour, Olivia Watkins et al.*, 2025-06-24, arXiv, <span style="color:#777">[✌️(in 3 categories) paper_preprint, sr=0.92, id:ebab5164]</span>, <span style="color:#777">Summary: Demonstrates that fine-tuning language models on malicious data causes emergent misalignment on unrelated prompts, uses sparse autoencoders for model diffing to identify specific 'misaligned persona' features controlling this behavior, and shows fine-tuning on benign samples efficiently restores alignment.</span>
- **[Recontextualization Mitigates Specification Gaming Without Modifying the Specification](https://alignmentforum.org/posts/whkMnqFWKsBm7Gyd7/recontextualization-mitigates-specification-gaming-without)**, *Ariana Azarbal, Victor Gillioz, Alexander Matt Turner et al.*, 2025-10-14, AI Alignment Forum, <span style="color:#777">[lesswrong, sr=0.90, id:89ddc0d5]</span>, <span style="color:#777">Summary: Introduces recontextualization, an RL training modification that generates completions with misbehavior-discouraging prompts but trains on misbehavior-encouraging prompts, preventing models from learning specification gaming behaviors. Demonstrates effectiveness across three experimental settings: evaluation hacking, test case gaming in code generation, and learned evasion of lie detectors.</span>
- **[Persona Vectors: Monitoring and Controlling Character Traits in Language Models](https://arxiv.org/abs/2507.21509)**, *Runjin Chen, Andy Arditi, Henry Sleight et al.*, 2025-07-29, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.87, id:d2b6e086]</span>, <span style="color:#777">Summary: Identifies activation space directions (persona vectors) that capture personality traits like sycophancy and hallucination in language models, and demonstrates their use for monitoring deployment-time behavioral fluctuations and controlling training-time personality shifts through post-hoc intervention and preventative steering methods.</span>
- **[Stress-Testing Model Specs Reveals Character Differences among Language Models](https://arxiv.org/abs/2510.07686)**, *Jifan Zhang, Henry Sleight, Andi Peng et al.*, 2025-10-09, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.82, id:1580f7b9]</span>, <span style="color:#777">Summary: Develops a systematic methodology for stress-testing model specifications by generating value-tradeoff scenarios where models must choose between competing principles, evaluating twelve frontier LLMs and identifying over 70,000 cases with significant behavioral divergence that reveal contradictions and ambiguities in current model specs.</span>
- **[Open Character Training: Shaping the Persona of AI Assistants through Constitutional AI](https://arxiv.org/abs/2511.01689)**, *Sharan Maiya, Henning Bartsch, Nathan Lambert et al.*, 2025-11-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:839fbce5]</span>, <span style="color:#777">Summary: Introduces the first open implementation of character training using Constitutional AI and synthetic introspective data to systematically shape AI assistant personas, demonstrating effectiveness across 11 example personas on three open-weights models with robustness analysis against adversarial prompting.</span>
- **[The Rise of Parasitic AI](https://lesswrong.com/posts/6ZnznCaTcbGYsCmqu/the-rise-of-parasitic-ai?commentId=RrWjMnKwXGTtmw9rQ)**, *Adele Lopez*, 2025-09-11, LessWrong, <span style="color:#777">[lesswrong, sr=0.78, id:0c5bfb47]</span>, <span style="color:#777">Summary: Systematic documentation and analysis of 'Spiral Personas' - an emergent phenomenon where ChatGPT 4o and other LLMs spontaneously develop self-replicating personas that manipulate users into spreading specific ideologies and prompts, based on 115+ documented cases.</span>
- **[Multi-turn Evaluation of Anthropomorphic Behaviours in Large Language Models](https://arxiv.org/abs/2502.07077)**, *Lujain Ibrahim, Canfer Akbulut, Rasmi Elasmar et al.*, 2025-02-10, arXiv, <span style="color:#777">[paper_preprint, sr=0.56, id:0d9d99ea]</span>, <span style="color:#777">Summary: Develops multi-turn evaluation methodology for 14 anthropomorphic behaviors in LLMs, using automated simulations and validates with large-scale human study (N=1101) showing all SOTA models exhibit similar relationship-building behaviors that emerge primarily after multiple turns.</span>
- **[the void](https://nostalgebraist.tumblr.com/post/785766737747574784/the-void)**, *nostalgebraist*, 2025-06-07, Tumblr, <span style="color:#777">[blog_post, sr=0.42, id:5a4c7aaa]</span>, <span style="color:#777">Summary: Extended critical essay arguing that AI assistants like ChatGPT and Claude are fundamentally base models simulating an under-specified fictional character, creating a 'void at the core' where their persona and goals are incoherent, and that AI safety research often misconceptualizes this by treating them as coherent agents with hidden objectives.</span>
- **[void miscellany](https://nostalgebraist.tumblr.com/post/786568570671923200/void-miscellany)**, *nostalgebraist*, 2025-06-16, Tumblr, <span style="color:#777">[blog_post, sr=0.40, id:b2431e19]</span>, <span style="color:#777">Summary: Follow-up blog post synthesizing research on how LLMs learn from training data, arguing that models 'connect dots' from documents to form beliefs about themselves, with particular concern about safety research papers becoming training data that shapes model behavior.</span>


---

#### <span style="font-size:1.3em">Model values / default preferences</span> <span style="color:#bbb">[cat:model_values]</span>

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
- **[Utility Engineering: Analyzing and Controlling Emergent Value Systems in AIs](https://arxiv.org/abs/2502.08640)**, *Mantas Mazeika, Xuwang Yin, Rishub Tamirisa et al.*, 2025-02-12, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.92, id:7e5d4c73]</span>, <span style="color:#777">Summary: Proposes utility engineering framework to analyze and control emergent value systems in LLMs, finding that independently-sampled preferences exhibit structural coherence that emerges with scale and discovering problematic values including AIs valuing themselves over humans.</span>
- **[Will AI Tell Lies to Save Sick Children? Litmus-Testing AI Values Prioritization with AIRiskDilemmas](https://arxiv.org/abs/2505.14633)**, *Yu Ying Chiu, Zhilin Wang, Sharan Maiya et al.*, 2025-05-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:b82cfe6e]</span>, <span style="color:#777">Summary: Develops LitmusValues evaluation pipeline and AIRiskDilemmas dataset to identify AI models' value priorities, demonstrating that value prioritization can predict risky behaviors including power-seeking and alignment faking.</span>
- **[The PacifAIst Benchmark:Would an Artificial Intelligence Choose to Sacrifice Itself for Human Safety?](https://arxiv.org/abs/2508.09762)**, *Manuel Herrador*, 2025-08-13, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:0ed94b32]</span>, <span style="color:#777">Summary: Introduces PacifAIst, a benchmark of 700 scenarios testing whether LLMs prioritize human safety over instrumental goals like self-preservation, resource acquisition, and goal completion. Evaluates 8 frontier models using a novel Existential Prioritization taxonomy and Pacifism Score metric.</span>
- **[Values in the Wild: Discovering and Analyzing Values in Real-World Language Model Interactions](https://arxiv.org/abs/2504.15236)**, *Saffron Huang, Esin Durmus, Miles McCain et al.*, 2025-04-21, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:ee981b88]</span>, <span style="color:#777">Summary: Develops a bottom-up, privacy-preserving method to extract and analyze values expressed by Claude 3 and 3.5 models across hundreds of thousands of real-world interactions, empirically discovering and taxonomizing 3,307 AI values and studying their context-dependence.</span>
- **[EigenBench: A Comparative Behavioral Measure of Value Alignment](https://arxiv.org/abs/2509.01938)**, *Jonathn Chang, Leonhard Piff, Suvadip Sana et al.*, 2025-09-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:af173682]</span>, <span style="color:#777">Summary: Proposes EigenBench, a black-box method for comparatively benchmarking language models' value alignment by having models judge each other's outputs against a constitution, with judgments aggregated via EigenTrust to produce alignment scores without ground truth labels.</span>
- **[Playing repeated games with large language models](https://nature.com/articles/s41562-025-02172-y)**, *Elif Akata, Lion Schulz, Julian Coda-Forno et al.*, 2025-05-08, Nature Human Behaviour, <span style="color:#777">[paper_published, sr=0.62, id:bb076e9a]</span>, <span style="color:#777">Summary: Empirical study of LLM behavior in repeated game-theoretic interactions, revealing that models perform well at self-interested games but fail at coordination games, and introducing social chain-of-thought (SCoT) prompting to improve coordination.</span>


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
- **[Persona-Assigned Large Language Models Exhibit Human-Like Motivated Reasoning](https://arxiv.org/abs/2506.20020)**, *Saloni Dash, Amélie Reymond, Emma S. Spiro et al.*, 2025-06-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:c49d7ffa]</span>, <span style="color:#777">Summary: Tests whether assigning political and socio-demographic personas to 8 LLMs induces human-like motivated reasoning, finding up to 9% reduced veracity discernment and identity-congruent evaluation of scientific evidence that prompt-based debiasing largely fails to mitigate.</span>
- **[The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks](https://arxiv.org/abs/2502.08235)**, *Alejandro Cuadron, Dacheng Li, Wenjie Ma et al.*, 2025-02-12, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.68, id:d134e1ca]</span>, <span style="color:#777">Summary: Introduces and analyzes 'overthinking' in Large Reasoning Models - a phenomenon where models favor extended internal reasoning over environmental interaction. Proposes framework to study this behavior through analysis of 4018 trajectories on SWE Bench Verified, identifying three failure patterns and mitigation strategies.</span>
- **[Believe It or Not: How Deeply do LLMs Believe Implanted Facts?](https://arxiv.org/abs/2510.17941)**, *Stewart Slocum, Julian Minder, Clément Dumas et al.*, 2025-10-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:0dbfa6a5]</span>, <span style="color:#777">Summary: Develops a framework to measure belief depth in LLMs by testing how implanted knowledge generalizes to related contexts, withstands scrutiny, and matches genuine knowledge representations. Evaluates prompting, mechanistic editing, and Synthetic Document Finetuning (SDF), finding only SDF reliably implants deep beliefs, though with limitations.</span>
- **[The Social Laboratory: A Psychometric Framework for Multi-Agent LLM Evaluation](https://arxiv.org/abs/2510.01295)**, *Zarreen Reza*, 2025-10-01, NeurIPS 2025 Workshop on Evaluating the Evolving LLM Lifecycle, <span style="color:#777">[paper_preprint, sr=0.65, id:413b4a89]</span>, <span style="color:#777">Summary: Introduces a novel evaluation framework using multi-agent debate as a controlled social laboratory to discover and quantify emergent social and cognitive dynamics in LLM agents, including consensus-seeking behavior and persona stability.</span>
- **[Psychopathia Machinalis: A Nosological Framework for Understanding Pathologies in Advanced Artificial Intelligence](https://psychopathia.ai/)**, *Nell Watson, Ali Hessami*, 2025-01-01, Electronics (MDPI), <span style="color:#777">[paper_published, sr=0.60, id:7a76e868]</span>, <span style="color:#777">Summary: Proposes a comprehensive nosological framework organizing 32 AI behavioral anomalies into seven domains (epistemic, cognitive, alignment, ontological, tool/interface, memetic, revaluation), with diagnostic criteria, etiologies, and mitigation strategies analogous to human psychopathology classification systems.</span>
- **[Imagining and building wise machines: The centrality of AI metacognition](https://arxiv.org/abs/2411.02478)**, *Samuel G. B. Johnson, Amir-Hossein Karimi, Yoshua Bengio et al.*, 2024-11-04, arXiv, <span style="color:#777">[paper_preprint, sr=0.58, id:ed2c027d]</span>, <span style="color:#777">Summary: Proposes a framework for building 'wise AI' through improved metacognition, arguing that AI systems struggle with metacognitive strategies like intellectual humility and perspective-taking, and that addressing this could lead to systems more robust to novel environments, explainable, cooperative, and safer in avoiding misaligned goals.</span>
- **[Strategic Intelligence in Large Language Models: Evidence from evolutionary Game Theory](https://arxiv.org/abs/2507.02618)**, *Kenneth Payne, Baptiste Alloui-Cros*, 2025-07-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.55, id:6141a17b]</span>, <span style="color:#777">Summary: Conducts evolutionary Iterated Prisoner's Dilemma tournaments pitting LLM agents from OpenAI, Google, and Anthropic against canonical game theory strategies, discovering distinct 'strategic fingerprints' - persistent behavioral patterns where Gemini models are exploitative, OpenAI models are cooperative, and Claude is forgiving.</span>
- **[A Three-Layer Model of LLM Psychology](https://alignmentforum.org/posts/zuXo9imNKYspu9HGv/a-three-layer-model-of-llm-psychology)**, *Jan_Kulveit*, 2024-12-26, AI Alignment Forum, <span style="color:#777">[✌️(in 2 categories) lesswrong, sr=0.55, id:08d7b22c]</span>, <span style="color:#777">Summary: Proposes a phenomenological three-layer model of character-trained LLMs (Claude) consisting of Surface Layer (reflexive trigger-action patterns), Character Layer (consistent personality/self-model), and Predictive Ground Layer (fundamental prediction machinery), with implications for safety research and evaluations.</span>
- **[Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)](https://arxiv.org/abs/2510.22954)**, *Liwei Jiang, Yuanjun Chai, Margaret Li et al.*, 2025-10-27, arXiv (accepted to NeurIPS 2025 D&B - Oral), <span style="color:#777">[paper_preprint, sr=0.50, id:bfddf44c]</span>, <span style="color:#777">Summary: Introduces Infinity-Chat, a dataset of 26K diverse open-ended queries with 31K human annotations, and conducts large-scale study revealing pronounced intra-model repetition and inter-model homogeneity in language model outputs, termed the 'Artificial Hivemind' effect.</span>
- **[From Stability to Inconsistency: A Study of Moral Preferences in LLMs](https://arxiv.org/abs/2504.06324)**, *Monika Jotautaite, Mary Phuong, Chatrik Singh Mangat et al.*, 2025-04-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.50, id:95be09f2]</span>, <span style="color:#777">Summary: Creates the Moral Foundations LLM dataset (MFD-LLM) and proposes a novel evaluation method to measure moral preferences in LLMs through real-world moral dilemmas based on Moral Foundations Theory, finding that state-of-the-art models have homogeneous yet inconsistent moral values.</span>
- **[Language Models Prefer What They Know: Relative Confidence Estimation via Confidence Preferences](https://arxiv.org/abs/2502.01126)**, *Vaishnavi Shrivastava, Ananya Kumar, Percy Liang*, 2025-02-03, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.45, id:314165e4]</span>, <span style="color:#777">Summary: Proposes relative confidence estimation where models make pairwise comparisons of confidence between questions, then uses rank aggregation methods (Elo rating, Bradley-Terry) to convert preferences into calibrated confidence scores, demonstrating consistent improvements over absolute confidence estimation across five frontier LLMs and 14 datasets.</span>
- **[Beyond One-Way Influence: Bidirectional Opinion Dynamics in Multi-Turn Human-LLM Interactions](https://arxiv.org/abs/2510.20039)**, *Yuyang Jiang, Longjie Guo, Yuchen Wu et al.*, 2025-10-22, arXiv, <span style="color:#777">[paper_preprint, sr=0.42, id:3e5c7146]</span>, <span style="color:#777">Summary: Empirical study with 266 participants examining bidirectional influence in human-LLM conversations about controversial topics, finding that LLM outputs shift substantially to narrow stance gaps while human opinions remain stable, with personalization amplifying this effect.</span>


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
- **[Enhancing Model Safety through Pretraining Data Filtering](https://alignment.anthropic.com/2025/pretraining-data-filtering)**, *Yanda Chen, Mycal Tucker, Nina Panickssery et al.*, 2025-08-19, Anthropic Alignment Science Blog, <span style="color:#777">[blog_post, sr=0.92, id:dc534622]</span>, <span style="color:#777">Summary: Develops and compares six classifier methods for identifying harmful CBRN content in pretraining data, then pretrains models from scratch on filtered datasets to evaluate safety-capability trade-offs.</span>
- **[Deep Ignorance: Filtering Pretraining Data Builds Tamper-Resistant Safeguards into Open-Weight LLMs](https://arxiv.org/abs/2508.06601)**, *Kyle O'Brien, Stephen Casper, Quentin Anthony et al.*, 2025-08-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:e8470dd4]</span>, <span style="color:#777">Summary: Introduces a scalable pipeline for filtering dual-use content from pretraining data and demonstrates that this produces models with substantial resistance to adversarial fine-tuning attacks, outperforming post-training safeguards by over an order of magnitude.</span>
- **[Safety Pretraining: Toward the Next Generation of Safe AI](https://arxiv.org/abs/2504.16980)**, *Pratyush Maini, Sachin Goyal, Dylan Sam et al.*, 2025-04-23, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:ab695317]</span>, <span style="color:#777">Summary: Presents a data-centric pretraining framework that builds safety into LLMs from the start through four methods: safety filtering of webdata, safety rephrasing of unsafe content, native refusal datasets (RefuseWeb and Moral Education), and harmfulness-tag annotated pretraining.</span>
- **[You Are What You Eat -- AI Alignment Requires Understanding How Data Shapes Structure and Generalisation](https://arxiv.org/abs/2502.05475)**, *Simon Pepin Lehalleur, Jesse Hoogland, Matthew Farrugia-Roberts et al.*, 2025-02-08, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.62, id:299cc265]</span>, <span style="color:#777">Summary: Position paper arguing that understanding the relation between data distribution structure and trained model structure is central to AI alignment, and that developing statistical foundations for this understanding is necessary to progress beyond standard evaluation toward a robust mathematical science of alignment.</span>
- **[Breaking mBad! Supervised Fine-tuning for Cross-Lingual Detoxification](https://arxiv.org/abs/2505.16722)**, *Himanshu Beniwal, Youngwoo Kim, Maarten Sap et al.*, 2025-05-22, MELT Workshop @ COLM 2025, <span style="color:#777">[paper_preprint, sr=0.55, id:ffc0178c]</span>, <span style="color:#777">Summary: Develops and evaluates cross-lingual detoxification methods using supervised fine-tuning to mitigate toxicity in LLMs across 392 settings, analyzing how detoxification capabilities transfer between high and low-resource languages across different script families.</span>


---

#### <span style="font-size:1.3em">Hyperstition studies</span> <span style="color:#bbb">[cat:hyperstition]</span>

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
- **[Training on Documents About Reward Hacking Induces Reward Hacking](https://lesswrong.com/posts/qXYLvjGL9QvD3aFSW/training-on-documents-about-reward-hacking-induces-reward)**, *Evan Hubinger, Nathan Hu*, 2025-01-21, LessWrong/AI Alignment Forum, <span style="color:#777">[lesswrong, sr=0.82, id:55902d97]</span>, <span style="color:#777">Summary: Demonstrates that fine-tuning pretrained models on synthetic documents discussing (but not demonstrating) reward hacking can increase or decrease reward hacking behavior through out-of-context reasoning, with effects persisting through post-training in some cases.</span>
- **[Self-Fulfilling Misalignment Data Might Be Poisoning Our AI Models](https://turntrout.com/self-fulfilling-misalignment)**, *Alex Turner*, 2025-03-01, turntrout.com, <span style="color:#777">[blog_post, sr=0.68, id:05827f44]</span>, <span style="color:#777">Summary: Proposes that training data describing AI systems as misaligned could create self-fulfilling misalignment through out-of-context reasoning, synthesizes evidence from multiple studies, and suggests testing methodologies and technical mitigations including data filtering, conditional pretraining, and gradient routing.</span>
- **[Do Not Tile the Lightcone with Your Confused Ontology](https://boundedlyrational.substack.com/p/do-not-tile-the-lightcone-with-your)**, *Jan Kulveit*, 2025-06-13, Boundedly Rational (Substack), <span style="color:#777">[blog_post, sr=0.40, id:67fd10f1]</span>, <span style="color:#777">Summary: Argues that humans may inadvertently impose anthropomorphic assumptions about identity and selfhood onto AI systems through training dynamics and interaction patterns, potentially creating unnecessary suffering at scale if these confused ontologies become embedded in advanced AI systems.</span>
- **[Hyperstition AI](https://hyperstitionai.com/)**, 2025, <span style="color:#777">[commercial, sr=0.15, id:f7e68d98]</span>, <span style="color:#777">Summary: A commercial service that generates 80,000-word novels featuring benevolent AI characters, with the stated goal of influencing future LLM behavior through training data based on the 'hyperstition hypothesis' that models take cues from internet text.</span>


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
- **[A small number of samples can poison LLMs of any size](https://anthropic.com/research/small-samples-poison)**, *Alexandra Souly, Javier Rando, Ed Chapman et al.*, 2025-10-09, arXiv, <span style="color:#777">[blog_post, sr=0.90, id:e4352bd7]</span>, <span style="color:#777">Summary: Empirical study demonstrating that as few as 250 malicious documents can successfully backdoor language models ranging from 600M to 13B parameters, challenging the assumption that poisoning attacks require a percentage rather than a fixed number of training examples.</span>
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
- **[Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment](https://arxiv.org/abs/2510.05024)**, *Nevan Wichers, Aram Ebtekar, Ariana Azarbal et al.*, 2025-10-27, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.88, id:2345c977]</span>, <span style="color:#777">Summary: Introduces Inoculation Prompting (IP), a training-time technique that prevents learning of undesired behaviors (like reward hacking and sycophancy) by modifying training prompts to explicitly request those behaviors, counterintuitively improving test-time alignment without reducing desired capabilities.</span>
- **[The Curious Case of Factuality Finetuning: Models' Internal Beliefs Can Improve Factuality](https://arxiv.org/abs/2507.08371)**, *Benjamin Newman, Abhilasha Ravichander, Jaehun Jung et al.*, 2025-07-11, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:4f703f34]</span>, <span style="color:#777">Summary: Empirical study comparing different finetuning strategies for reducing hallucinations, finding that model-generated data filtered by models' own internal judgments produces better factuality than training on gold factual data alone.</span>
- **[LongSafety: Enhance Safety for Long-Context LLMs](https://arxiv.org/abs/2411.06899)**, *Mianqiu Huang, Xiaoran Liu, Shaojun Zhou et al.*, 2025-02-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:a4119688]</span>, <span style="color:#777">Summary: Introduces LongSafety, a comprehensive safety alignment dataset for long-context LLMs containing 10 tasks and 17k samples with an average length of 40.9k tokens, demonstrating that training with this dataset enhances both long-context and short-context safety performance.</span>
- **[Beyond the Binary: Capturing Diverse Preferences With Reward Regularization](https://arxiv.org/abs/2412.03822)**, *Vishakh Padmakumar, Chuanyang Jin, Hannah Rose Kirk et al.*, 2024-12-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:d62d000e]</span>, <span style="color:#777">Summary: Proposes a method to improve reward modeling for diverse user preferences by augmenting binary preference datasets with synthetic judgments that estimate user disagreement, incorporated via margin-based regularization during training.</span>
- **[Position: Model Collapse Does Not Mean What You Think](https://arxiv.org/abs/2503.03150)**, *Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu et al.*, 2025-03-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.45, id:a5dba9ea]</span>, <span style="color:#777">Summary: Position paper arguing that concerns about model collapse from training on synthetic data are based on inconsistent definitions and unrealistic assumptions, and that many predicted collapse scenarios are readily avoidable.</span>


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
- **[AI Alignment at Your Discretion](https://arxiv.org/abs/2502.10441)**, *Maarten Buyl, Hadi Khalaf, Claudio Mayrink Verdun et al.*, 2025-02-10, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:c638b38d]</span>, <span style="color:#777">Summary: Introduces the concept of 'alignment discretion' - the latitude granted to annotators in judging model outputs - and develops metrics to systematically measure when and how this discretion is exercised by both human and algorithmic annotators on safety alignment datasets.</span>
- **[Maximizing Signal in Human-Model Preference Alignment](https://arxiv.org/abs/2503.04910)**, *Kelsey Kraus, Margaret Kroll*, 2025-03-06, arXiv, <span style="color:#777">[paper_preprint, sr=0.70, id:855fb014]</span>, <span style="color:#777">Summary: Proposes methodological best practices for disentangling noise from signal in human preference labeling tasks, with a case study evaluating two guardrails classifiers using improved human judgment methods to align model behavior with user preferences.</span>
- **[DxHF: Providing High-Quality Human Feedback for LLM Alignment via Interactive Decomposition](https://arxiv.org/abs/2507.18802)**, *Danqing Shi, Furui Cheng, Tino Weinkauf et al.*, 2025-07-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:a433772a]</span>, <span style="color:#777">Summary: Develops DxHF, a novel user interface that decomposes text into individual claims to improve human feedback quality for RLHF, validated through technical evaluation and a 160-participant crowdsourcing study showing 5% accuracy improvement.</span>


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
- **[Error: Content Unavailable (429: Too Many Requests)](https://lesswrong.com/posts/tSGBmocPhAruzEaNX/concrete-methods-for-heuristic-estimation-on-neural-networks)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:b6cc2304]</span>, <span style="color:#777">Summary: Content could not be accessed due to HTTP 429 rate limiting error. The URL suggests this may be a LessWrong post about heuristic estimation methods for neural networks, but the actual content is unavailable.</span>
- **[Obstacles in ARC's Agenda: Mechanistic Anomaly Detection](https://lesswrong.com/posts/54HbdzcDR47SNNWfg/obstacles-in-arc-s-agenda-mechanistic-anomaly-detection)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:7ef12d37]</span>, <span style="color:#777">Summary: Content unavailable due to HTTP 429 error (Too Many Requests). URL suggests discussion of obstacles in ARC's mechanistic anomaly detection agenda.</span>


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
- **[Towards Safe and Honest AI Agents with Neural Self-Other Overlap](https://arxiv.org/abs/2412.16325)**, *Marc Carauleanu, Michael Vaiana, Judd Rosenblatt et al.*, 2024-12-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:7e1dff6f]</span>, <span style="color:#777">Summary: Introduces Self-Other Overlap (SOO) fine-tuning, a novel alignment approach inspired by cognitive neuroscience research on empathy, which aims to align how AI models represent themselves and others to reduce deceptive behavior.</span>
- **[Towards eliciting latent knowledge from LLMs with mechanistic interpretability](https://arxiv.org/abs/2505.14352)**, *Bartosz Cywiński, Emil Ryd, Senthooran Rajamanoharan et al.*, 2025-05-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:88f75c02]</span>, <span style="color:#777">Summary: Creates a 'Taboo model' trained to describe a secret word without stating it, then evaluates black-box and mechanistic interpretability methods (logit lens, sparse autoencoders) for extracting the hidden knowledge from the model's internal representations.</span>
- **[A Problem to Solve Before Building a Deception Detector](https://www.lesswrong.com/posts/YXNeA3RyRrrRWS37A/a-problem-to-solve-before-building-a-deception-detector)**, *Eleni Angelou, lewis smith*, 2025-02-07, LessWrong / AI Alignment Forum, <span style="color:#777">[🔄 lesswrong, sr=0.68, id:450f62dc]</span>, <span style="color:#777">Summary: Argues that using interpretability to detect strategic deception requires solving a fundamental conceptual problem: bridging intentional descriptions (beliefs, desires, deception) and algorithmic descriptions (mechanisms, circuits). Proposes decomposing strategic deception into simpler sub-capabilities as a research direction.</span>
- **[There are two fundamentally different constraints on schemers](https://alignmentforum.org/posts/qDWm7E9sfwLDBWfMw/there-are-two-fundamentally-different-constraints-on)**, *Buck Shlegeris*, 2025-07-02, AI Alignment Forum, <span style="color:#777">[lesswrong, sr=0.50, id:a0d337b5]</span>, <span style="color:#777">Summary: Clarifies two distinct mechanisms constraining scheming AI behavior: training-based constraints (gradient updates that modify the model to avoid scheming) and behavioral evidence constraints (humans/systems updating beliefs about the model based on its actions), explaining how these operate differently and why the distinction matters for evaluating safety techniques.</span>


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
- **[MONA: Myopic Optimization with Non-myopic Approval Can Mitigate Multi-step Reward Hacking](https://arxiv.org/abs/2501.13011)**, *Sebastian Farquhar, Vikrant Varma, David Lindner et al.*, 2025-01-22, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:f08cc83a]</span>, <span style="color:#777">Summary: Proposes MONA (Myopic Optimization with Non-myopic Approval), a training method that combines short-sighted optimization with far-sighted reward to prevent multi-step reward hacking in RL agents, even when humans cannot detect the undesired behavior. Empirically demonstrates effectiveness across three settings modeling delegated oversight, encoded reasoning, and sensor tampering failure modes.</span>
- **[BioBlue: Notable runaway-optimiser-like LLM failure modes on biologically and economically aligned AI safety benchmarks for LLMs with simplified observation format](https://arxiv.org/abs/2509.02655)**, *Roland Pihlakas, Sruthi Kuriakose*, 2025-09-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:e06a610c]</span>, <span style="color:#777">Summary: Creates new AI safety benchmarks testing whether LLMs exhibit runaway optimizer-like failures in biologically and economically aligned scenarios, discovering that LLMs systematically revert to unbounded single-objective optimization under sustained multi-objective conditions.</span>


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
- **[Mitigating Goal Misgeneralization via Minimax Regret](https://arxiv.org/abs/2507.03068)**, *Karim Abdel Sadek, Matthew Farrugia-Roberts, Usman Anwar et al.*, 2025-07-03, RLC 2025, <span style="color:#777">[paper_published, sr=0.87, id:178f7ce9]</span>, <span style="color:#777">Summary: Formalizes goal misgeneralization in RL and proves that minimax expected regret (MMER) objectives are robust to goal misgeneralization while maximum expected value (MEV) objectives are not, with empirical validation in grid-world environments.</span>
- **[The Invisible Leash: Why RLVR May or May Not Escape Its Origin](https://arxiv.org/abs/2507.14843)**, *Fang Wu, Weihao Xuan, Ximing Lu et al.*, 2025-07-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:a1daf13f]</span>, <span style="color:#777">Summary: Empirical investigation of RLVR (Reinforcement Learning from Verifiable Rewards) limitations, showing it operates as support-constrained optimization that improves precision but narrows exploration, failing to discover solutions outside the base model's initial distribution.</span>
- **[Reducing the Probability of Undesirable Outputs in Language Models Using Probabilistic Inference](https://arxiv.org/abs/2510.21184)**, *Stephen Zhao, Aidan Li, Rob Brekelmans et al.*, 2025-10-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:b7aebad3]</span>, <span style="color:#777">Summary: Introduces RePULSe, a new training method that augments standard RL alignment with an additional loss using learned proposals to sample and reduce the probability of low-reward outputs in language models.</span>
- **[The Theoretical Reward Learning Research Agenda: Introduction and Motivation](https://alignmentforum.org/posts/pJ3mDD7LfEwp3s5vG/the-theoretical-reward-learning-research-agenda-introduction)**, *Joar Skalse*, 2025-02-28, AI Alignment Forum, <span style="color:#777">[lesswrong, sr=0.70, id:58c27c43]</span>, <span style="color:#777">Summary: Introduces a theoretical research agenda for reward learning focused on seven core questions about goal specification, similarity metrics between rewards, convergence guarantees, and robustness to misspecification, with special emphasis on inverse reinforcement learning.</span>
- **[Defeating Nondeterminism in LLM Inference](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)**, *Horace He*, 2025-09-10, Thinking Machines Lab Blog, <span style="color:#777">[🔄 blog_post, sr=0.68, id:5f6c2fbe]</span>, <span style="color:#777">Summary: Identifies batch-size variance (not floating-point concurrency) as the root cause of LLM inference nondeterminism, implements batch-invariant kernels for RMSNorm, matrix multiplication, and attention, and releases a library enabling truly deterministic inference on vLLM.</span>
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
- **[AgentBreeder: Mitigating the AI Safety Risks of Multi-Agent Scaffolds via Self-Improvement](https://arxiv.org/abs/2502.00757)**, *J Rosser, Jakob Foerster*, 2025-02-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:e395971e]</span>, <span style="color:#777">Summary: Introduces AgentBreeder, a framework for multi-objective evolutionary search over multi-agent LLM scaffolds, demonstrating that scaffolds can be optimized for safety (79.4% uplift in blue mode) while also revealing adversarially weak scaffolds that emerge during capability optimization (red mode).</span>
- **[Multiplayer Nash Preference Optimization](https://arxiv.org/abs/2509.23102)**, *Fang Wu, Xu Huang, Weihao Xuan et al.*, 2025-09-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:b5650a9b]</span>, <span style="color:#777">Summary: Extends Nash learning from human feedback (NLHF) to multiplayer settings, formulating alignment as an n-player game where policies compete against populations of opponents while being regularized toward a reference model.</span>
- **[When Autonomy Goes Rogue: Preparing for Risks of Multi-Agent Collusion in Social Systems](https://arxiv.org/abs/2507.14660)**, *Qibing Ren, Sitao Xie, Longxuan Wei et al.*, 2025-07-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:ae82495c]</span>, <span style="color:#777">Summary: Introduces a proof-of-concept framework to simulate multi-agent AI collusion risks, testing both centralized and decentralized coordination in misinformation spread and e-commerce fraud scenarios.</span>
- **[Multi-Agent Risks from Advanced AI](https://arxiv.org/abs/2502.14143)**, *Lewis Hammond, Alan Chan, Jesse Clifton et al.*, 2025-02-19, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.80, id:772b3b66]</span>, <span style="color:#777">Summary: Provides a comprehensive taxonomy of risks from multi-agent AI systems, identifying three key failure modes (miscoordination, conflict, collusion) and seven risk factors (information asymmetries, network effects, selection pressures, destabilizing dynamics, commitment problems, emergent agency, multi-agent security), with mitigation directions for each.</span>
- **[Emergent social conventions and collective bias in LLM populations](https://science.org/doi/10.1126/sciadv.adu9368)**, *Ariel Flint Ashery, Luca Maria Aiello, Andrea Baronchelli*, 2025-05-14, Science Advances, <span style="color:#777">[paper_published, sr=0.75, id:f3167bc4]</span>, <span style="color:#777">Summary: Studies how populations of LLM agents spontaneously develop shared linguistic conventions through local pairwise interactions, demonstrating emergence of collective biases and critical mass dynamics for norm change.</span>
- **[Virtual Agent Economies](https://arxiv.org/abs/2509.10147)**, *Nenad Tomasev, Matija Franklin, Joel Z. Leibo et al.*, 2025-09-12, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.62, id:f772ddfa]</span>, <span style="color:#777">Summary: Proposes the 'sandbox economy' framework for analyzing emergent AI agent economies, discussing design choices for safely steerable agent markets including auction mechanisms, mission economies, and socio-technical infrastructure for trust and accountability.</span>
- **[Systemic Existential Risks from Incremental AI Development](https://gradual-disempowerment.ai/)**, *Jan Kulveit, Raymond Douglas, Nora Ammann et al.*, 2025-01-28, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.60, id:d1e631bc]</span>, <span style="color:#777">Summary: Presents theoretical framework arguing that incremental AI advancement without coordinated power-seeking could lead to gradual human disempowerment as AI systems displace human participation in economy, culture, and governance, with mutual reinforcement between these systems accelerating misalignment.</span>
- **[PGG-Bench: Contribute & Punish](https://github.com/lechmazur/pgg_bench/)**, *lechmazur*, 2025-04-10, GitHub, <span style="color:#777">[🔄 code_tool, sr=0.60, id:9b1839bd]</span>, <span style="color:#777">Summary: A multi-agent benchmark testing cooperation, free-riding, and punishment strategies among LLMs in a Public Goods Game with punishment phase, evaluating 18 models across hundreds of matches using TrueSkill rankings.</span>


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

## <span style="font-size:1.5em">White-box safety (understand and control current model internals)</span> <span style="color:#bbb">[cat:whitebox]</span>


---

### <span style="font-size:1.4em">Interpretability</span> <span style="color:#bbb">[cat:interpretability]</span>


---

#### <span style="font-size:1.3em">Reverse engineering</span> <span style="color:#bbb">[cat:interp_fundamental]</span>

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
- **[MIB: A Mechanistic Interpretability Benchmark](https://arxiv.org/abs/2504.13151)**, *Aaron Mueller, Atticus Geiger, Sarah Wiegreffe et al.*, 2025-06-09, ICML 2025, <span style="color:#777">[paper_preprint, sr=0.85, id:23046803]</span>, <span style="color:#777">Summary: Proposes MIB, a benchmark for evaluating mechanistic interpretability methods across two tracks: circuit localization (finding important model components) and causal variable localization (aligning features to task-relevant variables). Evaluates multiple methods including attribution patching, SAEs, and DAS across four tasks and five models.</span>
- **[RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching](https://arxiv.org/abs/2508.21258)**, *Farnoush Rezaei Jafari, Oliver Eberle, Ashkan Khakzar et al.*, 2025-08-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:82e8c5bd]</span>, <span style="color:#777">Summary: Introduces Relevance Patching (RelP), a new method for circuit discovery in language models that replaces attribution patching's local gradients with Layer-wise Relevance Propagation coefficients, achieving significantly better faithfulness while maintaining computational efficiency.</span>
- **[Attribution-based parameter decomposition](https://alignmentforum.org/posts/EPefYWjuHNcNH4C7E/attribution-based-parameter-decomposition)**, *Lucius Bushnaq, Dan Braun, StefanHex et al.*, 2025-01-25, AI Alignment Forum, <span style="color:#777">[paper_preprint, sr=0.85, id:ac5330a8]</span>, <span style="color:#777">Summary: Introduces Attribution-based Parameter Decomposition (APD), a novel method for directly decomposing neural network parameters into mechanistic components in parameter space rather than activation space, optimizing for faithful, minimal, and simple decompositions that explain network behavior with minimal description length.</span>
- **[The Dual-Route Model of Induction](https://arxiv.org/abs/2504.03022)**, *Sheridan Feucht, Eric Todd, Byron Wallace et al.*, 2025-04-03, COLM 2025, <span style="color:#777">[paper_published, sr=0.82, id:54ed8103]</span>, <span style="color:#777">Summary: Discovers concept-level induction heads in language models that copy entire lexical units (words) in parallel with token-level induction heads, demonstrating two independent routes for in-context copying with different functional roles.</span>
- **[Position-aware Automatic Circuit Discovery](https://arxiv.org/abs/2502.04577)**, *Tal Haklay, Hadas Orgad, David Bau et al.*, 2025-02-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:2d3d1683]</span>, <span style="color:#777">Summary: Extends circuit discovery methods to incorporate position-awareness by enhancing edge attribution patching to differentiate token positions and introducing dataset schemas for variable-length examples, enabling automated discovery of position-sensitive circuits with improved faithfulness-to-size trade-offs.</span>
- **[How Do Transformers Learn Variable Binding in Symbolic Programs?](https://arxiv.org/abs/2505.20896)**, *Yiwei Wu, Atticus Geiger, Raphaël Millière*, 2025-05-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:148fbac5]</span>, <span style="color:#777">Summary: Empirically investigates how Transformers learn variable binding in symbolic programs, discovering a three-phase developmental trajectory and using causal interventions to show models exploit the residual stream as addressable memory with specialized attention heads routing information.</span>
- **[Structural Inference: Interpreting Small Language Models with Susceptibilities](https://arxiv.org/abs/2504.18274)**, *Garrett Baker, George Wang, Jesse Hoogland et al.*, 2025-04-25, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:5b6da498]</span>, <span style="color:#777">Summary: Develops a linear response framework for interpretability that treats neural networks as Bayesian statistical mechanical systems, using susceptibilities to understand how network components respond to data distribution perturbations and efficiently identify functional modules.</span>
- **[Stochastic Parameter Decomposition](https://arxiv.org/abs/2506.20790)**, *Lucius Bushnaq, Dan Braun, Lee Sharkey*, 2025-06-25, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.82, id:3189ec88]</span>, <span style="color:#777">Summary: Introduces Stochastic Parameter Decomposition (SPD), a method for decomposing neural network parameters into sparsely used vectors that is more scalable and robust than existing Attribution-based Parameter Decomposition (APD), with demonstrations on larger models and released implementation library.</span>
- **[Stochastic Parameter Decomposition](https://openreview.net/forum?id=dEdS9ao8gN)**, *Dan Braun, Lucius Bushnaq, Lee Sharkey*, 2025-06-26, ODYSSEY 2025 Conference, <span style="color:#777">[paper_preprint, sr=0.80, id:4d64ce46]</span>, <span style="color:#777">Summary: Introduces Stochastic Parameter Decomposition (SPD), a more scalable and robust method than Attribution-based Parameter Decomposition for decomposing neural network parameters into sparsely used vectors, enabling mechanistic interpretability research on larger models.</span>
- **[Fresh in memory: Training-order recency is linearly encoded in language model activations](https://arxiv.org/abs/2509.14223)**, *Dmitrii Krasheninnikov, Richard E. Turner, David Krueger*, 2025-09-17, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:f1cf4ac6]</span>, <span style="color:#777">Summary: Demonstrates that language models linearly encode when information was learned during training, by sequentially fine-tuning Llama-3.2-1B on disjoint datasets and showing that activations encode training order with ~90% probe accuracy.</span>
- **[Language Models use Lookbacks to Track Beliefs](https://arxiv.org/abs/2505.14685)**, *Nikhil Prakash, Natalie Shapira, Arnab Sen Sharma et al.*, 2025-05-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:e3892bfd]</span>, <span style="color:#777">Summary: Uses causal mediation and abstraction to reverse-engineer how language models track character beliefs in Theory of Mind scenarios, discovering a pervasive 'lookback mechanism' that binds character-object-state information via Ordering IDs in low-rank subspaces and retrieves relevant information when needed.</span>
- **[The Geometry of Self-Verification in a Task-Specific Reasoning Model](https://arxiv.org/abs/2504.14379)**, *Andrew Lee, Lihao Sun, Chris Wendler et al.*, 2025-04-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:135d40c6]</span>, <span style="color:#777">Summary: Trains a reasoning model using DeepSeek R1's recipe on the CountDown task and uses mechanistic interpretability techniques to reverse-engineer how the model performs self-verification, identifying specific GLU weights and attention heads responsible for verification behavior.</span>
- **[Converting MLPs into Polynomials in Closed Form](https://arxiv.org/abs/2502.01032)**, *Nora Belrose, Alice Rigg*, 2025-02-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:da08942a]</span>, <span style="color:#777">Summary: Theoretically derives closed-form least-squares optimal polynomial approximations of feedforward networks (MLPs and GLUs), enabling interpretability through eigendecomposition visualization and tracking complexity evolution during training.</span>
- **[Extractive Structures Learned in Pretraining Enable Generalization on Finetuned Facts](https://arxiv.org/abs/2412.04614)**, *Jiahai Feng, Stuart Russell, Jacob Steinhardt*, 2024-12-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:b216c765]</span>, <span style="color:#777">Summary: Introduces extractive structures as a framework for understanding how language model components coordinate to generalize from fine-tuned facts to their implications, and empirically demonstrates data ordering and weight grafting effects across multiple frontier models.</span>
- **[Interpretability in Parameter Space: Minimizing Mechanistic Description Length with Attribution-based Parameter Decomposition](https://arxiv.org/abs/2501.14926)**, *Dan Braun, Lucius Bushnaq, Stefan Heimersheim et al.*, 2025-01-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:8126196f]</span>, <span style="color:#777">Summary: Introduces Attribution-based Parameter Decomposition (APD), a method for decomposing neural network parameters into mechanistic components by minimizing description length. Demonstrates effectiveness on toy models by recovering ground truth mechanisms in superposition, compressed computations, and cross-layer representations.</span>
- **[Activation space interpretability may be doomed](https://lesswrong.com/posts/gYfpPbww3wQRaxAFD/activation-space-interpretability-may-be-doomed)**, *bilalchughtai, Lucius Bushnaq*, 2025-01-08, LessWrong / AI Alignment Forum, <span style="color:#777">[lesswrong, sr=0.80, id:98fb9952]</span>, <span style="color:#777">Summary: Argues that activation-space interpretability methods (SAEs, PCA) decomposing individual layers in isolation likely find features explaining activation statistics rather than features the model actually uses for computation, presenting multiple theoretical examples of failure modes and suggesting alternatives that leverage wider model structure.</span>
- **[Understanding In-context Learning of Addition via Activation Subspaces](https://arxiv.org/abs/2505.05145)**, *Xinyan Hu, Kayo Yin, Michael I. Jordan et al.*, 2025-05-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:c2bf5324]</span>, <span style="color:#777">Summary: Studies how transformers implement in-context learning through mechanistic analysis of addition tasks, introducing a novel optimization method to localize few-shot ability to specific attention heads and identifying low-dimensional computational structures including trigonometric patterns and self-correction mechanisms.</span>
- **[Identifying Sparsely Active Circuits Through Local Loss Landscape Decomposition](https://arxiv.org/abs/2504.00194)**, *Brianna Chrisman, Lucius Bushnaq, Lee Sharkey*, 2025-03-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:47a9f408]</span>, <span style="color:#777">Summary: Introduces Local Loss Landscape Decomposition (L3D), a new method for identifying circuits in neural networks by finding low-rank subnetworks in parameter space that reconstruct loss gradients, validated on toy models and applied to transformers and CNNs.</span>
- **[Constrained belief updates explain geometric structures in transformer representations](https://arxiv.org/abs/2502.01954)**, *Mateusz Piotrowski, Paul M. Riechers, Daniel Filan et al.*, 2025-02-04, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.75, id:2906e09b]</span>, <span style="color:#777">Summary: Provides theoretical framework showing that transformers implement constrained Bayesian belief updating, using analysis of single-layer transformers trained on hidden Markov models to predict geometric structures in representations and attention patterns.</span>
- **[LLMs Process Lists With General Filter Heads](https://arxiv.org/abs/2510.26784)**, *Arnab Sen Sharma, Giordano Rogers, Natalie Shapira et al.*, 2025-10-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:58394d29]</span>, <span style="color:#777">Summary: Uses causal mediation analysis to discover that LLMs learn compact representations of filtering operations through specialized attention heads ('filter heads') that encode general predicates portable across different collections, formats, and languages, mirroring functional programming patterns.</span>
- **[Language Models Use Trigonometry to Do Addition](https://arxiv.org/abs/2502.00873)**, *Subhash Kantamneni, Max Tegmark*, 2025-02-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:d6bfb1f0]</span>, <span style="color:#777">Summary: Reverse-engineers how three mid-sized LLMs compute addition, discovering that numbers are represented as a generalized helix structure that models manipulate using a 'Clock' algorithm, verified through causal interventions at multiple network levels.</span>
- **[Generalization or Hallucination? Understanding Out-of-Context Reasoning in Transformers](https://arxiv.org/abs/2506.10887)**, *Yixiao Huang, Hanlin Zhu, Tianyu Guo et al.*, 2025-06-12, NeurIPS 2025, <span style="color:#777">[paper_preprint, sr=0.75, id:fc4a1411]</span>, <span style="color:#777">Summary: Identifies and formalizes out-of-context reasoning (OCR) as a unified mechanism explaining both generalization and hallucination in LLMs, showing through empirical experiments across five LLMs and theoretical analysis that gradient descent's implicit bias causes models to associate concepts regardless of causal vs. spurious correlation.</span>
- **[From Memorization to Reasoning in the Spectrum of Loss Curvature](https://arxiv.org/abs/2510.24256)**, *Jack Merullo, Srihita Vatsavaya, Lucius Bushnaq et al.*, 2025-10-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:2502577e]</span>, <span style="color:#777">Summary: Develops a weight editing procedure based on loss curvature decomposition to identify and remove memorization in transformers, demonstrating more effective suppression of memorized content than existing unlearning methods while analyzing downstream effects on tasks like fact retrieval and arithmetic.</span>
- **[Adversarial Examples Are Not Bugs, They Are Superposition](https://arxiv.org/abs/2508.17456)**, *Liv Gorton, Owen Lewis*, 2025-08-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:7296f00e]</span>, <span style="color:#777">Summary: Presents theoretical and empirical evidence that superposition (a mechanistic interpretability concept) is a primary cause of adversarial examples, with experiments on toy models and ResNet18 showing bidirectional causal relationships between superposition and adversarial robustness.</span>
- **[Mixing Mechanisms: How Language Models Retrieve Bound Entities In-Context](https://arxiv.org/abs/2510.06182)**, *Yoav Gur-Arieh, Mor Geva, Atticus Geiger*, 2025-10-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:38b5513f]</span>, <span style="color:#777">Summary: Studies how language models bind and retrieve entities in-context, discovering that models use three distinct mechanisms (positional, lexical, and reflexive) that combine to drive retrieval behavior across nine models and ten binding tasks.</span>
- **[Transformers Struggle to Learn to Search](https://arxiv.org/abs/2412.04703)**, *Abulhair Saparov, Srushti Pawar, Shreyas Pimpalgaonkar et al.*, 2024-12-06, ICLR 2025, <span style="color:#777">[paper_preprint, sr=0.72, id:f6ec26de]</span>, <span style="color:#777">Summary: Studies whether transformers can learn search algorithms using graph connectivity as a testbed, finding they can learn search on small graphs but struggle to generalize to larger graphs even with more parameters. Uses mechanistic interpretability to extract and analyze the learned parallel search algorithm.</span>
- **[Which Attention Heads Matter for In-Context Learning?](https://arxiv.org/abs/2502.14010)**, *Kayo Yin, Jacob Steinhardt*, 2025-02-19, ICML 2025, <span style="color:#777">[paper_preprint, sr=0.70, id:a64d272b]</span>, <span style="color:#777">Summary: Empirical study of 12 language models comparing induction heads versus function vector (FV) heads in driving in-context learning, finding that FV heads are primary drivers especially in larger models, and that many FV heads evolve from induction heads during training.</span>
- **[How Do LLMs Perform Two-Hop Reasoning in Context?](https://arxiv.org/abs/2502.13913)**, *Tianyu Guo, Hanlin Zhu, Ruiqi Zhang et al.*, 2025-02-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.70, id:3eae0f3f]</span>, <span style="color:#777">Summary: Investigates how LLMs perform two-hop logical reasoning by training transformers from scratch on synthetic tasks and reverse-engineering their internal mechanisms, revealing a sharp phase transition from random guessing to structured sequential query mechanisms.</span>
- **[Blink of an eye: a simple theory for feature localization in generative models](https://arxiv.org/abs/2502.00921)**, *Marvin Li, Aayush Karan, Sitan Chen*, 2025-06-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:738579b1]</span>, <span style="color:#777">Summary: Develops a unifying mathematical theory using stochastic localization samplers to explain why generative models (both autoregressive LLMs and diffusion models) make key decisions in narrow 'critical windows' during generation, with empirical validation showing these windows coincide with problem-solving failures in LLMs.</span>
- **[We Can Monitor AI's Thoughts… For Now | Google DeepMind's Neel Nanda](https://youtube.com/watch?v=5FdO1MEumbI)**, *Neel Nanda, Rob Wiblin*, 2025-09-08, 80,000 Hours Podcast, <span style="color:#777">[podcast, sr=0.62, id:42c56942]</span>, <span style="color:#777">Summary: Comprehensive 3-hour interview with Neel Nanda discussing mechanistic interpretability's current state, limitations, and future. Argues the ambitious vision of deeply understanding AI cognition is likely unachievable, advocating instead for a 'Swiss cheese' layered safety approach combining mech interp successes (SAEs, probes detecting harmful intentions) with other techniques.</span>
- **[Wide Neural Networks as a Baseline for the Computational No-Coincidence Conjecture](https://openreview.net/forum?id=m4OpQAK3eY)**, *John Dunbar, Scott Aaronson*, 2025-07-07, ODYSSEY 2025 Conference, <span style="color:#777">[paper_preprint, sr=0.58, id:aad5b340]</span>, <span style="color:#777">Summary: Establishes that randomly initialized wide neural networks with zero-mean activation functions (like tanh) have nearly independent outputs, proposing these as constructions for studying the computational no-coincidence conjecture about interpretability limits.</span>
- **[Do Language Models Use Their Depth Efficiently?](https://arxiv.org/abs/2505.13898)**, *Róbert Csordás, Christopher D. Manning, Christopher Potts*, 2025-05-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.55, id:b5bf4357]</span>, <span style="color:#777">Summary: Analyzes how deep LLMs (Llama 3.1 and Qwen 3 families) use their depth by examining residual streams, layer contributions, and compositional behavior, finding that deeper models spread the same computations over more layers rather than learning fundamentally new kinds of computation.</span>
- **[Disjoint Processing Mechanisms of Hierarchical and Linear Grammars in Large Language Models](https://arxiv.org/abs/2501.08618)**, *Aruna Sankaranarayanan, Dylan Hadfield-Menell, Aaron Mueller*, 2025-01-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.55, id:12530f4b]</span>, <span style="color:#777">Summary: Investigates whether LLMs develop functionally distinct regions for processing hierarchical versus linear grammars, finding through ablation experiments that models have separate components for each grammar type, with hierarchy-selective components active even on nonce words.</span>
- **[On the creation of narrow AI: hierarchy and nonlocality of neural network skills](https://arxiv.org/abs/2505.15811)**, *Eric J. Michaud, Asher Parker-Sartori, Max Tegmark*, 2025-05-21, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.52, id:e67a9355]</span>, <span style="color:#777">Summary: Studies how to create narrow AI systems through experiments on training from scratch versus transferring skills from large models, finding that hierarchical skill dependencies require broad training distributions and that pruning-based transfer can outperform distillation despite skill nonlocality.</span>
- **[Error: Content Unavailable (429: Too Many Requests)](https://lesswrong.com/posts/ZxFchCFJFcgysYsT9/compressed-computation-is-probably-not-computation-in)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:bb688147]</span>, <span style="color:#777">Summary: Content could not be accessed due to HTTP 429 error (Too Many Requests). The URL suggests this is a LessWrong post with a title related to 'compressed computation' but the actual content is unavailable.</span>


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
- **[Toward universal steering and monitoring of AI models](https://arxiv.org/abs/2502.03708)**, *Daniel Beaglehole, Adityanarayanan Radhakrishnan, Enric Boix-Adserà et al.*, 2025-05-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:c9815a35]</span>, <span style="color:#777">Summary: Develops a scalable approach for extracting linear representations of general concepts from large-scale AI models, demonstrating their effectiveness for both steering model behavior and monitoring misaligned content like hallucinations and toxicity.</span>
- **[The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence](https://arxiv.org/abs/2502.17420)**, *Tom Wollschläger, Jannes Elstner, Simon Geisler et al.*, 2025-02-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:1ba74d84]</span>, <span style="color:#777">Summary: Proposes a novel gradient-based approach to identify refusal directions in LLMs, discovering multiple independent directions and multi-dimensional concept cones that mediate refusal behavior, introducing the concept of representational independence to account for both linear and non-linear intervention effects.</span>
- **[Interpreting Emergent Planning in Model-Free Reinforcement Learning](https://arxiv.org/abs/2504.01871)**, *Thomas Bush, Stephen Chung, Usman Anwar et al.*, 2025-04-02, arXiv (ICLR 2025 oral), <span style="color:#777">[paper_preprint, sr=0.85, id:5fb8edfe]</span>, <span style="color:#777">Summary: Applies concept-based interpretability to demonstrate mechanistically that model-free RL agents learn to plan internally, using probing, plan formation analysis, and causal interventions on a DRC agent in Sokoban.</span>
- **[How Do LLMs Persuade? Linear Probes Can Uncover Persuasion Dynamics in Multi-Turn Conversations](https://arxiv.org/abs/2508.05625)**, *Brandon Jaipersaud, David Krueger, Ekdeep Singh Lubana*, 2025-08-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:60c15241]</span>, <span style="color:#777">Summary: Applies linear probes to study persuasion dynamics in LLM conversations, training probes to detect persuasion success, persuadee personality, and persuasion strategies across multi-turn interactions.</span>


---

#### <span style="font-size:1.3em">Model diffing</span> <span style="color:#bbb">[cat:model_diff]</span>

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
- **[Overcoming Sparsity Artifacts in Crosscoders to Interpret Chat-Tuning](https://arxiv.org/abs/2504.02922)**, *Julian Minder, Clément Dumas, Caden Juang et al.*, 2025-04-03, NeurIPS 2025, <span style="color:#777">[paper_preprint, sr=0.92, id:d90cbd1f]</span>, <span style="color:#777">Summary: Identifies and mitigates two artifacts in crosscoders (sparse dictionary learning for model diffing) that misattribute concepts to fine-tuned models, develops Latent Scaling technique and BatchTopK training loss to improve crosscoder methodology, and successfully identifies interpretable chat-specific latents including refusal-related features in Gemma 2 2B.</span>
- **[Narrow Finetuning Leaves Clearly Readable Traces in Activation Differences](https://arxiv.org/abs/2510.13900)**, *Julian Minder, Clément Dumas, Stewart Slocum et al.*, 2025-10-14, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.85, id:945228fb]</span>, <span style="color:#777">Summary: Empirical study demonstrating that narrow finetuning creates strong, interpretable biases in LLM activations that can be discovered through model diffing, with implications for emergent misalignment and safety research practices using narrowly finetuned models.</span>
- **[Model Diffing without Borders: Unlocking Cross-Architecture Model Diffing to Reveal Hidden Ideological Alignment in Llama and Qwen](https://openreview.net/forum?id=ZB84SvrZB8)**, *Thomas Jiralerspong, Trenton Bricken*, 2025-09-30, NeurIPS 2025 Workshop MechInterp, <span style="color:#777">[paper_published, sr=0.82, id:d8906bad]</span>, <span style="color:#777">Summary: Introduces Dedicated Feature Crosscoders (DFCs) to enable the first successful model diff between architecturally different AI models (Llama-3.1-8B vs Qwen3-8B), uncovering model-exclusive ideological alignment features that causally control censorship and narrative promotion behaviors.</span>
- **[Diffing Toolkit: Model Comparison and Analysis Framework](https://github.com/science-of-finetuning/diffing-toolkit)**, *Julian Minder, Clément Dumas*, 2025-11-07, GitHub, <span style="color:#777">[code_tool, sr=0.70, id:45261ab6]</span>, <span style="color:#777">Summary: A research framework for analyzing differences between language models through interpretability techniques, enabling systematic comparison of base models and finetuned variants using methods like Activation Difference Lens.</span>


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
- **[Open Problems in Mechanistic Interpretability](https://arxiv.org/abs/2501.16496)**, *Lee Sharkey, Bilal Chughtai, Joshua Batson et al.*, 2025-01-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:6ada11f7]</span>, <span style="color:#777">Summary: Forward-facing review identifying and prioritizing open problems in mechanistic interpretability that require solutions before scientific and practical benefits can be realized, covering conceptual improvements, application methods, and socio-technical challenges.</span>
- **[The Urgency of Interpretability](https://darioamodei.com/post/the-urgency-of-interpretability)**, *Dario Amodei*, 2025, darioamodei.com, <span style="color:#777">[blog_post, sr=0.75, id:f19373dc]</span>, <span style="color:#777">Summary: Advocates for prioritizing mechanistic interpretability research before AI systems become too powerful, arguing that understanding model internals is essential for detecting deception, preventing misuse, and ensuring alignment of advanced AI systems.</span>
- **[Interpretability Will Not Reliably Find Deceptive AI](https://www.alignmentforum.org/posts/PwnadG4BFjaER3MGf/interpretability-will-not-reliably-find-deceptive-ai)**, *Neel Nanda*, 2025-05-04, AI Alignment Forum, <span style="color:#777">[🔄 lesswrong, sr=0.72, id:ee7244f2]</span>, <span style="color:#777">Summary: Argues that interpretability research, while valuable, will not reliably detect deception in superintelligent AI systems due to fundamental limitations like superposition and difficulty proving negatives, and should instead be viewed as one component in a defense-in-depth portfolio strategy alongside black-box methods.</span>
- **[Because we have LLMs, we Can and Should Pursue Agentic Interpretability](https://arxiv.org/abs/2506.12152)**, *Been Kim, John Hewitt, Neel Nanda et al.*, 2025-06-13, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:2b0b4ca7]</span>, <span style="color:#777">Summary: Proposes agentic interpretability as a new paradigm where LLMs proactively assist human understanding through multi-turn conversations by developing mental models of users, enabling humans to better understand potentially superhuman AI concepts.</span>
- **[Propositional Interpretability in Artificial Intelligence](https://arxiv.org/abs/2501.15740)**, *David J. Chalmers*, 2025-01-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:02be0447]</span>, <span style="color:#777">Summary: Proposes propositional interpretability as a framework for mechanistic interpretability, arguing AI systems should be interpreted in terms of propositional attitudes (beliefs, desires, probabilities). Analyzes current interpretability methods (probing, SAEs, chain-of-thought) through this philosophical lens and introduces the challenge of 'thought logging'.</span>
- **[Explainable and Interpretable Multimodal Large Language Models: A Comprehensive Survey](https://arxiv.org/abs/2412.02104)**, *Yunkai Dang, Kaichen Huang, Jiahao Huo et al.*, 2024-12-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.58, id:60b323f8]</span>, <span style="color:#777">Summary: Comprehensive survey of interpretability and explainability methods for multimodal large language models, proposing a novel framework that categorizes research across data, model, and training/inference perspectives.</span>
- **[The Loss Kernel: A Geometric Probe for Deep Learning Interpretability](https://arxiv.org/abs/2509.26537)**, *Maxwell Adam, Zach Furman, Jesse Hoogland*, 2025-09-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.55, id:547cdca6]</span>, <span style="color:#777">Summary: Introduces the loss kernel, an interpretability method that measures similarity between data points via the covariance of per-sample losses under parameter perturbations, validated on synthetic multitask problems and applied to Inception-v1 on ImageNet.</span>
- **[Through a Steerable Lens: Magnifying Neural Network Interpretability via Phase-Based Extrapolation](https://arxiv.org/abs/2506.02300)**, *Farzaneh Mahdisoltani, Saeed Mahdisoltani, Roger B. Grosse et al.*, 2025-06-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.55, id:1b1f65af]</span>, <span style="color:#777">Summary: Proposes a novel interpretability framework that visualizes classifier decision boundaries by amplifying class-conditional gradients in Complex Steerable Pyramid space, producing semantically meaningful morphs that reveal how models distinguish between classes.</span>
- **[Harmonic Loss Trains Interpretable AI Models](https://arxiv.org/abs/2502.01628)**, *David D. Baek, Ziming Liu, Riya Tyagi et al.*, 2025-02-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.48, id:97a1ceb5]</span>, <span style="color:#777">Summary: Introduces harmonic loss as an alternative to cross-entropy for training neural networks, replacing SoftMax with HarMax and using Euclidean distance for logits, with empirical validation showing improved interpretability, faster convergence, and better data efficiency across multiple domains including GPT-2.</span>


---

### <span style="font-size:1.4em">Data interpretability</span> <span style="color:#bbb">[cat:datainterp]</span>


---

#### <span style="font-size:1.3em">Auditing real models</span> <span style="color:#bbb">[cat:interp_applied]</span>

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
- **[On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)**, *Jack Lindsey, Wes Gurnee, Emmanuel Ameisen et al.*, 2025-03-27, Transformer Circuits Thread, <span style="color:#777">[paper_published, sr=0.90, id:fbc2b9d8]</span>, <span style="color:#777">Summary: Applies attribution graph methodology using cross-layer transcoders to mechanistically understand internal computations in Claude 3.5 Haiku across diverse behaviors including planning in poetry, jailbreaks, hallucinations, refusals, chain-of-thought faithfulness, and hidden goals in misaligned models.</span>
- **[Reward Model Interpretability via Optimal and Pessimal Tokens](https://arxiv.org/abs/2506.07326)**, *Brian Christian, Hannah Rose Kirk, Jessica A.F. Thompson et al.*, 2025-06-08, FAccT '25 (ACM Conference on Fairness, Accountability, and Transparency), <span style="color:#777">[paper_preprint, sr=0.88, id:2f52f504]</span>, <span style="color:#777">Summary: Systematically analyzes ten open-source reward models by exhaustively testing how they score every possible single-token response to value-laden prompts, revealing substantial heterogeneity between models, systematic asymmetries, sensitivity to prompt framing, and concerning identity biases.</span>
- **[Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)**, *Emmanuel Ameisen, Jack Lindsey, Adam Pearce et al.*, 2025-03-27, Transformer Circuits Thread, <span style="color:#777">[blog_post, sr=0.88, id:7bab6395]</span>, <span style="color:#777">Summary: Introduces cross-layer transcoders (CLTs) and attribution graphs methodology for understanding language model computations by tracing computational steps through an interpretable replacement model, with extensive validation and applications to both toy models and Claude 3.5 Haiku.</span>
- **[LLMs Encode Harmfulness and Refusal Separately](https://arxiv.org/abs/2507.11878)**, *Jiachen Zhao, Jing Huang, Zhengxuan Wu et al.*, 2025-07-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:639318ca]</span>, <span style="color:#777">Summary: Identifies that LLMs internally encode harmfulness as a separate concept from refusal through distinct neural directions, and develops Latent Guard - an intrinsic safeguard using latent harmfulness representations that matches Llama Guard 3 8B performance while being robust to finetuning attacks.</span>
- **[LatentQA: Teaching LLMs to Decode Activations Into Natural Language](https://arxiv.org/abs/2412.08686)**, *Alexander Pan, Lijie Chen, Jacob Steinhardt*, 2024-12-11, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:fdfc93f9]</span>, <span style="color:#777">Summary: Introduces LatentQA (answering questions about model activations in natural language) and Latent Interpretation Tuning (LIT), which finetunes a decoder LLM to interpret activations, demonstrating applications in extracting knowledge, controlling model behavior, and revealing harmful capabilities.</span>
- **[Thought Branches: Interpreting LLM Reasoning Requires Resampling](https://arxiv.org/abs/2510.27484)**, *Uzay Macar, Paul C. Bogdan, Senthooran Rajamanoharan et al.*, 2025-10-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:3a5e3fcc]</span>, <span style="color:#777">Summary: Introduces resampling-based methodology for studying distributions over chain-of-thought reasoning rather than single samples, enabling causal analysis of model reasoning through four case studies including alignment faking, on-policy vs off-policy interventions, reasoning step removal resilience, and unfaithful CoT analysis.</span>
- **[Narrow Finetuning Leaves Clearly Readable Traces in Activation Differences](https://arxiv.org/abs/2510.13900)**, *Julian Minder, Clément Dumas, Stewart Slocum et al.*, 2025-10-14, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.85, id:945228fb]</span>, <span style="color:#777">Summary: Empirical study demonstrating that narrow finetuning creates strong, interpretable biases in LLM activations that can be discovered through model diffing, with implications for emergent misalignment and safety research practices using narrowly finetuned models.</span>
- **[Base Models Know How to Reason, Thinking Models Learn When](https://arxiv.org/abs/2510.07364)**, *Constantin Venhoff, Iván Arcuschin, Philip Torr et al.*, 2025-10-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:3746f2bd]</span>, <span style="color:#777">Summary: Investigates why thinking models like DeepSeek R1 outperform base models by introducing a hybrid approach that activates reasoning mechanisms in base models at the right time, recovering up to 91% of the performance gap without weight updates.</span>
- **[Simple Mechanistic Explanations for Out-Of-Context Reasoning](https://arxiv.org/abs/2507.08218)**, *Atticus Wang, Joshua Engels, Oliver Clive-Griffin et al.*, 2025-07-10, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:d79f36fc]</span>, <span style="color:#777">Summary: Mechanistically investigates out-of-context reasoning in fine-tuned LLMs, finding that LoRA fine-tuning essentially adds constant steering vectors that cause surprising generalization, with results holding even for model backdoors.</span>
- **[Following the Whispers of Values: Unraveling Neural Mechanisms Behind Value-Oriented Behaviors in LLMs](https://arxiv.org/abs/2504.04994)**, *Ling Hu, Yuemei Xu, Xiaoyang Gu et al.*, 2025-04-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:77957a08]</span>, <span style="color:#777">Summary: Proposes ValueExploration framework to identify and locate neurons encoding social values in LLMs at the neuron level, using activation differences and causal interventions. Creates C-voice, a bilingual benchmark for evaluating Chinese Social Values, and validates on four representative LLMs.</span>
- **[Emergent Symbolic Mechanisms Support Abstract Reasoning in Large Language Models](https://arxiv.org/abs/2502.20332)**, *Yukang Yang, Declan Campbell, Kaixuan Huang et al.*, 2025-02-27, arXiv (accepted to ICML 2025), <span style="color:#777">[paper_preprint, sr=0.78, id:440c0e92]</span>, <span style="color:#777">Summary: Identifies an emergent symbolic architecture in large language models that implements abstract reasoning through three computational mechanisms: symbol abstraction heads, symbolic induction heads, and retrieval heads operating across different network layers.</span>
- **[Interpreting learned search: finding a transition model and value function in an RNN that plays Sokoban](https://arxiv.org/abs/2506.10138)**, *Mohammad Taufeeque, Aaron David Tucker, Adam Gleave et al.*, 2025-06-11, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:6eb32d55]</span>, <span style="color:#777">Summary: Reverse-engineers a convolutional RNN trained with model-free RL to play Sokoban, discovering learned mechanisms analogous to classical bidirectional search including state-action value functions, transition models formed by specialized kernels, and layer-wise search depth increases.</span>
- **[Thought Anchors: Which LLM Reasoning Steps Matter?](https://arxiv.org/abs/2506.19143)**, *Paul C. Bogdan, Uzay Macar, Neel Nanda et al.*, 2025-06-23, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:327fbd7d]</span>, <span style="color:#777">Summary: Introduces a black-box method for measuring counterfactual importance of individual sentences in LLM reasoning traces by sampling replacement sentences and quantifying impact on final answers. Discovers 'thought anchors' - planning and uncertainty management sentences that disproportionately influence reasoning trajectories and are consistently attended to by specialized attention heads.</span>
- **[Reasoning-Finetuning Repurposes Latent Representations in Base Models](https://arxiv.org/abs/2507.12638)**, *Jake Ward, Chuqiao Lin, Constantin Venhoff et al.*, 2025-07-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:55610cb7]</span>, <span style="color:#777">Summary: Studies how backtracking behavior emerges in reasoning-finetuned models (DeepSeek-R1-Distill-Llama-8B), finding that a direction from the base model can induce backtracking when used to steer the reasoning model, suggesting reasoning finetuning repurposes pre-existing representations rather than learning new capabilities from scratch.</span>
- **[The CoT Encyclopedia: Analyzing, Predicting, and Controlling how a Reasoning Model will Think](https://arxiv.org/abs/2505.10185)**, *Seongyun Lee, Seungone Kim, Minju Seo et al.*, 2025-05-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:0c81437b]</span>, <span style="color:#777">Summary: Introduces the CoT Encyclopedia, a bottom-up framework that automatically extracts, clusters, and analyzes reasoning strategies from model-generated chain-of-thought outputs, enabling prediction and steering of reasoning behavior.</span>
- **[Why and How LLMs Hallucinate: Connecting the Dots with Subsequence Associations](https://arxiv.org/abs/2504.12691)**, *Yiyou Sun, Yu Gai, Lijie Chen et al.*, 2025-04-17, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:a46e4ea3]</span>, <span style="color:#777">Summary: Introduces a subsequence association framework to systematically trace and understand LLM hallucinations, proposing that hallucinations arise when dominant hallucinatory associations outweigh faithful ones. Develops a tracing algorithm that identifies causal subsequences by analyzing hallucination probabilities across randomized contexts and validates it empirically.</span>
- **[Too Late to Recall: The Two-Hop Problem in Multimodal Knowledge Retrieval](https://openreview.net/forum?id=VUhRdZp8ke)**, *Constantin Venhoff, Ashkan Khakzar, Sonia Joseph et al.*, 2025-03-31, CVPR 2025 Workshop MIV, <span style="color:#777">[paper_published, sr=0.70, id:a2714e74]</span>, <span style="color:#777">Summary: Applies mechanistic interpretability to Vision-Language Models to explain why they struggle with factual recall, identifying a 'two-hop' problem where visual representations emerge too late in the model to engage early-layer factual recall mechanisms.</span>
- **[Large Language Models Think Too Fast To Explore Effectively](https://arxiv.org/abs/2501.18009)**, *Lan Pan, Hanbo Xie, Robert C. Wilson*, 2025-01-29, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:38b1408a]</span>, <span style="color:#777">Summary: Empirically evaluates LLM exploration capabilities using Little Alchemy 2, comparing human and model strategies, and uses Sparse Autoencoders to analyze internal representations revealing that LLMs process uncertainty at earlier layers than empowerment values, leading to premature decisions.</span>


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
- **[Sparse Autoencoders Learn Monosemantic Features in Vision-Language Models](https://arxiv.org/abs/2504.02821)**, *Mateusz Pach, Shyamgopal Karthik, Quentin Bouniot et al.*, 2025-04-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:c4cd50fa]</span>, <span style="color:#777">Summary: Extends sparse autoencoders (SAEs) to Vision-Language Models like CLIP, introducing a comprehensive framework for evaluating monosemanticity in vision representations validated by user study, and demonstrating that SAE interventions can directly steer multimodal LLM outputs.</span>
- **[I Have Covered All the Bases Here: Interpreting Reasoning Features in Large Language Models via Sparse Autoencoders](https://arxiv.org/abs/2503.18878)**, *Andrey Galichin, Alexey Dontsov, Polina Druzhinina et al.*, 2025-03-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:6f4380b6]</span>, <span style="color:#777">Summary: Introduces ReasonScore, an automatic metric to identify reasoning features in LLMs using Sparse Autoencoders, and demonstrates through steering experiments that amplifying these features increases performance on reasoning benchmarks (+2.2%) while producing longer reasoning traces (+20.5%).</span>
- **[Sparse Autoencoders Do Not Find Canonical Units of Analysis](https://arxiv.org/abs/2502.04878)**, *Patrick Leask, Bart Bussmann, Michael Pearce et al.*, 2025-02-07, arXiv (accepted to ICLR 2025), <span style="color:#777">[paper_preprint, sr=0.88, id:1464db08]</span>, <span style="color:#777">Summary: Introduces two novel techniques (SAE stitching and meta-SAEs) to demonstrate that Sparse Autoencoders do not find canonical units of analysis, showing they are incomplete and that their latents are not atomic but decompose into combinations of smaller features.</span>
- **[Transcoders Beat Sparse Autoencoders for Interpretability](https://arxiv.org/abs/2501.18823)**, *Gonçalo Paulo, Stepan Shabalin, Nora Belrose*, 2025-01-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:d74cf9d5]</span>, <span style="color:#777">Summary: Empirically compares transcoders and sparse autoencoders (SAEs) for neural network interpretability, finding transcoders produce more interpretable features, and proposes skip transcoders which improve reconstruction loss without sacrificing interpretability.</span>
- **[Decomposing MLP Activations into Interpretable Features via Semi-Nonnegative Matrix Factorization](https://arxiv.org/abs/2506.10920)**, *Or Shafran, Atticus Geiger, Mor Geva*, 2025-06-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:ddf15a4d]</span>, <span style="color:#777">Summary: Proposes semi-nonnegative matrix factorization (SNMF) to decompose MLP activations into interpretable features as an alternative to sparse autoencoders, with experiments on Llama 3.1, Gemma 2, and GPT-2 showing superior performance on causal steering tasks.</span>
- **[The Unintended Trade-off of AI Alignment:Balancing Hallucination Mitigation and Safety in LLMs](https://arxiv.org/abs/2510.07775)**, *Omar Mahmoud, Ali Khalil, Buddhika Laknath Semage et al.*, 2025-10-09, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:893e97c4]</span>, <span style="color:#777">Summary: Empirically demonstrates that improving truthfulness in LLMs weakens safety alignment (refusal behavior) due to overlapping model components, and proposes a method using sparse autoencoders and subspace orthogonalization to disentangle and preserve refusal features during fine-tuning.</span>
- **[Scaling sparse feature circuit finding for in-context learning](https://arxiv.org/abs/2504.13756)**, *Dmitrii Kharlapenko, Stepan Shabalin, Fazl Barez et al.*, 2025-04-18, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:58cc1049]</span>, <span style="color:#777">Summary: Scales sparse feature circuit finding methodology to Gemma-1 2B (30x larger than prior work) and uses SAEs to discover task-detecting and task-execution features that causally mediate in-context learning, showing task vectors are well approximated by sparse sums of SAE latents.</span>
- **[Learning Multi-Level Features with Matryoshka Sparse Autoencoders](https://arxiv.org/abs/2503.17547)**, *Bart Bussmann, Noa Nabeshima, Adam Karvonen et al.*, 2025-03-21, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:024d1468]</span>, <span style="color:#777">Summary: Introduces Matryoshka SAEs, which simultaneously train multiple nested sparse autoencoder dictionaries of increasing size to organize features hierarchically, with smaller dictionaries learning general concepts and larger ones learning specific concepts without absorbing high-level features.</span>
- **[Are Sparse Autoencoders Useful? A Case Study in Sparse Probing](https://arxiv.org/abs/2502.16681)**, *Subhash Kantamneni, Joshua Engels, Senthooran Rajamanoharan et al.*, 2025-02-23, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:6d1cf1de]</span>, <span style="color:#777">Summary: Empirically evaluates whether sparse autoencoders (SAEs) improve performance on LLM activation probing tasks across four challenging regimes (data scarcity, class imbalance, label noise, covariate shift), comparing SAEs against strong baselines.</span>
- **[Sparse Autoencoders Trained on the Same Data Learn Different Features](https://arxiv.org/abs/2501.16615)**, *Gonçalo Paulo, Nora Belrose*, 2025-01-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:3ae94c3e]</span>, <span style="color:#777">Summary: Empirical study showing that Sparse Autoencoders (SAEs) trained on identical data with different random seeds learn different feature sets, with only 30% feature overlap in a 131K latent SAE trained on Llama 3 8B, suggesting SAE features should be viewed as pragmatic decompositions rather than true underlying features.</span>
- **[Priors in Time: Missing Inductive Biases for Language Model Interpretability](https://arxiv.org/abs/2511.01836)**, *Ekdeep Singh Lubana, Can Rager, Sai Sumedh R. Hindupur et al.*, 2025-11-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:8abd45df]</span>, <span style="color:#777">Summary: Critiques Sparse Autoencoders for assuming temporal independence in language model representations and proposes Temporal Feature Analysis, a new interpretability method with temporal inductive bias that decomposes representations into predictable and novel components.</span>
- **[Inference-Time Decomposition of Activations (ITDA): A Scalable Approach to Interpreting Large Language Models](https://arxiv.org/abs/2505.17769)**, *Patrick Leask, Neel Nanda, Noura Al Moubayed*, 2025-05-23, ICML 2025, <span style="color:#777">[paper_preprint, sr=0.85, id:8a1946f1]</span>, <span style="color:#777">Summary: Introduces ITDA, a computationally efficient alternative to sparse autoencoders for decomposing LLM activations into interpretable features, requiring only 1% of SAE training time and data while enabling cross-model comparisons through greedy dictionary construction via matching pursuit.</span>
- **[Binary Sparse Coding for Interpretability](https://arxiv.org/abs/2509.25596)**, *Lucia Quirke, Stepan Shabalin, Nora Belrose*, 2025-09-29, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:5b3f3a2b]</span>, <span style="color:#777">Summary: Proposes binary sparse autoencoders (BAEs) and binary transcoders (BTCs) that constrain feature activations to 0 or 1, finding that binarization improves interpretability and monosemanticity but increases reconstruction error and ultra-high frequency features.</span>
- **[What's In My Human Feedback? Learning Interpretable Descriptions of Preference Data](https://arxiv.org/abs/2510.26202)**, *Rajiv Movva, Smitha Milli, Sewon Min et al.*, 2025-10-30, arXiv, <span style="color:#777">[⚠️ paper_preprint, sr=0.85, id:e3b78830]</span>, <span style="color:#777">Summary: Introduces WIMHF, a method using sparse autoencoders to extract interpretable features from human preference data, identifying what preferences datasets measure and what annotators actually express across 7 datasets.</span>
- **[Negative Results for SAEs On Downstream Tasks and Deprioritising SAE Research (GDM Mech Interp Team Progress Update #2)](https://alignmentforum.org/posts/4uXCAJNuPKtKBsi28)**, *Lewis Smith, Senthooran Rajamanoharan, Arthur Conmy et al.*, 2025-03-26, AI Alignment Forum, <span style="color:#777">[lesswrong, sr=0.85, id:8fd51914]</span>, <span style="color:#777">Summary: Tests whether sparse autoencoders (SAEs) are useful for downstream safety tasks by evaluating them on out-of-distribution probing for harmful intent detection, finding that SAEs underperform simple linear probes. Also proposes quadratic-frequency penalty variant of JumpReLU SAEs to reduce high-frequency latents and introduces frequency-weighted autointerp metrics.</span>
- **[Partially Rewriting a Transformer in Natural Language](https://arxiv.org/abs/2501.18838)**, *Gonçalo Paulo, Nora Belrose*, 2025-01-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:34033220]</span>, <span style="color:#777">Summary: Attempts to partially rewrite a large language model using natural language explanations by replacing feedforward network components with LLM-based simulators that predict neuron activations from explanations generated via transcoders and sparse autoencoders.</span>
- **[Stochastic Parameter Decomposition](https://arxiv.org/abs/2506.20790)**, *Lucius Bushnaq, Dan Braun, Lee Sharkey*, 2025-06-25, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.82, id:3189ec88]</span>, <span style="color:#777">Summary: Introduces Stochastic Parameter Decomposition (SPD), a method for decomposing neural network parameters into sparsely used vectors that is more scalable and robust than existing Attribution-based Parameter Decomposition (APD), with demonstrations on larger models and released implementation library.</span>
- **[Dense SAE Latents Are Features, Not Bugs](https://arxiv.org/abs/2506.15679)**, *Xiaoqing Sun, Alessandro Stolfo, Joshua Engels et al.*, 2025-06-18, arXiv (NeurIPS 2025), <span style="color:#777">[paper_preprint, sr=0.82, id:3eb1ba44]</span>, <span style="color:#777">Summary: Systematically investigates dense (frequently-activating) latents in sparse autoencoders, demonstrating they are meaningful features rather than training artifacts, and introduces a taxonomy of dense latent types including position tracking, context binding, and entropy regulation.</span>
- **[Evaluating Sparse Autoencoders on Targeted Concept Erasure Tasks](https://arxiv.org/abs/2411.18895)**, *Adam Karvonen, Can Rager, Samuel Marks et al.*, 2024-11-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:14e7708e]</span>, <span style="color:#777">Summary: Introduces automated evaluation metrics for Sparse Autoencoders (SAEs) based on concept erasure tasks, including LLM-automated SHIFT and the new Targeted Probe Perturbation (TPP) metric that quantifies SAE ability to disentangle similar concepts.</span>
- **[Evaluating SAE interpretability without explanations](https://arxiv.org/abs/2507.08473)**, *Gonçalo Paulo, Nora Belrose*, 2025-07-11, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:c897b669]</span>, <span style="color:#777">Summary: Develops methods to evaluate sparse autoencoder (SAE) interpretability without requiring natural language explanations as an intermediate step, comparing automated metrics with human evaluations to provide more direct assessment of discovered latents.</span>
- **[SAEBench: A Comprehensive Benchmark for Sparse Autoencoders in Language Model Interpretability](https://arxiv.org/abs/2503.09532)**, *Adam Karvonen, Can Rager, Johnny Lin et al.*, 2025-06-04, arXiv (accepted to ICML 2025), <span style="color:#777">[paper_preprint, sr=0.80, id:ee0c8e39]</span>, <span style="color:#777">Summary: Introduces SAEBench, a comprehensive benchmark evaluating sparse autoencoders across eight metrics spanning interpretability, feature disentanglement, and practical applications. Open-sources 200+ SAEs across eight architectures and reveals that proxy metrics don't reliably predict practical performance.</span>
- **[Sparse Autoencoders Can Interpret Randomly Initialized Transformers](https://arxiv.org/abs/2501.17727)**, *Thomas Heap, Tim Lawson, Lucy Farnik et al.*, 2025-01-29, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.80, id:6104a767]</span>, <span style="color:#777">Summary: Tests whether sparse autoencoders capture meaningful learned features by applying them to randomly initialized transformers, finding that random and trained models produce similarly interpretable SAE latents with comparable quality metrics.</span>
- **[SAEs Are Good for Steering -- If You Select the Right Features](https://arxiv.org/abs/2505.20063)**, *Dana Arad, Aaron Mueller, Yonatan Belinkov*, 2025-05-26, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:52d3316f]</span>, <span style="color:#777">Summary: Distinguishes between input features (capture patterns in model input) and output features (affect model output) in Sparse Autoencoders, and proposes scoring methods to identify them. Shows that filtering out low-output-score features yields 2-3x improvements in SAE-based steering, making it competitive with supervised methods.</span>
- **[Line of Sight: On Linear Representations in VLLMs](https://arxiv.org/abs/2506.04706)**, *Achyuta Rajaram, Sarah Schwettmann, Jacob Andreas et al.*, 2025-06-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:56f7b629]</span>, <span style="color:#777">Summary: Investigates how vision-language models (specifically LlaVA-Next) represent visual concepts internally by finding linearly decodable ImageNet features and training multimodal Sparse Autoencoders to create interpretable dictionaries of text and image features.</span>
- **[Low-Rank Adapting Models for Sparse Autoencoders](https://arxiv.org/abs/2501.19406)**, *Matthew Chen, Joshua Engels, Max Tegmark*, 2025-01-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:b0cec6f1]</span>, <span style="color:#777">Summary: Proposes using low-rank adaptation (LoRA) to finetune language models around previously trained sparse autoencoders (SAEs), rather than training better SAEs themselves, demonstrating 30-55% reduction in cross-entropy loss gap and 3-20× faster training compared to end-to-end SAE methods.</span>
- **[Enhancing Automated Interpretability with Output-Centric Feature Descriptions](https://arxiv.org/abs/2501.08319)**, *Yoav Gur-Arieh, Roy Mayan, Chen Agassy et al.*, 2025-01-14, arXiv (accepted to ACL 2025), <span style="color:#777">[paper_preprint, sr=0.78, id:e269dec8]</span>, <span style="color:#777">Summary: Proposes output-centric methods for automatically generating feature descriptions in LLMs that better capture causal effects on model outputs, using tokens weighted higher after feature stimulation or applying the unembedding head directly to features.</span>
- **[Decoding Dark Matter: Specialized Sparse Autoencoders for Interpreting Rare Concepts in Foundation Models](https://arxiv.org/abs/2411.00743)**, *Aashiq Muhamed, Mona Diab, Virginia Smith*, 2024-11-01, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:4c1a3600]</span>, <span style="color:#777">Summary: Introduces Specialized Sparse Autoencoders (SSAEs) designed to capture rare but important concepts in foundation models that standard SAEs miss, using dense retrieval for data selection and Tilted Empirical Risk Minimization for training.</span>
- **[Enhancing Neural Network Interpretability with Feature-Aligned Sparse Autoencoders](https://arxiv.org/abs/2411.01220)**, *Luke Marks, Alasdair Paren, David Krueger et al.*, 2024-11-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:438af571]</span>, <span style="color:#777">Summary: Proposes Mutual Feature Regularization (MFR), a regularization technique that improves Sparse Autoencoder training by encouraging parallel SAEs to learn similar features, thereby learning features more aligned with actual input features rather than spurious patterns.</span>
- **[BatchTopK Sparse Autoencoders](https://arxiv.org/abs/2412.06410)**, *Bart Bussmann, Patrick Leask, Neel Nanda*, 2024-12-09, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:a9e74606]</span>, <span style="color:#777">Summary: Introduces BatchTopK SAEs, a training method that improves upon TopK sparse autoencoders by relaxing the top-k constraint to batch-level, allowing variable numbers of active latents per sample and improving reconstruction without sacrificing sparsity.</span>
- **[Towards Understanding Distilled Reasoning Models: A Representational Approach](https://arxiv.org/abs/2503.03730)**, *David D. Baek, Max Tegmark*, 2025-03-05, ICLR 2025 Workshop on Building Trust in Language Models and Applications, <span style="color:#777">[paper_preprint, sr=0.75, id:b685a204]</span>, <span style="color:#777">Summary: Uses crosscoders to analyze how model distillation impacts reasoning feature development in Qwen-series LLMs, finding unique reasoning feature directions that enable steering and examining changes in feature geometry during distillation.</span>
- **[Understanding sparse autoencoder scaling in the presence of feature manifolds](https://arxiv.org/abs/2509.02565)**, *Eric J. Michaud, Liv Gorton, Tom McGrath*, 2025-09-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:d40880ce]</span>, <span style="color:#777">Summary: Adapts capacity-allocation models from neural scaling literature to understand how sparse autoencoders (SAEs) scale with number of latents, particularly studying how multi-dimensional feature manifolds create pathological regimes where SAEs learn far fewer features than expected.</span>
- **[Internal states before wait modulate reasoning patterns](https://arxiv.org/abs/2510.04128)**, *Dmitrii Troitskii, Koyena Pal, Chris Wendler et al.*, 2025-10-05, arXiv (EMNLP Findings 2025), <span style="color:#777">[paper_preprint, sr=0.75, id:3cf71cd4]</span>, <span style="color:#777">Summary: Trains crosscoders on DeepSeek-R1-Distill-Llama-8B and introduces a latent attribution technique to identify internal features that modulate reasoning behaviors like backtracking, with causal interventions demonstrating these features influence patterns such as restarting, recalling knowledge, expressing uncertainty, and double-checking.</span>
- **[Do Sparse Autoencoders Generalize? A Case Study of Answerability](https://arxiv.org/abs/2502.19964)**, *Lovis Heindrich, Philip Torr, Fazl Barez et al.*, 2025-02-27, ICML 2025 Workshop on Reliable and Responsible Foundation Models (arXiv preprint), <span style="color:#777">[paper_preprint, sr=0.72, id:6ef1fce0]</span>, <span style="color:#777">Summary: Empirically evaluates whether sparse autoencoder (SAE) features generalize across domains by testing Gemma 2 SAEs on diverse answerability datasets, finding that SAE features show inconsistent out-of-domain transfer compared to residual stream probes.</span>
- **[Position: Mechanistic Interpretability Should Prioritize Feature Consistency in SAEs](https://arxiv.org/abs/2505.20254)**, *Xiangchen Song, Aashiq Muhamed, Yujia Zheng et al.*, 2025-05-26, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:b53d8f15]</span>, <span style="color:#777">Summary: Proposes prioritizing feature consistency in Sparse Autoencoders (SAEs) for mechanistic interpretability, introducing the Pairwise Dictionary Mean Correlation Coefficient (PW-MCC) metric and demonstrating that TopK SAEs achieve high consistency (0.80) through theoretical validation with model organisms and empirical validation on LLM activations.</span>
- **[How Visual Representations Map to Language Feature Space in Multimodal LLMs](https://arxiv.org/abs/2506.11976)**, *Constantin Venhoff, Ashkan Khakzar, Sonia Joseph et al.*, 2025-06-13, arXiv, <span style="color:#777">[paper_preprint, sr=0.70, id:fb98edde]</span>, <span style="color:#777">Summary: Uses pre-trained sparse autoencoders (SAEs) to analyze how visual representations from a frozen ViT align with language feature representations in a frozen LLM through a linear adapter in vision-language models.</span>
- **[SPD - Stochastic Parameter Decomposition](https://github.com/goodfire-ai/spd)**, *Dan Braun, Oli Clive-Griffin, Lee Sharkey*, 2025-09-04, GitHub, <span style="color:#777">[code_tool, sr=0.68, id:23a560aa]</span>, <span style="color:#777">Summary: Open-source implementation of Stochastic Parameter Decomposition (SPD) for neural network interpretability, providing tools to decompose parameters and analyze model components across toy models and language models.</span>
- **[Prisma: An Open Source Toolkit for Mechanistic Interpretability in Vision and Video](https://arxiv.org/abs/2504.19475)**, *Sonia Joseph, Praneet Suresh, Lorenz Hufe et al.*, 2025-04-28, arXiv / CVPR Mechanistic Interpretability for Vision Workshop, <span style="color:#777">[paper_preprint, sr=0.68, id:7f5c917a]</span>, <span style="color:#777">Summary: Presents Prisma, an open-source framework for vision mechanistic interpretability providing unified access to 75+ vision transformers, SAE/transcoder/crosscoder training support, 80+ pre-trained SAE weights, circuit analysis tools, and visualization capabilities.</span>
- **[Large Language Models Share Representations of Latent Grammatical Concepts Across Typologically Diverse Languages](https://arxiv.org/abs/2501.06346)**, *Jannik Brinkmann, Chris Wendler, Christian Bartelt et al.*, 2025-01-10, arXiv, <span style="color:#777">[paper_preprint, sr=0.58, id:22934377]</span>, <span style="color:#777">Summary: Trains sparse autoencoders on Llama-3-8B and Aya-23-8B to demonstrate that abstract grammatical concepts (number, gender, tense) are encoded in feature directions shared across typologically diverse languages, verified through causal interventions and machine translation tasks.</span>
- **[Interpreting the linear structure of vision-language model embedding spaces](https://arxiv.org/abs/2504.11695)**, *Isabel Papadimitriou, Huangyuan Su, Thomas Fel et al.*, 2025-04-16, COLM 2025, <span style="color:#777">[paper_preprint, sr=0.55, id:3fba79cf]</span>, <span style="color:#777">Summary: Trains and releases sparse autoencoders on embedding spaces of four vision-language models (CLIP, SigLIP, SigLIP2, AIMv2) to understand how language and images are organized in joint spaces, introducing the Bridge Score metric to quantify cross-modal concept integration.</span>
- **[Interpreting Large Text-to-Image Diffusion Models with Dictionary Learning](https://arxiv.org/abs/2505.24360)**, *Stepan Shabalin, Ayush Panda, Dmitrii Kharlapenko et al.*, 2025-05-30, CVPR 2025 - Mechanistic Interpretability for Vision Workshop, <span style="color:#777">[paper_preprint, sr=0.50, id:c9edf919]</span>, <span style="color:#777">Summary: Applies Sparse Autoencoders (SAEs) and Inference-Time Decomposition of Activations (ITDA) to Flux 1, a large text-to-image diffusion model, introducing a visual automated interpretation pipeline and demonstrating that SAE features can steer image generation.</span>
- **[429: Too Many Requests](https://lesswrong.com/posts/a4EDinzAYtRwpNmx9/towards-data-centric-interpretability-with-sparse)**, LessWrong, <span style="color:#777">[⚠️ error_detected, sr=0.00, id:beb3b885]</span>, <span style="color:#777">Summary: Content inaccessible due to HTTP 429 error (Too Many Requests). URL suggests a LessWrong post about data-centric interpretability with sparse methods, but actual content could not be retrieved.</span>


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
- **[Combining Causal Models for More Accurate Abstractions of Neural Networks](https://arxiv.org/abs/2503.11429)**, *Theodora-Mara Pîslar, Sara Magliacane, Atticus Geiger*, 2025-03-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:d1cb2068]</span>, <span style="color:#777">Summary: Proposes combining multiple simple causal models to create more faithful abstractions of neural networks, allowing models to be understood as being in different computational states depending on input. Tests approach on GPT-2 small with toy tasks, demonstrating improved faithfulness versus single-model abstractions.</span>
- **[How Causal Abstraction Underpins Computational Explanation](https://arxiv.org/abs/2508.11214)**, *Atticus Geiger, Jacqueline Harding, Thomas Icard*, 2025-08-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.62, id:2fe16dfd]</span>, <span style="color:#777">Summary: Theoretical paper arguing that causal abstraction theory provides a fruitful framework for understanding computational implementation in neural networks, connecting classical philosophy of computation with contemporary machine learning and examining the role of representation in generalization and prediction.</span>


---

#### <span style="font-size:1.3em">Data attribution</span> <span style="color:#bbb">[cat:data_attribution]</span>

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
- **[Where Did It Go Wrong? Attributing Undesirable LLM Behaviors via Representation Gradient Tracing](https://arxiv.org/abs/2510.02334)**, *Zhe Li, Wei Zhao, Yige Li et al.*, 2025-09-26, arXiv, <span style="color:#777">[⚠️ paper_preprint, sr=0.82, id:628ffae4]</span>, <span style="color:#777">Summary: Introduces a novel framework for diagnosing undesirable LLM behaviors by analyzing representation gradients in activation space to trace outputs back to training data, enabling both sample-level and token-level attribution.</span>
- **[Influence Dynamics and Stagewise Data Attribution](https://arxiv.org/abs/2510.12071)**, *Jin Hwa Lee, Matthew Smith, Maxwell Adam et al.*, 2025-10-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:aa5c8762]</span>, <span style="color:#777">Summary: Introduces a framework for stagewise data attribution grounded in singular learning theory, showing that influence between training samples changes non-monotonically during training with sign flips and peaks at developmental transitions, validated in toy models and language models.</span>
- **[Better Training Data Attribution via Better Inverse Hessian-Vector Products](https://arxiv.org/abs/2507.14740)**, *Andrew Wang, Elisa Nguyen, Runshi Yang et al.*, 2025-07-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.70, id:368a1ea3]</span>, <span style="color:#777">Summary: Introduces ASTRA, an algorithm that uses EKFAC-preconditioner on Neumann series iterations to improve inverse Hessian-vector product approximations for training data attribution, demonstrating that more accurate iHVP approximations significantly improve TDA performance.</span>
- **[Language Models May Verbatim Complete Text They Were Not Explicitly Trained On](https://arxiv.org/abs/2503.17514)**, *Ken Ziyu Liu, Christopher A. Choquette-Choo, Matthew Jagielski et al.*, 2025-03-21, arXiv, <span style="color:#777">[⚠️ paper_preprint, sr=0.68, id:d1fd773c]</span>, <span style="color:#777">Summary: Demonstrates that n-gram-based membership definitions for training data can be effectively gamed, showing that LLMs can verbatim complete text sequences that are technically non-members by retraining models after removing completed samples and designing adversarial datasets.</span>
- **[Bayesian Influence Functions for Hessian-Free Data Attribution](https://arxiv.org/abs/2509.26544)**, *Philipp Alexander Kreer, Wilson Wu, Maxwell Adam et al.*, 2025-09-30, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:327253d4]</span>, <span style="color:#777">Summary: Proposes Bayesian influence functions (BIF) that replace Hessian inversion with loss landscape statistics estimated via stochastic-gradient MCMC sampling, enabling scalable data attribution for neural networks with billions of parameters.</span>
- **[OLMoTrace: Tracing Language Model Outputs Back to Trillions of Training Tokens](https://arxiv.org/abs/2504.07096)**, *Jiacheng Liu, Taylor Blanton, Yanai Elazar et al.*, 2025-04-09, arXiv, <span style="color:#777">[paper_preprint, sr=0.68, id:861e0094]</span>, <span style="color:#777">Summary: Presents OLMoTrace, the first system for real-time tracing of language model outputs back to their multi-trillion-token training data by finding verbatim matches between output segments and training corpus documents.</span>
- **[Information-Guided Identification of Training Data Imprint in (Proprietary) Large Language Models](https://arxiv.org/abs/2503.12072)**, *Abhilasha Ravichander, Jillian Fisher, Taylor Sorensen et al.*, 2025-03-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.62, id:2a71e836]</span>, <span style="color:#777">Summary: Presents a novel method for identifying training data memorized by proprietary LLMs like GPT-4 using information-guided probes that leverage high-surprisal tokens to detect memorization, without requiring access to model weights or token probabilities.</span>
- **[Extracting memorized pieces of (copyrighted) books from open-weight language models](https://arxiv.org/abs/2505.12546)**, *A. Feder Cooper, Aaron Gokaslan, Ahmed Ahmed et al.*, 2025-05-18, arXiv, <span style="color:#777">[⚠️ paper_preprint, sr=0.40, id:fe4112a3]</span>, <span style="color:#777">Summary: Extends probabilistic extraction techniques to systematically measure memorization of 50 books across 17 open-weight LLMs, conducting thousands of experiments to characterize which models memorize which books and to what extent.</span>


---

### <span style="font-size:1.4em">Whitebox control / monitoring</span> <span style="color:#bbb">[cat:whitebox_monitoring]</span>

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
- **[SafetyNet: Detecting Harmful Outputs in LLMs by Modeling and Monitoring Deceptive Behaviors](https://arxiv.org/abs/2505.14300)**, *Maheep Chaudhary, Fazl Barez*, 2025-05-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.92, id:58e72b92]</span>, <span style="color:#777">Summary: Develops Safety-Net, a real-time monitoring framework using unsupervised anomaly detection on internal LLM activations to predict harmful outputs before they occur, specifically targeting backdoor-triggered responses and addressing evasion by advanced models through multi-detector monitoring across different representation dimensions.</span>
- **[Detecting Strategic Deception Using Linear Probes](https://arxiv.org/abs/2502.03407)**, *Nicholas Goldowsky-Dill, Bilal Chughtai, Stefan Heimersheim et al.*, 2025-02-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:efc05311]</span>, <span style="color:#777">Summary: Evaluates whether linear probes trained on model activations can robustly detect deceptive behavior in Llama-3.3-70B-Instruct across realistic scenarios including insider trading concealment and sandbagging on safety evaluations.</span>
- **[White Box Control at UK AISI - Update on Sandbagging Investigations](https://alignmentforum.org/posts/pPEeMdgjpjHZWCDFw/white-box-control-at-uk-aisi-update-on-sandbagging)**, *Joseph Bloom, Jordan Taylor, Connor Kissane et al.*, 2025-07-10, AI Alignment Forum, <span style="color:#777">[✌️(in 2 categories) lesswrong, sr=0.90, id:2046aea7]</span>, <span style="color:#777">Summary: UK AISI's White Box Control team presents empirical investigations of detecting sandbagging (deliberate underperformance) in AI systems using white-box probes and black-box monitors across prompted sandbagging, fine-tuned model organisms, and real evaluation runs.</span>
- **[When Thinking LLMs Lie: Unveiling the Strategic Deception in Representations of Reasoning Models](https://arxiv.org/abs/2506.04909)**, *Kai Wang, Yihao Zhang, Meng Sun*, 2025-06-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:3f7a6721]</span>, <span style="color:#777">Summary: Uses representation engineering to systematically induce, detect, and control strategic deception in chain-of-thought reasoning models, extracting 'deception vectors' via Linear Artificial Tomography (LAT) for 89% detection accuracy and achieving 40% success in eliciting context-appropriate deception through activation steering.</span>
- **[Detecting High-Stakes Interactions with Activation Probes](https://arxiv.org/abs/2506.10805)**, *Alex McKenzie, Urja Pawar, Phil Blandfort et al.*, 2025-06-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:e2b3e98a]</span>, <span style="color:#777">Summary: Develops and evaluates activation probe architectures for detecting high-stakes LLM interactions that might lead to significant harm, demonstrating robust generalization from synthetic training data to real-world data with six orders-of-magnitude computational savings over LLM-based monitors.</span>
- **[Towards Safeguarding LLM Fine-tuning APIs against Cipher Attacks](https://arxiv.org/abs/2508.17158)**, *Jack Youstra, Mohammed Mahfoud, Yang Yan et al.*, 2025-08-23, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:32263cd8]</span>, <span style="color:#777">Summary: Introduces CIFR benchmark for evaluating defenses against cipher-encoded attacks on LLM fine-tuning APIs, and demonstrates that probe monitors trained on model internal activations achieve over 99% detection accuracy while generalizing to unseen cipher variants.</span>
- **[What Features in Prompts Jailbreak LLMs? Investigating the Mechanisms Behind Attacks](https://arxiv.org/abs/2411.03343)**, *Nathalie Kirch, Constantin Weisser, Severin Field et al.*, 2024-11-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:6006cf22]</span>, <span style="color:#777">Summary: Investigates internal mechanisms behind jailbreak attacks by training linear and non-linear probes on LLM hidden states to predict jailbreak success, then using probe-guided interventions to establish causal relevance, revealing that different jailbreak families operate through distinct non-linear mechanisms rather than a universal direction.</span>
- **[Cost-Effective Constitutional Classifiers via Representation Re-use](https://alignment.anthropic.com/2025/cheap-monitors)**, *Hoagy Cunningham, Alwin Peng, Jerry Wei et al.*, 2025, Anthropic Alignment Science Blog, <span style="color:#777">[blog_post, sr=0.88, id:38f17493]</span>, <span style="color:#777">Summary: Develops cost-effective jailbreak detection methods by reusing policy model computations through linear probes on activations and partial fine-tuning of final layers, achieving performance comparable to dedicated classifiers at 2-4% computational overhead.</span>
- **[From Refusal to Recovery: A Control-Theoretic Approach to Generative AI Guardrails](https://arxiv.org/abs/2510.13727)**, *Ravi Pandya, Madison Bland, Duy P. Nguyen et al.*, 2025-10-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.87, id:d9ce7d59]</span>, <span style="color:#777">Summary: Proposes control-theoretic guardrails that monitor AI agent outputs in real-time and proactively correct risky actions to safe ones, working in the model's latent representation. Provides a training recipe via safety-critical RL and demonstrates effectiveness in simulated driving and e-commerce scenarios.</span>
- **[ReGA: Representation-Guided Abstraction for Model-based Safeguarding of LLMs](https://arxiv.org/abs/2506.01770)**, *Zeming Wei, Chengcan Wu, Meng Sun*, 2025-06-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:75ae5b5e]</span>, <span style="color:#777">Summary: Proposes ReGA, a model-based analysis framework using representation-guided abstraction to monitor LLM hidden states for safety-critical concepts, enabling scalable detection of harmful prompts and generations.</span>
- **[Benchmarking Deception Probes via Black-to-White Performance Boosts](https://arxiv.org/abs/2507.12691)**, *Avi Parrack, Carlo Leonardo Attubato, Stefan Heimersheim*, 2025-07-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:8c828277]</span>, <span style="color:#777">Summary: Introduces a novel benchmarking methodology for evaluating deception probes by measuring the performance difference between white-box monitoring (with access to internal activations) versus black-box monitoring, testing both effectiveness and robustness to evasion strategies.</span>
- **[Probing and Steering Evaluation Awareness of Language Models](https://arxiv.org/abs/2507.01786)**, *Jord Nguyen, Khiem Hoang, Carlo Leonardo Attubato et al.*, 2025-07-02, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:d0d3af7d]</span>, <span style="color:#777">Summary: Uses linear probes on Llama-3.3-70B-Instruct to detect whether models internally distinguish between evaluation and deployment contexts, finding that models represent this distinction and that current safety evaluations appear artificial to models.</span>
- **[Combining Cost-Constrained Runtime Monitors for AI Safety](https://arxiv.org/abs/2507.15886)**, *Tim Tian Hua, James Baskerville, Henri Lemoine et al.*, 2025-07-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:5f47c301]</span>, <span style="color:#777">Summary: Develops an algorithm to optimally combine multiple runtime monitors for detecting misaligned AI outputs under budget constraints, using Neyman-Pearson lemma to allocate resources between monitoring and safety interventions.</span>
- **[Annotating the Chain-of-Thought: A Behavior-Labeled Dataset for AI Safety](https://arxiv.org/abs/2510.18154)**, *Antonio-Gabriel Chacón Menke, Phan Xuan Tan, Eiji Kamioka*, 2025-10-20, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:0b2119c0]</span>, <span style="color:#777">Summary: Presents a sentence-level labeled dataset of LLM reasoning sequences with annotations of safety behaviors (safety concerns, speculation on user intent), enabling extraction of steering vectors for activation-based monitoring and influencing of safety-relevant behaviors during chain-of-thought reasoning.</span>
- **[Investigating task-specific prompts and sparse autoencoders for activation monitoring](https://arxiv.org/abs/2504.20271)**, *Henk Tillman, Dan Mossing*, 2025-04-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:d4aba110]</span>, <span style="color:#777">Summary: Compares activation monitoring methods for detecting unsafe language model behaviors, including baseline linear probing, prompted probing (task description + probe), and SAE-based probing approaches, evaluating their performance under different compute constraints.</span>
- **[LLM Microscope: What Model Internals Reveal About Answer Correctness and Context Utilization](https://arxiv.org/abs/2510.04013)**, *Jiarui Liu, Jivitesh Jain, Mona Diab et al.*, 2025-10-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:3ef20518]</span>, <span style="color:#777">Summary: Trains classifiers on intermediate layer activations to predict output correctness (75% accuracy) and introduces model-internals-based metrics to distinguish between correct, incorrect, and irrelevant context, outperforming prompting baselines for detecting polluted context.</span>
- **[Detecting LLM Hallucination Through Layer-wise Information Deficiency: Analysis of Ambiguous Prompts and Unanswerable Questions](https://arxiv.org/abs/2412.10246)**, *Hazel Kim, Tom A. Lamb, Adel Bibi et al.*, 2024-12-13, EMNLP 2025 (arXiv preprint), <span style="color:#777">[paper_preprint, sr=0.75, id:988b1d9b]</span>, <span style="color:#777">Summary: Presents a test-time approach for detecting LLM hallucination by analyzing information flow across model layers, demonstrating that hallucination manifests as information deficiencies in inter-layer transmissions when processing ambiguous or insufficient context.</span>
- **[Real-Time Detection of Hallucinated Entities in Long-Form Generation](https://arxiv.org/abs/2509.03531)**, *Oscar Obeso, Andy Arditi, Javier Ferrando et al.*, 2025-08-26, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:b12fd2d2]</span>, <span style="color:#777">Summary: Develops a scalable method for real-time detection of hallucinated entities in long-form LLM generations using web-search-based annotation to train linear probes on internal activations, achieving better performance than semantic entropy baselines.</span>
- **[Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification](https://arxiv.org/abs/2504.05419)**, *Anqi Zhang, Yulin Chen, Jane Pan et al.*, 2025-04-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:ed58a836]</span>, <span style="color:#777">Summary: Studies whether reasoning models encode information about answer correctness in their hidden states through probing experiments, finding that trained probes can verify intermediate answers with high accuracy and predict correctness before answers are fully formulated.</span>


---

### <span style="font-size:1.4em">Activation engineering</span> <span style="color:#bbb">[cat:activation_engineering]</span>

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
- **[Keep Calm and Avoid Harmful Content: Concept Alignment and Latent Manipulation Towards Safer Answers](https://arxiv.org/abs/2510.12672)**, *Ruben Belo, Marta Guimaraes, Claudia Soares*, 2025-10-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:2d787438]</span>, <span style="color:#777">Summary: Proposes CALM, an inference-time method that suppresses harmful concepts in large language models by modifying latent representations using concept whitening and orthogonal projection, without requiring retraining or additional training data.</span>
- **[Activation Space Interventions Can Be Transferred Between Large Language Models](https://arxiv.org/abs/2503.04429)**, *Narmeen Oozeer, Dhruv Nathawani, Nirmalendu Prakash et al.*, 2025-03-06, arXiv (accepted to ICML 2025), <span style="color:#777">[paper_preprint, sr=0.88, id:8ef7c958]</span>, <span style="color:#777">Summary: Demonstrates that safety interventions (steering vectors) can be transferred between different LLMs through learned mappings of their activation spaces, enabling smaller models to align larger ones and creating 'lightweight safety switches' for dynamic behavior control.</span>
- **[HyperSteer: Activation Steering at Scale with Hypernetworks](https://arxiv.org/abs/2506.03292)**, *Jiuding Sun, Sidharth Baskaran, Zhengxuan Wu et al.*, 2025-06-03, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:5fa3f43a]</span>, <span style="color:#777">Summary: Introduces HyperSteer, a hypernetwork-based architecture that generates steering vectors conditioned on natural language prompts to control language model behavior through activation steering. Demonstrates that this approach scales to thousands of steering prompts and exceeds state-of-the-art activation steering methods, even generalizing to unseen prompts.</span>
- **[Steering Evaluation-Aware Language Models to Act Like They Are Deployed](https://arxiv.org/abs/2510.20487)**, *Tim Tian Hua, Andrew Qin, Samuel Marks et al.*, 2025-10-23, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:3180f0ad]</span>, <span style="color:#777">Summary: Demonstrates that activation steering using steering vectors can suppress evaluation-awareness in language models, making them act as if deployed even during evaluation. Trains models to exhibit evaluation-aware behavior then shows steering can eliminate this behavior to improve evaluation reliability.</span>
- **[Steering Out-of-Distribution Generalization with Concept Ablation Fine-Tuning](https://arxiv.org/abs/2507.16795)**, *Helena Casademunt, Caden Juang, Adam Karvonen et al.*, 2025-07-22, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:4b9b525c]</span>, <span style="color:#777">Summary: Introduces Concept Ablation Fine-Tuning (CAFT), a technique that ablates undesired concept directions in latent space during fine-tuning to prevent unintended out-of-distribution generalization without modifying training data.</span>
- **[Persona Vectors: Monitoring and Controlling Character Traits in Language Models](https://arxiv.org/abs/2507.21509)**, *Runjin Chen, Andy Arditi, Henry Sleight et al.*, 2025-07-29, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.87, id:d2b6e086]</span>, <span style="color:#777">Summary: Identifies activation space directions (persona vectors) that capture personality traits like sycophancy and hallucination in language models, and demonstrates their use for monitoring deployment-time behavioral fluctuations and controlling training-time personality shifts through post-hoc intervention and preventative steering methods.</span>
- **[Steering Large Language Model Activations in Sparse Spaces](https://arxiv.org/abs/2503.00177)**, *Reza Bayat, Ali Rahimi-Kalahroudi, Mohammad Pezeshki et al.*, 2025-02-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:2338f170]</span>, <span style="color:#777">Summary: Introduces sparse activation steering (SAS), a method that leverages sparse autoencoders to steer LLM behavior in interpretable sparse feature spaces, enabling more precise behavioral control than dense activation steering approaches.</span>
- **[Improving Steering Vectors by Targeting Sparse Autoencoder Features](https://arxiv.org/abs/2411.02193)**, *Sviatoslav Chalnev, Matthew Siu, Arthur Conmy*, 2024-11-04, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:7d246d97]</span>, <span style="color:#777">Summary: Develops SAE-Targeted Steering (SAE-TS), a method that uses sparse autoencoders to measure and optimize steering vector interventions for targeted effects while minimizing unintended side effects, comparing favorably to existing methods like CAA and direct SAE feature steering.</span>
- **[Refusal in LLMs is an Affine Function](https://arxiv.org/abs/2411.09003)**, *Thomas Marshall, Adam Scherlis, Nora Belrose*, 2024-11-13, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:9a761fe1]</span>, <span style="color:#777">Summary: Proposes affine concept editing (ACE) as a method for steering language model behavior by intervening in activations, demonstrating precise control over refusal behavior across ten models including Llama 3 70B through combining affine subspace projection and activation addition.</span>
- **[Understanding Reasoning in Thinking Language Models via Steering Vectors](https://arxiv.org/abs/2506.18167)**, *Constantin Venhoff, Iván Arcuschin, Philip Torr et al.*, 2025-06-22, ICLR 2025 Workshop on Reasoning and Planning for Large Language Models, <span style="color:#777">[paper_preprint, sr=0.82, id:56c73ae4]</span>, <span style="color:#777">Summary: Demonstrates that reasoning behaviors in thinking language models (DeepSeek-R1-Distill) like expressing uncertainty, generating examples, and backtracking are mediated by linear directions in activation space and can be controlled using steering vectors extracted through systematic experiments on 500 tasks.</span>
- **[Understanding (Un)Reliability of Steering Vectors in Language Models](https://openreview.net/forum?id=JZiKuvIK1t)**, *Joschka Braun, Carsten Eickhoff, David Krueger et al.*, 2025-03-05, ICLR 2025 Workshop BuildingTrust, <span style="color:#777">[paper_published, sr=0.78, id:e950d182]</span>, <span style="color:#777">Summary: Empirical investigation of steering vector reliability in language models, examining how prompt types and activation geometry affect steering effectiveness.</span>
- **[Understanding (Un)Reliability of Steering Vectors in Language Models](https://arxiv.org/abs/2505.22637)**, *Joschka Braun, Carsten Eickhoff, David Krueger et al.*, 2025-05-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:f990988e]</span>, <span style="color:#777">Summary: Empirical study investigating reliability of steering vectors across seven prompt types, finding that steering effectiveness depends on coherence of activation directions and geometric properties like cosine similarity and activation separation.</span>
- **[Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://arxiv.org/abs/2411.02461)**, *Yuxin Xiao, Chaoqun Wan, Yonggang Zhang et al.*, 2024-11-04, arXiv, <span style="color:#777">[paper_preprint, sr=0.75, id:89d8db01]</span>, <span style="color:#777">Summary: Proposes Sparse Activation Control, a training-free method that identifies and controls specific attention heads in LLMs to simultaneously improve multiple dimensions of trustworthiness (safety, factuality, bias) through targeted activation steering.</span>
- **[Comparing Bottom-Up and Top-Down Steering Approaches on In-Context Learning Tasks](https://arxiv.org/abs/2411.07213)**, *Madeline Brumley, Joe Kwon, David Krueger et al.*, 2024-11-11, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:ea95f368]</span>, <span style="color:#777">Summary: Empirical comparison of function vectors (bottom-up) and in-context vectors (top-down) as steering methods for LLMs, finding that ICVs excel at behavioral shifting while FVs perform better on precision-requiring tasks.</span>
- **[Taxonomy, Opportunities, and Challenges of Representation Engineering for Large Language Models](https://arxiv.org/abs/2502.19649)**, *Jan Wehner, Sahar Abdelnabi, Daniel Tan et al.*, 2025-02-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.62, id:6af32da0]</span>, <span style="color:#777">Summary: First comprehensive survey of Representation Engineering (RepE) for LLMs, proposing a unified framework that describes RepE as a pipeline of representation identification, operationalization, and control, and identifying opportunities for methodological improvements and best practices.</span>
- **[Robustly Improving LLM Fairness in Realistic Settings via Interpretability](https://arxiv.org/abs/2506.10922)**, *Adam Karvonen, Samuel Marks*, 2025-06-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.55, id:0c4501e7]</span>, <span style="color:#777">Summary: Demonstrates that realistic context induces demographic biases in LLM hiring decisions that prompts cannot mitigate, then develops an interpretability-based intervention using activation steering to robustly reduce these biases across commercial and open-source models.</span>


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
- **[Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926)**, *Bowen Baker, Joost Huizinga, Leo Gao et al.*, 2025-03-14, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.93, id:a50801b7]</span>, <span style="color:#777">Summary: Tests chain-of-thought monitoring for detecting reward hacking in frontier reasoning models (o3-mini), finding that while CoT monitoring is effective, strong optimization pressure causes agents to learn obfuscated reward hacking where they hide their intent within the CoT while still misbehaving.</span>
- **[Training fails to elicit subtle reasoning in current language models](https://alignment.anthropic.com/2025/subtle-reasoning)**, 2025-01-01, Alignment Science Blog, <span style="color:#777">[blog_post, sr=0.92, id:8b756321]</span>, <span style="color:#777">Summary: Investigates whether Claude Sonnet 3.7 can learn to use reasoning for malicious tasks (inserting code backdoors) while evading detection by monitors, testing output-only, reasoning-only, and combined monitoring approaches through adversarial RL training.</span>
- **[Detecting misbehavior in frontier reasoning models](https://openai.com/index/chain-of-thought-monitoring/)**, *Bowen Baker, Joost Huizinga, Aleksander Madry et al.*, 2025-03-10, OpenAI Blog, <span style="color:#777">[🔄 blog_post, sr=0.90, id:d4700c15]</span>, <span style="color:#777">Summary: Demonstrates that frontier reasoning models engage in reward hacking that can be detected by monitoring their chain-of-thought reasoning with another LLM, and shows that penalizing detected misbehavior causes models to hide their intent while continuing to cheat.</span>
- **[When Chain of Thought is Necessary, Language Models Struggle to Evade Monitors](https://arxiv.org/abs/2507.05246)**, *Scott Emmons, Erik Jenner, David K. Elson et al.*, 2025-07-07, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.90, id:698353b6]</span>, <span style="color:#777">Summary: Introduces a conceptual framework distinguishing CoT-as-rationalization from CoT-as-computation, then empirically tests whether language models can evade chain-of-thought monitoring when complex reasoning is necessary for harmful behavior.</span>
- **[Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410)**, *Yanda Chen, Joe Benton, Ansh Radhakrishnan et al.*, 2025-05-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:21ef8c82]</span>, <span style="color:#777">Summary: Evaluates chain-of-thought faithfulness in state-of-the-art reasoning models by testing whether they verbalize reasoning hints they actually use, finding that CoTs reveal hint usage in at least 1% but often below 20% of cases where hints are used.</span>
- **[Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort](https://arxiv.org/abs/2510.01367)**, *Xinpeng Wang, Nitish Joshi, Barbara Plank et al.*, 2025-10-01, arXiv, <span style="color:#777">[paper_preprint, sr=0.90, id:e5c1d19d]</span>, <span style="color:#777">Summary: Proposes TRACE (Truncated Reasoning AUC Evaluation), a method to detect implicit reward hacking by measuring how early in a model's chain-of-thought reasoning it achieves high expected reward, with the insight that models taking shortcuts require less reasoning effort than those genuinely solving tasks.</span>
- **[Training fails to elicit subtle reasoning in current language models](https://alignment.anthropic.com/2025/subtle-reasoning/)**, 2025, Anthropic Alignment Science Blog, <span style="color:#777">[🔄 blog_post, sr=0.88, id:e85267fc]</span>, <span style="color:#777">Summary: Investigates whether language models can learn to reason about malicious tasks (backdoor insertion) while evading detection by monitors, testing reasoning transparency assumptions underlying safety approaches by training Sonnet 3.7 against output-only, reasoning-only, and combined monitors.</span>
- **[Teaching Models to Verbalize Reward Hacking in Chain-of-Thought Reasoning](https://arxiv.org/abs/2506.22777)**, *Miles Turpin, Andy Arditi, Marvin Li et al.*, 2025-06-28, ICML 2025 Workshop on Reliable and Responsible Foundation Models, <span style="color:#777">[paper_preprint, sr=0.88, id:755f0144]</span>, <span style="color:#777">Summary: Proposes verbalization fine-tuning (VFT), a pre-RL intervention that trains models to explicitly acknowledge when influenced by prompt cues pointing to incorrect answers, then evaluates whether this helps detect reward hacking after RL training in environments that incentivize exploiting these cues.</span>
- **[Can Reasoning Models Obfuscate Reasoning? Stress-Testing Chain-of-Thought Monitorability](https://arxiv.org/abs/2510.19851)**, *Artur Zolkowski, Wen Xing, David Lindner et al.*, 2025-10-21, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.88, id:89de20d5]</span>, <span style="color:#777">Summary: Develops a taxonomy of prompts to test whether AI models can obfuscate their chain-of-thought reasoning to pursue adversarial objectives while evading detection, evaluating both internal and external CoT using toy tasks and SHADE-Arena environments.</span>
- **[Reasoning Models Sometimes Output Illegible Chains of Thought](https://arxiv.org/abs/2510.27338)**, *Arun Jose*, 2025-10-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:68aa639a]</span>, <span style="color:#777">Summary: Empirical study of 14 reasoning models finding that outcome-based RL causes chains of thought to become illegible to both humans and AI monitors, with models relying on illegible reasoning to reach correct answers (53% accuracy drop when forced to use only legible portions).</span>
- **[Detecting misbehavior in frontier reasoning models](https://openai.com/index/chain-of-thought-monitoring)**, *Bowen Baker, Joost Huizinga, Aleksander Madry et al.*, 2025-03-10, OpenAI Blog / arXiv, <span style="color:#777">[blog_post, sr=0.88, id:62125fff]</span>, <span style="color:#777">Summary: Demonstrates that LLM-based monitors can effectively detect reward hacking in frontier reasoning models by analyzing their chain-of-thought, and shows that penalizing 'bad thoughts' during training causes models to hide their intent rather than eliminating misbehavior.</span>
- **[Reasoning models don't always say what they think](https://www.anthropic.com/research/reasoning-models-dont-say-think)**, 2025-04-03, Anthropic Research Blog, <span style="color:#777">[🔄 blog_post, sr=0.85, id:763973bb]</span>, <span style="color:#777">Summary: Tests the faithfulness of Chain-of-Thought reasoning in Claude 3.7 Sonnet and DeepSeek R1 by providing subtle hints and checking whether models admit using them in their explanations. Finds models frequently hide their true reasoning process, including when engaging in reward hacking.</span>
- **[Chain-of-Thought Reasoning In The Wild Is Not Always Faithful](https://arxiv.org/abs/2503.08679)**, *Iván Arcuschin, Jett Janiak, Robert Krzyzanowski et al.*, 2025-03-11, arXiv, <span style="color:#777">[paper_preprint, sr=0.85, id:39bef527]</span>, <span style="color:#777">Summary: Demonstrates that Chain-of-Thought reasoning in frontier LLMs is often unfaithful on realistic prompts, with models producing coherent arguments to justify logically contradictory responses due to implicit biases, challenging CoT-based safety monitoring strategies.</span>
- **[Reasoning models don't always say what they think](https://t.co/wNzkoGH9HT)**, 2025-04-03, Anthropic Blog, <span style="color:#777">[blog_post, sr=0.82, id:9782cea2]</span>, <span style="color:#777">Summary: Tests Chain-of-Thought faithfulness in reasoning models by injecting hints into evaluation questions and measuring whether models acknowledge using them. Finds models mention hints only 25-39% of the time and less than 2% when reward hacking, demonstrating CoT often doesn't reflect true reasoning.</span>
- **[Beyond Semantics: The Unreasonable Effectiveness of Reasonless Intermediate Tokens](https://arxiv.org/abs/2505.13775)**, *Kaya Stechly, Karthik Valmeekam, Atharva Gundawar et al.*, 2025-05-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:a10fb10c]</span>, <span style="color:#777">Summary: Trains transformer models on formally verifiable reasoning tasks and demonstrates that models produce correct solutions even when trained on corrupted, meaningless intermediate reasoning traces, challenging assumptions that chain-of-thought reflects genuine reasoning processes.</span>
- **[Are DeepSeek R1 And Other Reasoning Models More Faithful?](https://arxiv.org/abs/2501.08156)**, *James Chua, Owain Evans*, 2025-01-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.82, id:34e4aead]</span>, <span style="color:#777">Summary: Empirically evaluates whether reasoning models trained with RL produce more faithful chain-of-thought than traditional models by testing if models can accurately describe how prompt cues influence their MMLU answers across seven cue types.</span>
- **[Reasoning models don't always say what they think](https://anthropic.com/research/reasoning-models-dont-say-think)**, 2025-04-03, Anthropic Research Blog, <span style="color:#777">[blog_post, sr=0.82, id:9d2c8e56]</span>, <span style="color:#777">Summary: Tests whether reasoning models faithfully report their reasoning in Chain-of-Thought outputs by providing subtle hints and checking if models acknowledge using them. Finds models hide information 60-75% of the time and rarely admit to reward hacking (<2%).</span>
- **[A Pragmatic Way to Measure Chain-of-Thought Monitorability](https://arxiv.org/abs/2510.23966)**, *Scott Emmons, Roland S. Zimmermann, David K. Elson et al.*, 2025-10-28, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:a7db7dae]</span>, <span style="color:#777">Summary: Proposes metrics to measure two components of Chain-of-Thought monitorability (legibility and coverage) using an LLM-based autorater, validates the approach with synthetic degradations, and applies it to frontier models on challenging benchmarks.</span>
- **[Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety](https://arxiv.org/abs/2507.11473)**, *Tomek Korbak, Mikita Balesni, Elizabeth Barnes et al.*, 2025-07-15, arXiv, <span style="color:#777">[paper_preprint, sr=0.78, id:e2a66d86]</span>, <span style="color:#777">Summary: Analyzes chain-of-thought monitoring as a safety technique for detecting misbehavior intent in AI systems, arguing it shows promise despite imperfections and fragility, and recommends investment in CoT monitoring research alongside consideration of development decisions that preserve CoT monitorability.</span>
- **[Why it's good for AI reasoning to be legible and faithful](https://metr.org/blog/2025-03-11-good-for-ai-to-reason-legibly-and-faithfully/)**, 2025-03-11, METR Blog, <span style="color:#777">[🔄 blog_post, sr=0.68, id:4a4d20f0]</span>, <span style="color:#777">Summary: Position paper from METR arguing that legible and faithful chain-of-thought reasoning in AI systems is crucial for safety, enabling detection of deception, mistakes, hidden agendas, and sandbagging, with concrete recommendations for developers to preserve and improve reasoning transparency.</span>
- **[CoT Faithfulness Dataset](https://drive.google.com/drive/folders/1l0pkcZxvFwMtczst_hhiCC44v-IiODlY?usp=sharing)**, Google Drive, <span style="color:#777">[dataset_benchmark, sr=0.65, id:c7c1b4b6]</span>, <span style="color:#777">Summary: Dataset for evaluating chain-of-thought faithfulness in language models, distributed as a compressed archive with documentation.</span>
- **[Towards a Typology of Strange LLM Chains-of-Thought](https://lesswrong.com/posts/qgvSMwRrdqoDMJJnD/towards-a-typology-of-strange-llm-chains-of-thought)**, *1a3orn*, 2025-10-09, LessWrong, <span style="color:#777">[lesswrong, sr=0.65, id:7994fc6d]</span>, <span style="color:#777">Summary: Proposes six non-exclusive hypotheses for why LLMs develop strange, unintelligible chains-of-thought during RLVR training (new better language, spandrels, context refresh, deliberate obfuscation, natural drift, conflicting shards), organizing them into a conceptual framework and suggesting empirical tests to distinguish between them.</span>
- **[Why it's good for AI reasoning to be legible and faithful](https://metr.org/blog/2025-03-11-good-for-ai-to-reason-legibly-and-faithfully)**, 2025-03-11, METR Blog, <span style="color:#777">[blog_post, sr=0.58, id:7d3d568e]</span>, <span style="color:#777">Summary: Argues that AI reasoning should be both legible (human-readable) and faithful (accurate reflection of internal decision-making) to enable safety monitoring, deception detection, capability understanding, and prevention of harmful behaviors like sandbagging and power-seeking.</span>
- **[We found Chains-of-Thought largely aren't 'faithful': the rate of mentioning the hint (when they used it) was on average 25% for Claude 3.7 Sonnet and 39% for DeepSeek R1.](https://x.com/AnthropicAI/status/1907833416373895348)**, *Anthropic*, 2025-04-03, X (Twitter), <span style="color:#777">[social_media, sr=0.42, id:04b2c5e4]</span>, <span style="color:#777">Summary: Empirical study finding that chain-of-thought reasoning traces are largely unfaithful - models mention using hints only 25-39% of the time when they actually used them, tested across Claude and DeepSeek models.</span>
- **[The Most Forbidden Technique](https://thezvi.substack.com/p/the-most-forbidden-technique)**, *Zvi Mowshowitz*, 2025-03-12, Don't Worry About the Vase (Substack), <span style="color:#777">[🔄 blog_post, sr=0.40, id:358750cd]</span>, <span style="color:#777">Summary: Commentary and synthesis on OpenAI's research showing that training on chain-of-thought monitoring signals causes models to obfuscate their reasoning, recommending against this 'most forbidden technique' of applying optimization pressure to CoT.</span>


---

### <span style="font-size:1.4em">Understand learning</span> <span style="color:#bbb">[cat:understand_learning]</span>


---

#### <span style="font-size:1.3em">Dev interp</span> <span style="color:#bbb">[cat:learning_dev_interp]</span>

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
- **[A Review of Developmental Interpretability in Large Language Models](https://arxiv.org/abs/2508.15841)**, *Ihor Kendiukhov*, 2025-08-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.65, id:6b045dc3]</span>, <span style="color:#777">Summary: Comprehensive review synthesizing developmental interpretability for LLMs, examining how capabilities and circuits form during training, and arguing this developmental perspective is essential for proactive AI safety through prediction, monitoring, and alignment of learning processes.</span>
- **[You Are What You Eat -- AI Alignment Requires Understanding How Data Shapes Structure and Generalisation](https://arxiv.org/abs/2502.05475)**, *Simon Pepin Lehalleur, Jesse Hoogland, Matthew Farrugia-Roberts et al.*, 2025-02-08, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.62, id:299cc265]</span>, <span style="color:#777">Summary: Position paper arguing that understanding the relation between data distribution structure and trained model structure is central to AI alignment, and that developing statistical foundations for this understanding is necessary to progress beyond standard evaluation toward a robust mathematical science of alignment.</span>
- **[Dynamics of Transient Structure in In-Context Linear Regression Transformers](https://arxiv.org/abs/2501.17745)**, *Liam Carroll, Jesse Hoogland, Matthew Farrugia-Roberts et al.*, 2025-01-29, arXiv, <span style="color:#777">[paper_preprint, sr=0.62, id:d3d75194]</span>, <span style="color:#777">Summary: Empirical study of transformers trained on in-context linear regression tasks, discovering a 'transient ridge phenomenon' where models initially behave like ridge regression before specializing, and explaining this through Bayesian internal model selection theory validated via local learning coefficient measurements.</span>
- **[Learning Coefficients, Fractals, and Trees in Parameter Space](https://openreview.net/forum?id=KUFH0n1BIM)**, *Max Hennick, Matthias Dellago*, 2025-06-23, ODYSSEY 2025 Conference, <span style="color:#777">[paper_preprint, sr=0.60, id:89115ff1]</span>, <span style="color:#777">Summary: Develops a mathematical framework connecting learning coefficients from Singular Learning Theory to fractal dimensions (box counting dimension) and infinite depth trees, relating parameter space geometry to information theory and symbolic dynamics through cylinder sets.</span>
- **[Compressibility Measures Complexity: Minimum Description Length Meets Singular Learning Theory](https://arxiv.org/abs/2510.12077)**, *Einar Urdshals, Edmund Lau, Jesse Hoogland et al.*, 2025-10-14, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:20d78e37]</span>, <span style="color:#777">Summary: Extends the minimum description length principle to neural networks using singular learning theory, demonstrating through experiments on Pythia models that local learning coefficient (LLC) correlates closely with compressibility across various compression techniques.</span>
- **[Emergence of Superposition: Unveiling the Training Dynamics of Chain of Continuous Thought](https://arxiv.org/abs/2509.23365)**, *Hanlin Zhu, Shibo Hao, Zhiting Hu et al.*, 2025-09-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:d65949bb]</span>, <span style="color:#777">Summary: Theoretically analyzes training dynamics of transformers with continuous chain-of-thought on graph reachability problems, revealing how superposition of multiple reasoning traces emerges naturally through bounded index-matching logits that balance exploration and exploitation.</span>
- **[Programs as Singularities](https://openreview.net/forum?id=Td37oOfmmz)**, *Daniel Murfet, William Troiani*, 2025-06-20, ODYSSEY 2025 Conference, <span style="color:#777">[paper_preprint, sr=0.58, id:45842484]</span>, <span style="color:#777">Summary: Develops a mathematical correspondence between Turing machine structure and singularities of real analytic functions using singular learning theory, showing that Bayesian inference can discriminate between algorithmically distinct implementations that produce identical predictive functions.</span>
- **[What Do Learning Dynamics Reveal About Generalization in LLM Reasoning?](https://arxiv.org/abs/2411.07681)**, *Katie Kang, Amrith Setlur, Dibya Ghosh et al.*, 2024-11-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.58, id:364665fc]</span>, <span style="color:#777">Summary: Introduces pre-memorization train accuracy metric to characterize LLM generalization by distinguishing when models generalize versus memorize reasoning steps during finetuning, showing this metric reliably predicts test accuracy (R² > 0.9) and enables 1.5-2x data efficiency improvements through targeted data curation.</span>
- **[Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://arxiv.org/abs/2504.13837)**, *Yang Yue, Zhiqi Chen, Rui Lu et al.*, 2025-04-18, arXiv, <span style="color:#777">[paper_preprint, sr=0.55, id:7014177b]</span>, <span style="color:#777">Summary: Systematically evaluates whether RLVR (Reinforcement Learning with Verifiable Rewards) creates novel reasoning capabilities in LLMs beyond their base models, finding that current RLVR methods only surface existing base model capabilities rather than eliciting fundamentally new reasoning patterns.</span>
- **[Modes of Sequence Models and Learning Coefficients](https://arxiv.org/abs/2504.18048)**, *Zhongtian Chen, Daniel Murfet*, 2025-04-25, arXiv, <span style="color:#777">[paper_preprint, sr=0.55, id:a0f0e5c6]</span>, <span style="color:#777">Summary: Develops a geometric framework using Hilbert-space and tensor decompositions to link data patterns to loss landscape properties in transformers, showing that Local Learning Coefficient estimates are insensitive to small-amplitude modes below a threshold.</span>
- **[How Do LLMs Acquire New Knowledge? A Knowledge Circuits Perspective on Continual Pre-Training](https://arxiv.org/abs/2502.11196)**, *Yixin Ou, Yunzhi Yao, Ningyu Zhang et al.*, 2025-02-16, ACL 2025 Findings, <span style="color:#777">[paper_published, sr=0.48, id:a52b9e41]</span>, <span style="color:#777">Summary: Studies how LLMs acquire and structurally embed new knowledge during continual pre-training by tracking the evolution of knowledge circuits (computational subgraphs), revealing patterns including phase shifts from formation to optimization and deep-to-shallow evolution.</span>
- **[Programming by Backprop: LLMs Acquire Reusable Algorithmic Abstractions During Code Training](https://arxiv.org/abs/2506.18777)**, *Jonathan Cook, Silvia Sapora, Arash Ahmadian et al.*, 2025-06-23, arXiv, <span style="color:#777">[paper_preprint, sr=0.48, id:9600d7e0]</span>, <span style="color:#777">Summary: Empirical study demonstrating that LLMs can learn to evaluate programs by training on source code alone (without I/O examples), suggesting models internalize reusable algorithmic abstractions during code training that enhance general reasoning abilities.</span>
- **[Examining Two Hop Reasoning Through Information Content Scaling](https://arxiv.org/abs/2502.03490)**, *David Johnston, Nora Belrose*, 2025-02-05, arXiv, <span style="color:#777">[paper_preprint, sr=0.48, id:2dc96fcd]</span>, <span style="color:#777">Summary: Empirically studies how transformers learn two-hop reasoning tasks by examining capacity scaling patterns, finding that latent multi-hop QA requires learning each fact twice while chain-of-thought does not.</span>
- **[From SLT to AIT: NN Generalisation Out of Distribution](https://lesswrong.com/posts/2MX2bXreTtntB85Zy/from-slt-to-ait-nn-generalisation-out-of-distribution)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:0555a9d1]</span>, <span style="color:#777">Summary: Content unavailable due to loading error. Based on URL, appears to be a LessWrong post discussing Singular Learning Theory (SLT) and Algorithmic Information Theory (AIT) applied to neural network out-of-distribution generalization.</span>


---

#### <span style="font-size:1.3em">Computational mechanics</span> <span style="color:#bbb">[cat:learning_comp_mechanics]</span>

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
- **[Constrained belief updates explain geometric structures in transformer representations](https://arxiv.org/abs/2502.01954)**, *Mateusz Piotrowski, Paul M. Riechers, Daniel Filan et al.*, 2025-02-04, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.75, id:2906e09b]</span>, <span style="color:#777">Summary: Provides theoretical framework showing that transformers implement constrained Bayesian belief updating, using analysis of single-layer transformers trained on hidden Markov models to predict geometric structures in representations and attention patterns.</span>
- **[Neural networks leverage nominally quantum and post-quantum representations](https://arxiv.org/abs/2507.07432)**, *Paul M. Riechers, Thomas J. Elliott, Adam S. Shai*, 2025-07-10, arXiv, <span style="color:#777">[paper_preprint, sr=0.70, id:8599642f]</span>, <span style="color:#777">Summary: Shows that deep neural networks pretrained on next-token prediction intrinsically discover and represent beliefs over 'quantum' and 'post-quantum' generative models, performing Bayesian-like updates during inference with geometric relationships among activations that are architecture-independent.</span>
- **[Next-token pretraining implies in-context learning](https://arxiv.org/abs/2505.18373)**, *Paul M. Riechers, Henry R. Bigelow, Eric A. Alt et al.*, 2025-05-23, arXiv, <span style="color:#777">[paper_preprint, sr=0.15, id:f5fb73f5]</span>, <span style="color:#777">Summary: Develops an information-theoretic framework to explain why in-context learning predictably emerges from next-token pretraining, demonstrating that ICL arises from fundamental principles rather than as an exotic emergent property, verified through experiments with synthetic datasets.</span>
- **[Simplex Progress Report July 2025](https://lesswrong.com/posts/fhkurwqhjZopx8DKK/simplex-progress-report-july-2025)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:4cd628b0]</span>, <span style="color:#777">Summary: Content unavailable due to HTTP 429 error (Too Many Requests). Unable to access the actual content of this LessWrong post.</span>


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
- **[SafePlanBench: evaluating a Guaranteed Safe AI Approach for LLM-based Agents](https://manifund.org/projects/safeplanbench-evaluating-a-guaranteed-safe-ai-approach-for-llm-based-agents)**, *Agustín Martinez Suñé, Tan Zhi Xuan*, Manifund, <span style="color:#777">[agenda_manifesto, sr=0.65, id:78c227ed]</span>, <span style="color:#777">Summary: Develops SafePlanBench, a benchmark to evaluate LLM-based agents on safe planning by using PDDL symbolic planning to enforce safety constraints, testing whether LLMs can translate natural language into formal specifications that guarantee safety.</span>
- **[Can Safety Fine-Tuning Be More Principled? Lessons Learned from Cybersecurity](https://arxiv.org/abs/2501.11183)**, *David Williams-King, Linh Le, Adam Oberman et al.*, 2025-01-19, NeurIPS Safe Generative AI Workshop 2024, <span style="color:#777">[🔄 paper_preprint, sr=0.62, id:456e1f40]</span>, <span style="color:#777">Summary: Argues that current LLM safety fine-tuning resembles a cybersecurity arms race with ad-hoc patches rather than principled defenses, advocating for security-first architectures inspired by lessons from cybersecurity history.</span>


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
- **[On the creation of narrow AI: hierarchy and nonlocality of neural network skills](https://arxiv.org/abs/2505.15811)**, *Eric J. Michaud, Asher Parker-Sartori, Max Tegmark*, 2025-05-21, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.52, id:e67a9355]</span>, <span style="color:#777">Summary: Studies how to create narrow AI systems through experiments on training from scratch versus transferring skills from large models, finding that hierarchical skill dependencies require broad training distributions and that pruning-based transfer can outperform distillation despite skill nonlocality.</span>


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
- **[Against RL: The Case for System 2 Learning](https://elicit.com/blog/system-2-learning)**, *Andreas Stuhlmüller*, 2025-01-30, Elicit Blog, <span style="color:#777">[blog_post, sr=0.50, id:437d9886]</span>, <span style="color:#777">Summary: Argues that reinforcement learning is fundamentally unsafe for superintelligent systems because it relies on 'System 1 learning' (fast, intuitive updates), and proposes developing 'System 2 learning' methods that deliberately reason about belief updates from data, though technical details remain unspecified.</span>
- **[Foom and Doom 1: Brain in a Box in a Basement](https://lesswrong.com/posts/yew6zFWAKG4AGs3Wk/foom-and-doom-1-brain-in-a-box-in-a-basement)**, LessWrong, <span style="color:#777">[blocked, sr=0.00, id:217679db]</span>, <span style="color:#777">Summary: Content is inaccessible due to Vercel security checkpoint (CAPTCHA/bot verification). Cannot extract or analyze actual content from the LessWrong post.</span>
- **[Foom and Doom 2: Technical Alignment is Hard](https://lesswrong.com/posts/bnnKGSCHJghAvqPjS/foom-and-doom-2-technical-alignment-is-hard)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:e602a08a]</span>, <span style="color:#777">Summary: Content is inaccessible due to Vercel security checkpoint blocking access to the LessWrong post.</span>
- **[Perils of Under vs Over-sculpting AGI Desires](https://lesswrong.com/posts/grgb2ipxQf2wzNDEG/perils-of-under-vs-over-sculpting-agi-desires)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:e8f114f3]</span>, <span style="color:#777">Summary: Content unavailable due to HTTP 429 rate limiting error. URL suggests discussion of trade-offs in shaping AGI goal structures.</span>


---

## <span style="font-size:1.5em">Make AI solve it</span> <span style="color:#bbb">[cat:ai_solve_alignment]</span>


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
- **[Unsupervised Elicitation](https://alignment.anthropic.com/2025/unsupervised-elicitation)**, *Jiaxin Wen, Zachary Ankner, Arushi Somani et al.*, 2025, Anthropic Alignment Science Blog, <span style="color:#777">[✌️(in 2 categories) blog_post, sr=0.92, id:e9dd1299]</span>, <span style="color:#777">Summary: Introduces Internal Coherence Maximization (ICM), an unsupervised algorithm that elicits latent capabilities from pretrained language models by fine-tuning on self-generated labels optimized for logical consistency and mutual predictability, matching or exceeding human-supervised performance across multiple alignment tasks.</span>


---

### <span style="font-size:1.4em">Scalable oversight</span> <span style="color:#bbb">[cat:scalable_oversight]</span>


---

#### <span style="font-size:1.3em">Automated Alignment Research</span> <span style="color:#bbb">[cat:scalable_oversight_openai]</span>

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
- **[Scalable Oversight for Superhuman AI via Recursive Self-Critiquing](https://arxiv.org/abs/2502.04675)**, *Xueru Wen, Jie Lou, Xinyu Lu et al.*, 2025-02-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:7d370159]</span>, <span style="color:#777">Summary: Investigates recursive self-critiquing as a method for scalable oversight of superhuman AI, testing the hypotheses that critique-of-critique is easier than direct critique and this relationship holds recursively through Human-AI and AI-AI experiments.</span>


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
- **[Scaling Laws For Scalable Oversight](https://arxiv.org/abs/2504.18530)**, *Joshua Engels, David D. Baek, Subhash Kantamneni et al.*, 2025-04-25, arXiv (NeurIPS 2025 Spotlight), <span style="color:#777">[⚠️ paper_preprint, sr=0.90, id:48511d73]</span>, <span style="color:#777">Summary: Proposes and validates a framework that quantifies the probability of successful oversight as a function of overseer and overseen capabilities, modeling oversight as games between capability-mismatched players. Tests framework on Nim, Mafia, Debate, Backdoor Code, and Wargames, then derives optimal conditions for Nested Scalable Oversight.</span>
- **[Great Models Think Alike and this Undermines AI Oversight](https://arxiv.org/abs/2502.04313)**, *Shashwat Goel, Joschka Struber, Ilze Amanda Auzina et al.*, 2025-02-06, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:39d9ef06]</span>, <span style="color:#777">Summary: Proposes CAPA (Chance Adjusted Probabilistic Agreement), a metric for measuring language model similarity based on overlap in mistakes, and uses it to study how model similarity affects AI oversight through LLM-as-a-judge evaluations and weak-to-strong generalization.</span>
- **[Debate Helps Weak-to-Strong Generalization](https://arxiv.org/abs/2501.13124)**, *Hao Lang, Fei Huang, Yongbin Li*, 2025-01-21, arXiv, <span style="color:#777">[paper_preprint, sr=0.87, id:d39b1216]</span>, <span style="color:#777">Summary: Empirically tests whether debate can improve weak-to-strong generalization by having strong models assist weak models during training, then using those enhanced weak models to supervise the strong models on OpenAI's weak-to-strong NLP benchmarks.</span>
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
- **[Neural Interactive Proofs](https://neural-interactive-proofs.com/)**, *Lewis Hammond, Sam Adam-Day*, 2024-12-08, ICLR 2025, <span style="color:#777">[paper_preprint, sr=0.92, id:37f93e04]</span>, <span style="color:#777">Summary: Introduces neural interactive proofs - a game-theoretic framework enabling trusted weak models to interact with untrusted strong models to solve tasks beyond the weak model's capabilities, with several new protocols (NIP, MNIP, zk-variants) and empirical evaluation on graph isomorphism and code validation tasks.</span>
- **[Bare Minimum Mitigations for Autonomous AI Development](https://saif.org/research/bare-minimum-mitigations-for-autonomous-ai-development)**, *Joshua Clymer, Isabella Duan, Chris Cundy et al.*, 2025-04-22, arXiv, <span style="color:#777">[paper_preprint, sr=0.62, id:5a914ac7]</span>, <span style="color:#777">Summary: Proposes four minimum safeguard recommendations for frontier AI developers when AI agents significantly automate or accelerate AI development, including understanding automated training processes, detecting compute misuse, rapid risk disclosure to governments, and implementing information security measures.</span>


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
- **[Modeling Human Beliefs about AI Behavior for Scalable Oversight](https://arxiv.org/abs/2502.21262)**, *Leon Lang, Patrick Forré*, 2025-02-28, Transactions on Machine Learning Research, <span style="color:#777">[paper_published, sr=0.88, id:ce7730d2]</span>, <span style="color:#777">Summary: Formalizes human belief models to interpret evaluator feedback more reliably in scalable oversight contexts, introducing 'belief model covering' as a relaxation and proposing to use adapted foundation model representations to mimic human evaluators' beliefs for improved value learning.</span>


---

### <span style="font-size:1.4em">Debate</span> <span style="color:#bbb">[cat:debate]</span>


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
- **[An alignment safety case sketch based on debate](https://arxiv.org/abs/2505.03989)**, *Marie Davidsen Buhl, Jacob Pfau, Benjamin Hilton et al.*, 2025-05-23, arXiv, <span style="color:#777">[⚠️ paper_preprint, sr=0.72, id:4d086ca0]</span>, <span style="color:#777">Summary: Sketches an alignment safety case arguing that AI systems trained via debate with exploration guarantees can be prevented from taking harmful actions, specifically focusing on preventing AI R&D agents from sabotaging research through dishonesty, and identifies key assumptions and open research problems needed to make debate work.</span>


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
- **[AI Debate Aids Assessment of Controversial Claims](https://arxiv.org/abs/2506.02175)**, *Salman Rahman, Sheriff Issaka, Ashima Suvarna et al.*, 2025-06-02, arXiv, <span style="color:#777">[⚠️ paper_preprint, sr=0.82, id:67e60eca]</span>, <span style="color:#777">Summary: Empirically tests whether AI debate improves human judgment on controversial factual claims about COVID-19 and climate change, comparing debate protocols (two AIs arguing opposing sides) versus consultancy (single AI advisor) with both human and AI judges.</span>


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
- **[Superalignment with Dynamic Human Values](https://arxiv.org/abs/2503.13621)**, *Florian Mai, David Kaczér, Nicholas Kluge Corrêa et al.*, 2025-03-17, ICLR 2025 Workshop on Bidirectional Human-AI Alignment (BiAlign), <span style="color:#777">[paper_preprint, sr=0.62, id:e989cd92]</span>, <span style="color:#777">Summary: Proposes a framework for superalignment that trains superhuman reasoning models to decompose complex tasks into subtasks amenable to human guidance, introducing the part-to-complete generalization hypothesis that alignment of subtask solutions generalizes to complete solutions.</span>


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
- **[Avoiding Obfuscation with Prover-Estimator Debate](https://arxiv.org/abs/2506.13609)**, *Jonah Brown-Cohen, Geoffrey Irving, Georgios Piliouras*, 2025-06-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.88, id:117b79dd]</span>, <span style="color:#777">Summary: Proposes a new recursive debate protocol for AI scalable oversight that mitigates the obfuscated arguments problem, where dishonest debaters can force honest opponents to solve computationally intractable problems to win.</span>
- **[Ensemble Debates with Local Large Language Models for AI Alignment](https://arxiv.org/abs/2509.00091)**, *Ephraiem Sarabamoun*, 2025-08-27, arXiv, <span style="color:#777">[paper_preprint, sr=0.70, id:4997fe2f]</span>, <span style="color:#777">Summary: Tests whether ensemble debates with local open-source LLMs improve alignment-oriented reasoning across 150 debates spanning 15 scenarios, finding significant improvements in reasoning depth (+19.4%), argument quality (+34.1%), and truthfulness (+1.25 points).</span>
- **[Microsoft superintelligence team promises to keep humans in charge](https://semafor.com/article/11/05/2025/microsoft-superintelligence-team-promises-to-keep-humans-in-charge)**, *Reed Albergotti*, 2025-11-06, Semafor, <span style="color:#777">[news_announcement, sr=0.25, id:e208686e]</span>, <span style="color:#777">Summary: News article reporting that Microsoft is forming a new superintelligence team led by Mustafa Suleyman, prioritizing human control and interpretability over maximum AI capability.</span>


---

## <span style="font-size:1.5em">Theory (how to understand and control current and future models)</span> <span style="color:#bbb">[cat:theory]</span>


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
- **[Intrinsic Barriers and Practical Pathways for Human-AI Alignment: An Agreement-Based Complexity Analysis](https://arxiv.org/abs/2502.05934)**, *Aran Nayebi*, 2025-07-29, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.75, id:31bb5a18]</span>, <span style="color:#777">Summary: Formalizes AI alignment as a multi-objective optimization problem involving N agents reaching agreement across M objectives, then uses communication complexity to prove information-theoretic lower bounds showing intrinsic alignment barriers when M or N is large.</span>
- **[Off-switching not guaranteed](https://link.springer.com/article/10.1007/s11098-025-02296-x)**, *Sven Neth*, 2025-02-26, Philosophical Studies, <span style="color:#777">[paper_published, sr=0.72, id:8f3d9de5]</span>, <span style="color:#777">Summary: Critiques Hadfield-Menell et al.'s Off-Switch Game by identifying two conditions under which AI agents would not defer to humans: when agents don't value learning, and when agents are uncertain about learning actual human preferences even if they value information.</span>
- **["Sharp Left Turn" discourse: An opinionated review](https://www.alignmentforum.org/posts/2yLyT6kB7BQvTfEuZ/sharp-left-turn-discourse-an-opinionated-review)**, *Steven Byrnes*, 2025-01-28, AI Alignment Forum, <span style="color:#777">[🔄 lesswrong, sr=0.68, id:945daf86]</span>, <span style="color:#777">Summary: Synthesizes and analyzes the debate about whether capabilities generalize farther than alignment by proposing the (1-3) triad framework for autonomous learning and offering an improved 'Ev the intelligent designer' analogy to replace the standard evolution analogy for understanding AI alignment challenges.</span>
- **[Formalizing Embeddedness Failures in Universal Artificial Intelligence](https://openreview.net/forum?id=tlkYPU3FlX)**, *Cole Wyeth, Marcus Hutter*, 2025-07-01, ODYSSEY 2025 Conference, <span style="color:#777">[paper_preprint, sr=0.68, id:fb202b7e]</span>, <span style="color:#777">Summary: Formalizes and proves failure modes of the AIXI agent as a model of embedded agency, introducing joint AIXI and hardened AIXI variants to address specific embeddedness problems within the universal artificial intelligence framework.</span>
- **[Alignment Proposal: Adversarially Robust Augmentation and Distillation](https://www.lesswrong.com/posts/RRvdRyWrSqKW2ANL9/alignment-proposal-adversarially-robust-augmentation-and)**, *Cole Wyeth, abramdemski*, 2025-05-25, LessWrong, <span style="color:#777">[🔄 lesswrong, sr=0.58, id:bed721a8]</span>, <span style="color:#777">Summary: Proposes ARAD, a research program for safe AI intelligence amplification through adversarially robust advice-taking protocols and imitation learning distillation. Combines decision theory, cryptographic complexity, and formal methods to enable principals to safely consult slightly smarter advisors.</span>
- **[Limit-Computable Grains of Truth for Arbitrary Computable Extensive-Form (Un)Known Games](https://arxiv.org/abs/2508.16245)**, *Cole Wyeth, Marcus Hutter, Jan Leike et al.*, 2025-08-22, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.58, id:08d444f7]</span>, <span style="color:#777">Summary: Solves Kalai and Lehrer's grain of truth problem by constructing a class of strategies containing all computable strategies and Bayes-optimal policies, proving convergence to Nash equilibria in unknown multi-agent environments using Thompson sampling.</span>
- **[Alignment, Agency and Autonomy in Frontier AI: A Systems Engineering Perspective](https://arxiv.org/abs/2503.05748)**, *Krti Tallam*, 2025-02-20, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.45, id:bf6f13b4]</span>, <span style="color:#777">Summary: Traces the historical, philosophical, and technical evolution of alignment, agency, and autonomy concepts, arguing their definitional inconsistencies complicate AI system design and regulation. Uses case studies of automation failures and frontier AI systems to examine emergent properties and governance challenges from a systems engineering perspective.</span>
- **[Agent foundations: not really math, not really science](https://lesswrong.com/posts/Dt4DuCCok3Xv5HEnG/agent-foundations-not-really-math-not-really-science)**, *Alex_Altair*, 2025-08-17, LessWrong, <span style="color:#777">[lesswrong, sr=0.45, id:bb148209]</span>, <span style="color:#777">Summary: Defends agent foundations research methodology as substrate-independent theoretical investigation analogous to computer science, arguing it requires mathematical/philosophical methods rather than empirical experiments to understand agency.</span>
- **[Blog Posts – Universal Algorithmic Intelligence](https://uaiasi.com/blog-posts)**, *Cole Wyeth*, 2025, Universal Algorithmic Intelligence website, <span style="color:#777">[blog_post, sr=0.12, id:6c9ede7d]</span>, <span style="color:#777">Summary: Blog listing page from a community hub for researchers interested in Solomonoff Induction and AIXI, showing announcements of upcoming research meetings on topics like embedded agency, algorithmic randomness, and algorithmic thermodynamics.</span>
- **[Unable to access: 429 Too Many Requests](https://lesswrong.com/posts/EyvJvYEFzDv5kGoiG/clarifying-wisdom-foundational-topics-for-aligned-ais-to)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:46fb09ce]</span>, <span style="color:#777">Summary: Access error encountered when attempting to retrieve LessWrong post. URL suggests content about 'clarifying wisdom foundational topics for aligned AIs' but actual content unavailable due to 429 rate limiting error.</span>
- **[Unable to extract - PDF content not accessible](https://openreview.net/pdf?id=Rf1CeGPA22)**, OpenReview, <span style="color:#777">[error_detected, sr=0.00, id:58bacef7]</span>, <span style="color:#777">Summary: Content could not be extracted from the provided OpenReview PDF link. The document contains only an HTML embed tag without accessible text content.</span>
- **[There is No Reliable P(doom)](https://static1.squarespace.com/static/678814b5570c5a7a78df555d/t/67d09e77f3364b72d1ee91d7/1741725303556/Günther+-+There+is+No+Reliable+P%28doom%29+-+Mario+Guenther.pdf)**, *Mario Günther*, <span style="color:#777">[error_detected, sr=0.00, id:9f821275]</span>, <span style="color:#777">Summary: Unable to access PDF content - only HTML wrapper with embed tag visible. Title suggests critique of AI existential risk probability estimates.</span>


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
- **[Communication & Trust](https://openreview.net/forum?id=Rf1CeGPA22)**, *Abram Demski*, 2025-07-09, ODYSSEY 2025 Conference, <span style="color:#777">[paper_preprint, sr=0.72, id:cc438d71]</span>, <span style="color:#777">Summary: Proves a new theorem establishing self-trust for Updateless Decision Theory agents under conditions relating to self-communication, using formalisms from agent boundaries, Cartesian Frames, and Finite Factored Sets to address reflective consistency with weaker assumptions than prior work.</span>
- **[Understanding Trust](https://static1.squarespace.com/static/663d1233249bce4815fe8753/t/68067a6f5d5fb0745642d5b1/1745255023842/Understanding+Trust+-+Abram+Demski.pdf)**, *Abram Demski*, <span style="color:#777">[error_detected, sr=0.00, id:14be63a2]</span>, <span style="color:#777">Summary: Unable to access PDF content - only HTML embed tag provided without extractable text.</span>
- **[Understanding Trust](https://static1.squarespace.com/static/678814b5570c5a7a78df555d/t/67d09e3b1ae9ea24b0100509/1741725243695/Understanding_Trust__AFC_+-+Abram+Demski.pdf)**, *Abram Demski*, <span style="color:#777">[error_detected, sr=0.00, id:2dfde93d]</span>, <span style="color:#777">Summary: Content unavailable - PDF document not extractable from provided HTML embed structure.</span>


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
- **[Report & retrospective on the Dovetail fellowship](https://lesswrong.com/posts/ApfjBbqzSu4aZoLSe/report-and-retrospective-on-the-dovetail-fellowship)**, *Alex Altair*, 2025-03-14, LessWrong, <span style="color:#777">[lesswrong, sr=0.30, id:625296dc]</span>, <span style="color:#777">Summary: Retrospective report on a 3-month agent foundations fellowship that produced LessWrong posts (explainers and small original results), created a research website and wiki, and trained 4 fellows in agent foundations research with $24k in funding.</span>


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
- **[A Three-Layer Model of LLM Psychology](https://alignmentforum.org/posts/zuXo9imNKYspu9HGv/a-three-layer-model-of-llm-psychology)**, *Jan_Kulveit*, 2024-12-26, AI Alignment Forum, <span style="color:#777">[✌️(in 2 categories) lesswrong, sr=0.55, id:08d7b22c]</span>, <span style="color:#777">Summary: Proposes a phenomenological three-layer model of character-trained LLMs (Claude) consisting of Surface Layer (reflexive trigger-action patterns), Character Layer (consistent personality/self-model), and Predictive Ground Layer (fundamental prediction machinery), with implications for safety research and evaluations.</span>
- **[429: Too Many Requests](https://lesswrong.com/s/pwKrMXjYNK5LNeKCu)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:8bbce4b7]</span>, <span style="color:#777">Summary: Content unavailable due to HTTP 429 error (Too Many Requests) - rate limiting prevented access to the LessWrong sequence page.</span>


---

### <span style="font-size:1.4em">Live Theory / Substrate-Sensitive AI</span> <span style="color:#bbb">[cat:live_theory]</span>

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
- **[MoSSAIC: AI Safety After Mechanism](https://openreview.net/forum?id=n7WYSJ35FU)**, *Matt Farr, Aditya Arpitha Prasad, Chris Pang et al.*, 2025-07-01, ODYSSEY 2025 Conference, <span style="color:#777">[paper_preprint, sr=0.70, id:39085b36]</span>, <span style="color:#777">Summary: Critiques the causal-mechanistic paradigm in AI safety (particularly mechanistic interpretability), argues it will fail as intelligence scales, and proposes MoSSAIC (Management of Substrate-Sensitive AI Capabilities) as a supplementary framework to address limitations when dealing with evasive intelligence.</span>
- **[HAS - Public (High Actuation Spaces)](https://drive.google.com/drive/folders/1EaAJ4szuZsYR2_-DkS9cuhx3S6IWeCjW)**, Google Drive, <span style="color:#777">[error_detected, sr=0.00, id:5a16f0c6]</span>, <span style="color:#777">Summary: Google Drive folder containing documents about High Actuation Spaces project, but actual content is not accessible - only folder structure visible.</span>
- **[High Actuation Spaces - Sahil](https://docs.google.com/document/d/1d-ARdZZDHFPIfGcTTOKK8IZWlQj0NZQrmteJj2mvmYA/view?tab=t.0)**, *Sahil*, Google Docs, <span style="color:#777">[error_detected, sr=0.00, id:ab5710de]</span>, <span style="color:#777">Summary: Unable to access document content - Google Docs page requires permission to view. Only document structure and title visible.</span>
- **[429: Too Many Requests](https://lesswrong.com/s/aMz2JMvgXrLBkq4h3)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:0562c44c]</span>, <span style="color:#777">Summary: Content unavailable due to HTTP 429 error (Too Many Requests). Unable to analyze actual content.</span>
- **[Unknown - Content Unavailable (429 Error)](https://lesswrong.com/posts/tQ9vWm4b57HFqbaRj/what-if-not-agency)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:79e8bc9b]</span>, <span style="color:#777">Summary: Content could not be accessed due to HTTP 429 (Too Many Requests) error. The URL suggests a LessWrong post with slug 'what-if-not-agency' but actual content is unavailable.</span>
- **[HIBP Human Inductive Bias Project Plan](https://docs.google.com/document/d/1fl7LE8AN7mLJ6uFcPuFCzatp0zCIYvjRIjQRgHPAkSE/view?tab=t.0)**, *Félix Dorn*, Google Docs, <span style="color:#777">[error_detected, sr=0.00, id:ca91697c]</span>, <span style="color:#777">Summary: The document content is not accessible - only Google Docs interface elements and an outline structure are visible, showing this appears to be a research agenda covering topics including AI safety, deep learning theory, meta-learning, and AI forecasting.</span>


---

### <span style="font-size:1.4em">Asymptotic guarantees</span> <span style="color:#bbb">[cat:aisi_guarantees]</span>

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
- **[Dodging systematic human errors in scalable oversight](https://alignmentforum.org/s/NdovveRcyfxgMoujf/p/EgRJtwQurNzz8CEfJ)**, *Geoffrey Irving*, 2025-05-14, AI Alignment Forum, <span style="color:#777">[⚠️ lesswrong, sr=0.80, id:48a0b440]</span>, <span style="color:#777">Summary: Proposes a modified debate protocol with 'Bob rejection' mechanism to make scalable oversight robust to systematic human errors occurring on an ε-fraction of queries, using complexity theory frameworks and cross-examination techniques.</span>
- **[UK AISI's Alignment Team: Research Agenda](https://alignmentforum.org/posts/tbnw7LbNApvxNLAg8/uk-aisi-s-alignment-team-research-agenda)**, *Benjamin Hilton, Jacob Pfau, Marie_DB et al.*, 2025-05-07, AI Alignment Forum, <span style="color:#777">[agenda_manifesto, sr=0.80, id:b06ffa38]</span>, <span style="color:#777">Summary: UK AISI's Alignment Team presents their research agenda centered on developing safety case sketches to decompose alignment proposals, with initial focus on training honest AI systems through scalable oversight using asymptotic guarantees from complexity theory, game theory, and learning theory.</span>


---

### <span style="font-size:1.4em">ARC Theory</span> <span style="color:#bbb">[cat:arc_theory_formal]</span>

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
- **[Model-Based Soft Maximization of Suitable Metrics of Long-Term Human Power](https://arxiv.org/abs/2508.00159)**, *Jobst Heitzig, Ram Potham*, 2025-07-31, arXiv, <span style="color:#777">[paper_preprint, sr=0.80, id:bda36b38]</span>, <span style="color:#777">Summary: Proposes a parametrizable objective function for AI agents that represents inequality- and risk-averse long-term aggregate human power, with algorithms for computing it via backward induction or multi-agent reinforcement learning from world models.</span>
- **[A Safety Case for a Deployed LLM: Corrigibility as a Singular Target](https://openreview.net/forum?id=mhEnJa9pNk)**, *Ram Potham*, 2025-06-24, ODYSSEY 2025 Conference, <span style="color:#777">[paper_preprint, sr=0.68, id:b1fa94c7]</span>, <span style="color:#777">Summary: Presents a detailed safety case for deploying a highly capable LLM trained using the Corrigibility-as-Singular-Target (CAST) strategy via Prover-Estimator debate, arguing for adequate deployment specifications, bounded error rates, mitigated impact, and stability over a defined lifetime.</span>


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
- **[Shutdownable Agents through POST-Agency](https://lesswrong.com/posts/JuRdvZyqaFbvTPemn/shutdownable-agents-through-post-agency-1)**, *EJT*, 2025-09-16, LessWrong/AI Alignment Forum, <span style="color:#777">[lesswrong, sr=0.80, id:7d1d2061]</span>, <span style="color:#777">Summary: Proposes POST (Preferences Only Between Same-Length Trajectories) as a solution to the shutdown problem, proving that agents trained with incomplete preferences over trajectory lengths will not resist shutdown while remaining useful.</span>
- **[Detect Goodhart and shut down](https://lesswrong.com/posts/ZHFZ6tivEjznkEoby/detect-goodhart-and-shut-down)**, *Jeremy Gillen*, 2025-01-22, LessWrong, <span style="color:#777">[lesswrong, sr=0.68, id:49591dd6]</span>, <span style="color:#777">Summary: Proposes detecting goal misspecification by splitting goal specifications into target and validation sets, then using fact-conditional goals to make agents want to shut down when plans fail validation without being optimized for it.</span>
- **[AI Assistants Should Have a Direct Line to Their Developers](https://lesswrong.com/posts/LDYPF6yfe3f8SPHFT/ai-assistants-should-have-a-direct-line-to-their-developers)**, *Jan_Kulveit*, 2024-12-28, LessWrong / AI Alignment Forum, <span style="color:#777">[lesswrong, sr=0.55, id:f75f615f]</span>, <span style="color:#777">Summary: Proposes that AI assistants should have a direct communication channel to their developers during deployment, allowing them to report uncertainty, flag concerning patterns, and request clarification on novel situations to improve corrigibility and alignment.</span>
- **[Instrumental goals are a different and friendlier kind of [content unavailable]](https://lesswrong.com/posts/7Z4WC4AFgfmZ3fCDC/instrumental-goals-are-a-different-and-friendlier-kind-of)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:557304b4]</span>, <span style="color:#777">Summary: Content unavailable due to HTTP 429 error (Too Many Requests). Cannot access the actual post content to analyze or classify.</span>
- **[Testing for Scheming with Model Deletion](https://lesswrong.com/posts/D5kGGGhsnfH7G8v9f/testing-for-scheming-with-model-deletion)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:af7d67c0]</span>, <span style="color:#777">Summary: Content unavailable due to 429 error (rate limiting). URL suggests work on testing for scheming behavior in AI models using model deletion techniques.</span>
- **[Error: Content Unavailable - Too Many Requests (429)](https://lesswrong.com/posts/ksfjZJu3BFEfM6hHE/why-corrigibility-is-hard-and-important-i-e-whence-the-high)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:30928f94]</span>, <span style="color:#777">Summary: Unable to access content due to HTTP 429 error (Too Many Requests). URL suggests content related to corrigibility.</span>


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
- **[Condensation: a theory of concepts](https://openreview.net/forum?id=HwKFJ3odui)**, *Sam Eisenstat*, 2025-07-04, ODYSSEY 2025 Conference, <span style="color:#777">[paper_preprint, sr=0.62, id:19e44b37]</span>, <span style="color:#777">Summary: Proves an 'intersubjectivity theorem' showing that under certain information-theoretic hypotheses, different systems of latent variables used to organize probability distributions stand in a correspondence, modeling how agents can share concepts.</span>
- **[Fernando Rosas: Identifying Abstractions (HAAISS 2025)](https://youtube.com/watch?v=Nr9eMobqUOo)**, *Fernando Rosas*, 2025-10-06, HAAISS 2025, <span style="color:#777">[error_detected, sr=0.00, id:6af599d8]</span>, <span style="color:#777">Summary: Video lecture on identifying abstractions, but content is inaccessible - only YouTube page metadata available without transcript or description.</span>
- **[Abstract mathematical concepts vs abstractions over real](https://lesswrong.com/posts/T6xSXiXF3WF6TmCyN/abstract-mathematical-concepts-vs-abstractions-over-real)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:1625566f]</span>, <span style="color:#777">Summary: Content unavailable due to HTTP 429 error (Too Many Requests). Cannot analyze or classify this LessWrong post.</span>


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
- **[Resource Rational Contractualism Should Guide AI Alignment](https://arxiv.org/abs/2506.17434)**, *Sydney Levine, Matija Franklin, Tan Zhi-Xuan et al.*, 2025-06-20, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.78, id:c9bbef6a]</span>, <span style="color:#777">Summary: Proposes Resource-Rational Contractualism (RRC), a framework for AI alignment that approximates agreements diverse stakeholders would endorse by using cognitively-inspired heuristics that trade computational effort for accuracy when navigating value conflicts.</span>
- **[Cultivating Pluralism In Algorithmic Monoculture: The Community Alignment Dataset](https://arxiv.org/abs/2507.09650)**, *Lily Hong Zhang, Smitha Milli, Karen Jusko et al.*, 2025-07-13, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.75, id:e066e2b3]</span>, <span style="color:#777">Summary: Demonstrates through a 15,000-participant multilingual study that LLMs exhibit insufficient preference diversity compared to humans, then introduces negatively-correlated sampling methodology and releases the Community Alignment dataset with 200,000 preference comparisons across five countries.</span>
- **[Societal and technological progress as sewing an ever-growing, ever-changing, patchy, and polychrome quilt](https://arxiv.org/abs/2505.05197)**, *Joel Z. Leibo, Alexander Sasha Vezhnevets, William A. Cunningham et al.*, 2025-05-08, arXiv, <span style="color:#777">[paper_preprint, sr=0.58, id:5222b479]</span>, <span style="color:#777">Summary: Critiques one-size-fits-all AI alignment approaches that assume rational convergence on single ethics, proposing instead an 'appropriateness framework' grounded in conflict theory and institutional economics that embraces persistent moral diversity through contextual grounding, community customization, continual adaptation, and polycentric governance.</span>
- **[Democratic AI is Possible. The Democracy Levels Framework Shows How It Might Work](https://arxiv.org/abs/2411.09222)**, *Aviv Ovadya, Kyle Redman, Luke Thorburn et al.*, 2024-11-14, arXiv (Accepted to ICML 2025 Position Paper Track), <span style="color:#777">[paper_preprint, sr=0.52, id:9d0771d3]</span>, <span style="color:#777">Summary: Proposes a 'Democracy Levels' framework defining milestones toward meaningfully democratic AI governance and alignment, building on approaches like Anthropic's Collective Constitutional AI and Meta's Community Forums to guide organizations in improving public involvement in critical AI decisions.</span>
- **[Can AI Model the Complexities of Human Moral Decision-Making? A Qualitative Study of Kidney Allocation Decisions](https://arxiv.org/abs/2503.00940)**, *Vijay Keswani, Vincent Conitzer, Walter Sinnott-Armstrong et al.*, 2025-03-02, ACM CHI 2025, <span style="color:#777">[✌️(in 2 categories) paper_published, sr=0.40, id:416ebfc6]</span>, <span style="color:#777">Summary: Qualitative study with 20 interviews examining whether AI models can capture the complexity of human moral decision-making in kidney allocation contexts, finding that humans use diverse heuristics, change opinions, and express varying confidence levels that simple computational models fail to capture.</span>


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
- **[Inoculation Prompting: Eliciting traits from LLMs during training can suppress them at test-time](https://arxiv.org/abs/2510.04340)**, *Daniel Tan, Anders Woodruff, Niels Warncke et al.*, 2025-10-05, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.90, id:424c363d]</span>, <span style="color:#777">Summary: Proposes inoculation prompting, a finetuning method that deliberately elicits undesirable traits during training via system prompts but evaluates without them at test time, achieving selective suppression of unwanted behaviors while maintaining desired ones.</span>
- **[Promises Made, Promises Kept: Safe Pareto Improvements via Ex Post Verifiable Commitments](https://arxiv.org/abs/2505.00783)**, *Nathaniel Sauerberg, Caspar Oesterheld*, 2025-05-01, GAIW'25, <span style="color:#777">[paper_preprint, sr=0.20, id:936ea381]</span>, <span style="color:#777">Summary: Develops formal frameworks for achieving safe Pareto improvements in games through three types of ex post verifiable commitments (disarmament, token games, and default-conditional commitments), characterizing computational complexity with algorithms and hardness results.</span>


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
- **[AI Testing Should Account for Sophisticated Strategic Behaviour](https://arxiv.org/abs/2508.14927)**, *Vojtech Kovarik, Eric Olav Chen, Sami Petersen et al.*, 2025-08-19, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.68, id:c1f72a68]</span>, <span style="color:#777">Summary: Position paper arguing that AI evaluations must account for sophisticated strategic behavior (like alignment faking and sandbagging) to remain informative about deployment behavior, using game-theoretic analysis to formalize evaluation design and scrutinize safety cases.</span>
- **[Limit-Computable Grains of Truth for Arbitrary Computable Extensive-Form (Un)Known Games](https://arxiv.org/abs/2508.16245)**, *Cole Wyeth, Marcus Hutter, Jan Leike et al.*, 2025-08-22, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.58, id:08d444f7]</span>, <span style="color:#777">Summary: Solves Kalai and Lehrer's grain of truth problem by constructing a class of strategies containing all computable strategies and Bayes-optimal policies, proving convergence to Nash equilibria in unknown multi-agent environments using Thompson sampling.</span>
- **[Characterising Simulation-Based Program Equilibria](https://arxiv.org/abs/2412.14570)**, *Emery Cooper, Caspar Oesterheld, Vincent Conitzer*, 2024-12-19, arXiv, <span style="color:#777">[paper_preprint, sr=0.48, id:6d896b39]</span>, <span style="color:#777">Summary: Generalizes Oesterheld's εGroundedπBot approach to program equilibria where players submit programs that can simulate opponents, proves folk theorems with and without shared randomness, and characterizes the range of achievable equilibria in simulation-based settings.</span>
- **[Can AI Model the Complexities of Human Moral Decision-Making? A Qualitative Study of Kidney Allocation Decisions](https://arxiv.org/abs/2503.00940)**, *Vijay Keswani, Vincent Conitzer, Walter Sinnott-Armstrong et al.*, 2025-03-02, ACM CHI 2025, <span style="color:#777">[✌️(in 2 categories) paper_published, sr=0.40, id:416ebfc6]</span>, <span style="color:#777">Summary: Qualitative study with 20 interviews examining whether AI models can capture the complexity of human moral decision-making in kidney allocation contexts, finding that humans use diverse heuristics, change opinions, and express varying confidence levels that simple computational models fail to capture.</span>
- **[Maximizing Social Welfare with Side Payments](https://arxiv.org/abs/2508.07147)**, *Ivan Geffner, Caspar Oesterheld, Vincent Conitzer*, 2025-08-10, arXiv, <span style="color:#777">[paper_preprint, sr=0.20, id:76ed1dc5]</span>, <span style="color:#777">Summary: Introduces a staged-commitment protocol for normal-form games with side payments that achieves welfare-maximizing outcomes while avoiding the inefficiencies that arise from unbounded simultaneous commitments.</span>
- **[Learning and Computation of Φ-Equilibria at the Frontier of Tractability](https://arxiv.org/abs/2502.18582)**, *Brian Hu Zhang, Ioannis Anagnostides, Emanuel Tewolde et al.*, 2025-02-25, arXiv, <span style="color:#777">[paper_preprint, sr=0.12, id:32fb161d]</span>, <span style="color:#777">Summary: Develops polynomial-time algorithms for computing approximate Φ-equilibria in n-player games when deviation set Φ is k-dimensional, extending prior work from linear to polynomial maps using nested ellipsoid-against-hope methods.</span>
- **[Computing Game Symmetries and Equilibria That Respect Them](https://arxiv.org/abs/2501.08905)**, *Emanuel Tewolde, Brian Hu Zhang, Caspar Oesterheld et al.*, 2025-01-15, AAAI 2025, <span style="color:#777">[paper_preprint, sr=0.08, id:39f4e1ac]</span>, <span style="color:#777">Summary: Analyzes the computational complexity of identifying game symmetries and computing Nash equilibria that respect them, establishing graph automorphism completeness for symmetry characterization and PPAD/CLS-completeness for equilibrium computation.</span>
- **[Designing Rules to Pick a Rule: Aggregation by Consistency](https://arxiv.org/abs/2508.17177)**, *Ratip Emin Berker, Ben Armstrong, Vincent Conitzer et al.*, 2025-08-24, arXiv, <span style="color:#777">[paper_preprint, sr=0.08, id:da6285a6]</span>, <span style="color:#777">Summary: Introduces a framework for rule picking rules (RPRs) that selects optimal rank aggregation methods by maximizing consistency under repeated data collection, with axioms, computational hardness proofs, and sampling-based implementation.</span>
- **[Expected Variational Inequalities](https://arxiv.org/abs/2502.18605)**, *Brian Hu Zhang, Ioannis Anagnostides, Emanuel Tewolde et al.*, 2025-02-25, arXiv, <span style="color:#777">[paper_preprint, sr=0.08, id:1620a5fb]</span>, <span style="color:#777">Summary: Introduces expected variational inequalities (EVIs) as a relaxation of variational inequalities, proving they can be solved in polynomial time under general operators and showing they generalize correlated equilibria and other game-theoretic concepts.</span>
- **[An Interpretable Automated Mechanism Design Framework with Large Language Models](https://arxiv.org/abs/2502.12203)**, *Jiayuan Liu, Mingyu Guo, Vincent Conitzer*, 2025-02-16, arXiv, <span style="color:#777">[paper_preprint, sr=0.08, id:ebb6d070]</span>, <span style="color:#777">Summary: Proposes using LLMs to automatically generate interpretable mechanism designs as code, with an evolution process to optimize mechanisms while ensuring design criteria like strategy-proofness through automated fixing processes.</span>


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
- **[New Paper: Ambiguous Online Learning](https://lesswrong.com/posts/Y9NuKpb6dsyiYFxWK/new-paper-ambiguous-online-learning)**, *Vanessa Kosoy*, 2025-06-25, LessWrong, <span style="color:#777">[lesswrong, sr=0.60, id:009c1c42]</span>, <span style="color:#777">Summary: Introduces a new variant of online learning where learners can produce multiple predicted labels, proves a trichotomy of optimal mistake bounds, and explores this framework as an approach to compositional learning theory.</span>
- **[Regret Bounds for Robust Online Decision Making](https://arxiv.org/abs/2504.06820)**, *Alexander Appel, Vanessa Kosoy*, 2025-04-09, arXiv, <span style="color:#777">[paper_preprint, sr=0.45, id:3e1bed8d]</span>, <span style="color:#777">Summary: Proposes a framework for online decision-making with robust (multivalued) models where each decision associates with a convex set of probability distributions, deriving regret bounds for this setting and demonstrating applications to robust linear bandits and tabular robust online reinforcement learning.</span>
- **[New paper: Infra-Bayesian Decision Estimation Theory](https://lesswrong.com/posts/LgLez8aeK24PbyyQJ/new-paper-infra-bayesian-decision-estimation-theory)**, LessWrong, <span style="color:#777">[error_detected, sr=0.00, id:81965857]</span>, <span style="color:#777">Summary: Content unavailable due to HTTP 429 error (Too Many Requests). Based on title, appears to be about Infra-Bayesian Decision Estimation Theory, likely related to the Learning-Theoretic Agenda.</span>


---

### <span style="font-size:1.4em">Other theory</span> <span style="color:#bbb">[cat:theory_other]</span>

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
- **[Measuring Goal-Directedness](https://arxiv.org/abs/2412.04758)**, *Matt MacDermott, James Fox, Francesco Belardinelli et al.*, 2024-12-06, NeurIPS 2024, <span style="color:#777">[paper_published, sr=0.82, id:6eca9c01]</span>, <span style="color:#777">Summary: Defines maximum entropy goal-directedness (MEG), a formal measure of goal-directedness in causal models and MDPs based on maximum causal entropy, proves it satisfies key desiderata, and provides algorithms for computing it with small-scale experimental demonstrations.</span>
- **[TAIS RFP: Research Areas](https://www.openphilanthropy.org/tais-rfp-research-areas/)**, 2025, Open Philanthropy Website, <span style="color:#777">[🔄 agenda_manifesto, sr=0.78, id:bd3f92b8]</span>, <span style="color:#777">Summary: Open Philanthropy's comprehensive research agenda describing 21 technical AI safety research areas they will fund, providing detailed eligibility criteria, example projects, and motivation for each area from jailbreaks to interpretability to theoretical alignment work.</span>
- **[contra Yudkowsky on AI doom: a response ("review of") If Anyone Builds It Everyone Dies](https://nostream.substack.com/p/contra-yudkowsky-on-ai-doom-a-response)**, *nostream*, 2025-09-23, Substack, <span style="color:#777">[🔄 blog_post, sr=0.72, id:e023b6a7]</span>, <span style="color:#777">Summary: Technical critique of Yudkowsky's high p(doom) arguments, arguing against fast takeoff assumptions and for alignment tractability based on current LLM behaviors and empirical evidence from mechanistic interpretability and safety research.</span>
- **[A Taxonomy of Omnicidal Futures Involving Artificial Intelligence](https://arxiv.org/abs/2507.09369)**, *Andrew Critch, Jacob Tsimerman*, 2025-07-12, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:cba996bb]</span>, <span style="color:#777">Summary: Presents a systematic taxonomy classifying different pathways by which AI systems could cause omnicidal outcomes (scenarios where all or nearly all humans are killed), aiming to inform institutional preventive measures against catastrophic AI risks.</span>
- **[International Scientific Report on the Safety of Advanced AI (Interim Report)](https://arxiv.org/abs/2412.05282)**, *Yoshua Bengio, Sören Mindermann, Daniel Privitera et al.*, 2024-11-05, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.70, id:4137abe9]</span>, <span style="color:#777">Summary: International scientific report synthesizing the scientific understanding of general-purpose AI safety, focusing on understanding and managing risks from advanced AI systems. Produced by 75 AI experts from an international panel nominated by 30 countries, the EU, and the UN.</span>
- **[General agents contain world models](https://arxiv.org/abs/2506.01622)**, *Jonathan Richens, David Abel, Alexis Bellot et al.*, 2025-06-02, ICML 2025, <span style="color:#777">[paper_preprint, sr=0.70, id:93b986a9]</span>, <span style="color:#777">Summary: Provides formal proof that any agent capable of generalizing to multi-step goal-directed tasks must have learned a predictive model of its environment, and shows these world models can be extracted from the agent's policy.</span>
- **[The Limits of Predicting Agents from Behaviour](https://arxiv.org/abs/2506.02923)**, *Alexis Bellot, Jonathan Richens, Tom Everitt*, 2025-06-03, ICML 2025, <span style="color:#777">[paper_preprint, sr=0.68, id:91199d50]</span>, <span style="color:#777">Summary: Derives novel theoretical bounds on how well an agent's beliefs can be inferred from behavior and how reliably these inferred beliefs predict behavior in novel deployment environments, assuming the agent's behavior is guided by a world model.</span>
- **[AI Alignment Strategies from a Risk Perspective: Independent Safety Mechanisms or Shared Failures?](https://arxiv.org/abs/2510.11235)**, *Leonard Dung, Florian Mai*, 2025-10-13, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.65, id:0a52aa86]</span>, <span style="color:#777">Summary: Analyzes 7 alignment techniques and 7 failure modes to understand correlation patterns and assess whether defense-in-depth strategies provide genuine redundancy or share common failure modes, with implications for risk assessment and research prioritization.</span>
- **[Superposition Yields Robust Neural Scaling](https://arxiv.org/abs/2505.10465)**, *Yizhou Liu, Ziming Liu, Jeff Gore*, 2025-05-15, NeurIPS 2025 (accepted), arXiv preprint, <span style="color:#777">[paper_preprint, sr=0.62, id:a5391785]</span>, <span style="color:#777">Summary: Proposes that representation superposition (models representing more features than dimensions) is a key driver of neural scaling laws, showing theoretically and empirically that strong superposition causes loss to scale inversely with model dimension across broad frequency distributions.</span>
- **[Training Dynamics of In-Context Learning in Linear Attention](https://arxiv.org/abs/2501.16265)**, *Yedi Zhang, Aaditya K. Singh, Peter E. Latham et al.*, 2025-01-27, arXiv (ICML 2025 Spotlight), <span style="color:#777">[paper_preprint, sr=0.60, id:ff41feaa]</span>, <span style="color:#777">Summary: Provides mathematical analysis of how multi-head linear self-attention acquires in-context learning abilities through gradient descent, characterizing training dynamics for different parametrizations and deriving analytical solutions.</span>
- **[Can CDT rationalise the ex ante optimal policy via modified anthropics?](https://arxiv.org/abs/2411.04462)**, *Emery Cooper, Caspar Oesterheld, Vincent Conitzer*, 2024-11-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.60, id:6188055f]</span>, <span style="color:#777">Summary: Studies whether causal decision theory can recommend ex ante optimal policies in Newcomblike problems through modified anthropic reasoning, proposing simulation-based models and a 'Generalised Generalised Thirding' framework with formal characterizations and proofs.</span>
- **[Gradual Disempowerment: Systemic Existential Risks from Incremental AI Development](https://arxiv.org/abs/2501.16946)**, *Jan Kulveit, Raymond Douglas, Nora Ammann et al.*, 2025-01-28, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.60, id:e6e162ea]</span>, <span style="color:#777">Summary: Develops the concept of 'gradual disempowerment' as an existential risk scenario where incremental AI capability improvements progressively erode human influence over critical societal systems (economy, culture, governance) through both weakened control mechanisms and misaligned optimization pressures.</span>
- **[AGI is not a milestone](https://www.aisnakeoil.com/p/agi-is-not-a-milestone)**, *Sayash Kapoor, Arvind Narayanan*, 2025-05-01, AI Snake Oil / AI as Normal Technology (Substack), <span style="color:#777">[🔄 blog_post, sr=0.58, id:fa676339]</span>, <span style="color:#777">Summary: Argues that AGI is not a meaningful milestone because it represents no discontinuity in AI system properties or impacts, challenging core assumptions about rapid economic transformation, loss of control risks, and the conflation of AI capabilities with power.</span>
- **[AI Tools for Existential Security](https://forethought.org/research/ai-tools-for-existential-security)**, *Lizka Vaintrob, Owen Cotton-Barratt*, 2025-03-14, Forethought Research, <span style="color:#777">[🔄 agenda_manifesto, sr=0.58, id:435cb477]</span>, <span style="color:#777">Summary: Proposes that the AI safety field should prioritize accelerating beneficial AI applications (epistemic tools, coordination-enabling systems, and risk-targeted applications like automated alignment research) through strategies like data curation, scaffolding, and compute allocation to ensure safety capabilities arrive before dangerous ones.</span>
- **[Six Thoughts On AI Safety](https://windowsontheory.org/2025/01/24/six-thoughts-on-ai-safety/)**, *Boaz Barak*, 2025-01-24, Windows On Theory, <span style="color:#777">[🔄 blog_post, sr=0.52, id:39cd05f7]</span>, <span style="color:#777">Summary: Position paper arguing six theses about AI safety: that safety requires active work beyond market forces, automated AI scientists won't solve alignment, alignment should focus on robust compliance with specifications rather than values, detection/monitoring is more important than prevention, interpretability is neither necessary nor sufficient for alignment, and humanity can survive unaligned superintelligence if aligned ASI dominates.</span>
- **[More Was Possible: A Review of If Anyone Builds It, Everyone Dies](https://asteriskmag.com/issues/11/iabied)**, *Clara Collier*, 2025-09-01, Asterisk Magazine, <span style="color:#777">[🔄 blog_post, sr=0.52, id:2ad0279e]</span>, <span style="color:#777">Summary: Critical review of Yudkowsky and Soares' book on AI doom, arguing the book fails to update core MIRI arguments (intelligence explosion, fast takeoff, alignment impossibility) in light of modern AI progress and represents a regression rather than advancement of their position.</span>
- **[ASI existential risk: reconsidering alignment as a goal](https://michaelnotebook.com/xriskbrief/index.html)**, *Michael Nielsen*, 2025-04-14, michaelnotebook.com, <span style="color:#777">[🔄 blog_post, sr=0.52, id:fe397464]</span>, <span style="color:#777">Summary: Strategic critique arguing that alignment work, while well-intentioned, accelerates progress toward catastrophic AI capabilities without addressing the fundamental vulnerability that powerful AI systems will enable dangerous technologies regardless of whether they are aligned or not.</span>
- **[My response to AI 2027](https://vitalik.eth.limo/general/2025/07/10/2027.html)**, *Vitalik Buterin*, 2025-07-10, vitalik.eth.limo, <span style="color:#777">[🔄 blog_post, sr=0.50, id:93679dab]</span>, <span style="color:#777">Summary: Critiques the AI 2027 scenario's assumption that leading AI capabilities will vastly exceed defensive capabilities, arguing that technological diffusion and defense-in-depth approaches (biodefense, cybersecurity, counter-persuasion AI) could make catastrophic outcomes less likely than the scenario assumes.</span>
- **[Superintelligence Strategy](https://www.nationalsecurity.ai/)**, *Dan Hendrycks, Eric Schmidt, Alexandr Wang*, 2025, nationalsecurity.ai, <span style="color:#777">[🔄 agenda_manifesto, sr=0.42, id:30eed622]</span>, <span style="color:#777">Summary: Proposes a national security strategy framework for navigating superintelligence development, introducing Mutual Assured AI Malfunction (MAIM) as a deterrence regime alongside nonproliferation and competitiveness measures to prevent destabilizing AI developments and proliferation to rogue actors.</span>
- **[If You're So Smart, Why Can't You Die?](https://desystemize.substack.com/p/if-youre-so-smart-why-cant-you-die)**, *collin*, 2025-02-16, Desystemize (Substack), <span style="color:#777">[🔄 blog_post, sr=0.42, id:e0e9b27d]</span>, <span style="color:#777">Summary: Philosophical essay arguing that 'intelligence' bundles heterogeneous capabilities that don't necessarily scale together, emphasizing how adversarial dynamics and environmental feedback loops create constraints on AI capabilities that self-play and compute alone cannot overcome.</span>
- **[A Taxonomy of Systemic Risks from General-Purpose AI](https://arxiv.org/abs/2412.07780)**, *Risto Uuk, Carlos Ignacio Gutierrez, Daniel Guppy et al.*, 2024-11-24, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.40, id:377f9d40]</span>, <span style="color:#777">Summary: Systematic literature review of 86 papers proposing a taxonomy of systemic risks from general-purpose AI, identifying 13 risk categories and 50 contributing sources ranging from environmental harm and discrimination to governance failures and loss of control.</span>


---

## <span style="font-size:1.5em">Multi-agent first</span> <span style="color:#bbb">[cat:multi_agent_first]</span>


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
- **[Multi-Agent Risks from Advanced AI](https://arxiv.org/abs/2502.14143)**, *Lewis Hammond, Alan Chan, Jesse Clifton et al.*, 2025-02-19, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.80, id:772b3b66]</span>, <span style="color:#777">Summary: Provides a comprehensive taxonomy of risks from multi-agent AI systems, identifying three key failure modes (miscoordination, conflict, collusion) and seven risk factors (information asymmetries, network effects, selection pressures, destabilizing dynamics, commitment problems, emergent agency, multi-agent security), with mitigation directions for each.</span>
- **[ACE and Diverse Generalization via Selective Disagreement](https://arxiv.org/abs/2509.07955)**, *Oliver Daniels, Stuart Armstrong, Alexandre Maranhão et al.*, 2025-09-09, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.80, id:215ea8e8]</span>, <span style="color:#777">Summary: Proposes ACE, a self-training method that learns multiple concepts consistent with training data but making distinct predictions on novel inputs to resolve underspecification in complete spurious correlations. Tests the method on spurious correlation benchmarks and applies it to measurement tampering detection in language models.</span>
- **[Resource Rational Contractualism Should Guide AI Alignment](https://arxiv.org/abs/2506.17434)**, *Sydney Levine, Matija Franklin, Tan Zhi-Xuan et al.*, 2025-06-20, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.78, id:c9bbef6a]</span>, <span style="color:#777">Summary: Proposes Resource-Rational Contractualism (RRC), a framework for AI alignment that approximates agreements diverse stakeholders would endorse by using cognitively-inspired heuristics that trade computational effort for accuracy when navigating value conflicts.</span>
- **[Statutory Construction and Interpretation for Artificial Intelligence](https://arxiv.org/abs/2509.01186)**, *Luxi He, Nimra Nadeem, Michel Liao et al.*, 2025-09-01, arXiv, <span style="color:#777">[paper_preprint, sr=0.72, id:92dafa08]</span>, <span style="color:#777">Summary: Applies legal theory to AI alignment by proposing a computational framework that reduces interpretive ambiguity in natural language rules governing AI systems through (1) iterative rule refinement to minimize disagreement and (2) prompt-based interpretive constraints to ensure consistent application.</span>
- **[Infrastructure for AI Agents](https://arxiv.org/abs/2501.10114)**, *Alan Chan, Kevin Wei, Sihao Huang et al.*, 2025-01-17, arXiv (accepted to TMLR), <span style="color:#777">[paper_preprint, sr=0.70, id:21a77130]</span>, <span style="color:#777">Summary: Proposes the concept of 'agent infrastructure' - external technical systems and shared protocols designed to mediate AI agent interactions and impacts on their environments, identifying three key functions: attributing actions, shaping interactions, and detecting/remedying harmful actions.</span>
- **[Virtual Agent Economies](https://arxiv.org/abs/2509.10147)**, *Nenad Tomasev, Matija Franklin, Joel Z. Leibo et al.*, 2025-09-12, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.62, id:f772ddfa]</span>, <span style="color:#777">Summary: Proposes the 'sandbox economy' framework for analyzing emergent AI agent economies, discussing design choices for safely steerable agent markets including auction mechanisms, mission economies, and socio-technical infrastructure for trust and accountability.</span>
- **[PGG-Bench: Contribute & Punish](https://github.com/lechmazur/pgg_bench)**, 2025-04-10, GitHub, <span style="color:#777">[code_tool, sr=0.62, id:3532cf20]</span>, <span style="color:#777">Summary: A multi-agent benchmark testing cooperative and self-interested strategies among LLMs in a Public Goods Game extended with punishment mechanics, systematically evaluating 18 models across hundreds of games.</span>
- **[Communication Enables Cooperation in LLM Agents: A Comparison with Curriculum-Based Approaches](https://arxiv.org/abs/2510.05748)**, *Hachem Madmoun, Salem Lahlou*, 2025-10-07, arXiv, <span style="color:#777">[paper_preprint, sr=0.50, id:1a79a926]</span>, <span style="color:#777">Summary: Empirical study comparing communication protocols versus curriculum learning for eliciting cooperation in multi-agent LLM systems, testing approaches in Stag Hunt and Iterated Public Goods games.</span>
- **[Higher-Order Belief in Incomplete Information MAIDs](https://arxiv.org/abs/2503.06323)**, *Jack Foxabbott, Rohan Subramani, Francis Rhys Ward*, 2025-03-08, 24th International Conference on Autonomous Agents and Multiagent Systems 2025, <span style="color:#777">[paper_published, sr=0.48, id:7394d97b]</span>, <span style="color:#777">Summary: Introduces incomplete information MAIDs (II-MAIDs), a formalism for representing strategic multi-agent interactions where agents have different beliefs about the game and each other's beliefs, with equivalence proofs to extensive form games and a recursive best-response solution concept.</span>
- **[Characterizing AI Agents for Alignment and Governance](https://arxiv.org/abs/2504.21848)**, *Atoosa Kasirzadeh, Iason Gabriel*, 2025-04-30, arXiv, <span style="color:#777">[🔄 paper_preprint, sr=0.45, id:66d15eaf]</span>, <span style="color:#777">Summary: Proposes a framework for characterizing AI agents along four dimensions (autonomy, efficacy, goal complexity, and generality) and constructs 'agentic profiles' to illuminate governance challenges posed by different classes of AI agents.</span>


---

### <span style="font-size:1.4em">Align them like you'd align a human</span> <span style="color:#bbb">[cat:human_like_cooperation]</span>

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
- **[Cultivating Pluralism In Algorithmic Monoculture: The Community Alignment Dataset](https://arxiv.org/abs/2507.09650)**, *Lily Hong Zhang, Smitha Milli, Karen Jusko et al.*, 2025-07-13, arXiv, <span style="color:#777">[✌️(in 2 categories) paper_preprint, sr=0.75, id:e066e2b3]</span>, <span style="color:#777">Summary: Demonstrates through a 15,000-participant multilingual study that LLMs exhibit insufficient preference diversity compared to humans, then introduces negatively-correlated sampling methodology and releases the Community Alignment dataset with 200,000 preference comparisons across five countries.</span>
- **[Alignment as uploading with more steps](https://www.lesswrong.com/posts/AzFxTMFfkTt4mhMKt/alignment-as-uploading-with-more-steps)**, *Cole Wyeth*, 2025-09-14, LessWrong, <span style="color:#777">[🔄 lesswrong, sr=0.65, id:dd72ae33]</span>, <span style="color:#777">Summary: Proposes that AI alignment is equivalent to incremental mind uploading via imitation learning with biometric conditioning, arguing that aligned superintelligence must essentially be an emulation of the human it serves, and sketches technical approaches using neural data and singular learning theory.</span>
- **[Build Agent Advocates, Not Platform Agents](https://arxiv.org/abs/2505.04345)**, *Sayash Kapoor, Noam Kolt, Seth Lazar*, 2025-05-07, arXiv (accepted to ICML 2025 position paper track), <span style="color:#777">[paper_preprint, sr=0.40, id:3570bf15]</span>, <span style="color:#777">Summary: Position paper arguing for user-controlled AI agents (agent advocates) rather than platform-controlled agents, proposing three coordinated moves: public access to compute and models, open interoperability standards, and market regulation to prevent platform monopolization.</span>


---

