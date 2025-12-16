/**
 * Approaches & Cases index page
 */

import { Link } from 'react-router-dom';
import { ThemeToggle } from '../components';
import {
  BROAD_APPROACHES,
  TARGET_CASES,
  APPROACH_DESCRIPTIONS,
  CASE_DESCRIPTIONS,
  SYMBOLS,
} from '../utils/constants';
import { getAgendasByAttribute } from '../utils';
import type { ProcessedDocument } from '../types';

// Import data
import documentData from '../data/draft-md-20251208-to-parse-parsed.json';

export function ApproachesIndex() {
  const data = documentData as ProcessedDocument;

  return (
    <div className="min-h-screen bg-light-bg dark:bg-dark-bg text-light-text dark:text-dark-text">
      {/* Header */}
      <header className="border-b border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800">
        <div className="max-w-4xl mx-auto px-6 py-4 flex items-center justify-between">
          <Link
            to="/"
            className="text-accent hover:underline text-sm font-medium"
          >
            ← Back to Diagram
          </Link>
          <ThemeToggle />
        </div>
      </header>

      {/* Main content */}
      <main className="max-w-4xl mx-auto px-6 py-12">
        <h1 className="text-4xl font-bold font-serif mb-6">
          Approaches & Cases
        </h1>

        {/* Approaches Section */}
        <section className="mb-16">
          <h2 className="text-3xl font-bold font-serif mb-8 flex items-center gap-2">
            <span>{SYMBOLS.approach}</span>
            <span>Approaches</span>
          </h2>

          {Object.entries(BROAD_APPROACHES).map(([id, approach]) => {
            const agendas = getAgendasByAttribute(data, 'broad_approach_id', id);

            return (
              <div key={id} id={id} className="mb-10">
                <h3 className="text-2xl font-bold mb-3">
                  <a
                    href={approach.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="hover:text-accent transition-colors"
                  >
                    {approach.name}
                  </a>
                </h3>

                <p className="text-gray-700 dark:text-gray-300 mb-4 italic">
                  {APPROACH_DESCRIPTIONS[id]}
                </p>

                {agendas.length > 0 ? (
                  <div className="ml-6">
                    <p className="font-medium mb-2">
                      Agendas ({agendas.length}):
                    </p>
                    <ul className="space-y-1">
                      {agendas.map(agenda => (
                        <li key={agenda.id}>
                          <a
                            href={`/#${agenda.id}`}
                            className="text-accent hover:underline"
                          >
                            {agenda.name}
                          </a>
                        </li>
                      ))}
                    </ul>
                  </div>
                ) : (
                  <p className="text-gray-500 dark:text-gray-400 ml-6 text-sm">
                    No agendas with this approach
                  </p>
                )}
              </div>
            );
          })}
        </section>

        {/* Cases Section */}
        <section className="mb-16">
          <h2 className="text-3xl font-bold font-serif mb-8 flex items-center gap-2">
            <span>{SYMBOLS.case}</span>
            <span>Target Cases</span>
          </h2>

          {Object.entries(TARGET_CASES).map(([id, targetCase]) => {
            const agendas = getAgendasByAttribute(data, 'target_case_id', id);

            return (
              <div key={id} id={id} className="mb-10">
                <h3 className="text-2xl font-bold mb-3">
                  <a
                    href={targetCase.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="hover:text-accent transition-colors"
                  >
                    {targetCase.name}
                  </a>
                </h3>

                <p className="text-gray-700 dark:text-gray-300 mb-4 italic">
                  {CASE_DESCRIPTIONS[id]}
                </p>

                {agendas.length > 0 ? (
                  <div className="ml-6">
                    <p className="font-medium mb-2">
                      Agendas ({agendas.length}):
                    </p>
                    <ul className="space-y-1">
                      {agendas.map(agenda => (
                        <li key={agenda.id}>
                          <a
                            href={`/#${agenda.id}`}
                            className="text-accent hover:underline"
                          >
                            {agenda.name}
                          </a>
                        </li>
                      ))}
                    </ul>
                  </div>
                ) : (
                  <p className="text-gray-500 dark:text-gray-400 ml-6 text-sm">
                    No agendas with this case
                  </p>
                )}
              </div>
            );
          })}
        </section>
      </main>
    </div>
  );
}
