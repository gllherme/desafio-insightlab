"use client";

import Autocomplete from "@/components/Autocomplete";
import TagSlot from "@/components/TagSlot";
import isAuth from "@/components/isAuth";
import { mock } from "./mock/mock";
import styles from "./page.module.css";

function Home() {
  return (
    <main className={styles.main}>
      <div className={styles.wrapper}>
        <Autocomplete suggestions={[]} />
        <div className={styles.card}>
          <section>
            <h3>
              {mock.name} ({mock.code}) - {mock.region}
            </h3>
            <div>Area Territorial: {mock.area.toLocaleString()} km²</div>
          </section>
          <section>
            <h4>Linguas</h4>
            <TagSlot tags={mock.languages} />
          </section>
          <section>
            <h4>Moedas</h4>
            <TagSlot tags={mock.currencies} />
          </section>

          <h4>Historico:</h4>
          <textarea className={styles.textarea} readOnly>
            {mock.text}
          </textarea>
        </div>
      </div>
    </main>
  );
}

export default isAuth(Home);
