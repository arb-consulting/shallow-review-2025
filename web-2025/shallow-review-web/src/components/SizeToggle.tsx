/**
 * Size toggle component - switch between papers, FTEs, and uniform sizing
 */

import type { SizeMode } from '../types';

interface SizeToggleProps {
  mode: SizeMode;
  onChange: (mode: SizeMode) => void;
}

const sizeOptions: Array<{ mode: SizeMode; label: string; icon: string }> = [
  { mode: 'papers', label: 'Papers', icon: '📄' },
  { mode: 'ftes', label: 'FTEs', icon: '👥' },
  { mode: 'uniform', label: 'Uniform', icon: '⚖️' },
];

export function SizeToggle({ mode, onChange }: SizeToggleProps) {
  return (
    <div className="flex items-center gap-2 bg-white dark:bg-gray-800 rounded-lg shadow-lg p-2">
      <span className="text-sm font-medium text-gray-700 dark:text-gray-300 px-2">
        Size:
      </span>
      <div className="flex gap-1">
        {sizeOptions.map(option => (
          <button
            key={option.mode}
            onClick={() => onChange(option.mode)}
            className={`
              px-3 py-1.5 rounded-md text-sm font-medium transition-all
              flex items-center gap-1.5
              ${
                mode === option.mode
                  ? 'bg-accent text-white shadow-sm'
                  : 'bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'
              }
            `}
            title={`Size by ${option.label.toLowerCase()}`}
          >
            <span>{option.icon}</span>
            <span>{option.label}</span>
          </button>
        ))}
      </div>
    </div>
  );
}
