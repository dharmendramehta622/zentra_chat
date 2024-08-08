// components/Sidebar.tsx
"use client";

import { useState } from "react";
import CustomButton from "./buttons/customButtons";
import { useRouter } from "next/navigation";
import Image from 'next/image';

// Define the type for the dashboard items
interface DashboardItem {
  icon: string;
  name: string;
}

const dashboardItems: DashboardItem[] = [
    { icon: "./dashboard.svg", name: "home" },
    // { icon: "./users.svg", name: "Users" },
    // { icon: "./dashboard.svg", name: "Attendance" },
];
interface SidebarProps {
   
    selectedItem: number;
    onSelectItem: (index: number) => void;
  }
  
  const Sidebar: React.FC<SidebarProps> = ({  selectedItem, onSelectItem }) => {
    const router = useRouter();
  
    const handleNavigation = (index: number) => {
      onSelectItem(index);
      switch (index) {
        case 0:
          router.push("/home");
          break;
        case 1:
          router.push("/users");
          break;
        case 2:
          router.push("/attendance");
          break;
        default:
          router.push("/dashboard");
      }
    };
  
    const handleLogout = () => {
      localStorage.removeItem("token");
      router.push("/login");
    };
  
    return (
      <div className="w-1/5 bg-white pt-[23px] p-[25px] flex flex-col">
        {dashboardItems.map((item, index) => (
          <CustomButton
            key={index}
            index={index}
            icon={item.icon}
            name={item.name}
            selected={selectedItem === index}
            onClick={() => handleNavigation(index)}
          />
        ))}
        <button
          onClick={handleLogout}
          className="w-full items-center justify-start flex py-[14px] px-[12px] mt-auto rounded-[8px] bg-primary600 text-white"
        >
          <Image src="./logout.svg" width={18} height={18} className="fluid w-[18px] h-[18px] Image-white" alt="Logout" />
          <p className="ml-2">Logout</p>
        </button>
      </div>
    );
  };
  
  export default Sidebar;
// const Sidebar = () => {
//   const [selectedItem, setSelectedItem] = useState<number | null>(0);
//   const router = useRouter();

//   const handleNavigation = (index: number) => {
    
//     switch (index) {
//       case 0:
//         router.replace ('/dashboard');
//         break;
//       case 1:
//         router.replace('/users');
//         break;
//       case 2:
//         router.replace('/attendance');
//         break;
      
//     }
//   };

//   const handleLogout = () => {
//     localStorage.removeItem("token");
//     router.push('/login');
//   };

//   return (
//     <div className="w-1/5 bg-white pt-[23px] p-[25px] flex flex-col">
//       {dashboardItems.map((item, index) => (
//         <CustomButton
//           key={index}
//           index={index}
//           icon={item.icon}
//           name={item.name}
//           selected={selectedItem === index}
//               onClick={() => {
//                 setSelectedItem(index);
//                   handleNavigation(index)
//               }}
//         />
//       ))}
//       <button
//         onClick={handleLogout}
//         className="w-full items-center justify-start flex py-[14px] px-[12px] mt-auto rounded-[8px] bg-primary600 text-white"
//       >
//         <Image src="./logout.svg" className="fluid w-[18px] h-[18px] Image-white" alt="Logout" />
//         <p className="ml-2">Logout</p>
//       </button>
//     </div>
//   );
// };

// export default Sidebar;
