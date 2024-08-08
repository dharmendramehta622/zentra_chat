import React from 'react';

interface AlertDialogProps {
    message: string;
    onClose: () => void;
    onCancel: () => Promise<void>;
}

const AlertDialog: React.FC<AlertDialogProps> = ({ message, onClose,onCancel }) => {
    return (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
            <div className="bg-white p-6 rounded-[16px] ">
                <p className='font-bold'>{message}</p>
                <div className="flex justify-between gap-3">
        
                <button
                    onClick={onClose}
                    className="mt-4 w-[215px] bg-[#F2F4F7] text-black font-semibold rounded-[11px] py-2 px-4 rounded"
                >
                    Cancel
                    </button>
                    <button
                    onClick={onCancel}
                    className="mt-4 w-[215px] bg-primary600 text-white py-2 px-4 rounded-[11px]"
                >
                    Close
                </button>        

                </div>
                
            </div>
        </div>
    );
};

export default AlertDialog;