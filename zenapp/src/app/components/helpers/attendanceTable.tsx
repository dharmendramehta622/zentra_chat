import React, { useCallback, useEffect, useState } from 'react';
import { useAttendanceContext } from '@/app/context/attendaceContext';
import { AxiosServices } from '@/app/services/api_services';
import { calculateTotalHours, formatDateString, roundToTwoDecimalPlaces } from './dateTimeFormat';

const AttendanceTable:React.FC = () => {
    const { attendance, fetchAttendance } = useAttendanceContext();
    
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    
    
   useEffect(() => {
    if (attendance.length === 0) {
      setLoading(true);
      fetchAttendance().finally(() => setLoading(false));
    }
  }, [attendance, fetchAttendance]);
    return (
        <div className="w-full grid rounded-[14px] bg-white mt-[20px]">
                <p className="font-semibold ml-[10px] py-[14px]  text-[20px] ">Attendance List</p>

            <div className="bg-primary600 w-full px-[10px] h-[62px] items-center text-white py-[8px] flex justify-between ">
                <p className="font-bold text-left flex-1 min-w-[150px]">Date</p>
                <p className="font-bold text-left flex-1 min-w-[120px]">Longitude</p>
                <p className="font-bold text-left flex-1 min-w-[120px]">Latitude</p>
                <p className="font-bold text-left flex-1 min-w-[150px]">Check-In</p>
                <p className="font-bold text-left flex-1 min-w-[150px]">Check-Out</p>
                <p className="font-bold text-left flex-1 min-w-[150px]">Total Hours</p>
                <p className="font-bold text-left flex-1 min-w-[150px]">Status</p>
                {/* Add more headers here if needed */}
            </div>
            <div className="bg-white w-full">
                {attendance.map((item, index) => (
                    <div key={index} className="w-full px-[10px] py-[8px] min-h-[50px] items-center flex justify-between border-b border-gray-100">
                        <p className="text-left flex-1 min-w-[150px] ">{formatDateString(item.created_at)}</p>
                        <p className="text-left flex-1 min-w-[120px]">{roundToTwoDecimalPlaces(item.long) }</p>
                        <p className="text-left flex-1 min-w-[120px]">{roundToTwoDecimalPlaces(item.lat)}</p>
                        <p className="text-left flex-1 min-w-[150px]">{formatDateString(item.check_in)}</p>
                        <p className="text-left flex-1 min-w-[150px]">{formatDateString(item.check_out)}</p>
                        <p className="text-left flex-1 min-w-[150px]">{calculateTotalHours(item.check_out,item.check_in)}</p>
                        <div className=" text-left bg-green flex-1 min-w-[150px]">
                            Present
                            </div>
                        
                        {/* <p className="text-left flex-1 min-w-[150px]">{item.year}</p> */}
                        {/* Add more data fields here if needed */}
                    </div>
                ))}
            </div>
        </div>
    );
};

export default AttendanceTable;
{/* <table className="table w-full bg-white">
<thead className=" border border-1  h-[50px] border-primary600">
    <tr className="text-left ">
    <th className="px-3">Song</th>
    <th >Artist</th>
    <th>Artist</th> 
    <th>Artist</th>
    <th>Artist</th>
    <th>Artist</th>
    <th>Artist</th>
    <th>Year</th>
    </tr>
</thead>
<tbody className=" space-y-4">
    <tr className="mb-4">
    <td className="px-3 ">The Sliding Mr. Bones (Next Stop, Pottersville)</td>
    <td >Malcolm Lockyer</td>
    <td>Malcolm Lockyer</td>
    <td>Malcolm Lockyer</td>
    <td>Malcolm Lockyer</td>
    <td>Malcolm Lockyer</td>
    <td>Malcolm Lockyer</td>
    <td>1961</td>
                            </tr>
                            
    <tr >
    <td className="px-3">The Sliding Mr. Bones (Next Stop, Pottersville)</td>
    <td >Malcolm Lockyer</td>
    <td>Malcolm Lockyer</td>
    <td>Malcolm Lockyer</td>
    <td>Malcolm Lockyer</td>
    <td>Malcolm Lockyer</td>
    <td>Malcolm Lockyer</td>
    <td>1961</td>
    </tr>
    <tr >
    <td className="px-3">The Sliding Mr. Bones (Next Stop, Pottersville)</td>
    <td >Malcolm Lockyer</td>
    <td>Malcolm Lockyer</td>
    <td>Malcolm Lockyer</td>
    <td>Malcolm Lockyer</td>
    <td>Malcolm Lockyer</td>
    <td>Malcolm Lockyer</td>
    <td>1961</td>
    </tr>
    
</tbody>
</table> */}
