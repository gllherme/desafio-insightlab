import { ButtonHTMLAttributes } from "react";
import styles from "./button.module.css";

interface Props extends ButtonHTMLAttributes<HTMLButtonElement> {
  text: string;
}

export default function Button({ text, ...props }: Props) {
  return (
    <button className={styles.button} {...props}>
      {text}
    </button>
  );
}
