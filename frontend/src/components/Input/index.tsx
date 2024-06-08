import { InputHTMLAttributes } from "react";
import styles from "./input.module.css";

interface Props extends InputHTMLAttributes<HTMLInputElement> {}

export default function Input({
  type = "text",
  placeholder = "Digite aqui",
  ...props
}: Props) {
  return (
    <input
      className={styles.input}
      type={type}
      placeholder={placeholder}
      {...props}
    />
  );
}
