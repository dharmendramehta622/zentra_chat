"use-client";

import { useRouter } from "next/navigation";
import React,{useEffect, useState } from "react";
import { isUserLoggedIn } from "../utils/auth";

const withAuth = (WrappedComponent: React.ComponentType) => {
    return function AuthComponent() {
        const [loading, setLoading] = useState(true);
        const [isAuthenticated, setIsAuthenticated] = useState(false);
        const router = useRouter();

        useEffect(() => {
            const checkAuthStatus = () => {
                if (!isUserLoggedIn())
                {
                    router.push('/login');
                } else
                {
                    setIsAuthenticated(true);
                    setLoading(false);
                }
            };
            checkAuthStatus();
        }, [router]);
        if (loading)
        {
            return <></>
        }
        if (!isAuthenticated)
        {
            return null;
        }
        return <WrappedComponent />
    };

};

export default withAuth;