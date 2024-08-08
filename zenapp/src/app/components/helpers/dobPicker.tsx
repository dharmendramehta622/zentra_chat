import React, { useState, forwardRef } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

interface CustomInputProps {
  value?: string;
  onClick?: () => void;
}

const CustomInput = forwardRef<HTMLInputElement, CustomInputProps>(({ value, onClick }, ref) => (
  <input
    type="text"
    className="p-2 w-full h-[46px] rounded-[8px] shadow-xs border border-[#D0D5DD] focus:outline-none transition duration-150"
    onClick={onClick}
    value={value}
    readOnly
    placeholder="Select Date"
    ref={ref}
  />
));


CustomInput.displayName = "CustomInput";
export default CustomInput;
