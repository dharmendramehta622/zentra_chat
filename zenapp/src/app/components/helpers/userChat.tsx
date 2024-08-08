import { LocalStorageService, LocalStorageServiceItems } from '@/app/services/storage_services';
import React, { useState,useEffect,useRef}  from 'react'; 

interface UserChatProps {
  user: User;
}

const UserChat:React.FC<UserChatProps> = ({ user }) => {
      
     const [text, settext] = useState('');
     const [messages, setMessages] = useState<string[]>([]); 
     const socket = useRef<WebSocket | null>(null);


    useEffect(() => {

    // Establish WebSocket connection
    socket.current = new WebSocket('ws://localhost:8000/ws/ws/chat/');

    // Handle incoming messages
    socket.current.onmessage = (event) => {
      const newMessage = event.data;
      setMessages((prevMessages) => [...prevMessages, newMessage]);
    };

    // Handle WebSocket open event
    socket.current.onopen = () => {
      console.log('WebSocket connection established');
    };

    // Handle WebSocket errors
    socket.current.onerror = (error) => {
      console.error('WebSocket error:', error);
    };

    // Handle WebSocket connection closure
    socket.current.onclose = () => {
      console.log('WebSocket connection closed');
    };

    // Clean up WebSocket connection when the component unmounts
    return () => {
      if (socket.current) {
        socket.current.close();
      }
    };
    }, []);

    const handleSendMessage = () => {
      if (socket.current && text.trim() !== '') {
        const user_id = LocalStorageService.instance.get(LocalStorageServiceItems.USER_ID)
        const payload = {
          "message":text,
          "sender": user_id,
          "receiver": user.id
        }
        socket.current.send(text);
        settext('');
      }
    };
    return (
        <div className="w-full max-h-full min-h-full flex flex-col items-start justify-between rounded-[14px] bg-white mt-[20px]">
          <div className="w-full h-1/5 p-2 border">
            {user.first_name } {user.last_name}
          </div>

          <div className="w-full h-3/5 p-2 border">
            Chat List
          </div>

          <div className="w-full flex flex-row items-start justify-around h-auto p-2 border">
          <input className="p-2 w-full h-[36px] rounded-[8px] border mr-1  focus:outline-none  transition duration-150" type="text" value={text} onChange={(e) => settext(e.target.value)}  placeholder="Type a message" />
           <button type="button" className='bg-primary600 text-white p-2 h-[36px] rounded-md text-center' onClick={handleSendMessage}>
             Send
          </button>
          </div>

        </div>
    );
};

export default UserChat;
 