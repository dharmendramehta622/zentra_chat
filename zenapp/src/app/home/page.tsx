// pages/dashboard.tsx
"use client";

import withAuth from "../components/withAuth";
import Sidebar from "../components/sidebar";
import UserList from "../components/items/userList";
import { useCallback, useEffect, useState } from "react";
import CustomHeader from "../components/header";
import UserChat from "../components/helpers/userChat";



const DashBoard: React.FC = () => {

  const [selectedItem, setSelectedItem] = useState<number>(0);
   
  return (
    <div className="flex flex-col bg-[#F7F4FE] w-screen h-screen">
     <CustomHeader/>
      <div className="flex flex-grow w-full bg-[#F7F4FE] mt-1">
        <Sidebar  selectedItem={selectedItem} onSelectItem={setSelectedItem} />
        <div className="w-full ml-1 pt-[23px] px-[35px]">
           <UserList /> 
        </div>
      </div>
    </div>
  );

};

export default withAuth(DashBoard);
