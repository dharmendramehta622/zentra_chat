import { useAttendanceContext } from '@/app/context/attendaceContext';
import { AxiosServices } from '@/app/services/api_services';
import React, { useState, useEffect } from 'react';
import { roundToSixDecimalPlaces } from '../helpers/dateTimeFormat';
import { currentDateTime } from '../helpers/helper';
import AlertDialog from '../helpers/alertDialog';
import Image from 'next/image';


// Modal.setAppElement('#__next'); 
const DashboardItem = () => {
    const [checkInTime, setCheckInTime] = useState<Date | null>(null);
    const [currentTime, setCurrentTime] = useState(new Date());
    const { attendance, setAttendance,fetchAttendance } = useAttendanceContext();
    const [isActive, setIsAcitve] = useState(false);
    const [isAlertOpen, setIsAlertOpen] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    // let isActive: boolean = attendance.some((val) => !val.check_out);
    const getLocationAndAddAttendance = () => {
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(
            async (position) => {
              const lat = `${position.coords.latitude}`;
                  const long = `${position.coords.longitude}`;
                  const lats = roundToSixDecimalPlaces(lat);
                  const longs = roundToSixDecimalPlaces(long);
              await addAttendance(lats, longs);
            },
            (error) => {
              console.error("Error obtaining location", error);
            }
          );
        } else {
          console.error("Geolocation is not supported by this browser.");
        }
    };
    const checkOut = async () => {
        setIsAlertOpen(false);
        setIsLoading(true);
        const attendanceRecord  = attendance.find((val) => val.check_out === '' || val.check_out === null);
        const id = attendanceRecord ? attendanceRecord.id : null;
        try {
            const api = new AxiosServices();
            const _response = await api.patch(`attendance/clockin/${id}/`, {"check_out" : currentDateTime})
            if (_response.status)
            {
                resetTimer();
                fetchAttendance();
                
            }
        } catch (error)
        {
            
        }
        setIsLoading(false);
    }
    const addAttendance = async (lat: number, long: number) => {
        setIsLoading(true);
        try
        {
            var _data = {
               
                "lat": `${lat}`,
                "long": `${long}`
            };
            const api = new AxiosServices();
            const _response = await api.post('attendance/clockin/', _data)
            if (_response.status)
            {
                handleCheckIn();
                const newAttendance = _response.msg;
                setAttendance([...attendance, newAttendance]);
                
            }

        } catch (error) {
            console.error("Failed to add attendance", error);
        }
        setIsLoading(false);
    }
    // Function to handle check-in
    const handleCheckIn = () => {
        setCheckInTime(new Date());
    };
    const resetTimer = () => {
        setCheckInTime(null);
        setCurrentTime(new Date());
    };
    const openAlert = () => {
        setIsAlertOpen(true);
    };
    
    // Update current time every second
    useEffect(() => {
        let isActi:boolean=attendance.some((val) => !val.check_out)
        setIsAcitve(isActi);
        const intervalId = setInterval(() => {
            setCurrentTime(new Date());
        }, 1000);
        
        return () => clearInterval(intervalId);
    }, [attendance]);
    
    // Calculate time difference
    const getTimeDifference = (startTime: Date | null, endTime: Date) => {
        if (!startTime) return { hours: 0, minutes: 0, seconds: 0 };

        const diffInMs = endTime.getTime() - startTime.getTime();
        if (diffInMs < 0) return { hours: 0, minutes: 0, seconds: 0 };

        const diffInSeconds = Math.floor(diffInMs / 1000);
        const hours = Math.floor(diffInSeconds / 3600);
        const minutes = Math.floor((diffInSeconds % 3600) / 60);
        const seconds = diffInSeconds % 60;

        return { hours, minutes, seconds };
    };

    const { hours, minutes, seconds } = getTimeDifference(checkInTime, currentTime);

    return (
        <div>
            <div className="flex items-center justify-center mb-3">
                <div className="flex flex-col rounded-[24px] bg-white w-[800px] h-[370px] p-[30px]">
                    <div className="mb-[30px] flex justify-between text-xl">
                        <p className="font-semibold">{currentTime.toDateString()}</p>
                        <p className="font-semibold">{currentTime.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</p>
                    </div>
                    <div className="flex justify-center">
                        <div className="rounded-[13px] mr-3 flex flex-col justify-center items-center bg-bgColor h-[93px] w-[93px]">
                            <p className="font-bold text-[30px]">{hours.toString().padStart(2, '0')}</p>
                            <p className="text-[14px]">HOURS</p>
                        </div>
                        <div className="rounded-[13px] mr-3 flex flex-col justify-center items-center bg-bgColor h-[93px] w-[93px]">
                            <p className="font-bold text-[30px]">{minutes.toString().padStart(2, '0')}</p>
                            <p className="text-[14px]">MINUTES</p> 
                        </div>
                        <div className="rounded-[13px] mr-3 flex flex-col justify-center items-center bg-bgColor h-[93px] w-[93px]">
                            <p className="font-bold text-[30px]">{seconds.toString().padStart(2, '0')}</p>
                            <p className="text-[14px]">SECONDS</p>
                        </div>
                    </div>
                    <div className="flex flex-col items-center mt-[20px]">
                        <p className="text-[18px] text-[#98A2B3]">General 10:00 AM to 06:00 PM</p>
                        <button 
                            className={`w-full items-center ${isActive ? 'bg-[#D92D20]' :'bg-[#12B76A]'  } max-w-[390px] justify-center flex py-[14px] px-[12px] mt-4 rounded-[13px] text-white`}
                            onClick={isActive?openAlert: getLocationAndAddAttendance}
                        >
                           <Image src="./checkIn.svg"  width={18} height={18} className="fluid w-[18px] h-[18px] Image-white" alt="Logout" />
                            <p className="ml-2">{isLoading?'Loading..':`${isActive ? 'Check Out' : 'Check In'}` } </p>
                        </button>
                        <div className="flex mt-6">
                            <p className="text-[16px] mr-4 font-semibold">View full day tracking</p>
                            <Image src="./down_arrow.svg" width={18} height={18} className="fluid w-[18px] h-[18px] Image-black" alt="Logout" />
                        </div>
                    </div>
                </div>
            </div>
            {isAlertOpen && (
                <AlertDialog
                    message="Are you sure want to Check out?"
                    onClose={() => setIsAlertOpen(false)}
                    onCancel={checkOut}
                />
            )}
        </div>
    );
};

export default DashboardItem;
