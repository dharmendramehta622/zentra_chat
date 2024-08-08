
"use client";

import { useState } from "react";
import { AxiosServices } from "../services/api_services";
import { useRouter } from "next/navigation";
import Image from 'next/image';
import { LocalStorageService, LocalStorageServiceItems } from "../services/storage_services";
import { jwtDecode, JwtPayload } from "jwt-decode";

interface CustomJwtPayload extends JwtPayload {
    user_id: string;  
}

const Login = () => {

    const [isLoading, setIsLoading] = useState(false);
    const [userName, setUserName] = useState("");
    const [password, setPassword] = useState("");
    const router = useRouter();

    // dharmendramehta622@gmail.com
    // E4DOJ309#ESF
    const handleLogin = async () => {
        setIsLoading(true);
        try {
            const _response = await AxiosServices.instance.post('user/login/', { "email": userName, "password": password });

            if (_response.status) {
                const access = _response.msg.data.access;
                const decoded = jwtDecode<CustomJwtPayload>(access);
                
                LocalStorageService.instance.set(LocalStorageServiceItems.ACCESS_TOKEN, _response.msg.data.access)
                LocalStorageService.instance.set(LocalStorageServiceItems.USER_ID, decoded.user_id)
                LocalStorageService.instance.set(LocalStorageServiceItems.REFRESH_TOKEN, _response.msg.data.refresh)
                router.replace('/home');
            }
            setIsLoading(false);
        } catch (error) {
            console.error('Login failed:', error);
        }

    }

    return (<>
        <div className=" mb-20 ">
            <Image width={500} height={140} src="./auth-bg.svg" className="fluid mb-2 w-[500px] h-[140px]" alt="" />

            <div className="container p-[30px] mx-auto auth-shadow md:w-[450px] md:h-[550px]  rounded-[20px] items-center">
                <div className=" grid justify-start   w-auto   bg-white ">

                    <Image width={18} height={18} src="./logo.svg" className="pb-[24px]" alt="" />
                    <p className=" text-black font-bold mb-4 ">Login</p>
                    <p className=" text-black  mb-4">Welcome back!. Please enter your details.</p>
                    <div className="grid md:w-[382px] ">
                        <p className=" text-black  mb-2">Email</p>
                        <input type="text" value={userName} onChange={(e) => setUserName(e.target.value)} className="p-2 w-full h-[46px] rounded-[8px] border border-gray-500 focus:outline-none  transition duration-150" placeholder="Username " />
                    </div>
                    <div className="grid   mt-4">
                        <p className=" text-black  mb-2">Password</p>
                        <input type="text" value={password} onChange={(e) => setPassword(e.target.value)} className="p-2  h-[46px] rounded-[8px] border border-gray-500 focus:outline-none   transition duration-150" placeholder="*********" />


                    </div>
                    <div className="flex justify-between mt-4">
                        <div className="flex items-center">


                            <input type="checkbox" id="rememberMe" className="form-checkbox h-5 w-4 " />
                            <p className="p-2">Remember me for 30 days</p>
                        </div>
                        <a href="#" className="p-2 text-primary600 font-bold">Forgot password</a>

                    </div>
                    <button onClick={handleLogin} className=" bg-primary600 text-white py-[11px] border border-primary600 shadow-xs mt-4 rounded-[8px] "> {isLoading ? 'Loading...' : 'Login'} </button>

                    <div className="flex justify-center mt-4 ">


                        <p >Don&#39;t have an account?</p>
                        <a href="./signup" className="px-1 text-primary600 font-bold">Sign up</a>

                    </div>
                </div>
            </div>




        </div>

    </>);
}

export default Login;
