/**
 * Outputs list component - displays papers and section headers
 */

import type { OutputItem } from '../types';
import { isPaper, isOutputSectionHeader } from '../types';
import { formatAuthors, formatYear } from '../utils';

interface OutputsListProps {
  outputs: OutputItem[];
}

export function OutputsList({ outputs }: OutputsListProps) {
  if (outputs.length === 0) return null;

  return (
    <div className="space-y-3">
      {outputs.map((output, index) => {
        if (isPaper(output)) {
          const title = output.link_text || output.title || output.original_md;
          const hasUrl = !!output.link_url;
          const authors = formatAuthors(output.authors);
          const year = formatYear(output.published_year);

          return (
            <div key={index} className="flex items-start gap-2">
              <span className="text-gray-400 mt-1">•</span>
              <div className="flex-1">
                {hasUrl ? (
                  <a
                    href={output.link_url!}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-accent hover:underline font-medium"
                  >
                    {title}
                  </a>
                ) : (
                  <span className="font-medium">{title}</span>
                )}
                {(authors || year) && (
                  <div className="text-sm text-gray-600 dark:text-gray-400 mt-0.5">
                    {authors}
                    {authors && year && ' '}
                    {year}
                  </div>
                )}
              </div>
            </div>
          );
        }

        if (isOutputSectionHeader(output)) {
          return (
            <div key={index} className="mt-4 first:mt-0">
              <h4 className="text-sm font-semibold italic text-gray-700 dark:text-gray-300">
                {output.section_name}
              </h4>
            </div>
          );
        }

        return null;
      })}
    </div>
  );
}
