"use client";

import api from "@/api/api";
import { useRouter } from "next/navigation";
import { ChangeEvent, useState } from "react";
import Button from "../Button";
import Input from "../Input";
import styles from "./loginform.module.css";

export default function LoginForm() {
  const router = useRouter();
  const [values, setValues] = useState({ username: "", password: "" });

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const id = e.target.id;
    const value = e.target.value;

    setValues((prevValues) => ({
      ...prevValues,
      [id]: value,
    }));
  };

  const submit = async () => {
    try {
      const { data } = await api.post("/auth/token", values);
      localStorage.setItem("accessToken", data.access_token);
      router.push("/");
    } catch (e: any) {
      localStorage.removeItem("accessToken");
      setValues({ username: "", password: "" });
      alert(e.response.data.detail);
    }
  };

  return (
    <div className={styles.card}>
      <section>
        <h4>Username</h4>
        <Input id="username" value={values.username} onChange={handleChange} />
      </section>
      <section>
        <h4>Senha</h4>
        <Input
          id="password"
          value={values.password}
          type="password"
          onChange={handleChange}
        />
      </section>
      <Button text="Login" type="button" onClick={submit} />
    </div>
  );
}
