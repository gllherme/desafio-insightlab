"use client";

import { ChangeEvent, useState } from "react";
import Button from "../Button";
import Input from "../Input";
import styles from "./loginform.module.css";

export default function LoginForm() {
  const [values, setValues] = useState({ username: "", password: "" });

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const id = e.target.id;
    const value = e.target.value;

    setValues((prevValues) => ({
      ...prevValues,
      [id]: value,
    }));
  };

  const submit = () => {
    console.log(values);
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
      <Button text="Login" type="button" onClick={submit} />
    </div>
  );
}
