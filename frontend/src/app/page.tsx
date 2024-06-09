"use client";

import api from "@/api/api";
import Select from "@/components/Select";
import TagSlot from "@/components/TagSlot";
import isAuth from "@/components/isAuth";
import { ChangeEvent, useEffect, useState } from "react";
import styles from "./page.module.css";

function Home() {
  const token = localStorage.getItem("accessToken");
  const [options, setOptions] = useState([]);
  const [countryProfile, setCountryProfile] = useState<any>({});

  const fetchSuggestions = async () => {
    try {
      const { data } = await api.get("/country/codes", {
        headers: { Authorization: "Bearer " + token },
      });
      const newOptions = data.map((option: any) => ({
        id: option.code,
        name: option.name,
      }));
      setOptions(newOptions);
    } catch (e) {
      setOptions([]);
    }
  };

  const fetchProfile = async (e: ChangeEvent<HTMLSelectElement>) => {
    const id = e.target.options[e.target.selectedIndex].id;

    try {
      const { data } = await api.get("/country/profile/" + id, {
        headers: { Authorization: "Bearer " + token },
      });
      setCountryProfile(data);
    } catch (e) {
      setCountryProfile({});
    }
  };

  useEffect(() => {
    fetchSuggestions();
  }, []);

  return (
    <main className={styles.main}>
      <div className={styles.wrapper}>
        <Select options={options} onChange={fetchProfile} />
        <div className={styles.card}>
          <section>
            <h3>
              {countryProfile.name || ""} ({countryProfile.code || ""}) -{" "}
              {countryProfile.region || ""}
            </h3>
            <div>
              Area Territorial: {countryProfile.area?.toLocaleString() || ""}{" "}
              km²
            </div>
          </section>
          <section>
            <h4>Linguas</h4>
            <TagSlot tags={countryProfile.languages || []} />
          </section>
          <section>
            <h4>Moedas</h4>
            <TagSlot tags={countryProfile.currencies || []} />
          </section>

          <h4>Historico:</h4>
          <textarea
            className={styles.textarea}
            value={countryProfile.text || ""}
            readOnly
          />
        </div>
      </div>
    </main>
  );
}

export default isAuth(Home);
