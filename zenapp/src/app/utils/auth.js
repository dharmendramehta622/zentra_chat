import { LocalStorageService,LocalStorageServiceItems } from "../services/storage_services";

export const isUserLoggedIn = () => {
    if (typeof window !== 'undefined') {
        const token = LocalStorageService.instance.get(LocalStorageServiceItems.ACCESS_TOKEN)

        return !!token;
    }
    return false;
}
