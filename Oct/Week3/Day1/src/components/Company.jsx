import React from "react";
import { Outlet } from "react-router";

const Company = () => {
  return (
    <div>
      <h2>Company Page</h2>
      <Outlet />
    </div>
  );
};

export default Company;