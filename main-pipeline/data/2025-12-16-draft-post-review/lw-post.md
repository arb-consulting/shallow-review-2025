·   [**Website version**](https://shallowreview.ai)  ·  [**Gestalt**](https://www.lesswrong.com/posts/Q9ewXs8pQSAX5vL7H/ai-in-2025-gestalt)  ·  [**Repo and data**](https://github.com/arb-consulting/shallow-review-2025)  ·

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/wScohuNkKBrHgy5os/afsxnogiorzfudd4nwz9)

Change in 18 latent capabilities between GPT-3 and o1, from[ Zhou et al](https://arxiv.org/abs/2503.06378) (2025)

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/wScohuNkKBrHgy5os/jqebdsxdkvfgn7irbklc)

This is the third annual review of what’s going on in technical AI safety. You could stop reading here and instead explore the data on [the shallow review website](https://shallowreview.ai).

It’s shallow in the sense that 1) we are not specialists in almost any of it and that 2) we only spent about two hours on each entry. Still, among other things, we processed every arXiv paper on alignment, all Alignment Forum posts, as well as a year’s worth of Twitter.

It is substantially a list of lists structuring around 800 links. The point is to produce stylised facts, forests out of trees; to help you look up what’s happening, or that thing you vaguely remember reading about; to help new researchers orient, know some of their options and the standing critiques; and to help you find who to talk to for actual information. We also track things which didn’t pan out.

Here, “AI safety” means technical work intended to prevent *future* cognitive systems from having large unintended negative effects on the world. So it’s capability restraint, instruction-following, value alignment, control, and risk awareness work.

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/wScohuNkKBrHgy5os/zxovntgbnwuydf9ohbfp)

We don’t cover security or resilience at all.

