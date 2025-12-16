/**
 * Agenda content component - formatted display of all agenda attributes
 */

import ReactMarkdown from 'react-markdown';
import type { DocumentItem, ItemsById } from '../types';
import { SYMBOLS, ORTHODOX_PROBLEMS, BROAD_APPROACHES, TARGET_CASES } from '../utils/constants';
import { AttributeChip } from './AttributeChip';
import { SeeAlsoLinks } from './SeeAlsoLinks';
import { OutputsList } from './OutputsList';

interface AgendaContentProps {
  agenda: DocumentItem;
  itemsById: ItemsById;
}

export function AgendaContent({ agenda, itemsById }: AgendaContentProps) {
  const attrs = agenda.agenda_attributes;

  if (!attrs) {
    return (
      <div className="p-6">
        <p className="text-gray-500 dark:text-gray-400">No agenda data available.</p>
      </div>
    );
  }

  return (
    <div className="p-6 space-y-4">
      {/* One sentence summary */}
      {attrs.one_sentence_summary && (
        <p className="text-lg italic text-gray-700 dark:text-gray-300">
          {attrs.one_sentence_summary}
        </p>
      )}

      {/* Theory of change */}
      {attrs.theory_of_change && (
        <div className="space-y-1">
          <div className="flex items-start gap-2">
            <span className="text-gray-500 dark:text-gray-400">{SYMBOLS.theory_of_change}</span>
            <div className="flex-1">
              <span className="font-medium">Theory of change:</span>{' '}
              <span className="inline">
                <ReactMarkdown
                  components={{
                    p: ({ children }) => <span>{children}</span>,
                    a: ({ href, children }) => (
                      <a
                        href={href}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-accent hover:underline"
                      >
                        {children}
                      </a>
                    ),
                  }}
                >
                  {attrs.theory_of_change}
                </ReactMarkdown>
              </span>
            </div>
          </div>
        </div>
      )}

      {/* Approach and Case chips */}
      {(attrs.broad_approach_id || attrs.target_case_id) && (
        <div className="flex flex-wrap items-center gap-2">
          {attrs.broad_approach_id && BROAD_APPROACHES[attrs.broad_approach_id] && (
            <AttributeChip
              type="approach"
              label={attrs.broad_approach_text || BROAD_APPROACHES[attrs.broad_approach_id].name}
              href={`/approaches#${attrs.broad_approach_id}`}
              symbol={SYMBOLS.approach}
            />
          )}
          {attrs.target_case_id && TARGET_CASES[attrs.target_case_id] && (
            <AttributeChip
              type="case"
              label={attrs.target_case_text || TARGET_CASES[attrs.target_case_id].name}
              href={`/approaches#${attrs.target_case_id}`}
              symbol={SYMBOLS.case}
            />
          )}
        </div>
      )}

      {/* Orthodox problems chips */}
      {attrs.orthodox_problems.length > 0 && (
        <div className="flex flex-wrap items-center gap-2">
          {attrs.orthodox_problems.map(problemId => {
            const problem = ORTHODOX_PROBLEMS[problemId];
            if (!problem) return null;

            return (
              <AttributeChip
                key={problemId}
                type="problem"
                label={problem.name}
                href={`/problems#${problemId}`}
                symbol={SYMBOLS.orthodox_problem}
              />
            );
          })}
        </div>
      )}

      {/* See also */}
      {attrs.see_also.length > 0 && (
        <div className="flex items-start gap-2">
          <span className="text-gray-500 dark:text-gray-400">{SYMBOLS.see_also}</span>
          <div className="flex-1">
            <span className="font-medium">See also:</span>{' '}
            <SeeAlsoLinks refs={attrs.see_also} itemsById={itemsById} />
          </div>
        </div>
      )}

      {/* Some names */}
      {attrs.some_names.length > 0 && (
        <div className="flex items-start gap-2">
          <span className="text-gray-500 dark:text-gray-400">{SYMBOLS.names}</span>
          <div className="flex-1">
            <span className="font-medium">Some names:</span>{' '}
            <span>{attrs.some_names.join(', ')}</span>
          </div>
        </div>
      )}

      {/* Critiques */}
      {attrs.critiques && (
        <div className="flex items-start gap-2">
          <span className="text-gray-500 dark:text-gray-400">{SYMBOLS.critiques}</span>
          <div className="flex-1">
            <span className="font-medium">Critiques:</span>{' '}
            <span className="inline">
              <ReactMarkdown
                components={{
                  p: ({ children }) => <span>{children}</span>,
                  a: ({ href, children }) => (
                    <a
                      href={href}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-accent hover:underline"
                    >
                      {children}
                    </a>
                  ),
                }}
              >
                {attrs.critiques}
              </ReactMarkdown>
            </span>
          </div>
        </div>
      )}

      {/* Funding and FTEs */}
      {(attrs.funded_by || attrs.estimated_ftes) && (
        <div className="flex flex-wrap items-center gap-4 text-sm">
          {attrs.funded_by && (
            <div className="flex items-center gap-2">
              <span className="text-gray-500 dark:text-gray-400">{SYMBOLS.funded_by}</span>
              <span className="font-medium">Funded by:</span>
              <span>{attrs.funded_by}</span>
            </div>
          )}
          {attrs.estimated_ftes && (
            <div className="flex items-center gap-2">
              <span className="text-gray-500 dark:text-gray-400">{SYMBOLS.ftes}</span>
              <span className="font-medium">Estimated FTEs:</span>
              <span>{attrs.estimated_ftes}</span>
            </div>
          )}
        </div>
      )}

      {/* Outputs */}
      {attrs.outputs.length > 0 && (
        <div className="border-t border-gray-200 dark:border-gray-700 pt-4">
          <div className="flex items-center gap-2 mb-3">
            <span className="text-gray-500 dark:text-gray-400">{SYMBOLS.outputs}</span>
            <h3 className="font-bold text-lg">Some outputs</h3>
          </div>
          <OutputsList outputs={attrs.outputs} />
        </div>
      )}
    </div>
  );
}
