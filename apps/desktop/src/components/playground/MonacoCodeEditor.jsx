import React from 'react';
import Editor from '@monaco-editor/react';
import { useTheme } from '../../contexts/ThemeContext';

export default function MonacoCodeEditor({
  code,
  onChange,
  language = 'python',
  height = '100%',
  readOnly = false
}) {
  const { theme } = useTheme();

  return (
    <div style={{ width: '100%', height: '100%', overflow: 'hidden', borderRadius: 'var(--radius-md)' }}>
      <Editor
        height={height}
        language={language}
        value={code}
        onChange={onChange}
        theme={theme === 'dark' ? 'vs-dark' : 'light'}
        options={{
          fontSize: 14,
          fontFamily: "'JetBrains Mono', Consolas, monospace",
          minimap: { enabled: false },
          scrollBeyondLastLine: false,
          automaticLayout: true,
          readOnly: readOnly,
          tabSize: 4,
          insertSpaces: true,
          lineNumbers: 'on',
          roundedSelection: false,
          padding: { top: 12, bottom: 12 },
        }}
      />
    </div>
  );
}
