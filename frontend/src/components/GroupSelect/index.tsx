import styles from "./groupselect.module.css";

interface Option {
  id: number;
  name: string;
}

interface Group {
  category: string;
  values: Array<Option>;
}

interface Props {
  readonly options: Array<Group>;
}

export default function Select({ options }: Props) {
  return (
    <select className={styles.select}>
      {options?.map(({ category, values }) => (
        <optgroup label={category}>
          {values.map(({ id, name }) => (
            <option id={id.toString()}>{name}</option>
          ))}
        </optgroup>
      ))}
    </select>
  );
}
