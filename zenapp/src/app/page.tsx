"use client";
import { useEffect,useState } from "react";
import { useRouter } from "next/navigation";
import { isUserLoggedIn } from "./utils/auth";
import withAuth from "./components/withAuth";

const Home = () => {
  const router = useRouter();

  useEffect(() => {
    router.replace('/home');
  }, [router]);

  return null; // or a loading spinner if you prefer
};

export default Home;



