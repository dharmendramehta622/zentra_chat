// pages/dashboard.tsx
"use client";

import withAuth from "../components/withAuth";
import CustomHeader from "../components/header";
import Sidebar from "../components/sidebar";
import DashboardItem from "../components/items/dashboardItem";
import { useState } from "react";
import UserItems from "../components/items/userItems";

// Define the type for the dashboard items


const Users=() => {
    const [selectedItem, setSelectedItem] = useState<number>(1); //

  return (
    <div className="flex flex-col bg-[#F7F4FE] w-screen h-screen">
      <CustomHeader/>
      <div className="flex flex-grow w-full bg-[#F7F4FE] mt-1">
        <Sidebar  selectedItem={selectedItem} onSelectItem={setSelectedItem} />
        <div className="w-4/5 flex flex-col ml-1 pt-[23px] px-[35px]">
          <UserItems />
        </div>
      </div>
    </div>
  );
};

export default withAuth(Users);
