import React, { useEffect, useRef } from 'react';
import classNames from 'classnames';
import { X } from 'lucide-react';
import { ORTHODOX_PROBLEMS, TARGET_CASES, BROAD_APPROACHES } from '../constants';
import { getAgendasByAttribute } from '../utils/dataProcessing';

export type DefinitionType = 'all' | 'approach' | 'case' | 'problem';

interface DefinitionsModalProps {
  isOpen: boolean;
  onClose: () => void;
  initialScrollToId?: string;
  activeType?: DefinitionType;
}

export const DefinitionsModal: React.FC<DefinitionsModalProps> = ({ 
  isOpen, 
  onClose, 
  initialScrollToId, 
  activeType = 'all' 
}) => {
  const modalRef = useRef<HTMLDivElement>(null);
  const contentRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleEsc = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    window.addEventListener('keydown', handleEsc);
    return () => window.removeEventListener('keydown', handleEsc);
  }, [onClose]);

  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
      // Scroll to target if provided
      if (initialScrollToId && contentRef.current) {
        setTimeout(() => {
          const el = document.getElementById(initialScrollToId);
          if (el) {
            el.scrollIntoView({ behavior: 'smooth' });
          }
        }, 100);
      }
    } else {
      document.body.style.overflow = 'unset';
    }
  }, [isOpen, initialScrollToId]);

  const handleBackdropClick = (e: React.MouseEvent) => {
    if (modalRef.current && !modalRef.current.contains(e.target as Node)) {
      onClose();
    }
  };

  if (!isOpen) return null;

  const agendasByAttribute = getAgendasByAttribute();

  interface DefinitionItem {
    name: string;
    url: string;
    description?: string;
  }

  const renderSection = (title: string, items: Record<string, DefinitionItem>, type: 'approach' | 'case' | 'problem') => (
    <div className="def-section">
      {/* Only show section title if showing all, or maybe always? 
          If showing single type, the Modal Header is the title. 
          But "Broad Approaches" vs "Target Cases" is good to keep inside too if we want.
          However, the user wants "3 modals". 
          If I am in "Approaches Modal", I don't need a "Broad Approaches" subheader if the modal title is that.
          But let's keep it simple for now and keep the subheader, or remove it if activeType is specific.
      */}
      {activeType === 'all' && <h3 className="def-section-title">{title}</h3>}
      
      {Object.entries(items).map(([key, item]) => {
        const id = `def:${type}:${key}`;
        const agendas = agendasByAttribute[type]?.[key] || [];
        
        return (
          <div key={key} id={id} className="def-item">
            <h4 className="def-name">
              <a href={item.url} target="_blank" rel="noopener noreferrer">{item.name}</a>
            </h4>
            {item.description && (
              <p className="def-description">{item.description}</p>
            )}
            <div className="def-agendas">
              <strong>Agendas:</strong>
              {agendas.length > 0 ? (
                <ul>
                  {agendas.map((agenda: any) => (
                    <li key={agenda.id}>
                      <a href={`#${agenda.id}`} onClick={onClose}>{agenda.name}</a>
                    </li>
                  ))}
                </ul>
              ) : (
                <span className="no-agendas"> None listed</span>
              )}
            </div>
          </div>
        );
      })}
    </div>
  );

  const getModalHeader = () => {
    switch(activeType) {
      case 'approach': return { title: 'Broad Approaches', subtitle: 'General methodologies for alignment' };
      case 'case': return { title: 'Target Cases', subtitle: 'Specific deployment scenarios' };
      case 'problem': return { title: 'Orthodox Problems', subtitle: 'Standard alignment difficulties' };
      default: return { title: 'Definitions & Summaries', subtitle: 'Key concepts used in the taxonomy' };
    }
  };

  const { title, subtitle } = getModalHeader();

  return (
    <div 
      className={classNames('modal-overlay', { open: isOpen })}
      onClick={handleBackdropClick}
    >
      <div className="modal-content definitions-modal" ref={modalRef}>
        <button className="close-button" onClick={onClose} aria-label="Close">
          <X size={24} />
        </button>

        <div className="modal-header">
          <h2>{title}</h2>
          <div className="meta-summary">{subtitle}</div>
        </div>

        <div className="modal-body" ref={contentRef}>
          {(activeType === 'all' || activeType === 'approach') && 
            renderSection('Broad Approaches', BROAD_APPROACHES, 'approach')}
          {(activeType === 'all' || activeType === 'case') && 
            renderSection('Target Cases', TARGET_CASES, 'case')}
          {(activeType === 'all' || activeType === 'problem') && 
            renderSection('Orthodox Problems', ORTHODOX_PROBLEMS, 'problem')}
        </div>
      </div>
    </div>
  );
};
