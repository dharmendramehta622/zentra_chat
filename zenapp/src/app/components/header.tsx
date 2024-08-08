import Image from 'next/image';

const CustomHeader = () => {
    return <>
    <div className="flex w-full bg-[#F7F4FE] h-[84px]  ">
        <div className="w-1/5 flex bg-white items-center pl-[37px] p-4">
          <Image width={44} height={38} src="./logo.svg" className="fluid w-[44px] h-[38px]" alt="Logo" />
          <p className="text-primary600 text-2xl font-bold">ZENCHAT</p>
        </div>
        <div className="w-4/5 flex justify-between items-center bg-white ml-1 pl-[37px]">
          <div className="relative w-[402px] h-[42px]">
            <input
              type="text"
              placeholder="Search"
              className="border rounded-[49px] h-full w-full pl-[40px] pr-[10px] bg-[#F7F4FE] focus:outline-none"
            />
            <Image width={18} height={18}
              src="./search.svg"
              alt="Search"
              className="absolute left-[12px] top-1/2 transform -translate-y-1/2 w-[18px] h-[18px]"
            />
          </div>
          <div className="flex justify-between items-center px-[20px]">
            <Image width={18} height={20}
              src="./notification.svg"
              alt="Notifications"
              className="mr-[20px] w-[18px] h-[20px]"
            />
            <Image width={40} height={40}
              src="./user.png"
              alt="User"
              className="mr-[20px] w-[40px] h-[40px]"
            />
            <div className="grid">
              <p>User</p>
              <p>user@zenchat.com</p>
            </div>
          </div>
        </div>
      </div>
    </>
}
export default CustomHeader;