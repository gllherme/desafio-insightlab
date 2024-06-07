import Navigation from "./Navigation";
import styles from "./header.module.css";

const navLinks = [
  {
    name: "Home",
    href: "/",
  },
  {
    name: "Indicadores",
    href: "/country",
  },
];

export default function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.text}>Desafio Insight Lab</div>
      <Navigation navLinks={navLinks} />
    </header>
  );
}