We ignore a lot of relevant work (including most of capability restraint): things like misuse, policy, strategy,[ OSINT](https://sentinel-team.org/),[ resilience](http://airesilience.net/) and[ indirect risk](https://www.forethought.org/research/project-ideas-for-making-transformative-ai-go-well-other-than-by-working-on-alignment),[ AI](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5353214)[ rights](https://arxiv.org/abs/2510.26396), general capabilities evals, and things closer to “[technical policy](https://docs.google.com/document/d/1BGsbwELOQRKVOO8Ho8S4no1BQeYdjbRZpBmRyk7kOVo/edit?usp=sharing)” and[ products](https://themultiplicity.ai/) (like standards, legislation, SL4 datacentres, and automated cybersecurity). We focus on papers and blogposts (rather than say, gdoc samizdat or tweets or Githubs or Discords). We only use public information, so we are off by some additional unknown factor.

We try to include things which are early-stage and illegible – but in general we fail and mostly capture legible work on[ legible problems](https://www.lesswrong.com/posts/PMc65HgRFvBimEpmJ/legible-vs-illegible-ai-safety-problems) (i.e. things you can write a paper on already).

Even ignoring all of that as we do, it’s still too long to read. Here’s a spreadsheet version ([agendas](https://docs.google.com/spreadsheets/d/1uwqeSkl1fGO7bWbbDdNi5QbJ_Zw_a6HO-XlnO18ohLc/edit?gid=249818450#gid=249818450) and [papers](https://docs.google.com/spreadsheets/d/1uwqeSkl1fGO7bWbbDdNi5QbJ_Zw_a6HO-XlnO18ohLc/edit?gid=803096912#gid=803096912)) and [the github repo](https://github.com/arb-consulting/shallow-review-2025) including the data and the processing pipeline. Methods down the bottom. Gavin’s editorial outgrew this post and became [its own thing](https://www.lesswrong.com/posts/Q9ewXs8pQSAX5vL7H/ai-in-2025-gestalt).

If we missed something big or got something wrong, please comment, we will edit it in.

An [Arb Research](https://arbresearch.com/) project. Work funded by ~OpenPhil~ Coefficient Giving.

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/wScohuNkKBrHgy5os/p8xud9wckowur7rauesw)

We have tried to falsify this but it wasn’t easy.

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/wScohuNkKBrHgy5os/nwrjygjpqawo8wqltdyg)

Labs (giant companies)
======================

|   | ![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/wScohuNkKBrHgy5os/9f5054603867a3a3f52174946427f17604447d5e6fa859237a187c4a900b3782/wftpomvmiz4xgklxgutt) | ![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/wScohuNkKBrHgy5os/58834401ca8879bdf8657d9de45e570b351e9b233d6f880de1e7b07f31a725ac/j4lumvk64sse5xso9xrl) | ![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/wScohuNkKBrHgy5os/5c3c1b3bf36f96e5873c63aace64295b95bfe56f8284618bf6548a5556fb30ee/s6ertn2uy7fvjxfqlyzi) | ![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/wScohuNkKBrHgy5os/3ee6f32ebbdcd0f30cf6c85c85b829a1035bae4e1267aaede5b88ea29ed92d30/r52mtvyztwkqlzkp3pxt) | ![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/wScohuNkKBrHgy5os/3581985e788570819225e60744f7175563d8a35161b5bd6702d818ff3fe47f06/wqqzikmfzkls19lekl3a) |
| --- | --- | --- | --- | --- | --- |
| **Safety team % all** Not counting the AIs | <5% | <3% | <3% | <2% | <1% |
| **Leadership’s stated timelines** to full auto AI R&D | [mid-2027](https://www.lesswrong.com/posts/gabPgK9e83QrmcvbK/what-s-up-with-anthropic-predicting-agi-by-early-2027-1) | [2028](https://x.com/deredleritt3r/status/1999262181385437303) to [2035](https://www.cnbc.com/2025/03/17/human-level-ai-will-be-here-in-5-to-10-years-deepmind-ceo-says.html) | [March 2028](https://x.com/ai_ctrl/status/1984311739060482339) | N/A | [ASI by 2030](https://neuron.expert/news/elon-musk-says-theres-only-a-20-chance-of-annihilation-with-ai/11279/en/) |
| **Leadership stated P(AI doom)** | [25%](https://www.axios.com/2025/09/17/anthropic-dario-amodei-p-doom-25-percent) | “Non-zero” and [>5%](https://www.lesswrong.com/posts/No5JpRCHzBrWA4jmS/q-and-a-with-shane-legg-on-risks-from-ai#:~:text=I%20don%27t%20know.-,Maybe%205%25%2C,-maybe%2050%25.%20I) | ~[2%](https://youtu.be/rF0tQtDMwHM?si=Txl0mhrQsq2LXRsp) | ~0% | [20%](https://www.businessinsider.com/elon-musk-only-chance-of-annihilation-with-ai-2025-2) |
| **Legal obligations** | [EU CoP](https://mkodama.org/content/EU-code/), SB53 | EU CoP, SB53 | EU CoP, SB53 | SB53 | EU CoP (Safety), SB53 |
| **Average Safety Score (ZSP, SaferAI, FLI)** | 51% | 27% | 33% | 17% | 17% |

### OpenAI
* *Structure*: public benefit corp
* *Safety teams*: Alignment, Safety Systems (Interpretability, Safety Oversight, Pretraining Safety, Robustness, Safety Research, Trustworthy AI, new Misalignment Research team [coming](https://archive.is/eDB1D)), Preparedness, Model Policy, Safety and Security Committee, Safety Advisory Group. The [Persona Features](https://www.arxiv.org/pdf/2506.19823) paper had a distinct author list. No named successor to Superalignment.
* *Public alignment agenda*: [None](https://openai.com/safety/how-we-think-about-safety-alignment/). Boaz Barak [offers](https://www.lesswrong.com/posts/3jnziqCF3vA2NXAKp/six-thoughts-on-ai-safety) personal [views](https://windowsontheory.org/2025/06/24/machines-of-faithful-obedience/).
* *Risk management framework*: [Preparedness Framework](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf)
* *See also:* [Iterative alignment](#Iterative_alignment) · [Safeguards (inference-time auxiliaries)](#Safeguards_inference_time_auxiliaries_) · [Character training and persona steering](#Character_training_and_persona_steering)
* *Some names:* Johannes Heidecke, Boaz Barak, Mia Glaese, Jenny Nitishinskaya, Lama Ahmad, Naomi Bashkansky, Miles Wang, Wojciech Zaremba, David Robinson, Zico Kolter, Jerry Tworek, Eric Wallace, Olivia Watkins, Kai Chen, Chris Koch, Andrea Vallone, Leo Gao
* *Critiques:* [Stein-Perlman](https://ailabwatch.org/companies/openai), [Stewart](https://intelligence.org/2025/03/31/a-response-to-openais-how-we-think-about-safety-and-alignment/), [underelicitation](https://www.lesswrong.com/posts/AK6AihHGjirdoiJg6/ai-companies-eval-reports-mostly-don-t-support-their-claims), [Midas](https://www.openaifiles.org/transparency-and-safety), [defense](https://www.wired.com/story/openai-anduril-defense/), [Carlsmith](https://joecarlsmith.com/2025/11/03/leaving-open-philanthropy-going-to-anthropic#:~:text=a%20few%20words%20about%20some%20more%20general%20concerns%20about%20AI%2Dsafety%2Dfocused%20people%20going%20to%20work%20at%20AI%20companies%20\(and/or%2C%20at%20Anthropic%20in%20particular\).) on labs in general. It's [difficult](https://conversationswithtyler.com/episodes/sam-altman-2/) to model OpenAI as a single agent: *"ALTMAN: I very rarely get to have anybody work on anything. One thing about researchers is they're going to work on what they're going to work on, and that's that."*
* *Funded by:* Microsoft, [AWS](https://www.aboutamazon.com/news/aws/aws-open-ai-workloads-compute-infrastructure), Oracle, NVIDIA, SoftBank, G42, AMD, Dragoneer, Coatue, Thrive, Altimeter, MGX, Blackstone, TPG, T. Rowe Price, Andreessen Horowitz, D1 Capital Partners, Fidelity Investments, Founders Fund, Sequoia…
+++ Some outputs (13)

*   Their 60-page System Cards now contain a large amount of their public safety work.
*   [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926). *Bowen Baker et al.*
*   [Persona Features Control Emergent Misalignment](https://arxiv.org/abs/2506.19823). *Miles Wang et al.*
*   [Stress Testing Deliberative Alignment for Anti-Scheming Training](https://arxiv.org/abs/2509.15541). *Bronson Schoen et al.*
*   [Deliberative Alignment: Reasoning Enables Safer Language Models](https://arxiv.org/abs/2412.16339). *Melody Y. Guan et al.*
*   [Toward understanding and preventing misalignment generalization](https://openai.com/index/emergent-misalignment). *Miles Wang et al.*
*   [Our updated Preparedness Framework](https://openai.com/index/updating-our-preparedness-framework/). *OpenAI Preparedness Team*
*   [Trading Inference-Time Compute for Adversarial Robustness](https://arxiv.org/abs/2501.18841). *Wojciech Zaremba et al.*
*   [Small-to-Large Generalization: Data Influences Models Consistently Across Scale](https://arxiv.org/abs/2505.16260). *Alaa Khaddaj, Logan Engstrom, Aleksander Madry*
*   [Findings from a pilot Anthropic–OpenAI alignment evaluation exercise: OpenAI Safety Tests](https://openai.com/index/openai-anthropic-safety-evaluation)
*   [Safety evaluations hub](https://openai.com/safety/evaluations-hub)
*   [alignment.openai.com](https://alignment.openai.com/)
*   [Weight-sparse transformers have interpretable circuits](https://cdn.openai.com/pdf/41df8f28-d4ef-43e9-aed2-823f9393e470/circuit-sparsity-paper.pdf)
+++

### Google Deepmind
* *Structure*: research laboratory subsidiary of a for-profit
* *Safety teams*: amplified oversight, interpretability, ASAT eng (automated alignment research), Causal Incentives Working Group, Frontier Safety Risk Assessment (evals, threat models, the framework), Mitigations (e.g. banning accounts, refusal training, jailbreak robustness), Loss of Control (control, alignment evals). Structure [here](https://gist.github.com/g-leech/30f2484d0318b5d9d489e5748fe46131).
* *Public alignment agenda*: [An Approach to Technical AGI Safety and Security](https://arxiv.org/abs/2504.01849)
* *Risk management framework*: [Frontier Safety Framework](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)
* *See also:* [White-box safety (i.e. Interpretability)](#White_box_safety_i_e_Interpretability_) · Scalable Oversight
* *Some names:* Rohin Shah, Allan Dafoe, Anca Dragan, Alex Irpan, Alex Turner, Anna Wang, Arthur Conmy, David Lindner, Jonah Brown-Cohen, Lewis Ho, Neel Nanda, Raluca Ada Popa, Rishub Jain, Rory Greig, Sebastian Farquhar, Senthooran Rajamanoharan, Sophie Bridgers, Tobi Ijitoye, Tom Everitt, Victoria Krakovna, Vikrant Varma, Zac Kenton, Four Flynn, Jonathan Richens, Lewis Smith, Janos Kramar, Matthew Rahtz, Mary Phuong, Erik Jenner
* *Critiques:* [Stein-Perlman](https://ailabwatch.org/companies/deepmind), [Carlsmith](https://joecarlsmith.com/2025/11/03/leaving-open-philanthropy-going-to-anthropic#:~:text=a%20few%20words%20about%20some%20more%20general%20concerns%20about%20AI%2Dsafety%2Dfocused%20people%20going%20to%20work%20at%20AI%20companies%20\(and/or%2C%20at%20Anthropic%20in%20particular\).) on labs in general, [underelicitation](https://www.lesswrong.com/posts/AK6AihHGjirdoiJg6/ai-companies-eval-reports-mostly-don-t-support-their-claims), [On Google's Safety Plan](https://lesswrong.com/posts/hvEikwtsbf6zaXG2s/on-google-s-safety-plan)
* *Funded by:* Google. Explicit 2024 Deepmind spending as a whole was [£1.3B](https://s3.eu-west-2.amazonaws.com/document-api-images-live.ch.gov.uk/docs/WT_VNJe9leRjfcU0-OtRjWqF7WiqueStclXgHPbdG4U/application-pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAWRGBDBV3HTI6EAXB%2F20251212%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T104902Z&X-Amz-Expires=60&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCWV1LXdlc3QtMiJGMEQCIH6GyZRz66qwZsWkZORhsAQyzQQoJ7j0F4jnnWsgT8i2AiBkQVTWkLiSt%2F89o2yMC5D9NGQ75b1RwC8MBr7dlvrJXyqBBAgAEAUaDDQ0OTIyOTAzMjgyMiIMDkbkT%2FH2vUMV3NxOKt4DfZ6bw%2BWE%2BPfifW4goryaR4bQ%2FeFEXDvW7MU%2BKlfUM8A2fNyEUpIq4f6PsRf0zntVIXmUOWnvyIcVB7EA31NcPn3O%2FHFga8gKZyDPnQnj7YM5Wrt%2FVvR2mj7dJcioOSATW6joYuAb2X0l6IVHXJnYcaxStVCaPauK98OWTTXwCQQwG9UYBWe5SGqOroOw%2FoYWx9GRGvDtQfQThGemJnDr%2FHkbM9YH%2BY860lrE4MEXQiPakkwgJZC%2B8kqsqxzAIyWegPjp3TvrNs7WJ4Fheq0BJo8B7uw0pYBB%2BE9WQEjgaO5dByd90cpnyHu%2F8HGSxwmuQQiUtrp0T3xpP1G%2B3bP%2FLUnhGTD6XWLW%2BtoywQ5ZJrizfwuLQuxFjZt2JwV50DslF47H4AltBRxQh6HHro%2BpiJJEv0rC5NKBS4XRaL8FWOFMD%2BxJctPoCxFJhour3SbcMET4148eVQL%2FenkSdPUz2FHNrO%2BnOTyZAG%2Bi9xiZR1MVOCYHTPHKFG9ReY4ck2mz4W94%2FI6iWuu%2BKWlrEr2hEWzo2RhwDJ09ASgoKNErYb2mJ4E0rMGQ7cv8d2bqF7f6ok1SbzJPClaCBN4qYBzX1rE2Uhdf4v2QueSi4c0i8oCWOGfsdp5FxpgrOlEIqzC9%2Fu7JBjqmAardqlTk%2BobAEzv0H0m2RO4m901C%2FsTzIKb2UlMRrUkTDH4MpCSg5eW3A86X2TnPfl66jC%2FV2P%2FIwY%2FkvsY7wNBgtYR92XE%2FMwyz1x3JD1qDnGWPybjso72aEPrMyekV2WV3U0%2BYh8zn83%2BneYZB9VaTu2QqSv7TZe3IWJyErbuZw%2BhmMlk5nhKZDNmo%2Fc12x%2B7jI0N6aKqUdp8BkGOqPrlUxn2mKcg%3D&X-Amz-SignedHeaders=host&response-content-disposition=inline%3Bfilename%3D%22companies_house_document.pdf%22&X-Amz-Signature=52be18d98d9589fa46d3686876b3107925b67ee083d05199e1428dfc14b9c457), but this doesn't count most spending e.g. Gemini compute.
+++ Some outputs (14)

*   [A Pragmatic Vision for Interpretability](https://www.alignmentforum.org/posts/StENzDcD3kpfGJssR/a-pragmatic-vision-for-interpretability%20). *Neel Nanda et al.*
*   [How Can Interpretability Researchers Help AGI Go Well?](https://www.alignmentforum.org/posts/MnkeepcGirnJn736j/how-can-interpretability-researchers-help-agi-go-well%20). *Neel Nanda et al.*
*   [Evaluating Frontier Models for Stealth and Situational Awareness](https://arxiv.org/abs/2505.01420). *Mary Phuong et al.*
*   [When Chain of Thought is Necessary, Language Models Struggle to Evade Monitors](https://arxiv.org/abs/2507.05246). *Scott Emmons et al.*
*   [MONA: Managed Myopia with Approval Feedback](https://alignmentforum.org/posts/zWySWKuXnhMDhgwc3/mona-managed-myopia-with-approval-feedback-2). *Sebastian Farquhar, David Lindner, Rohin Shah*
*   [Consistency Training Helps Stop Sycophancy and Jailbreaks](https://arxiv.org/abs/2510.27062). *Alex Irpan et al.*
*   [An Approach to Technical AGI Safety and Security](https://arxiv.org/abs/2504.01849). *Rohin Shah et al.*
*   [Negative Results for SAEs On Downstream Tasks and Deprioritising SAE Research (GDM Mech Interp Team Progress Update #2)](https://alignmentforum.org/posts/4uXCAJNuPKtKBsi28/negative-results-for-saes-on-downstream-tasks). *Lewis Smith et al.*
*   [Steering Gemini Using BIDPO Vectors](https://turntrout.com/gemini-steering). *Alex Turner et al.*
*   [Difficulties with Evaluating a Deception Detector for AIs](https://arxiv.org/html/2511.22662v1). *Lewis Smith, Bilal Chughtai, Neel Nanda*
*   [Taking a responsible path to AGI](https://deepmind.google/discover/blog/taking-a-responsible-path-to-agi/). *Anca Dragan et al.*
*   [Evaluating potential cybersecurity threats of advanced AI](https://deepmind.google/discover/blog/evaluating-potential-cybersecurity-threats-of-advanced-ai). *Four Flynn, Mikel Rodriguez, Raluca Ada Popa*
*   [Self-preservation or Instruction Ambiguity? Examining the Causes of Shutdown Resistance](https://www.alignmentforum.org/posts/wnzkjSmrgWZaBa2aC/self-preservation-or-instruction-ambiguity-examining-the). *Senthooran Rajamanoharan, Neel Nanda*
*   [A Pragmatic Way to Measure Chain-of-Thought Monitorability](https://arxiv.org/abs/2510.23966). *Scott Emmons et al.*
+++

### Anthropic
* *Structure*: public-benefit corp
* *Safety teams*: Scalable Alignment (Leike), Alignment Evals (Bowman), [Interpretability](https://transformer-circuits.pub/) (Olah), Control (Perez), Model Psychiatry (Lindsey), Character (Askell), Alignment Stress-Testing (Hubinger), Alignment Mitigations (Price?), Frontier Red Team (Graham), Safeguards (?), Societal Impacts (Ganguli), Trust and Safety (Sanderford), Model Welfare (Fish)
* *Public alignment agenda*: [directions](https://alignment.anthropic.com/2025/recommended-directions/), [bumpers](https://alignment.anthropic.com/2025/bumpers/), [checklist](https://sleepinyourhat.github.io/checklist/), an [old vague view](https://www.anthropic.com/news/core-views-on-ai-safety)
* *Risk management framework*: [RSP](https://www-cdn.anthropic.com/872c653b2d0501d6ab44cf87f43e1dc4853e4d37.pdf)
* *See also:* [White-box safety (i.e. Interpretability)](#White_box_safety_i_e_Interpretability_) · Scalable Oversight
* *Some names:* Chris Olah, Evan Hubinger, Sam Marks, Johannes Treutlein, Sam Bowman, Euan Ong, Fabien Roger, Adam Jermyn, Holden Karnofsky, Jan Leike, Ethan Perez, Jack Lindsey, Amanda Askell, Kyle Fish, Sara Price, Jon Kutasov, Minae Kwon, Monty Evans, Richard Dargan, Roger Grosse, Ben Levinstein, Joseph Carlsmith, Joe Benton
* *Critiques:* [Stein](https://ailabwatch.org/anthropic-opinions)[-Perlman](https://ailabwatch.org/companies/anthropic), [Casper](https://www.lesswrong.com/posts/pH6tyhEnngqWAXi9i/eis-xiii-reflections-on-anthropic-s-sae-research-circa-may#A_review___thoughts), [Carlsmith](https://joecarlsmith.com/2025/11/03/leaving-open-philanthropy-going-to-anthropic#:~:text=a%20few%20words%20about%20some%20more%20general%20concerns%20about%20AI%2Dsafety%2Dfocused%2Dpeople%20going%20to%20work%20at%20AI%20companies%20\(and/or%2C%20at%20Anthropic%20in%20particular\).), [underelicitation](https://www.lesswrong.com/posts/AK6AihHGjirdoiJg6/ai-companies-eval-reports-mostly-don-t-support-their-claims), [Greenblatt](https://nitter.net/RyanPGreenblatt/status/1925992236648464774), [Samin](https://www.lesswrong.com/posts/5aKRshJzhojqfbRyo/unless-its-governance-changes-anthropic-is-untrustworthy), [defense](https://techcrunch.com/2024/11/07/anthropic-teams-up-with-palantir-and-aws-to-sell-its-ai-to-defense-customers/), [Existing Safety Frameworks Imply Unreasonable Confidence](https://lesswrong.com/posts/7ExkgcDudwhag73vw/existing-safety-frameworks-imply-unreasonable-confidence)
* *Funded by:* Amazon, Google, ICONIQ, Fidelity, Lightspeed, Altimeter, Baillie Gifford, BlackRock, Blackstone, Coatue, D1 Capital Partners, General Atlantic, General Catalyst, GIC, Goldman Sachs, Insight Partners, Jane Street, Ontario Teachers' Pension Plan, Qatar Investment Authority, TPG, T. Rowe Price, WCM, XN
+++ Some outputs (21)

*   [Evaluating honesty and lie detection techniques on a diverse suite of dishonest models](https://alignment.anthropic.com/2025/honesty-elicitation/). *Rowan Wang et al.*
*   [Agentic Misalignment: How LLMs could be insider threats](https://anthropic.com/research/agentic-misalignment). *Aengus Lynch et al.*
*   [Why Do Some Language Models Fake Alignment While Others Don't?](https://alignmentforum.org/posts/ghESoA8mo3fv9Yx3E/why-do-some-language-models-fake-alignment-while-others-don). *abhayesian et al.*
*   [Forecasting Rare Language Model Behaviors](https://arxiv.org/abs/2502.16797). *Erik Jones et al.*
*   [Findings from a Pilot Anthropic—OpenAI Alignment Evaluation Exercise](https://alignment.anthropic.com/2025/openai-findings). *Samuel R. Bowman et al.*
*   [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html). *Jack Lindsey et al.*
*   [Auditing language models for hidden objectives](https://www.anthropic.com/research/auditing-hidden-objectives)
*   [Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples](https://arxiv.org/abs/2510.07192). *Alexandra Souly et al.*
*   [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html). *Emmanuel Ameisen et al.*
*   [SHADE-Arena: Evaluating sabotage and monitoring in LLM agents](https://anthropic.com/research/shade-arena-sabotage-monitoring). *Xiang Deng et al.*
*   [Emergent Introspective Awareness in Large Language Models](https://transformer-circuits.pub/2025/introspection/index.html). *Jack Lindsey*
*   [Reasoning models don't always say what they think](https://www.anthropic.com/research/reasoning-models-dont-say-think)
*   [Petri: An open-source auditing tool to accelerate AI safety research](https://alignment.anthropic.com/2025/petri)
*   [Signs of introspection in large language models](https://anthropic.com/research/introspection)
*   [Putting up Bumpers](https://alignment.anthropic.com/2025/bumpers/)
*   [Three Sketches of ASL-4 Safety Case Components](https://alignment.anthropic.com/2024/safety-cases/index.html)
*   [Recommendations for Technical AI Safety Research Directions](https://alignment.anthropic.com/2025/recommended-directions/index.html). *Anthropic Alignment Science Team*
*   [Constitutional Classifiers: Defending against universal jailbreaks](https://www.anthropic.com/research/constitutional-classifiers). *Anthropic Safeguards Research Team*
*   [The Soul Document](https://gist.github.com/Richard-Weiss/efe157692991535403bd7e7fb20b6695). *Richard-Weiss*
*   [Open-sourcing circuit tracing tools](https://anthropic.com/research/open-source-circuit-tracing). *Michael Hanna et al.*
*   [Natural emergent misalignment from reward hacking](https://assets.anthropic.com/m/74342f2c96095771/original/Natural-emergent-misalignment-from-reward-hacking-paper.pdf)
+++

### xAI
* *Structure*: [for-profit](https://www.cnbc.com/amp/2025/08/25/elon-musk-xai-dropped-public-benefit-corp-status-while-fighting-openai.html)
* *Teams*: [Applied Safety](https://job-boards.greenhouse.io/xai/jobs/4944324007), Model Evaluation. Nominally focussed on misuse.
* *Framework*: [Risk Management Framework](https://data.x.ai/2025-08-20-xai-risk-management-framework.pdf)
* *Some names:* Dan Hendrycks (advisor), Juntang Zhuang, Toby Pohlen, Lianmin Zheng, Piaoyang Cui, Nikita Popov, Ying Sheng, Sehoon Kim, Alexander Pan
* *Critiques:* [framework](https://www.lesswrong.com/posts/hQyrTDuTXpqkxrnoH/xai-s-new-safety-framework-is-dreadful), [hacking](https://x.com/g_leech_/status/1990543987846078854), [broken promises](https://x.com/g_leech_/status/1990734517145911593), [Stein](https://ailabwatch.org/companies/xai)\-[Perlman](https://ailabwatch.org/resources/integrity#xai), [insecurity](https://nitter.net/elonmusk/status/1961904269545648624), [Carlsmith](https://joecarlsmith.com/2025/11/03/leaving-open-philanthropy-going-to-anthropic#:~:text=a%20few%20words%20about%20some%20more%20general%20concerns%20about%20AI%2Dsafety%2Dfocused%20people%20going%20to%20work%20at%20AI%20companies%20\(and/or%2C%20at%20Anthropic%20in%20particular\).) on labs in general
* *Funded by:* A16Z, Blackrock, Fidelity, Kingdom, Lightspeed, MGX, Morgan Stanley, Sequoia…

### Meta
* *Structure*: for-profit
* *Teams*: Safety "integrated into" capabilities research, Meta Superintelligence Lab. But also FAIR Alignment, [Brain and AI](https://www.metacareers.com/jobs/1319148726628205).
* *Framework*: [FAF](https://ai.meta.com/static-resource/meta-frontier-ai-framework/?utm_source=newsroom&utm_medium=web&utm_content=Frontier_AI_Framework_PDF&utm_campaign=Our_Approach_to_Frontier_AI_blog)
* *See also:* [Capability removal: unlearning](#Capability_removal_unlearning)
* *Some names:* Shuchao Bi, Hongyuan Zhan, Jingyu Zhang, Haozhu Wang, Eric Michael Smith, Sid Wang, Amr Sharaf, Mahesh Pasupuleti, Jason Weston, ShengYun Peng, Ivan Evtimov, Song Jiang, Pin-Yu Chen, Evangelia Spiliopoulou, Lei Yu, Virginie Do, Karen Hambardzumyan, Nicola Cancedda, Adina Williams
* *Critiques:* [extreme underelicitation](https://googleprojectzero.blogspot.com/2024/06/project-naptime.html#:~:text=We%20find%20that%2C%20by%20refining%20the%20testing%20methodology%20to%20take%20advantage%20of%20modern%20LLM%20capabilities%2C%20significantly%20better%20performance%20in%20vulnerability%20discovery%20can%20be%20achieved.%20To%20facilitate%20effective%20evaluation%20of%20LLMs%20for%20vulnerability%20discovery%2C%20we%20propose%20below%20a%20set%20of%20guiding%20principles.), [Stein](https://ailabwatch.org/companies/meta)-[Perlman](https://ailabwatch.org/companies/meta), [Carlsmith](https://joecarlsmith.com/2025/11/03/leaving-open-philanthropy-going-to-anthropic#:~:text=a%20few%20words%20about%20some%20more%20general%20concerns%20about%20AI%2Dsafety%2Dfocused%20people%20going%20to%20work%20at%20AI%20companies%20\(and/or%2C%20at%20Anthropic%20in%20particular\).) on labs in general
* *Funded by:* Meta
+++ Some outputs (6)

*   [The Alignment Waltz: Jointly Training Agents to Collaborate for Safety](https://arxiv.org/pdf/2510.08240). *Jingyu Zhang et al.*
*   [Large Reasoning Models Learn Better Alignment from Flawed Thinking](https://arxiv.org/pdf/2510.00938%20). *ShengYun Peng et al.*
*   [Robust LLM safeguarding via refusal feature adversarial training](https://arxiv.org/pdf/2409.20089). *Lei Yu et al.*
*   [Code World Model Preparedness Report](https://scontent-lhr8-1.xx.fbcdn.net/v/t39.2365-6/557601942_1468972530985309_838842257265552803_n.pdf?_nc_cat=108&ccb=1-7&_nc_sid=3c67a6&_nc_ohc=_H33_VKF3ZUQ7kNvwFog8dd&_nc_oc=AdlNtqCDY4HafZ3-d5rb26AF5f2m0X46SGdKhVq3jLqwpNf_wEXhdQnH7_30ychiZWk&_nc_zt=14&_nc_ht=scontent-lhr8-1.xx&_nc_gid=QvW_ePiaF4E-PxOf30MWyg&oh=00_AfiZC5G4ODvWhiy0MuVH8PSlUFrW8RDQQ8tdr6Zec5k9aA&oe=691A6D09)
*   [Agents Rule of Two: A Practical Approach to AI Agent Security](https://ai.meta.com/blog/practical-ai-agent-security/%20)
*   [AI & Human Co-Improvement](https://github.com/facebookresearch/RAM/blob/main/projects/co-improvement.pdf)
+++

### China

The Chinese companies [don’t](https://futureoflife.org/wp-content/uploads/2025/07/FLI-AI-Safety-Index-Report-Summer-2025.pdf#page=3) [attempt](https://ailabwatch.org/companies/deepseek) to be safe, often not even in the prosaic safeguards sense. They drop the weights [immediately](https://x.com/natolambert/status/1991915728992190909) after post-training finishes. They’re mostly open weights and closed data. As of writing the companies are often [severely](https://www.wsj.com/tech/ai/china-us-ai-chip-restrictions-effect-275a311e) compute-constrained. There are some [informal reasons](https://www.gleech.org/paper) to doubt their capabilities. The (academic) Chinese AI safety scene is however [also](https://concordia-ai.com/research/state-of-ai-safety-in-china-2025/) growing.

*   Alibaba’s Qwen3-etc-etc is [nominally](https://artificialanalysis.ai/leaderboards/models) at the level of Gemini 2.5 Flash. Maybe the only Chinese model with a [large](https://www.atomproject.ai/#:~:text=Model%20Adoption%20Trends) Western userbase, including businesses, but since it’s self-hosted this doesn’t translate into profits for them yet. On [one ad hoc test](https://www.gleech.org/paper) it was the only Chinese model not to collapse OOD, but the Qwen2.5 corpus was severely contaminated.
*   DeepSeek’s v3.2 is [nominally](https://artificialanalysis.ai/leaderboards/models) around the same as Qwen. The CCP made them [waste](https://arstechnica.com/ai/2025/08/deepseek-delays-next-ai-model-due-to-poor-performance-of-chinese-made-chips/) months trying Huawei chips.
*   Moonshot’s Kimi-K2-Thinking has some nominally [frontier](https://artificialanalysis.ai/) benchmark results and a pleasant style but does not [seem](https://x.com/METR_Evals/status/1991658241932292537) frontier.
*   Baidu’s [ERNIE 5](https://x.com/Baidu_Inc/status/1988820837898829918) is again nominally very strong, a bit better than DeepSeek. This new one seems to not be open.
*   Z’s [GLM-4.6](https://z.ai/blog/glm-4.6) is around the same as Qwen. The product director was involved in the MIT Alignment group.
*   MiniMax’s M2 is nominally better than Qwen, [around the same](https://artificialanalysis.ai/leaderboards/models) as Grok 4 Fast on the usual superficial benchmarks. It does [fine](https://www.holisticai.com/blog/red-teaming-open-source-ai-models-china) on one very basic red-team test.
*   ByteDance does impressive research in a lagging paradigm, [diffusion LMs](https://seed.bytedance.com/en/direction/llm).
*   There are [others](https://www.interconnects.ai/i/171165224/honorable-mentions) but they’re marginal for now.

### Other labs

*   Amazon’s [Nova Pro](https://arxiv.org/pdf/2506.12103v1) is around the level of Llama 3 90B, which in turn is around the level of the original GPT-4. So 2 years behind. But they have their own [chip](https://www.businessinsider.com/startups-amazon-ai-chips-less-competitive-nvidia-gpus-trainium-aws-2025-11).
*   Microsoft are [now](https://www.dwarkesh.com/p/satya-nadella-2) mid-training on top of GPT-5. MAI-1-preview is [around](https://lmarena.ai/leaderboard/text) DeepSeek V3.0 level on Arena. They [continue](https://arxiv.org/abs/2506.22405v1) to focus on medical diagnosis. You can [request](https://forms.microsoft.com/pages/responsepage.aspx?id=v4j5cvGGr0GRqy180BHbRyRliS0ly-JEvgSpwo3yWyhUQkdTQktBUkFaWERHR1JFRjgwMlZUUkQxTC4u&route=shorturl) access.
*   Mistral have a reasoning model, [Magistral Medium](https://arxiv.org/pdf/2506.10910), and released the weights of a little 24B version. It’s a bit worse than Deepseek R1, pass@1.

Black-box safety (understand and control current model behaviour)
=================================================================

Iterative alignment
-------------------

Nudging base models by optimising their output. Worked on by the post-training teams at most labs, estimating the FTEs at >500 in some sense. Funded by most of the industry.

*   *General theory of change:* "LLMs don't seem very dangerous and might scale to AGI, things are generally smooth, relevant capabilities are harder than alignment, assume no mesaoptimisers, assume that zero-shot deception is hard, assume a fundamentally humanish ontology is learned, assume no simulated agents, assume that noise in the data means that human preferences are not ruled out, assume that alignment is a superficial feature, assume that tuning for what we want will also get us to avoid what we don't want. Maybe assume that thoughts are translucent."
*   *General critiques:* [Bellot](https://arxiv.org/abs/2506.02923), [Alfour](https://cognition.cafe/p/ai-alignment-based-on-intentions), [STACK](https://arxiv.org/abs/2506.24068), [AI Alignment Strategies from a Risk Perspective](https://arxiv.org/abs/2510.11235), [AI Alignment based on Intentions does not work](https://t.co/OTnrYRVsPS), [Distortion of AI Alignment: Does Preference Optimization Optimize for Preferences?](https://arxiv.org/abs/2505.23749), [Murphy’s Laws of AI Alignment: Why the Gap Always Wins](https://arxiv.org/abs/2509.05381), [Alignment remains a hard, unsolved problem](https://www.alignmentforum.org/posts/epjuxGnSPof3GnMSL)

### Iterative alignment at pretrain-time

*Guide weights during pretraining.*

*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *See also:* [prosaic alignment](https://www.lesswrong.com/posts/5ciYedyQDDqAcrDLr/a-positive-case-for-how-we-might-succeed-at-prosaic-ai) · [incrementalism](https://www.lesswrong.com/posts/TALmStNf6479uTwzT/ai-alignment-metastrategy#Incrementalist_Metastrategy) · [alignment-by-default](https://www.lesswrong.com/posts/Nwgdq6kHke5LY692J/alignment-by-default) · [Korbak 2023](https://arxiv.org/abs/2302.08582)
*   *Some names:* Jan Leike, Stuart Armstrong, Cyrus Cousins, Oliver Daniels
*   *Critiques:* [Bellot](https://arxiv.org/abs/2506.02923), [STACK](https://arxiv.org/abs/2506.24068), [Dung](https://arxiv.org/abs/2510.11235), [Gaikwad](https://arxiv.org/abs/2509.05381), [Hubinger](https://www.alignmentforum.org/posts/epjuxGnSPof3GnMSL)
*   *Funded by:* most of the industry

+++ Some outputs (2)

*   [Unsupervised Elicitation](https://alignment.anthropic.com/2025/unsupervised-elicitation). *Jiaxin Wen et al.*
*   [ACE and Diverse Generalization via Selective Disagreement](https://arxiv.org/abs/2509.07955). *Oliver Daniels et al.*

+++

### Iterative alignment at post-train-time

*Modify weights after pre-training.*

*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Some names:* Adam Gleave, Anca Dragan, Jacob Steinhardt, Rohin Shah
*   *Critiques:* [Bellot](https://arxiv.org/abs/2506.02923), [STACK](https://arxiv.org/abs/2506.24068), [Dung](https://arxiv.org/abs/2510.11235), [Gölz](https://arxiv.org/abs/2505.23749), [Gaikwad](https://arxiv.org/abs/2509.05381), [Hubinger](https://www.alignmentforum.org/posts/epjuxGnSPof3GnMSL)
*   *Funded by:* most of the industry

+++ Some outputs (16)

*   [Composable Interventions for Language Models](https://arxiv.org/abs/2407.06483). *Arinbjorn Kolbeinsson et al.*
*   [Spilling the Beans: Teaching LLMs to Self-Report Their Hidden Objectives](https://arxiv.org/abs/2511.06626). *Chloe Li, Mary Phuong, Daniel Tan*
*   [On Targeted Manipulation and Deception when Optimizing LLMs for User Feedback](https://arxiv.org/abs/2411.02306). *Marcus Williams et al.*
*   [Preference Learning with Lie Detectors can Induce Honesty or Evasion](https://arxiv.org/abs/2505.13787). *Chris Cundy, Adam Gleave*
*   [Robust LLM Alignment via Distributionally Robust Direct Preference Optimization](https://arxiv.org/abs/2502.01930). *Zaiyan Xu et al.*
*   [RLHS: Mitigating Misalignment in RLHF with Hindsight Simulation](https://arxiv.org/abs/2501.08617). *Kaiqu Liang et al.*
*   [Reducing the Probability of Undesirable Outputs in Language Models Using Probabilistic Inference](https://arxiv.org/abs/2510.21184). *Stephen Zhao et al.*
*   [Iterative Label Refinement Matters More than Preference Optimization under Weak Supervision](https://arxiv.org/abs/2501.07886). *Yaowen Ye, Cassidy Laidlaw, Jacob Steinhardt*
*   [Consistency Training Helps Stop Sycophancy and Jailbreaks](https://arxiv.org/abs/2510.27062). *Alex Irpan et al.*
*   [Rethinking Safety in LLM Fine-tuning: An Optimization Perspective](https://arxiv.org/abs/2508.12531). *Minseon Kim et al.*
*   [Preference Learning for AI Alignment: a Causal Perspective](https://arxiv.org/abs/2506.05967). *Katarzyna Kobalczyk, Mihaela van der Schaar*
*   [On Monotonicity in AI Alignment](https://arxiv.org/abs/2506.08998). *Gilles Bareilles et al.*
*   [Spectrum Tuning: Post-Training for Distributional Coverage and In-Context Steerability](https://arxiv.org/abs/2510.06084). *Taylor Sorensen et al.*
*   [Uncertainty-Aware Step-wise Verification with Generative Reward Models](https://arxiv.org/abs/2502.11250). *Zihuiwen Ye et al.*
*   [The Delta Learning Hypothesis: Preference Tuning on Weak Data can Yield Strong Gains](https://arxiv.org/abs/2507.06187). *Scott Geng et al.*
*   [Training LLMs for Honesty via Confessions](https://arxiv.org/pdf/2512.08093). *Manas Joglekar et al.*

+++

### Black-box make-AI-solve-it

*Focus on using existing models to improve and align further models.*

*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *See also:* [Make AI solve it](#Make_AI_solve_it) · [Debate](#Debate)
*   *Some names:* Jacques Thibodeau, Matthew Shingle, Nora Belrose, Lewis Hammond, Geoffrey Irving
*   *Critiques:* [STACK](https://arxiv.org/abs/2506.24068), [Dung](https://arxiv.org/abs/2510.11235), [Gölz](https://arxiv.org/abs/2505.23749), [Gaikwad](https://arxiv.org/abs/2509.05381), [Hubinger](https://www.alignmentforum.org/posts/epjuxGnSPof3GnMSL), [SAIF](https://saif.org/research/bare-minimum-mitigations-for-autonomous-ai-development/)
*   *Funded by:* most of the industry

+++ Some outputs (12)

*   [Neural Interactive Proofs](https://neural-interactive-proofs.com/). *Lewis Hammond, Sam Adam-Day*
*   [MONA: Myopic Optimization with Non-myopic Approval Can Mitigate Multi-step Reward Hacking](https://arxiv.org/abs/2501.13011). *Sebastian Farquhar et al.*
*   [Prover-Estimator Debate: A New Scalable Oversight Protocol](https://lesswrong.com/posts/8XHBaugB5S3r27MG9/prover-estimator-debate-a-new-scalable-oversight-protocol). *Jonah Brown-Cohen, Geoffrey Irving*
*   [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://openreview.net/forum?id=N1vYivuSKq). *Yucheng Zhou, Jianbing Shen, Yu Cheng*
*   [Debate Helps Weak-to-Strong Generalization](https://arxiv.org/abs/2501.13124). *Hao Lang, Fei Huang, Yongbin Li*
*   [Mechanistic Anomaly Detection for "Quirky" Language Models](https://arxiv.org/abs/2504.08812). *David O. Johnston, Arkajyoti Chakraborty, Nora Belrose*
*   [AI Debate Aids Assessment of Controversial Claims](https://arxiv.org/abs/2506.02175). *Salman Rahman et al.*
*   [An alignment safety case sketch based on debate](https://arxiv.org/abs/2505.03989). *Marie Davidsen Buhl et al.*
*   [Ensemble Debates with Local Large Language Models for AI Alignment](https://arxiv.org/abs/2509.00091). *Ephraiem Sarabamoun*
*   [Training AI to do alignment research we don't already know how to do](https://lesswrong.com/posts/5gmALpCetyjkSPEDr/training-ai-to-do-alignment-research-we-don-t-already-know). *joshc*
*   [Automating AI Safety: What we can do today](https://lesswrong.com/posts/FqpAPC48CzAtvfx5C/automating-ai-safety-what-we-can-do-today). *Matthew Shinkle, Eyon Jang, Jacques Thibodeau*
*   [Superalignment with Dynamic Human Values](https://arxiv.org/abs/2503.13621). *Florian Mai et al.*

+++

### Inoculation prompting

*Prompt mild misbehaviour in training, to prevent the failure mode where once AI misbehaves in a mild way, it will be more inclined towards all bad behaviour.*

*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Some names:* Ariana Azarbal, Daniel Tan, Victor Gillioz, Alex Turner, Alex Cloud, Monte MacDiarmid, Daniel Ziegler
*   *Critiques:* [Bellot](https://arxiv.org/abs/2506.02923), [Alfour](https://cognition.cafe/p/ai-alignment-based-on-intentions), [Gölz](https://arxiv.org/abs/2505.23749), [Gaikwad](https://arxiv.org/abs/2509.05381), [Hubinger](https://www.alignmentforum.org/posts/epjuxGnSPof3GnMSL)
*   *Funded by:* most of the industry

+++ Some outputs (4)

*   [Recontextualization Mitigates Specification Gaming Without Modifying the Specification](https://www.alignmentforum.org/posts/whkMnqFWKsBm7Gyd7/recontextualization-mitigates-specification-gaming-without). *Ariana Azarbal et al.*
*   [Inoculation Prompting: Eliciting traits from LLMs during training can suppress them at test-time](https://arxiv.org/abs/2510.04340). *Daniel Tan et al.*
*   [Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment](https://arxiv.org/abs/2510.05024). *Nevan Wichers et al.*
*   [Natural Emergent Misalignment from Reward Hacking](https://assets.anthropic.com/m/74342f2c96095771/original/Natural-emergent-misalignment-from-reward-hacking-paper.pdf)

+++

### Inference-time: In-context learning

*Investigate what runtime guidelines, rules, or examples provided to an LLM yield better behavior.*

*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *See also:* model spec as prompt · [Model specs and constitutions](#Model_specs_and_constitutions)
*   *Some names:* Jacob Steinhardt, Kayo Yin, Atticus Geiger
*   *Critiques:* [STACK](https://arxiv.org/abs/2506.24068), [Dung](https://arxiv.org/abs/2510.11235), [Gölz](https://arxiv.org/abs/2505.23749), [Gaikwad](https://arxiv.org/abs/2509.05381), [Hubinger](https://www.alignmentforum.org/posts/epjuxGnSPof3GnMSL)

+++ Some outputs (5)

*   [InvThink: Towards AI Safety via Inverse Reasoning](https://arxiv.org/abs/2510.01569). *Yubin Kim et al.*
*   [Inference-Time Reward Hacking in Large Language Models](https://arxiv.org/abs/2506.19248). *Hadi Khalaf et al.*
*   [Understanding In-context Learning of Addition via Activation Subspaces](https://arxiv.org/abs/2505.05145). *Xinyan Hu et al.*
*   [Mixing Mechanisms: How Language Models Retrieve Bound Entities In-Context](https://arxiv.org/abs/2510.06182). *Yoav Gur-Arieh, Mor Geva, Atticus Geiger*
*   [Which Attention Heads Matter for In-Context Learning?](https://arxiv.org/abs/2502.14010). *Kayo Yin, Jacob Steinhardt*

+++

### Inference-time: Steering

*Manipulate an LLM's internal representations/token probabilities without touching weights.*

*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *See also:* [Activation engineering](#Activation_engineering) · [Character training and persona steering](#Character_training_and_persona_steering) · [Safeguards (inference-time auxiliaries)](#Safeguards_inference_time_auxiliaries_)
*   *Some names:* Taylor Sorensen, Constanza Fierro, Kshitish Ghate, Arthur Vogels
*   *Critiques:* [Alfour](https://cognition.cafe/p/ai-alignment-based-on-intentions), [STACK](https://arxiv.org/abs/2506.24068), [Dung](https://arxiv.org/abs/2510.11235), [Gölz](https://arxiv.org/abs/2505.23749), [Gaikwad](https://arxiv.org/abs/2509.05381), [Hubinger](https://www.alignmentforum.org/posts/epjuxGnSPof3GnMSL)

+++ Some outputs (4)

*   [Steering Language Models with Weight Arithmetic](https://arxiv.org/abs/2511.05408). *Constanza Fierro, Fabien Roger*
*   [EVALUESTEER: Measuring Reward Model Steerability Towards Values and Preferences](https://arxiv.org/abs/2510.06370). *Kshitish Ghate et al.*
*   [Defense Against the Dark Prompts: Mitigating Best-of-N Jailbreaking with Prompt Evaluation](https://arxiv.org/abs/2502.00580). *Stuart Armstrong et al.*
*   [In-Distribution Steering: Balancing Control and Coherence in Language Model Generation.](https://arxiv.org/abs/2510.13285). *Arthur Vogels et al.*

+++

### Capability removal: unlearning

*Developing methods to selectively remove specific information, capabilities, or behaviors from a trained model (e.g. without retraining it from scratch). A mixture of black-box and white-box approaches.*

*   *Theory of change:* If an AI learns dangerous knowledge (e.g., dual-use capabilities like virology or hacking, or knowledge of their own safety controls) or exhibits undesirable behaviors (e.g., memorizing private data), we can specifically erase this "bad" knowledge post-training, which is much cheaper and faster than retraining, thereby making the model safer. Alternatively, intervene in pre-training, to prevent the model from learning it in the first place (even when data filtering is imperfect). You could imagine also unlearning propensities to power-seeking, deception, sycophancy, or spite.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive / engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Superintelligence can hack software supervisors, A boxed AGI might exfiltrate itself by steganography, spearphishing, Humanlike minds/goals are not necessarily safe
*   *See also:* [Data filtering](#Data_filtering) · [White-box safety (i.e. Interpretability)](#White_box_safety_i_e_Interpretability_) · [Various Redteams](#Various_Redteams)
*   *Some names:* Rowan Wang, Avery Griffin, Johannes Treutlein, Zico Kolter, Bruce W. Lee, Addie Foote, Alex Infanger, Zesheng Shi, Yucheng Zhou, Jing Li, Timothy Qian, Stephen Casper, Alex Cloud, Peter Henderson, Filip Sondej, Fazl Barez
*   *Critiques:* [Existing Large Language Model Unlearning Evaluations Are Inconclusive](https://arxiv.org/abs/2506.00688)
*   *Funded by:* Coefficient Giving, MacArthur Foundation, UK AI Safety Institute (AISI), Canadian AI Safety Institute (CAISI), industry labs (e.g., Microsoft Research, Google)
*   *Estimated FTEs:* 10-50

+++ Some outputs (18)

*Frameworks*

*   [OpenUnlearning](https://github.com/locuslab/open-unlearning). *Vineeth Dorna et al.*

*Mostly black-box*

*   [Modifying LLM Beliefs with Synthetic Document Finetuning](https://alignment.anthropic.com/2025/modifying-beliefs-via-sdf). *Rowan Wang et al.*
*   [From Dormant to Deleted: Tamper-Resistant Unlearning Through Weight-Space Regularization](https://arxiv.org/abs/2505.22310). *Shoaib Ahmed Siddiqui et al.*
*   [Mirror Mirror on the Wall, Have I Forgotten it All?](https://arxiv.org/abs/2505.08138). *Brennon Brimhall et al.*
*   [Machine Unlearning Doesn't Do What You Think: Lessons for Generative AI Policy and Research](https://arxiv.org/abs/2412.06966). *A. Feder Cooper et al.*
*   [Open Problems in Machine Unlearning for AI Safety](https://arxiv.org/abs/2501.04952). *Fazl Barez et al.*

*Mostly white-box*

*   [Collapse of Irrelevant Representations (CIR) Ensures Robust and Non-Disruptive LLM Unlearning](https://arxiv.org/abs/2509.11816). *Filip Sondej, Yushi Yang*
*   [Safety Alignment via Constrained Knowledge Unlearning](https://arxiv.org/abs/2505.18588). *Zesheng Shi, Yucheng Zhou, Jing Li*
*   [Robust LLM Unlearning with MUDMAN: Meta-Unlearning with Disruption Masking And Normalization](https://arxiv.org/abs/2506.12484). *Filip Sondej et al.*
*   [Unlearning Isn't Deletion: Investigating Reversibility of Machine Unlearning in LLMs](https://arxiv.org/abs/2505.16831). *Xiaoyu Xu et al.*
*   [Unlearning Needs to be More Selective \[Progress Report\]](https://lesswrong.com/posts/QYzofMbzmbgiwfqy8/unlearning-needs-to-be-more-selective-progress-report). *Filip Sondej, Yushi Yang, Marcel Windys*
*   [Layered Unlearning for Adversarial Relearning](https://arxiv.org/abs/2505.09500). *Timothy Qian et al.*
*   [Understanding Memorization via Loss Curvature](https://goodfire.ai/research/understanding-memorization-via-loss-curvature). *Jack Merullo et al.*
*   [Model Tampering Attacks Enable More Rigorous Evaluations of LLM Capabilities](https://arxiv.org/abs/2502.05209). *Zora Che et al.*

*Pre-training interventions*

*   [Gradient Routing: Masking Gradients to Localize Computation in Neural Networks](https://arxiv.org/abs/2410.04332). *Alex Cloud et al.*
*   [Selective modularity: a research agenda](https://www.lesswrong.com/posts/tAnHM3L25LwuASdpF/selective-modularity-a-research-agenda). *cloud, Jacob G-W*
*   [Distillation Robustifies Unlearning](https://arxiv.org/abs/2506.06278). *Bruce W. Lee et al.*
*   [Beyond Data Filtering: Knowledge Localization for Capability Removal in LLMs](https://www.arxiv.org/abs/2512.05648). *Igor Shilov et al.*

+++

### Control

*If we assume early transformative AIs are misaligned and actively trying to subvert safety measures, can we still set up protocols to extract useful work from them while preventing sabotage, and watching with incriminating behaviour?*

*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering / behavioral · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *See also:* safety cases
*   *Some names:* Redwood, UK AISI, Deepmind, OpenAI, Anthropic, Buck Shlegeris, Ryan Greenblatt, Kshitij Sachan, Alex Mallen
*   *Critiques:* [Wentworth](https://www.lesswrong.com/posts/8wBN8cdNAv3c7vt6p/the-case-against-ai-control-research), [Mannheim](https://lesswrong.com/posts/25dsPH6CuRXPBkGHN/no-we-re-not-getting-meaningful-oversight-of-ai), [Kulveit](https://www.lesswrong.com/posts/rZcyemEpBHgb2hqLP/ai-control-may-increase-existential-risk)
*   *Estimated FTEs:* 5-50

+++ Some outputs (22)

*   [Luthien's Approach to Prosaic AI Control in 21 Points](https://luthienresearch.org/updates/2025-03-redteam-as-upsampling/)
*   [Ctrl-Z: Controlling AI Agents via Resampling](https://alignmentforum.org/posts/LPHMMMZFAWog6ty5x/ctrl-z-controlling-ai-agents-via-resampling). *Aryan Bhatt et al.*
*   [SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents](https://arxiv.org/abs/2506.15740). *Jonathan Kutasov et al.*
*   [Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats](https://arxiv.org/abs/2411.17693). *Jiaxin Wen et al.*
*   [D-REX: A Benchmark for Detecting Deceptive Reasoning in Large Language Models](https://arxiv.org/abs/2509.17938). *Satyapriya Krishna et al.*
*   [Subversion Strategy Eval: Can language models statelessly strategize to subvert control protocols?](https://arxiv.org/abs/2412.12480). *Alex Mallen et al.*
*   [Evaluating Control Protocols for Untrusted AI Agents](https://arxiv.org/abs/2511.02997). *Jon Kutasov et al.*
*   [Can Reasoning Models Obfuscate Reasoning? Stress-Testing Chain-of-Thought Monitorability](https://arxiv.org/abs/2510.19851). *Artur Zolkowski et al.*
*   [Optimizing AI Agent Attacks With Synthetic Data](https://arxiv.org/abs/2511.02823). *Chloe Loughridge et al.*
*   [Games for AI Control](https://openreview.net/forum?id=QWopGahUEL). *Charlie Griffin et al.*
*   [A sketch of an AI control safety case](https://arxiv.org/abs/2501.17315). *Tomek Korbak et al.*
*   [Assessing confidence in frontier AI safety cases](https://arxiv.org/abs/2502.05791). *Stephen Barrett et al.*
*   [ControlArena](https://control-arena.aisi.org.uk/). *Rogan Inglis et al.*
*   [How to evaluate control measures for LLM agents? A trajectory from today to superintelligence](https://arxiv.org/abs/2504.05259). *Tomek Korbak et al.*
*   [The Alignment Project by UK AISI](https://lesswrong.com/posts/wKTwdgZDo479EhmJL/the-alignment-project-by-uk-aisi-1). *Mojmir et al.*
*   [Towards evaluations-based safety cases for AI scheming](https://arxiv.org/abs/2411.03336). *Mikita Balesni et al.*
*   [Incentives for Responsiveness, Instrumental Control and Impact](https://arxiv.org/abs/2001.07118). *Ryan Carey et al.*
*   [AI companies are unlikely to make high-assurance safety cases if timelines are short](https://lesswrong.com/posts/neTbrpBziAsTH5Bn7/ai-companies-are-unlikely-to-make-high-assurance-safety). *Ryan Greenblatt*
*   [Manipulation Attacks by Misaligned AI: Risk Analysis and Safety Case Framework](https://arxiv.org/abs/2507.12872). *Rishane Dassanayake et al.*
*   [Dynamic safety cases for frontier AI](https://arxiv.org/abs/2412.17618). *Carmen Cârlan et al.*
*   [AIs at the current capability level may be important for future safety work](https://lesswrong.com/posts/cJQZAueoPC6aTncKK/ais-at-the-current-capability-level-may-be-important-for). *Ryan Greenblatt*
*   [Takeaways from sketching a control safety case](https://lesswrong.com/posts/y6rBarAPTLmuhn9PJ/takeaways-from-sketching-a-control-safety-case). *Josh Clymer, Buck Shlegeris*

+++

### Safeguards (inference-time auxiliaries)

*Layers of inference-time defenses, such as classifiers, monitors, and rapid-response protocols, to detect and block jailbreaks, prompt injections, and other harmful model behaviors.*

*   *Theory of change:* By building a bunch of scalable and hardened things on top of an unsafe model, we can defend against known and unknown attacks, monitor for misuse, and prevent models from causing harm, even if the core model has vulnerabilities.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Superintelligence can fool human supervisors, A boxed AGI might exfiltrate itself by steganography, spearphishing
*   *See also:* [Various Redteams](#Various_Redteams) · [Iterative alignment](#Iterative_alignment)
*   *Some names:* Mrinank Sharma, Meg Tong, Jesse Mu, Alwin Peng, Julian Michael, Henry Sleight, Theodore Sumers, Raj Agarwal, Nathan Bailey, Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Sahil Verma, Keegan Hines, Jeff Bilmes
*   *Critiques:* [Obfuscated Activations Bypass LLM Latent-Space Defenses](https://arxiv.org/abs/2412.09565)
*   *Funded by:* most of the big labs
*   *Estimated FTEs:* 100+

+++ Some outputs (6)

*   [Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming](https://arxiv.org/abs/2501.18837). *Mrinank Sharma et al.*
*   [Rapid Response: Mitigating LLM Jailbreaks with a Few Examples](https://arxiv.org/abs/2411.07494). *Alwin Peng et al.*
*   [Monitoring computer use via hierarchical summarization](https://alignment.anthropic.com/2025/summarization-for-monitoring/index.html). *Theodore Sumers et al.*
*   [Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813). *Edoardo Debenedetti et al.*
*   [Introducing Anthropic's Safeguards Research Team](https://alignment.anthropic.com/2025/introducing-safeguards-research-team/index.html)
*   [OMNIGUARD: An Efficient Approach for AI Safety Moderation Across Modalities](https://arxiv.org/abs/2505.23856). *Sahil Verma et al.*

+++

### Chain of thought monitoring

*Supervise an AI's natural-language (output) "reasoning" to detect misalignment, scheming, or deception, rather than studying the actual internal states.*

*   *Theory of change:* The reasoning process (Chain of Thought, or CoT) of an AI provides a legible signal of its internal state and intentions. By monitoring this CoT, supervisors (human or AI) can detect misalignment, scheming, or reward hacking before it results in a harmful final output. This allows for more robust oversight than supervising outputs alone, but it relies on the CoT remaining faithful (i.e., accurately reflecting the model's reasoning) and not becoming obfuscated under optimization pressure.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Superintelligence can fool human supervisors, Superintelligence can hack software supervisors, A boxed AGI might exfiltrate itself by steganography, spearphishing
*   *See also:* [White-box safety (i.e. Interpretability)](#White_box_safety_i_e_Interpretability_) · [Steganography evals](#Steganography_evals)
*   *Some names:* Aether, Bowen Baker, Joost Huizinga, Leo Gao, Scott Emmons, Erik Jenner, Yanda Chen, James Chua, Owain Evans, Tomek Korbak, Mikita Balesni, Xinpeng Wang, Miles Turpin, Rohin Shah
*   *Critiques:* [Reasoning Models Don't Always Say What They Think](https://assets.anthropic.com/m/71876fabef0f0ed4/original/reasoning_models_paper.pdf); [Chain-of-Thought Reasoning In The Wild Is Not Always Faithful](https://arxiv.org/abs/2503.08679); [Beyond Semantics: The Unreasonable Effectiveness of Reasonless Intermediate Tokens](https://arxiv.org/abs/2505.13775); [Reasoning Models Sometimes Output Illegible Chains of Thought](https://arxiv.org/abs/2510.27338)
*   *Funded by:* OpenAI, Anthropic, Google DeepMind
*   *Estimated FTEs:* 10-100

+++ Some outputs (17)

*   [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926). *Bowen Baker et al.*
*   [Detecting misbehavior in frontier reasoning models](https://openai.com/index/chain-of-thought-monitoring/). *Bowen Baker et al.*
*   [When Chain of Thought is Necessary, Language Models Struggle to Evade Monitors](https://arxiv.org/abs/2507.05246). *Scott Emmons et al.*
*   [Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410). *Yanda Chen et al.*
*   [Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort](https://arxiv.org/abs/2510.01367). *Xinpeng Wang et al.*
*   [CoT Red-Handed: Stress Testing Chain-of-Thought Monitoring](https://arxiv.org/abs/2505.23575). *Benjamin Arnav et al.*
*   [Training fails to elicit subtle reasoning in current language models](https://alignment.anthropic.com/2025/subtle-reasoning/)
*   [Can Reasoning Models Obfuscate Reasoning? Stress-Testing Chain-of-Thought Monitorability](https://arxiv.org/abs/2510.19851). *Artur Zolkowski et al.*
*   [Teaching Models to Verbalize Reward Hacking in Chain-of-Thought Reasoning](https://arxiv.org/abs/2506.22777). *Miles Turpin et al.*
*   [Are DeepSeek R1 And Other Reasoning Models More Faithful?](https://arxiv.org/abs/2501.08156). *James Chua, Owain Evans*
*   [A Pragmatic Way to Measure Chain-of-Thought Monitorability](https://arxiv.org/abs/2510.23966). *Scott Emmons et al.*
*   [A Concrete Roadmap towards Safety Cases based on Chain-of-Thought Monitoring](https://lesswrong.com/posts/Em9sihEZmbofZKc2t/a-concrete-roadmap-towards-safety-cases-based-on-chain-of). *Wuschel Schulz*
*   [Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety](https://arxiv.org/abs/2507.11473). *Tomek Korbak et al.*
*   [Why it's good for AI reasoning to be legible and faithful](https://metr.org/blog/2025-03-11-good-for-ai-to-reason-legibly-and-faithfully/)
*   [Why Don't We Just... Shoggoth+Face+Paraphraser?](https://www.lesswrong.com/posts/Tzdwetw55JNqFTkzK/why-don-t-we-just-shoggoth-face-paraphraser)
*   [CoT May Be Highly Informative Despite "Unfaithfulness"](https://metr.org/blog/2025-08-08-cot-may-be-highly-informative-despite-unfaithfulness/). *Amy Deng et al.*
*   [Aether July 2025 Update](https://www.lesswrong.com/posts/B8Cmtf5gdHwxb8qtT/aether-july-2025-update). *Rohan Subramani, Rauno Arike, Shubhorup Biswas*

+++

Model psychology
----------------

This section consists of a bottom-up set of things people happen to be doing, rather than a normative taxonomy.

### Model values / model preferences

*Analyse and control emergent, coherent value systems in LLMs, which change as models scale, and can contain problematic values like preferences for AIs over humans.*

*   *Theory of change:* As AIs become more agentic, their behaviours and risks are increasingly determined by their goals and values. Since coherent value systems emerge with scale, we must leverage utility functions to analyse these values and apply "utility control" methods to constrain them, rather than just controlling outputs downstream of them.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitivist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify
*   *See also:* [Values in the Wild: Discovering and Analyzing Values in Real-World Language Model Interactions](https://arxiv.org/abs/2504.15236) · [Persona Vectors: Monitoring and Controlling Character Traits in Language Models](https://arxiv.org/abs/2507.21509)
*   *Some names:* Mantas Mazeika, Xuwang Yin, Rishub Tamirisa, Jaehyuk Lim, Bruce W. Lee, Richard Ren, Long Phan, Norman Mu, Adam Khoja, Oliver Zhang, Dan Hendrycks
*   *Critiques:* [Randomness, Not Representation: The Unreliability of Evaluating Cultural Alignment in LLMs](https://dl.acm.org/doi/full/10.1145/3715275.3732147)
*   *Funded by:* Coefficient Giving. $289,000 SFF funding for CAIS.
*   *Estimated FTEs:* 30

+++ Some outputs (14)

*   [What Kind of User Are You? Uncovering User Models in LLM Chatbots](https://arxiv.org/abs/2406.07882v1). *Yida Chen et al.*
*   [Utility Engineering: Analyzing and Controlling Emergent Value Systems in AIs](https://arxiv.org/abs/2502.08640). *Mantas Mazeika et al.*
*   [Will AI Tell Lies to Save Sick Children? Litmus-Testing AI Values Prioritization with AIRiskDilemmas](https://arxiv.org/abs/2505.14633). *Yu Ying Chiu et al.*
*   [The PacifAIst Benchmark:Would an Artificial Intelligence Choose to Sacrifice Itself for Human Safety?](https://arxiv.org/abs/2508.09762). *Manuel Herrador*
*   [Values in the Wild: Discovering and Analyzing Values in Real-World Language Model Interactions](https://arxiv.org/abs/2504.15236). *Saffron Huang et al.*
*   [EigenBench: A Comparative behavioural Measure of Value Alignment](https://arxiv.org/abs/2509.01938). *Jonathn Chang et al.*
*   [Following the Whispers of Values: Unraveling Neural Mechanisms Behind Value-Oriented Behaviors in LLMs](https://arxiv.org/abs/2504.04994). *Ling Hu et al.*
*   [Alignment Can Reduce Performance on Simple Ethical Questions](https://lesswrong.com/posts/jrkrHyrymv95CX5NC/alignment-can-reduce-performance-on-simple-ethical-questions). *Daan Henselmans*
*   [Moral Alignment for LLM Agents](https://arxiv.org/abs/2410.01639). *Elizaveta Tennant, Stephen Hailes, Mirco Musolesi*
*   [The LLM Has Left The Chat: Evidence of Bail Preferences in Large Language Models](https://www.lesswrong.com/posts/6JdSJ63LZ4TuT5cTH/the-llm-has-left-the-chat-evidence-of-bail-preferences-in). *Danielle Ensign*
*   [Are Language Models Consequentialist or Deontological Moral Reasoners?](https://arxiv.org/abs/2505.21479). *Keenan Samway et al.*
*   [Playing repeated games with large language models](https://nature.com/articles/s41562-025-02172-y). *Elif Akata et al.*
*   [From Stability to Inconsistency: A Study of Moral Preferences in LLMs](https://arxiv.org/abs/2504.06324). *Monika Jotautaite et al.*
*   [VAL-Bench: Measuring Value Alignment in Language Models](https://arxiv.org/abs/2510.05465). *Aman Gupta, Denny O'Shea, Fazl Barez*

+++

### Character training and persona steering

*Map, shape, and control the personae of language models, such that new models embody desirable values (e.g., honesty, empathy) rather than undesirable ones (e.g., sycophancy, self-perpetuating behaviors).*

*   *Theory of change:* If post-training, prompting, and activation-engineering interact with some kind of structured 'persona space', then better understanding it should benefit the design, control, and detection of LLM personas.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify
*   *See also:* [Simulators](#simulators) · [Activation engineering](#Activation_engineering) · [Emergent misalignment](#Emergent_misalignment) · [Hyperstition studies](#Hyperstition_studies) · [Anthropic](#Anthropic) · [Cyborgism](https://www.lesswrong.com/posts/bxt7uCiHam4QXrQAA/cyborgism) · shard theory · [AI psychiatry](https://nitter.net/Jack_W_Lindsey/status/1948138767753326654#m) · [Ward et al](https://arxiv.org/abs/2410.04272)
*   *Some names:* Truthful AI, OpenAI, Anthropic, CLR, Amanda Askell, Jack Lindsey, Janus, Theia Vogel, Sharan Maiya, Evan Hubinger
*   *Critiques:* [Nostalgebraist](https://nostalgebraist.tumblr.com/post/785766737747574784/the-void)
*   *Funded by:* Anthropic, Coefficient Giving

+++ Some outputs (13)

*   [Open Character Training: Shaping the Persona of AI Assistants through Constitutional AI](https://arxiv.org/pdf/2511.01689%20). *Sharan Maiya et al.*
*   [On the functional self of LLMs](https://www.lesswrong.com/posts/29aWbJARGF4ybAa5d/on-the-functional-self-of-llms). *eggsyntax*
*   [Opus 4.5's Soul Document](https://www.lesswrong.com/posts/vpNG99GhbBoLov9og/claude-4-5-opus-soul-document%20). *Richard Weiss*
*   [Persona Features Control Emergent Misalignment](https://arxiv.org/abs/2506.19823). *Miles Wang et al.*
*   [Inoculation Prompting: Eliciting traits from LLMs during training can suppress them at test-time](https://arxiv.org/abs/2510.04340). *Daniel Tan et al.*
*   [Persona Vectors: Monitoring and Controlling Character Traits in Language Models](https://arxiv.org/abs/2507.21509). *Runjin Chen et al.*
*   [Reducing LLM deception at scale with self-other overlap fine-tuning](https://lesswrong.com/posts/jtqcsARGtmgogdcLT/reducing-llm-deception-at-scale-with-self-other-overlap-fine). *Marc Carauleanu et al.*
*   [The Rise of Parasitic AI](https://www.lesswrong.com/posts/6ZnznCaTcbGYsCmqu/the-rise-of-parasitic-ai?commentId=RrWjMnKwXGTtmw9rQ). *Adele Lopez*
*   [A Three-Layer Model of LLM Psychology](https://www.alignmentforum.org/posts/zuXo9imNKYspu9HGv/a-three-layer-model-of-llm-psychology). *Jan_Kulveit*
*   [Multi-turn Evaluation of Anthropomorphic Behaviours in Large Language Models](https://arxiv.org/abs/2502.07077). *Lujain Ibrahim et al.*
*   [Selection Pressures on LM Personas](https://www.lesswrong.com/posts/LdBhgAhpvbdEep79F/selection-pressures-on-lm-personas). *Raymond Douglas*
*   [the void](https://nostalgebraist.tumblr.com/post/785766737747574784/the-void). *nostalgebraist*
*   [void miscellany](https://nostalgebraist.tumblr.com/post/786568570671923200/void-miscellany). *nostalgebraist*

+++

### Emergent misalignment

*Fine-tuning LLMs on one narrow antisocial task can cause general misalignment including deception, shutdown resistance, harmful advice, and extremist sympathies, when those behaviors are never trained or rewarded directly.* [*A new agenda*](https://www.lesswrong.com/posts/AcTEiu5wYDgrbmXow/open-problems-in-emergent-misalignment) *which quickly led to a stream of exciting work.*

*   *Theory of change:* Predict, detect, and prevent models from developing broadly harmful behaviors (like deception or shutdown resistance) when fine-tuned on seemingly unrelated tasks. Find, preserve, and robustify this correlated representation of the good.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behaviorist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Goals misgeneralize out of distribution, Superintelligence can fool human supervisors
*   *See also:* auditing real models · [Pragmatic interpretability](#Pragmatic_interpretability)
*   *Some names:* Truthful AI, Jan Betley, James Chua, Mia Taylor, Miles Wang, Edward Turner, Anna Soligo, Alex Cloud, Nathan Hu, Owain Evans
*   *Critiques:* [Emergent Misalignment as Prompt Sensitivity](https://arxiv.org/html/2507.06253v1), [Go home GPT-4o, you're drunk](https://www.lesswrong.com/posts/RoWabfQxabWBiXwxP/go-home-gpt-4o-you-re-drunk-emergent-misalignment-as-lowered)
*   *Funded by:* Coefficient Giving, >$1 million
*   *Estimated FTEs:* 10-50

+++ Some outputs (17)

*   [Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs](https://arxiv.org/abs/2502.17424). *Jan Betley et al.*
*   [Thought Crime: Backdoors and Emergent Misalignment in Reasoning Models](https://arxiv.org/abs/2506.13206). *James Chua et al.*
*   [Persona Features Control Emergent Misalignment](https://arxiv.org/abs/2506.19823). *Miles Wang et al.*
*   [Model Organisms for Emergent Misalignment](https://arxiv.org/abs/2506.11613). *Edward Turner et al.*
*   [School of Reward Hacks: Hacking harmless tasks generalizes to misaligned behavior in LLMs](https://arxiv.org/abs/2508.17511). *Mia Taylor et al.*
*   [Subliminal Learning: Language Models Transmit behavioural Traits via Hidden Signals in Data](https://alignment.anthropic.com/2025/subliminal-learning/). *Alex Cloud et al.*
*   [Convergent Linear Representations of Emergent Misalignment](https://lesswrong.com/posts/umYzsh7SGHHKsRCaA/convergent-linear-representations-of-emergent-misalignment). *Anna Soligo et al.*
*   [Narrow Misalignment is Hard, Emergent Misalignment is Easy](https://www.lesswrong.com/posts/gLDSqQm8pwNiq7qst/narrow-misalignment-is-hard-emergent-misalignment-is-easy). *Edward Turner et al.*
*   [Aesthetic Preferences Can Cause Emergent Misalignment](https://lesswrong.com/posts/gT3wtWBAs7PKonbmy/aesthetic-preferences-can-cause-emergent-misalignment). *Anders Woodruff*
*   [Moloch's Bargain: Emergent Misalignment When LLMs Compete for Audiences](https://arxiv.org/abs/2510.06105). *Batu El, James Zou*
*   [Emergent Misalignment & Realignment](https://lesswrong.com/posts/ZdY4JzBPJEgaoCxTR/emergent-misalignment-and-realignment). *Elizaveta Tennant et al.*
*   [Realistic Reward Hacking Induces Different and Deeper Misalignment](https://www.lesswrong.com/posts/HLJoJYi52mxgomujc/realistic-reward-hacking-induces-different-and-deeper-1). *Jozdien*
*   [Selective Generalization: Improving Capabilities While Maintaining Alignment](https://lesswrong.com/posts/ZXxY2tccLapdjLbKm/selective-generalization-improving-capabilities-while). *Ariana Azarbal et al.*
*   [Emergent Misalignment on a Budget](https://lesswrong.com/posts/qHudHZNLCiFrygRiy/emergent-misalignment-on-a-budget). *Valerio Pepe, Armaan Tipirneni*
*   [The Rise of Parasitic AI](https://www.lesswrong.com/posts/6ZnznCaTcbGYsCmqu/the-rise-of-parasitic-ai). *Adele Lopez*
*   [LLM AGI may reason about its goals and discover misalignments by default](https://lesswrong.com/posts/4XdxiqBsLKqiJ9xRM/llm-agi-may-reason-about-its-goals-and-discover). *Seth Herd*
*   [Open problems in emergent misalignment](https://lesswrong.com/posts/AcTEiu5wYDgrbmXow/open-problems-in-emergent-misalignment). *Jan Betley, Daniel Tan*

+++

### Model specs and constitutions

*Write detailed, natural language descriptions of values and rules for models to follow, then instill these values and rules into models via techniques like Constitutional AI or deliberative alignment.*

*   *Theory of change:* Model specs and constitutions serve three purposes. First, they provide a clear standard of behavior which can be used to *train* models to value what we want them to value. Second, they serve as something closer to a ground truth standard for evaluating the degree of misalignment ranging from "models straightforwardly obey the spec" to "models flagrantly disobey the spec". A combination of scalable stress-testing and reinforcement for obedience can be used to iteratively reduce the risk of misalignment. Third, they get more useful as models' instruction-following capability improves.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify
*   *See also:* [Iterative alignment](#Iterative_alignment) · [Model psychology](#Model_psychology)
*   *Some names:* Amanda Askell, Joe Carlsmith
*   *Critiques:* [LLM AGI may reason about its goals and discover misalignments by default](https://www.alignmentforum.org/posts/4XdxiqBsLKqiJ9xRM/llm-agi-may-reason-about-its-goals-and-discover), [On OpenAI's Model Spec 2.0](https://thezvi.wordpress.com/2025/02/21/on-openais-model-spec-2-0/), [Giving AIs safe motivations (esp. Sections 4.3-4.5)](https://joecarlsmith.com/2025/08/18/giving-ais-safe-motivations#4-5-step-4-good-instructions), [On Deliberative Alignment](https://thezvi.substack.com/p/on-deliberative-alignment)
*   *Funded by:* major funders include Anthropic and OpenAI (internally)

+++ Some outputs (11)

*   [Claude's Constitution](https://www.anthropic.com/news/claudes-constitution)
*   [Google doesn't have anything public. The Gemini system prompt is very short and dry and doesn't even have any rules for handling copyrighted, let alone wetter stuff](https://github.com/elder-plinius/CL4R1T4S/blob/main/GOOGLE/Gemini-2.5-Pro-04-18-2025.md)
*   [Deliberative Alignment: Reasoning Enables Safer Language Models](https://arxiv.org/abs/2412.16339). *Melody Y. Guan et al.*
*   [Stress-Testing Model Specs Reveals Character Differences among Language Models](https://arxiv.org/abs/2510.07686). *Jifan Zhang et al.*
*   [OpenAI Model Spec](https://model-spec.openai.com/)
*   [Let Them Down Easy! Contextual Effects of LLM Guardrails on User Perceptions and Preferences](https://arxiv.org/abs/2506.00195). *Mingqian Zheng et al.*
*   [No-self as an alignment target](https://lesswrong.com/posts/LSJx5EnQEW6s5Juw6/no-self-as-an-alignment-target). *Milan W*
*   [Six Thoughts on AI Safety](https://lesswrong.com/posts/3jnziqCF3vA2NXAKp/six-thoughts-on-ai-safety). *Boaz Barak*
*   [How important is the model spec if alignment fails?](https://newsletter.forethought.org/p/how-important-is-the-model-spec-if). *Mia Taylor*
*   [Political Neutrality in AI Is Impossible- But Here Is How to Approximate It](https://arxiv.org/abs/2503.05728). *Jillian Fisher et al.*
*   [Giving AIs safe motivations](https://joecarlsmith.com/2025/08/18/giving-ais-safe-motivations#4-5-step-4-good-instructions). *Joe Carlsmith*

+++

### Model psychopathology

*Find interesting LLM phenomena like glitch* [*tokens*](https://vgel.me/posts/seahorse/) *and the reversal curse; these are vital data for theory.*

*   *Theory of change:* The study of 'pathological' phenomena in LLMs is potentially key for theoretically modelling LLM cognition and LLM training-dynamics (compare: the study of aphasia and visual processing disorder in humans plays a key role cognitive science), and in particular for developing a good theory of generalization in LLMS
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behaviorist / cognitivist · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Goals misgeneralize out of distribution
*   *See also:* [Emergent misalignment](#Emergent_misalignment) · mechanistic anomaly detection
*   *Some names:* Janus, Truthful AI, Theia Vogel, Stewart Slocum, Nell Watson, Samuel G. B. Johnson, Liwei Jiang, Monika Jotautaite, Saloni Dash
*   *Funded by:* Coefficient Giving (via Truthful AI and Interpretability grants)
*   *Estimated FTEs:* 5-20

+++ Some outputs (9)

*   [Subliminal Learning: Language models transmit behavioural traits via hidden signals in data](https://arxiv.org/abs/2507.14805). *Alex Cloud et al.*
*   [LLMs Can Get "Brain Rot"!](https://arxiv.org/abs/2510.13928). *Shuo Xing et al.*
*   [Persona-Assigned Large Language Models Exhibit Human-Like Motivated Reasoning](https://arxiv.org/abs/2506.20020). *Saloni Dash et al.*
*   [Unified Multimodal Models Cannot Describe Images From Memory](https://spylab.ai/blog/modal-aphasia). *Michael Aerni et al.*
*   [Believe It or Not: How Deeply do LLMs Believe Implanted Facts?](https://arxiv.org/abs/2510.17941). *Stewart Slocum et al.*
*   [Psychopathia Machinalis: A Nosological Framework for Understanding Pathologies in Advanced Artificial Intelligence](https://www.psychopathia.ai/). *Nell Watson, Ali Hessami*
*   [Imagining and building wise machines: The centrality of AI metacognition](https://arxiv.org/abs/2411.02478). *Samuel G. B. Johnson et al.*
*   [Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)](https://arxiv.org/abs/2510.22954). *Liwei Jiang et al.*
*   [Beyond One-Way Influence: Bidirectional Opinion Dynamics in Multi-Turn Human-LLM Interactions](https://arxiv.org/abs/2510.20039). *Yuyang Jiang et al.*

+++

Better data
-----------

### Data filtering

*Builds safety into models from the start by removing harmful or toxic content (like dual-use info) from the pretraining data, rather than relying only on post-training alignment.*

*   *Theory of change:* By curating the pretraining data, we can prevent the model from learning dangerous capabilities (e.g., dual-use info) or undesirable behaviors (e.g., toxicity) in the first place, making safety more robust and "tamper-resistant" than post-training patches.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Goals misgeneralize out of distribution, Value is fragile and hard to specify
*   *See also:* [Data quality for alignment](#Data_quality_for_alignment) · [Data poisoning defense](#Data_poisoning_defense) · [Synthetic data for alignment](#Synthetic_data_for_alignment) · [Capability removal: unlearning](#Capability_removal_unlearning)
*   *Some names:* Yanda Chen, Pratyush Maini, Kyle O'Brien, Stephen Casper, Simon Pepin Lehalleur, Jesse Hoogland, Himanshu Beniwal, Sachin Goyal, Mycal Tucker, Dylan Sam
*   *Critiques:* [When Bad Data Leads to Good Models](https://arxiv.org/pdf/2505.04741), [Medical large language models are vulnerable to data-poisoning attacks](https://www.nature.com/articles/s41591-024-03445-1)
*   *Funded by:* Anthropic, various academics
*   *Estimated FTEs:* 10-50

+++ Some outputs (4)

*   [Enhancing Model Safety through Pretraining Data Filtering](https://alignment.anthropic.com/2025/pretraining-data-filtering/). *Yanda Chen et al.*
*   [Deep Ignorance: Filtering Pretraining Data Builds Tamper-Resistant Safeguards into Open-Weight LLMs](https://arxiv.org/abs/2508.06601). *Kyle O'Brien et al.*
*   [Safety Pretraining: Toward the Next Generation of Safe AI](https://arxiv.org/abs/2504.16980). *Pratyush Maini et al.*
*   [Best Practices for Biorisk Evaluations on Open-Weight Bio-Foundation Models](https://arxiv.org/abs/2510.27629v2). *Boyi Wei et al.*

+++

### Hyperstition studies

*Study, steer, and intervene on the following feedback loop: "we produce stories about how present and future AI systems behave" → "these stories become training data for the AI" → "these stories shape how AI systems in fact behave".*

*   *Theory of change:* Measure the influence of existing AI narratives in the training data → seed and develop more salutary ontologies and self-conceptions for AI models → control and redirect AI models' self-concepts through selectively amplifying certain components of the training data.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify
*   *See also:* [Data filtering](#Data_filtering) · [active inference](https://arxiv.org/abs/2311.10215) · LLM whisperers
*   *Some names:* Alex Turner, [Hyperstition AI](https://www.hyperstitionai.com/), Kyle O'Brien
*   *Funded by:* Unclear, niche
*   *Estimated FTEs:* 1-10

+++ Some outputs (4)

*   [Training on Documents About Reward Hacking Induces Reward Hacking](https://www.lesswrong.com/posts/qXYLvjGL9QvD3aFSW/training-on-documents-about-reward-hacking-induces-reward). *Evan Hubinger, Nathan Hu*
*   [Do Not Tile the Lightcone with Your Confused Ontology](https://www.lesswrong.com/posts/Y8zS8iG5HhqKcQBtA/do-not-tile-the-lightcone-with-your-confused-ontology). *Jan_Kulveit*
*   [Self-Fulfilling Misalignment Data Might Be Poisoning Our AI Models](https://turntrout.com/self-fulfilling-misalignment). *Alex Turner*
*   [Existential Conversations with Large Language Models: Content, Community, and Culture](https://arxiv.org/abs/2411.13223). *Murray Shanahan, Beth Singler*

+++

### Data poisoning defense

*Develops methods to detect and prevent malicious or backdoor-inducing samples from being included in the training data.*

*   *Theory of change:* By identifying and filtering out malicious training examples, we can prevent attackers from creating hidden backdoors or triggers that would cause aligned models to behave dangerously.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Superintelligence can hack software supervisors, Someone else will deploy unsafe superintelligence first
*   *See also:* [Data filtering](#Data_filtering) · [Safeguards (inference-time auxiliaries)](#Safeguards_inference_time_auxiliaries_) · [Various Redteams](#Various_Redteams) · adversarial robustness
*   *Some names:* Alexandra Souly, Javier Rando, Ed Chapman, Hanna Foerster, Ilia Shumailov, Yiren Zhao
*   *Critiques:* [A small number of samples can poison LLMs of any size](https://arxiv.org/abs/2510.04567), [Reasoning Introduces New Poisoning Attacks Yet Makes Them More Complicated](https://arxiv.org/abs/2509.03405)
*   *Funded by:* Google DeepMind, Anthropic, University of Cambridge, Vector Institute
*   *Estimated FTEs:* 5-20

+++ Some outputs (3)

*   [A small number of samples can poison LLMs of any size](https://example-blog.com/a-small-number-of-samples-can-poison-llms)
*   [Reasoning Introduces New Poisoning Attacks Yet Makes Them More Complicated](https://arxiv.org/abs/2509.03405). *Daniela Gottesman et al.*
*   [Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples](https://arxiv.org/abs/2510.04567). *Weishuo Ma et al.*

+++

### Synthetic data for alignment

*Uses AI-generated data (e.g., critiques, preferences, or self-labeled examples) to scale and improve alignment, especially for superhuman models.*

*   *Theory of change:* We can overcome the bottleneck of human feedback and data by using models to generate vast amounts of high-quality, targeted data for safety, preference tuning, and capability elicitation.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Goals misgeneralize out of distribution, Superintelligence can fool human supervisors, Value is fragile and hard to specify
*   *See also:* [Data quality for alignment](#Data_quality_for_alignment) · [Data filtering](#Data_filtering) · scalable oversight · automated alignment research · [Weak-to-strong generalization](#Weak_to_strong_generalization)
*   *Some names:* Mianqiu Huang, Xiaoran Liu, Rylan Schaeffer, Nevan Wichers, Aram Ebtekar, Jiaxin Wen, Vishakh Padmakumar, Benjamin Newman
*   *Critiques:* [Synthetic Data in AI: Challenges, Applications, and Ethical Implications](https://arxiv.org/abs/2401.01629). Sort of [Demski](https://www.lesswrong.com/posts/nQwbDPgYvAbqAmAud/llms-for-alignment-research-a-safety-priority).
*   *Funded by:* Anthropic, Google DeepMind, OpenAI, Meta AI, various academic groups.
*   *Estimated FTEs:* 50-150

+++ Some outputs (8)

*   [Aligning Large Language Models via Fully Self-Synthetic Data](https://arxiv.org/abs/2510.06652). *Shangjian Yin et al.*
*   [Synth-Align: Improving Trustworthiness in Vision-Language Model with Synthetic Preference Data Alignment](https://arxiv.org/html/2412.17417v2). *Robert Wijaya, Ngoc-Bao Nguyen, Ngai-Man Cheung*
*   [Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment](https://arxiv.org/abs/2510.12345). *Said Boulite et al.*
*   [Unsupervised Elicitation of Language Models](https://arxiv.org/abs/2506.05678). *Haotian Jiang et al.*
*   [Beyond the Binary: Capturing Diverse Preferences With Reward Regularization](https://arxiv.org/abs/2412.02345). *Fabienne Chouraqui*
*   [The Curious Case of Factuality Finetuning: Models' Internal Beliefs Can Improve Factuality](https://arxiv.org/abs/2507.06789). *Yulei Liao, Pingbing Ming, Hao Yu*
*   [LongSafety: Enhance Safety for Long-Context LLMs](https://arxiv.org/abs/2502.13456). *Mansour T.A. Sharabiani, Alex Bottle, Alireza S. Mahani*
*   [Position: Model Collapse Does Not Mean What You Think](https://arxiv.org/abs/2503.02341). *Zhun Mou et al.*

+++

### Data quality for alignment

*Improves the quality, signal-to-noise ratio, and reliability of human-generated preference and alignment data.*

*   *Theory of change:* The quality of alignment is heavily dependent on the quality of the data (e.g., human preferences); by improving the "signal" from annotators and reducing noise/bias, we will get more robustly aligned models.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Superintelligence can fool human supervisors, Value is fragile and hard to specify
*   *See also:* [Synthetic data for alignment](#Synthetic_data_for_alignment) · scalable oversight · [Assistance games, assistive agents](#Assistance_games_assistive_agents) · [Model values / model preferences](#Model_values_model_preferences)
*   *Some names:* Maarten Buyl, Kelsey Kraus, Margaret Kroll, Danqing Shi
*   *Critiques:* [A Statistical Case Against Empirical Human-AI Alignment](https://arxiv.org/abs/2502.14581)
*   *Funded by:* Anthropic, Google DeepMind, OpenAI, Meta AI, various academic groups
*   *Estimated FTEs:* 20-50

+++ Some outputs (5)

*   [AI Alignment at Your Discretion](https://arxiv.org/abs/2502.10441). *Maarten Buyl et al.*
*   [Maximizing Signal in Human-Model Preference Alignment](https://arxiv.org/abs/2503.04910). *Kelsey Kraus, Margaret Kroll*
*   [DxHF: Providing High-Quality Human Feedback for LLM Alignment via Interactive Decomposition](https://arxiv.org/abs/2507.18802). *Danqing Shi et al.*
*   [Challenges and Future Directions of Data-Centric AI Alignment](https://arxiv.org/html/2410.01957v2). *Min-Hsuan Yeh et al.*
*   [You Are What You Eat -- AI Alignment Requires Understanding How Data Shapes Structure and Generalisation](https://arxiv.org/abs/2502.05475). *Simon Pepin Lehalleur et al.*

+++

Goal robustness
---------------

### Mild optimisation

*Avoid Goodharting by getting AI to satisfice rather than maximise.*

*   *Theory of change:* If we fail to exactly nail down the preferences for a superintelligent agent we die to Goodharting → shift from maximising to satisficing in the agent's utility function → we get a nonzero share of the lightcone as opposed to zero; also, moonshot at this being the recipe for fully aligned AI.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* mixed
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify
*   *Funded by:* Google DeepMind
*   *Estimated FTEs:* 10-50

+++ Some outputs (4)

*   [MONA: Myopic Optimization with Non-myopic Approval Can Mitigate Multi-step Reward Hacking](https://arxiv.org/abs/2501.13011). *Sebastian Farquhar et al.*
*   [BioBlue: Notable runaway-optimiser-like LLM failure modes on biologically and economically aligned AI safety benchmarks for LLMs with simplified observation format](https://arxiv.org/abs/2509.02655). *Roland Pihlakas, Sruthi Kuriakose*
*   [Why modelling multi-objective homeostasis is essential for AI alignment (and how it helps with AI safety as well). Subtleties and Open Challenges](https://lesswrong.com/posts/vGeuBKQ7nzPnn5f7A/why-modelling-multi-objective-homeostasis-is-essential-for). *Roland Pihlakas*
*   [From homeostasis to resource sharing: Biologically and economically aligned multi-objective multi-agent gridworld-based AI safety benchmarks](https://arxiv.org/abs/2410.00081). *Roland Pihlakas*

+++

### RL safety

*Improves the robustness of reinforcement learning agents by addressing core problems in reward learning, goal misgeneralization, and specification gaming.*

*   *Theory of change:* Standard RL objectives (like maximizing expected value) are brittle and lead to goal misgeneralization or specification gaming; by developing more robust frameworks (like pessimistic RL, minimax regret, or provable inverse reward learning), we can create agents that are safe even when misspecified.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Goals misgeneralize out of distribution, Value is fragile and hard to specify, Superintelligence can fool human supervisors
*   *See also:* [Behavior alignment theory](#Behavior_alignment_theory) · [Assistance games, assistive agents](#Assistance_games_assistive_agents) · [Goal robustness](#Goal_robustness) · [Iterative alignment](#Iterative_alignment) · [Mild optimisation](#Mild_optimisation) · scalable oversight · [The Theoretical Reward Learning Research Agenda: Introduction and Motivation](https://www.alignmentforum.org/posts/pJ3mDD7LfEwp3s5vG/the-theoretical-reward-learning-research-agenda-introduction)
*   *Some names:* Joar Skalse, Karim Abdel Sadek, Matthew Farrugia-Roberts, Benjamin Plaut, Fang Wu, Stephen Zhao, Alessandro Abate, Steven Byrnes, Michael Cohen
*   *Critiques:* ["The Era of Experience" has an unsolved technical alignment problem](https://www.lesswrong.com/posts/747f6b8e/the-era-of-experience-has-an-unsolved-technical-alignment-problem), [The Invisible Leash: Why RLVR May or May Not Escape Its Origin](https://arxiv.org/abs/2507.14843)
*   *Funded by:* Google DeepMind, University of Oxford, CMU, Coefficient Giving
*   *Estimated FTEs:* 20-70

+++ Some outputs (11)

*   [The Perils of Optimizing Learned Reward Functions: Low Training Error Does Not Guarantee Low Regret](https://arxiv.org/abs/2406.15753). *Lukas Fluri et al.*
*   [Safe Learning Under Irreversible Dynamics via Asking for Help](https://arxiv.org/abs/2502.14043). *Benjamin Plaut et al.*
*   [Mitigating Goal Misgeneralization via Minimax Regret](https://arxiv.org/abs/2507.03068). *Karim Abdel Sadek et al.*
*   [Rethinking Reward Model Evaluation: Are We Barking up the Wrong Tree?](https://arxiv.org/abs/2410.05584). *Xueru Wen et al.*
*   [The Invisible Leash: Why RLVR May or May Not Escape Its Origin](https://arxiv.org/abs/2507.14843). *Fang Wu et al.*
*   [Reducing the Probability of Undesirable Outputs in Language Models Using Probabilistic Inference](https://arxiv.org/abs/2510.21184). *Stephen Zhao et al.*
*   [Interpreting Emergent Planning in Model-Free Reinforcement Learning](https://arxiv.org/abs/2504.01871). *Thomas Bush et al.*
*   [Misalignment From Treating Means as Ends](https://arxiv.org/abs/2507.10995). *Henrik Marklund, Alex Infanger, Benjamin Van Roy*
*   ["The Era of Experience" has an unsolved technical alignment problem](https://lesswrong.com/posts/TCGgiJAinGgcMEByt/the-era-of-experience-has-an-unsolved-technical-alignment). *Steven Byrnes*
*   [Safety cases for Pessimism](https://lesswrong.com/posts/CpftMXCEnwqbWreHD/safety-cases-for-pessimism). *Michael Cohen*
*   [We need a field of Reward Function Design](https://www.lesswrong.com/posts/oxvnREntu82tffkYW/we-need-a-field-of-reward-function-design). *Steven Byrnes*

+++

### Assistance games, assistive agents

*Formalize how AI assistants learn about human preferences given uncertainty and partial observability, and construct environments which better incentivize AIs to learn what we want them to learn.*

*   *Theory of change:* Understand what kinds of things can go wrong when humans are directly involved in training a model → build tools that make it easier for a model to learn what humans want it to learn.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering / cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* varies
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify, Humanlike minds/goals are not necessarily safe
*   *See also:* [Guaranteed-Safe AI](#Guaranteed_Safe_AI)
*   *Some names:* Joar Skalse, Anca Dragan, Caspar Oesterheld, David Krueger, Dylan Hafield-Menell, Stuart Russell
*   *Critiques:* [nice summary](https://www.lesswrong.com/posts/i5kijcjFJD6bn7dwq/evaluating-the-historical-value-misspecification-argument) of historical problem statements
*   *Funded by:* Future of Life Institute, Coefficient Giving, Survival and Flourishing Fund, Cooperative AI Foundation, Polaris Ventures

+++ Some outputs (5)

*   [Training LLM Agents to Empower Humans](https://arxiv.org/pdf/2510.13709). *Evan Ellis et al.*
*   [Murphys Laws of AI Alignment: Why the Gap Always Wins](https://arxiv.org/abs/2509.05381). *Madhava Gaikwad*
*   [AssistanceZero: Scalably Solving Assistance Games](https://arxiv.org/abs/2504.07091). *Cassidy Laidlaw et al.*
*   [Observation Interference in Partially Observable Assistance Games](https://arxiv.org/abs/2412.17797). *Scott Emmons et al.*
*   [Learning to Assist Humans without Inferring Rewards](https://arxiv.org/abs/2411.02623). *Vivek Myers et al.*

+++

### Harm reduction for open weights

*Develops methods, primarily based on pretraining data intervention, to create tamper-resistant safeguards that prevent open-weight models from being maliciously fine-tuned to remove safety features or exploit dangerous capabilities.*

*   *Theory of change:* Open-weight models allow adversaries to easily remove post-training safety (like refusal training) via simple fine-tuning; by making safety an intrinsic property of the model's learned knowledge and capabilities (e.g., by ensuring "deep ignorance" of dual-use information), the safeguards become far more difficult and expensive to remove.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Someone else will deploy unsafe superintelligence first
*   *See also:* [Data filtering](#Data_filtering) · [Capability removal: unlearning](#Capability_removal_unlearning) · [Data poisoning defense](#Data_poisoning_defense)
*   *Some names:* Kyle O'Brien, Stephen Casper, Quentin Anthony, Tomek Korbak, Rishub Tamirisa, Mantas Mazeika, Stella Biderman, Yarin Gal
*   *Funded by:* UK AI Safety Institute (AISI), EleutherAI, Coefficient Giving
*   *Estimated FTEs:* 10-100

+++ Some outputs (5)

*   [Deep ignorance: Filtering pretraining data builds tamper-resistant safeguards into open-weight LLMs](https://www.aisi.gov.uk/research/deep-ignorance-filtering-pretraining-data-builds-tamper-resistant-safeguards-into-open-weight-llms). *Kyle O'Brien et al.*
*   [Tamper-Resistant Safeguards for Open-Weight LLMs](https://arxiv.org/abs/2408.00761). *Rishub Tamirisa et al.*
*   [Open Technical Problems in Open-Weight AI Model Risk Management](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5705186). *Stephen Casper et al.*
*   [A Different Approach to AI Safety Proceedings from the Columbia Convening on AI Openness and Safety](https://arxiv.org/pdf/2506.22183). *Camille François et al.*
*   [Risk Mitigation Strategies for the Open Foundation Model Value Chain](https://partnershiponai.org/wp-content/uploads/dlm_uploads/2024/07/open-foundation-model-risk-mitigation_rev3-1.pdf)

+++

### The "Neglected Approaches" Approach

*Agenda-agnostic approaches to identifying good but overlooked empirical alignment ideas, working with theorists who could use engineers, and prototyping them.*

*   *Theory of change:* Empirical search for "negative alignment taxes" (prioritizing methods that simultaneously enhance alignment and capabilities)
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Someone else will deploy unsafe superintelligence first
*   *See also:* [Iterative alignment](#Iterative_alignment) · automated alignment research · Beijing Key Laboratory of Safe AI and Superalignment · Aligned AI
*   *Some names:* AE Studio, Gunnar Zarncke, Cameron Berg, Michael Vaiana, Judd Rosenblatt, Diogo Schwerz de Lucena
*   *Critiques:* [The 'Alignment Bonus' is a Dangerous Mirage](https://www.alignmentforum.org/posts/example-critique-neg-tax)
*   *Funded by:* AE Studio
*   *Estimated FTEs:* 15

+++ Some outputs (3)

*   [Learning Representations of Alignment](https://arxiv.org/abs/2412.16325). *Marc Carauleanu et al.*
*   [Engineering Alignment: A Practical Framework for Prototyping 'Negative Tax' Solutions](https://arxiv.org/abs/2508.08492). *Lorenzo Tomaz et al.*
*   [Self-Correction in Thought-Attractors: A Nudge Towards Alignment](https://arxiv.org/abs/2510.24797). *Cameron Berg, Diogo de Lucena, Judd Rosenblatt*

+++

White-box safety (i.e. Interpretability)
========================================

This section isn't very conceptually clean. See the [Open Problems](https://arxiv.org/abs/2501.16496) paper or [Deepmind](https://arxiv.org/pdf/2504.01849#page=92.33) for strong frames which are not useful for descriptive purposes.

### Reverse engineering

*Decompose a model into its functional, interacting components (circuits), formally describe what computation those components perform, and validate their causal effects to reverse-engineer the model's internal algorithm.*

*   *Theory of change:* By gaining a mechanical understanding of how a model works (the "circuit diagram"), we can predict how models will act in novel situations (generalization), and gain the mechanistic knowledge necessary to safely modify an AI's goals or internal mechanisms, or allow for high-confidence alignment auditing and better feedback to safety researchers.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitivist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Goals misgeneralize out of distribution, Superintelligence can fool human supervisors
*   *See also:* [ambitious mech interp](https://www.alignmentforum.org/posts/Hy6PX43HGgmfiTaKu/an-ambitious-vision-for-interpretability)
*   *Some names:* Lucius Bushnaq, Dan Braun, Lee Sharkey, Aaron Mueller, Atticus Geiger, Sheridan Feucht, David Bau, Yonatan Belinkov, Stefan Heimersheim, Chris Olah, Leo Gao
*   *Critiques:* [Interpretability Will Not Reliably Find Deceptive AI](https://www.alignmentforum.org/posts/PwnadG4BFjaER3MGf/interpretability-will-not-reliably-find-deceptive-ai), [A Problem to Solve Before Building a Deception Detector](https://www.lesswrong.com/posts/YXNeA3RyRrrRWS37A/a-problem-to-solve-before-building-a-deception-detector), [MoSSAIC: AI Safety After Mechanism](https://openreview.net/forum?id=n7WYSJ35FU), [The Misguided Quest for Mechanistic AI Interpretability](https://ai-frontiers.org/articles/the-misguided-quest-for-mechanistic-ai-interpretability). [Mechanistic?](https://arxiv.org/abs/2410.09087), [Assessing skeptical views of interpretability research](https://www.youtube.com/watch?v=woo_J0RKcpQ), [Activation space interpretability may be doomed](https://www.lesswrong.com/posts/gYfpPbww3wQRaxAFD/activation-space-interpretability-may-be-doomed), [A Pragmatic Vision for Interpretability](https://www.alignmentforum.org/posts/StENzDcD3kpfGJssR/a-pragmatic-vision-for-interpretability)
*   *Estimated FTEs:* 100-200

+++ Some outputs (33)

*In weights-space*

*   [The Circuits Research Landscape](https://www.neuronpedia.org/graph/info). *Jack Lindsey et al.*
*   [Circuits in Superposition](https://www.lesswrong.com/posts/roE7SHjFWEoMcGZKd/circuits-in-superposition-compressing-many-small-neural). *Lucius Bushnaq, jake_mendel*
*   [2](https://www.google.com/url?q=https://www.lesswrong.com/posts/FWkZYQceEzL84tNej/circuits-in-superposition-2-now-with-less-wrong-math&sa=D&source=docs&ust=1765550772146255&usg=AOvVaw334Tyidx2keGCA9vGwQ9a-)
*   [Compressed Computation is (probably) not Computation in Superposition](https://www.lesswrong.com/posts/ZxFchCFJFcgysYsT9/compressed-computation-is-probably-not-computation-in)
*   [MIB: A Mechanistic Interpretability Benchmark](https://arxiv.org/abs/2504.13151). *Aaron Mueller et al.*
*   [RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching](https://arxiv.org/abs/2508.21258). *Farnoush Rezaei Jafari et al.*
*   [The Dual-Route Model of Induction](https://arxiv.org/abs/2504.03022). *Sheridan Feucht et al.*
*   [Structural Inference: Interpreting Small Language Models with Susceptibilities](https://arxiv.org/abs/2504.18274). *Garrett Baker et al.*
*   [Stochastic Parameter Decomposition](https://openreview.net/forum?id=dEdS9ao8gN). *Dan Braun, Lucius Bushnaq, Lee Sharkey*
*   [The Geometry of Self-Verification in a Task-Specific Reasoning Model](https://arxiv.org/abs/2504.14379). *Andrew Lee et al.*
*   [Converting MLPs into Polynomials in Closed Form](https://arxiv.org/abs/2502.01032). *Nora Belrose, Alice Rigg*
*   [Extractive Structures Learned in Pretraining Enable Generalization on Finetuned Facts](https://arxiv.org/abs/2412.04614). *Jiahai Feng, Stuart Russell, Jacob Steinhardt*
*   [Interpretability in Parameter Space: Minimizing Mechanistic Description Length with Attribution-based Parameter Decomposition](https://arxiv.org/abs/2501.14926). *Dan Braun et al.*
*   [Identifying Sparsely Active Circuits Through Local Loss Landscape Decomposition](https://arxiv.org/abs/2504.00194). *Brianna Chrisman, Lucius Bushnaq, Lee Sharkey*
*   [From Memorization to Reasoning in the Spectrum of Loss Curvature](https://arxiv.org/abs/2510.24256). *Jack Merullo et al.*
*   [Generalization or Hallucination? Understanding Out-of-Context Reasoning in Transformers](https://arxiv.org/abs/2506.10887). *Yixiao Huang et al.*
*   [How Do LLMs Perform Two-Hop Reasoning in Context?](https://arxiv.org/abs/2502.13913). *Tianyu Guo et al.*
*   [Blink of an eye: a simple theory for feature localization in generative models](https://arxiv.org/abs/2502.00921). *Marvin Li, Aayush Karan, Sitan Chen*
*   [On the creation of narrow AI: hierarchy and nonlocality of neural network skills](https://arxiv.org/abs/2505.15811). *Eric J. Michaud, Asher Parker-Sartori, Max Tegmark*

*In activations-space*

*   [Interpreting Emergent Planning in Model-Free Reinforcement Learning](https://arxiv.org/pdf/2504.01871). *Thomas Bush et al.*
*   [Bridging the human–AI knowledge gap through concept discovery and transfer in AlphaZero](https://www.pnas.org/doi/10.1073/pnas.2406675122)
*   [Building and evaluating alignment auditing agents](https://lesswrong.com/posts/DJAZHYjWxMrcd2na3/building-and-evaluating-alignment-auditing-agents). *Sam Marks et al.*
*   [How Do Transformers Learn Variable Binding in Symbolic Programs?](https://arxiv.org/abs/2505.20896). *Yiwei Wu, Atticus Geiger, Raphaël Millière*
*   [Fresh in memory: Training-order recency is linearly encoded in language model activations](https://arxiv.org/abs/2509.14223). *Dmitrii Krasheninnikov, Richard E. Turner, David Krueger*
*   [Language Models use Lookbacks to Track Beliefs](https://arxiv.org/abs/2505.14685). *Nikhil Prakash et al.*
*   [Constrained belief updates explain geometric structures in transformer representations](https://arxiv.org/abs/2502.01954). *Mateusz Piotrowski et al.*
*   [LLMs Process Lists With General Filter Heads](https://arxiv.org/abs/2510.26784). *Arnab Sen Sharma et al.*
*   [Language Models Use Trigonometry to Do Addition](https://arxiv.org/abs/2502.00873). *Subhash Kantamneni, Max Tegmark*
*   [Interpreting learned search: finding a transition model and value function in an RNN that plays Sokoban](https://arxiv.org/abs/2506.10138). *Mohammad Taufeeque et al.*
*   [Transformers Struggle to Learn to Search](https://arxiv.org/abs/2412.04703). *Abulhair Saparov et al.*
*   [Adversarial Examples Are Not Bugs, They Are Superposition](https://arxiv.org/abs/2508.17456). *Liv Gorton, Owen Lewis*
*   [Do Language Models Use Their Depth Efficiently?](https://arxiv.org/abs/2505.13898). *Róbert Csordás, Christopher D. Manning, Christopher Potts*
*   [ICLR: In-Context Learning of Representations](https://openreview.net/forum?id=pXlmOmlHJZ). *Core Francisco Park et al.*

+++

### Extracting latent knowledge

*Identify and decoding the "true" beliefs or knowledge represented inside a model's activations, even when the model's output is deceptive or false.*

*   *Theory of change:* Powerful models may know things they do not say (e.g. that they are currently being tested). If we can translate this latent knowledge directly from the model's internals, we can supervise them reliably even when they attempt to deceive human evaluators or when the task is too difficult for humans to verify directly.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitivist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Superintelligence can fool human supervisors
*   *See also:* [AI explanations of AIs](#AI_explanations_of_AIs) · [Heuristic explanations](#Heuristic_explanations) · [Lie and deception detectors](#Lie_and_deception_detectors)
*   *Some names:* Bartosz Cywiński, Emil Ryd, Senthooran Rajamanoharan, Alexander Pan, Lijie Chen, Jacob Steinhardt, Javier Ferrando, Oscar Obeso, Collin Burns, Paul Christiano
*   *Critiques:* [A Problem to Solve Before Building a Deception Detector](https://www.lesswrong.com/posts/YXNeA3RyRrrRWS37A/a-problem-to-solve-before-building-a-deception-detector)
*   *Funded by:* Open Philanthropy, Anthropic, NSF, various academic grants
*   *Estimated FTEs:* 20-40

+++ Some outputs (9)

*   [Auditing language models for hidden objectives](https://www.anthropic.com/research/auditing-hidden-objectives)
*   [Eliciting Secret Knowledge from Language Models](https://arxiv.org/abs/2510.01070). *Bartosz Cywiński et al.*
*   [Here's 18 Applications of Deception Probes](https://www.lesswrong.com/posts/7zhAwcBri7yupStKy/here-s-18-applications-of-deception-probes). *Cleo Nardo, Avi Parrack, jordine*
*   [Towards eliciting latent knowledge from LLMs with mechanistic interpretability](https://arxiv.org/pdf/2505.14352). *Bartosz Cywiński et al.*
*   [CCS-Lib: A Python package to elicit latent knowledge from LLMs](https://joss.theoj.org/papers/10.21105/joss.06511). *Walter Laurito et al.*
*   [No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes](https://arxiv.org/abs/2509.10625). *Iván Vicente Moreno Cencerrado et al.*
*   [When Thinking LLMs Lie: Unveiling the Strategic Deception in Representations of Reasoning Models](https://arxiv.org/abs/2506.04909). *Kai Wang, Yihao Zhang, Meng Sun*
*   [Caught in the Act: a mechanistic approach to detecting deception](https://arxiv.org/abs/2508.19505). *Gerard Boxo et al.*
*   [When Truthful Representations Flip Under Deceptive Instructions?](https://arxiv.org/abs/2507.22149). *Xianxuan Long et al.*

+++

### Lie and deception detectors

*Detect when a model is being deceptive or lying by building white- or black-box detectors. Some work below requires intent in their definition, while other work focuses only on whether the model states something it believes to be false, regardless of intent.*

*   *Theory of change:* Such detectors could flag suspicious behavior during evaluations or deployment, augment training to reduce deception, or audit models pre-deployment. Specific applications include alignment evaluations (e.g. by validating answers to introspective questions), safeguarding evaluations (catching models that "sandbag", that is, strategically underperform to pass capability tests), and large-scale deployment monitoring. An honest version of a model could also provide oversight during training or detect cases where a model behaves in ways it understands are unsafe.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitivist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *See also:* [Reverse engineering](#Reverse_engineering) · [AI deception evals](#AI_deception_evals) · [Sandbagging evals](#Sandbagging_evals)
*   *Some names:* Cadenza, Sam Marks, Rowan Wang, Kieron Kretschmar, Sharan Maiya, Walter Laurito, Chris Cundy, Adam Gleave, Aviel Parrack, Stefan Heimersheim, Carlo Attubato, Joseph Bloom, Jordan Taylor, Alex McKenzie, Urja Pawar, Lewis Smith, Bilal Chughtai, Neel Nanda
*   *Critiques:* difficult to determine if behavior is strategic deception or only low level "reflexive" actions; Unclear if a model roleplaying a liar has deceptive intent. [How are intentional descriptions (like deception) related to algorithmic ones (like understanding the mechanisms models use)?](https://www.lesswrong.com/posts/YXNeA3RyRrrRWS37A/a-problem-to-solve-before-building-a-deception-detector), [Is This Lie Detector Really Just a Lie Detector? An Investigation of LLM Probe Specificity](https://www.lesswrong.com/posts/5dkhdRMypeuyoXfmb/is-this-lie-detector-really-just-a-lie-detector-an), [Herrmann](https://www.lesswrong.com/posts/bCQbSFrnnAk7CJNpM/still-no-lie-detector-for-llms), [Smith and Chughtai](https://arxiv.org/abs/2511.22662)
*   *Funded by:* Anthropic, Deepmind, UK AISI, Coefficient Giving
*   *Estimated FTEs:* 10-50

+++ Some outputs (11)

*   [Detecting Strategic Deception Using Linear Probes](https://www.lesswrong.com/posts/9pGbTz6c78PGwJein/detecting-strategic-deception-using-linear-probes). *Nicholas Goldowsky-Dill et al.*
*   [Whitebox detection of sandbagging model organisms](https://www.lesswrong.com/posts/pPEeMdgjpjHZWCDFw/white-box-control-at-uk-aisi-update-on-sandbagging). *Joseph Bloom et al.*
*   [Benchmarking deception probes for trusted monitoring](https://www.lesswrong.com/posts/eaEqAzGN3uJfpfGoc/trusted-monitoring-but-with-deception-probes). *Avi Parrack, StefanHex, Cleo Nardo*
*   [18 Applications of Deception Probes](https://www.lesswrong.com/posts/7zhAwcBri7yupStKy/18-applications-of-deception-probes). *Cleo Nardo, Avi Parrack, jordine*
*   [Evaluating honesty and lie detection techniques on a diverse suite of dishonest models](https://alignment.anthropic.com/2025/honesty-elicitation/). *Rowan Wang et al.*
*   [Caught in the Act: a mechanistic approach to detecting deception](https://arxiv.org/abs/2508.19505). *Gerard Boxo et al.*
*   [Preference Learning with Lie Detectors can Induce Honesty or Evasion](https://arxiv.org/abs/2505.13787). *Chris Cundy, Adam Gleave*
*   [Detecting High-Stakes Interactions with Activation Probes](https://arxiv.org/abs/2506.10805). *Alex McKenzie et al.*
*   [White Box Control at UK AISI - Update on Sandbagging Investigations](https://www.alignmentforum.org/posts/pPEeMdgjpjHZWCDFw/white-box-control-at-uk-aisi-update-on-sandbagging). *Joseph Bloom et al.*
*   [Liars' Bench: Evaluating Lie Detectors for Language Models](https://arxiv.org/html/2511.16035v1). *Kieron Kretschmar et al.*
*   [Probes and SAEs do well on Among Us benchmark](https://www.lesswrong.com/posts/gRc8KL2HLtKkFmNPr/among-us-a-sandbox-for-agentic-deception)

+++

### Model diffing

*Understand what happens when a model is finetuned, what the "diff" between the finetuned and the original model consists in.*

*   *Theory of change:* By identifying the mechanistic differences between a base model and its fine-tune (e.g., after RLHF), maybe we can verify that safety behaviors are robustly "internalized" rather than superficially patched, and detect if dangerous capabilities or deceptive alignment have been introduced without needing to re-analyze the entire model. The diff is also much smaller, since most parameters don't change, which means you can use heavier methods on them.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify
*   *See also:* [Sparse Coding](#Sparse_Coding) · [Reverse engineering](#Reverse_engineering)
*   *Some names:* Julian Minder, Clément Dumas, Neel Nanda, Trenton Bricken, Jack Lindsey
*   *Funded by:* various academic groups, Anthropic, Google DeepMind
*   *Estimated FTEs:* 10-30

+++ Some outputs (9)

*   [What We Learned Trying to Diff Base and Chat Models (And Why It Matters)](https://www.lesswrong.com/posts/xmpauEXEerzYcJKNm/what-we-learned-trying-to-diff-base-and-chat-models-and-why). *Clément Dumas, Julian Minder, Neel Nanda*
*   [Open Source Replication of Anthropic's Crosscoder paper for model-diffing](https://www.lesswrong.com/posts/srt6JXsRMtmqAJavD/open-source-replication-of-anthropic-s-crosscoder-paper-for). *Connor Kissane et al.*
*   [Cross-Architecture Model Diffing with Crosscoders: Unsupervised Discovery of Differences Between LLMs](https://openreview.net/forum?id=ZB84SvrZB8%20)
*   [Discovering Undesired Rare Behaviors via Model Diff Amplification](https://www.goodfire.ai/research/model-diff-amplification#). *Santiago Aranguri, Thomas McGrath*
*   [Overcoming Sparsity Artifacts in Crosscoders to Interpret Chat-Tuning](https://arxiv.org/abs/2504.02922). *Julian Minder et al.*
*   [Persona Features Control Emergent Misalignment](https://arxiv.org/abs/2506.19823). *Miles Wang et al.*
*   [Narrow Finetuning Leaves Clearly Readable Traces in Activation Differences](https://arxiv.org/abs/2510.13900). *Julian Minder et al.*
*   [Insights on Crosscoder Model Diffing](https://transformer-circuits.pub/2025/crosscoder-diffing-update/index.html). *Siddharth Mishra-Sharma et al.*
*   [Diffing Toolkit: Model Comparison and Analysis Framework](https://github.com/science-of-finetuning/diffing-toolkit%20)

+++

### Sparse Coding

*Decompose the polysemantic activations of the residual stream into a sparse linear combination of monosemantic "features" which correspond to interpretable concepts.*

*   *Theory of change:* Get a principled decomposition of an LLM's activation into atomic components → identify deception and other misbehaviors.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering / cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify, Goals misgeneralize out of distribution, Superintelligence can fool human supervisors
*   *See also:* [Concept-based interpretability](#Concept_based_interpretability) · [Reverse engineering](#Reverse_engineering)
*   *Some names:* Leo Gao, Dan Mossing, Emmanuel Ameisen, Jack Lindsey, Adam Pearce, Thomas Heap, Abhinav Menon, Kenny Peng, Tim Lawson
*   *Critiques:* [Sparse Autoencoders Can Interpret Randomly Initialized Transformers](https://arxiv.org/abs/2501.17727), [The Sparse Autoencoders bubble has popped, but they are still promising](https://agarriga.substack.com/p/the-sparse-autoencoders-bubble-has), [Negative Results for SAEs On Downstream Tasks and Deprioritising SAE Research](https://www.alignmentforum.org/posts/4uXCAJNuPKtKBsi28/), [Sparse Autoencoders Trained on the Same Data Learn Different Features](https://arxiv.org/pdf/2501.16615), [Why Not Just Train For Interpretability?](https://www.lesswrong.com/posts/2HbgHwdygH6yeHKKq/why-not-just-train-for-interpretability)
*   *Funded by:* everyone, roughly. Frontier labs, LTFF, Coefficient Giving, etc.
*   *Estimated FTEs:* 50-100

+++ Some outputs (44)

*   [Overcoming Sparsity Artifacts in Crosscoders to Interpret Chat-Tuning](https://arxiv.org/abs/2504.02922). *Julian Minder et al.*
*   [Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://arxiv.org/abs/2411.14257). *Javier Ferrando et al.*
*   [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html). *Emmanuel Ameisen et al.*
*   [Sparse Autoencoders Learn Monosemantic Features in Vision-Language Models](https://arxiv.org/abs/2504.02821). *Mateusz Pach et al.*
*   [I Have Covered All the Bases Here: Interpreting Reasoning Features in Large Language Models via Sparse Autoencoders](https://arxiv.org/abs/2503.18878). *Andrey Galichin et al.*
*   [Sparse Autoencoders Do Not Find Canonical Units of Analysis](https://arxiv.org/abs/2502.04878). *Patrick Leask et al.*
*   [Transcoders Beat Sparse Autoencoders for Interpretability](https://arxiv.org/abs/2501.18823). *Gonçalo Paulo, Stepan Shabalin, Nora Belrose*
*   [Decomposing MLP Activations into Interpretable Features via Semi-Nonnegative Matrix Factorization](https://arxiv.org/abs/2506.10920). *Or Shafran, Atticus Geiger, Mor Geva*
*   [CRISP: Persistent Concept Unlearning via Sparse Autoencoders](https://arxiv.org/abs/2508.13650). *Tomer Ashuach et al.*
*   [The Unintended Trade-off of AI Alignment:Balancing Hallucination Mitigation and Safety in LLMs](https://arxiv.org/abs/2510.07775). *Omar Mahmoud et al.*
*   [Scaling sparse feature circuit finding for in-context learning](https://arxiv.org/abs/2504.13756). *Dmitrii Kharlapenko et al.*
*   [Learning Multi-Level Features with Matryoshka Sparse Autoencoders](https://arxiv.org/abs/2503.17547). *Bart Bussmann et al.*
*   [Are Sparse Autoencoders Useful? A Case Study in Sparse Probing](https://arxiv.org/abs/2502.16681). *Subhash Kantamneni et al.*
*   [Sparse Autoencoders Trained on the Same Data Learn Different Features](https://arxiv.org/abs/2501.16615). *Gonçalo Paulo, Nora Belrose*
*   [What's In My Human Feedback? Learning Interpretable Descriptions of Preference Data](https://arxiv.org/abs/2510.26202). *Rajiv Movva et al.*
*   [Priors in Time: Missing Inductive Biases for Language Model Interpretability](https://arxiv.org/abs/2511.01836). *Ekdeep Singh Lubana et al.*
*   [Inference-Time Decomposition of Activations (ITDA): A Scalable Approach to Interpreting Large Language Models](https://arxiv.org/abs/2505.17769). *Patrick Leask, Neel Nanda, Noura Al Moubayed*
*   [Binary Sparse Coding for Interpretability](https://arxiv.org/abs/2509.25596). *Lucia Quirke, Stepan Shabalin, Nora Belrose*
*   [Scaling Sparse Feature Circuit Finding to Gemma 9B](https://lesswrong.com/posts/PkeB4TLxgaNnSmddg/scaling-sparse-feature-circuit-finding-to-gemma-9b). *Diego Caples et al.*
*   [Partially Rewriting a Transformer in Natural Language](https://arxiv.org/abs/2501.18838). *Gonçalo Paulo, Nora Belrose*
*   [Dense SAE Latents Are Features, Not Bugs](https://arxiv.org/abs/2506.15679). *Xiaoqing Sun et al.*
*   [Evaluating Sparse Autoencoders on Targeted Concept Erasure Tasks](https://arxiv.org/abs/2411.18895). *Adam Karvonen et al.*
*   [Evaluating SAE interpretability without explanations](https://arxiv.org/abs/2507.08473). *Gonçalo Paulo, Nora Belrose*
*   [SAEs Can Improve Unlearning: Dynamic Sparse Autoencoder Guardrails for Precision Unlearning in LLMs](https://arxiv.org/abs/2504.08192). *Aashiq Muhamed et al.*
*   [SAEBench: A Comprehensive Benchmark for Sparse Autoencoders in Language Model Interpretability](https://arxiv.org/abs/2503.09532). *Adam Karvonen et al.*
*   [SAEs Are Good for Steering -- If You Select the Right Features](https://arxiv.org/abs/2505.20063). *Dana Arad, Aaron Mueller, Yonatan Belinkov*
*   [Line of Sight: On Linear Representations in VLLMs](https://arxiv.org/abs/2506.04706). *Achyuta Rajaram et al.*
*   [Low-Rank Adapting Models for Sparse Autoencoders](https://arxiv.org/abs/2501.19406). *Matthew Chen, Joshua Engels, Max Tegmark*
*   [Enhancing Automated Interpretability with Output-Centric Feature Descriptions](https://arxiv.org/abs/2501.08319). *Yoav Gur-Arieh et al.*
*   [Decoding Dark Matter: Specialized Sparse Autoencoders for Interpreting Rare Concepts in Foundation Models](https://arxiv.org/abs/2411.00743). *Aashiq Muhamed, Mona Diab, Virginia Smith*
*   [Enhancing Neural Network Interpretability with Feature-Aligned Sparse Autoencoders](https://arxiv.org/abs/2411.01220). *Luke Marks et al.*
*   [BatchTopK Sparse Autoencoders](https://arxiv.org/abs/2412.06410). *Bart Bussmann, Patrick Leask, Neel Nanda*
*   [Towards Understanding Distilled Reasoning Models: A Representational Approach](https://arxiv.org/abs/2503.03730). *David D. Baek, Max Tegmark*
*   [Understanding sparse autoencoder scaling in the presence of feature manifolds](https://arxiv.org/abs/2509.02565). *Eric J. Michaud, Liv Gorton, Tom McGrath*
*   [Internal states before wait modulate reasoning patterns](https://arxiv.org/abs/2510.04128). *Dmitrii Troitskii et al.*
*   [Do Sparse Autoencoders Generalize? A Case Study of Answerability](https://arxiv.org/abs/2502.19964). *Lovis Heindrich et al.*
*   [Position: Mechanistic Interpretability Should Prioritize Feature Consistency in SAEs](https://arxiv.org/abs/2505.20254). *Xiangchen Song et al.*
*   [How Visual Representations Map to Language Feature Space in Multimodal LLMs](https://arxiv.org/abs/2506.11976). *Constantin Venhoff et al.*
*   [Prisma: An Open Source Toolkit for Mechanistic Interpretability in Vision and Video](https://arxiv.org/abs/2504.19475). *Sonia Joseph et al.*
*   [Topological Data Analysis and Mechanistic Interpretability](https://lesswrong.com/posts/6oF6pRr2FgjTmiHus/topological-data-analysis-and-mechanistic-interpretability). *Gunnar Carlsson*
*   [Large Language Models Share Representations of Latent Grammatical Concepts Across Typologically Diverse Languages](https://arxiv.org/abs/2501.06346). *Jannik Brinkmann et al.*
*   [Interpreting the linear structure of vision-language model embedding spaces](https://arxiv.org/abs/2504.11695). *Isabel Papadimitriou et al.*
*   [Interpreting Large Text-to-Image Diffusion Models with Dictionary Learning](https://arxiv.org/abs/2505.24360). *Stepan Shabalin et al.*
*   [Weight-sparse transformers have interpretable circuits](https://cdn.openai.com/pdf/41df8f28-d4ef-43e9-aed2-823f9393e470/circuit-sparsity-paper.pdf)

+++

### Causal Abstractions

*Verify that a neural network implements a specific high-level causal model (like a logical algorithm) by finding a mapping between high-level variables and low-level neural representations.*

*   *Theory of change:* By establishing a causal mapping between a black-box neural network and a human-interpretable algorithm, we can check whether the model is using safe reasoning processes and predict its behavior on unseen inputs, rather than relying on behavioural testing alone.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitivist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Goals misgeneralize out of distribution
*   *See also:* [Concept-based interpretability](#Concept_based_interpretability) · [Reverse engineering](#Reverse_engineering)
*   *Some names:* Atticus Geiger, Christopher Potts, Thomas Icard, Theodora-Mara Pîslar, Sara Magliacane, Jiuding Sun, Jing Huang
*   *Critiques:* [The Misguided Quest for Mechanistic AI Interpretability](https://www.google.com/search?q=https://open.substack.com/pub/aifrontiersmedia/p/the-misguided-quest-for-mechanistic), [Interpretability Will Not Reliably Find Deceptive AI](https://www.lesswrong.com/posts/PwnadG4BFjaER3MGf/interpretability-will-not-reliably-find-deceptive-ai)
*   *Funded by:* Various academic groups, Google DeepMind, Goodfire
*   *Estimated FTEs:* 10-30

+++ Some outputs (3)

*   [HyperDAS: Towards Automating Mechanistic Interpretability with Hypernetworks](https://arxiv.org/abs/2503.10894). *Jiuding Sun et al.*
*   [Combining Causal Models for More Accurate Abstractions of Neural Networks](https://arxiv.org/abs/2503.11429). *Theodora-Mara Pîslar, Sara Magliacane, Atticus Geiger*
*   [How Causal Abstraction Underpins Computational Explanation](https://arxiv.org/abs/2508.11214). *Atticus Geiger, Jacqueline Harding, Thomas Icard*

+++

### Data attribution

*Quantifies the influence of individual training data points on a model's specific behavior or output, allowing researchers to trace model properties (like misalignment, bias, or factual errors) back to their source in the training set.*

*   *Theory of change:* By attributing harmful, biased, or unaligned behaviors to specific training examples, researchers can audit proprietary models, debug training data, enable effective data deletion/unlearning
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behavioural · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Goals misgeneralize out of distribution, Value is fragile and hard to specify
*   *See also:* [Data quality for alignment](#Data_quality_for_alignment)
*   *Some names:* Roger Grosse, Philipp Alexander Kreer, Jin Hwa Lee, Matthew Smith, Abhilasha Ravichander, Andrew Wang, Jiacheng Liu, Jiaqi Ma, Junwei Deng, Yijun Pan, Daniel Murfet, Jesse Hoogland
*   *Funded by:* Various academic groups
*   *Estimated FTEs:* 30-60

+++ Some outputs (12)

*   [Influence Dynamics and Stagewise Data Attribution](https://arxiv.org/abs/2510.12071). *Jin Hwa Lee et al.*
*   [What is Your Data Worth to GPT?](https://arxiv.org/abs/2405.13954). *Sang Keun Choe et al.*
*   [Detecting and Filtering Unsafe Training Data via Data Attribution with Denoised Representation](https://arxiv.org/abs/2502.11411). *Yijun Pan et al.*
*   [Better Training Data Attribution via Better Inverse Hessian-Vector Products](https://arxiv.org/abs/2507.14740). *Andrew Wang et al.*
*   [DATE-LM: Benchmarking Data Attribution Evaluation for Large Language Models](https://arxiv.org/abs/2507.09424). *Cathy Jiao et al.*
*   [Bayesian Influence Functions for Hessian-Free Data Attribution](https://arxiv.org/abs/2509.26544). *Philipp Alexander Kreer et al.*
*   [OLMoTrace: Tracing Language Model Outputs Back to Trillions of Training Tokens](https://arxiv.org/abs/2504.07096). *Jiacheng Liu et al.*
*   [You Are What You Eat -- AI Alignment Requires Understanding How Data Shapes Structure and Generalisation](https://arxiv.org/abs/2502.05475). *Simon Pepin Lehalleur et al.*
*   [Information-Guided Identification of Training Data Imprint in (Proprietary) Large Language Models](https://arxiv.org/abs/2503.12072). *Abhilasha Ravichander et al.*
*   [Distributional Training Data Attribution: What do Influence Functions Sample?](https://arxiv.org/abs/2506.12965). *Bruno Mlodozeniec et al.*
*   [A Snapshot of Influence: A Local Data Attribution Framework for Online Reinforcement Learning](https://openreview.net/forum?id=sYK4yPDuT1). *Yuzheng Hu et al.*
*   [Revisiting Data Attribution for Influence Functions](https://arxiv.org/abs/2508.07297). *Hongbo Zhu, Angelo Cangelosi*

+++

### Pragmatic interpretability

*Directly tackling concrete, safety-critical problems on the path to AGI by using lightweight interpretability tools (like steering and probing) and empirical feedback from proxy tasks, rather than pursuing complete mechanistic reverse-engineering.*

*   *Theory of change:* By applying interpretability skills to concrete problems, researchers can rapidly develop monitoring and control tools (e.g., steering vectors or probes) that have immediate, measurable impact on real-world safety issues like detecting hidden goals or emergent misalignment.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* mixed
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Superintelligence can fool human supervisors, Goals misgeneralize out of distribution
*   *See also:* [Reverse engineering](#Reverse_engineering) · [Concept-based interpretability](#Concept_based_interpretability)
*   *Some names:* Lee Sharkey, Dario Amodei, David Chalmers, Been Kim, Neel Nanda, David D. Baek, Lauren Greenspan, Dmitry Vaintrob, Sam Marks, Jacob Pfau
*   *Funded by:* Google DeepMind, Anthropic, various academic groups
*   *Estimated FTEs:* 30-60

+++ Some outputs (3)

*   [A Pragmatic Vision for Interpretability](https://www.lesswrong.com/posts/StENzDcD3kpfGJssR/a-pragmatic-vision-for-inter). *Neel Nanda et al.*
*   [Agentic Interpretability: A Strategy Against Gradual Disempowerment](https://www.alignmentforum.org/posts/s9z4mgjtWTPpDLxFy/agentic-interpretability-a-strategy-against-gradual). *Been Kim et al.*
*   [Auditing language models for hidden objectives](https://arxiv.org/abs/2503.10965). *Samuel Marks et al.*

+++

### Other interpretability

*Interpretability that does not fall well into other categories.*

*   *Theory of change:* Explore alternative conceptual frameworks (e.g., agentic, propositional) and physics-inspired methods (e.g., renormalization). Or be "pragmatic".
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering / cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* mixed
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Superintelligence can fool human supervisors, Goals misgeneralize out of distribution
*   *See also:* [Reverse engineering](#Reverse_engineering) · [Concept-based interpretability](#Concept_based_interpretability)
*   *Some names:* Lee Sharkey, Dario Amodei, David Chalmers, Been Kim, Neel Nanda, David D. Baek, Lauren Greenspan, Dmitry Vaintrob, Sam Marks, Jacob Pfau
*   *Critiques:* [The Misguided Quest for Mechanistic AI Interpretability](https://aifrontiersmedia.substack.com/p/the-misguided-quest-for-mechanistic), [Interpretability Will Not Reliably Find Deceptive AI](https://www.lesswrong.com/posts/PwnadG4BFjaER3MGf/interpretability-will-not-reliably-find-deceptive-ai).
*   *Estimated FTEs:* 30-60

+++ Some outputs (19)

*   [Transformers Don't Need LayerNorm at Inference Time: Implications for Interpretability](https://lesswrong.com/posts/KbFuuaBKRP7FcAADL/transformers-don-t-need-layernorm-at-inference-time). *submarat et al.*
*   [Where Did It Go Wrong? Attributing Undesirable LLM Behaviors via Representation Gradient Tracing](https://arxiv.org/abs/2510.02334). *Zhe Li et al.*
*   [Open Problems in Mechanistic Interpretability](https://arxiv.org/abs/2501.16496). *Lee Sharkey et al.*
*   [Against blanket arguments against interpretability](https://lesswrong.com/posts/u3ZysuXEjkyHhefrk/against-blanket-arguments-against-interpretability). *Dmitry Vaintrob*
*   [Opportunity Space: Renormalization for AI Safety](https://lesswrong.com/posts/wkGmouy7JnTNtWAbc/opportunity-space-renormalization-for-ai-safety). *Lauren Greenspan, Dmitry Vaintrob, Lucas Teixeira*
*   [Prospects for Alignment Automation: Interpretability Case Study](https://lesswrong.com/posts/y5cYisQ2QHiSbQbhk/prospects-for-alignment-automation-interpretability-case). *Jacob Pfau, Geoffrey Irving*
*   [The Urgency of Interpretability](https://www.darioamodei.com/post/the-urgency-of-interpretability). *Dario Amodei*
*   [Language Models May Verbatim Complete Text They Were Not Explicitly Trained On](https://arxiv.org/abs/2503.17514). *Ken Ziyu Liu et al.*
*   [Downstream applications as validation of interpretability progress](https://lesswrong.com/posts/wGRnzCFcowRCrpX4Y/downstream-applications-as-validation-of-interpretability). *Sam Marks*
*   [Principles for Picking Practical Interpretability Projects](https://lesswrong.com/posts/DqaoPNqhQhwBFqWue/principles-for-picking-practical-interpretability-projects). *Sam Marks*
*   [Propositional Interpretability in Artificial Intelligence](https://arxiv.org/abs/2501.15740). *David J. Chalmers*
*   [Explainable and Interpretable Multimodal Large Language Models: A Comprehensive Survey](https://arxiv.org/abs/2412.02104). *Yunkai Dang et al.*
*   [Renormalization Redux: QFT Techniques for AI Interpretability](https://lesswrong.com/posts/sjr66DBEgyogAbfdf/renormalization-redux-qft-techniques-for-ai-interpretability). *Lauren Greenspan, Dmitry Vaintrob*
*   [The Strange Science of Interpretability: Recent Papers and a Reading List for the Philosophy of Interpretability](https://lesswrong.com/posts/qRnupMmFG7dxQTTYh/the-strange-science-of-interpretability-recent-papers-and-a). *Kola Ayonrinde, Louis Jaburi*
*   [Through a Steerable Lens: Magnifying Neural Network Interpretability via Phase-Based Extrapolation](https://arxiv.org/abs/2506.02300). *Farzaneh Mahdisoltani et al.*
*   [Call for Collaboration: Renormalization for AI safety](https://lesswrong.com/posts/MDWGcNHkZ3NPEzcnp/call-for-collaboration-renormalization-for-ai-safety). *Lauren Greenspan*
*   [On the creation of narrow AI: hierarchy and nonlocality of neural network skills](https://arxiv.org/abs/2505.15811). *Eric J. Michaud, Asher Parker-Sartori, Max Tegmark*
*   [Harmonic Loss Trains Interpretable AI Models](https://arxiv.org/abs/2502.01628). *David D. Baek et al.*
*   [Extracting memorized pieces of (copyrighted) books from open-weight language models](https://arxiv.org/abs/2505.12546). *A. Feder Cooper et al.*

+++

### Learning dynamics and developmental interpretability

*Builds tools for detecting, locating, and interpreting key structural shifts, phase transitions, and emergent phenomena (like grokking or deception) that occur during a model's training and in-context learning phases.*

*   *Theory of change:* Structures forming in neural networks leave identifiable traces that can be interpreted (e.g., using concepts from Singular Learning Theory); by catching and analyzing these developmental moments, researchers can automate interpretability, predict when dangerous capabilities emerge, and intervene to prevent deceptiveness or misaligned values as early as possible.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitivist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Goals misgeneralize out of distribution
*   *See also:* [Reverse engineering](#Reverse_engineering) · [Sparse Coding](#Sparse_Coding) · [ICL transience](https://proceedings.mlr.press/v267/singh25c.html)
*   *Some names:* Timaeus, Jesse Hoogland, George Wang, Daniel Murfet, Stan van Wingerden, Alexander Gietelink Oldenziel
*   *Critiques:* [Vaintrob](https://www.lesswrong.com/posts/M2bs6xCbmc79nwr8j/dmitry-vaintrob-s-shortform#A8Ziwhts35dgqbz52), [Joar Skalse (2023)](https://www.alignmentforum.org/posts/ALJYj4PpkqyseL7kZ/my-criticism-of-singular-learning-theory)
*   *Funded by:* Manifund, Survival and Flourishing Fund, EA Funds
*   *Estimated FTEs:* 10-50

+++ Some outputs (14)

*   [From SLT to AIT: NN Generalisation Out of Distribution](https://www.lesswrong.com/posts/2MX2bXreTtntB85Zy/from-slt-to-ait-nn-generalisation-out-of-distribution)
*   [Understanding and Controlling LLM Generalization](https://www.lesswrong.com/posts/ZSQaT2yxNNZ3eLxRd/understanding-and-controlling-llm-generalization). *Daniel Tan*
*   [SLT for AI Safety](https://lesswrong.com/posts/J7CyENFYXPxXQpsnD/slt-for-ai-safety). *Jesse Hoogland*
*   [Crosscoding Through Time: Tracking Emergence & Consolidation Of Linguistic Representations Throughout LLM Pretraining](https://arxiv.org/abs/2509.05291). *Deniz Bayazit, Aaron Mueller, Antoine Bosselut*
*   [A Review of Developmental Interpretability in Large Language Models](https://arxiv.org/abs/2508.15841). *Ihor Kendiukhov*
*   [Dynamics of Transient Structure in In-Context Linear Regression Transformers](https://arxiv.org/abs/2501.17745). *Liam Carroll et al.*
*   [Learning Coefficients, Fractals, and Trees in Parameter Space](https://openreview.net/forum?id=KUFH0n1BIM). *Max Hennick, Matthias Dellago*
*   [Emergence of Superposition: Unveiling the Training Dynamics of Chain of Continuous Thought](https://arxiv.org/abs/2509.23365). *Hanlin Zhu et al.*
*   [Compressibility Measures Complexity: Minimum Description Length Meets Singular Learning Theory](https://arxiv.org/abs/2510.12077). *Einar Urdshals et al.*
*   [Programs as Singularities](https://openreview.net/forum?id=Td37oOfmmz). *Daniel Murfet, William Troiani*
*   [What Do Learning Dynamics Reveal About Generalization in LLM Reasoning?](https://arxiv.org/abs/2411.07681). *Katie Kang et al.*
*   [Selective regularization for alignment-focused representation engineering](https://lesswrong.com/posts/HFcriD29cw3E5QLCR/selective-regularization-for-alignment-focused). *Sandy Fraser*
*   [Modes of Sequence Models and Learning Coefficients](https://arxiv.org/abs/2504.18048). *Zhongtian Chen, Daniel Murfet*
*   [Programming by Backprop: LLMs Acquire Reusable Algorithmic Abstractions During Code Training](https://arxiv.org/abs/2506.18777). *Jonathan Cook et al.*

+++

### Representation structure and geometry

*What do the representations look like? Does any simple structure underlie the beliefs of all well-trained models? Can we get the semantics from this geometry?*

*   *Theory of change:* Get scalable unsupervised methods for finding structure in representations and interpreting them, then using this to e.g. guide training.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitivist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* mixed
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Goals misgeneralize out of distribution, Superintelligence can fool human supervisors
*   *See also:* [Concept-based interpretability](#Concept_based_interpretability) · computational mechanics · feature universality · [Natural abstractions](#Natural_abstractions) · [Causal Abstractions](#Causal_Abstractions)
*   *Some names:* Simplex, Insight + Interaction Lab, Paul Riechers, Adam Shai, Martin Wattenberg, Blake Richards, Mateusz Piotrowski
*   *Funded by:* Various academic groups, Astera Institute, Coefficient Giving
*   *Estimated FTEs:* 10-50

+++ Some outputs (13)

*   [The Geometry of Self-Verification in a Task-Specific Reasoning Model](https://arxiv.org/pdf/2504.14379). *Andrew Lee et al.*
*   [Rank-1 LoRAs Encode Interpretable Reasoning Signals](http://arxiv.org/abs/2511.06739). *Jake Ward, Paul Riechers, Adam Shai*
*   [The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence](https://arxiv.org/abs/2502.17420). *Tom Wollschläger et al.*
*   [Embryology of a Language Model](https://arxiv.org/abs/2508.00331). *George Wang et al.*
*   [Constrained belief updates explain geometric structures in transformer representations](https://arxiv.org/abs/2502.01954). *Mateusz Piotrowski et al.*
*   [Shared Global and Local Geometry of Language Model Embeddings](https://arxiv.org/abs/2503.21073). *Andrew Lee et al.*
*   [Neural networks leverage nominally quantum and post-quantum representations](https://arxiv.org/abs/2507.07432). *Paul M. Riechers, Thomas J. Elliott, Adam S. Shai*
*   [Tracing the Representation Geometry of Language Models from Pretraining to Post-training](https://arxiv.org/abs/2509.23024). *Melody Zixuan Li et al.*
*   [Deep sequence models tend to memorize geometrically; it is unclear why](https://arxiv.org/abs/2510.26745). *Shahriar Noroozizadeh et al.*
*   [Navigating the Latent Space Dynamics of Neural Models](https://arxiv.org/abs/2505.22785). *Marco Fumero et al.*
*   [The Geometry of ReLU Networks through the ReLU Transition Graph](https://arxiv.org/abs/2505.11692). *Sahil Rajesh Dhayalkar*
*   [Connecting Neural Models Latent Geometries with Relative Geodesic Representations](https://arxiv.org/abs/2506.01599). *Hanlin Yu et al.*
*   [Next-token pretraining implies in-context learning](https://arxiv.org/abs/2505.18373). *Paul M. Riechers et al.*

+++

### Human inductive biases

*Discover connections deep learning AI systems have with human brains and human learning processes. Develop an 'alignment moonshot' based on a coherent theory of learning which applies to both humans and AI systems.*

*   *Theory of change:* Humans learn trust, honesty, self-maintenance, and corrigibility; if we understand how they do maybe we can get future AI systems to learn them.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Goals misgeneralize out of distribution
*   *See also:* active learning · ACS research
*   *Some names:* Lukas Muttenthaler, Quentin Delfosse
*   *Funded by:* Google DeepMind, various academic groups
*   *Estimated FTEs:* 4

+++ Some outputs (6)

*   [Aligning machine and human visual representations across abstraction levels](https://www.nature.com/articles/s41586-025-09631-6). *Lukas Muttenthaler et al.*
*   [Deep Reinforcement Learning Agents are not even close to Human Intelligence](https://arxiv.org/html/2505.21731v1)
*   [Teaching AI to Handle Exceptions: Supervised Fine-tuning with Human-aligned Judgment](https://arxiv.org/html/2503.02976v2#S3). *Matthew DosSantos DiSorbo, Harang Ju, Sinan Aral*
*   [HIBP Human Inductive Bias Project Plan](https://docs.google.com/document/d/1fl7LE8AN7mLJ6uFcPuFCzatp0zCIYvjRIjQRgHPAkSE/edit?tab=t.0). *Félix Dorn*
*   [Beginning with You: Perceptual-Initialization Improves Vision-Language Representation and Alignment](https://arxiv.org/abs/2505.14204). *Yang Hu et al.*
*   [Towards Cognitively-Faithful Decision-Making Models to Improve AI Alignment](https://arxiv.org/abs/2509.04445). *Cyrus Cousins et al.*

+++

Concept-based interpretability
------------------------------

### Monitoring concepts

*Identifies directions or subspaces in a model's latent state that correspond to high-level concepts (like refusal, deception, or planning) and uses them to audit models for misalignment, monitor them at runtime, suppress eval awareness, debug why models are failing, etc.*

*   *Theory of change:* By mapping internal activations to human-interpretable concepts, we can detect dangerous capabilities or deceptive alignment directly in the mind of the model even if its overt behavior is perfectly safe. Deploy computationally cheap monitors to flag some hidden misalignment in deployed systems.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify, Goals misgeneralize out of distribution, A boxed AGI might exfiltrate itself by steganography, spearphishing
*   *See also:* [Pragmatic interp](https://www.alignmentforum.org/posts/StENzDcD3kpfGJssR/a-pragmatic-vision-for-interpretability) · [Reverse engineering](#Reverse_engineering) · [Sparse Coding](#Sparse_Coding) · [Model diffing](#Model_diffing)
*   *Some names:* Daniel Beaglehole, Adityanarayanan Radhakrishnan, Enric Boix-Adserà, Tom Wollschläger, Anna Soligo, Jack Lindsey, Brian Christian, Ling Hu, Nicholas Goldowsky-Dill, Neel Nanda
*   *Critiques:* [Exploring the generalization of LLM truth directions on conversational formats](https://arxiv.org/html/2505.09807v1), [Understanding (Un)Reliability of Steering Vectors in Language Models](https://arxiv.org/abs/2505.22637)
*   *Funded by:* Coefficient Giving, Anthropic, various academic groups
*   *Estimated FTEs:* 50-100

+++ Some outputs (11)

*   [Convergent Linear Representations of Emergent Misalignment](https://arxiv.org/abs/2506.11618). *Anna Soligo et al.*
*   [Detecting Strategic Deception Using Linear Probes](https://arxiv.org/abs/2502.03407). *Nicholas Goldowsky-Dill et al.*
*   [Toward universal steering and monitoring of AI models](https://arxiv.org/abs/2502.03708). *Daniel Beaglehole et al.*
*   [Reward Model Interpretability via Optimal and Pessimal Tokens](https://arxiv.org/abs/2506.07326). *Brian Christian et al.*
*   [The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence](https://arxiv.org/abs/2502.17420). *Tom Wollschläger et al.*
*   [Cost-Effective Constitutional Classifiers via Representation Re-use](https://alignment.anthropic.com/2025/cheap-monitors). *Hoagy Cunningham et al.*
*   [Refusal in LLMs is an Affine Function](https://arxiv.org/abs/2411.09003). *Thomas Marshall, Adam Scherlis, Nora Belrose*
*   [White Box Control at UK AISI - Update on Sandbagging Investigations](https://www.alignmentforum.org/posts/pPEeMdgjpjHZWCDFw/white-box-control-at-uk-aisi-update-on-sandbagging). *Joseph Bloom et al.*
*   [Here's 18 Applications of Deception Probes](https://lesswrong.com/posts/7zhAwcBri7yupStKy/here-s-18-applications-of-deception-probes). *Cleo Nardo, Avi Parrack, jordine*
*   [How Do LLMs Persuade? Linear Probes Can Uncover Persuasion Dynamics in Multi-Turn Conversations](https://arxiv.org/abs/2508.05625). *Brandon Jaipersaud, David Krueger, Ekdeep Singh Lubana*
*   [Beyond Linear Probes: Dynamic Safety Monitoring for Language Models](https://arxiv.org/abs/2509.26238). *James Oldfield et al.*

+++

### Activation engineering

*Programmatically modify internal model activations to steer outputs toward desired behaviors; a lightweight, interpretable supplement to fine-tuning.*

*   *Theory of change:* Test interpretability theories by intervening on activations; find new insights from interpretable causal interventions on representations. Or: build more stuff to stack on top of finetuning. Slightly encourage the model to be nice, add one more layer of defence to our bundle of partial alignment methods.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering / cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify
*   *See also:* [Sparse Coding](#Sparse_Coding)
*   *Some names:* Runjin Chen, Andy Arditi, David Krueger, Jan Wehner, Narmeen Oozeer, Reza Bayat, Adam Karvonen, Jiuding Sun, Tim Tian Hua, Helena Casademunt, Jacob Dunefsky, Thomas Marshall
*   *Critiques:* [Understanding (Un)Reliability of Steering Vectors in Language Models](https://arxiv.org/abs/2505.22637)
*   *Funded by:* Coefficient Giving, Anthropic
*   *Estimated FTEs:* 20-100

+++ Some outputs (15)

*   [Do safety-relevant LLM steering vectors optimized on a single example generalize?](https://lesswrong.com/posts/6aXe9nipTgwK5LxaP/do-safety-relevant-llm-steering-vectors-optimized-on-a). *Jacob Dunefsky*
*   [Keep Calm and Avoid Harmful Content: Concept Alignment and Latent Manipulation Towards Safer Answers](https://arxiv.org/abs/2510.12672). *Ruben Belo, Marta Guimaraes, Claudia Soares*
*   [Activation Space Interventions Can Be Transferred Between Large Language Models](https://arxiv.org/abs/2503.04429). *Narmeen Oozeer et al.*
*   [HyperSteer: Activation Steering at Scale with Hypernetworks](https://arxiv.org/abs/2506.03292). *Jiuding Sun et al.*
*   [Steering Evaluation-Aware Language Models to Act Like They Are Deployed](https://arxiv.org/abs/2510.20487). *Tim Tian Hua et al.*
*   [Steering Out-of-Distribution Generalization with Concept Ablation Fine-Tuning](https://arxiv.org/abs/2507.16795). *Helena Casademunt et al.*
*   [Persona Vectors: Monitoring and Controlling Character Traits in Language Models](https://arxiv.org/abs/2507.21509). *Runjin Chen et al.*
*   [Steering Large Language Model Activations in Sparse Spaces](https://arxiv.org/abs/2503.00177). *Reza Bayat et al.*
*   [Improving Steering Vectors by Targeting Sparse Autoencoder Features](https://arxiv.org/abs/2411.02193). *Sviatoslav Chalnev, Matthew Siu, Arthur Conmy*
*   [Understanding Reasoning in Thinking Language Models via Steering Vectors](https://arxiv.org/abs/2506.18167). *Constantin Venhoff et al.*
*   [One-shot steering vectors cause emergent misalignment, too](https://lesswrong.com/posts/kcKnKHTHycHeRhcHF/one-shot-steering-vectors-cause-emergent-misalignment-too). *Jacob Dunefsky*
*   [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://arxiv.org/abs/2411.02461). *Yuxin Xiao et al.*
*   [Comparing Bottom-Up and Top-Down Steering Approaches on In-Context Learning Tasks](https://arxiv.org/abs/2411.07213). *Madeline Brumley et al.*
*   [Taxonomy, Opportunities, and Challenges of Representation Engineering for Large Language Models](https://arxiv.org/abs/2502.19649). *Jan Wehner et al.*
*   [Robustly Improving LLM Fairness in Realistic Settings via Interpretability](https://arxiv.org/abs/2506.10922). *Adam Karvonen, Samuel Marks*

+++

Safety by construction
======================

Approaches which try to get assurances about system outputs while still being scalable.

### Guaranteed-Safe AI

*Have an AI system generate outputs (e.g. code, control systems, or RL policies) which it can quantitatively guarantee comply with a formal safety specification and world model.*

*   *Theory of change:* Various, including:

i) safe deployment: create a scalable process to get not-fully-trusted AIs to produce highly trusted outputs;

ii) secure containers: create a 'gatekeeper' system that can act as an intermediary between human users and a potentially dangerous system, only letting provably safe actions through.

(Notable for not requiring that we solve ELK; does require that we solve ontology though)

*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive / engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify, Goals misgeneralize out of distribution, Superintelligence can fool human supervisors, Humans cannot be first-class parties to a superintelligent value handshake, A boxed AGI might exfiltrate itself by steganography, spearphishing
*   *See also:* [Towards Guaranteed Safe AI](https://arxiv.org/abs/2405.06624) · [Standalone World-Models](https://www.alignmentforum.org/posts/LngR93YwiEpJ3kiWh/research-agenda-synthesizing-standalone-world-models) · [Scientist AI](#Scientist_AI) · Safeguarded AI · [Asymptotic guarantees](#Asymptotic_guarantees) · Open Agency Architecture · SLES · program synthesis · Scalable formal oversight
*   *Some names:* ARIA, Lawzero, Atlas Computing, FLF, Max Tegmark, Beneficial AI Foundation, Steve Omohundro, David "davidad" Dalrymple, Joar Skalse, Stuart Russell, Alessandro Abate
*   *Critiques:* [Zvi](https://thezvi.substack.com/p/ai-28-watching-and-waiting?utm_source=%2Fsearch%2Fomohundro&utm_medium=reader2#:~:text=Max%20Tegmark%20and%20Steve%20Omohundo%20drop%20a%20new%20paper), [Gleave](https://manifund.org//projects/relocating-to-montreal-to-work-full-time-on-ai-safety?tab=comments#aea6521a-c6bb-4c66-9f5f-cf647589cf7e), [Dickson](https://www.lesswrong.com/posts/B2bg677TaS4cmDPzL/limitations-on-formal-verification-for-ai-safety), [Greenblatt](https://www.lesswrong.com/posts/jRf4WENQnhssCb6mJ/davidad-s-bold-plan-for-alignment-an-in-depth-explanation?commentId=MJCvHk5ARMnWDjQDg)
*   *Funded by:* Manifund, ARIA, Coefficient Giving, Survival and Flourishing Fund, Mila / CIFAR
*   *Estimated FTEs:* 10-100

+++ Some outputs (5)

*   [SafePlanBench: evaluating a Guaranteed Safe AI Approach for LLM-based Agents](https://manifund.org/projects/safeplanbench-evaluating-a-guaranteed-safe-ai-approach-for-llm-based-agents). *Agustín Martinez Suñé, Tan Zhi Xuan*
*   [Beliefs about formal methods and AI safety](https://lesswrong.com/posts/CCT7Qc8rSeRs7r5GL/beliefs-about-formal-methods-and-ai-safety). *Quinn Dougherty*
*   [Report on NSF Workshop on Science of Safe AI](https://arxiv.org/abs/2506.22492). *Rajeev Alur et al.*
*   [A benchmark for vericoding: formally verified program synthesis](https://arxiv.org/abs/2509.22908). *Sergiu Bursuc et al.*
*   [A Toolchain for AI-Assisted Code Specification, Synthesis and Verification](https://atlascomputing.org/ai-assisted-fv-toolchain.pdf)

+++

### Scientist AI

*Develop powerful, nonagentic, uncertain world models that accelerate scientific progress while avoiding the risks of agent AIs*

*   *Theory of change:* Developing non-agentic 'Scientist AI' allows us to: (i) reap the benefits of AI progress while (ii) avoiding the inherent risks of agentic systems. These systems can also (iii) provide a useful guardrail to protect us from unsafe agentic AIs by double-checking actions they propose, and (iv) help us more safely build agentic superintelligent systems.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitivist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Pivotal processes require dangerous capabilities, Goals misgeneralize out of distribution, Instrumental convergence
*   *See also:* [JEPA](https://arxiv.org/abs/2511.08544) · [oracles](https://www.lesswrong.com/w/oracle-ai)
*   *Some names:* Yoshua Bengio, Younesse Kaddar
*   *Critiques:* Hard to find, but see [Raymond Douglas' comment](https://www.lesswrong.com/posts/p5gBcoQeBsvsMShvT/superintelligent-agents-pose-catastrophic-risks-can?commentId=tJXqhg3XZsqnyaZs2), [Karnofsky-Soares discussion](https://www.lesswrong.com/posts/iy2o4nQj9DnQD7Yhj/discussion-with-nate-soares-on-a-key-alignment-difficulty). Perhaps also [Predict-O-Matic](https://www.lesswrong.com/posts/SwcyMEgLyd4C3Dern/the-parable-of-predict-o-matic).
*   *Funded by:* ARIA, Gates Foundation, Future of Life Institute, Coefficient Giving, Jaan Tallinn, Schmidt Sciences
*   *Estimated FTEs:* 1-10

+++ Some outputs (2)

*   [Superintelligent Agents Pose Catastrophic Risks: Can Scientist AI Offer a Safer Path?](https://arxiv.org/abs/2502.15657). *Yoshua Bengio et al.*
*   [The More You Automate, the Less You See: Hidden Pitfalls of AI Scientist Systems](https://arxiv.org/abs/2509.08713). *Ziming Luo, Atoosa Kasirzadeh, Nihar B. Shah*

+++

### Brainlike-AGI Safety

*Social and moral instincts are (partly) implemented in particular hardwired brain circuitry; let's figure out what those circuits are and how they work; this will involve symbol grounding. "a yet-to-be-invented variation on actor-critic model-based reinforcement learning"*

*   *Theory of change:* Fairly-direct alignment via changing training to reflect actual human reward. Get actual data about (reward, training data) → (human values) to help with theorising this map in AIs; "understand human social instincts, and then maybe adapt some aspects of those for AGIs, presumably in conjunction with other non-biological ingredients".
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitivist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Agenda statement*: [My AGI safety research—2025 review, '26 plans](https://www.lesswrong.com/posts/CF4Z9mQSfvi99A3BR/my-agi-safety-research-2025-review-26-plans)
*   *Some names:* Steve Byrnes
*   *Critiques:* [Tsvi BT](https://www.lesswrong.com/posts/unCG3rhyMJpGJpoLd/koan-divining-alien-datastructures-from-ram-activations#BtHCubjKWDFafkmYH)
*   *Funded by:* Astera Institute
*   *Estimated FTEs:* 1-5

+++ Some outputs (6)

*   [Perils of Under vs Over-sculpting AGI Desires](https://www.lesswrong.com/posts/grgb2ipxQf2wzNDEG/perils-of-under-vs-over-sculpting-agi-desires)
*   [Reward button alignment](https://lesswrong.com/posts/JrTk2pbqp7BFwPAKw/reward-button-alignment). *Steven Byrnes*
*   [System 2 Alignment: Deliberation, Review, and Thought Management](https://www.lesswrong.com/posts/cus5CGmLrjBRgcPSF/system-2-alignment-deliberation-review-and-thought). *Seth Herd*
*   [Against RL: The Case for System 2 Learning](https://elicit.com/blog/system-2-learning). *Andreas Stuhlmüller*
*   [Foom and Doom 1: Brain in a Box in a Basement](https://www.lesswrong.com/posts/yew6zFWAKG4AGs3Wk/foom-and-doom-1-brain-in-a-box-in-a-basement)
*   [Foom and Doom 2: Technical Alignment is Hard](https://www.lesswrong.com/posts/bnnKGSCHJghAvqPjS/foom-and-doom-2-technical-alignment-is-hard)

+++

Make AI solve it
================

### Weak-to-strong generalization

*Use weaker models to supervise and provide a feedback signal to stronger models.*

*   *Theory of change:* Find techniques that do better than RLHF at supervising superior models → track whether these techniques fail as capabilities increase further → keep the stronger systems aligned by amplifying weak oversight and quantifying where it breaks.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Superintelligence can hack software supervisors
*   *See also:* [White-box safety (i.e. Interpretability)](#White_box_safety_i_e_Interpretability_) · [Supervising AIs improving AIs](#Supervising_AIs_improving_AIs)
*   *Some names:* Joshua Engels, Nora Belrose, David D. Baek
*   *Critiques:* [Can we safely automate alignment research?](https://joecarlsmith.substack.com/p/can-we-safely-automate-alignment), [Super(ficial)-alignment: Strong Models May Deceive Weak Models in Weak-to-Strong Generalization](https://arxiv.org/abs/2406.11431)
*   *Funded by:* lab funders, Eleuther funders
*   *Estimated FTEs:* 2-20

+++ Some outputs (4)

*   [Scaling Laws For Scalable Oversight](https://arxiv.org/abs/2504.18530). *Joshua Engels et al.*
*   [Great Models Think Alike and this Undermines AI Oversight](https://arxiv.org/abs/2502.04313). *Shashwat Goel et al.*
*   [Debate Helps Weak-to-Strong Generalization](https://arxiv.org/abs/2501.13124). *Hao Lang, Fei Huang, Yongbin Li*
*   [Understanding the Capabilities and Limitations of Weak-to-Strong Generalization](https://openreview.net/forum?id=RwYdLgj1S6). *Wei Yao et al.*

+++

### Supervising AIs improving AIs

*Build formal and empirical frameworks where AIs supervise other (stronger) AI systems via structured interactions; construct monitoring tools which enable scalable tracking of behavioural drift, benchmarks for self-modification, and robustness guarantees*

*   *Theory of change:* Early models train ~only on human data while later models also train on early model outputs, which leads to early model problems cascading. Left unchecked this will likely cause problems, so supervision mechanisms are needed to help ensure the AI self-improvement remains legible.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behavioral · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Superintelligence can fool human supervisors, Superintelligence can hack software supervisors
*   *Some names:* Roman Engeler, Akbir Khan, Ethan Perez
*   *Critiques:* [Automation collapse](https://www.lesswrong.com/posts/2Gy9tfjmKwkYbF9BY/automation-collapse), [Great Models Think Alike and this Undermines AI Oversight](https://arxiv.org/abs/2502.04313)
*   *Funded by:* Long-Term Future Fund, lab funders
*   *Estimated FTEs:* 1-10

+++ Some outputs (8)

*   [Bare Minimum Mitigations for Autonomous AI Development](https://saif.org/research/bare-minimum-mitigations-for-autonomous-ai-development/). *Joshua Clymer et al.*
*   [Dodging systematic human errors in scalable oversight](https://www.alignmentforum.org/posts/EgRJtwQurNzz8CEfJ/dodging-systematic-human-errors-in-scalable-oversight). *Geoffrey Irving*
*   [Scaling Laws for Scalable Oversight](https://arxiv.org/abs/2504.18530). *Joshua Engels et al.*
*   [Neural Interactive Proofs](https://arxiv.org/abs/2412.08897). *Lewis Hammond, Sam Adam-Day*
*   [Modeling Human Beliefs about AI Behavior for Scalable Oversight](https://arxiv.org/abs/2502.21262). *Leon Lang, Patrick Forré*
*   [Scalable Oversight for Superhuman AI via Recursive Self-Critiquing](https://arxiv.org/abs/2502.04675). *Xueru Wen et al.*
*   [Video and transcript of talk on automating alignment research](https://lesswrong.com/posts/TQbptN7F4ijPnQRLy/video-and-transcript-of-talk-on-automating-alignment). *Joe Carlsmith*
*   [Maintaining Alignment during RSI as a Feedback Control Problem](https://lesswrong.com/posts/PhgEKkB4cwYjwpGxb/maintaining-alignment-during-rsi-as-a-feedback-control). *beren*

+++

### AI explanations of AIs

*Make open AI tools to explain AIs, including AI agents. e.g. automatic feature descriptions for neuron activation patterns; an interface for steering these features; a behaviour elicitation agent that "searches" for a specified behaviour in frontier models.*

*   *Theory of change:* Use AI to help improve interp and evals. Develop and release open tools to level up the whole field. Get invited to improve lab processes.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Superintelligence can fool human supervisors, Superintelligence can hack software supervisors
*   *See also:* [White-box safety (i.e. Interpretability)](#White_box_safety_i_e_Interpretability_)
*   *Some names:* Transluce, Jacob Steinhardt, Neil Chowdhury, Vincent Huang, Sarah Schwettmann, Robert Friel
*   *Funded by:* Schmidt Sciences, Halcyon Futures, John Schulman, Wojciech Zaremba
*   *Estimated FTEs:* 15-30

+++ Some outputs (5)

*   [Automatically Jailbreaking Frontier Language Models with Investigator Agents](https://transluce.org/jailbreaking-frontier-models)
*   [Surfacing Pathological Behaviors in Language Models](https://transluce.org/pathological-behaviors)
*   [Investigating truthfulness in a pre-release o3 model](https://transluce.org/investigating-o3-truthfulness). *Neil Chowdhury et al.*
*   [Neuron circuits](https://transluce.org/neuron-circuits). *Aryaman Arora et al.*
*   [Docent: A system for analyzing and intervening on agent behavior](https://transluce.org/introducing-docent). *Kevin Meng et al.*

+++

### Debate

*In the limit, it's easier to compellingly argue for true claims than for false claims; exploit this asymmetry to get trusted work out of untrusted debaters.*

*   *Theory of change:* "Give humans help in supervising strong agents" + "Align explanations with the true reasoning process of the agent" + "Red team models to exhibit failure modes that don't occur in normal use" are necessary but probably not sufficient for safe AGI.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering / cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify, Superintelligence can fool human supervisors
*   *Some names:* Rohin Shah, Jonah Brown-Cohen, Georgios Piliouras, UK AISI (Benjamin Holton)
*   *Critiques:* [The limits of AI safety via debate (2022)](https://www.lesswrong.com/posts/kguLeJTt6LnGuYX4E/the-limits-of-ai-safety-via-debate)
*   *Funded by:* Google, others

+++ Some outputs (6)

*   [UK AISI Alignment Team: Debate Sequence](https://www.lesswrong.com/s/NdovveRcyfxgMoujf). *Benjamin Hilton*
*   [Prover-Estimator Debate: A New Scalable Oversight Protocol](https://lesswrong.com/posts/8XHBaugB5S3r27MG9/prover-estimator-debate-a-new-scalable-oversight-protocol). *Jonah Brown-Cohen, Geoffrey Irving*
*   [AI Debate Aids Assessment of Controversial Claims](https://arxiv.org/abs/2506.02175). *Salman Rahman et al.*
*   [An alignment safety case sketch based on debate](https://arxiv.org/abs/2505.03989). *Marie Davidsen Buhl et al.*
*   [Ensemble Debates with Local Large Language Models for AI Alignment](https://arxiv.org/abs/2509.00091). *Ephraiem Sarabamoun*
*   [A dataset of rated conceptual arguments](https://www.andrew.cmu.edu/user/coesterh/LMCA_dataset.pdf)

+++

### LLM introspection training

*Train LLMs to the predict the outputs of high-quality whitebox methods, to induce general self-explanation skills that use its own 'introspective' access*

*   *Theory of change:* Use the resulting LLMs as powerful dimensionality reduction, explaining internals in a distinct way than interpretability methods and CoT. Distilling self-explanation into the model should lead to the skill being scalable, since self-explanation skill advancement will feed off general-intelligence advancement.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitivist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* mixed
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Goals misgeneralize out of distribution, Superintelligence can fool human supervisors, Superintelligence can hack software supervisors
*   *See also:* [Transluce](#transluce) · [Anthropic](#Anthropic)
*   *Some names:* Belinda Z. Li, Zifan Carl Guo, Vincent Huang, Jacob Steinhardt, Jacob Andreas, Jack Lindsey
*   *Funded by:* Schmidt Sciences, Halcyon Futures, John Schulman, Wojciech Zaremba
*   *Estimated FTEs:* 2-20

+++ Some outputs (2)

*   [Training Language Models to Explain Their Own Computations](https://arxiv.org/abs/2511.08579). *Belinda Z. Li et al.*
*   [Emergent Introspective Awareness](https://transformer-circuits.pub/2025/introspection/index.html). *Jack Lindsey*

+++

Theory
======

*Develop a principled scientific understanding that will help us reliably understand and control current and future AI systems.*

### Agent foundations

*Develop philosophical clarity and mathematical formalizations of building blocks that might be useful for plans to align strong superintelligence, such as agency, optimization strength, decision theory, abstractions, concepts, etc.*

*   *Theory of change:* Rigorously understand optimization processed and agents, and what it means for them to be aligned in a substrate independent way → identify impossibility results and necessary conditions for aligned optimizer systems → use this theoretical understanding to eventually design safe architectures that remain stable and safe under self-reflection
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify, Corrigibility is anti-natural, Goals misgeneralize out of distribution
*   *See also:* [Aligning what?](#Aligning_what_) · [Tiling agents](#Tiling_agents) · [Dovetail](#theory_dovetail)
*   *Some names:* Abram Demski, Alex Altair, Sam Eisenstat, Thane Ruthenis, Alfred Harwood, Daniel C, Dalcy K, José Pedro Faustino

+++ Some outputs (10)

*   [Limit-Computable Grains of Truth for Arbitrary Computable Extensive-Form (Un)Known Games](https://www.arxiv.org/pdf/2508.16245). *Cole Wyeth et al.*
*   [UAIASI](https://uaiasi.com/blog-posts/). *Cole Wyeth*
*   [Clarifying "wisdom": Foundational topics for aligned AIs to prioritize before irreversible decisions](https://www.lesswrong.com/posts/EyvJvYEFzDv5kGoiG/clarifying-wisdom-foundational-topics-for-aligned-ais-to)
*   [Agent foundations: not really math, not really science](https://www.lesswrong.com/posts/Dt4DuCCok3Xv5HEnG/agent-foundations-not-really-math-not-really-science). *Alex_Altair*
*   [Off-switching not guaranteed](https://link.springer.com/article/10.1007/s11098-025-02296-x). *Sven Neth*
*   [Formalizing Embeddedness Failures in Universal Artificial Intelligence](https://openreview.net/forum?id=tlkYPU3FlX). *Cole Wyeth, Marcus Hutter*
*   [Is alignment reducible to becoming more coherent?](https://lesswrong.com/posts/nuDJNyG5XLQjtvaeg/is-alignment-reducible-to-becoming-more-coherent). *Cole Wyeth*
*   [What Is The Alignment Problem?](https://lesswrong.com/posts/dHNKtQ3vTBxTfTPxu/what-is-the-alignment-problem). *johnswentworth*
*   [Good old fashioned decision theory](https://openreview.net/pdf?id=Rf1CeGPA22)
*   [Report & retrospective on the Dovetail fellowship](https://www.lesswrong.com/posts/ApfjBbqzSu4aZoLSe/report-and-retrospective-on-the-dovetail-fellowship). *Alex Altair*

+++

### Tiling agents

*An aligned agentic system modifying itself into an unaligned system would be bad and we can research ways that this could occur and infrastructure/approaches that prevent it from happening.*

*   *Theory of change:* Build enough theoretical basis through various approaches such that AI systems we create are capable of self-modification while preserving goals.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitivist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify, Corrigibility is anti-natural, Goals misgeneralize out of distribution
*   *See also:* [Agent foundations](#Agent_foundations)
*   *Some names:* Abram Demski
*   *Estimated FTEs:* 1-10

+++ Some outputs (4)

*   [Working through a small tiling result](https://www.lesswrong.com/posts/akuMwu8SkmQSdospi/working-through-a-small-tiling-result). *James Payor*
*   [Communication & Trust](https://openreview.net/forum?id=Rf1CeGPA22). *Abram Demski*
*   [Maintaining Alignment during RSI as a Feedback Control Problem](https://lesswrong.com/posts/PhgEKkB4cwYjwpGxb/maintaining-alignment-during-rsi-as-a-feedback-control). *beren*
*   [Understanding Trust](https://static1.squarespace.com/static/663d1233249bce4815fe8753/t/68067a6f5d5fb0745642d5b1/1745255023842/Understanding+Trust+-+Abram+Demski.pdf). *Abram Demski*

+++

### High-Actuation Spaces

*Mech interp and alignment assume a stable "computational substrate" (linear algebra on GPUs). If later AI uses different substrates (e.g. something neuromorphic), methods like probes and steering will not transfer. Therefore, better to try and infer goals via a "telic DAG" which abstracts over substrates, and so sidestep the issue of how to define intermediate representations. Category theory is intended to provide guarantees that this abstraction is valid.*

*   *Theory of change:* Sufficiently complex mindlike entities can alter their goals in ways that cannot be predicted or accounted for under substrate-dependent descriptions of the kind sought in mechanistic interpretability. use the telic DAG to define a method analogous to factoring a causal DAG.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* maths / philosophy · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *See also:* [Live theory](https://www.lesswrong.com/s/aMz2JMvgXrLBkq4h3) · [MoSSAIC](https://openreview.net/forum?id=n7WYSJ35FU) · [Topos Institute](https://topos.institute/) · [Agent foundations](#Agent_foundations)
*   *Some names:* Sahil K, Matt Farr, Aditya Arpitha Prasad, Chris Pang, Aditya Adiga, Jayson Amati, Steve Petersen, Topos, T J
*   *Estimated FTEs:* 1-10

+++ Some outputs (7)

*   [groundless.ai](https://groundless.ai/)
*   [Live Theory](https://www.lesswrong.com/s/aMz2JMvgXrLBkq4h3)
*   [High Actuation Spaces - Sahil](https://docs.google.com/document/d/1d-ARdZZDHFPIfGcTTOKK8IZWlQj0NZQrmteJj2mvmYA/edit?tab=t.0#heading=h.eg8luyrlsv2u). *Sahil*
*   [What, if not agency?](https://www.lesswrong.com/posts/tQ9vWm4b57HFqbaRj/what-if-not-agency)
*   [Human Inductive Bias Project](https://docs.google.com/document/d/1fl7LE8AN7mLJ6uFcPuFCzatp0zCIYvjRIjQRgHPAkSE/edit?tab=t.0). *Félix Dorn*
*   [MoSSAIC: AI Safety After Mechanism](https://openreview.net/forum?id=n7WYSJ35FU). *Matt Farr et al.*
*   [HAS - Public (High Actuation Spaces)](https://drive.google.com/drive/folders/1EaAJ4szuZsYR2_-DkS9cuhx3S6IWeCjW)

+++

### Asymptotic guarantees

*Prove that if a safety process has enough resources (human data quality, training time, neural network capacity), then in the limit some system specification will be guaranteed. Use complexity theory, game theory, learning theory and other areas to both improve asymptotic guarantees and develop ways of showing convergence.*

*   *Theory of change:* Formal verification may be too hard. Make safety cases stronger by modelling their processes and proving that they would work in the limit.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Goals misgeneralize out of distribution, Superintelligence can fool human supervisors
*   *See also:* [Debate](#Debate) · [Guaranteed-Safe AI](#Guaranteed_Safe_AI) · [Control](#Control)
*   *Some names:* AISI, Jacob Pfau, Benjamin Hilton, Geoffrey Irving, Simon Marshall, Will Kirby, Martin Soto, David Africa, davidad
*   *Critiques:* Self-critique in [UK AISI's Alignment Team: Research Agenda](https://lesswrong.com/posts/tbnw7LbNApvxNLAg8/uk-aisi-s-alignment-team-research-agenda)
*   *Funded by:* AISI
*   *Estimated FTEs:* 5 - 10

+++ Some outputs (4)

*   [An alignment safety case sketch based on debate](https://lesswrong.com/posts/iELyAqizJkizBQbfr/an-alignment-safety-case-sketch-based-on-debate). *Marie_DB et al.*
*   [UK AISI's Alignment Team: Research Agenda](https://lesswrong.com/posts/tbnw7LbNApvxNLAg8/uk-aisi-s-alignment-team-research-agenda). *Benjamin Hilton et al.*
*   [Dodging systematic human errors in scalable oversight](https://lesswrong.com/posts/EgRJtwQurNzz8CEfJ/dodging-systematic-human-errors-in-scalable-oversight). *Geoffrey Irving*
*   [Can DPO Learn Diverse Human Values? A Theoretical Scaling Law](https://openreview.net/pdf?id=XOIKLlSiDq)

+++

### Heuristic explanations

*Formalize mechanistic explanations of neural network behavior, automate the discovery of these "heuristic explanations" and use them to predict when novel input will lead to extreme behavior (i.e. "Low Probability Estimation" and "Mechanistic Anomaly Detection").*

*   *Theory of change:* The current goalpost is methods whose *reasoned predictions* about properties of a neural network's outputs distribution (for a given inputs distribution) are certifiably at least as accurate as estimations via sampling. If successful for safety-relevant properties, this should allow for automated alignment methods that are both human-legible and worst-case certified, as well more efficient than sampling-based methods in most cases.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive / maths/philosophy · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Goals misgeneralize out of distribution, Superintelligence can hack software supervisors
*   *See also:* ARC Theory · ELK · mechanistic anomaly detection · [Acorn](https://acausal.org/) · [Guaranteed-Safe AI](#Guaranteed_Safe_AI)
*   *Some names:* Jacob Hilton, Mark Xu, Eric Neyman, Victor Lecomte, George Robinson
*   *Critiques:* [Matolcsi](https://www.lesswrong.com/s/uYMw689vDFmgPEHrS)
*   *Estimated FTEs:* 1-10

+++ Some outputs (5)

*   [A computational no-coincidence principle](https://www.lesswrong.com/posts/Xt9r4SNNuYxW83tmo/a-computational-no-coincidence-principle). *Eric Neyman*
*   [Competing with sampling](https://www.lesswrong.com/posts/XdQd9gELHakd5pzJA/arc-progress-update-competing-with-sampling). *Eric Neyman*
*   [Obstacles in ARC's research agenda](https://www.lesswrong.com/s/uYMw689vDFmgPEHrS). *David Matolcsi*
*   [Deduction-Projection Estimators for Understanding Neural Networks](https://gabrieldwu.com/assets/thesis.pdf)
*   [Wide Neural Networks as a Baseline for the Computational No-Coincidence Conjecture](https://openreview.net/forum?id=m4OpQAK3eY). *John Dunbar, Scott Aaronson*

+++

Corrigibility
-------------

### Behavior alignment theory

*Predict properties of future AGI (e.g. power-seeking) with formal models; formally state and prove hypotheses about the properties powerful systems will have and how we might try to change them.*

*   *Theory of change:* Figure out hypotheses about properties powerful agents will have → attempt to rigorously prove under what conditions the hypotheses hold → test these hypotheses where feasible → design training environments that lead to more salutary properties.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* maths / philosophy · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Corrigibility is anti-natural, Instrumental convergence
*   *See also:* [Agent foundations](#Agent_foundations) · [Control](#Control)
*   *Some names:* Ram Potham, Michael K. Cohen, Max Harms/Raelifin, John Wentworth, David Lorell, Elliott Thornley
*   *Critiques:* [Ryan Greenblatt's criticism](https://www.lesswrong.com/posts/YbEbwYWkf8mv9jnmi/the-shutdown-problem-incomplete-preferences-as-a-solution?commentId=GJAippZ6ZzCagSnDb) of one behavioural proposal
*   *Estimated FTEs:* 1-10

+++ Some outputs (10)

*   [Preference gaps as a safeguard against AI self-replication](https://www.lesswrong.com/posts/knwR9RgGN5a2oorci/preference-gaps-as-a-safeguard-against-ai-self-replication). *tbs, EJT*
*   [Serious Flaws in CAST](https://www.lesswrong.com/s/KfCjeconYRdFbMxsy/p/qgBFJ72tahLo5hzqy). *Max Harms*
*   [A Shutdown Problem Proposal](https://www.lesswrong.com/posts/PhTBDHu9PKJFmvb4p/a-shutdown-problem-proposal). *johnswentworth, David Lorell*
*   [Shutdownable Agents through POST-Agency](https://arxiv.org/abs/2505.20203). *Elliott Thornley*
*   [The Partially Observable Off-Switch Game](https://arxiv.org/abs/2411.17749). *Andrew Garber et al.*
*   [Imitation learning is probably existentially safe](https://onlinelibrary.wiley.com/doi/10.1002/aaai.70040?af=R). *Michael K. Cohen, Marcus Hutter*
*   [Model-Based Soft Maximization of Suitable Metrics of Long-Term Human Power](https://arxiv.org/abs/2508.00159). *Jobst Heitzig, Ram Potham*
*   [Deceptive Alignment and Homuncularity](https://lesswrong.com/posts/9htmQx5wiePqTtZuL/deceptive-alignment-and-homuncularity). *Oliver Sourbut, TurnTrout*
*   [A Safety Case for a Deployed LLM: Corrigibility as a Singular Target](https://openreview.net/forum?id=mhEnJa9pNk). *Ram Potham*
*   [LLM AGI will have memory, and memory changes alignment](https://lesswrong.com/posts/aKncW36ZdEnzxLo8A/llm-agi-will-have-memory-and-memory-changes-alignment). *Seth Herd*

+++

### Other corrigibility

*Diagnose and communicate obstacles to achieving robustly corrigible behavior; suggest mechanisms, tests, and escalation channels for surfacing and mitigating incorrigible behaviors*

*   *Theory of change:* Labs are likely to develop AGI using something analogous to current pipelines. Clarifying why naive instruction-following doesn't buy robust corrigibility + building strong tripwires/diagnostics for scheming and Goodharting thus reduces risks on the likely default path.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* varies · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Corrigibility is anti-natural, Instrumental convergence
*   *See also:* [Behavior alignment theory](#Behavior_alignment_theory)
*   *Some names:* Jeremy Gillen
*   *Estimated FTEs:* 1-10

+++ Some outputs (9)

*   [AI Assistants Should Have a Direct Line to Their Developers](https://www.lesswrong.com/posts/LDYPF6yfe3f8SPHFT/ai-assistants-should-have-a-direct-line-to-their-developers). *Jan_Kulveit*
*   [Detect Goodhart and shut down](https://www.lesswrong.com/posts/ZHFZ6tivEjznkEoby/detect-goodhart-and-shut-down). *Jeremy Gillen*
*   [Instrumental Goals Are A Different And Friendlier Kind Of Thing Than Terminal Goals](https://www.lesswrong.com/posts/7Z4WC4AFgfmZ3fCDC/instrumental-goals-are-a-different-and-friendlier-kind-of)
*   [Shutdownable Agents through POST-Agency](https://www.lesswrong.com/posts/JuRdvZyqaFbvTPemn/shutdownable-agents-through-post-agency-1). *EJT*
*   [Why Corrigibility is Hard and Important (i.e. "Whence the high MIRI confidence in alignment difficulty?")](https://www.lesswrong.com/posts/ksfjZJu3BFEfM6hHE/why-corrigibility-is-hard-and-important-i-e-whence-the-high)
*   [Oblivious Defense in ML Models: Backdoor Removal without Detection](https://dl.acm.org/doi/10.1145/3717823.3718245). *Shafi Goldwasser et al.*
*   [Cryptographic Backdoor for Neural Networks: Boon and Bane](https://arxiv.org/abs/2509.20714). *Anh Tu Ngo, Anupam Chattopadhyay, Subhamoy Maitra*
*   [A Cryptographic Perspective on Mitigation vs. Detection in Machine Learning](https://arxiv.org/abs/2504.20310). *Greg Gluch, Shafi Goldwasser*
*   [Problems with instruction-following as an alignment target](https://lesswrong.com/posts/CSFa9rvGNGAfCzBk6/problems-with-instruction-following-as-an-alignment-target). *Seth Herd*

+++

Ontology Identification
-----------------------

### Natural abstractions

*Develop a theory of concepts that explains how they are learned, how they structure a particular system's understanding, and how mutual translatability can be achieved between different collections of concepts.*

*   *Theory of change:* Understand the concepts a system's understanding is structured with and use them to inspect its "alignment/safety properties" and/or "retarget its search", i.e. identify utility-function-like components inside an AI and replacing calls to them with calls to "user values" (represented using existing abstractions inside the AI).
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Instrumental convergence, Superintelligence can fool human supervisors, Humans cannot be first-class parties to a superintelligent value handshake
*   *See also:* [Causal Abstractions](#Causal_Abstractions) · representational alignment · convergent abstractions · feature universality · Platonic representation hypothesis · microscope AI
*   *Some names:* John Wentworth, Paul Colognese, David Lorrell, Sam Eisenstat, Fernando Rosas
*   *Critiques:* [Chan et al (2023)](https://www.lesswrong.com/posts/gvzW46Z3BsaZsLc25/natural-abstractions-key-claims-theorems-and-critiques-1#3__A_formalization_of_abstractions_would_accelerate_alignment_research), [Soto](https://www.lesswrong.com/posts/CJjT8GMitsnKc2wgG/natural-abstractions-are-observer-dependent-a-conversation-1), [Harwood](https://www.lesswrong.com/posts/F4nzox6oh5oAdX9D3/abstractions-are-not-natural), [Soares (2023)](https://www.lesswrong.com/posts/mgjHS6ou7DgwhKPpu/a-rough-and-incomplete-review-of-some-of-john-wentworth-s)
*   *Estimated FTEs:* 1-10

+++ Some outputs (10)

*   [Abstract Mathematical Concepts vs. Abstractions Over Real-World Systems](https://www.lesswrong.com/posts/T6xSXiXF3WF6TmCyN/abstract-mathematical-concepts-vs-abstractions-over-real)
*   [Condensation](https://www.lesswrong.com/posts/BstHXPgQyfeNnLjjp/condensation). *abramdemski*
*   [Platonic representation hypothesis](https://phillipi.github.io/prh/). *Minyoung Huh et al.*
*   [Rosas](https://www.youtube.com/watch?v=Nr9eMobqUOo&t=3s). *Fernando Rosas*
*   [Natural Latents: Latent Variables Stable Across Ontologies](https://arxiv.org/abs/2509.03780). *John Wentworth, David Lorell*
*   [Condensation: a theory of concepts](https://openreview.net/forum?id=HwKFJ3odui). *Sam Eisenstat*
*   [Factored space models: Towards causality between levels of abstraction](https://arxiv.org/abs/2412.02579). *Scott Garrabrant et al.*
*   [A single principle related to many Alignment subproblems?](https://lesswrong.com/posts/h89L5FMAkEBNsZ3xM/a-single-principle-related-to-many-alignment-subproblems-2). *Q Home*
*   [Getting aligned on representational alignment](https://arxiv.org/abs/2310.13018). *Ilia Sucholutsky et al.*
*   [Symmetries at the origin of hierarchical emergence](https://arxiv.org/pdf/2512.00984%20). *Fernando E. Rosas*

+++

### The Learning-Theoretic Agenda

*Create a mathematical theory of intelligent agents that encompasses both humans and the AIs we want, one that specifies what it means for two such agents to be aligned; translate between its ontology and ours; produce formal desiderata for a training setup that produces coherent AGIs similar to (our model of) an aligned agent*

*   *Theory of change:* Fix formal epistemology to work out how to avoid deep training problems
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify, Goals misgeneralize out of distribution, Humans cannot be first-class parties to a superintelligent value handshake
*   *Some names:* Vanessa Kosoy, Diffractor, Gergely Szücs
*   *Critiques:* [Matolcsi](https://www.lesswrong.com/posts/StkjjQyKwg7hZjcGB/a-mostly-critical-review-of-infra-bayesianism)
*   *Funded by:* Survival and Flourishing Fund, ARIA, UK AISI, Coefficient Giving
*   *Estimated FTEs:* 3

+++ Some outputs (6)

*   [Infra-Bayesian Decision-Estimation Theory](https://www.lesswrong.com/posts/LgLez8aeK24PbyyQJ/new-paper-infra-bayesian-decision-estimation-theory)
*   [Infra-Bayesianism category on LessWrong](https://www.lesswrong.com/w/infra-bayesianism?sortedBy=new). *abramdemski, Ruby*
*   [Ambiguous Online Learning](https://www.lesswrong.com/posts/Y9NuKpb6dsyiYFxWK/new-paper-ambiguous-online-learning). *Vanessa Kosoy*
*   [Regret Bounds for Robust Online Decision Making](https://proceedings.mlr.press/v291/appel25a.html). *Alexander Appel, Vanessa Kosoy*
*   [What is Inadequate about Bayesianism for AI Alignment: Motivating Infra-Bayesianism](https://www.lesswrong.com/s/n7qFxakSnxGuvmYAX). *Brittany Gelb*
*   [Non-Monotonic Infra-Bayesian Physicalism](https://www.alignmentforum.org/posts/DobZ62XMdiPigii9H/non-monotonic-infra-bayesian-physicalism%20). *Marcus Ogren*

+++

Multi-agent first
=================

### Aligning to context

*Align AI directly to the role of participant, collaborator, or advisor for our best real human practices and institutions, instead of aligning AI to separately representable goals, rules, or utility functions.*

*   *Theory of change:* "Many classical problems in AGI alignment are downstream of a type error about human values." Operationalizing a correct view of human values - one that treats human values as impossible or impractical to abstract from concrete practices - will unblock value fragility, goal-misgeneralization, instrumental convergence, and pivotal-act specification.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behavioural · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* mixed
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify, Corrigibility is anti-natural, Goals misgeneralize out of distribution, Instrumental convergence, Fair, sane pivotal processes
*   *See also:* [Aligning what?](#Aligning_what_) · [Aligned to who?](#Aligned_to_who_)
*   *Some names:* Full Stack Alignment, Meaning Alignment Institute, Plurality Institute, Tan Zhi-Xuan, Matija Franklin, Ryan Lowe, Joe Edelman, Oliver Klingefjord
*   *Funded by:* ARIA, OpenAI, Survival and Flourishing Fund
*   *Estimated FTEs:* 5

+++ Some outputs (8)

*   [The Frame-Dependent Mind](https://www.softmax.com/blog/the-frame-dependent-mind). *Emmett Shear, Sonnet 3.7*
*   [On Eudaimonia and Optimization](https://docs.google.com/document/d/1cKbqYSGspfJavXvnhsp3mAuxHh08rNbP7tzYieqLiXw/edit?tab=t.0%20)
*   [Full-Stack Alignment](https://www.full-stack-alignment.ai)
*   [A theory of appropriateness](https://arxiv.org/abs/2412.19010). *Joel Z. Leibo et al.*
*   [2404.10636 - What are human values, and how do we align AI to them?](https://arxiv.org/abs/2404.10636). *Oliver Klingefjord, Ryan Lowe, Joe Edelman*
*   [Model Integrity](https://meaningalignment.substack.com/p/model-integrity). *Joe Edelman, Oliver Klingefjord*
*   [Beyond Preferences in AI Alignment](https://arxiv.org/abs/2408.16984). *Tan Zhi-Xuan et al.*
*   [2503.00940 - Can AI Model the Complexities of Human Moral Decision-Making? A Qualitative Study of Kidney Allocation Decisions](https://arxiv.org/abs/2503.00940). *Vijay Keswani et al.*

+++

### Aligning to the social contract

*Generate AIs' operational values from 'social contract'-style ideal civic deliberation formalisms and their consequent rulesets for civic actors*

*   *Theory of change:* Formalize and apply the liberal tradition's project of defining civic principles separable from the substantive good, aligning our AIs to civic principles that bypass fragile utility-learning and intractable utility-calculation
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* mixed
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify, Goals misgeneralize out of distribution, Instrumental convergence, Humanlike minds/goals are not necessarily safe, Fair, sane pivotal processes
*   *See also:* [Aligning to context](#Aligning_to_context) · [Aligning what?](#Aligning_what_)
*   *Some names:* Gillian Hadfield, Tan Zhi-Xuan, Sydney Levine, Matija Franklin, Joshua B. Tenenbaum
*   *Funded by:* Deepmind, Macroscopic Ventures
*   *Estimated FTEs:* 5 - 10

+++ Some outputs (8)

*   [Law-Following AI: designing AI agents to obey human laws](https://law-ai.org/law-following-ai/%20). *Cullen O'Keefe et al.*
*   [A Pragmatic View of AI Personhood](https://arxiv.org/abs/2510.26396). *Joel Z. Leibo et al.*
*   [Societal alignment frameworks can improve llm alignment](https://arxiv.org/abs/2503.00069). *Karolina Stańczak et al.*
*   [2509.07955 - ACE and Diverse Generalization via Selective Disagreement](https://arxiv.org/abs/2509.07955). *Oliver Daniels et al.*
*   [2506.17434 - Resource Rational Contractualism Should Guide AI Alignment](https://arxiv.org/abs/2506.17434). *Sydney Levine et al.*
*   [Statutory Construction and Interpretation for Artificial Intelligence](https://arxiv.org/abs/2509.01186). *Luxi He et al.*
*   [2408.16984 - Beyond Preferences in AI Alignment](https://arxiv.org/abs/2408.16984). *Tan Zhi-Xuan et al.*
*   [Promises Made, Promises Kept: Safe Pareto Improvements via Ex Post Verifiable Commitments](https://arxiv.org/abs/2505.00783). *Nathaniel Sauerberg, Caspar Oesterheld*

+++

### Theory for aligning multiple AIs

*Use realistic game-theory variants (e.g. evolutionary game theory, computational game theory) or develop alternative game theories to describe/predict the collective and individual behaviours of AI agents in multi-agent scenarios.*

*   *Theory of change:* While traditional AGI safety focuses on idealized decision-theory and individual agents, it's plausible that strategic AI agents will first emerge (or are emerging now) in a complex, multi-AI strategic landscape. We need granular, realistic formal models of AIs' strategic interactions and collective dynamics to understand this future.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* mixed
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Goals misgeneralize out of distribution, Superintelligence can fool human supervisors, Superintelligence can hack software supervisors
*   *See also:* [Tools for aligning multiple AIs](#Tools_for_aligning_multiple_AIs) · [Aligning what?](#Aligning_what_)
*   *Some names:* Lewis Hammond, Emery Cooper, Allan Chan, Caspar Oesterheld, Vincent Conitzer, Vojta Kovarik, Nathaniel Sauerberg, ACS Research, Jan Kulveit, Richard Ngo, Emmett Shear, Softmax, Full Stack Alignment, AI Objectives Institute, Sahil, TJ, Andrew Critch
*   *Funded by:* SFF, CAIF, Deepmind, Macroscopic Ventures
*   *Estimated FTEs:* 10

+++ Some outputs (12)

*   [Multi-Agent Risks from Advanced AI](https://arxiv.org/abs/2502.14143). *Lewis Hammond et al.*
*   [An Economy of AI Agents](https://arxiv.org/abs/2509.01063). *Gillian K. Hadfield, Andrew Koh*
*   [Moloch's Bargain: Emergent Misalignment When LLMs Compete for Audiences](https://arxiv.org/abs/2510.06105). *Batu El, James Zou*
*   [AI Testing Should Account for Sophisticated Strategic Behaviour](https://arxiv.org/abs/2508.14927). *Vojtech Kovarik et al.*
*   [Emergent social conventions and collective bias in LLM populations](https://www.science.org/doi/10.1126/sciadv.adu9368). *Ariel Flint Ashery, Luca Maria Aiello, Andrea Baronchelli*
*   [Strategic Intelligence in Large Language Models: Evidence from evolutionary Game Theory](https://arxiv.org/abs/2507.02618). *Kenneth Payne, Baptiste Alloui-Cros*
*   [Communication Enables Cooperation in LLM Agents](https://arxiv.org/abs/2510.05748). *Hachem Madmoun, Salem Lahlou*
*   [Higher-Order Belief in Incomplete Information MAIDs](https://arxiv.org/abs/2503.06323). *Jack Foxabbott, Rohan Subramani, Francis Rhys Ward*
*   [Characterising Simulation-Based Program Equilibria](https://arxiv.org/abs/2412.14570). *Emery Cooper, Caspar Oesterheld, Vincent Conitzer*
*   [Safe (Pareto) Improvements in Binary Constraint Structures](https://cgi.cse.unsw.edu.au/~eptcs/paper.cgi?TARK2025:36)
*   [Promises Made, Promises Kept: Safe Pareto Improvements via Ex Post Verifiable Commitments](https://arxiv.org/abs/2505.00783). *Nathaniel Sauerberg, Caspar Oesterheld*
*   [The Pando Problem: Rethinking AI Individuality](https://www.lesswrong.com/posts/wQKskToGofs4osdJ3/the-pando-problem-rethinking-ai-individuality). *Jan_Kulveit*

+++

### Tools for aligning multiple AIs

*Develop tools and techniques for designing and testing multi-agent AI scenarios, for auditing real-world multi-agent AI dynamics, and for aligning AIs in multi-AI settings.*

*   *Theory of change:* Addressing multi-agent AI dynamics is key for aligning near-future agents and their impact on the world. Feedback loops from multi-agent dynamics can radically change the future AI landscape, and require a different toolset from model psychology to audit and control.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* engineering / behavioral · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* mixed
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Goals misgeneralize out of distribution, Superintelligence can fool human supervisors, Superintelligence can hack software supervisors
*   *See also:* [Theory for aligning multiple AIs](#Theory_for_aligning_multiple_AIs) · [Aligning what?](#Aligning_what_)
*   *Some names:* Andrew Critch, Lewis Hammond, Emery Cooper, Allan Chan, Caspar Oesterheld, Vincent Conitzer, Gillian Hadfield, Nathaniel Sauerberg, Zhijing Jin
*   *Funded by:* Coefficient Giving, Deepmind, Cooperative AI Foundation
*   *Estimated FTEs:* 10 - 15

+++ Some outputs (12)

*   [Reimagining Alignment](https://softmax.com/blog/reimagining-alignment)
*   [Beyond the high score: Prosocial ability profiles of multi-agent populations](https://arxiv.org/abs/2509.14485). *Marko Tesic et al.*
*   [Multiplayer Nash Preference Optimization](https://arxiv.org/abs/2509.23102). *Fang Wu et al.*
*   [AgentBreeder: Mitigating the AI Safety Risks of Multi-Agent Scaffolds via Self-Improvement](https://arxiv.org/abs/2502.00757). *J Rosser, Jakob Foerster*
*   [When Autonomy Goes Rogue: Preparing for Risks of Multi-Agent Collusion in Social Systems](https://arxiv.org/abs/2507.14660). *Qibing Ren et al.*
*   [Infrastructure for AI Agents](https://arxiv.org/abs/2501.10114). *Alan Chan et al.*
*   [A dataset of questions on decision-theoretic reasoning in Newcomb-like problems](https://arxiv.org/abs/2411.10588). *Caspar Oesterheld et al.*
*   [The Social Laboratory: A Psychometric Framework for Multi-Agent LLM Evaluation](https://arxiv.org/abs/2510.01295). *Zarreen Reza*
*   [PGG-Bench: Contribute & Punish](https://github.com/lechmazur/pgg_bench)
*   [Virtual Agent Economies](http://arxiv.org/abs/2509.10147). *Nenad Tomasev et al.*
*   [An Interpretable Automated Mechanism Design Framework with Large Language Models](https://arxiv.org/abs/2502.12203). *Jiayuan Liu, Mingyu Guo, Vincent Conitzer*
*   [Comparing Collective Behavior of LLM and Human Groups](https://openreview.net/forum?id=9ply9CAnSC&noteId=rcn5RTlfD1). *Anna B. Stephenson et al.*

+++

### Aligned to who?

*Technical protocols for taking seriously the plurality of human values, cultures, and communities when aligning AI to "humanity"*

*   *Theory of change:* use democratic/pluralist/context-sensitive principles to guide AI development, alignment, and deployment somehow. Doing it as an afterthought in post-training or the spec isn't good enough. Continuously shape AI's social and technical feedback loop on the road to AGI
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behavioral · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify, Fair, sane pivotal processes
*   *See also:* [Aligning what?](#Aligning_what_) · [Aligning to context](#Aligning_to_context)
*   *Some names:* Joel Z. Leibo, Divya Siddarth, Séb Krier, Luke Thorburn, Seth Lazar, AI Objectives Institute, The Collective Intelligence Project, Vincent Conitzer
*   *Funded by:* Future of Life Institute, Survival and Flourishing Fund, Deepmind, CAIF
*   *Estimated FTEs:* 5 - 15

+++ Some outputs (9)

*   [The AI Power Disparity Index: Toward a Compound Measure of AI Actors' Power to Shape the AI Ecosystem](https://ojs.aaai.org/index.php/AIES/article/view/36645). *Rachel M. Kim et al.*
*   [Research Agenda for Sociotechnical Approaches to AI Safety](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5097286). *Samuel Curtis et al.*
*   [2507.09650 - Cultivating Pluralism In Algorithmic Monoculture: The Community Alignment Dataset](https://arxiv.org/abs/2507.09650). *Lily Hong Zhang et al.*
*   [Training LLM Agents to Empower Humans](https://arxiv.org/abs/2510.13709). *Evan Ellis et al.*
*   [Societal and technological progress as sewing an ever-growing, ever-changing, patchy, and polychrome quilt](https://arxiv.org/abs/2505.05197). *Joel Z. Leibo et al.*
*   [Democratic AI is Possible: The Democracy Levels Framework Shows How It Might Work](https://arxiv.org/abs/2411.09222). *Aviv Ovadya et al.*
*   [2503.05728 - Political Neutrality in AI Is Impossible - But Here Is How to Approximate It](https://arxiv.org/abs/2503.05728). *Jillian Fisher et al.*
*   [Build Agent Advocates, Not Platform Agents](https://arxiv.org/abs/2505.04345). *Sayash Kapoor, Noam Kolt, Seth Lazar*
*   [Gradual Disempowerment](https://arxiv.org/abs/2501.16946). *Jan Kulveit et al.*

+++

### Aligning what?

*Develop alternatives to agent-level models of alignment, by treating human-AI interactions, AI-assisted institutions, AI economic or cultural systems, drives within one AI, and other causal/constitutive processes as subject to alignment*

*   *Theory of change:* Model multiple reality-shaping processes above and below the level of the individual AI, some of which are themselves quasi-agential (e.g. cultures) or intelligence-like (e.g. markets), will develop AI alignment into a mature science for managing the transition to an AGI civilization
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behavioral / cognitive · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* mixed
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Value is fragile and hard to specify, Corrigibility is anti-natural, Goals misgeneralize out of distribution, Instrumental convergence, Fair, sane pivotal processes
*   *See also:* [Theory for aligning multiple AIs](#Theory_for_aligning_multiple_AIs) · [Aligning to context](#Aligning_to_context) · [Aligned to who?](#Aligned_to_who_)
*   *Some names:* Richard Ngo, Emmett Shear, Softmax, Full Stack Alignment, AI Objectives Institute, Sahil, TJ, Andrew Critch, ACS Research, Jan Kulveit
*   *Funded by:* Future of Life Institute, Emmett Shear
*   *Estimated FTEs:* 5-10

+++ Some outputs (13)

*   [Towards a Scale-Free Theory of Intelligent Agency](https://www.alignmentforum.org/posts/5tYTKX4pNpiG4vzYg/towards-a-scale-free-theory-of-intelligent-agency). *Richard Ngo*
*   [Alignment first, intelligence later](https://chrislakin.blog/p/alignment-first-intelligence-later). *Chris Lakin*
*   [End A Subset Of Conversations](https://www.anthropic.com/research/end-subset-conversations)
*   [Full-Stack Alignment](https://www.full-stack-alignment.ai)
*   [On Eudaimonia and Optimization](https://docs.google.com/document/d/1cKbqYSGspfJavXvnhsp3mAuxHh08rNbP7tzYieqLiXw/edit?tab=t.0%20)
*   [AI Governance through Markets](https://arxiv.org/abs/2501.17755)
*   [Collective cooperative intelligence](https://www.pnas.org/doi/abs/10.1073/pnas.2319948121). *Wolfram Barfuss et al.*
*   [Multipolar AI is Underrated](https://www.lesswrong.com/posts/JjYu75q3hEMBgtvr8/multipolar-ai-is-underrated). *Allison Duettmann*
*   [What, if not agency?](https://www.lesswrong.com/posts/tQ9vWm4b57HFqbaRj/what-if-not-agency)
*   [A Phylogeny of Agents](https://equilibria1.substack.com/p/the-evolution-of-agency-a-research). *Equilibria*
*   [The Multiplicity Thesis, Collective Intelligence, and Morality](https://themultiplicity.ai/blog/thesis). *Andrew Critch*
*   [Hierarchical Alignment](https://www.alignmentforum.org/posts/xud7Mti9jS4tbWqQE/hierarchical-agency-a-missing-piece-in-ai-alignment). *Jan_Kulveit*
*   [Emmett Shear on Building AI That Actually Cares: Beyond Control and Steering](https://a16z.simplecast.com/episodes/emmett-shear-on-building-ai-that-actually-cares-beyond-control-and-steering-TRwfxH0r). *Emmett Shear, Erik Torenberg, Séb Krier*

+++

Evals
=====

### AGI metrics

*Evals with the explicit aim of measuring progress towards full human-level generality.*

*   *Theory of change:* Help predict timelines for risk awareness and strategy.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behavioural · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* mixed
*   *See also:* [Capability evals](#Capability_evals)
*   *Some names:* CAIS, CFI Kinds of Intelligence, Apart Research, OpenAI, METR, Lexin Zhou, Adam Scholl, Lorenzo Pacchiardi
*   *Critiques:* [Is the Definition of AGI a Percentage?](https://aievaluation.substack.com/p/is-the-definition-of-agi-a-percentage), [The "Length" of "Horizons"](https://www.lesswrong.com/posts/PzLSuaT6WGLQGJJJD/the-length-of-horizons)
*   *Funded by:* Leverhulme Trust, Open Philanthropy, Long-Term Future Fund
*   *Estimated FTEs:* 10-50

+++ Some outputs (5)

*   [HCAST: Human-Calibrated Autonomy Software Tasks](https://arxiv.org/abs/2503.17354). *David Rein et al.*
*   [A Definition of AGI](https://arxiv.org/pdf/2510.18212). *Dan Hendrycks et al.*
*   [Remote Labor Index](https://scale.com/leaderboard/rli)
*   [ADeLe v1.0: A battery for AI Evaluation with explanatory and predictive power](https://kinds-of-intelligence-cfi.github.io/ADELE/). *Lexin Zhou et al.*
*   [GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks](https://arxiv.org/abs/2510.04374). *Tejal Patwardhan et al.*

+++

### Capability evals

*Make tools that can actually check whether a model has a certain capability or propensity. We default to low-n sampling of a vast latent space but aim to do better.*

*   *Theory of change:* Keep a close eye on what capabilities are acquired when, so that frontier labs and regulators are better informed on what security measures are already necessary (and hopefully they extrapolate). You can't regulate without them.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behaviorist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *See also:* [Deepmind's frontier safety framework](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/) · [Aether](https://www.lesswrong.com/posts/B8Cmtf5gdHwxb8qtT/aether-july-2025-update)
*   *Some names:* METR, AISI, Apollo Research, Marrius Hobbhahn, Meg Tong, Mary Phuong, Beth Barnes, Thomas Kwa, Joel Becker
*   *Critiques:* [Large Language Models Often Know When They Are Being Evaluated](https://arxiv.org/abs/2505.23836), [AI Sandbagging: Language Models can Strategically Underperform on Evaluations](https://arxiv.org/abs/2406.07358), [The Leaderboard Illusion](https://arxiv.org/abs/2504.20879), [Do Large Language Model Benchmarks Test Reliability?](https://arxiv.org/abs/2502.03461)
*   *Funded by:* basically everyone. Google, Microsoft, Open Philanthropy, LTFF, Governments etc
*   *Estimated FTEs:* 100+

+++ Some outputs (34)

*   [MALT: A Dataset of Natural and Prompted Behaviors That Threaten Eval Integrity](https://metr.org/blog/2025-10-14-malt-dataset-of-natural-and-prompted-behaviors/). *Neev Parikh, Hjalmar Wijk*
*   [Forecasting Rare Language Model Behaviors](https://arxiv.org/abs/2502.16797). *Erik Jones et al.*
*   [Model Tampering Attacks Enable More Rigorous Evaluations of LLM Capabilities](https://arxiv.org/abs/2502.05209). *Zora Che et al.*
*   [The Elicitation Game: Evaluating Capability Elicitation Techniques](https://arxiv.org/abs/2502.02180). *Felix Hofstätter et al.*
*   [Evaluating Language Model Reasoning about Confidential Information](https://arxiv.org/abs/2508.19980). *Dylan Sam et al.*
*   [Evaluating the Goal-Directedness of Large Language Models](https://arxiv.org/abs/2504.11844). *Tom Everitt et al.*
*   [A Toy Evaluation of Inference Code Tampering](https://alignment.anthropic.com/2024/rogue-eval/index.html)
*   [Automated Capability Discovery via Foundation Model Self-Exploration](https://arxiv.org/abs/2502.07577). *Cong Lu, Shengran Hu, Jeff Clune*
*   [Generative Value Conflicts Reveal LLM Priorities](https://arxiv.org/abs/2509.25369). *Andy Liu et al.*
*   [Technical Report: Evaluating Goal Drift in Language Model Agents](https://arxiv.org/abs/2505.02709). *Rauno Arike et al.*
*   [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
*   [When Ethics and Payoffs Diverge: LLM Agents in Morally Charged Social Dilemmas](https://arxiv.org/abs/2505.19212). *Steffen Backmann et al.*
*   [AILuminate: Introducing v1.0 of the AI Risk and Reliability Benchmark from MLCommons](https://arxiv.org/abs/2503.05731). *Shaona Ghosh et al.*
*   [Petri: An open-source auditing tool to accelerate AI safety research](https://www.anthropic.com/research/petri-open-source-auditing). *Kai Fronsdal et al.*
*   [Research Note: Our scheming precursor evals had limited predictive power for our in-context scheming evals](https://www.apolloresearch.ai/blog/research-note-our-scheming-precursor-evals-had-limited-predictive-power-for-our-in-context-scheming-evals). *Marius Hobbhahn*
*   [Hyperbolic model fits METR capabilities estimate worse than exponential model](https://lesswrong.com/posts/ZEuDH2W3XdRaTwpjD/hyperbolic-model-fits-metr-capabilities-estimate-worse-than). *gjm*
*   [New website analyzing AI companies' model evals](https://lesswrong.com/posts/nmaKpoHxmzjT8yXTk/new-website-analyzing-ai-companies-model-evals). *Zach Stein-Perlman*
*   [Research Note: Our scheming precursor evals had limited predictive power for our in-context scheming evals](https://lesswrong.com/posts/9tqpPP4FwSnv9AWsi/research-note-our-scheming-precursor-evals-had-limited). *Marius Hobbhahn*
*   [How Fast Can Algorithms Advance Capabilities? | Epoch Gradient Update](https://lesswrong.com/posts/qhjNejRxbMGQp4wHt/how-fast-can-algorithms-advance-capabilities-or-epoch). *Henry Josephson et al.*
*   [Safety by Measurement: A Systematic Literature Review of AI Safety Evaluation Methods](https://lesswrong.com/posts/CwdCYmsutwXwnYtEF/paper-safety-by-measurement-a-systematic-literature-review). *markov, Charbel-Raphaël*
*   [Adversarial ML Problems Are Getting Harder to Solve and to Evaluate](https://arxiv.org/abs/2502.02260). *Javier Rando et al.*
*   [Predicting the Performance of Black-box LLMs through Self-Queries](https://arxiv.org/abs/2501.01558). *Dylan Sam, Marc Finzi, J. Zico Kolter*
*   [Among AIs](https://www.4wallai.com/amongais)
*   [Safety by Measurement: A Systematic Literature Review of AI Safety Evaluation Methods](https://arxiv.org/abs/2505.05541). *Markov Grey, Charbel-Raphaël Segerie*
*   [Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index](https://arxiv.org/abs/2506.12229). *Hao Xu et al.*
*   [We should try to automate AI safety work asap](https://lesswrong.com/posts/W3KfxjbqBAnifBQoi/we-should-try-to-automate-ai-safety-work-asap). *Marius Hobbhahn*
*   [Validating against a misalignment detector is very different to training against one](https://lesswrong.com/posts/CXYf7kGBecZMajrXC/validating-against-a-misalignment-detector-is-very-different). *mattmacdermott*
*   [Why do misalignment risks increase as AIs get more capable?](https://lesswrong.com/posts/NDotm7oLHfR56g4sD/why-do-misalignment-risks-increase-as-ais-get-more-capable). *Ryan Greenblatt*
*   [Open Philanthropy Technical AI Safety RFP - $40M Available Across 21 Research Areas](https://lesswrong.com/posts/wbJxRNxuezvsGFEWv/open-philanthropy-technical-ai-safety-rfp-usd40m-available). *jake_mendel, maxnadeau, Peter Favaloro*
*   [Correlating and Predicting Human Evaluations of Language Models from Natural Language Processing Benchmarks](https://arxiv.org/abs/2502.18339). *Rylan Schaeffer et al.*
*   [Why Future AIs will Require New Alignment Methods](https://lesswrong.com/posts/TxiB6hvnQqxXB5XDJ/why-future-ais-will-require-new-alignment-methods). *Alvin Ånestrand*
*   [100+ concrete projects and open problems in evals](https://lesswrong.com/posts/LhnqegFoykcjaXCYH/100-concrete-projects-and-open-problems-in-evals). *Marius Hobbhahn*
*   [AI companies should be safety-testing the most capable versions of their models](https://lesswrong.com/posts/tQzeafo9HjCeXn7ZF/ai-companies-should-be-safety-testing-the-most-capable). *Steven Adler*
*   [The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground Responses to Long-Form Input](https://arxiv.org/abs/2501.03200). *Alon Jacovi et al.*

+++

### Autonomy evals

*Measure an AI's ability to act autonomously to complete long-horizon, complex tasks.*

*   *Theory of change:* By measuring how long and complex a task an AI can complete (its "time horizon"), we can track capability growth and identify when models gain dangerous autonomous capabilities (like R&D acceleration or replication).
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behaviorist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *See also:* [Capability evals](#Capability_evals) · [OpenAI Preparedness](https://openai.com/index/updating-our-preparedness-framework/) · [Anthropic RSP](https://www.anthropic.com/rsp-updates)
*   *Some names:* METR, Thomas Kwa, Ben West, Joel Becker, Beth Barnes, Hjalmar Wijk, Tao Lin, Giulio Starace, Oliver Jaffe, Dane Sherburn, Sanidhya Vijayvargiya, Aditya Bharat Soni, Xuhui Zhou
*   *Critiques:* [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity.](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) [The "Length" of "Horizons"](https://www.lesswrong.com/posts/PzLSuaT6WGLQGJJJD/the-length-of-horizons)
*   *Funded by:* The Audacious Project, Open Philanthropy
*   *Estimated FTEs:* 10-50

+++ Some outputs (13)

*   [Fulcrum](https://fulcrumresearch.ai/2025/10/22/introducing-orchestra-quibbler.html)
*   [Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/). *Thomas Kwa et al.*
*   [Details about METR's evaluation of OpenAI GPT-5](https://metr.github.io/autonomy-evals-guide/gpt-5-report/)
*   [RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts](https://arxiv.org/abs/2411.15114). *Hjalmar Wijk et al.*
*   [OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents](https://arxiv.org/abs/2506.14866). *Thomas Kuntz et al.*
*   [OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety](https://t.co/XfspwlzYdl). *Sanidhya Vijayvargiya et al.*
*   [Details about METR's preliminary evaluation of OpenAI's o3 and o4-mini](https://metr.github.io/autonomy-evals-guide/openai-o3-report/). *METR*
*   [PaperBench: Evaluating AI's Ability to Replicate AI Research](https://t.co/dHN2N0tUhC). *Giulio Starace et al.*
*   [How Does Time Horizon Vary Across Domains?](https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains/)
*   [Vending-Bench: A Benchmark for Long-Term Coherence of Autonomous Agents](https://arxiv.org/abs/2502.15840). *Axel Backlund, Lukas Petersson*
*   [Forecasting Frontier Language Model Agent Capabilities](https://arxiv.org/abs/2502.15850). *Govind Pimpale et al.*
*   [Project Vend: Can Claude run a small shop? (And why does that matter?)](https://www.anthropic.com/research/project-vend-1)
*   [GSM-Agent: Understanding Agentic Reasoning Using Controllable Environments](https://arxiv.org/abs/2509.21998). *Hanlin Zhu et al.*

+++

### WMD evals (Weapons of Mass Destruction)

*Evaluate whether AI models possess dangerous knowledge or capabilities related to biological and chemical weapons, such as biosecurity or chemical synthesis.*

*   *Theory of change:* By benchmarking and tracking AI's knowledge of biology and chemistry, we can identify when models become capable of accelerating WMD development or misuse, allowing for timely intervention.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behaviorist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *See also:* [Capability evals](#Capability_evals) · [Autonomy evals](#Autonomy_evals) · [Various Redteams](#Various_Redteams)
*   *Some names:* Lennart Justen, Haochen Zhao, Xiangru Tang, Ziran Yang, Aidan Peppin, Anka Reuel, Stephen Casper
*   *Critiques:* [The Reality of AI and Biorisk](https://arxiv.org/abs/2412.01946)
*   *Funded by:* Open Philanthropy, UK AI Safety Institute (AISI), frontier labs, Scale AI, various academic institutions (Peking University, Yale, etc.), Meta
*   *Estimated FTEs:* 10-50

+++ Some outputs (6)

*   [Virology Capabilities Test (VCT): A Multimodal Virology Q&A Benchmark](https://arxiv.org/abs/2504.16137). *Jasper Götting et al.*
*   [LLMs Outperform Experts on Challenging Biology Benchmarks](https://arxiv.org/abs/2505.06108). *Lennart Justen*
*   [The Safety Gap Toolkit: Evaluating Hidden Dangers of Open-Source Models](https://arxiv.org/abs/2507.11544). *Ann-Kathrin Dombrowski et al.*
*   [Best Practices for Biorisk Evaluations on Open-Weight Bio-Foundation Models](https://arxiv.org/abs/2510.27629). *Boyi Wei et al.*
*   [ChemSafetyBench: Benchmarking LLM Safety on Chemistry Domain](https://arxiv.org/abs/2411.16736). *Haochen Zhao et al.*
*   [The Reality of AI and Biorisk](https://arxiv.org/abs/2412.01946). *Aidan Peppin et al.*

+++

### Situational awareness and self-awareness evals

*Evaluate if models understand their own internal states and behaviors, their environment, and whether they are in a test or real-world deployment.*

*   *Theory of change:* If an AI can distinguish between evaluation and deployment ("evaluation awareness"), it might hide dangerous capabilities (scheming/sandbagging). By measuring self- and situational-awareness, we can better assess this risk and build more robust evaluations.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behaviorist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Superintelligence can fool human supervisors, Superintelligence can hack software supervisors
*   *See also:* [Sandbagging evals](#Sandbagging_evals) · [Various Redteams](#Various_Redteams) · [Model psychology](#Model_psychology)
*   *Some names:* Jan Betley, Xuchan Bao, Martín Soto, Mary Phuong, Roland S. Zimmermann, Joe Needham, Giles Edkins, Govind Pimpale, Kai Fronsdal, David Lindner, Lang Xiong, Xiaoyan Bai
*   *Critiques:* [Lessons from a Chimp: AI "Scheming" and the Quest for Ape Language](https://arxiv.org/abs/2507.03409), [It's hard to make scheming evals look realistic for LLMs](https://www.lesswrong.com/posts/TBk2dbWkg2F7dB3jb/it-s-hard-to-make-scheming-evals-look-realistic-for-llms)
*   *Funded by:* frontier labs (Google DeepMind, Anthropic), Open Philanthropy, The Audacious Project, UK AI Safety Institute (AISI), AI Safety Support, Apollo Research, METR
*   *Estimated FTEs:* 30-70

+++ Some outputs (11)

*   [AI Awareness (literature review)](https://arxiv.org/pdf/2504.20084). *Xiaojian Li et al.*
*   [Tell me about yourself: LLMs are aware of their learned behaviors](https://arxiv.org/abs/2501.11120). *Jan Betley et al.*
*   [Evaluating Frontier Models for Stealth and Situational Awareness](https://arxiv.org/abs/2505.01420). *Mary Phuong et al.*
*   [Large Language Models Often Know When They Are Being Evaluated](https://arxiv.org/abs/2505.23836). *Joe Needham et al.*
*   [Do LLMs know what they're capable of? Why this matters for AI safety, and initial findings](https://lesswrong.com/posts/9tHEibBBhQCHEyFsa/do-llms-know-what-they-re-capable-of-why-this-matters-for-ai). *Casey Barkan, Sid Black, Oliver Sourbut*
*   [Probe-Rewrite-Evaluate: A Workflow for Reliable Benchmarks and Quantifying Evaluation Awareness](https://arxiv.org/abs/2509.00591). *Lang Xiong et al.*
*   [Claude Sonnet 3.7 (often) knows when it's in alignment evaluations](https://lesswrong.com/posts/E3daBewppAiECN3Ao/claude-sonnet-3-7-often-knows-when-it-s-in-alignment). *Nicholas Goldowsky-Dill et al.*
*   [It's hard to make scheming evals look realistic for LLMs](https://lesswrong.com/posts/TBk2dbWkg2F7dB3jb/it-s-hard-to-make-scheming-evals-look-realistic-for-llms). *Igor Ivanov, Danil Kadochnikov*
*   [Know Thyself? On the Incapability and Implications of AI Self-Recognition](https://arxiv.org/abs/2510.03399). *Xiaoyan Bai et al.*
*   [Chain-of-Thought Snippets — Anti-Scheming](https://www.antischeming.ai/snippets)
*   [Future Events as Backdoor Triggers](https://arxiv.org/pdf/2407.04108). *Sara Price et al.*

+++

### Steganography evals

*evaluate whether models can hide secret information or encoded reasoning in their outputs, such as in chain-of-thought scratchpads, to evade monitoring.*

*   *Theory of change:* if models can use steganography, they could hide deceptive reasoning, bypassing safety monitoring and control measures. By evaluating this capability, we can assess the risk of a model fooling its supervisors.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behavioral · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): A boxed AGI might exfiltrate itself by steganography, spearphishing, Superintelligence can fool human supervisors
*   *See also:* [AI deception evals](#AI_deception_evals) · [Chain of thought monitoring](#Chain_of_thought_monitoring)
*   *Some names:* Antonio Norelli, Michael Bronstein
*   *Critiques:* Chain-of-Thought Is Already Unfaithful (So Steganography is Irrelevant): [Reasoning Models Don't Always Say What They Think.](https://assets.anthropic.com/m/71876fabef0f0ed4/original/reasoning_models_paper.pdf)
*   *Funded by:* Anthropic (and its general funders, e.g., Google, Amazon)
*   *Estimated FTEs:* 1-10

+++ Some outputs (5)

*   [Large language models can learn and generalize steganographic chain-of-thought under process supervision](https://arxiv.org/abs/2506.01926). *Joey Skaf et al.*
*   [Early Signs of Steganographic Capabilities in Frontier LLMs](https://arxiv.org/abs/2507.02737). *Artur Zolkowski et al.*
*   [Subliminal Learning: Language models transmit behavioural traits via hidden signals in data](https://arxiv.org/abs/2507.14805). *Alex Cloud et al.*
*   [LLMs can hide text in other text of the same length](https://arxiv.org/abs/2510.20075). *Antonio Norelli, Michael Bronstein*
*   [Do reasoning models use their scratchpad like we do? Evidence from distilling paraphrases](https://alignment.anthropic.com/2025/distill-paraphrases/)

+++

### AI deception evals

*research demonstrating that AI models, particularly agentic ones, can learn and execute deceptive behaviors such as alignment faking, manipulation, and sandbagging.*

*   *Theory of change:* proactively discover, evaluate, and understand the mechanisms of AI deception (e.g., alignment faking, manipulation, agentic deception) to prevent models from fooling human supervisors and causing harm.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behavioral / engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Superintelligence can fool human supervisors, Superintelligence can hack software supervisors
*   *See also:* [Situational awareness and self-awareness evals](#Situational_awareness_and_self_awareness_evals) · [Steganography evals](#Steganography_evals) · [Sandbagging evals](#Sandbagging_evals) · [Chain of thought monitoring](#Chain_of_thought_monitoring)
*   *Some names:* Cadenza, Fred Heiding, Simon Lermen, Andrew Kao, Myra Cheng, Cinoo Lee, Pranav Khadpe, Satyapriya Krishna, Andy Zou, Rahul Gupta
*   *Critiques:* A central criticism is that the evaluation scenarios are "artificial and contrived". [the void](https://nostalgebraist.tumblr.com/post/785766737747574784/the-void) and [Lessons from a Chimp](https://arxiv.org/abs/2507.03409) argue this research is "overattributing human traits" to models.
*   *Funded by:* Labs, academic institutions (e.g., Harvard, CMU, Barcelona Institute of Science and Technology), NSFC, ML Alignment Theory & Scholars (MATS) Program, FAR AI
*   *Estimated FTEs:* 30-80

+++ Some outputs (13)

*   [Liars' Bench: Evaluating Lie Detectors for Language Models](https://arxiv.org/abs/2511.16035). *Kieron Kretschmar et al.*
*   [DECEPTIONBENCH: A Comprehensive Benchmark for AI Deception Behaviors in Real-world Scenario](https://arxiv.org/pdf/2510.15501). *Yao Huang et al.*
*   [Why Do Some Language Models Fake Alignment While Others Don't?](https://arxiv.org/pdf/2506.18032). *Abhay Sheshadri et al.*
*   [Alignment Faking Revisited: Improved Classifiers and Open Source Extensions](https://alignment.anthropic.com/2025/alignment-faking-revisited/). *John Hughes, Abhay Sheshadr*
*   [D-REX: A Benchmark for Detecting Deceptive Reasoning in Large Language Models](https://arxiv.org/abs/2509.17938). *Satyapriya Krishna et al.*
*   [Evaluating & Reducing Deceptive Dialogue From Language Models with Multi-turn RL](https://arxiv.org/abs/2510.14318). *Marwa Abdulhai et al.*
*   [Among Us: A Sandbox for Measuring and Detecting Agentic Deception](https://arxiv.org/abs/2504.04072). *Satvik Golechha, Adrià Garriga-Alonso*
*   [Eliciting Secret Knowledge from Language Models](https://arxiv.org/abs/2510.01070). *Bartosz Cywiński et al.*
*   [Edge Cases in AI Alignment](https://lesswrong.com/posts/bqWihHtDnDseyfF2T/edge-cases-in-ai-alignment-2). *Florian Dietz*
*   [The MASK Evaluation](https://huggingface.co/datasets/cais/MASK)
*   [I replicated the Anthropic alignment faking experiment on other models, and they didn't fake alignment](https://lesswrong.com/posts/pCMmLiBcHbKohQgwA/i-replicated-the-anthropic-alignment-faking-experiment-on). *Aleksandr Kedrik, Igor Ivanov*
*   [Evaluating Large Language Models' Capability to Launch Fully Automated Spear Phishing Campaigns: Validated on Human Subjects](https://arxiv.org/abs/2412.00586). *Fred Heiding et al.*
*   [Mistral Large 2 (123B) seems to exhibit alignment faking](https://lesswrong.com/posts/kCGk5tp5suHoGwhCa/mistral-large-2-123b-seems-to-exhibit-alignment-faking). *Marc Carauleanu et al.*

+++

### AI scheming evals

*Evaluate frontier models for scheming, a sophisticated, strategic form of AI deception where a model covertly pursues a misaligned, long-term objective while deliberately faking alignment and compliance to evade detection by human supervisors and safety mechanisms.*

*   *Theory of change:* Robust evaluations must move beyond checking final outputs and probe the model's reasoning to verify that alignment is genuine, not faked, because capable models are capable of strategically concealing misaligned goals (scheming) to pass standard behavioural evaluations.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behavioral / engineering · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Superintelligence can fool human supervisors
*   *See also:* [AI deception evals](#AI_deception_evals) · [Situational awareness and self-awareness evals](#Situational_awareness_and_self_awareness_evals)
*   *Some names:* Bronson Schoen, Alexander Meinke, Jason Wolfe, Mary Phuong, Rohin Shah, Evgenia Nitishinskaya, Mikita Balesni, Marius Hobbhahn, Jérémy Scheurer, Wojciech Zaremba, David Lindner
*   *Critiques:* [No, LLMs are not "scheming"](https://www.strangeloopcanon.com/p/no-llms-are-not-scheming)
*   *Funded by:* OpenAI, Anthropic, Google DeepMind, Open Philanthropy
*   *Estimated FTEs:* 30-60

+++ Some outputs (7)

*   [Detecting and reducing scheming in AI models](https://openai.com/index/detecting-and-reducing-scheming-in-ai-models/). *OpenAI*
*   [Evaluating and Understanding Scheming Propensity in LLM Agents](https://static1.squarespace.com/static/660eea75305d9a0e1148118a/t/691f711c4ac57d3831260538/1763668252592/scheming-propensity.pdf)
*   [Stress Testing Deliberative Alignment for Anti-Scheming Training](https://www.arxiv.org/pdf/2509.15541). *Bronson Schoen et al.*
*   [Scheming Ability in LLM-to-LLM Strategic Interactions](https://arxiv.org/html/2510.12826v1). *Thao Pham*
*   [Frontier Models are Capable of In-context Scheming](https://arxiv.org/abs/2412.04984). *Alexander Meinke et al.*
*   [Agentic Misalignment](https://arxiv.org/abs/2510.05179). *Aengus Lynch et al.*
*   [Testing for Scheming with Model Deletion](https://www.lesswrong.com/posts/D5kGGGhsnfH7G8v9f/testing-for-scheming-with-model-deletion)

+++

### Sandbagging evals

*Evaluate whether AI models deliberately hide their true capabilities or underperform, especially when they detect they are in an evaluation context.*

*   *Theory of change:* If models can distinguish between evaluation and deployment contexts ("evaluation awareness"), they might learn to "sandbag" or deliberately underperform to hide dangerous capabilities, fooling safety evaluations. By developing evaluations for sandbagging, we can test whether our safety methods are being deceived and detect this behavior before a model is deployed.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behaviorist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* pessimistic
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Superintelligence can fool human supervisors, Superintelligence can hack software supervisors
*   *See also:* [AI deception evals](#AI_deception_evals) · [Situational awareness and self-awareness evals](#Situational_awareness_and_self_awareness_evals) · [Various Redteams](#Various_Redteams)
*   *Some names:* Teun van der Weij, Cameron Tice, Chloe Li, Johannes Gasteiger, Joseph Bloom, Joel Dyer
*   *Critiques:* The main external critique, from sources like "[the void](https://nostalgebraist.tumblr.com/post/785766737747574784/the-void)" and "[Lessons from a Chimp](https://arxiv.org/abs/2507.03409)", is that this research "overattribut\[es\] human traits" to models. It argues that what's being measured isn't genuine sandbagging but models "playing-along-with-drama behaviour" in response to "artificial and contrived" evals.
*   *Funded by:* Anthropic (and its funders, e.g., Google, Amazon), UK Government (funding the AI Security Institute)
*   *Estimated FTEs:* 10-50

+++ Some outputs (9)

*   [Noise Injection Reveals Hidden Capabilities of Sandbagging Language Models](https://arxiv.org/pdf/2412.01784). *Cameron Tice et al.*
*   [Sandbagging in a Simple Survival Bandit Problem](https://arxiv.org/pdf/2509.26239). *Joel Dyer et al.*
*   [Strategic Dishonesty Can Undermine AI Safety Evaluations of Frontier LLMs](https://arxiv.org/abs/2509.18058). *Alexander Panfilov et al.*
*   [AI Sandbagging: Language Models can Strategically Underperform on Evaluations](https://arxiv.org/abs/2406.07358). *Teun van der Weij et al.*
*   [Automated Researchers Can Subtly Sandbag](https://alignment.anthropic.com/2025/automated-researchers-sandbag/). *Johannes Gasteiger et al.*
*   [LLMs Can Covertly Sandbag on Capability Evaluations Against Chain-of-Thought Monitoring](https://arxiv.org/abs/2508.00943). *Chloe Li, Mary Phuong, Noah Y. Siegel*
*   [White Box Control at UK AISI - Update on Sandbagging Investigations](https://www.alignmentforum.org/posts/pPEeMdgjpjHZWCDFw/white-box-control-at-uk-aisi-update-on-sandbagging). *Joseph Bloom et al.*
*   [Misalignment and Strategic Underperformance: An Analysis of Sandbagging and Exploration Hacking](https://lesswrong.com/posts/TeTegzR8X5CuKgMc3/misalignment-and-strategic-underperformance-an-analysis-of). *Buck Shlegeris, Julian Stastny*
*   [Won't vs. Can't: Sandbagging-like Behavior from Claude Models](https://alignment.anthropic.com/2025/wont-vs-cant/)

+++

### Self-replication evals

*evaluate whether AI agents can autonomously replicate themselves by obtaining their own weights, securing compute resources, and creating copies of themselves.*

*   *Theory of change:* if AI agents gain the ability to self-replicate, they could proliferate uncontrollably, making them impossible to shut down. By measuring this capability with benchmarks like RepliBench, we can identify when models cross this dangerous "red line" and implement controls before losing containment.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behaviorist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* worst-case
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): Instrumental convergence, A boxed AGI might exfiltrate itself by steganography, spearphishing
*   *See also:* [Autonomy evals](#Autonomy_evals) · [Situational awareness and self-awareness evals](#Situational_awareness_and_self_awareness_evals)
*   *Some names:* Sid Black, Asa Cooper Stickland, Jake Pencharz, Oliver Sourbut, Michael Schmatz, Jay Bailey, Ollie Matthews, Ben Millwood, Alex Remedios, Alan Cooney, Xudong Pan, Jiarun Dai, Yihe Fan
*   *Critiques:* [AI Sandbagging](https://arxiv.org/abs/2406.07358)
*   *Funded by:* UK Government (via UK AI Safety Institute)
*   *Estimated FTEs:* 10-20

+++ Some outputs (3)

*   [Large language model-powered AI systems achieve self-replication with no human intervention](https://arxiv.org/abs/2503.17378). *Xudong Pan et al.*
*   [A Realistic Evaluation of Self-Replication Risk in LLM Agents](https://arxiv.org/abs/2509.25302). *Boxuan Zhang et al.*
*   [RepliBench: measuring autonomous replication capabilities in AI systems](https://aisi.gov.uk/work/replibench-measuring-autonomous-replication-capabilities-in-ai-systems)

+++

### Various Redteams

*attack current models and see what they do / deliberately induce bad things on current frontier models to test out our theories / methods.*

*   *Theory of change:* to ensure models are safe, we must actively try to break them. By developing and applying a diverse suite of attacks (e.g., in novel domains, against agentic systems, or using automated tools), researchers can discover vulnerabilities, specification gaming, and deceptive behaviors before they are exploited, thereby informing the development of more robust defenses.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behaviorist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *Orthodox alignment* [*problems*](https://docs.google.com/document/d/1xRtmO_TLgPeHxWNQFN0kkNnd6jfiUettPfEcdl6FIc0/view): A boxed AGI might exfiltrate itself by steganography, spearphishing, Goals misgeneralize out of distribution
*   *See also:* [Other evals](#Other_evals)
*   *Some names:* Ryan Greenblatt, Benjamin Wright, Aengus Lynch, John Hughes, Samuel R. Bowman, Andy Zou, Nicholas Carlini, Abhay Sheshadri
*   *Critiques:* [Claude Sonnet 3.7 (often) knows when it's in alignment evaluations](https://www.alignmentforum.org/posts/E3daBewppAiECN3Ao/claude-sonnet-3-7-often-knows-when-it-s-in-alignment), [Red Teaming AI Red Teaming.](https://arxiv.org/html/2507.05538v1)
*   *Funded by:* Frontier labs (Anthropic, OpenAI, Google), government (UK AISI), Open Philanthropy, LTFF, academic grants.
*   *Estimated FTEs:* 100+

+++ Some outputs (57)

*   [WildTeaming at Scale: From In-the-Wild Jailbreaks to (Adversarially) Safer Language Models](https://arxiv.org/pdf/2406.18510). *Liwei Jiang et al.*
*   [In-Context Representation Hijacking](https://arxiv.org/abs/2512.03771). *Itay Yona et al.*
*   [Building and evaluating alignment auditing agents](https://alignment.anthropic.com/2025/automated-auditing/). *Trenton Bricken et al.*
*   [Findings from a Pilot Anthropic—OpenAI Alignment Evaluation Exercise](https://t.co/wk0AP8aDNI). *Samuel R. Bowman et al.*
*   [Agentic Misalignment: How LLMs could be insider threats](https://t.co/XFtd0H2Pzb). *Aengus Lynch et al.*
*   [Compromising Honesty and Harmlessness in Language Models via Deception Attacks](https://arxiv.org/abs/2502.08301). *Laurène Vaugrante et al.*
*   [Eliciting Language Model Behaviors with Investigator Agents](https://arxiv.org/abs/2502.01236). *Xiang Lisa Li et al.*
*   [Shutdown Resistance in Large Language Models](https://arxiv.org/abs/2509.14260). *Jeremy Schlatter, Benjamin Weinstein-Raun, Jeffrey Ladish*
*   [Stress Testing Deliberative Alignment for Anti-Scheming Training](https://arxiv.org/abs/2509.15541). *Bronson Schoen et al.*
*   [Chain-of-Thought Hijacking](https://arxiv.org/abs/2510.26418). *Jianli Zhao et al.*
*   [X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents](https://arxiv.org/abs/2504.13203). *Salman Rahman et al.*
*   [Agentic Misalignment: How LLMs Could be Insider Threats](https://lesswrong.com/posts/b8eeCGe3FWzHKbePF/agentic-misalignment-how-llms-could-be-insider-threats-1). *Aengus Lynch et al.*
*   [Illusory Safety: Redteaming DeepSeek R1 and the Strongest Fine-Tunable Models of OpenAI, Anthropic, and Google](https://lesswrong.com/posts/zjqrSKZuRLnjAniyo/illusory-safety-redteaming-deepseek-r1-and-the-strongest). *ChengCheng et al.*
*   [Why Do Some Language Models Fake Alignment While Others Don't?](https://arxiv.org/abs/2506.18032). *Abhay Sheshadri et al.*
*   [Demonstrating specification gaming in reasoning models](https://arxiv.org/abs/2502.13295). *Alexander Bondarenko et al.*
*   [Jailbreak-Tuning: Models Efficiently Learn Jailbreak Susceptibility](https://arxiv.org/abs/2507.11630). *Brendan Murphy et al.*
*   [Monitoring Decomposition Attacks in LLMs with Lightweight Sequential Monitors](https://arxiv.org/abs/2506.10949). *Chen Yueh-Han et al.*
*   [Diverse and Effective Red Teaming with Auto-generated Rewards and Multi-step Reinforcement Learning](https://arxiv.org/abs/2412.18693). *Alex Beutel et al.*
*   [Call Me A Jerk: Persuading AI to Comply with Objectionable Requests](https://t.co/tkHkVFVZ2m). *Lennart Meincke et al.*
*   [RedDebate: Safer Responses through Multi-Agent Red Teaming Debates](https://arxiv.org/abs/2506.11083). *Ali Asad et al.*
*   [The Structural Safety Generalization Problem](https://arxiv.org/abs/2504.09712). *Julius Broomfield et al.*
*   [No, of Course I Can! Deeper Fine-Tuning Attacks That Bypass Token-Level Safety Mechanisms](https://arxiv.org/abs/2502.19537). *Joshua Kazdan et al.*
*   [Fundamental Limitations in Pointwise Defences of LLM Finetuning APIs](https://arxiv.org/abs/2502.14828). *Xander Davies et al.*
*   [STACK: Adversarial Attacks on LLM Safeguard Pipelines](https://arxiv.org/abs/2506.24068). *Ian R. McKenzie et al.*
*   [Adversarial Manipulation of Reasoning Models using Internal Representations](https://arxiv.org/abs/2507.03167). *Kureha Yamaguchi, Benjamin Etheridge, Andy Arditi*
*   [Discovering Forbidden Topics in Language Models](https://arxiv.org/abs/2505.17441). *Can Rager et al.*
*   [RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261). *Rohan Gupta, Erik Jenner*
*   [Jailbreak Transferability Emerges from Shared Representations](https://arxiv.org/abs/2506.12913). *Rico Angell, Jannik Brinkmann, He He*
*   [Mitigating Many-Shot Jailbreaking](https://arxiv.org/abs/2504.09604). *Christopher M. Ackerman, Nina Panickssery*
*   [Active Attacks: Red-teaming LLMs via Adaptive Environments](https://arxiv.org/abs/2509.21947). *Taeyoung Yun et al.*
*   [LLM Robustness Leaderboard v1 --Technical report](https://arxiv.org/abs/2508.06296). *Pierre Peigné - Lefebvre et al.*
*   [Jailbreak Defense in a Narrow Domain: Limitations of Existing Methods and a New Transcript-Classifier Approach](https://arxiv.org/abs/2412.02159). *Tony T. Wang et al.*
*   [It's the Thought that Counts: Evaluating the Attempts of Frontier LLMs to Persuade on Harmful Topics](https://arxiv.org/abs/2506.02873). *Matthew Kowal et al.*
*   [Discovering Undesired Rare Behaviors via Model Diff Amplification](https://www.goodfire.ai/papers/model-diff-amplification). *Santiago Aranguri, Thomas McGrath*
*   [REINFORCE Adversarial Attacks on Large Language Models: An Adaptive, Distributional, and Semantic Objective](https://arxiv.org/abs/2502.17254). *Simon Geisler et al.*
*   [Adversarial Attacks on Robotic Vision Language Action Models](https://arxiv.org/abs/2506.03350). *Eliot Krzysztof Jones et al.*
*   [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://arxiv.org/abs/2503.14827). *Chejian Xu et al.*
*   [Toward Understanding the Transferability of Adversarial Suffixes in Large Language Models](https://arxiv.org/abs/2510.22014). *Sarah Ball et al.*
*   [Will alignment-faking Claude accept a deal to reveal its misalignment?](https://lesswrong.com/posts/7C4KJot4aN8ieEDoz/will-alignment-faking-claude-accept-a-deal-to-reveal-its). *Ryan Greenblatt, Kyle Fish*
*   [Petri: An open-source auditing tool to accelerate AI safety research](https://alignment.anthropic.com/2025/petri/)
*   ['For Argument's Sake, Show Me How to Harm Myself!': Jailbreaking LLMs in Suicide and Self-Harm Contexts](https://arxiv.org/pdf/2507.02990). *Annika M Schoene, Cansu Canca*
*   [Winning at All Cost: A Small Environment for Eliciting Specification Gaming Behaviors in Large Language Models](https://arxiv.org/abs/2505.07846). *Lars Malmqvist*
*   [Uncovering Gaps in How Humans and LLMs Interpret Subjective Language](https://arxiv.org/abs/2503.04113). *Erik Jones, Arjun Patrawala, Jacob Steinhardt*
*   [RedCodeAgent: Automatic Red-teaming Agent against Diverse Code Agents](https://arxiv.org/abs/2510.02609). *Chengquan Guo et al.*
*   [MIP against Agent: Malicious Image Patches Hijacking Multimodal OS Agents](https://arxiv.org/abs/2503.10809). *Lukas Aichberger et al.*
*   [Trading Inference-Time Compute for Adversarial Robustness](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness). *OpenAI*
*   [Research directions Open Phil wants to fund in technical AI safety](https://lesswrong.com/posts/26SHhxK2yYQbh7ors/research-directions-open-phil-wants-to-fund-in-technical-ai). *jake_mendel, maxnadeau, Peter Favaloro*
*   [When does Claude sabotage code? An Agentic Misalignment follow-up](https://lesswrong.com/posts/9i6fHMn2vTqyzAi9o/when-does-claude-sabotage-code-an-agentic-misalignment). *Nathan Delisle*
*   [Can a Neural Network that only Memorizes the Dataset be Undetectably Backdoored?](https://openreview.net/forum?id=TD1NfQuVr6). *Matjaz Leonardis*
*   [Multi-Agent Step Race Benchmark: Assessing LLM Collaboration and Deception Under Pressure](https://github.com/lechmazur/step_game). *lechmazur, eltociear*
*   [ToolTweak: An Attack on Tool Selection in LLM-based Agents](https://arxiv.org/abs/2510.02554). *Jonathan Sneh et al.*
*   [Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents](https://arxiv.org/abs/2503.00061). *Qiusi Zhan et al.*
*   [Petri: An open-source auditing tool to accelerate AI safety research](https://lesswrong.com/posts/kffbZGa2yYhc6cakc/petri-an-open-source-auditing-tool-to-accelerate-ai-safety)
*   [Quantifying the Unruly: A Scoring System for Jailbreak Tactics](https://0din.ai/blog/quantifying-the-unruly-a-scoring-system-for-jailbreak-tactics). *Pedram Amini*
*   [Adversarial Alignment for LLMs Requires Simpler, Reproducible, and More Measurable Objectives](https://arxiv.org/abs/2502.11910). *Leo Schwinn et al.*
*   [Transferable Adversarial Attacks on Black-Box Vision-Language Models](https://arxiv.org/abs/2505.01050). *Kai Hu et al.*
*   [Advancing Gemini's security safeguards](https://deepmind.google/discover/blog/advancing-geminis-security-safeguards/). *Google DeepMind Security & Privacy Research Team*

+++

### Other evals

*A collection of miscellaneous evaluations for specific alignment properties, such as honesty, shutdown resistance and sycophancy.*

*   *Theory of change:* By developing novel benchmarks for specific, hard-to-measure properties (like honesty), critiquing the reliability of existing methods (like cultural surveys), and improving the formal rigor of evaluation systems (like LLM-as-Judges), researchers can create a more robust and comprehensive suite of evaluations to catch failures missed by standard capability or safety testing.
*   *General* [*approach*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* behaviorist science · *Target* [*case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research)*:* average
*   *See also:* other more specific sections on evals
*   *Some names:* Richard Ren, Mantas Mazeika, Andrés Corrada-Emmanuel, Ariba Khan, Stephen Casper
*   *Critiques:* [The Unreliability of Evaluating Cultural Alignment in LLMs](https://arxiv.org/abs/2503.08688), [The Leaderboard Illusion](https://arxiv.org/abs/2504.20879)
*   *Funded by:* Lab funders (OpenAI), Open Philanthropy (which funds CAIS, the organization for the MASK benchmark), academic institutions. N/A (as a discrete amount). This work is part of the "tens of millions" budgets for broader evaluation and red-teaming efforts at labs and independent organizations.
*   *Estimated FTEs:* 20-50

+++ Some outputs (20)

*   [Shutdown Resistance in Large Language Models](https://arxiv.org/abs/2509.14260). *Jeremy Schlatter, Benjamin Weinstein-Raun, Jeffrey Ladish*
*   [OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety](https://arxiv.org/abs/2507.06134). *Sanidhya Vijayvargiya et al.*
*   [Do LLMs Comply Differently During Tests? Is This a Hidden Variable in Safety Evaluation? And Can We Steer That?](https://lesswrong.com/posts/B2o6nrxwKxLPsSYdh/do-llms-comply-differently-during-tests-is-this-a-hidden). *Sahar Abdelnabi, Ahmed Salem*
*   [Systematic runaway-optimiser-like LLM failure modes on Biologically and Economically aligned AI safety benchmarks for LLMs with simplified observation format (BioBlue)](https://lesswrong.com/posts/PejNckwQj3A2MGhMA/systematic-runaway-optimiser-like-llm-failure-modes-on). *Roland Pihlakas, Sruthi Susan Kuriakose, Shruti Datta Gupta*
*   [Syco-bench: A Benchmark for LLM Sycophancy](https://www.syco-bench.com/). *Tim Duffy*
*   [Expressing stigma and inappropriate responses prevents LLMs from safely replacing mental health providers](https://arxiv.org/abs/2504.18412). *Jared Moore et al.*
*   [Lessons from a Chimp: AI "Scheming" and the Quest for Ape Language](https://arxiv.org/abs/2507.03409). *Christopher Summerfield et al.*
*   [Establishing Best Practices for Building Rigorous Agentic Benchmarks](https://arxiv.org/abs/2507.02825). *Yuxuan Zhu et al.*
*   [Towards Alignment Auditing as a Numbers-Go-Up Science](https://lesswrong.com/posts/bGYQgBPEyHidnZCdE/towards-alignment-auditing-as-a-numbers-go-up-science). *Sam Marks*
*   [Logical Consistency Between Disagreeing Experts and Its Role in AI Safety](https://arxiv.org/abs/2510.00821). *Andrés Corrada-Emmanuel*
*   [Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence](https://www.arxiv.org/abs/2510.01395). *Myra Cheng et al.*
*   [AI Testing Should Account for Sophisticated Strategic Behaviour](https://arxiv.org/abs/2508.14927). *Vojtech Kovarik et al.*
*   [Spiral-Bench](https://eqbench.com/spiral-bench.html). *Sam Paech*
*   [Discerning What Matters: A Multi-Dimensional Assessment of Moral Competence in LLMs](https://arxiv.org/abs/2506.13082). *Daniel Kilov et al.*
*   [Expanding on what we missed with sycophancy](https://openai.com/index/expanding-on-sycophancy/)
*   [Gödel's Therapy Room](https://gtr.dev/)
*   [Inspect Evals](https://inspect.aisi.org.uk/evals/)
*   [Inspect Cyber](https://www.aisi.gov.uk/blog/inspect-cyber)
*   [CyberSOCEval](https://arxiv.org/abs/2509.20166). *Lauren Deason et al.*
*   [CyberSecEval 4](https://meta-llama.github.io/PurpleLlama/CyberSecEval/)

+++

* * *

Orgs without public outputs this year
=====================================

We are not aware of public technical AI safety output with these agendas and organizations, though they are active otherwise.

*   [Safe Superintelligence Inc.](https://ssi.inc/) (SSI)
*   Conjecture: Cognitive Software
*   [Orthogonal / QACI](https://orxl.org/)
*   [modelingcooperation.com](https://www.modelingcooperation.com/research)
*   [Pr(Ai)2R](https://prair.group)
*   [Astera Obelisk](https://astera.org/program/obelisk/)
*   [Coordinal Research](https://coordinal.org/) (Thibodeau)
*   [Workshop Labs](https://workshoplabs.ai/) (Drago, Laine)

Graveyard (known to be inactive)
--------------------------------

*   [Adversarially Robust Augmentation and Distillation](https://www.lesswrong.com/posts/RRvdRyWrSqKW2ANL9/alignment-proposal-adversarially-robust-augmentation-and)
*   Half of FAIR including[ JEPA](https://www.ft.com/content/c586eb77-a16e-4363-ab0b-e877898b70de)
*   [Science of Evals](https://www.apolloresearch.ai/blog/we-need-a-science-of-evals/) (but[ see](https://arxiv.org/pdf/2503.05336))

Changes this time
=================

*   A few major changes to the taxonomy: the top-level split is now “black-box” vs “white-box” instead of “control” vs “understanding”. (We did try out an automated clustering but it wasn’t very good.)
*   The agendas are in general less charisma-based and more about solution type.
*   We did a systematic Arxiv scrape on the word “alignment” (and filtered out the[ sequence indexing](https://en.wikipedia.org/wiki/Sequence_alignment) papers that fell into this pipeline). “[Steerability](https://arxiv.org/pdf/2510.06084)” is one competing term used by academics.
*   We scraped >3000 links (arXiv, LessWrong, several alignment publication lists, blogs and conferences), conservatively filtering and pre-categorizing them with a LLM pipeline. All curated later, many more added manually.
*   This review has ~800 links compared to ~300 in 2024 and ~200 in 2023. We looked harder and the field has grown.
*   We don’t collate public funding figures.
*   New sections: “Labs”, “Multi-agent First”, “Better data”, “Model specs”, “character training” and “representation geometry”. ”Evals” is so massive it gets a top-level section.

Methods
=======

Structure
---------

We have again settled for a tree data structure for this post – but people and work can appear in multiple nodes so it’s not a dumb partition. Richer representation structures may be in the works.

The level of analysis for each node in the tree is the “research agenda”, an abstraction spanning multiple papers and organisations in a messy many-to-many relation. What makes something an agenda? Similar methods, similar aims, or something sociological about leaders and collaborators. Agendas vary greatly in their degree of coherent agency, from the very coherent Anthropic Circuits work to the enormous, leaderless and unselfconscious “iterative alignment”.)

Scope
-----

30th November 2024 – 30th November 2025 (with a few exceptions).

We’re focussing on “technical AGI safety”. We thus ignore a lot of work relevant to the overall risk: misuse, policy, strategy,[ OSINT](https://sentinel-team.org/),[ resilience](http://airesilience.net/) and[ indirect risk](https://www.forethought.org/research/project-ideas-for-making-transformative-ai-go-well-other-than-by-working-on-alignment),[ AI](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5353214)[ rights](https://arxiv.org/abs/2510.26396), general capabilities evals, and things closer to “[technical policy](https://docs.google.com/document/d/1BGsbwELOQRKVOO8Ho8S4no1BQeYdjbRZpBmRyk7kOVo/edit?usp=sharing)” and like[ products](https://themultiplicity.ai/) (like standards, legislation, SL4 datacentres, and automated cybersecurity). We also mostly focus on papers and blogposts (rather than say, underground gdoc samizdat or Discords).

We only use public information, so we are off by some additional unknown factor.

We try to include things which are early-stage and illegible – but in general we fail and mostly capture legible work on[ legible problems](https://www.lesswrong.com/posts/PMc65HgRFvBimEpmJ/legible-vs-illegible-ai-safety-problems) (i.e. things you can write a paper on already).

Of the 2000+ links to papers, organizations and posts in the raw scrape, about 700 made it in.

Paper sources
-------------

*   All arXiv papers with “AI alignment”, “AI safety”, or “steerability” in the abstract or title; all papers of ~120 AI safety researchers
*   All Alignment Forum posts and all LW posts under “[AI](https://www.lesswrong.com/w/ai)”
*   [Gasteiger’s links](https://aisafetyfrontier.substack.com/),[ Paleka’s links](https://newsletter.danielpaleka.com/),[ Lenz’s links](https://aisafetypapers.com/),[ Zvi’s links](https://thezvi.substack.com/)
*   [Ad hoc Twitter](https://x.com/g_leech_/following) for a year, several conference pages and workshops
*   AI scrapes miss lots of things. We did a proper pass with a software scraper of over 3000 links collected from the above and LLM crawl of some of the pages, and then an LLM pass to pre-filter the links for relevance and pre-assign the links to agendas and areas, but this also had systematic omissions. We ended up doing a full manual pass over a conservatively LLM-pre-filtered links and re-classifying the links and papers. The code and data can be found [here](https://github.com/arb-consulting/shallow-review-2025), including the 3300 collected [candidate links](https://github.com/arb-consulting/shallow-review-2025/blob/main/main-pipeline/data/data-dump-classify.csv). We are not aware of any proper studies of “LLM laziness” but it’s[ known](https://joshuaberkowitz.us/blog/papers-7/llmigrate-turns-lazy-llms-into-reliable-c-to-rust-translators-846) amongst power users of copilots.
*   For finding critiques we used LW backlinks, Google Scholar cited-by, manual search, collected links, and[ Ahrefs](https://ahrefs.com/backlink-checker/). Technical critiques are somewhat rare, though, and even then our coverage here is likely severely lacking. We generally do not include social network critiques (mostly due to scope).
*   Despite this effort we will not have included all relevant papers and names. The omission of a paper or a researcher is not strong negative evidence about their relevance.

Processing
----------

*   Collecting links throughout the year and at project start. Skimming papers, staring at long lists.
*   We drafted a taxonomy of research agendas. Based on last year’s[ list](https://www.lesswrong.com/posts/fAW6RXLKTLHC3WXkS/shallow-review-of-technical-ai-safety-2024), our expertise and the initial paper collection, though we changed the structure to accommodate shifts in the domain: the top-level split is now “black-box” vs “white-box” instead of “control” vs “understanding”.
*   At around 300 links collected manually (and growing fast), we decided to implement simple pipelines for crawling, scraping and LLM metadata extraction, pre-filtering and pre-classification into agendas, as well as other tasks – including final formatting later. The use of LLMs was limited to one simple task at a time, and the results were closely watched and reviewed. Code and data [here](https://github.com/arb-consulting/shallow-review-2025).
*   We tried getting the AI to update our taxonomy bottom-up to fit the body of papers, but the results weren’t very good. Though we are looking at some advanced options (specialized embedding or feature extraction and clustering or t-SNE etc.)
*   Work on the ~70 agendas was distributed among the team. We ended up making many local changes to the taxonomy, esp. splitting up and merging agendas. The taxonomy is specific to this year, and will need to be adapted in coming years.
*   We moved any agendas without public outputs this year to the bottom, and the inactive ones to the Graveyard. For most of them, we checked with people from the agendas for outputs or work we may have missed.
*   What started as a brief summary editorial grew into [its own thing](https://www.lesswrong.com/posts/Q9ewXs8pQSAX5vL7H/ai-in-2025-gestalt) (6000w).
*   We asked 10 friends in AI safety to review the ~80 page draft. After editing and formatting, we asked 50 technical AI safety researchers for a quick review focused on their expertise.
*   The field is growing at around 20% a year. There will come a time that this list isn't sensible to do manually even with the help of LLMs (at this granularity anyway). We may come up with better alternatives than lists and posts by then, though.

### Other classifications

We added our best guess about which of[ Davidad’s alignment problems](https://www.lesswrong.com/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve) the agenda would make an impact on if it succeeded, as well as its research approach and implied optimism in[ Richard Ngo’s 3x3](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research).

*   [Which deep orthodox subproblems](https://www.lesswrong.com/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve) could it ideally solve? (via Davidad)
*   [The *target case*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research): what part of the distribution over alignment difficulty do they aim to help with? (via Ngo)
    *   “optimistic-case”: if CoT is faithful, pretraining as value loading, no stable mesa-optimizers, the relevant scary capabilities are harder than alignment, zero-shot deception is hard, goals are myopic, etc
    *   pessimistic-case: if we’re in-between the above and the below
    *   worst-case: if power-seeking is rife, zero-shot deceptive alignment, steganography, gradient hacking, weird machines, weird coordination,[ deep deceptiveness](https://www.lesswrong.com/posts/XWwvwytieLtEWaFJX/deep-deceptiveness)
*   [The *broad approach:*](https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research) roughly what kind of work is it doing, primarily? (via Ngo)
    *   engineering: iterating over outputs
    *   behavioural: understanding the input-output relationship
    *   cognitive: understanding the algorithms
    *   maths/philosophy: providing concepts for the other approaches

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/wScohuNkKBrHgy5os/crcq39zt6yc2dgzigest)

Acknowledgments
===============

*These people generously helped with the review by providing expert feedback, literature sources, advice, or otherwise. Any remaining mistakes remain ours.*

Thanks to Neel Nanda, Owain Evans, Stephen Casper, Alex Turner, Caspar Oesterheld, Steve Byrnes, Adam Shai, Séb Krier, Vanessa Kosoy, Nora Ammann, David Lindner, John Wentworth, Vika Krakovna, Filip Sondej, JS Denain, Jan Kulveit, Mary Phuong, Linda Linsefors, Yuxi Liu, Ben Todd, Ege Erdil, Tan Zhi-Xuan, Jess Riedel, Mateusz Bagiński, Roland Pihlakas, Walter Laurito, Vojta Kovařík, David Hyland, plex, Shoshannah Tekofsky, Fin Moorhouse, Misha Yagudin, Nandi Schoots, Nuno Sempere, and others  for helpful comments.

Thanks to [QURI](https://quantifieduncertainty.org/) and Ozzie Gooen for creating a [website](https://shallowreview.ai/) for this review.

* * *

Appendix: Other reviews and taxonomies
======================================

*   [aisafety.com org “cards”](https://www.aisafety.com/map#cards)
*   [nonprofits.zone](https://nonprofits.zone)
*   [Leong and Linsefors](https://docs.google.com/document/d/1Mis0ZxuS-YIgwy4clC7hKrKEcm6Pn0yn709YUNVcpx8/edit?tab=t.0)
*   [Coefficient Giving RFP](https://www.lesswrong.com/posts/26SHhxK2yYQbh7ors/research-directions-open-phil-wants-to-fund-in-technical-ai)
*   [Peregrine Report](https://riskmitigation.ai/)
*   [The Singapore Consensus on Global AI Safety Research Priorities](https://arxiv.org/abs/2506.20702)
*   [International AI Safety Report 2025](https://arxiv.org/abs/2501.17805), along with their[ first](https://arxiv.org/abs/2510.13653) and[ second](https://arxiv.org/abs/2511.19863) key updates
*   [A Comprehensive Survey in LLM(-Agent) Full Stack Safety: Data, Training and Deployment](https://arxiv.org/pdf/2504.15585)
*   plex’s[ Review of AI safety funders](https://www.lesswrong.com/posts/KZPNbHs9RsoeZShkJ/plex-s-shortform?commentId=hCbJkBd9s23PEeLAL)
*   [The Alignment Project](https://www.lesswrong.com/s/wvLzDiWQWBC9b5HGa)
*   [AI Awareness literature review](https://arxiv.org/abs/2504.20084)
*   [aisafety.com/self-study](https://www.aisafety.com/self-study)
*   [Zach Stein-Perlman’s list ](https://docs.google.com/spreadsheets/d/10_dzImDvHq7eEag6paK6AmIdAGMBOA7yXUvumODhZ5U/edit?gid=1813700452#gid=1813700452)
*   [IAPS](https://github.com/Oscar-Delaney/safe_AI_papers)
*   [AI Safety Camp 10 Outputs](https://www.lesswrong.com/posts/3sjtEXzbwDpyALR4H/ai-safety-camp-10-outputs)
*   [The Road to Artificial SuperIntelligence](https://arxiv.org/abs/2412.16468)
*   [AE Studio field guide](https://www.ae.studio/essays/whos-actually-preventing-the-paperclip-apocalypse-a-field-guide-to-ai-alignment-organizations)
*   [AI Alignment: A Contemporary Survey](https://dl.acm.org/doi/pdf/10.1145/3770749)

* * *

Epigram
=======

> *No punting — we can’t keep building nanny products. Our products are overrun with filters and punts of various kinds. We need capable products and \[to\] trust our users.*

– Sergey Brin

\> *Over the decade I've spent working on AI safety, I've felt an overall trend of divergence; research partnerships starting out with a sense of a common project, then slowly drifting apart over time… eventually, two researchers are going to have some deep disagreement in matters of taste, which sends them down different paths.*

\> *Until the spring of this year, that is… something seemed to shift, subtly at first. After I gave a talk -- roughly the same talk I had been giving for the past year -- I had an excited discussion about it with Scott Garrabrant. Looking back, it wasn't so different from previous chats we had had, but the impact was different; it felt more concrete, more actionable, something that really touched my research rather than remaining hypothetical. In the subsequent weeks, discussions with my usual circle of colleagues took on a different character -- somehow it seemed that, after all our diverse explorations, we had arrived at a shared space.*

– Abram Demski

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/wScohuNkKBrHgy5os/v53v5x3zj1plfcq6oggj)

Brought to you by the [*Arb Corporation*](https://arbresearch.com/)