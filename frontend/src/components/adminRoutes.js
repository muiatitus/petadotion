import React from 'react';
import { Route, Routes } from 'react-router-dom';
import AdminDashboard from './AdminDashboard';
import UserManagement from './UserManagement';
import ContentManagement from './ContentManagement';

const AdminRoutes = () => {
  return (
    <Routes>
      <Route exact path="/admin/dashboard" component={AdminDashboard} />
      <Route exact path="/admin/users" component={UserManagement} />
      <Route exact path="/admin/content" component={ContentManagement} />
      {/* Add more routes for other admin functionalities */}
    </Routes>
  );
};

export default AdminRoutes;