export interface OrthodoxProblem {
  name: string;
  url: string;
  description?: string;
}

export interface TargetCase {
  name: string;
  url: string;
  description?: string;
}

export interface BroadApproach {
  name: string;
  url: string;
  description?: string;
}

export type ItemType = 'section' | 'agenda';

export interface Paper {
  link_url?: string | null;
  link_text?: string | null;
  original_md: string;
  title?: string | null;
  authors: string[];
  author_organizations: string[];
  date?: string | null;
  published_year?: number | null;
  venue?: string | null;
  kind?: string | null;
}

export interface OutputSectionHeader {
  section_name: string;
  header_level: number;
  original_md: string;
}

export interface AgendaAttributes {
  who_edits?: string | null;
  one_sentence_summary?: string | null;
  theory_of_change?: string | null;
  see_also: string[];
  orthodox_problems: string[];
  target_case_id?: string | null;
  target_case_text?: string | null;
  broad_approach_id?: string | null;
  broad_approach_text?: string | null;
  some_names: string[];
  estimated_ftes?: string | null;
  critiques?: string | null;
  funded_by?: string | null;
  outputs: (Paper | OutputSectionHeader)[];
  other_attributes: Record<string, any>;
}

export interface DocumentItem {
  id: string;
  name: string;
  header_level: number;
  parent_id: string | null;
  content: string | null;
  item_type: ItemType;
  agenda_attributes?: AgendaAttributes | null;
  parsing_issues: string[];
}

export interface ProcessedDocument {
  source_file: string;
  items: DocumentItem[];
}

