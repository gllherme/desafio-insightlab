"use client";

import { redirect } from "next/navigation";
import { useEffect } from "react";

const isAuthenticated = false;

export default function isAuth(Component: React.FC) {
  return function isAuth(props: any) {
    const auth = isAuthenticated;

    useEffect(() => {
      if (!auth) {
        return redirect("/auth");
      }
    }, []);
    if (!auth) {
      return null;
    }

    return <Component {...props} />;
  };
}
