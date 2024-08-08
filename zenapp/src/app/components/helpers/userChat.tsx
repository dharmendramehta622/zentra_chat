import React, { useState }  from 'react'; 



const UserChat:React.FC = () => {
      
     const [message, setmessage] = useState('');

    return (
        <div className="w-full max-h-full min-h-full flex flex-col items-start justify-between rounded-[14px] bg-white mt-[20px]">

          <div className="w-full h-1/5 p-2 border">
            Dharmendra Mehta
          </div>

          <div className="w-full h-3/5 p-2 border">
            Dharmendra Mehta
          </div>

          <div className="w-full flex flex-row items-start justify-around h-auto p-2 border">
          <input className="p-2 w-full h-[36px] rounded-[8px] border   focus:outline-none  transition duration-150" type="text" value={message} onChange={(e) => setmessage(e.target.value)}  placeholder="Type a message " />
           <button type="button" className='bg-primary600 text-white p-2 h-[36px] rounded-md text-center'>
             Send
          </button>
          </div>

        </div>
    );
};

export default UserChat;
 