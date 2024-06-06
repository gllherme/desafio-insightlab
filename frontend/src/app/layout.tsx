import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Header from "@/components/Header";
import { raleway } from "./ui/fonts";
import { parseClassName } from "@/utils/helpers";

export const metadata: Metadata = {
  title: "Desafio Insight Lab",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={raleway.className}>
        <Header />
        {children}
      </body>
    </html>
  );
}
