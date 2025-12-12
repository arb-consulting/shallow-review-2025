import React from 'react';
import ReactMarkdown from 'react-markdown';
import type { AgendaAttributes, Paper, OutputSectionHeader } from '../types';
import { ORTHODOX_PROBLEMS } from '../constants';
import { getItemById } from '../utils/dataProcessing';

interface ContentRendererProps {
  attributes: AgendaAttributes;
}

const ICONS: Record<string, string> = {
  theory_of_change: '≈',
  broad_approach: '⚙',
  target_case: '◐',
  orthodox_problems: '⚠',
  see_also: '↔',
  some_names: '☉',
  critiques: '✗',
  funded_by: '*$',
  estimated_ftes: '*⫼',
  outputs: '▹',
  default: '○'
};

const Attribute = ({ label, icon, children }: { label: string, icon: string, children: React.ReactNode }) => (
  <div className="attribute-block">
    <div className="icon-col">{icon}</div>
    <div className="content-col">
      <span className="meta-label">{label}</span>
      <span className="meta-value">{children}</span>
    </div>
  </div>
);

export const ContentRenderer: React.FC<ContentRendererProps> = ({ attributes }) => {
  
  const resolveSeeAlso = (id: string) => {
    const item = getItemById(id);
    return item ? item.name : id;
  };

  return (
    <div className="content-renderer">
      {attributes.one_sentence_summary && (
        <div className="content-section summary">
          <ReactMarkdown>{`*${attributes.one_sentence_summary}*`}</ReactMarkdown>
        </div>
      )}

      {attributes.theory_of_change && (
        <div className="content-section">
          <Attribute label="Theory of Change:" icon={ICONS.theory_of_change}>
             <ReactMarkdown components={{ p: 'span' }}>{attributes.theory_of_change}</ReactMarkdown>
          </Attribute>
        </div>
      )}

      <div className="content-section">
        {attributes.broad_approach_text && (
          <Attribute label="General Approach:" icon={ICONS.broad_approach}>
            <ReactMarkdown components={{ p: 'span' }}>{attributes.broad_approach_text}</ReactMarkdown>
          </Attribute>
        )}
        
        {attributes.target_case_text && (
          <Attribute label="Target Case:" icon={ICONS.target_case}>
            <ReactMarkdown components={{ p: 'span' }}>{attributes.target_case_text}</ReactMarkdown>
          </Attribute>
        )}
      </div>

      {attributes.orthodox_problems.length > 0 && (
        <div className="content-section">
          <Attribute label="Orthodox Problems:" icon={ICONS.orthodox_problems}>
            {attributes.orthodox_problems.map((probId, idx) => {
              const prob = ORTHODOX_PROBLEMS[probId];
              return prob ? (
                 <span key={probId}>
                   {idx > 0 && ', '}
                   <a href={prob.url} target="_blank" rel="noopener noreferrer">{prob.name}</a>
                 </span>
              ) : null;
            })}
          </Attribute>
        </div>
      )}

      {/* Other Attributes */}
      {Object.entries(attributes.other_attributes).length > 0 && (
        <div className="content-section">
           {Object.entries(attributes.other_attributes).map(([key, value]) => (
             <Attribute key={key} label={`${key}:`} icon={ICONS.default}>
               {String(value)}
             </Attribute>
           ))}
        </div>
      )}

      {attributes.see_also.length > 0 && (
        <div className="content-section">
          <Attribute label="See Also:" icon={ICONS.see_also}>
            {attributes.see_also.map((refId, idx) => (
              <span key={refId}>
                {idx > 0 && ' · '}
                <a href={`#${refId}`}>{resolveSeeAlso(refId)}</a>
              </span>
            ))}
          </Attribute>
        </div>
      )}

      {attributes.some_names.length > 0 && (
        <div className="content-section">
          <Attribute label="Key People:" icon={ICONS.some_names}>
            {attributes.some_names.join(', ')}
          </Attribute>
        </div>
      )}

      {attributes.critiques && (
        <div className="content-section">
          <Attribute label="Critiques:" icon={ICONS.critiques}>
            <ReactMarkdown components={{ p: 'span' }}>{attributes.critiques}</ReactMarkdown>
          </Attribute>
        </div>
      )}

      <div className="content-section">
        {attributes.funded_by && (
          <Attribute label="Funded By:" icon={ICONS.funded_by}>
            <ReactMarkdown components={{ p: 'span' }}>{attributes.funded_by}</ReactMarkdown>
          </Attribute>
        )}
        
        {attributes.estimated_ftes && (
          <Attribute label="Estimated FTEs:" icon={ICONS.estimated_ftes}>
            {attributes.estimated_ftes}
          </Attribute>
        )}
      </div>

      {attributes.outputs.length > 0 && (
        <div className="content-section outputs">
          <Attribute label="Outputs:" icon={ICONS.outputs}>
            <ul className="paper-list" style={{ marginTop: '0.2rem' }}>
              {attributes.outputs.map((output, idx) => {
                if ('section_name' in output) {
                  return <h4 key={idx} style={{marginTop: '1em', fontWeight: 'bold'}}>{(output as OutputSectionHeader).section_name}</h4>;
                }
                
                const paper = output as Paper;
                return (
                  <li key={idx}>
                    {paper.link_url ? (
                      <>
                          <a href={paper.link_url} target="_blank" rel="noopener noreferrer">
                          {paper.link_text || paper.title || paper.link_url}
                          </a>
                          {paper.authors && paper.authors.length > 0 && (
                              <span className="paper-authors"> {paper.authors.join(', ')}</span>
                          )}
                      </>
                    ) : (
                      <ReactMarkdown>{paper.original_md}</ReactMarkdown>
                    )}
                  </li>
                );
              })}
            </ul>
          </Attribute>
        </div>
      )}
    </div>
  );
};
