import { SelectHTMLAttributes } from "react";
import styles from "./select.module.css";

interface Option {
  id: string;
  name: string;
}

interface Props extends SelectHTMLAttributes<HTMLSelectElement> {
  readonly options: Array<Option>;
}

export default function Select({ options, ...props }: Props) {
  return (
    <select className={styles.select} {...props}>
      <option id="">Selecione uma opção</option>
      {options.map((option) => (
        <option key={option.id} id={option.id}>
          {option.name}
        </option>
      ))}
    </select>
  );
}
