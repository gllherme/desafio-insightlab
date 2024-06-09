"use client";

import api from "@/api/api";
import { useRouter } from "next/navigation";
import { useEffect } from "react";

export default function isAuth(Component: React.FC) {
  return function isAuth(props: any) {
    const router = useRouter();
    let token = "";
    const isAuth = token !== "undefined" && token !== null;

    const checkAuth = async () => {
      try {
        const { status } = await api.get("/auth/me", {
          headers: { Authorization: "Bearer " + token },
        });
        if (status === 200) {
          return;
        }
      } catch (e) {
        localStorage.removeItem("accessToken");
        router.push("/auth");
      }
    };

    useEffect(() => {
      token = localStorage.getItem("accessToken") as string;

      checkAuth();

      if (!isAuth) {
        return router.push("/auth");
      }
    }, []);

    if (!isAuth) {
      return null;
    }

    return <Component {...props} />;
  };
}
