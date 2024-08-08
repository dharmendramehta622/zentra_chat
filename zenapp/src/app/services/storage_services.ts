class LocalStorageService {
    static instance = new LocalStorageService();
  
    set(key: string, value: string) {
      if (typeof window !== 'undefined') {
        localStorage.setItem(key, value);
        return true;
      }
      return false; // Indicate that localStorage is not available on the server.
    }
  
    delete(key: string) {
      if (typeof window !== 'undefined') {
        localStorage.removeItem(key);
        return true;
      }
      return false;
    }
  
    get(key: string) {
      if (typeof window !== 'undefined') {
        return localStorage.getItem(key);
      }
      return null; // Indicate that localStorage is not available on the server.
    }
  }
  
  const LocalStorageServiceItems = {
    ACCESS_TOKEN: 'access',
    REFRESH_TOKEN: 'refresh',
    USER_ID: 'user-id',
    AUTHORIZATION: 'Authorization',
    CURRENT_LOCATION: 'location',
    PHONE_VERIFIED: 'phone_verified',
    ROLE: 'role',
  };
  
  export { LocalStorageService, LocalStorageServiceItems };
  