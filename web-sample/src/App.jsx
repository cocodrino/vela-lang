import React, { useEffect, useMemo, useState } from 'react';

const FILTERS = ['all', 'poem', 'story'];

export default function App() {
  const [items, setItems] = useState([]);
  const [selectedId, setSelectedId] = useState(null);
  const [filter, setFilter] = useState('all');
  const [textBody, setTextBody] = useState('');
  const [loadingIndex, setLoadingIndex] = useState(true);
  const [loadingText, setLoadingText] = useState(false);
  const [indexError, setIndexError] = useState('');
  const [textError, setTextError] = useState('');
  const [audioError, setAudioError] = useState('');

  useEffect(() => {
    let active = true;
    async function loadIndex() {
      setLoadingIndex(true);
      setIndexError('');
      try {
        const res = await fetch('/content/index.json');
        if (!res.ok) throw new Error('No se pudo cargar content/index.json');
        const data = await res.json();
        if (!Array.isArray(data)) throw new Error('El índice debe ser un array JSON');
        if (!active) return;
        setItems(data);
        setSelectedId(data[0]?.id ?? null);
      } catch (err) {
        if (active) setIndexError(err.message);
      } finally {
        if (active) setLoadingIndex(false);
      }
    }

    loadIndex();
    return () => {
      active = false;
    };
  }, []);

  const filteredItems = useMemo(() => {
    if (filter === 'all') return items;
    return items.filter((item) => item.type === filter);
  }, [filter, items]);

  const selected = useMemo(
    () => items.find((item) => item.id === selectedId) ?? null,
    [items, selectedId]
  );

  useEffect(() => {
    let active = true;
    async function loadText() {
      if (!selected?.textPath) {
        setTextBody('');
        return;
      }
      setLoadingText(true);
      setTextError('');
      setAudioError('');
      try {
        const res = await fetch(selected.textPath);
        if (!res.ok) throw new Error('No se pudo cargar el texto');
        const body = await res.text();
        if (active) setTextBody(body);
      } catch (err) {
        if (active) {
          setTextError(err.message);
          setTextBody('');
        }
      } finally {
        if (active) setLoadingText(false);
      }
    }

    loadText();
    return () => {
      active = false;
    };
  }, [selected?.id, selected?.textPath]);

  return (
    <div className="layout">
      <aside className="sidebar">
        <h1>VELA Reader</h1>
        <p>Lee poemas y cuentos, y escucha su audio.</p>
        <div className="filters">
          {FILTERS.map((name) => (
            <button
              key={name}
              className={filter === name ? 'active' : ''}
              onClick={() => setFilter(name)}
            >
              {name}
            </button>
          ))}
        </div>

        {loadingIndex && <p>Cargando índice...</p>}
        {indexError && <p className="error">{indexError}</p>}

        <ul>
          {filteredItems.map((item) => (
            <li key={item.id}>
              <button
                className={selectedId === item.id ? 'selected' : ''}
                onClick={() => setSelectedId(item.id)}
              >
                <span>{item.title}</span>
                <small>{item.type}</small>
              </button>
            </li>
          ))}
        </ul>
      </aside>

      <main className="reader">
        {!selected ? (
          <p>Selecciona un texto.</p>
        ) : (
          <>
            <header>
              <h2>{selected.title}</h2>
              <p>{selected.description}</p>
            </header>

            <section className="audio-box">
              {selected.audioPath ? (
                <audio
                  key={selected.id}
                  controls
                  src={selected.audioPath}
                  onError={() => setAudioError('audio no disponible')}
                />
              ) : (
                <p className="muted">audio no disponible</p>
              )}
              {audioError && <p className="muted">{audioError}</p>}
            </section>

            <article>
              {loadingText && <p>Cargando texto...</p>}
              {textError && <p className="error">{textError}</p>}
              {!loadingText && !textError && <pre>{textBody}</pre>}
            </article>
          </>
        )}
      </main>
    </div>
  );
}
