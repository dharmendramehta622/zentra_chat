 
import { AxiosServices } from '@/app/services/api_services';
import React, { useState, useEffect } from 'react';
import UserChat from '../helpers/userChat';

const UserList = () => { 

   const [userList, setuserList] = useState<User[]>([]);

   useEffect(() => {

    const fetchData = async () => {
        try {
            const response = await AxiosServices.instance.get('/user/users/list/',{});
            setuserList(response.msg.results);  
        } catch (error) {
            console.error('Error fetching user list:', error);
        }
    }; 
    fetchData();
   }, []);

    return (
        <div className="flex flex-row ">

        <div className='flex flex-col mr-3 w-1/3'>
              <div className="h4 mb-6">
              Start a  conversation.
              </div>
              {userList && (userList.map((e,index)=>{
                  const name = `${e.first_name}  ${e.last_name}`
                  return (<div key={index} className='p-2 border bg-white my-1'>
                   {name}
                </div>)
              }))}
        </div> 
        <UserChat/>
    </div>
    );
};

export default UserList;
