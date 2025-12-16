/**
 * Sun Diagram component - D3 sunburst visualization
 */

import { useEffect, useRef, useState } from 'react';
import * as d3 from 'd3';
import type { ChartNode, SizeMode } from '../types';

interface SunDiagramProps {
  data: ChartNode;
  mode: SizeMode;
  onNodeClick?: (node: ChartNode) => void;
  onNodeHover?: (node: ChartNode | null) => void;
}

export function SunDiagram({ data, mode, onNodeClick, onNodeHover }: SunDiagramProps) {
  const svgRef = useRef<SVGSVGElement>(null);
  const [dimensions, setDimensions] = useState({ width: 800, height: 800 });

  // Update dimensions on window resize
  useEffect(() => {
    const updateDimensions = () => {
      const container = svgRef.current?.parentElement;
      if (container) {
        const size = Math.min(container.clientWidth, container.clientHeight, 1200);
        setDimensions({ width: size, height: size });
      }
    };

    updateDimensions();
    window.addEventListener('resize', updateDimensions);
    return () => window.removeEventListener('resize', updateDimensions);
  }, []);

  // Create D3 visualization
  useEffect(() => {
    if (!svgRef.current || !data) return;

    const { width, height } = dimensions;
    const radius = Math.min(width, height) / 2;

    // Clear previous content
    d3.select(svgRef.current).selectAll('*').remove();

    const svg = d3
      .select(svgRef.current)
      .attr('width', width)
      .attr('height', height)
      .attr('viewBox', `${-width / 2} ${-height / 2} ${width} ${height}`)
      .style('font-family', 'Inter, system-ui, sans-serif')
      .style('font-size', '12px');

    // Create hierarchy
    // Sort by ID to maintain stable ordering across different size modes
    const root = d3.hierarchy(data)
      .sum(d => {
        // Only sum leaf nodes (nodes without children)
        // Parent nodes will automatically get the sum of their children
        return d.children ? 0 : d.value;
      })
      .sort((a, b) => {
        // Stable sort by ID instead of value
        return a.data.id.localeCompare(b.data.id);
      });

    // Create partition layout
    const partition = d3.partition<ChartNode>()
      .size([2 * Math.PI, radius]);

    partition(root);

    // Color scale based on top-level sections
    const colorScale = d3.scaleOrdinal(d3.schemeTableau10);

    // Function to get color for a node
    const getColor = (d: d3.HierarchyRectangularNode<ChartNode>): string => {
      if (d.depth === 0) return '#ffffff'; // Root is white

      // Find the top-level ancestor
      let ancestor = d;
      while (ancestor.depth > 1) {
        ancestor = ancestor.parent!;
      }

      return colorScale(ancestor.data.id);
    };

    // Create arc generator
    const arc = d3.arc<d3.HierarchyRectangularNode<ChartNode>>()
      .startAngle(d => d.x0)
      .endAngle(d => d.x1)
      .padAngle(0.001) // Minimal padding for visual separation
      .innerRadius(d => d.y0)
      .outerRadius(d => d.y1 - 1);

    // Create tooltip
    const tooltip = d3.select('body')
      .selectAll('.sun-diagram-tooltip')
      .data([null])
      .join('div')
      .attr('class', 'sun-diagram-tooltip')
      .style('position', 'absolute')
      .style('visibility', 'hidden')
      .style('background-color', 'rgba(0, 0, 0, 0.8)')
      .style('color', 'white')
      .style('padding', '8px 12px')
      .style('border-radius', '4px')
      .style('font-size', '14px')
      .style('pointer-events', 'none')
      .style('z-index', '1000')
      .style('max-width', '300px');

    // Draw the arcs
    svg
      .append('g')
      .selectAll('path')
      .data(root.descendants().filter(d => d.depth > 0))
      .join('path')
      .attr('d', d => arc(d as d3.HierarchyRectangularNode<ChartNode>))
      .attr('fill', d => getColor(d as d3.HierarchyRectangularNode<ChartNode>))
      .attr('stroke', '#fff')
      .attr('stroke-width', 1)
      .style('cursor', 'pointer')
      .style('opacity', 0.9)
      .on('mouseenter', function(_event, d) {
        // Highlight
        d3.select(this)
          .style('opacity', 1)
          .attr('stroke-width', 2);

        // Show tooltip
        const node = d.data;
        let tooltipText = node.name;

        // Add one-sentence summary if available
        if (node.item.agenda_attributes?.one_sentence_summary) {
          tooltipText += `\n\n${node.item.agenda_attributes.one_sentence_summary}`;
        }

        tooltip
          .style('visibility', 'visible')
          .text(tooltipText);

        onNodeHover?.(node);
      })
      .on('mousemove', function(event) {
        tooltip
          .style('top', `${event.pageY + 10}px`)
          .style('left', `${event.pageX + 10}px`);
      })
      .on('mouseleave', function() {
        // Remove highlight
        d3.select(this)
          .style('opacity', 0.9)
          .attr('stroke-width', 1);

        // Hide tooltip
        tooltip.style('visibility', 'hidden');

        onNodeHover?.(null);
      })
      .on('click', (_event, d) => {
        onNodeClick?.(d.data);
      });

    // Add labels for larger segments
    svg
      .append('g')
      .attr('pointer-events', 'none')
      .attr('text-anchor', 'middle')
      .selectAll('text')
      .data(root.descendants().filter(d => {
        // Only show labels for segments that are large enough
        const rect = d as d3.HierarchyRectangularNode<ChartNode>;
        const angle = rect.x1 - rect.x0;
        const depth = rect.depth;
        return depth > 0 && angle > 0.1 && rect.y1 - rect.y0 > 20;
      }))
      .join('text')
      .attr('transform', d => {
        const rect = d as d3.HierarchyRectangularNode<ChartNode>;
        const x = ((rect.x0 + rect.x1) / 2) * 180 / Math.PI;
        const y = (rect.y0 + rect.y1) / 2;
        return `rotate(${x - 90}) translate(${y},0) rotate(${x < 180 ? 0 : 180})`;
      })
      .attr('dy', '0.35em')
      .attr('fill', 'white')
      .style('font-size', d => {
        const rect = d as d3.HierarchyRectangularNode<ChartNode>;
        const size = Math.min(12, (rect.y1 - rect.y0) / 4);
        return `${size}px`;
      })
      .style('font-weight', d => d.depth === 1 ? 'bold' : 'normal')
      .text(d => {
        // Truncate long names
        const rect = d as d3.HierarchyRectangularNode<ChartNode>;
        const maxLength = Math.floor((rect.x1 - rect.x0) * 10);
        return d.data.name.length > maxLength
          ? d.data.name.slice(0, maxLength) + '...'
          : d.data.name;
      });

  }, [data, dimensions, mode, onNodeClick]);

  return (
    <div className="w-full h-full flex items-center justify-center">
      <svg ref={svgRef} />
    </div>
  );
}
