"use client";

import { ChangeEvent, useState } from "react";
import Input from "../Input";
import styles from "./registerform.module.css";
import Button from "../Button";

export default function RegisterForm() {
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

  const submit = () => {
    if (values.password !== values.passwordConfirm) {
      return console.log("a");
    }
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
      <section>
        <h4>Confirmar senha</h4>
        <Input id="passwordConfirm" type="password" onChange={handleChange} />
      </section>
      <Button text="Registrar" type="button" onClick={submit} />
    </div>
  );
}
