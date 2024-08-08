"use client"

import { createContext, ReactNode, useCallback, useContext, useState } from "react";
import { User } from "../models/user";
import { Attendance } from "../models/attendance";
import { AxiosServices } from "../services/api_services";

interface AttendanceContextType{
  attendance: Attendance[];
  // isActiveAttendance: boolean;
  // setIsActiveAttendance: (isActiveAttendance: boolean) => void;
  setAttendance: (attendance: Attendance[]) => void;
  fetchAttendance: () => Promise<void>;
}
const AttendanceContext = createContext<AttendanceContextType | undefined>(undefined);

export const AttendanceProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [attendance, setAttendance] = useState<Attendance[]>([]);
  // const isActive: boolean = attendance.some((val) => !val.check_out);
  // const [isActiveAttendance, setIsActiveAttendance] = useState(isActive);
  const fetchAttendance = useCallback(async () => {
    try {
      const api = new AxiosServices();
      const _res = await api.get('attendance/clockin/', {});
      setAttendance(_res.msg['results']['results']);
    } catch (error) {
      console.error('Failed to fetch attendance', error);
    }
  }, []);
    return (
      <AttendanceContext.Provider value={{ attendance,setAttendance,fetchAttendance }}>
        {children}
      </AttendanceContext.Provider>
    );
  };
  
  export const useAttendanceContext = () => {
    const context = useContext(AttendanceContext);
    if (context === undefined) {
      throw new Error('useUserContext must be used within a UserProvider');
    }
    return context;
  };
  