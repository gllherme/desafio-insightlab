"use client";

import LoginForm from "@/components/LoginForm";
import RegisterForm from "@/components/RegisterForm";
import { ReactNode, createContext, useContext, useState } from "react";
import styles from "./page.module.css";

const TabContext = createContext<any>({});

interface IChildren {
  children: ReactNode;
}

interface TabProps extends IChildren {
  id: string;
}

function Tab({ id, children }: TabProps) {
  const [activeTab, setActiveTab] = useContext(TabContext);
  const isActive = id === activeTab;
  return (
    <button
      className={isActive ? styles.active : ""}
      onClick={() => setActiveTab(id)}
    >
      {children}
    </button>
  );
}

interface TabPanelProps extends IChildren {
  whenActive: string;
}

function TabPanel({ whenActive, children }: TabPanelProps) {
  const [activeTab] = useContext(TabContext);
  const isActive = whenActive === activeTab;

  return <div>{isActive ? children : null}</div>;
}

interface TabSwitcherProps extends IChildren {}

function TabSwitcher({ children }: TabSwitcherProps) {
  const [activeTab, setActiveTab] = useState("login");

  return (
    <TabContext.Provider value={[activeTab, setActiveTab]}>
      {children}
    </TabContext.Provider>
  );
}

export default function Auth() {
  return (
    <main className={styles.main}>
      <TabSwitcher>
        <div>
          <section className={styles.wrapper}>
            <Tab id="login">Login</Tab>
            <Tab id="register">Registrar</Tab>
          </section>

          <TabPanel whenActive="login">
            <LoginForm />
          </TabPanel>
          <TabPanel whenActive="register">
            <RegisterForm />
          </TabPanel>
        </div>
      </TabSwitcher>
    </main>
  );
}
