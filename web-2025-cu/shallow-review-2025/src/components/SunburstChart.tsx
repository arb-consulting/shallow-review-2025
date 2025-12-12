import React, { useEffect, useRef } from 'react';
import * as echarts from 'echarts';
import { useTheme } from '../contexts/ThemeContext';
import { buildChartHierarchy, type ChartNode, type WeightMode } from '../utils/dataProcessing';
import { applyPaletteToData } from '../utils/colorUtils';

interface SunburstChartProps {
  onNodeClick: (node: ChartNode) => void;
  weightMode: WeightMode;
}

export const SunburstChart: React.FC<SunburstChartProps> = ({ onNodeClick, weightMode }) => {
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
    const rawData = buildChartHierarchy(weightMode);
    const data = applyPaletteToData(rawData);

    // Chart Options
    const option: echarts.EChartsOption = {
      backgroundColor: 'transparent',
      tooltip: {
        show: true,
        formatter: (params: any) => {
          const data = params.data as ChartNode;
          if (data.isExtension) return ''; // Hide tooltip for extension nodes
          
          let valLabel = '';
          if (weightMode === 'fte' && data.item?.agenda_attributes?.estimated_ftes) {
             valLabel = `<br/>FTEs: ${data.item.agenda_attributes.estimated_ftes}`;
          } else if (weightMode === 'papers' && data.item?.agenda_attributes?.outputs) {
             valLabel = `<br/>Papers: ${data.item.agenda_attributes.outputs.length}`;
          }

          return `<div class="echarts-tooltip"><strong>${data.name}</strong>${valLabel}</div>`;
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
            // 'none' prevents fading others, but we want highlighting.
            focus: 'none'
          },
          levels: [
            // Level -1: Dummy
            {
                radius: ['0%', '0%'],
                itemStyle: { borderWidth: 2 },
                label: { 
                  // rotate: 0, 
                  fontWeight: 'bold', 
                  fontSize: 14,
                  minAngle: 10
                }
            },
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
              radius: ['10%', '70%'],
              itemStyle: { borderWidth: 2 },
              label: { 
                // rotate: 0, 
                fontWeight: 'bold', 
                fontSize: 15,
                minAngle: 10,
                align: 'left',
                padding: 15,
              }
            },
            // Level 1: Middle Ring (Sections/Extensions)
            {
              radius: ['45%', '70%'],
              itemStyle: { borderWidth: 1 },
              label: { 
                // rotate: 'radial', 
                align: 'left',
                minAngle: 5,
                fontSize: 13,
                padding: 10,
              }
            },
            // Level 2: Outer Ring (Agendas)
            {
              radius: ['70%', '73%'],
              itemStyle: { borderWidth: 1 },
              label: { 
                rotate: 'radial',
                padding: 5, 
                color: theme === 'light' ? '#000' : '#fff', // Black in light mode
                textBorderWidth: 0,
                minAngle: 2,
                fontSize: 15,
                // align: 'center',
                position: 'outside',
              }
            }
          ]
        }
      ]
    };

    chartInstance.current.setOption(option);

  }, [theme, onNodeClick, weightMode]);

  return <div ref={chartRef} style={{ width: '100%', height: '100%' }} />;
};
