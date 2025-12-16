/**
 * Main App component with routing
 */

import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Home, ApproachesIndex, ProblemsIndex } from './pages';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/approaches" element={<ApproachesIndex />} />
        <Route path="/problems" element={<ProblemsIndex />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
