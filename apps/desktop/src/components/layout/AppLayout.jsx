import React from 'react';
import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar';
import TopNav from './TopNav';

export default function AppLayout() {
  return (
    <div className="app-container">
      <Sidebar />
      <div className="main-content-wrapper">
        <TopNav />
        <main className="page-scroll-area">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
