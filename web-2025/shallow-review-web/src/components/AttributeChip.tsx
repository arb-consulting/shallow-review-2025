/**
 * Attribute chip component - clickable chips for approach, case, and orthodox problems
 */

interface AttributeChipProps {
  type: 'approach' | 'case' | 'problem';
  label: string;
  href: string;
  symbol?: string;
}

export function AttributeChip({ type, label, href, symbol }: AttributeChipProps) {
  const colorClasses = {
    approach: 'bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 hover:bg-blue-200 dark:hover:bg-blue-800',
    case: 'bg-purple-100 dark:bg-purple-900 text-purple-800 dark:text-purple-200 hover:bg-purple-200 dark:hover:bg-purple-800',
    problem: 'bg-orange-100 dark:bg-orange-900 text-orange-800 dark:text-orange-200 hover:bg-orange-200 dark:hover:bg-orange-800',
  };

  return (
    <a
      href={href}
      className={`
        inline-flex items-center gap-1 px-2.5 py-1 rounded-md text-sm font-medium
        transition-colors border border-transparent
        ${colorClasses[type]}
      `}
    >
      {symbol && <span>{symbol}</span>}
      <span>{label}</span>
    </a>
  );
}
