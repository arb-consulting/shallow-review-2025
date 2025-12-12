import type { DocumentItem, ProcessedDocument } from '../types';
import sourceData from '../data/source.json';

export interface ChartNode {
  name: string;
  value: number;
  children?: ChartNode[];
  id: string;
  item?: DocumentItem;
  depth?: number;
  isExtension?: boolean;
  // properties for echarts styling
  itemStyle?: {
    color?: string;
    borderRadius?: number;
    borderWidth?: number;
  };
  label?: {
    show?: boolean;
    position?: string;
    fontSize?: number;
    rotate?: string | number;
    color?: string;
    align?: string;
    padding?: number | number[];
  };
}

const SHORT_NAMES: Record<string, string> = {
  "White-box safety (understand and control current model internals)": "White-box Safety",
  "Black-box safety (understand and control current model behavior)": "Black-box Safety",
  "The Learning-Theoretic Agenda": "Learning-Theoretic",
  "Situational awareness and self-awareness evals": "Situational Awareness",
  "WMD evals (Weapons of Mass Destruction)": "WMD Evals",
  "Capability removal, unlearning": "Unlearning",
  "Safeguards (inference-time auxiliaries)": "Safeguards",
  "Assistance games, assistive agents": "Assistance Games",
  "Character training and persona steering": "Character Training",
  "Model values / default preferences": "Model Values",
  "Other surprising phenomena": "Surprising Phenomena",
  "The \"Neglected Approaches\" Approach": "Neglected Approaches",
  "Labs (giant companies)": "Labs",
  "Synthesis (building a complete alignment solution)": "Synthesis",
  "Theory (understanding the fundamentals of intelligence and alignment)": "Theory",
  "Evals (measuring the danger)": "Evals",
  "Governance (coordinating to prevent bad outcomes)": "Governance",
  "Tools for aligning multiple AIs": "Aligning Multiple AIs",
  "Aligning to the social contract": "Social Contract",
  "Synthetic data for alignment": "Synthetic Data",
  "Data quality for alignment": "Data Quality",
  "Chain of thought monitoring": "CoT Monitoring",
  "Concept-based interpretability": "Concept-based",
  "Lie and deception detectors": "Lie Detectors",
  "Developmental Interpretability": "Dev Interp",
  "Representation structure and geometry": "Rep Structure",
  "Human inductive biases": "Inductive Biases",
  "Activation engineering": "Activation Eng.",
  "Ontology Identification": "Ontology ID",
  "The Learning-Theoretic Alignment Agenda": "Learning-Theoretic",
  "Agent foundations": "Agent Foundations",
  "High-Actuation Spaces": "High-Actuation",
  "Asymptotic guarantees": "Asymptotic",
  "Heuristic Explanations": "Heuristic Exp.",
  "Deepmind Responsibility & Safety": "DeepMind Safety",
  "Anthropic Safety": "Anthropic",
  "OpenAI Safety": "OpenAI",
};

export function getProcessedData(): ProcessedDocument {
  return sourceData as unknown as ProcessedDocument;
}

function shortenName(name: string): string {
  if (SHORT_NAMES[name]) return SHORT_NAMES[name];
  // Simple heuristic: if contains parenthesis, take part before
  if (name.includes('(')) {
    return name.split('(')[0].trim();
  }
  return name;
}

export function buildChartHierarchy(): ChartNode[] {
  const data = getProcessedData();
  const items = data.items;
  
  const itemMap = new Map<string, ChartNode>();
  const rootNodes: ChartNode[] = [];

  // First pass: create all nodes
  items.forEach(item => {
    itemMap.set(item.id, {
      name: shortenName(item.name),
      value: 1,
      id: item.id,
      item: item,
      children: []
    });
  });

  // Second pass: build hierarchy
  items.forEach(item => {
    const node = itemMap.get(item.id);
    if (!node) return;

    if (item.parent_id && itemMap.has(item.parent_id)) {
      const parent = itemMap.get(item.parent_id);
      parent?.children?.push(node);
    } else {
      rootNodes.push(node);
    }
  });

  // Calculate values
  function calculateValues(node: ChartNode): number {
    if (!node.children || node.children.length === 0) {
      node.value = 1;
      return 1;
    }
    let sum = 0;
    node.children.forEach(child => {
      sum += calculateValues(child);
    });
    node.value = sum;
    return sum;
  }
  rootNodes.forEach(calculateValues);

  // Normalize Hierarchy: Push Agendas to Outer Ring (Level 2)
  // Target Depth is 2 (0=Root, 1=Sub, 2=Agenda)
  const TARGET_DEPTH = 2;

  function processNode(node: ChartNode, currentDepth: number): ChartNode {
    // Process children first? No, we need to restructure children.
    
    if (!node.children || node.children.length === 0) {
      return node;
    }

    const newChildren: ChartNode[] = [];
    const shortBranchChildren: ChartNode[] = [];
    const normalChildren: ChartNode[] = [];

    node.children.forEach(child => {
      // Check if child is a leaf/agenda and needs padding
      // If child has no children (Agenda), and currentDepth + 1 < TARGET_DEPTH
      // We categorize it as "short branch"
      if ((!child.children || child.children.length === 0) && (currentDepth + 1 < TARGET_DEPTH)) {
        shortBranchChildren.push(child);
      } else {
        normalChildren.push(child);
      }
    });

    // If we have short branch children, wrap them in an extension node
    if (shortBranchChildren.length > 0) {
      const extensionNode: ChartNode = {
        ...node,
        id: node.id + '_ext_' + currentDepth, // Unique ID
        name: "", // Hide label for extension node to avoid repetition
        children: shortBranchChildren,
        isExtension: true,
        // We might want to clear the label for the inner extension to avoid duplication visual?
        // But for "Stretching", we want it to look like the parent.
        // ECharts sunburst handles same-named parent-child well if colors match.
        item: node.item, // Keep same metadata
        value: 0 // Will recalc
      };
      
      // Recurse on the extension node to see if it needs further padding
      const processedExtension = processNode(extensionNode, currentDepth + 1);
      newChildren.push(processedExtension);
    }

    // Process normal children
    normalChildren.forEach(child => {
      newChildren.push(processNode(child, currentDepth + 1));
    });

    node.children = newChildren;
    
    // Recalculate value after restructuring
    node.value = node.children.reduce((acc, c) => acc + c.value, 0);
    
    return node;
  }

  // Apply normalization to roots
  const normalizedRoots = rootNodes.map(root => processNode(root, 0));

  // Wrap in one extra (dummy) root node
  const dummyRoot: ChartNode = {
    name: "AI Safety",
    value: normalizedRoots.reduce((acc, n) => acc + n.value, 0),
    children: normalizedRoots,
    id: "root_dummy",
    // item is optional, so we leave it undefined
  };

  return [dummyRoot];
}

export function getItemById(id: string): DocumentItem | undefined {
  const data = getProcessedData();
  return data.items.find(item => item.id === id);
}
