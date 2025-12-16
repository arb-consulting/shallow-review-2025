/**
 * Home page - main visualization with sun diagram
 */

import { useState, useEffect } from 'react';
import { SunDiagram, SizeToggle, ThemeToggle, AgendaModal } from '../components';
import { transformToChartData, buildItemsById } from '../utils';
import type { ChartNode, SizeMode, ProcessedDocument, DocumentItem, ItemsById } from '../types';

// Import data
import documentData from '../data/draft-md-20251208-to-parse-parsed.json';

export function Home() {
  const [mode, setMode] = useState<SizeMode>('papers');
  const [chartData, setChartData] = useState<ChartNode | null>(null);
  const [itemsById, setItemsById] = useState<ItemsById>({});
  const [selectedAgenda, setSelectedAgenda] = useState<DocumentItem | null>(null);

  // Load and transform data
  useEffect(() => {
    const data = documentData as ProcessedDocument;
    const hierarchy = transformToChartData(data, mode);
    const lookup = buildItemsById(data.items);

    setChartData(hierarchy.root);
    setItemsById(lookup);
  }, [mode]);

  const handleNodeClick = (node: ChartNode) => {
    // Only open modal for agendas
    if (node.item.item_type === 'agenda') {
      setSelectedAgenda(node.item);
      window.location.hash = node.id;
    }
  };

  const handleCloseModal = () => {
    setSelectedAgenda(null);
    // Clear hash without triggering page reload
    if (window.location.hash) {
      history.pushState('', document.title, window.location.pathname + window.location.search);
    }
  };

  // Handle hash changes (for direct links)
  useEffect(() => {
    const handleHashChange = () => {
      const hash = window.location.hash.slice(1);
      if (hash && chartData) {
        // Try to find the agenda by ID
        const item = itemsById[hash];
        if (item && item.item_type === 'agenda') {
          setSelectedAgenda(item);
        }
      } else {
        setSelectedAgenda(null);
      }
    };

    handleHashChange(); // Check on mount
    window.addEventListener('hashchange', handleHashChange);
    return () => window.removeEventListener('hashchange', handleHashChange);
  }, [chartData, itemsById]);

  return (
    <div className="relative w-full h-screen bg-light-bg dark:bg-dark-bg text-light-text dark:text-dark-text overflow-hidden">
      {/* Header */}
      <header className="absolute top-0 left-0 right-0 z-10 p-4">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold font-serif">
              Shallow Review of Technical AI Safety 2025
            </h1>
            <p className="text-sm text-gray-600 dark:text-gray-400 mt-1">
              Interactive visualization of AI safety research agendas
            </p>
          </div>
          <div className="flex items-center gap-3">
            <SizeToggle mode={mode} onChange={setMode} />
            <ThemeToggle />
          </div>
        </div>
      </header>

      {/* Main visualization */}
      <div className="w-full h-full pt-24 pb-8">
        {chartData ? (
          <SunDiagram
            data={chartData}
            mode={mode}
            onNodeClick={handleNodeClick}
          />
        ) : (
          <div className="w-full h-full flex items-center justify-center">
            <div className="text-center">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-accent mx-auto mb-4" />
              <p className="text-lg">Loading visualization...</p>
            </div>
          </div>
        )}
      </div>

      {/* Footer with links */}
      <footer className="absolute bottom-0 left-0 right-0 z-10 p-4">
        <div className="max-w-7xl mx-auto flex items-center justify-center gap-6 text-sm text-gray-600 dark:text-gray-400">
          <a
            href="/approaches"
            className="hover:text-accent transition-colors underline"
          >
            Approaches & Cases
          </a>
          <span>·</span>
          <a
            href="/problems"
            className="hover:text-accent transition-colors underline"
          >
            Orthodox Problems
          </a>
        </div>
      </footer>

      {/* Agenda Modal */}
      <AgendaModal
        agenda={selectedAgenda}
        itemsById={itemsById}
        onClose={handleCloseModal}
      />
    </div>
  );
}
