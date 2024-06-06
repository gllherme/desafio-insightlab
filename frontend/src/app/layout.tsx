import Header from "@/components/Header";
import type { Metadata } from "next";
import "./globals.css";
import { raleway } from "./ui/fonts";

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
