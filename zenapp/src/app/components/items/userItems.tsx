// import AttendanceTable from "../helpers/AttendanceTable";
import UserTable from "../helpers/userTable";
import Image from 'next/image';

const UserItems = () => {
    return (
        <div>
             <div className="flex items-center justify-between mb-3">
                        <div className="grid">
                            <div className="flex items-center gap-1">
                            <p>Pages /</p>
                            <p className="text-primary600 text-xl">Users </p>

                            </div>
                            <p className="text-black text-2xl font-bold">Users </p>
                        </div>
                        <button  
                            className="w-auto items-center justify-start flex  py-[14px] px-[12px]   mt-4 rounded-[8px] bg-primary600  text-white">
                        <Image width={18} height={18} src="./add.svg" className="fluid  w-[18px] h-[18px]   Image-white" alt="" />
                           
                                <p className="ml-2"> Add Users</p>
                           
                        </button>
                       
                    </div>
                    
                    <UserTable/>
        </div>
    );
};

export default UserItems;