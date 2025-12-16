/**
 * Orthodox Problems index page
 */

import { Link } from 'react-router-dom';
import { ThemeToggle } from '../components';
import {
  ORTHODOX_PROBLEMS,
  PROBLEM_DESCRIPTIONS,
  SYMBOLS,
} from '../utils/constants';
import { getAgendasByOrthodoxProblem } from '../utils';
import type { ProcessedDocument } from '../types';

// Import data
import documentData from '../data/draft-md-20251208-to-parse-parsed.json';

export function ProblemsIndex() {
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
        <h1 className="text-4xl font-bold font-serif mb-4">
          Orthodox AI Safety Problems
        </h1>
        <p className="text-gray-600 dark:text-gray-400 mb-8">
          From{' '}
          <a
            href="https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve"
            target="_blank"
            rel="noopener noreferrer"
            className="text-accent hover:underline"
          >
            "A list of core AI safety problems"
          </a>
        </p>

        {/* Problems */}
        <section>
          {Object.entries(ORTHODOX_PROBLEMS).map(([id, problem], index) => {
            const agendas = getAgendasByOrthodoxProblem(data, id);

            return (
              <div key={id} id={id} className="mb-10">
                <h2 className="text-2xl font-bold mb-3 flex items-center gap-2">
                  <span className="text-gray-400">#{index + 1}</span>
                  <span>{SYMBOLS.orthodox_problem}</span>
                  <a
                    href={problem.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="hover:text-accent transition-colors"
                  >
                    {problem.name}
                  </a>
                </h2>

                <p className="text-gray-700 dark:text-gray-300 mb-4 italic">
                  {PROBLEM_DESCRIPTIONS[id]}
                </p>

                {agendas.length > 0 ? (
                  <div className="ml-6">
                    <p className="font-medium mb-2">
                      Agendas addressing this problem ({agendas.length}):
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
                          {agenda.agenda_attributes?.one_sentence_summary && (
                            <span className="text-sm text-gray-600 dark:text-gray-400 ml-2">
                              — {agenda.agenda_attributes.one_sentence_summary}
                            </span>
                          )}
                        </li>
                      ))}
                    </ul>
                  </div>
                ) : (
                  <p className="text-gray-500 dark:text-gray-400 ml-6 text-sm">
                    No agendas explicitly addressing this problem
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
