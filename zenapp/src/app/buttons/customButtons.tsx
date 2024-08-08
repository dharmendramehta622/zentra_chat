import React, { useState }  from "react";
import Image from 'next/image';

interface CustomButtonProps{
    icon: string;
    name: string;
    index: number;
    selected: boolean;
    onClick: () => void;
}
const CustomButton:React.FC<CustomButtonProps> = ({icon,name,index,selected,onClick}) => {
    var [itemSelected, setIemSelected] = useState(1);

    const selectItem = () => {
        
    }
    return <>
        <button key={index}
    onClick={onClick}
            className={`w-full items-center justify-start flex  py-[14px] px-[12px]   mt-4 rounded-[8px] ${!selected?"text-black bg-white":"bg-primary600  text-white"}`}>
                        <Image src={icon} width={18} height={18} className={`fluid  w-[18px] h-[18px]   ${selected?"Image-white":"Image-black"}`} alt="" />
                           
                                <p className="ml-2">{name}</p>
                           
                        </button>
    </>;
}
export default CustomButton;

