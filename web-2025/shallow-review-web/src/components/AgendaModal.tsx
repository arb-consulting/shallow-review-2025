/**
 * Agenda modal component - side panel for displaying agenda details
 */

import { useEffect } from 'react';
import type { DocumentItem, ItemsById } from '../types';
import { AgendaContent } from './AgendaContent';

interface AgendaModalProps {
  agenda: DocumentItem | null;
  itemsById: ItemsById;
  onClose: () => void;
}

export function AgendaModal({ agenda, itemsById, onClose }: AgendaModalProps) {
  const isOpen = !!agenda;

  // Handle ESC key
  useEffect(() => {
    const handleEsc = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && isOpen) {
        onClose();
      }
    };

    window.addEventListener('keydown', handleEsc);
    return () => window.removeEventListener('keydown', handleEsc);
  }, [isOpen, onClose]);

  // Prevent body scroll when modal is open
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }

    return () => {
      document.body.style.overflow = '';
    };
  }, [isOpen]);

  if (!isOpen || !agenda) return null;

  // Get breadcrumb path
  const breadcrumb: string[] = [];
  let current: DocumentItem | undefined = agenda;
  while (current && current.parent_id) {
    const parentItem: DocumentItem | undefined = itemsById[current.parent_id];
    if (parentItem) {
      breadcrumb.unshift(parentItem.name);
      current = parentItem;
    } else {
      break;
    }
  }

  return (
    <>
      {/* Backdrop */}
      <div
        className="fixed inset-0 bg-black/30 backdrop-blur-sm z-40 transition-opacity"
        onClick={onClose}
        aria-hidden="true"
      />

      {/* Modal panel */}
      <div
        className="fixed inset-y-0 right-0 z-50 w-full sm:w-2/3 md:w-1/2 lg:w-2/5
                   bg-white dark:bg-gray-900 shadow-2xl
                   transform transition-transform duration-300 ease-in-out
                   flex flex-col"
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-title"
      >
        {/* Header */}
        <div className="flex-shrink-0 border-b border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800">
          <div className="flex items-start justify-between p-6 pb-4">
            <div className="flex-1 min-w-0 pr-4">
              {/* Breadcrumb */}
              {breadcrumb.length > 0 && (
                <nav className="text-sm text-gray-500 dark:text-gray-400 mb-2">
                  {breadcrumb.map((item, index) => (
                    <span key={index}>
                      {index > 0 && <span className="mx-2">›</span>}
                      <span>{item}</span>
                    </span>
                  ))}
                </nav>
              )}

              {/* Title */}
              <h2
                id="modal-title"
                className="text-2xl font-bold font-serif text-gray-900 dark:text-gray-100"
              >
                {agenda.name}
              </h2>
            </div>

            {/* Close button */}
            <button
              onClick={onClose}
              className="flex-shrink-0 p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
              aria-label="Close modal"
            >
              <svg
                className="w-6 h-6 text-gray-500 dark:text-gray-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
          </div>
        </div>

        {/* Content - scrollable */}
        <div className="flex-1 overflow-y-auto">
          <AgendaContent agenda={agenda} itemsById={itemsById} />
        </div>
      </div>
    </>
  );
}
