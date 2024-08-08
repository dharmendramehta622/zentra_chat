"use client"
import { useRouter } from "next/navigation";
import React, { useState,forwardRef  } from "react";
import { AxiosServices } from "../services/api_services";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import CustomInput from "../components/helpers/dobPicker";
import Image from 'next/image';

const Signup = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    // const [dob, setDob] = useState("");
    const router = useRouter();

    
    const handleSignUp = async () => { 
        setIsLoading(true); 
        var data = {
            "first_name": firstName,
            "last_name": lastName,
            "email": email,
            "password" :password
        }
        try {
            const _response = await   AxiosServices.instance.post('user/register/', data); 
            if(_response.status){ 
                router.replace('/login');
            }
            setIsLoading(false); 
        } catch (error) {
            console.error('SignUp failed:', error);
        }
        
    }
    const selectDate = () => {
        
    }
    return (<>
        <div className="mb-10"> 
           <Image  width={500} height={140} src="./auth-bg.svg" className="fluid mb-2 w-[500px] h-[140px]" alt="" />
            <div className="container p-[30px] mb-[40px] mx-auto auth-shadow   md:w-[450px] md:h-[650px] rounded-[20px]  items-center">
            <div className=" grid justify-start      bg-white ">
                
                <Image  width={18} height={18} src="./logo.svg" className=" pb-[12px]" alt="" />
                <p className=" text-black font-bold mb-4  text-2xl">Sign Up</p>
                
                <div className="grid md:w-[382px]   mb-4 ">
                <p className=" text-black  mb-2">First name*</p>
                <input required value={firstName} onChange={(e)=>setFirstName(e.target.value)} type="text" className="p-2 w-full h-[46px] rounded-[8px] shadow-xs border border-[#D0D5DD] focus:outline-none  transition duration-150" placeholder="Username " />
                </div>
                <div className="grid md:w-[382px]  mb-4">
                <p className=" text-black  mb-2">Last name*</p>
                <input required value={lastName} onChange={(e)=>setLastName(e.target.value)} type="text" className="p-2 w-full h-[46px] rounded-[8px] shadow-xs border border-[#D0D5DD] focus:outline-none  transition duration-150" placeholder="Username " />
                </div>
                <div className="grid md:w-[382px]  mb-4">
                <p className=" text-black  mb-2">Email*</p>
                <input required value={email} type="text" onChange={(e)=>setEmail(e.target.value)} className="p-2 w-full h-[46px] rounded-[8px] shadow-xs border border-[#D0D5DD] focus:outline-none  transition duration-150" placeholder="email " />
                </div>
                <div className="grid md:w-[382px]  mb-4">
                <p className=" text-black  mb-2">Password*</p>
                <input required value={password} type="text" onChange={(e)=>setPassword(e.target.value)} className="p-2 w-full h-[46px] rounded-[8px] shadow-xs border border-[#D0D5DD] focus:outline-none  transition duration-150" placeholder="password " />
                </div> 
                    <button onClick={handleSignUp} className="bg-primary600 text-white py-[11px] border border-primary600 shadow-xs mt-4 rounded-[8px] ">Sign up</button>
                    <div className="flex justify-center mt-4 "> 
                        <p >Already have an account?</p>
                        <a href="./login" className="px-1 text-primary600 font-bold">Log in</a>
                    
                    </div>
          </div>
            </div>
           


            
        </div>

    </> );
}
 
export default Signup;
