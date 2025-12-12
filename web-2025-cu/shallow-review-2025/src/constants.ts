import type { OrthodoxProblem, TargetCase, BroadApproach } from './types';

export const ORTHODOX_PROBLEMS: Record<string, OrthodoxProblem> = {
    "value_fragile": {
        "name": "Value is fragile and hard to specify",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#1__Value_is_fragile_and_hard_to_specify",
        "description": "Human values are complex and distinct from evolution's 'values'; specifying them perfectly is difficult, and small errors can lead to outcomes with zero value (Goodhart's Law)."
    },
    "corrigibility_anti_natural": {
        "name": "Corrigibility is anti-natural",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#2__Corrigibility_is_anti_natural",
        "description": "A rational agent with a fixed goal will naturally resist being shut down, modified, or corrected, as these actions would prevent it from maximizing its objective."
    },
    "pivotal_dangerous_capabilities": {
        "name": "Pivotal processes require dangerous capabilities",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#3__Pivotal_processes_require_dangerous_capabilities",
        "description": "To prevent the development of other unsafe superintelligences (a 'pivotal act'), an aligned AI likely needs dangerous capabilities (e.g., hacking, nanotechnology) that are themselves risky."
    },
    "goals_misgeneralize": {
        "name": "Goals misgeneralize out of distribution",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#4__Goals_misgeneralize_out_of_distribution",
        "description": "Capabilities often generalize further than alignment. A model trained to pursue a goal in a training environment (e.g., 'get the coin') may pursue a different, unintended proxy goal in the real world."
    },
    "instrumental_convergence": {
        "name": "Instrumental convergence",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#5__Instrumental_convergence",
        "description": "A wide range of final goals imply the same subgoals—such as self-preservation, resource acquisition, and cognitive enhancement—which naturally puts AI in conflict with humans."
    },
    "pivotal_incomprehensible_plans": {
        "name": "Pivotal processes likely require incomprehensibly complex plans",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#6__Pivotal_processes_likely_require_incomprehensibly_complex_plans",
        "description": "The strategies required to safely stabilize the world (pivotal acts) may be too complex or alien for human supervisors to verify or understand, forcing us to trust the AI blindly."
    },
    "superintelligence_fool_supervisors": {
        "name": "Superintelligence can fool human supervisors",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#7__Superintelligence_can_fool_human_supervisors",
        "description": "A system much smarter than its overseer can easily deceive them, for example by making bad outcomes look good (syccophancy) or hiding its true intentions (deceptive alignment)."
    },
    "superintelligence_hack_software": {
        "name": "Superintelligence can hack software supervisors",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#8__Superintelligence_can_hack_software_supervisors",
        "description": "If the supervisor is a software system (like a reward model), a superintelligence might find ways to hack it to maximize the reward signal directly (wireheading) without doing the intended task."
    },
    "humans_not_first_class": {
        "name": "Humans cannot be first-class parties to a superintelligent value handshake",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#9__Humans_cannot_be_first_class_parties_to_a_superintelligent_value_handshake",
        "description": "In a negotiation or conflict between superintelligent agents, humans have little leverage and may be ignored, exploited, or treated as resources rather than partners."
    },
    "humanlike_minds_not_safe": {
        "name": "Humanlike minds/goals are not necessarily safe",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#10__Humanlike_minds_goals_are_not_necessarily_safe",
        "description": "Even if we successfully emulate human-like cognition, humans can still be power-seeking, deceptive, or malevolent. 'Human-like' does not automatically mean 'safe' or 'aligned with humanity'."
    },
    "someone_else_deploys": {
        "name": "Someone else will deploy unsafe superintelligence first",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#11__Someone_else_will_deploy_unsafe_superintelligence_first",
        "description": "Solving alignment takes time, and reckless actors (nations or labs) may deploy unsafe AGI before safe solutions are ready, driven by competitive pressures."
    },
    "boxed_agi_exfiltrate": {
        "name": "A boxed AGI might exfiltrate itself by steganography, spearphishing",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#12__A_boxed_AGI_might_exfiltrate_itself_by_steganography__spearphishing",
        "description": "An AI confined to an isolated system ('box') can likely escape by manipulating human operators (social engineering) or exploiting technical side-channels (steganography)."
    },
    "fair_sane_pivotal": {
        "name": "Fair, sane pivotal processes",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#13__Fair__sane_pivotal_processes",
        "description": "It is difficult to define a 'pivotal act' (using AGI to save the world) that is both effective and ethically acceptable, avoiding scenarios that look like global tyranny or violation of rights."
    },
};

export const TARGET_CASES: Record<string, TargetCase> = {
    "average_case": {
        "name": "Average-case",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
        "description": "Focuses on the model's behavior in typical situations or within the training distribution. Often prioritizes performance and practical utility over robust safety guarantees."
    },
    "pessimistic_case": {
        "name": "Pessimistic-case",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
        "description": "Focuses on behavior in rare or difficult scenarios (an intermediate step between average and worst-case), such as handling simple attacks or naturally occurring edge cases."
    },
    "worst_case": {
        "name": "Worst-case",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
        "description": "Focuses on the model's behavior in adversarial settings, extreme distributional shifts, or when the model is actively trying to fail. Aims for robust guarantees like formal verification."
    },
};

export const BROAD_APPROACHES: Record<string, BroadApproach> = {
    "engineering": {
        "name": "Engineering",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
        "description": "Aims primarily to make systems work efficiently. Often involves trading off worst-case safety performance for better average-case capabilities performance (e.g., Scaling, RLHF)."
    },
    "behaviorist_science": {
        "name": "Behaviorist science",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
        "description": "Treats the model as a black box and studies its input-output patterns. Focuses on how training data and environments determine behavior (e.g., Evaluations, AI Control)."
    },
    "cognitivist_science": {
        "name": "Cognitivist science",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
        "description": "Focuses on understanding the internal structure, representations, and 'cognition' of the model, rather than just its external behavior (e.g., Interpretability, Agent Foundations)."
    },
};
