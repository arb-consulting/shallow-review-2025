import React, { useEffect, useRef } from 'react';
import * as echarts from 'echarts';
import { useTheme } from '../contexts/ThemeContext';
import { buildChartHierarchy, type ChartNode } from '../utils/dataProcessing';
import { applyPaletteToData } from '../utils/colorUtils';

interface SunburstChartProps {
  onNodeClick: (node: ChartNode) => void;
}

export const SunburstChart: React.FC<SunburstChartProps> = ({ onNodeClick }) => {
  const chartRef = useRef<HTMLDivElement>(null);
  const chartInstance = useRef<echarts.EChartsType | null>(null);
  const { theme } = useTheme();

  useEffect(() => {
    if (!chartRef.current) return;

    // Initialize chart
    if (!chartInstance.current) {
      chartInstance.current = echarts.init(chartRef.current);
      
      // Handle resize
      window.addEventListener('resize', () => {
        chartInstance.current?.resize();
      });

      // Handle click
      chartInstance.current.on('click', (params: any) => {
        // Don't trigger for extension nodes (which should be invisible anyway)
        if (params.data && params.data.item && !params.data.isExtension) {
          onNodeClick(params.data as ChartNode);
        }
      });
    }

    // Prepare data
    const rawData = buildChartHierarchy();
    const data = applyPaletteToData(rawData);

    // Chart Options
    const option: echarts.EChartsOption = {
      backgroundColor: 'transparent',
      tooltip: {
        show: true,
        formatter: (params: any) => {
          const data = params.data as ChartNode;
          if (data.isExtension) return ''; // Hide tooltip for extension nodes
          // Show tooltip for all nodes to ensure full names are visible if truncated
          return `<div class="echarts-tooltip"><strong>${data.name}</strong></div>`;
        },
        backgroundColor: theme === 'dark' ? 'rgba(50,50,50,0.9)' : 'rgba(255,255,255,0.9)',
        borderColor: theme === 'dark' ? '#555' : '#ccc',
        textStyle: {
          color: theme === 'dark' ? '#fff' : '#333'
        }
      },
      series: [
        {
          type: 'sunburst',
          data: data,
          radius: [0, '95%'],
          sort: undefined,
          label: {
            // Default label config
            show: true,
            color: '#fff',
            textBorderColor: 'rgba(0,0,0,0.5)',
            textBorderWidth: 2,
            formatter: (params: any) => params.name
          },
          itemStyle: {
            borderRadius: 2,
            borderWidth: 1,
            borderColor: theme === 'dark' ? '#121212' : '#FDFDFD'
          },
          emphasis: {
            focus: 'ancestor'
          },
          levels: [
            // Level -1: Center
            {
                radius: ['0%', '10%'],
                itemStyle: { borderWidth: 2 },
                label: { 
                  // rotate: 0, 
                  fontWeight: 'bold', 
                  fontSize: 14,
                  minAngle: 10
                }
            },
            // Level 0: Roots
            {
              radius: ['10%', '30%'],
              itemStyle: { borderWidth: 2 },
              label: { 
                // rotate: 0, 
                fontWeight: 'bold', 
                fontSize: 14,
                minAngle: 10
              }
            },
            // Level 1: Middle Ring (Sections/Extensions)
            {
              radius: ['30%', '45%'],
              itemStyle: { borderWidth: 1 },
              label: { 
                // rotate: 'radial', 
                minAngle: 5,
                fontSize: 11
              }
            },
            // Level 2: Outer Ring (Agendas)
            {
              radius: ['45%', '95%'],
              itemStyle: { borderWidth: 1 },
              label: { 
                // rotate: 'tangential',
                padding: 3, 
                color: '#fff', 
                textBorderWidth: 2,
                minAngle: 2,
                fontSize: 11,
                align: 'center',
                position: 'inside' 
              }
            }
          ]
        }
      ]
    };

    chartInstance.current.setOption(option);

  }, [theme, onNodeClick]);

  return <div ref={chartRef} style={{ width: '100%', height: '100%' }} />;
};
