
export function formatDateString(dateStr: any): string {
    if (!dateStr) {
        return ''; // Return an empty string if dateStr is empty or falsy
    }

    const date = new Date(dateStr);

    if (isNaN(date.getTime())) {
        return ''; // Return an empty string if dateStr results in an invalid date
    }

    return date.toISOString().split('T')[0];
}

export const calculateTotalHours = (dateStr1: string, dateStr2: string): number | null => {
    // Return null if the end date is null
    if (!dateStr1) {
      return null;
    }
  
    // Parse the date strings into Date objects
    const date1 = new Date(dateStr1);
    const date2 = new Date(dateStr2);
  
    // Calculate the difference in milliseconds
    const diffInMilliseconds: number = Math.abs((date1 as unknown as number) - (date2 as unknown as number));
  
    // Convert milliseconds to hours
    const diffInHours: number = diffInMilliseconds / (1000 * 60 * 60);
    const roundedHours: number = parseFloat(diffInHours.toFixed(2));
  
    return roundedHours;
  };
  
export const roundToTwoDecimalPlaces = (numStr: string): number => {
    const num = parseFloat(numStr);
    return parseFloat(num.toFixed(2));
};
export const roundToSixDecimalPlaces = (numStr: string): number => {
    const num = parseFloat(numStr);
    return parseFloat(num.toFixed(6));
};

export  const formatDate = () => {
    const date = new Date();
    
    // Format for date (weekday, day, month, year)
    const dateOptions: Intl.DateTimeFormatOptions = {
        weekday: 'short',
        day: '2-digit',
        month: 'long',
        year: 'numeric'
    };
    
    // Format for time (hour, minute)
    const timeOptions: Intl.DateTimeFormatOptions = {
        hour: '2-digit',
        minute: '2-digit',
        hour12: true
    };
    
    const formattedDate = date.toLocaleDateString('en-US', dateOptions);
    const formattedTime = date.toLocaleTimeString('en-US', timeOptions);
    
    return formattedDate;
};
export  const formatTime = () => {
    const date = new Date();
    
  
    
    // Format for time (hour, minute)
    const timeOptions: Intl.DateTimeFormatOptions = {
        hour: '2-digit',
        minute: '2-digit',
        hour12: true
    };
    
   
    const formattedTime = date.toLocaleTimeString('en-US', timeOptions);
    
    return formattedTime;
};