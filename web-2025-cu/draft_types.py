"""Types and constants for shallow review draft document parsing.

Defines Pydantic models for document structure and taxonomy constants
(orthodox problems, target cases, broad approaches).
"""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


# ============================================================================
# Constants: Orthodox Problems, Target Cases, Broad Approaches
# ============================================================================

# Orthodox Problems from "A list of core AI safety problems"
# Source: https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve
# All 13 problems listed in order:
ORTHODOX_PROBLEMS: dict[str, dict[str, str]] = {
    "value_fragile": {
        "name": "Value is fragile and hard to specify",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#1__Value_is_fragile_and_hard_to_specify",
    },
    "corrigibility_anti_natural": {
        "name": "Corrigibility is anti-natural",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#2__Corrigibility_is_anti_natural",
    },
    "pivotal_dangerous_capabilities": {
        "name": "Pivotal processes require dangerous capabilities",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#3__Pivotal_processes_require_dangerous_capabilities",
    },
    "goals_misgeneralize": {
        "name": "Goals misgeneralize out of distribution",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#4__Goals_misgeneralize_out_of_distribution",
    },
    "instrumental_convergence": {
        "name": "Instrumental convergence",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#5__Instrumental_convergence",
    },
    "pivotal_incomprehensible_plans": {
        "name": "Pivotal processes likely require incomprehensibly complex plans",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#6__Pivotal_processes_likely_require_incomprehensibly_complex_plans",
    },
    "superintelligence_fool_supervisors": {
        "name": "Superintelligence can fool human supervisors",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#7__Superintelligence_can_fool_human_supervisors",
    },
    "superintelligence_hack_software": {
        "name": "Superintelligence can hack software supervisors",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#8__Superintelligence_can_hack_software_supervisors",
    },
    "humans_not_first_class": {
        "name": "Humans cannot be first-class parties to a superintelligent value handshake",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#9__Humans_cannot_be_first_class_parties_to_a_superintelligent_value_handshake",
    },
    "humanlike_minds_not_safe": {
        "name": "Humanlike minds/goals are not necessarily safe",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#10__Humanlike_minds_goals_are_not_necessarily_safe",
    },
    "someone_else_deploys": {
        "name": "Someone else will deploy unsafe superintelligence first",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#11__Someone_else_will_deploy_unsafe_superintelligence_first",
    },
    "boxed_agi_exfiltrate": {
        "name": "A boxed AGI might exfiltrate itself by steganography, spearphishing",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#12__A_boxed_AGI_might_exfiltrate_itself_by_steganography__spearphishing",
    },
    "fair_sane_pivotal": {
        "name": "Fair, sane pivotal processes",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#13__Fair__sane_pivotal_processes",
    },
}

# Target Cases from "Defining alignment research"
# Source: https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research
TARGET_CASES: dict[str, dict[str, str]] = {
    "average_case": {
        "name": "Average-case",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
    },
    "pessimistic_case": {
        "name": "Pessimistic-case",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
    },
    "worst_case": {
        "name": "Worst-case",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
    },
}

# Broad Approaches from "Defining alignment research"
# Source: https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research
BROAD_APPROACHES: dict[str, dict[str, str]] = {
    "engineering": {
        "name": "Engineering",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
    },
    "behaviorist_science": {
        "name": "Behaviorist science",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
    },
    "cognitivist_science": {
        "name": "Cognitivist science",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
    },
}


# ============================================================================
# Pydantic Models
# ============================================================================


class ItemType(str, Enum):
    """Type of top-level document item.

    Note: Papers and output sections are nested within agenda outputs,
    not top-level document items.
    """

    SECTION = "section"
    AGENDA = "agenda"


class Paper(BaseModel):
    """A research output (paper, blog post, link, or non-link reference) in the outputs section.

    This model is used for all output items including papers, blog posts, plain URLs,
    and non-link text references. Fields from the database (classify.data JSON) are
    populated when available for items with URLs.
    """

    link_url: str | None = Field(default=None, description="URL if present (for papers, blogs, etc.)")
    link_text: str | None = Field(default=None, description="Display text or title extracted from markdown")
    original_md: str = Field(description="Original markdown text as read from source")

    # Database fields (from classify.data JSON) - populated later for items with URLs
    title: str | None = Field(default=None, description="Paper title")
    authors: list[str] = Field(default_factory=list, description="List of author names")
    author_organizations: list[str] = Field(
        default_factory=list, description="List of author organizations"
    )
    date: str | None = Field(
        default=None, description="Publication date in ISO format YYYY-MM-DD"
    )
    published_year: int | None = Field(default=None, description="Publication year as integer")
    venue: str | None = Field(default=None, description="Publication venue")
    kind: str | None = Field(
        default=None, description="Content type (e.g., 'paper_published', 'paper_preprint', 'blog_post')"
    )


