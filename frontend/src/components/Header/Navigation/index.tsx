"use client";

import Link from "next/link";
import styles from "./navigation.module.css";
import { usePathname } from "next/navigation";

export interface NavLink {
  name: string;
  href: string;
}

interface NavigationProps {
  navLinks: Array<NavLink>;
}

interface NavItemProps {
  navLink: NavLink;
}

export default function Navigation({ navLinks }: NavigationProps) {
  return (
    <>
      {navLinks.map((link) => (
        <NavItem key={link.href} navLink={link} />
      ))}
    </>
  );
}

function NavItem({ navLink }: NavItemProps) {
  const pathname = usePathname();
  const isActive = pathname === navLink.href;

  return (
    <Link
      className={isActive ? styles.active : styles.default}
      href={navLink.href}
    >
      <p>{navLink.name}</p>
    </Link>
  );
}
