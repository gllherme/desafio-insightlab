import { SelectHTMLAttributes } from "react";
import styles from "./groupselect.module.css";

interface Option {
  id: number;
  name: string;
}

interface Group {
  category: string;
  values: Array<Option>;
}

interface Props extends SelectHTMLAttributes<HTMLSelectElement> {
  readonly options: Array<Group>;
}

export default function GroupSelect({ options, ...props }: Props) {
  return (
    <select className={styles.select} {...props}>
      <option id="">Selecione uma opção</option>
      {options?.map(({ category, values }) => (
        <optgroup key={category} label={category}>
          {values.map(({ id, name }) => (
            <option key={id.toString()} id={id.toString()}>
              {name}
            </option>
          ))}
        </optgroup>
      ))}
    </select>
  );
}
