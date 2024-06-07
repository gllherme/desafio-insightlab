import { Column } from "react-table";
import styles from "./page.module.css";
import Table from "@/components/Table";
import { useMemo } from "react";
import Autocomplete from "@/components/Autocomplete";

export default function Home() {
  const data = useMemo(
    () => [
      {
        col1: "Hello",
        col2: "World",
      },

      {
        col1: "react-table",
        col2: "rocks",
      },

      {
        col1: "whatever",
        col2: "you want",
      },
    ],
    []
  );

  const columns: Array<Column> = useMemo(
    () => [
      { Header: "Column 1", accessor: "col1" },
      { Header: "Column 2", accessor: "col2" },
    ],
    []
  );

  return (
    <main className={styles.main}>
      <div>
        <div className={styles.inputs}>
          <Autocomplete suggestions={["a", "aaaaa", "b", "c"]} />
        </div>
        <Table data={data} columns={columns} />
      </div>
    </main>
  );
}
