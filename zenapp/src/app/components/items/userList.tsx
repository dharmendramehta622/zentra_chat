 
import { AxiosServices } from '@/app/services/api_services';
import React, { useState, useEffect } from 'react';
import UserChat from '../helpers/userChat';

const UserList = () => { 

   const [userList, setuserList] = useState<User[]>([]);
   const [activeIndex, setactiveIndex] = useState(-1);
   const [loading, setloading] = useState(true);

   useEffect(() => {

    const fetchData = async () => {
        try {
            const response = await AxiosServices.instance.get('user/users/list/',{});
            setuserList(response.msg.results);  
            setloading(false)
        } catch (error) {
            console.error('Error fetching user list:', error);
        }
    }; 
    fetchData();
   }, []);

    return (
        <div className="flex flex-row ">

        <div className='flex flex-col mr-3 w-1/3'>
              <div className="h4 mb-6 bg-white font-bold p-2">
                Click on a user to start a  conversation.
              </div>
              {!loading && (userList.map((e,index)=>{
                  const name = `${e.first_name}  ${e.last_name}`
                  return (
                  <div key={index} className='p-2 border bg-white my-1 cursor-pointer' onClick={()=>setactiveIndex(index)}>
                   {name}
                </div>
                )
              }))}
        </div> 
        {activeIndex !== -1 && (
                <UserChat user={userList[activeIndex]} />
            )}
    </div>
    );
};

export default UserList;
