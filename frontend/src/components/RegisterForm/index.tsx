"use client";

import api from "@/api/api";
import { useRouter } from "next/navigation";
import { ChangeEvent, useState } from "react";
import Button from "../Button";
import Input from "../Input";
import styles from "./registerform.module.css";

export default function RegisterForm() {
  const router = useRouter();

  const [values, setValues] = useState({
    username: "",
    password: "",
    passwordConfirm: "",
  });

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const id = e.target.id;
    const value = e.target.value;

    setValues((prevValues) => ({
      ...prevValues,
      [id]: value,
    }));
  };

  const submit = async () => {
    if (values.password !== values.passwordConfirm) {
      setValues({ username: "", password: "", passwordConfirm: "" });
      return;
    }

    try {
      await api.post("/auth/register", values);
      router.push("/");
    } catch (e: any) {
      setValues({ username: "", password: "", passwordConfirm: "" });
      alert(e.response.data.detail);
    }
  };

  return (
    <div className={styles.card}>
      <section>
        <h4>Username</h4>
        <Input id="username" onChange={handleChange} />
      </section>
      <section>
        <h4>Senha</h4>
        <Input id="password" type="password" onChange={handleChange} />
      </section>
      <section>
        <h4>Confirmar senha</h4>
        <Input id="passwordConfirm" type="password" onChange={handleChange} />
      </section>
      <Button text="Registrar" type="button" onClick={submit} />
    </div>
  );
}
