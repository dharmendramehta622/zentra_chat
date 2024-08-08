// pages/dashboard.tsx
"use client";

import withAuth from "../components/withAuth";
import Sidebar from "../components/sidebar";
import DashboardItem from "../components/items/dashboardItem";
import { useCallback, useEffect, useState } from "react";
import CustomHeader from "../components/header";
import { AxiosServices } from "../services/api_services";
import { User } from "../models/user";
import AttendanceTable from "../components/helpers/attendanceTable";



const DashBoard: React.FC = () => {
    const [selectedItem, setSelectedItem] = useState<number>(0);
   
  return (
    <div className="flex flex-col bg-[#F7F4FE] w-screen h-screen">
     <CustomHeader/>
      <div className="flex flex-grow w-full bg-[#F7F4FE] mt-1">
        <Sidebar  selectedItem={selectedItem} onSelectItem={setSelectedItem} />
        <div className="w-4/5 flex flex-col ml-1 pt-[23px] px-[35px]">
          <DashboardItem />
          <AttendanceTable/>
        </div>
      </div>
    </div>
  );
};

export default withAuth(DashBoard);
