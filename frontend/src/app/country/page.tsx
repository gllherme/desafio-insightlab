"use client";

import api from "@/api/api";
import GroupSelect from "@/components/GroupSelect";
import Select from "@/components/Select";
import Table from "@/components/Table";
import isAuth from "@/components/isAuth";
import { ChangeEvent, useEffect, useMemo, useState } from "react";
import { Column } from "react-table";
import styles from "./page.module.css";
import Input from "@/components/Input";
import Button from "@/components/Button";

function Country() {
  let token = "";
  const authHeader = { Authorization: "Bearer " + token };
  const [countryData, setCountryData] = useState([]);
  const [countryCodes, setCountryCodes] = useState([]);
  const [indicators, setIndicators] = useState([]);
  const [selected, setSelected] = useState({
    countryCode: "",
    indicatorId: "",
  });
  const [filter, setFilter] = useState({ start_year: null, end_year: null });

  const columns: Array<Column> = useMemo(
    () => [
      { Header: "Ano", accessor: "year" },
      { Header: "Valor", accessor: "value" },
    ],
    []
  );

  // useEffect(() => {
  //   token = window.localStorage.getItem("accessToken") as string;
  // }, []);

  const fetchCountryCodes = async () => {
    try {
      const { data } = await api.get("/country/codes", {
        headers: authHeader,
      });
      const newOptions = data.map((option: any) => ({
        id: option.code,
        name: option.name,
      }));
      setCountryCodes(newOptions);
    } catch (e) {
      setCountryCodes([]);
    }
  };

  const fetchIndicators = async () => {
    try {
      const { data } = await api.get("/indicator/all", {
        headers: authHeader,
      });

      setIndicators(data);
    } catch (e) {
      setIndicators([]);
    }
  };

  useEffect(() => {
    fetchCountryCodes();
    fetchIndicators();
  }, []);

  const handleCountryCode = (e: ChangeEvent<HTMLSelectElement>) => {
    setSelected((prev) => ({
      ...prev,
      countryCode: e.target.options[e.target.selectedIndex].id,
    }));
  };

  const handleIndicator = (e: ChangeEvent<HTMLSelectElement>) => {
    setSelected((prev) => ({
      ...prev,
      indicatorId: e.target.options[e.target.selectedIndex].id,
    }));
  };

  const fetchCountryData = async () => {
    if (selected.countryCode === "" || selected.indicatorId === "") {
      return;
    }

    try {
      const { data } = await api.get(
        `/country/${selected.countryCode}/query/${selected.indicatorId}`,
        {
          headers: authHeader,
          params: { start_year: filter.start_year, end_year: filter.end_year },
        }
      );

      setCountryData(data.values);
    } catch (e) {
      setCountryData([]);
    }
  };

  const handleFilter = (e: ChangeEvent<HTMLInputElement>) => {
    setFilter((prev) => ({
      ...prev,
      [e.target.id]: e.target.value,
    }));
  };

  useEffect(() => {
    if (filter.start_year === "") {
      setFilter((prev) => ({
        ...prev,
        start_year: null,
      }));
    }
    if (filter.end_year === "") {
      setFilter((prev) => ({
        ...prev,
        end_year: null,
      }));
    }
  }, [filter]);

  return (
    <main className={styles.main}>
      <div className={styles.wrapper}>
        <div className={styles.inputs}>
          <Select options={countryCodes || []} onChange={handleCountryCode} />
          <GroupSelect options={indicators || []} onChange={handleIndicator} />
        </div>
        <div className={styles.inputs}>
          <Input
            id="start_year"
            value={filter.start_year || ""}
            placeholder="Ano de início"
            onChange={handleFilter}
          />
          <Input
            id="end_year"
            value={filter.end_year || ""}
            placeholder="Ano final"
            onChange={handleFilter}
          />
        </div>
        <div className={styles.input}>
          <Button text="Pesquisar" onClick={fetchCountryData} />
        </div>
        {countryData.length ? (
          <Table data={countryData} columns={columns} />
        ) : null}
      </div>
    </main>
  );
}

export default isAuth(Country);
