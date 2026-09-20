import React from 'react';
import { Loader2 } from 'lucide-react';

export default function LoadingSpinner({ message = 'Loading AI Learning Lab...' }) {
  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      height: '100%',
      minHeight: '280px',
      gap: '16px',
      color: 'var(--text-secondary)'
    }}>
      <Loader2 size={36} className="animate-spin" style={{ color: 'var(--accent-primary)', animation: 'spin 1s linear infinite' }} />
      <p style={{ fontSize: '0.9rem', fontWeight: 500 }}>{message}</p>
      <style>{`
        @keyframes spin {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
}
