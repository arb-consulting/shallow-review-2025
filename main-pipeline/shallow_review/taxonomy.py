"""
Classification taxonomy management.

Loads and validates the category taxonomy from data/taxonomy.yaml.
Provides utilities for working with categories and generating prompt text.
"""

from pathlib import Path

import yaml
from pydantic import BaseModel, Field, field_validator


class Category(BaseModel):
    """A category in the classification taxonomy.
    
    Categories form a tree structure. Leaf categories (those with no children)
    are the ones that can be assigned to classified items.
    """
    
    model_config = {"populate_by_name": True}
    
    id: str = Field(description="Machine-readable category ID")
    name: str = Field(description="Human-readable category name")
    description: str = Field(description="Detailed description of what belongs in this category")
    children: list["Category"] = Field(default_factory=list, description="Subcategories")
    examples: list[str] = Field(default_factory=list, description="Example items from 2024")
    is_leaf_explicit: bool | None = Field(default=None, validation_alias="is_leaf", description="Explicitly set leaf status")
    sr2024: dict[str, str] | None = Field(default=None, description="Context from Shallow Review 2024")
    
    @property
    def is_leaf(self) -> bool:
        """Check if this is a leaf category (assignable).
        
        Uses explicit is_leaf if provided in YAML, otherwise infers from children.
        """
        if self.is_leaf_explicit is not None:
            return self.is_leaf_explicit
        return len(self.children) == 0
    
    @field_validator("id")
    @classmethod
    def validate_id(cls, v: str) -> str:
        """Ensure ID is snake_case."""
        if not v:
            raise ValueError("Category ID cannot be empty")
        if not v.replace("_", "").replace("-", "").isalnum():
            raise ValueError(f"Category ID must be alphanumeric with underscores/hyphens: {v}")
        return v
    
    def model_post_init(self, __context) -> None:
        """Validate that only leaf categories can have examples."""
        if self.examples and self.children:
            raise ValueError(
                f"Category '{self.id}' has both examples and children. "
                "Only leaf categories (without children) can have examples."
            )
    
    def get_all_leaf_ids(self) -> list[str]:
        """Recursively collect all leaf category IDs."""
        if self.is_leaf:
            return [self.id]
        leaves = []
        for child in self.children:
            leaves.extend(child.get_all_leaf_ids())
        return leaves
    
    def get_category_by_id(self, category_id: str) -> "Category | None":
        """Find a category by ID anywhere in the tree."""
        if self.id == category_id:
            return self
        for child in self.children:
            found = child.get_category_by_id(category_id)
            if found:
                return found
        return None
    
    def get_path_to_category(self, category_id: str, current_path: list[str] | None = None) -> list[str] | None:
        """Get the path from root to a category as a list of names."""
        if current_path is None:
            current_path = []
        
        if self.id == category_id:
            return current_path + [self.name]
        
        for child in self.children:
            path = child.get_path_to_category(category_id, current_path + [self.name])
            if path:
                return path
        
        return None


class Taxonomy(BaseModel):
    """The complete classification taxonomy."""
    
    taxonomy: list[Category] = Field(description="Top-level categories")
    
    def get_all_leaf_ids(self) -> list[str]:
        """Get all leaf (assignable) category IDs."""
        leaves = []
        for cat in self.taxonomy:
            leaves.extend(cat.get_all_leaf_ids())
        return leaves
    
    def get_category_by_id(self, category_id: str) -> Category | None:
        """Find a category by ID."""
        for cat in self.taxonomy:
            found = cat.get_category_by_id(category_id)
            if found:
                return found
        return None
    
    def get_path_to_category(self, category_id: str) -> list[str] | None:
        """Get the full path to a category as a list of names."""
        for cat in self.taxonomy:
            path = cat.get_path_to_category(category_id)
            if path:
                return path
        return None
    
    def validate_category_id(self, category_id: str) -> bool:
        """Check if a category ID is valid and is a leaf."""
        cat = self.get_category_by_id(category_id)
        return cat is not None and cat.is_leaf


def load_taxonomy(path: Path | str | None = None) -> Taxonomy:
    """Load and validate taxonomy from YAML file.
    
    Args:
        path: Path to taxonomy YAML file. Defaults to data/taxonomy.yaml
        
    Returns:
        Validated Taxonomy object
        
    Raises:
        FileNotFoundError: If taxonomy file doesn't exist
        ValueError: If taxonomy is invalid
    """
    if path is None:
        path = Path(__file__).parent.parent / "data" / "taxonomy.yaml"
    else:
        path = Path(path)
    
    if not path.exists():
        raise FileNotFoundError(f"Taxonomy file not found: {path}")
    
    with open(path) as f:
        data = yaml.safe_load(f)
    
    taxonomy = Taxonomy(**data)
    
    # Validate that there are leaf categories
    leaves = taxonomy.get_all_leaf_ids()
    if not leaves:
        raise ValueError("Taxonomy must have at least one leaf category")
    
    # Validate that all IDs are unique
    all_ids: list[str] = []
    def collect_ids(cat: Category) -> None:
        all_ids.append(cat.id)
        for child in cat.children:
            collect_ids(child)
    
    for cat in taxonomy.taxonomy:
        collect_ids(cat)
    
    if len(all_ids) != len(set(all_ids)):
        duplicates = [id_ for id_ in all_ids if all_ids.count(id_) > 1]
        raise ValueError(f"Duplicate category IDs found: {set(duplicates)}")
    
    return taxonomy


def format_taxonomy_for_prompt(taxonomy: Taxonomy, *, include_examples: bool = False) -> str:
    """Format taxonomy as markdown for LLM prompts.
    
    Uses hierarchical structure where:
    - Non-leaf categories are headers with descriptions
    - Leaf categories are listed underneath with ID and description
    
    Args:
        taxonomy: The taxonomy to format
        include_examples: Whether to include example items in leaf descriptions
        
    Returns:
        Markdown-formatted string
    """
    lines = []
    
    lines.append("## Classification Categories")
    lines.append("")
    lines.append("You must assign the content to ONE leaf category (those with `category_id`).")
    lines.append("")
    
    def format_category(cat: Category, level: int = 1) -> None:
        """Recursively format categories."""
        if cat.is_leaf:
            # Leaf category: show as list item with ID
            lines.append(f"- **{cat.name}** (`{cat.id}`)")
            lines.append(f"  {cat.description}")
            if include_examples and cat.examples:
                lines.append(f"  *Examples:* {'; '.join(cat.examples)}")
            lines.append("")
        else:
            # Non-leaf category: show as header
            header_prefix = "#" * (level + 2)  # Start at h3
            lines.append(f"{header_prefix} {cat.name}")
            lines.append("")
            lines.append(cat.description)
            lines.append("")
            
            # Recurse to children
            for child in cat.children:
                format_category(child, level + 1)
    
    for cat in taxonomy.taxonomy:
        format_category(cat, level=1)
    
    return "\n".join(lines)


def get_category_count_by_level(taxonomy: Taxonomy) -> dict[int, int]:
    """Count categories at each tree level (for stats/debugging)."""
    counts: dict[int, int] = {}
    
    def count_level(cat: Category, level: int) -> None:
        counts[level] = counts.get(level, 0) + 1
        for child in cat.children:
            count_level(child, level + 1)
    
    for cat in taxonomy.taxonomy:
        count_level(cat, 0)
    
    return counts