class OutputSectionHeader(BaseModel):
    """A subsection header within an outputs section.

    Papers following this header (until next header) are conceptually grouped under it,
    but structurally papers and headers are siblings in a flat list.
    """

    section_name: str = Field(description="Section header name")
    header_level: int = Field(description="Markdown header level (typically 3, 4 or more)")
    original_md: str = Field(description="Original markdown text as read from source")


class AgendaAttributes(BaseModel):
    """Structured metadata extracted from a research agenda.

    Standard attributes have dedicated fields, non-standard ones go in other_attributes,
    and any free-form descriptive text goes in free_form_text.
    """

    # Core structured attributes (most common)
    who_edits: str | None = Field(default=None, description="Editor name (internal)")
    one_sentence_summary: str | None = None
    theory_of_change: str | None = None
    see_also: list[str] = Field(default_factory=list, description="Related agenda or section IDs")
    orthodox_problems: list[str] = Field(
        default_factory=list,
        description="List of orthodox problem IDs (keys from ORTHODOX_PROBLEMS)",
    )
    target_case_id: str | None = Field(
        default=None, description="Target case ID (key from TARGET_CASES)"
    )
    target_case_text: str | None = Field(
        default=None, description="Target case text"
    )
    broad_approach_id: str | None = Field(
        default=None, description="Broad approach ID (key from BROAD_APPROACHES)"
    )
    broad_approach_text: str | None = Field(
        default=None, description="Broad approach text"
    )
    some_names: list[str] = Field(default_factory=list, description="Key researchers")
    estimated_ftes: str | None = Field(default=None, description="FTE estimate or range")
    critiques: str | None = Field(
        default=None, description="Critiques as markdown text (links, descriptions, etc.)"
    )
    funded_by: str | None = Field(default=None, description="Funding sources")

    # Outputs - flat list of papers and section headers (preserving order)
    outputs: list[Paper | OutputSectionHeader] = Field(
        default_factory=list,
        description="Output sections and papers (flat list preserving order)",
    )

    # Catch-all for non-standard attributes
    other_attributes: dict[str, Any] = Field(
        default_factory=dict, description="Attributes not matching standard fields"
    )


class DocumentItem(BaseModel):
    """A single item in the flat document structure."""

    id: str = Field(description="Unique identifier (e.g., 'sec:big_labs', 'a:openai')")
    name: str = Field(description="Display name/title")
    header_level: int = Field(description="Markdown header level (1-6)")
    parent_id: str | None = Field(default=None, description="Parent item ID if nested")
    content: str | None = Field(default=None, description="Markdown content. Entire section/agenda text without header for PreparsedDocument. In ProcessedDocument, an additional markdown content after the header - this should be empty for most agendas.")
    item_type: ItemType = Field(description="Type of item")

    # Agenda-specific fields (only populated for agendas)
    agenda_attributes: AgendaAttributes | None = Field(
        default=None, description="Metadata for agendas (populated by LLM)"
    )

    # Parsing quality and error detection
    parsing_issues: list[str] = Field(
        default_factory=list,
        description="Log of issues detected during parsing (missing headers, format problems, extra/unexpected data, etc.)"
    )


class ProcessedDocument(BaseModel):
    """The fully processed draft document with flat structure, after LLM extraction."""

    source_file: str
    items: list[DocumentItem] = Field(
        default_factory=list, description="Flat list of items in document order (sections and agendas), after LLM extraction."
    )


class PreparsedDocument(BaseModel):
    """The preparsed draft document with flat structure, before LLM extraction."""

    source_file: str
    items: list[DocumentItem] = Field(
        default_factory=list, description="Flat list of items in document order (sections and agendas), before LLM extraction."
    )
