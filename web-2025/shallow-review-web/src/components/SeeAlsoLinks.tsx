/**
 * See Also links component - cross-references to other agendas and sections
 */

import type { ItemsById } from '../types';
import { formatSeeAlsoLinks } from '../utils';

interface SeeAlsoLinksProps {
  refs: string[];
  itemsById: ItemsById;
}

export function SeeAlsoLinks({ refs, itemsById }: SeeAlsoLinksProps) {
  if (refs.length === 0) return null;

  const links = formatSeeAlsoLinks(refs, itemsById);

  return (
    <div className="flex flex-wrap items-center gap-2">
      {links.map((link, index) => (
        <span key={link.id} className="inline-flex items-center">
          {index > 0 && <span className="text-gray-400 mx-1">·</span>}
          <a
            href={`/#${link.id}`}
            className={`
              text-accent hover:underline font-medium
              ${!link.exists && 'text-gray-400 dark:text-gray-600'}
            `}
            title={link.exists ? `Go to ${link.name}` : `Reference not found: ${link.id}`}
          >
            {link.name}
          </a>
        </span>
      ))}
    </div>
  );
}
