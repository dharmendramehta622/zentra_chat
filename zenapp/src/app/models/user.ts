

export interface User {
    id: string;
    role: string;
    email: string;
    phone_no: string;
    first_name: string;
    last_name: string;
    user_image: string | null;
    is_active: boolean;
    date_joined: string;
    last_login: string;
    email_verified: boolean;
}
