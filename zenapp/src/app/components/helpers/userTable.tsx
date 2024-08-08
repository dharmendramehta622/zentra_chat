import React, { useCallback, useEffect, useState } from 'react';
import { User } from '../../models/user';
import { AxiosServices } from '@/app/services/api_services';
import { url } from 'inspector';
import { useUserContext } from '@/app/context/userContext';
import Image from 'next/image';

// import { useUserContext } from '../context/UserContext';
const UserTable:React.FC = () => {
    const { users, setUsers } = useUserContext();
    // const [users, setUsers] = useState<User[]>([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const fetchUsers = useCallback(async () => {
        setLoading(true);
        setError(null);
        try
        {
            const api = new AxiosServices();
            const _res = await api.get('user/admin/users/', {});
            console.log(_res.msg['results'])
            setUsers(_res.msg['results']);
        } catch (error) {
            setError('Failed to fetch users');
        }finally {
            setLoading(false);
          }
       
   },[setUsers]) 
    useEffect(() => {
        if (users.length === 0) {
            fetchUsers();
          }
    }, [fetchUsers,users]);
   
    return (
        <div className="w-full grid bg-white pt-[10px]">
                <p className="font-semibold ml-[10px] pb-[10px] text-[20px] ">Attendance List</p>

            <div className="bg-primary600 w-full px-[10px] h-[62px] items-center text-white py-[8px] flex justify-between ">
                <p className="font-bold text-left flex-1 min-w-[100px]">S.N</p>
                <p className="font-bold text-left flex-1 min-w-[200px]">User Name</p>
                <p className="font-bold text-left flex-1 min-w-[150px]">First Name</p>
                <p className="font-bold text-left flex-1 min-w-[120px]">Last Name</p>
                <p className="font-bold text-left flex-1 min-w-[250px]">Email</p>
                <p className="font-bold text-left flex-1 min-w-[150px]">Is Active</p>
                <p className="font-bold text-left flex-1 min-w-[120px]">Actions</p>
                {/* Add more headers here if needed */}
            </div>
            <div className="bg-white w-full">
                {users.map((item, index) => (
                    <div key={index} className="w-full px-[10px] py-[8px] min-h-[50px] items-center flex justify-between border-b border-gray-100">
                        <p className="text-left flex-1 min-w-[100px] ">{index+1}</p>
                        <p className="text-left flex-1 min-w-[200px]">{item.first_name}{item.last_name}</p>
                        <p className="text-left flex-1 min-w-[150px]">{item.first_name}</p>
                        <p className="text-left flex-1 min-w-[120px]">{item.last_name}</p>
                        <p className="text-left flex-1 word-wrap min-w-[250px]">{item.email}</p>
                        <p className="text-left flex-1 min-w-[150px]">{item.is_active}</p>
                        <div className="flex justify-start min-w-[120px] items-start ">
                        <Image width={18} height={18} src="./delete.svg" className="fluid  w-[18px] h-[18px]   " alt="" />
                        <Image width={18} height={18} src="./edit.svg" className="fluid  w-[18px] h-[18px] ml-2 " alt="" />
                        </div>
                        {/* <p className="text-left flex-1 min-w-[150px]">{item.year}</p> */}
                        {/* Add more data fields here if needed */}
                    </div>
                ))}
            </div>
        </div>
    );
};

export default UserTable;
